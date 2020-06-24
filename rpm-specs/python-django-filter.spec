%global pypi_name django-filter

Name:           python-%{pypi_name}
Version:        2.2.0
Release:        5%{?dist}
Summary:        A Django application for allowing users to filter queryset dynamically

License:        BSD
URL:            https://github.com/carltongibson/django-filter
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-django
BuildRequires:  python3-mock
BuildRequires:  python3-setuptools
BuildRequires:  python3-django-rest-framework
BuildRequires:  python3-django-crispy-forms
BuildRequires:	python3-sphinx
BuildRequires:	python3-sphinx_rtd_theme

%global _description\
Django-filter is a reusable Django application for allowing users to filter\
querysets dynamically.

%description %_description

%package -n python3-%{pypi_name}
Summary:        %summary
Requires:       python3-django
Requires:       python3-django-rest-framework
%{?python_provide:%python_provide python3-%{pypi_name}}

Obsoletes:      python-%{pypi_name} < 1.0.2-3
Obsoletes:      python2-%{pypi_name} < 1.0.2-3

%description -n python3-%{pypi_name} %_description

%package -n python-%{pypi_name}-doc
Summary:        django-filter documentation
%description -n python-%{pypi_name}-doc
Documentation for django-filter

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%build
%py3_build
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

# https://github.com/carltongibson/django-filter/issues/1069
# %check
# %{__python3} runtests.py

%files -n python3-%{pypi_name}
%doc CHANGES.rst README.rst LICENSE docs/
%{python3_sitelib}/django_filters
%{python3_sitelib}/django_filter-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-2
- Rebuilt for Python 3.8

* Fri Aug 16 2019 Luis Bazan <lbazan@fedoraproject.org> - 2.2.0-1
- New upstream version

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 11 2019 Luis Bazan <lbazan@fedoraproject.org> - 2.1.0-2
- Add BuildRequires

* Thu Apr 11 2019 Luis Bazan <lbazan@fedoraproject.org> - 2.1.0-1
- New upstream version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Luis Bazan <lbazan@fedoraproject.org> - 2.0.0-1
- New upstream version

* Mon Jul 23 2018 Luis Bazan <lbazan@fedoraproject.org> - 1.1.0-3
- Add Buildrequires

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Luis Bazan <lbazan@fedoraproject.org> - 1.1.0-1
- New Upstream version

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 04 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-3
- Remove Python 2 subpackage (#1494761)
- Remove Groups
- Use modern Python build+install macros
- Remove Python 3 conditional (it makes no sense now)

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.2-2
- Python 2 binary package renamed to python2-django-filter
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Fri Dec 08 2017 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-1
- Update to 1.0.2 (#1523407)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Adam Williamson <awilliam@redhat.com> - 1.0.1-1
- Update to latest release (Django 1.10-compatible)
- Update dependencies

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com>
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Jun 19 2015 Slavek Kabrda <bkabrda@redhat.com> - 0.10.0-1
- Update to 0.10.0
- Introduce python3 subpackage

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 10 2014 Luis Bazan <lbazan@fedoraproject.org> - 0.7-2
- change dependecy 

* Thu Apr 10 2014 Luis Bazan <lbazan@fedoraproject.org> - 0.7-1
- New Upstream Version

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 16 2013 Miro Hrončok <mhroncok@redhat.com> - 0.6-1
- New version compatible with Django 1.5
- Using runtests.py instead of creating own test suite
- Added BR python-django-discover-runner
- Filenames in %%docs changed
- Removed patches for Django 1.4
- Added BR python-mock >=1 (3 tests are failing with older mock)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 15 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.5.3-1
- Renamed to python-django-filter.
- Updated to version 0.5.3.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Aug 20 2009 Diego Búrigo Zacarão <diegobz@gmail.com> 0.5.0-1
- Initial RPM release
