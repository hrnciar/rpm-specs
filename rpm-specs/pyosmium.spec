%global libosmium_version 2.15.0

Name:           pyosmium
Version:        3.0.0
Release:        2%{?dist}
Summary:        Python bindings for libosmium

License:        BSD
URL:            https://osmcode.org/pyosmium/
Source0:        https://github.com/osmcode/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# Disable stripping
Patch0:         pyosmium-no-strip.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx python3-sphinxcontrib-autoprogram
BuildRequires:  python3-nose
BuildRequires:  python3-mock
BuildRequires:  python3-shapely
BuildRequires:  pybind11-devel
BuildRequires:  boost-devel boost-python3-devel
BuildRequires:  libosmium-devel >= %{libosmium_version}
BuildRequires:  libosmium-static >= %{libosmium_version}

%description
Provides Python bindings for the Libosmium C++ library, a library
for working with OpenStreetMap data in a fast and flexible manner.


%package -n python3-osmium
Summary:        %{summary}
%{?python_provide:%python_provide python3-osmium}

%description -n python3-osmium
Provides Python bindings for the Libosmium C++ library, a library
for working with OpenStreetMap data in a fast and flexible manner.


%prep
%autosetup


%build
%set_build_flags
%py3_build
cd doc
make html SPHINXBUILD=sphinx-build-3


%install
%py3_install


%check
cd test
%{__python3} run_tests.py


%files -n python3-osmium
%doc README.md README.rst CHANGELOG.md doc/_build/html
%license LICENSE.TXT
%{python3_sitearch}/*
%{_bindir}/*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-2
- Rebuilt for Python 3.9

* Thu May  7 2020 Tom Hughes <tom@compton.nu> - 3.0.0-1
- Update to 3.0.0 upstream release

* Sun Mar  1 2020 Tom Hughes <tom@compton.nu> - 2.15.4-1
- Update to 2.15.4 upstream release

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.15.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.15.3-3
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.15.3-2
- Rebuilt for Python 3.8

* Fri Aug 16 2019 Tom Hughes <tom@compton.nu> - 2.15.3-1
- Update to 2.15.3 upstream release

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar  9 2019 Tom Hughes <tom@compton.nu> - 2.15.2-1
- Update to 2.15.2 upstream release

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 2.15.1-2
- Rebuilt for Boost 1.69

* Thu Jan 24 2019 Tom Hughes <tom@compton.nu> - 2.15.1-1
- Update to 2.15.1 upstream release

* Mon Dec 10 2018 Tom Hughes <tom@compton.nu> - 2.15.0-1
- Update to 2.15.0 upstream release

* Mon Nov 12 2018 Tom Hughes <tom@compton.nu> - 2.14.4-1
- Update to 2.14.4 upstream release

* Mon Oct  1 2018 Tom Hughes <tom@compton.nu> - 2.14.3-2
- Drop python2 subpackage

* Thu Aug  9 2018 Tom Hughes <tom@compton.nu> - 2.14.3-1
- Update to 2.14.3 upstream release

* Tue Aug  7 2018 Tom Hughes <tom@compton.nu> - 2.14.2-1
- Update to 2.14.2 upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.14.1-2
- Rebuilt for Python 3.7

* Fri Apr 27 2018 Tom Hughes <tom@compton.nu> - 2.14.1-1
- Update to 2.14.1 upstream release

* Sun Apr  1 2018 Tom Hughes <tom@compton.nu> - 2.14.0-1
- Update to 2.14.0 upstream release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 2.13.0-2
- Rebuilt for Boost 1.66

* Fri Sep  1 2017 Tom Hughes <tom@compton.nu> - 2.13.0-1
- Update to 2.13.0 upstream release

* Sun Aug 20 2017 Tom Hughes <tom@compton.nu> - 2.12.4-1
- Update to 2.12.4 upstream release

* Thu Aug 10 2017 Tom Hughes <tom@compton.nu> - 2.12.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 2.12.3-3
- Rebuilt for s390x binutils bug

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 2.12.3-2
- Rebuilt for Boost 1.64

* Thu May 25 2017 Tom Hughes <tom@compton.nu> - 2.12.3-1
- Update to 2.12.3 upstream release

* Fri May  5 2017 Tom Hughes <tom@compton.nu> - 2.12.2-1
- Update to 2.12.2 upstream release

* Tue Apr 11 2017 Tom Hughes <tom@compton.nu> - 2.12.0-2
- Rebuild against libosmium 2.12.1

* Sun Mar 19 2017 Tom Hughes <tom@compton.nu> - 2.12.0-1
- Update to 2.12.0 upstream release

* Tue Mar  7 2017 Tom Hughes <tom@compton.nu> - 2.11.0-2
- Rebuild against libosmium 2.12.0

* Fri Mar  3 2017 Tom Hughes <tom@compton.nu> - 2.11.0-1
- Initial build of 2.11.0
