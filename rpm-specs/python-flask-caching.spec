# Created by pyp2rpm-3.3.2

%global srcname flask-caching

Name:           python-%{srcname}
Version:        1.9.0
Release:        2%{?dist}
Summary:        Adds caching support to your Flask application

License:        BSD
URL:            https://github.com/sh4nks/flask-caching
Source0:        https://github.com/sh4nks/%{srcname}/archive/v%{version}/%{srcname}-v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(flask)
BuildRequires:  python3dist(pylibmc)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-xprocess)
BuildRequires:  python3dist(redis)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
Flask-Caching Adds easy cache support to Flask

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

Requires:       python3dist(flask)
%description -n python3-%{srcname}
Flask-Caching Adds easy cache support to Flask

%package -n python-%{srcname}-doc
Summary:        Flask-Caching documentation
%description -n python-%{srcname}-doc
Documentation for Flask-Caching

%prep
%autosetup -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{srcname}.egg-info

%build

%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE docs/license.rst
%doc README.md
%{python3_sitelib}/flask_caching
%{python3_sitelib}/Flask_Caching-%{version}-py%{python3_version}.egg-info

%files -n python-%{srcname}-doc
%doc html
%license LICENSE docs/license.rst

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.9.0-1
- Update to 1.9.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.8.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.8.0-1
- Update to 1.8.0
- Drop hack for new pytest-cov

* Mon Jun 17 2019 Lukas Brabec <lbrabec@redhat.com> - 1.7.2-1
- Initial package.