%global pypi_name flask-healthz
%global mod_name flask_healthz

Name:           python-%{pypi_name}
Version:        0.0.2
Release:        1%{?dist}
Summary:        Module to easily add health endpoints to a Flask application

License:        BSD
URL:            https://github.com/fedora-infra/%{pypi_name}
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
This module allows you to define endpoints in your Flask application
that can be used as liveness and readiness probes.


%package -n python3-%{pypi_name}
Summary:        Module to easily add health endpoints to a Flask application
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This module allows you to define endpoints in your Flask application
that can be used as liveness and readiness probes.


%prep
%autosetup -n %{pypi_name}-%{version} -p1


%build
%py3_build


%install
%py3_install


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{mod_name}/
%{python3_sitelib}/%{mod_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Mon Sep 21 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.2-1
- Initial packaging
