Name:		dhtest
Version:	1.5
Release:	5%{?snapinfo:.%{snapinfo}}%{?dist}
Summary:	A DHCP client simulation on linux

License:	GPLv2
URL:		https://github.com/saravana815/dhtest
Source0:	https://github.com/saravana815/dhtest/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:		dhtest-1.5-globals.patch
Patch2:		dhtest-1.5-strncpy.patch

BuildRequires:	gcc

%description
It can simulate multiple DHCP clients behind a network device.
It can help in testing the DHCP servers or in testing switch/router
by loading the device with multiple DHCP clients.

%prep
%autosetup -n %{name}-%{version} -p1
#sed -e 's,^#!/usr/bin/env python,#!/usr/bin/python,' -i dhscript.py

%build
%make_build CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"


%install
mkdir -p %{buildroot}%{_bindir}
%{__install} -m 0755 dhtest %{buildroot}%{_bindir}/dhtest

%check
# run dhscript.py here once it can run without special setup
# or dhcp server is configured

%files
%doc README.txt
%license LICENSE
%{_bindir}/dhtest

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 02 2020 Petr Menšík <pemensik@redhat.com> - 1.5-4
- Fix link errors (#1799278)
- Correct some strncpy usage errors

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 15 2019 Petr Menšík <pemensik@redhat.com> - 1.5-2
- Add license

* Thu Mar 15 2018 Petr Menšík <pemensik@redhat.com> - 1.5-1
- Initial package

