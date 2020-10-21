%bcond_without tests

%global pypi_name toposort

%global _description %{expand:
In computer science, a topological sort (sometimes abbreviated topsort or 
toposort) or topological ordering of a directed graph is a linear ordering of
its vertices such that for every directed edge uv from vertex u to vertex v, u
comes before v in the ordering.}

Name:           python-%{pypi_name}
Version:        1.5
Release:        1%{?dist}
Summary:        Implements a topological sort algorithm

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %{pypi_source}
BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        Implements a topological sort algorithm
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}

rm -rf %{pypi_name}.egg-info
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

chmod -x README.txt
chmod -x LICENSE.txt

%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
PYTHONPATH="%{buildroot}/%{python3_sitelib}/" python%{python3_version} setup.py test
%endif

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.txt
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/__pycache__/*

%changelog
* Fri Aug 28 2020 Aniket Pradhan <major AT fedoraproject DOT org> - 1.5.0-1
- Initial build
