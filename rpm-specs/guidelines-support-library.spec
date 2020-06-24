Name: guidelines-support-library
Version: 3.1.0
Release: 2%{?dist}

License: MIT
URL: https://github.com/Microsoft/GSL
Summary: Guidelines Support Library
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

# https://github.com/microsoft/GSL/pull/893
Patch100: %{name}-fix-noarch.patch

%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n GSL-%{version} -p1
mkdir -p %{_target_platform}

%build
pushd %{_target_platform}
    %cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DGSL_TEST:BOOL=OFF \
    ..
popd
%ninja_build -C %{_target_platform}

%install
%ninja_install -C %{_target_platform}

%files devel
%doc README.md CONTRIBUTING.md
%license LICENSE ThirdPartyNotices.txt
%{_datadir}/cmake/Microsoft.GSL/
%{_includedir}/gsl/

%changelog
* Sat Jun 06 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.1.0-2
- Added patch with architecture independent fixes.

* Fri Jun 05 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.1.0-1
- Updated to version 3.1.0.

* Sat Apr 25 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.0.1-1
- Updated to version 3.0.1.

* Fri Apr 17 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.0.0-1
- Updated to version 3.0.0.

* Mon Feb 03 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2.1.0-1
- Updated to version 2.1.0.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0.0-1
- Updated to version 1.0.0.

* Thu Mar 08 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0-3.20180305gitc9e423d
- Updated to latest snapshot.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-2.20171014git1c95f94
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 28 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.20171014git1c95f94
- Initial SPEC release.
