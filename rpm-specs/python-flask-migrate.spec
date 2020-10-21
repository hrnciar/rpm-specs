%global modname flask-migrate

Name:               python-flask-migrate
Version:            2.5.3
Release:            1%{?dist}
Summary:            SQLAlchemy database migrations for Flask applications using Alembic

License:            MIT
URL:                http://pypi.python.org/pypi/flask-migrate
Source0:            https://pypi.python.org/packages/d4/42/9e1bab5b15495e7acd25cb6b164a050b90da20af7e801aa2a7b1f74efdfa/Flask-Migrate-%{version}.tar.gz
BuildArch:          noarch

%description
SQLAlchemy database migrations for Flask applications using Alembic.

%package -n python%{python3_pkgversion}-%{modname}
Summary:            SQLAlchemy database migrations for Flask applications using Alembic
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}

BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-setuptools
BuildRequires:      python%{python3_pkgversion}-flask
BuildRequires:      python%{python3_pkgversion}-flask-sqlalchemy
BuildRequires:      python%{python3_pkgversion}-alembic
BuildRequires:      python%{python3_pkgversion}-flask-script
Requires:           python%{python3_pkgversion}-flask
Requires:           python%{python3_pkgversion}-flask-sqlalchemy
Requires:           python%{python3_pkgversion}-alembic
Requires:           python%{python3_pkgversion}-flask-script

%description -n python%{python3_pkgversion}-%{modname}
SQLAlchemy database migrations for Flask applications using Alembic.

%prep
%autosetup -n Flask-Migrate-%{version}

# For rpmlint
chmod 0644 flask_migrate/templates/flask-multidb/*
chmod 0644 flask_migrate/templates/flask/*

%build
%py3_build

%install
%py3_install

# Tests are expecting flaskcli which we don't have packaged.
#%check
#%{__python3} setup.py test

%files -n python%{python3_pkgversion}-%{modname}
%doc README.md
%license LICENSE
%{python3_sitelib}/flask_migrate/
%{python3_sitelib}/Flask_Migrate-%{version}*

%changelog
* Tue Sep 29 2020 José Lemos Neto <LemosJoseX@protonmail.com> - 2.5.3-1
- Update to version 2.5.3

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.1-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.1-7
- Subpackage python2-flask-migrate has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.1-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.1-2
- Rebuilt for Python 3.7

* Sun Apr 15 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.1.1-1
- new version

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.0-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 16 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.0.0-7
- make spec file compatible with epel7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Ralph Bean <rbean@redhat.com> - 2.0.0-3
- Conditionalize deps for EL7.

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-2
- Rebuild for Python 3.6

* Wed Aug 10 2016 Ralph Bean <rbean@redhat.com> - 2.0.0-1
- Initial package for Fedora!  \ó/
