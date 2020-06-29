%global pypi_name httpcore
# Dependency generator is having problems with the given requirements
%{?python_disable_dependency_generator}

Name:           python-%{pypi_name}
Version:        0.9.1
Release:        1%{?dist}
Summary:        Minimal low-level HTTP client

License:        BSD
URL:            https://github.com/encode/httpcore
Source0:        %{pypi_source}
BuildArch:      noarch

%description
The HTTP Core package provides a minimal low-level HTTP client, which does
one thing only: Sending HTTP requests. It does not provide any high level
model abstractions over the API, does not handle redirects, multipart uploads,
building authentication headers, transparent HTTP caching, URL parsing, etc.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       (python3dist(h11) >= 0.8 with python3dist(h11) < 0.10)
Requires:       (python3dist(h2) >= 3 with python3dist(h2) < 4)
Requires:       (python3dist(sniffio) >= 1 with python3dist(sniffio) < 2)

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The HTTP Core package provides a minimal low-level HTTP client, which does
one thing only: Sending HTTP requests. It does not provide any high level
model abstractions over the API, does not handle redirects, multipart uploads,
building authentication headers, transparent HTTP caching, URL parsing, etc.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.md
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jun 05 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.1-1
- Initial package for Fedora
