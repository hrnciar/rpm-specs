%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Summary:    Download Ticket Service
URL:        http://www.thregr.org/~wavexx/software/dl/
Name:       dl
Version:    0.17.1
Release:    9%{?dist}
License:    GPLv2+

Source0:    http://www.thregr.org/~wavexx/software/dl/releases/dl-%{version}.zip
Source1:    dl-httpd-conf
Source2:    README.fedora.dl

Patch0:     dl-0.12-fix-doc-file-dependency.patch

BuildArch:  noarch

Requires:   php >= 5.3
Requires:   php-mbstring
Requires:   php-openssl
Requires:   php-pdo
Requires:   sqlite
Requires:   webserver

# Unbundled libraries replaced by system libraries

Requires:   php-php-gettext

%if 0%{?rhel} || 0%{?fedora} < 23
Requires(post):     policycoreutils-python
Requires(postun):   policycoreutils-python
%else
Requires(post):     policycoreutils-python-utils
Requires(postun):   policycoreutils-python-utils
%endif

%description
dl is a file exchange service that allows you to upload any file to a web
server and generate a unique ticket for others to download. The ticket is
automatically expired according to the specified rules, so that you don't need
to keep track or cleanup afterward. dl also allows you to grant an anonymous,
one-time upload for others to send *you* a file, without the requirement of
account management.

dl is usually installed as a "email attachments replacement" due to its
simplicity (though can be used in other ways).

%prep
%setup -q

%patch0 -p1

%build
# Cleanup
rm -f client/thunderbird-filelink-dl/.gitignore
rm -f htdocs/include/.htaccess
rm -f htdocs/style/include/.htaccess

%install
# Application
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/dl
cp -pr htdocs/* ${RPM_BUILD_ROOT}%{_datadir}/dl/.

# Unbundle php-php-gettext
rm -rf ${RPM_BUILD_ROOT}%{_datadir}/dl/include/gettext
ln -sf /usr/share/php/gettext ${RPM_BUILD_ROOT}%{_datadir}/dl/include/gettext

# DL configuration
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/dl
cp -p htdocs/include/config.php.dist ${RPM_BUILD_ROOT}%{_sysconfdir}/dl/config.php
sed -i -e 's:dl.example.com:localhost/dl:g' ${RPM_BUILD_ROOT}%{_sysconfdir}/dl/config.php
ln -sf ../../../../etc/dl/config.php ${RPM_BUILD_ROOT}%{_datadir}/dl/include/config.php

# Apache configuration
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/httpd/conf.d
cp -p %{SOURCE1} ${RPM_BUILD_ROOT}%{_sysconfdir}/httpd/conf.d/dl.conf

# Storage
mkdir -p ${RPM_BUILD_ROOT}%{_localstatedir}/spool/dl
mkdir -p ${RPM_BUILD_ROOT}%{_localstatedir}/spool/dl/data

cp -p %{SOURCE2} ./README.fedora

%post
# selinux: allow PHP to read/write data directory
semanage fcontext -a -t httpd_sys_rw_content_t "%{_localstatedir}/spool/dl(/.*)?"
restorecon -R -v %{_localstatedir}/spool/dl > /dev/null

# create sqlite db if it doesn't already exist
if [ ! -f %{_localstatedir}/spool/dl/data.sdb ]; then
    su -c 'sqlite3 %{_localstatedir}/spool/dl/data.sdb' -s /bin/sh apache < %{_datadir}/dl/include/scripts/db/sqlite.sql
fi
:

%postun
# selinux: cleanup after uninstall
if [ $1 -eq 0 ]; then
    semanage fcontext -d -t httpd_sys_rw_content_t "%{_localstatedir}/spool/dl(/.*)?"
    restorecon -R -v %{_localstatedir}/spool/dl > /dev/null
fi
:

%files
%doc README.fedora
%doc COPYING.txt
%doc *.html
%doc *.rst
%doc client
%dir %{_sysconfdir}/dl
%config(noreplace) %{_sysconfdir}/dl/config.php
%config(noreplace) %{_sysconfdir}/httpd/conf.d/dl.conf
%{_datadir}/dl
%dir %attr(0700,apache,apache) %{_localstatedir}/spool/dl
%dir %attr(0755,apache,apache) %{_localstatedir}/spool/dl/data

%changelog
* Sat May 09 2020 Greg Bailey <gbailey@lxpro.com> - 0.17.1-9
- Revert unbundling of php-phpass (removed from repo) (#1832436)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 18 2016 Greg Bailey <gbailey@lxpro.com> - 0.17.1-1
- dl 0.17.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov  8 2015 Greg Bailey <gbailey@lxpro.com> - 0.17-2
- Use conditional macros for proper policycoreutils-python dependency

* Fri Nov  6 2015 Greg Bailey <gbailey@lxpro.com> - 0.17-1
- dl 0.17 (#1197397)

* Fri Jul 24 2015 Tomas Radej <tradej@redhat.com> - 0.13-5
- Updated dep on policycoreutils-python-utils

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug  1 2014 Greg Bailey <gbailey@lxpro.com> - 0.13-3
- Unbundle php-phpass and php-php-gettext

* Fri Aug  1 2014 Greg Bailey <gbailey@lxpro.com> - 0.13-2
- License is GPLv2+ according to AUTHORS.rst

* Thu Jul 31 2014 Greg Bailey <gbailey@lxpro.com> - 0.13-1
- dl 0.13

* Wed Jul 30 2014 Greg Bailey <gbailey@lxpro.com> - 0.12-2
- Patches to remove rpmlint errors/warnings

* Wed Jul 30 2014 Greg Bailey <gbailey@lxpro.com> - 0.12-1
- Initial RPM

