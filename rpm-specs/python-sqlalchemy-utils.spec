%global modname SQLAlchemy-Utils

Name:               python-sqlalchemy-utils
Version:            0.34.2
Release:            4%{?dist}
Summary:            Various utility functions for SQLAlchemy

License:            BSD
URL:                http://pypi.python.org/pypi/SQLAlchemy-Utils
Source0:            %pypi_source SQLAlchemy-Utils

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-six
BuildRequires:      python3-sqlalchemy >= 0.9.3
BuildRequires:      python3-pytest
BuildRequires:      python3-pytz
BuildRequires:      python3-flexmock
BuildRequires:      python3-dateutil
BuildRequires:      python3-mock

%global _description\
Various utility functions and custom data types for SQLAlchemy.\


%description %_description

%package -n         python3-sqlalchemy-utils
Summary:            Various utility functions for SQLAlchemy
%{?python_provide:%python_provide python3-sqlalchemy-utils}
Requires:           python3-sqlalchemy >= 0.9.3
Requires:           python3-six

%description -n python3-sqlalchemy-utils
Various utility functions and custom data types for SQLAlchemy.


%prep
%setup -q -n %{modname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'


%build
%py3_build


%install
%py3_install

%check
# Unit-tests seems to be broken in the unittest module on py3.5
#%{__python3} setup.py test


%files -n python3-sqlalchemy-utils
%doc README.rst
%license LICENSE
%{python3_sitelib}/sqlalchemy_utils/
%{python3_sitelib}/SQLAlchemy_Utils-%{version}*/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.34.2-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.34.2-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Tue Aug 20 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.34.2-1
- Update to 0.34.2

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.32.12-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 05 2019 Miro Hrončok <mhroncok@redhat.com> - 0.32.12-10
- Subpackage python2-sqlalchemy-utils has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.32.12-7
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.32.12-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.32.12-4
- Python 2 binary package renamed to python2-sqlalchemy-utils
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.32.12-1
- Update to 0.32.12

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.31.3-3
- Rebuild for Python 3.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 20 2015 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.31.3-1
- Update to 0.31.3

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 26 2015 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.30.0-1
- Update to 0.30.0

* Mon Sep 01 2014 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.26.13-2
- Clean python macro at the top
- Add python3 subpackage

* Tue Aug 26 2014 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.26.13-1
- initial package for Fedora
