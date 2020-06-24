%global debug_package %{nil}

Name: range-v3
Summary: Experimental range library for C++11/14/17
Version: 0.10.0
Release: 2%{?dist}

License: Boost
URL: https://github.com/ericniebler/%{name}
Source0: %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
%autosetup
mkdir -p %{_target_platform}
sed -i 's@lib/@%{_lib}/@g' CMakeLists.txt
sed -i '/-Werror/d' cmake/ranges_flags.cmake

%build
pushd %{_target_platform}
    %cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DRANGE_V3_TESTS=OFF \
    -DRANGE_V3_DOCS=OFF \
    -DRANGE_V3_EXAMPLES=OFF \
    -DRANGES_MODULES=OFF \
    ..
popd
%ninja_build -C %{_target_platform}

%install
%ninja_install -C %{_target_platform}
rm -f %{buildroot}%{_includedir}/module.modulemap

%check
pushd %{_target_platform}
    ctest --output-on-failure
popd

%files devel
%doc README.md CREDITS.md TODO.md
%license LICENSE.txt
%{_includedir}/{meta,range,concepts,std}
%{_libdir}/cmake/%{name}

%changelog
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
