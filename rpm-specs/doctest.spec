%undefine __cmake_in_source_build
%global debug_package %{nil}

Name: doctest
Version: 2.4.0
Release: 2%{?dist}
Summary: Feature-rich header-only C++ testing framework
License: MIT
URL: https://github.com/onqtam/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake

%description
A fast (both in compile times and runtime) C++ testing framework, with the
ability to write tests directly along production source (or in their own
source, if you prefer).

%package devel
Summary: Development files for %{name}
Provides: %{name}-static%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: libstdc++-devel%{?_isa}

%description devel
%{summary}.

%prep
%autosetup -p1

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DDOCTEST_WITH_MAIN_IN_STATIC_LIB:BOOL=OFF \
  -DDOCTEST_WITH_TESTS:BOOL=ON \
  %{nil}
%cmake_build

%check
%ctest

%install
%cmake_install

%files devel
%doc README.md CHANGELOG.md CONTRIBUTING.md
%license LICENSE.txt
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 28 2020 Nick Black <dankamongmen@gmail.com> - 2.4.0-1
- New upstream release

* Sun May 24 2020 Nick Black <dankamongmen@gmail.com> - 2.3.8-1
- New upstream release

* Thu Apr 30 2020 Nick Black <dankamongmen@gmail.com> - 2.3.7-1
- Initial RPM release
