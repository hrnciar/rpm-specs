%bcond_without tests

%global pypi_name ratelimiter
%global extraver post0

%global _description %{expand:
This package provides the ratelimiter module, which ensures that an operation
will not be executed more than a given number of times on a given period. This
can prove useful when working with third parties APIs which require for example
a maximum of 10 requests per second.}

Name:           python-%{pypi_name}
Version:        1.2.0
Release:        1.%{extraver}%{?dist}
Summary:        Python module providing rate limiting

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %{pypi_source %{pypi_name} %{version}.%{extraver}}
BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        Python module providing rate limiting
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist pytest}

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}.%{extraver}

rm -rf %{pypi_name}.egg-info
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
PYTHONPATH="%{buildroot}/%{python3_sitelib}/" pytest-%{python3_version}
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}-%{version}.%{extraver}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/__pycache__/*

%changelog
* Mon Aug 24 2020 Aniket Pradhan <major AT fedoraproject DOT org> - 1.2.0-1.post1
- Initial build
