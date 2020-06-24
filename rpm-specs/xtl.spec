# Header-only library.
%global debug_package %{nil}

Name:           xtl
Version:        0.6.13
Release:        1%{?dist}
License:        BSD
Summary:        QuantStack tools library
Url:            https://github.com/QuantStack/xtl
Source0:        https://github.com/QuantStack/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# https://github.com/QuantStack/xtl/issues/97
Patch0001:      0001-Fix-complex-test.patch

BuildRequires:  binutils
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  make
BuildRequires:  cmake(nlohmann_json)
BuildRequires:  python3dist(breathe)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description
Basic tools (containers, algorithms) used by other QuantStack packages.


%package devel
Summary:        %{summary}
Provides:       xtl-static = %{version}-%{release}
Requires:       cmake-filesystem

%description devel
Development files for %{name} library.


%package doc
Summary:        %{summary}

%description doc
Documentation files for %{name} library.


%prep
%autosetup -p1


%build
%cmake -DBUILD_TESTS=ON .
%make_build

pushd docs
make html SPHINXBUILD=sphinx-build-3
rm build/html/.buildinfo
popd


%install
%make_install


%check
make xtest


%files devel
%doc README.md
%license LICENSE
%{_includedir}/xtl/
%{_libdir}/cmake/xtl/
%{_libdir}/pkgconfig/xtl.pc

%files doc
%doc docs/build/html


%changelog
* Sat Mar 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.13-1
- Update to latest version

* Fri Feb 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.12-2
- Re-enable armv7hl and ppc64le

* Fri Feb 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.12-1
- Update to latest version

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.11-1
- Update to latest version

* Thu Oct 31 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.8-1
- Update to latest version

* Mon Sep 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.7-1
- Update to latest version

* Wed Sep 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.6-1
- Update to latest version

* Tue Aug 27 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.5-1
- Update to latest version
- Exclude arches that don't work

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.4-1
- Update to latest version

* Wed Apr 10 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.3-1
- Update to latest version

* Sat Apr 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.2-1
- Update to latest version

* Tue Mar 26 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.1-1
- Update to latest version

* Fri Mar 08 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.0-1
- Update to latest version

* Wed Feb 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.4-1
- Update to latest version

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.3-1
- Update to latest version

* Wed Sep 05 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.15-1
- Update to latest version

* Thu Aug 16 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.14-2
- rebuilt

* Tue Aug 14 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.14-1
- Update to latest version

* Tue Aug 07 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.13-1
- Update to latest version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 02 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.4.7-1
- Update to latest version

* Wed Mar 21 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.4.4-2
- Split documentation into subpackage
- Run more tests on broken arches

* Mon Mar 19 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.4.4-1
- Initial package for Fedora
