# The (empty) main package is arch, to have the package built and tests run
# on all arches, but the actual result package is the noarch -devel subpackge.
# Debuginfo packages are disabled to prevent rpmbuild from generating an empty
# debuginfo package for the empty main package.
%global debug_package %{nil}

Name:           cereal
Version:        1.3.0
Release:        2%{?dist}
Summary:        A header-only C++11 serialization library
License:        BSD
Url:            http://uscilab.github.io/cereal/
Source0:        https://github.com/USCiLab/cereal/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  cmake3 >= 3.0

%description
cereal is a header-only C++11 serialization library. cereal takes arbitrary
data types and reversibly turns them into different representations, such as
compact binary encodings, XML, or JSON. cereal was designed to be fast,
light-weight, and easy to extend - it has no external dependencies and can be
easily bundled with other code or used standalone.

%package devel
Summary:        Development headers and libraries for %{name}
BuildArch:      noarch

%description devel
cereal is a header-only C++11 serialization library. cereal takes arbitrary
data types and reversibly turns them into different representations, such as
compact binary encodings, XML, or JSON. cereal was designed to be fast,
light-weight, and easy to extend - it has no external dependencies and can be
easily bundled with other code or used standalone.

This package contains development headers and libraries for the cereal library

%prep
%setup -q

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake3} .. -DSKIP_PORTABILITY_TEST=ON -DWITH_WERROR=OFF
%make_build

%install
%make_install -C %{_target_platform}

%check
make -C %{_target_platform} test

%files devel
%doc README.md
%license LICENSE
%{_includedir}/%{name}
%dir %{_datadir}/cmake
%{_datadir}/cmake/%{name}

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 26 2019 Christoph Junghans <junghans@votca.org> - 1.3.0-1
- Version bump (bug #1765568)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 15 2017 Christoph Junghans <junghans@votca.org> - 1.2.2-1
- Update to v1.2.2 (bug #1422474) 

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Sep 03 2016 Christoph Junghans <junghans@votca.org> - 1.2.1-2
- Minor changes from review (bug #1372403)

* Thu Sep 01 2016 Christoph Junghans <junghans@votca.org> - 1.2.1-1
- First release.
