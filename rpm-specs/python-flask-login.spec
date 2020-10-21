%global pypi_name Flask-Login

Name:           python-flask-login
Version:        0.4.1
Release:        11%{?dist}
Summary:        User session management for Flask

License:        MIT
URL:            https://github.com/maxcountryman/flask-login
Source0:        https://files.pythonhosted.org/packages/source/F/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%global _description\
Flask-Login provides user session management for Flask. It handles the common\
tasks of logging in, logging out, and remembering your users' sessions over\
extended periods of time.

%description %_description

%package -n     python%{python3_pkgversion}-flask-login
Summary:        User session management for Flask
Requires:       python%{python3_pkgversion}-flask
%{?python_provide:%python_provide python%{python3_pkgversion}-flask-login}
%description -n python%{python3_pkgversion}-flask-login
Flask-Login provides user session management for Flask. It handles the common
tasks of logging in, logging out, and remembering your users' sessions over
extended periods of time.


%prep
%setup -q -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'



%build
%{__python3} setup.py build


%install
%{__python3} setup.py install --skip-build --root %{buildroot}



%files -n python%{python3_pkgversion}-flask-login
%doc README.md
%license LICENSE
%{python3_sitelib}/*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 25 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-5
- Subpackage python2-flask-login has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-2
- Rebuilt for Python 3.7

* Fri Feb 16 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.4.1-1
- make spec file compatible with epel7
- always build for python 3
- 0.4.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3.0-8
- Python 2 binary package renamed to python2-flask-login
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Sep 14 2015 Richard Marko <rmarko@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 03 2015 Miroslav Suchy <msuchy@redhat.com> - 0.2.11-3
- add python3- subpackage

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Richard Marko <rmarko@fedoraproject.org> - 0.2.11-1
- Update to 0.2.11

* Mon Aug 26 2013 Richard Marko <rmarko@fedoraproject.org> - 0.2.7-1
- Update to 0.2.7

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 07 2013 Richard Marko <rmarko@fedoraproject.org> - 0.2.4-3
- Removed upstream egg

* Thu Jul 04 2013 Richard Marko <rmarko@fedoraproject.org> - 0.2.4-2
- Added python-setuptools to BuildRequires
- Fixed Summary

* Tue Jul 02 2013 Richard Marko <rmarko@fedoraproject.org> - 0.2.4-1
- Initial packaging attempt
