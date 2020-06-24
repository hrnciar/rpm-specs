%global selinux_types %(%{__awk} '/^#[[:space:]]*SELINUXTYPE=/,/^[^#]/ { if ($3 == "-") printf "%s ", $2 }' /etc/selinux/config 2>/dev/null)
%global selinux_variants %([ -z "%{selinux_types}" ] && echo mls targeted || echo %{selinux_types})

Name:             radicale
Version:          2.1.12
Release:          2%{?dist}
Summary:          A simple CalDAV (calendar) and CardDAV (contact) server
License:          GPLv3+
URL:              https://radicale.org
Source0:          https://github.com/Kozea/Radicale/archive/%{version}/%{name}-%{version}.tar.gz
Source1:          %{name}.service
Source2:          %{name}-logrotate
Source3:          %{name}-httpd
Source4:          %{name}.te
Source5:          %{name}.fc
Source6:          %{name}.if
Source7:          %{name}-tmpfiles.conf

BuildArch:        noarch
BuildRequires:    python3-devel
BuildRequires:    python3-setuptools
BuildRequires:    systemd
BuildRequires:    checkpolicy
BuildRequires:    selinux-policy-devel
BuildRequires:    hardlink

Requires:         python3-%{name} = %{version}-%{release}
Requires(pre):    shadow-utils
%{?systemd_requires}
%if "%{_selinux_policy_version}" != ""
Requires:         selinux-policy >= %{_selinux_policy_version}
%endif
Requires(post):   /usr/sbin/semodule
Requires(post):   /usr/sbin/fixfiles
Requires(post):   /usr/sbin/restorecon
%if 0%{?rhel}
Requires(post):   policycoreutils-python
%else
Requires(post):   policycoreutils-python-utils
%endif
Requires(postun): /usr/sbin/semodule
Requires(postun): /usr/sbin/fixfiles
Requires(postun): /usr/sbin/restorecon
%if 0%{?rhel}
Requires(postun): policycoreutils-python
%else
Requires(postun): policycoreutils-python-utils
%endif

%description
The Radicale Project is a CalDAV (calendar) and CardDAV (contact) server. It
aims to be a light solution, easy to use, easy to install, easy to configure.
As a consequence, it requires few software dependencies and is pre-configured
to work out-of-the-box.

The Radicale Project runs on most of the UNIX-like platforms (Linux, BSD,
MacOS X) and Windows. It is known to work with Evolution, Lightning, iPhone
and Android clients. It is free and open-source software, released under GPL
version 3.

%package -n python3-%{name}
Summary:          A simple CalDAV (calendar) and CardDAV (contact) server
Recommends:       python3-bcrypt
Recommends:       python3-passlib
%{?python_provide:%python_provide python3-%{name}}
Obsoletes:        python-%{name} < %{version}-%{release}

%description -n python3-%{name}
The Radicale Project is a CalDAV (calendar) and CardDAV (contact) server. It
aims to be a light solution, easy to use, easy to install, easy to configure.
As a consequence, it requires few software dependencies and is pre-configured
to work out-of-the-box.

The Radicale Project runs on most of the UNIX-like platforms (Linux, BSD,
MacOS X) and Windows. It is known to work with Evolution, Lightning, iPhone
and Android clients. It is free and open-source software, released under GPL
version 3.

%package httpd
Summary:        httpd config for Radicale
Requires:       %{name} = %{version}-%{release}
Requires:       httpd
Requires:       python3-mod_wsgi

%description httpd
httpd example config for Radicale (Python3).

%prep
%autosetup -n Radicale-%{version}
mkdir SELinux
cp -p %{SOURCE4} %{SOURCE5} %{SOURCE6} SELinux

%build
%py3_build
cd SELinux
for selinuxvariant in %{selinux_variants}
do
    make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile
    mv %{name}.pp %{name}.pp.${selinuxvariant}
    make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile clean
done
cd -

%install
%py3_install

# Install configuration files
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/
install -p -m 640 config %{buildroot}%{_sysconfdir}/%{name}/
install -p -m 644 logging %{buildroot}%{_sysconfdir}/%{name}/
install -p -m 644 rights %{buildroot}%{_sysconfdir}/%{name}/

