# Post release snapshot of 3.1.4.
%global commit 283534d97d5a181b09960ae1f0c53dbbe42d8a90
%global shortcommit %(c=%{commit}; echo ${c:0:12})
%global snapinfo 20190113git%{shortcommit}

# We need to include this git submodule, mxml. :(
# It's written by the author of elog; it's _not_ the mxml in Fedora.
%global commit1 cb34fe499c80fcb80aa6e5a2ae7f2dbaf7e790e1
%global shortcommit1 %(c=%{commit1}; echo ${c:0:12})

Name:           elog
Version:        3.1.4
Release:        3.%{snapinfo}%{?dist}
Summary:        Logbook system to manage notes through a Web interface

License:        GPLv2 and GPLv3+
URL:            https://midas.psi.ch/elog/
Source0:        https://bitbucket.org/ritt/elog/get/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz

Source1:        elogd.service

# elog "mxml" library.
# Remove if we move away from bitbucket snapshot.
Source2:        https://bitbucket.org/tmidas/mxml/get/%{commit1}.tar.gz#/%{name}-mxml-%{shortcommit1}.tar.gz

# Patch for the makefile.
Patch0:         https://tc01.fedorapeople.org/elog/elog-makefile-elogdir.patch

BuildRequires:  gcc
BuildRequires:  glibc-devel, openssl-devel, systemd, ckeditor, dos2unix, glibc-common
BuildRequires:  krb5-devel, openldap-devel

# JavaScript that we're unbundling.
Requires:       ckeditor

# Require the subpackage.
Requires:       elog-client

Requires(pre):  shadow-utils

%description
ELOG is part of a family of applications known as weblogs. Their general
purpose is:

1. To make it easy for people to put information online in a chronological
fashion, in the form of short, time-stamped text messages ("entries") with
optional HTML markup for presentation, and optional file attachments
(images, archives, etc.)

2. To make it easy for other people to access this information through a
Web interface, browse entries, search, download files, and optionally add,
update, delete or comment on entries.

ELOG is a remarkable implementation of a weblog in at least two respects:

1. Its simplicity of use: you don't need to be a seasoned server operator
and/or an experimented database administrator to run ELOG ; one executable
file (under Unix or Windows), a simple configuration text file, and it works.
No Web server or relational database required. It is also easy to translate
the interface to the appropriate language for your users.

2. Its versatility: through its single configuration file, ELOG can be made
to display an infinity of variants of the weblog concept. There are options
for what to display, how to display it, what commands are available and to
whom, access control, etc. Moreover, a single server can host several
weblogs, and each weblog can be totally different from the rest.

%package client

Summary:        CLI client for the ELOG logbook system


%description client

This package contains only the "elog" client binary, for communicating
with an ELOG logbook. See the description of the "elog" package for more
information.

%package doc

Summary:        ELOG documentation
BuildArch:      noarch

%description doc

This package contains the documentation for the ELOG logbook server.
See the description of the "elog" package for more information.

%prep
%autosetup -n ritt-elog-%{shortcommit} -p1

# Various fixes; remove executable bits, remove bundled ckeditor.
rm -rf scripts/ckeditor

cd scripts && find . -type f -print0 | xargs -0 chmod a-x && cd ..
chmod a-x COPYING

#rm doc/index.html~
cd doc && find . -type f -print0 | xargs -0 chmod a-x && cd ..
dos2unix doc/strftime.txt
iconv -f latin1 -t utf-8 doc/strftime.txt > doc/strftime.txt.conv
mv -f doc/strftime.txt.conv doc/strftime.txt

# Fix some spurious executable permissions.
chmod -x src/elog.c
chmod -x src/regex.h
chmod -x src/regex.c
chmod -x src/elogd.c

# We need to drop source1 into the "mxml" directory.
# I'm sure this _could_ be done with a version of the setup macro...
tar xfz %SOURCE2 -C mxml --strip-components=1

%build
make %{?_smp_mflags} CFLAGS="%{optflags} -Imxml -DHAVE_SSL -DHAVE_KRB5 -DHAVE_LDAP" LIBS="%{__global_ldflags} -lssl -lkrb5 -lldap -llber"

%install
# This makefile needs a fair amount of massaging to do the right thing.
# Hence the above patch.
make install ROOT=%{buildroot} PREFIX=%{_prefix} MANDIR=%{buildroot}%{_mandir} ELOGDIR=%{buildroot}%{_datadir}/elog
rm %{buildroot}%{_initddir}/elogd

# Move the configuration file to the right place.
mv %{buildroot}%{_datadir}/elog/elogd.cfg %{buildroot}%{_sysconfdir}/

