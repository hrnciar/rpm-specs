%bcond_without check

Name:           libnitrokey
Version:        3.5
Release:        2%{?dist}
Summary:        Communicate with Nitrokey stick devices in a clean and easy manner

License:        LGPLv3+
URL:            https://github.com/Nitrokey/libnitrokey
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/Nitrokey/libnitrokey/pull/165
Patch0001:      0001-meson-Bring-buildsystem-to-parity-with-CMake.patch

BuildRequires:  meson >= 0.44.0
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(hidapi-libusb)
BuildRequires:  pkgconfig(udev)
%if %{with check}
# For one of tests
BuildRequires:  gcc
BuildRequires:  pkgconfig(catch2)
%endif

%description
Libnitrokey is a project to communicate with Nitrokey Pro and Storage devices
in a clean and easy manner.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package contains development libraries and header files are needed
to develop using libnitrokey.

%prep
%autosetup -p1
# Remove catch
rm -vr unittest/Catch
# Remove hidapi
rm -vr hidapi libnitrokey/hidapi

%build
%meson \
  -Doffline-tests=%{?with_check:true}%{!?with_check:false} \
  %{nil}
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_libdir}/libnitrokey.so.*
%{_udevrulesdir}/*-nitrokey.rules

%files devel
%{_libdir}/libnitrokey.so
%{_libdir}/pkgconfig/libnitrokey-1.pc
%{_includedir}/libnitrokey/

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.5-1
- Update to 3.5

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Tom Hughes <tom@compton.nu> - 3.4.1-2
- Patch for changes in catch2 pkg-config module name

* Wed Jul 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.4.1-1
- Update to 3.4.1

* Tue Jul 17 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.4-1
- Update to 3.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Ed Marshall <esm@logic.net> - 3.3-1
- Update to 3.3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1-2
- Switch to %%ldconfig_scriptlets

* Tue Oct 17 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1-1
- Update to 3.1

* Sat Oct 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0-0.2.20171007git.fa871ec
- Update to latest snapshot

* Sat Oct 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0-0.1.20171007git.544f69c
- Initial package
