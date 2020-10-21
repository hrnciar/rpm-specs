%global with_checks 0

%global pypi_name django-pyscss

Name:           python-%{pypi_name}
Version:        2.0.2
Release:        17%{?dist}
Summary:        Makes it easier to use PySCSS in Django

License:        BSD
URL:            https://github.com/fusionbox/django-pyscss
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description
A collection of tools for making it easier to use
pyScss within Django.

%package -n python3-%{pypi_name}
Summary:        Makes it easier to use PySCSS in Django - Python 3 version

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pillow
BuildRequires:  python3-django-compressor >= 1.3
# django-discover-runner is dead upstream
#BuildRequires:  python3-django-discover-runner
BuildRequires:  python3-scss >= 1.2.0
BuildRequires:  python3-django
BuildRequires:  python3-mock

Requires:       python3-django >= 1.4
Requires:       python3-scss >= 1.3.4

Obsoletes:      python2-%{pypi_name} < 2.0.2-8
Obsoletes:      python-%{pypi_name} < 2.0.2-8

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A collection of tools for making it easier to use
pyScss within Django.
This package provides Python 3 build of %{pypi_name}.


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%if 0%{?with_checks} > 0
%check
%{__python3} setup.py test
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/django_pyscss
%{python3_sitelib}/django_pyscss-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-16
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Matthias Runge <mrunge@redhat.com> - 2.0.2-8
- Removed Python 2 subpackage for https://fedoraproject.org/wiki/Changes/Django20

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-5
- Rebuild for Python 3.6

* Wed Aug 3 2016 Jan Beran <jberan@redhat.com> - 2.0.2-4
- source update
- Python 3 subpackage

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 13 2015 Matthias Runge <mrunge@redhat.com> - 2.0.2-1
- fix FTBFS and update (rhbz#1239832)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 17 2014 Matthias Runge <mrunge@redhat.com> - 1.0.5-1
- update to 1.0.5
- fix tests and utils.py to work with Django-1.7

* Fri Sep 26 2014 Matthias Runge <mrunge@redhat.com> - 1.0.3-1
- update to 1.0.3

* Thu Aug 07 2014 Matthias Runge <mrunge@redhat.com> - 1.0.2-1
- update to 1.0.2

* Tue Jul 08 2014 Matthias Runge <mrunge@redhat.com> - 1.0.1-2
- add br python-setuptools

* Tue Jul 08 2014 Matthias Runge <mrunge@redhat.com> - 1.0.1-1
- Initial package.


