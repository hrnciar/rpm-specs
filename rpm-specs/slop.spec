Name:       slop
Version:    7.4
Release:    11%{?dist}
Summary:    Command line tool to perform region SeLect OPeration with mouse
URL:        https://github.com/naelstrof/slop

License:    GPLv3
Source0:    https://github.com/naelstrof/slop/archive/v%{version}/%{name}-%{version}.tar.gz

%if 0%{?fedora} && 0%{?fedora} >= 32
BuildRequires: libXext-devel
%endif
BuildRequires: gcc-c++ >= 4.9
BuildRequires: cmake
BuildRequires: glew-devel
BuildRequires: glm-devel
BuildRequires: libicu-devel
BuildRequires: libXrender-devel
BuildRequires: mesa-libEGL-devel

%description
slop (Select Operation) is an application that queries for a selection
from the user and prints the region to stdout.

%package -n libslopy
Summary: Library to perform region SeLect OPeration with mouse
%description -n libslopy
slop (Select Operation) is an application that queries for a selection
from the user and prints the region to stdout.

This sub-package contains libslopy library.

%package -n libslopy-devel
Summary: Library to perform region SeLect OPeration with mouse
Requires: %{name}%{?_isa} = %{version}-%{release}
%description -n libslopy-devel
slop (Select Operation) is an application that queries for a selection
from the user and prints the region to stdout.

This sub-package contains development files for libslopy library.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n libslopy

%check
%ctest

%files
%doc README.md
%license COPYING license.txt
%{_bindir}/slop
%{_mandir}/man1/slop.1.*

%files -n libslopy
%{_libdir}/libslopy.so.%{version}

%files -n libslopy-devel
%{_libdir}/libslopy.so
%{_includedir}/slop.hpp

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 15 2020 Pete Walter <pwalter@fedoraproject.org> - 7.4-10
- Rebuild for ICU 67

* Mon Mar 16 2020 Alois Mahdal <n9042e84@vornet.cz> - 7.4-9
- Fixed BZ#1800099; missing libXext build dependency

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 7.4-5
- Rebuild for ICU 63

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 7.4-4
- Rebuilt for glew 2.1.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 7.4-2
- Rebuild for ICU 62

* Thu Jun 28 2018 Alois Mahdal <n9042e84@vornet.cz> 7.4-1
- Initial packaging.
