%global mod_name Flask-Script

Name:       python-flask-script
Version:    2.0.6
Release:    8%{?dist}
Summary:    Scripting support for Flask

License:    BSD
URL:        http://flask-script.readthedocs.org/en/latest/
Source0:    https://pypi.python.org/packages/source/F/%{mod_name}/%{mod_name}-%{version}.tar.gz

# using flask_script everywhere instead of flask.ext.script
# adjusted https://github.com/smurfix/flask-script/commit/fcf894b6e4d0ad17489480b722c870aaea600db1
Patch0:     fix-imports.patch

BuildArch:  noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-flask
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-pytest

%global _description\
The Flask-Script extension provides support for writing external scripts in\
Flask.This includes running a development server, a customized Python shell,\
scripts to set up your database, cronjobs, and other command-line tasks that\
belong outside the web application itself.

%description %_description

%package -n python%{python3_pkgversion}-flask-script
Summary:    Scripting support for flask in python3-flask

Requires:       python%{python3_pkgversion}-flask

%description -n python%{python3_pkgversion}-flask-script
The Flask-Script extension provides support for writing external scripts in
Flask.This includes running a development server, a customized Python shell,
scripts to set up your database, cronjobs, and other command-line tasks that
belong outside the web application itself.

%prep
%autosetup -p1 -n %{mod_name}-%{version}
# delete the mac's .ds_store file
rm -f docs/.DS_Store

%build
%py3_build

# generate sphinx documentation
cd docs && make SPHINXBUILD=sphinx-build-3 html
# deleting unneeded buildinfo, we dont expect users to change html docs
rm -f _build/html/.buildinfo


%check
py.test-3 tests.py

%install
%py3_install


%files -n python%{python3_pkgversion}-flask-script
%doc docs/_build/html README.rst LICENSE 
%{python3_sitelib}/*.egg-info/
%{python3_sitelib}/flask_script/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.6-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 12 2019 Lubomír Sedlář <lsedlar@redhat.com> - 2.0.6-6
- Drop python 2 subpackage

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.6-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.6-1
- Update to 2.0.6
- Clean spec
- Add upstream patch for new Flask compatibility (#1595388)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.5-13
- Rebuilt for Python 3.7

* Fri Feb 16 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.0.5-12
- make spec file compatible with epel7
- always build for python 3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.5-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0.5-9
- Python 2 binary package renamed to python2-flask-script
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0.5-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jul 03 2014 Robert Kuska <rkuska@redhat.com> - 2.0.5-1
- Updated to 2.0.5

* Thu Jul 03 2014 Robert Kuska <rkuska@redhat.com> - 0.6.7-4
- Move Python 3 Requires into correct place

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 16 2014 Robert Kuska <rkuska@redhat.com> - 0.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Apr 28 2014 Robert Kuska <rkuska@redhat.com> - 0.6.7-1
- Update to 0.6.7

* Wed Sep 25 2013 Robert Kuska <rkuska@redhat.com> - 0.6.2-1
- Updated source to latest upstream version and added python3 support

* Tue Aug 06 2013 Robert Kuska <rkuska@redhat.com> - 0.5.3-4
- Fix BuildRequires

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 02 2013 Robert Kuska <rkuska@redhat.com> - 0.5.3-2
- Review fixes

* Thu Mar 21 2013 Robert Kuska <rkuska@redhat.com> - 0.5.3-1
- Initial package
