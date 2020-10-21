%undefine __cmake_in_source_build
%global debug_package %{nil}

Name: range-v3
Summary: Experimental range library for C++11/14/17
Version: 0.11.0
Release: 1%{?dist}

License: Boost
URL: https://github.com/ericniebler/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# https://github.com/ericniebler/range-v3/pull/1549
Patch100: %{name}-fix-installation.patch

BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -p1
sed -e '/-Werror/d' -i cmake/ranges_flags.cmake

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DRANGE_V3_TESTS:BOOL=OFF \
    -DRANGE_V3_DOCS:BOOL=OFF \
    -DRANGE_V3_EXAMPLES:BOOL=OFF \
    -DRANGES_MODULES:BOOL=OFF
%cmake_build

%install
%cmake_install
rm -f %{buildroot}%{_includedir}/module.modulemap

%check
%ctest

%files devel
%doc README.md CREDITS.md TODO.md
%license LICENSE.txt
%{_includedir}/{meta,range,concepts,std}
%{_libdir}/cmake/%{name}

%changelog
* Thu Aug 13 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.11.0-1
- Updated to version 0.11.0.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.10.0-1
- Updated to version 0.10.0.

* Wed Oct 02 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0.9.1-1
- Updated to version 0.9.1.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.0-1
- Updated to version 0.5.0.

* Mon Feb 04 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.0-3
- Fixed FTBFS on Fedora 30.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 05 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.0-1
- Updated to version 0.4.0.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.6-1
- Updated to version 0.3.6.

* Thu Mar 08 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.5-2
- Fixed bogus changelog entry.

* Thu Mar 08 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.5-1
- Updated to version 0.3.5.

* Fri Dec 01 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.0-1.20171112git0b0dd88
- Initial SPEC release.
