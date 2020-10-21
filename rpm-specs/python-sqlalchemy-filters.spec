%global pypi_name sqlalchemy-filters

Name:           python-%{pypi_name}
Version:        0.12.0
Release:        2%{?dist}
Summary:        A library to filter SQLAlchemy queries

License:        ASL 2.0
URL:            https://github.com/juliotrigo/sqlalchemy-filters
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Filter, sort and paginate SQLAlchemy query
objects. Ideal for exposing these actions over a REST API.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(six) >= 1.10
Requires:       python3dist(sqlalchemy) >= 1.0.16
%description -n python3-%{pypi_name}
Filter, sort and paginate SQLAlchemy query
objects. Ideal for exposing these actions over a REST API.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
# Tests are not included in the tarball

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/sqlalchemy_filters
%{python3_sitelib}/sqlalchemy_filters-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Sep 25 2020 Javier Peña <jpena@redhat.com> - 0.12.0-2
- Removed funcsigs dependency, not needed in this Python release.

* Fri Sep 25 2020 Javier Peña <jpena@redhat.com> - 0.12.0-1
- Initial package.
