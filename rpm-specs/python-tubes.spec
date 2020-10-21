%global pypi_name tubes

# Something broken in Twisted breaks these tests
%bcond_with check

Name:           python-%{pypi_name}
Version:        0.2.0
Release:        1%{?dist}
Summary:        Flow control and backpressure for event-driven applications

License:        MIT
URL:            https://github.com/twisted/tubes/
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(twisted)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(setuptools)

%description
%{summary}.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
%description -n python3-%{pypi_name}
%{summary}.

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Remove unused dependency
sed -e '/"characteristic",/d' -i setup.py

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
%python3 setup.py test
%endif

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/Tubes-%{version}-py%{python3_version}.egg-info/

%changelog
* Sun Aug 23 2020 Neal Gompa <ngompa13@gmail.com> - 0.2.0-1
- Initial package (#1870882)
