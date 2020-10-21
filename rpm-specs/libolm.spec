%undefine __cmake_in_source_build
%global appname olm

Name: libolm
Version: 3.2.1
Release: 1%{?dist}

Summary: Double Ratchet cryptographic library
License: ASL 2.0
URL: https://gitlab.matrix.org/matrix-org/%{appname}
Source0: https://gitlab.matrix.org/matrix-org/%{appname}/-/archive/%{version}/%{appname}-%{version}.tar.bz2

BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3dist(cffi)
BuildRequires: python3dist(future)

%description
An implementation of the Double Ratchet cryptographic ratchet in C++.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%package python3
Summary: Python 3 bindings for %{name}
%{?python_provide:%python_provide python3-%{appname}}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%description python3
%{summary}.

%prep
%autosetup -n %{appname}-%{version} -p1
sed -e "s@/build@/%{_vpath_builddir}@g" -i python/olm_build.py

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DOLM_TESTS=ON
%cmake_build

pushd python
%py3_build
popd

%check
pushd %{_vpath_builddir}/tests
    ctest --output-on-failure
popd

%install
%cmake_install

pushd python
%py3_install
popd

%files
%license LICENSE
%doc *.md *.rst docs/*.md
%{_libdir}/%{name}.so.3*

%files devel
%{_includedir}/%{appname}
%{_libdir}/%{name}.so
%{_libdir}/cmake/Olm

%files python3
%{python3_sitearch}/%{appname}
%{python3_sitearch}/_%{name}.abi3.so
%{python3_sitearch}/python_%{appname}-*.egg-info

%changelog
* Wed Oct 14 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.1-1
- Updated to version 3.2.1.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.1.5-1
- Updated to version 3.1.5.

* Wed Jun 24 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.1.4-4
- Added python3-setuptools to build requirements.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.4-3
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 04 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 3.1.4-1
- Updated to version 3.1.4.
- Added Python 3 bindings.

* Tue Aug 06 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 3.1.3-1
- Updated to version 3.1.3.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 05 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 3.0.0-1
- Updated to version 3.0.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 10 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 2.2.2-1
- Initial SPEC release.
