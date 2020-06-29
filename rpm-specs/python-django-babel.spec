%global pypi_name django-babel

Name:           python-%{pypi_name}

Version:        0.6.2
Release:        12%{?dist}
Summary:        Utilities for using Babel in Django

License:        BSD
URL:            http://github.com/python-babel/django-babel/
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This package contains various utilities for integration of
Babel into the Django web framework:

* A message extraction plugin for Django templates.
* A middleware class that adds the Babel `Locale`_ object to requests.
 * A set
of template tags for date and number formatting.


%package -n python3-django-babel
Summary:        Utilities for using Babel in Django

%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-django
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx

# test requirements
# BuildRequires:  python3-coverage
# BuildRequires:  python3-pytest
# BuildRequires:  python3-pytest-cov
# BuildRequires:  python3-pytest-flakes
# currently missing test dep:
# BuildRequires:  python3-coveralls

Requires:       python3-django
Requires:       python3-babel >= 1.3
Requires:       python3-setuptools

Obsoletes:      python-django-babel < 0.6.2-3
Obsoletes:      python2-django-babel < 0.6.2-3

%description -n python3-django-babel
This package contains various utilities for integration of
Babel into the Django web framework:

* A message extraction plugin for Django templates.
* A middleware class that adds the Babel `Locale`_ object to requests.
 * A set
of template tags for date and number formatting.

%prep
%setup -q -n %{pypi_name}-%{version}



%build
%py3_build

# generate html docs
export PYTHONPATH=.:$PYTHONPATH
sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}




%install
%py3_install

%check
# python-coveralls is missing test requirement
#%{__python3} setup.py test

%files -n python3-django-babel
%doc README.rst
%{python3_sitelib}/django_babel/
%{python3_sitelib}/django_babel-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-5
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-4
- Removed Python 2 subpackage for https://fedoraproject.org/wiki/Changes/Django20
- Run Python 3 version of Sphinx
- Use %%py3_... macros for build and install
- Make sure %%{python3_sitelib}/django_babel/ is a directory

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Matthias Runge <mrunge@redhat.com> - 0.6.2-2
- fix python2 and python2-django requires

* Wed Dec 20 2017 Matthias Runge <mrunge@redhat.com> - 0.6.2-1
- update to 0.6.2 (rhbz#1445554)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Mar 01 2016 Matthias Runge <mrunge@redhat.com> - 0.5.0-1
- update to 0.5.0, support django-1.9

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Sep 10 2015 Matthias Runge <mrunge@redhat.com> - 0.4.0-2
- spec fixes, move docs creation to build (rhbz#1261042)

* Tue Sep 08 2015 Matthias Runge <mrunge@redhat.com> - 0.4.0-1
- Initial package.
