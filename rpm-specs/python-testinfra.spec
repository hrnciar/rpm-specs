%global srcname testinfra

Name:           python-%{srcname}
Version:        4.0.0
Release:        3%{?dist}
Summary:        Unit testing for config-managed server state

License:        ASL 2.0
URL:            https://github.com/philpep/testinfra
Source:         %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)

# testing requirements
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(ansible)
BuildRequires:  python3dist(paramiko)
BuildRequires:  python3dist(pywinrm)

# docs requirements
BuildRequires:  python3dist(sphinx)

%global _description %{expand:
With Testinfra you can write unit tests in Python to test actual state of your
servers configured by management tools like Salt, Ansible, Puppet, Chef and so
on.

Testinfra aims to be a Serverspec equivalent in python and is written as a
plugin to the powerful Pytest test engine.}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        Unit testing for config-managed server state
Requires:       python%{python3_version}dist(ansible)
Requires:       python%{python3_version}dist(paramiko)
Requires:       python%{python3_version}dist(pywinrm)
Suggests:       python%{python3_version}dist(pytest-xdist)
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version}

# no Python 3 salt
rm testinfra/backend/salt.py
sed -i "/'salt':/d" testinfra/backend/__init__.py

%build
%py3_build

# generate html docs
sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -vr html/.{doctrees,buildinfo}

%install
%py3_install

%check
# majority of the tests gets skipped without docker, but some run
%{python3} -m pytest test -v

%files -n python3-%{srcname}
%license LICENSE
%doc html *.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.0.0-1
- Update to 4.0.0

* Sat Aug 31 2019 Chedi Toueiti <chedi.toueiti@gmail.com> - 3.1.0-1
- Update to 3.1.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.17.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Miro Hrončok <mhroncok@redhat.com>
- Drop Python 2 subpackage

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Brett Lentz <brett.lentz@gmail.com> - 1.17.0-1
- update version

* Tue Jul 17 2018 Brett Lentz <brett.lentz@gmail.com> - 1.14.0-1
- update version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.12.0-3
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.12.0-2
- Rebuilt for Python 3.7

* Tue May 1 2018 Brett Lentz <brett.lentz@gmail.com> - 1.12.0-1
- update version

* Tue Apr 3 2018 Brett Lentz <brett.lentz@gmail.com> - 1.11.1-2
- fix deps

* Tue Mar 6 2018 Brett Lentz <brett.lentz@gmail.com> - 1.11.1-1
- update version

* Wed Jan 24 2018 Brett Lentz <brett.lentz@gmail.com> - 1.10.1-1
- initial package