# Install wsgi file
mkdir -p %{buildroot}%{_datadir}/%{name}
sed -i 's|^#!/usr/bin/env python3$|#!/usr/bin/python3|' radicale.wsgi
sed -i 's|^#!/usr/bin/env python3$|#!/usr/bin/python3|' radicale.fcgi
install -p -m 755 radicale.wsgi %{buildroot}%{_datadir}/%{name}/
install -p -m 755 radicale.fcgi %{buildroot}%{_datadir}/%{name}/

# Install apache's configuration file
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d/
install -p -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf

# Create folder where the calendar will be stored
mkdir -p  %{buildroot}%{_sharedstatedir}/%{name}/

install -D -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -D -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -D -p -m 644 %{SOURCE7} %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}%{_localstatedir}/run/%{name}

mkdir -p %{buildroot}%{_localstatedir}/log/%{name}

for selinuxvariant in %{selinux_variants}
do
    install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
    install -p -m 644 SELinux/%{name}.pp.${selinuxvariant} \
        %{buildroot}%{_datadir}/selinux/${selinuxvariant}/%{name}.pp
done

%if 0%{?rhel}
/usr/sbin/hardlink -cv %{buildroot}%{_datadir}/selinux
%else
/usr/bin/hardlink -cv %{buildroot}%{_datadir}/selinux
%endif

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
    useradd -r -g %{name} -d %{_sharedstatedir}/%{name} -s /sbin/nologin \
    -c "Radicale service account" %{name}
exit 0

%post
%systemd_post %{name}.service
for selinuxvariant in %{selinux_variants}
do
  /usr/sbin/semodule -s ${selinuxvariant} -i \
    %{_datadir}/selinux/${selinuxvariant}/%{name}.pp &> /dev/null || :
done
# http://danwalsh.livejournal.com/10607.html
semanage port -a -t radicale_port_t -p tcp 5232 &> /dev/null || :
/usr/sbin/fixfiles -R %{name} restore &> /dev/null || :
/usr/sbin/fixfiles -R %{name}-httpd restore &> /dev/null || :
/usr/sbin/fixfiles -R %{name}-httpd-python2 restore &> /dev/null || :
/usr/sbin/restorecon -R %{_localstatedir}/log/%{name} &> /dev/null || :

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service 
if [ $1 -eq 0 ] ; then
  semanage port -d -p tcp 5232 &> /dev/null || :
  for selinuxvariant in %{selinux_variants}
  do
    /usr/sbin/semodule -s ${selinuxvariant} -r %{name} &> /dev/null || :
  done
  /usr/sbin/restorecon -R %{_localstatedir}/log/%{name} &> /dev/null || :
fi

%files
%doc README.md NEWS.md
%doc SELinux/*
%{_bindir}/%{name}
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %attr(0640, root, %{name}) %{_sysconfdir}/%{name}/config
%config(noreplace) %{_sysconfdir}/%{name}/logging
%config(noreplace) %{_sysconfdir}/%{name}/rights
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%dir %attr(750, %{name}, %{name}) %{_localstatedir}/log/%{name}
%dir %attr(750, %{name}, %{name}) %{_sharedstatedir}/%{name}/
%dir %{_datadir}/%{name}
%dir %attr(755, %{name}, %{name}) %{_localstatedir}/run/%{name}
%{_datadir}/selinux/*/%{name}.pp

%files -n python3-%{name}
%license COPYING
%{python3_sitelib}/%{name}
%{python3_sitelib}/Radicale-*.egg-info

%files httpd
%{_datadir}/%{name}/%{name}.wsgi
%{_datadir}/%{name}/%{name}.fcgi
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.12-2
- Rebuilt for Python 3.9

* Tue May 19 2020 Juan Orti Alcaine <jortialc@redhat.com> - 2.1.12-1
- Version 2.1.12

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 12 2020 Juan Orti Alcaine <jortialc@redhat.com> - 2.1.11-2
- Fix hardlink path on epel

* Sun Jan 05 2020 Juan Orti Alcaine <jortialc@redhat.com> - 2.1.11-1
- Version 2.1.11

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.10-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 26 2019 Juan Orti Alcaine <jortialc@redhat.com> - 2.1.10-6
- Use autogenerated python dependencies

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.10-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.10-3
- hardlink moved to /usr/bin

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 10 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.10-1
- Version 2.1.10

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.9-4
- Rebuilt for Python 3.7

