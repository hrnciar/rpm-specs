%global pypi_name coveralls

Name:           python-%{pypi_name}
Version:        2.1.2
Release:        1%{?dist}
Summary:        Coveralls.io provides seamless integration with coverage.py

LICENSE:        MIT
URL:            https://github.com/coveralls-clients/coveralls-python
Source0:        https://github.com/coveralls-clients/%{pypi_name}-python/archive/%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel > 3.4
BuildRequires:  python3-setuptools
BuildRequires:  %{py3_dist coverage} > 4.0
BuildRequires:  python3-sphinx

%description
Coveralls makes custom report for data generated by coverage.py package and
sends it to json API of coveralls.io service. All python files in your coverage
analysis are posted to this service along with coverage stats, so please make
sure you're not ruining your own security! For private projects there is
Coveralls Pro.

%package -n python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

# Dependencies are automatically provided by the dependency generator

%description -n python3-%{pypi_name}
Coveralls makes custom report for data generated by coverage.py package and
sends it to json API of coveralls.io service. All python files in your coverage
analysis are posted to this service along with coverage stats, so please make
sure you're not ruining your own security! For private projects there is
Coveralls Pro.

%package -n python3-%{pypi_name}-docs
Summary: python-%{pypi_name} documentation
Requires: python-%{pypi_name} = %{version}-%{release}

%description -n python3-%{pypi_name}-docs
Includes the documentation for python-%{pypi_name}


%prep
%autosetup -n %{pypi_name}-python-%{version}
PYTHONPATH=./ sphinx-build-3 -a -b html ./docs/ ./docs/html/

%build
%py3_build

%install
%py3_install
cp %{buildroot}%{_bindir}/coveralls %{buildroot}%{_bindir}/coveralls-py3

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc CHANGELOG.md README.rst
%{python3_sitelib}/*
%{_bindir}/coveralls
%{_bindir}/coveralls-py3

%files -n python3-%{pypi_name}-docs
%doc docs/*

%changelog
* Thu Aug 13 2020 Brian C. Lane <bcl@redhat.com> - 2.1.2-1
- Upstream release 2.1.2
  rhbz#1868205

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 08 2020 Brian C. Lane <bcl@redhat.com> - 2.1.1-1
- Upstream release 2.1.1 to fix regression in 2.1.0
  rhbz#1855051

* Tue Jul 07 2020 Brian C. Lane <bcl@redhat.com> - 2.1.0-1
- Upstream release 2.1.0
  rhbz#1854258

* Thu Jun 25 2020 Brian C. Lane <bcl@redhat.com> - 2.0.0-3
- Add BuildRequires: python3-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-2
- Rebuilt for Python 3.9

* Tue Apr 07 2020 Brian C. Lane <bcl@redhat.com> - 2.0.0-1
- Upstream release 2.0.0
  rhbz#1821549
- Upstream drops support for Python 2.x and Python 3 versions < 3.5

* Wed Feb 19 2020 Brian C. Lane <bcl@redhat.com> - 1.11.1-1
- Upstream release 1.11.1
  rhbz#1803285

* Wed Feb 12 2020 Brian C. Lane <bcl@redhat.com> - 1.11.0-1
- Upstream release 1.11.0
  rhbz#1802032

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Brian C. Lane <bcl@redhat.com> - 1.10.0-1
- Upstream release 1.10.0
  rhbz#1787781

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.8.2-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.8.2-2
- Rebuilt for Python 3.8

* Wed Aug 07 2019 Brian C. Lane <bcl@redhat.com> - 1.8.2-1
- Upstream release 1.8.2
  rhbz#1719981
- Removeing python2 package
- Switched to upstream source tar.gz from GitHub because it includes docs (and tests)
- Add new python3-coveralls-docs package with html documentation and sphinx source

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-4
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 30 2017 williamjmorenor@gmail.com - 1.2.0-1
- Update to v.1.2.0 release
- Update Source0 url
- Update BuildRequires
- Update files manifest

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1-3
- Rebuild for Python 3.6

* Mon Aug 22 2016 William Moreno <williamjmorenor@gmail.com> - 1.1-2
- Temporary disable tests

* Sat Jan 23 2016 Germano Massullo <germano.massullo@gmail.com> - 1.1-1
- First commit on Fedora's Git
