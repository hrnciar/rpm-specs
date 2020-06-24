%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with    python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with    python3
%endif

%global pypi_name sphinxcontrib-pecanwsme

Name:           python-%{pypi_name}
Version:        0.10.0
Release:        2%{?dist}
Summary:        Extension to Sphinx for documenting APIs built with Pecan and WSME

License:        ASL 2.0
URL:            https://github.com/dreamhost/sphinxcontrib-pecanwsme
Source0:        https://pypi.python.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This is an extension to Sphinx (http://sphinx-doc.org/) for documenting APIs
built with the Pecan WSGI object-dispatching web framework and WSME
(Web Services Made Easy).

%if %{with python2}
%package -n python2-%{pypi_name}
Summary:        Extension to Sphinx for documenting APIs built with Pecan and WSME
%{?python_provide:%python_provide python2-%{pypi_name}}

BuildRequires:  python2-devel
BuildRequires:  python2-pbr
BuildRequires:  python2-setuptools

Requires: python2-six
Requires: python2-sphinxcontrib-httpdomain

%description -n python2-%{pypi_name}
This is an extension to Sphinx (http://sphinx-doc.org/) for documenting APIs
built with the Pecan WSGI object-dispatching web framework and WSME
(Web Services Made Easy).
%endif

%if %{with python3}
%package -n python3-%{pypi_name}
Summary:        Extension to Sphinx for documenting APIs built with Pecan and WSME
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools

Requires: python3-six
Requires: python3-sphinxcontrib-httpdomain

%description -n python3-%{pypi_name}
This is an extension to Sphinx (http://sphinx-doc.org/) for documenting APIs
built with the Pecan WSGI object-dispatching web framework and WSME
(Web Services Made Easy).
%endif

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif

%install
%if %{with python2}
%py2_install
%endif
%if %{with python3}
%py3_install
%endif

%if %{with python2}
%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/sphinxcontrib/pecanwsme
%{python2_sitelib}/*.egg-info
%{python2_sitelib}/*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/sphinxcontrib/pecanwsme
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/*-nspkg.pth
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-2
- Rebuilt for Python 3.9

* Thu Feb 27 2020 Yatin Karel <ykarel@redhat.com> - 0.10.0-1
- Update to 0.10.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 01 2018 Javier Peña <jpena@redhat.com> - 0.9.0-2
- Removed Python 2 package from Fedora 30+ (bz#1634644)

* Wed Aug 08 2018 Javier Peña <jpena@redhat.com> - 0.9.0-1
- Updated to upstream version 0.9.0
- Enabled python3 build, since 0.9.0 supports it

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8.0-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun 20 2016 Javier Peña <jpena@redhat.com> - 0.8.0-3
- Added BR on python-setuptools
* Mon Jan 11 2016 Javier Peña <jpena@redhat.com> - 0.8.0-2
- Expanded description
- Improved macro usage
* Wed Nov 18 2015 jpena <jpena@redhat.com> - 0.8.0-1
- Initial package.