* Thu May 31 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.9-3
- Add versioned dependencies

* Wed May 23 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.9-2
- Recommends: python3-bcrypt, python3-passlib

* Wed May 16 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.9-1
- Version 2.1.9

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.8-3
- SELinux rule to allow connection to POP port

* Sun Oct 08 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.8-2
- Run in daemon mode so it creates the PID file

* Mon Sep 25 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.8-1
- Version 2.1.8

* Wed Sep 20 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.7-1
- Version 2.1.7

* Tue Sep 12 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.6-2
- Upload 2.1.6 sources

* Tue Sep 12 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.6-1
- Version 2.1.6

* Sun Aug 27 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.5-1
- Version 2.1.5

* Mon Aug 07 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.4-1
- Version 2.1.4

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.2-1
- Version 2.1.2

* Sat Jul 01 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.1-1
- Version 2.1.1

* Fri Jun 30 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.0-3
- Update SELinux policy

* Fri Jun 30 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.0-2
- Remove PrivateDevices=true (RHBZ#1452328)

* Sun Jun 25 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.1.0-1
- Version 2.1.0

* Sun May 28 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.0.0-1
- Version 2.0.0

* Wed May 03 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.0.0rc2-2
- Run in foreground

* Wed May 03 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 2.0.0rc2-1
- Version 2.0.0rc2
- Drop python2 support

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-10
- Rebuild for Python 3.6

* Fri Dec 09 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.1-9
- Allow radicale_t to execute bin_t in SELinux policy RHBZ#1393569

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jul 01 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.1-7
- Additional systemd hardening

* Fri Jun 24 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.1-6
- Correctly label the files

* Wed Jun 22 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.1-5
- Add /var/run/radicale directory

* Tue Jun 21 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.1-4
- Update dependencies

* Tue Jun 21 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.1-3
- Create python2 subpackage

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1 (#1296746)

* Fri Jan 01 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1-1
- Version 1.1

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Nov 05 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.0.1-3
- Fix radicale-httpd for python3

* Thu Sep 24 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.0.1-2
- Unify spec for Fedora and epel7

* Tue Sep 22 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.0.1-1
- Version 1.0.1

* Tue Sep 15 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.0-1
- Version 1.0
- Merge SELinux subpackage into the main package

* Mon Sep 07 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.10-7
- Drop old _selinux_policy_version hack
- Require radicale-selinux

* Fri Jul 24 2015 Tomas Radej <tradej@redhat.com> - 0.10-6
- Updated dep on policycoreutils-python-utils

* Wed Jun 17 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.10-5
- Switch to python3

* Thu Apr 09 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.10-4
- Use license macro

* Mon Apr 06 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.10-3
- Add patch1 to fix rhbz#1206813

* Tue Feb 24 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.10-2
- Add radicale_var_run_t to SELinux policy 1.0.3

* Tue Jan 13 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.10-1
- Version 0.10

* Mon Aug 18 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.9-2
- Hide error when re-adding SELinux port label.

* Thu Aug 14 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.9-1
- Version 0.9
- Automatically restart service if it dies.
- Update systemwide patch

* Mon Aug 04 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-11
- Handle PID file.

* Thu Jul 17 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-10
- Add network-online.target dependency. Bug #1119818

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 29 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-8
- Add PrivateDevices to unit file

* Wed Dec 25 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-7
- SELinux policy 1.0.2

* Fri Nov 29 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-6
- SELinux policy 1.0.1 fix bug #1035925

* Fri Nov 08 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-5
- Hardcode _selinux_policy_version in F20 because of #999584

* Thu Oct 03 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-4
- Update httpd config file and add SELinux policy. Bug #1014408

* Tue Aug 27 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-3
- Move .wsgi and .fcgi to main package

* Sun Jul 21 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-2
- BuildRequire python2-devel

* Thu Jul 18 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.8-1
- Update to version 0.8
- Merge Till Maas's spec file. Bug #922276

* Mon Jul 08 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 0.7.1-1
- Initial packaging
