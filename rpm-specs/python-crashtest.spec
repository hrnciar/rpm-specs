%global pypi_name crashtest

%global common_description %{expand:
Crashtest is a Python library that makes exceptions handling and
inspection easier.}

Name:           python-%{pypi_name}
Version:        0.3.1
Release:        1%{?dist}
Summary:        Manage Python errors with ease
License:        MIT

URL:            https://github.com/sdispater/crashtest
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel >= 3.6
BuildRequires:  python3dist(setuptools)

%description %{common_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{common_description}


%prep
%autosetup -n %{pypi_name}-%{version} -p1


%build
%py3_build


%install
%py3_install


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md

%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/


%changelog
* Sat Oct 03 2020 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-1
- Initial package

