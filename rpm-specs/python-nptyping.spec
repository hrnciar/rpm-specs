%global pypi_name nptyping
%{?python_disable_dependency_generator}

Name:           python-%{pypi_name}
Version:        1.3.0
Release:        1%{?dist}
Summary:        Type hints for Numpy

License:        MIT
URL:            https://github.com/ramonhagenaars/nptyping
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Type hints for Numpy.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Type hints for Numpy.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

#%%check
# There is a circular dependency nptying <-> typish

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%exclude %{python3_sitelib}/tests

%changelog
* Fri Sep 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.0-1
- Initial package for Fedora