# Land the systemd initscript.
mkdir -p %{buildroot}%{_unitdir}
cp %SOURCE1 %{buildroot}%{_unitdir}

# Create the local state directory for logbooks.
mkdir -p %{buildroot}%{_localstatedir}/lib/elog/logbooks

# replace bundled ckeditor with a symlink.
ln -s %{_datadir}/ckeditor %{buildroot}%{_datadir}/elog/scripts/ckeditor

# Create elog user/group.
%pre
getent group elog > /dev/null || groupadd -r elog
getent passwd elog  > /dev/null || \
    useradd -r -g elog -d /usr/share/elog -s /sbin/nologin \
    -c "ELOG logbook daemon user" elog
exit 0

# Systemd snippets for elogd service file

%post
%systemd_post elogd.service

%preun
%systemd_preun elogd.service

%postun
%systemd_postun_with_restart elogd.service

%files
%{_bindir}/elconv
%{_sbindir}/elogd
%{_datadir}/elog/
%{_mandir}/man1/elconv.1*
%{_mandir}/man8/elogd.8*
%{_unitdir}/elogd.service

# The directory for a user's logbooks.
%dir %attr(-,elog,elog) %{_localstatedir}/lib/elog
%dir %attr(-,elog,elog) %{_localstatedir}/lib/elog/logbooks

# Configuration for elogd.
%config(noreplace) %{_sysconfdir}/elogd.cfg

%doc README
%license COPYING

%files client
%{_bindir}/elog
%{_mandir}/man1/elog.1*
%license COPYING

%files doc
%doc doc/

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-3.20190113git283534d97d5a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-2.20190113git283534d97d5a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Ben Rosser <rosser.bjr@gmail.com> - 3.1.4-1.20190113git283534d97d5a
- Update to post-release snapshot of 3.1.4.
- Fix several security issues.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1.3-6
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Ben Rosser <rosser.bjr@gmail.com> - 3.1.3-2
- Elog wasn't being built with SSL support, so explicitly enable it.
- Also enable Kerberos and LDAP support too.

* Thu May 25 2017 Ben Rosser <rosser.bjr@gmail.com> - 3.1.3-1
- Update to latest upstream release.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 22 2016 Ben Rosser <rosser.bjr@gmail.com> 3.1.2-1
- Update to latest upstream release.

* Tue Aug 30 2016 Ben Rosser <rosser.bjr@gmail.com> 3.1.1-7
- Apply patches to fix CVE-2016-6342.

* Tue Jul 19 2016 Ben Rosser <rosser.bjr@gmail.com> 3.1.1-6
- Add license to the elog-client subpackage
- Remove manual cleanup of the buildroot
- Created -doc subpackage for the documentation
- Added systemd snippets for elogd.service
- Changed _usr to _prefix when running make install.
- Manually set LIBS=%%{__global_ldflags} in order to pass LDFLAGS to the makefile
- Changed license tag to GPLv2 and GPLv3+

* Mon Jun 13 2016 Ben Rosser <rosser.bjr@gmail.com> 3.1.1-5
- Fix file-not-utf8 warning on doc/strftime.txt using iconv.
- Fix spurious executable permissions on some of the source files.

* Fri Jun 3 2016 Ben Rosser <rosser.bjr@gmail.com> 3.1.1-4
- Use attr to set ownership on /usr/share/elog.
- Fixed typo in systemd service file URL
- Revised package summaries.
- Moved elogs out of datadir and into /var/lib.

* Wed Jan 27 2016 Ben Rosser <rosser.bjr@gmail.com> 3.1.1-3
- Fixed ckeditor symlink.

* Wed Jan 27 2016 Ben Rosser <rosser.bjr@gmail.com> 3.1.1-2
- Broke elog binary off into -client subpackage.

* Thu Dec 10 2015 Ben Rosser <rosser.bjr@gmail.com> 3.1.1-1
- Updated to latest elog release.

* Wed Jul 8 2015 Ben Rosser <rosser.bjr@gmail.com> 3.1.0-3
- Removed bundled ckeditor, replaced with an absolute symlink
- Moved configuration file to /etc/elogd.cfg.
- Created elog user/group so that the script works successfully.

* Tue Jul 7 2015 Ben Rosser <rosser.bjr@gmail.com> 3.1.0-2
- Removed initscript, replaced it with a systemd service file.

* Tue Jul 7 2015 Ben Rosser <rosser.bjr@gmail.com> 3.1.0-1
- Created initial package.
- Applied a patch to the makefile to make everything work correctly.
