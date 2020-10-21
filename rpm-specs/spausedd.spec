%bcond_without vmguestlib

Name: spausedd
Summary: Utility to detect and log scheduler pause
Version: 20200323
Release: 4%{?dist}
License: ISC
URL: https://github.com/jfriesse/spausedd
Source0: https://github.com/jfriesse/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

# VMGuestLib exists only for x86 architectures (for Fedora) and x86_64 (for RHEL)
%if %{with vmguestlib}
%if 0%{?rhel} >= 6
%ifarch x86_64
%global use_vmguestlib 1
%endif
%else
%ifarch %{ix86} x86_64
%global use_vmguestlib 1
%endif
%endif
%endif

BuildRequires: gcc
%{?systemd_requires}
BuildRequires: systemd

%if %{defined use_vmguestlib}
BuildRequires: pkgconfig(vmguestlib)
%endif

%description
Utility to detect and log scheduler pause

%prep
%setup -q -n %{name}-%{version}

%build
%set_build_flags
%make_build \
%if %{defined use_vmguestlib}
    WITH_VMGUESTLIB=1 \
%else
    WITH_VMGUESTLIB=0 \
%endif

%install
%make_install PREFIX="%{_prefix}"

mkdir -p %{buildroot}/%{_unitdir}
install -m 644 -p init/%{name}.service %{buildroot}/%{_unitdir}

%clean

%files
%doc AUTHORS
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man8/*
%{_unitdir}/spausedd.service

%post
%systemd_post spausedd.service

%preun
%systemd_preun spausedd.service

%postun
%systemd_postun spausedd.service

%changelog
* Tue Sep 22 2020 Jan Friesse <jfriesse@redhat.com> - 20200323-4
- Fix build for ELN

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200323-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Jan Friesse <jfriesse@redhat.com> - 20200323-2
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Mon Mar 23 2020 Jan Friesse <jfriesse@redhat.com> - 20200323-1
- Enhance man page
- Add CI tests
- Enable gating
- Rebase to new version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20190807-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 07 2019 Jan Friesse <jfriesse@redhat.com> - 20190807-1
- Enhance makefile
- Rebase to new version

* Tue Aug 06 2019 Jan Friesse <jfriesse@redhat.com> - 20190320-3
- Do not set exec permission for service file

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20190320-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 20 2019 Jan Friesse <jfriesse@redhat.com> - 20190320-1
- Use license macro in spec file

* Tue Mar 19 2019 Jan Friesse <jfriesse@redhat.com> - 20190319-1
- Add AUTHORS and COPYING
- Fix version number in specfile
- Use install -p to preserve timestamps
- Use set_build_flags macro
- Rebase to new version

* Mon Mar 18 2019 Jan Friesse <jfriesse@redhat.com> - 20190318-2
- Initial version for Fedora

* Mon Mar 18 2019 Jan Friesse <jfriesse@redhat.com> - 20190318-1
- Require VMGuestLib only on x86 and x86_64

* Wed Mar 21 2018 Jan Friesse <jfriesse@redhat.com> - 20180321-1
- Remove exlusivearch for VMGuestLib.
- Add copr branch with enhanced spec file which tries to automatically
  detect what build options should be used (systemd/vmguestlib).

* Tue Mar 20 2018 Jan Friesse <jfriesse@redhat.com> - 20180320-1
- Add support for VMGuestLib
- Add more examples

* Mon Feb 19 2018 Jan Friesse <jfriesse@redhat.com> - 20180219-1
- Add support for steal time

* Fri Feb 9 2018 Jan Friesse <jfriesse@redhat.com> - 20180209-1
- Initial version
