Name:           taskd
Version:        1.1.0
Release:        11%{?dist}
Summary:        Secure server providing multi-user, multi-client access to task data
License:        MIT
URL:            http://tasktools.org/projects/taskd.html
Source0:        http://taskwarrior.org/download/%{name}-%{version}.tar.gz
Source1:        taskd.service
Source2:        taskd-config
Source3:        taskd.xml
Source4:        README.Fedora

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  libuuid-devel
BuildRequires:  gnutls-devel
BuildRequires:  shadow-utils


%if 0%{?rhel} && 0%{?rhel} <= 6
# On rhel, we don't need systemd to build.  but we do on fedora.
# ...just to define some macros
%else
BuildRequires:  systemd
%endif

# For certificate generation
Requires:       gnutls-utils

# Systemd requires
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd

%description
The Taskserver is a lightweight, secure server providing multi-user,
multi-client access to task data.  This allows true syncing between desktop and
mobile clients.

Users want task list access from multiple devices running software of differing
sophistication levels to synchronize data seamlessly.  Synchronization requires
the ability to exchange transactions between devices that may not have
continuous connectivity, and may not have feature parity.

The Taskserver provides this and builds a framework to go several steps beyond
merely synchronizing data.

%prep
%setup -q %{name}-%{version}

cp -a %{SOURCE4} .


%build
%cmake
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_sharedstatedir}/taskd/

# Users will keep their keys here, but we copy some helpful scripts too.
mkdir -p %{buildroot}%{_sysconfdir}/pki/taskd/
cp -a pki/generate* %{buildroot}%{_sysconfdir}/pki/taskd/.
cp -a pki/vars %{buildroot}%{_sysconfdir}/pki/taskd/.
cp -a pki/README %{buildroot}%{_sysconfdir}/pki/taskd/.

mkdir -p %{buildroot}%{_localstatedir}/log/taskd/

%if 0%{?rhel} && 0%{?rhel} <= 6
# EL6 and earlier needs a sysvinit script
# Also, no firewalld on old EL
%else
mkdir -p %{buildroot}%{_unitdir}/
cp -a %{SOURCE1} %{buildroot}%{_unitdir}/taskd.service

mkdir -p %{buildroot}%{_prefix}/lib/firewalld/services
cp -a %{SOURCE3} %{buildroot}%{_prefix}/lib/firewalld/services/taskd.xml
%endif

mkdir -p %{buildroot}%{_sharedstatedir}/taskd/orgs/
cp -a %{SOURCE2} %{buildroot}%{_sharedstatedir}/taskd/config

rm -r %{buildroot}%{_datadir}/doc/taskd/

%pre
getent group taskd >/dev/null || groupadd -r taskd
getent passwd taskd >/dev/null || \
    useradd -r -g taskd -d %{_sharedstatedir}/taskd/ -s /usr/bin/sh \
    -c "Task Server system user" taskd
exit 0

# Systemd scriptlets
%if 0%{?rhel} && 0%{?rhel} <= 6
# No systemd for el6
%else

%post
%systemd_post taskd.service

%preun
%systemd_preun taskd.service

%postun
%systemd_postun_with_restart taskd.service

%endif


%files
%doc AUTHORS COPYING ChangeLog NEWS README README.Fedora
%{_bindir}/taskd
%{_bindir}/taskdctl
%{_mandir}/man1/taskd.1.*
%{_mandir}/man1/taskdctl.1.*
%{_mandir}/man5/taskdrc.5.*

%{_sysconfdir}/pki/taskd/generate*
%{_sysconfdir}/pki/taskd/vars
%{_sysconfdir}/pki/taskd/README

%dir %attr(0750, taskd, taskd) %{_sysconfdir}/pki/taskd/
%dir %attr(0750, taskd, taskd) %{_localstatedir}/log/taskd/

%dir %attr(0750, taskd, taskd) %{_sharedstatedir}/taskd/
%config(noreplace) %attr(0644, taskd, taskd) %{_sharedstatedir}/taskd/config
%dir %attr(0750, taskd, taskd) %{_sharedstatedir}/taskd/orgs/

%if 0%{?rhel} && 0%{?rhel} <= 6
# No sysvinit files for el6
%else
%{_unitdir}/taskd.service
%{_prefix}/lib/firewalld/services/taskd.xml
%endif

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Ralph Bean <rbean@redhat.com> - 1.1.0-2
- Add pki/vars fixing https://bugzilla.redhat.com/show_bug.cgi?id=1232832

* Thu May 14 2015 Ralph Bean <rbean@redhat.com> - 1.1.0-1
- Latest upstream.

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.0-11
- Rebuilt for GCC 5 C++11 ABI change

* Wed Aug 27 2014 Ralph Bean <rbean@redhat.com> - 1.0.0-10
- Add a README.Fedora with setup instructions.

* Thu Aug 21 2014 Ralph Bean <rbean@redhat.com> - 1.0.0-9
- Adjust config to point at /var/log/taskd/taskd.log

* Wed Aug 20 2014 Ralph Bean <rbean@redhat.com> - 1.0.0-8
- Adjust location of firewalld file to match others.
- Change port in the firewalld file to match taskd config.

* Wed Aug 20 2014 Ralph Bean <rbean@redhat.com> - 1.0.0-7
- Allow login as the taskd user.

* Sat Aug 16 2014 Ralph Bean <rbean@redhat.com> - 1.0.0-6
- Specify HOMEDIR when creating taskd user.
- Add firewalld service definition for taskd for el7 and fedora.

* Thu Feb 27 2014 Ralph Bean <rbean@redhat.com> - 1.0.0-5
- Add ?dist to Release.
- Replace __mkdir_p macro with just mkdir -p
- Use "-a" with cp to preserve timestamp.
- Add requirement on gnutls-utils
- Improve creation of taskd user and group.
- Add systemd scriptlets.
- Update permissions on files and dirs.

* Tue Feb 18 2014 Ralph Bean <rbean@redhat.com> - 1.0.0-4
- Sorting out permissions on /var/lib, /var/log, and /etc/pki/taskd

* Mon Feb 17 2014 Ralph Bean <rbean@redhat.com> - 1.0.0-3
- Included default config and pki tools.

* Mon Feb 17 2014 Ralph Bean <rbean@redhat.com> - 1.0.0-2
- Remove duplicate docs.

* Mon Feb 17 2014 Ralph Bean <rbean@redhat.com> - 1.0.0-1
- Initial packaging for COPR.
