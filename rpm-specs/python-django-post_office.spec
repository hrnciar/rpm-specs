%global app_name django-post_office

Name:           python-%{app_name}
Version:        3.4.0
Release:        4%{?dist}
Summary:        Allows you to log email activities and send mail asynchronously
License:        MIT
URL:            https://pypi.python.org/pypi/%{app_name}
Source0:        https://files.pythonhosted.org/packages/source/d/%{app_name}/%{app_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:	python3-setuptools
BuildRequires:  python3-django
BuildRequires:	python3-jsonfield
BuildRequires:  python3-tox
BuildRequires:	python3-six

%global _description \
Django Post Office is a simple app that allows you to send email asynchronously\
in Django. Supports HTML email, database backed templates and logging.\
\
``post_office`` is implemented as a Django ``EmailBackend`` so you dont need\
to change any of your code to start sending email asynchronously.

%description %{_description}

%package -n python3-%{app_name}
Summary:        Allows you to log email activities and send mail asynchronously
%{?python_provide:%python_provide python3-%{app_name}}

Requires:       python3-django
Requires:	python3-tox
Requires:	python3-jsonfield

%description -n python3-%{app_name} %_description

%prep
%autosetup -n %{app_name}-%{version}

#remove bundled egg info
rm -rf django_post_office.egg-info
find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build
%py3_build

%install
%py3_install

%files -n python3-%{app_name}
%license LICENSE.txt
%doc README.rst AUTHORS.rst
%{python3_sitelib}/post_office
%{python3_sitelib}/django_post_office-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.4.0-3
- Rebuilt for Python 3.9

* Mon Apr 27 2020 Luis Bazan <lbazan@fedoraproject.org> - 3.4.0-2
- Rename BuildRequire

* Mon Apr 20 2020 Luis Bazan <lbazan@fedoraproject.org> - 3.4.0-1
- New upstream version

* Fri Feb 28 2020 Luis Bazan <lbazan@fedoraproject.org> - 3.3.1-1
- New upstream version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 17 2019 Luis Bazan <lbazan@fedoraproject.org> - 3.1.0-4
- Fix changelog

* Wed Apr 17 2019 Luis Bazan <lbazan@fedoraproject.org> - 3.1.0-3
- Fix some lines

* Wed Apr 17 2019 Luis Bazan <lbazan@fedoraproject.org> - 3.1.0-2
- remove 1 duplicate line

* Wed Apr 17 2019 Luis Bazan <lbazan@fedoraproject.org> - 3.1.0-1
- New upstream version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.4-5
- Rebuilt for Python 3.7

* Tue Mar 13 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.0.4-4
- Fix requires

* Tue Mar 06 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.0.4-3
- Correct obsoletes
- Update as per new python guidelines

* Tue Mar 06 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.0.4-2
- Add missing obsoletes

* Sun Mar 04 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 3.0.4-1
- Update to latest upstream release
- Remove python2
- Clean up spec

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.6.0-11
- Python 2 binary package renamed to python2-django-post_office
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-8
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Jan 13 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.6.0-1
- Update to 0.6.0
- Enable python3 support
- Disable tests until python-django-jsonfield is packaged

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 20 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.3.1-3
- Bumpspec to correct upgrade path

* Fri May 03 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.3.1-2
- Update spec as per review: 959172
- Run tests
- add python-django as requires
- remove bundled egg info

* Fri May 03 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.3.1-1
- Initial rpm build

