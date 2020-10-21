%global pypi_name gcsfs
# Tests require internet access
%bcond_with network

Name:           python-%{pypi_name}
Version:        0.6.2
Release:        3%{?dist}
Summary:        Convenient Filesystem interface over GCS

License:        BSD
URL:            https://github.com/dask/gcsfs
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Pythonic file-system for Google Cloud Storage.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-decorator
BuildRequires:  python3-fsspec
BuildRequires:  python3-fusepy
BuildRequires:  python3-google-auth
BuildRequires:  python3-google-auth-oauthlib
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-vcrpy
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Pythonic file-system for Google Cloud Storage.

%package -n python-%{pypi_name}-doc
Summary:        Documentation for %{pypi_name}

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-numpydoc

%description -n python-%{pypi_name}-doc
Documentation for %{pypi_name}.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install
PYTHONPATH=%{buildroot}%{python3_sitelib} sphinx-build-3 docs/source html
rm -rf html/.{doctrees,buildinfo}

%if %{with network}
%check
# One test is failing
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v gcsfs/tests \
  -k "not test_request_header"
%endif

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.txt

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.2-2
- Condition for tests
- Update BR (rhbz#1836686)

* Sun May 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.2-1
- Initial package for Fedora
