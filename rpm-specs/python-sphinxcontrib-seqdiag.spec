%global pypi_name sphinxcontrib-seqdiag

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        1%{?dist}
Summary:        Sphinx "seqdiag" extension

License:        BSD
URL:            http://github.com/blockdiag/sphinxcontrib-seqdiag
Source0:        https://pypi.python.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%package -n python3-%{pypi_name}
Summary:        Sphinx "seqdiag" extension

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

Requires:       python3-blockdiag >= 1.5.0
Requires:       python3-seqdiag >= 0.9.3
Requires:       python3-sphinx >= 2.0

%description -n python3-%{pypi_name}
A sphinx extension for embedding sequence diagram using seqdiag_.

%description
A sphinx extension for embedding sequence diagram using seqdiag_.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/sphinxcontrib
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/*-nspkg.pth
%exclude %{python3_sitelib}/tests/


%changelog
* Mon Sep 14 2020 Javier Peña <jpena@redhat.com> - 2.0.0-1
- Update to version 2.0.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.4-22
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.4-20
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.4-19
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 19 2018 Javier Peña <jpena@redhat.com> - 0.8.4-16
- Removed Python 2 package from Fedora 30+ (bz#1629739)
- Modernized prep, build, install sections

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.4-14
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8.4-13
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.4-9
- Rebuild for Python 3.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 13 2015 Javier Peña <jpena@redhat.com> - 0.8.4-7
- Fixed package build with Python 3.5
* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Aug 27 2015 Javier Peña <jpena@redhat.com> - 0.8.4-5
- Drop python_sitelib fallback macro
* Thu Aug 27 2015 Javier Peña <jpena@redhat.com> - 0.8.4-4
- Comply with updated Python packaging guidelines
* Thu Aug 27 2015 Javier Peña <jpena@redhat.com> - 0.8.4-3
- Fixed python3 macro
- Improved file listing
* Mon Jul 13 2015 jpena <jpena@redhat.com> - 0.8.4-2
- Added python3 build.
* Thu Jul 09 2015 jpena <jpena@redhat.com> - 0.8.4-1
- Initial package.
