%global srcname google-api-core
%global _description %{expand:This library is not meant to stand-alone. Instead it defines common helpers used
by all Google API clients.}

Name:           python-%{srcname}
Version:        1.21.0
Release:        1%{?dist}
Summary:        Core Library for Google Client Libraries

License:        ASL 2.0
URL:            https://github.com/googleapis/python-api-core/
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
# Required for tests
BuildRequires:  %{py3_dist google-auth}
BuildRequires:  %{py3_dist googleapis-common-protos}
BuildRequires:  %{py3_dist grpcio}
BuildRequires:  %{py3_dist mock}
BuildRequires:  %{py3_dist protobuf}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytz}
BuildRequires:  %{py3_dist requests}
BuildRequires:  %{py3_dist six}
BuildArch:      noarch

%description
%{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
# Extras
Requires:       %{py3_dist grpcio}
Requires:       %{py3_dist grpcio-gcp}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{_description}


%prep
%autosetup -n python-api-core-%{version}

# Remove bundled egg-info
rm -rf *.egg-info


%build
%py3_build


%install
%py3_install


%check
PYTHONPATH=$RPM_BUILD_ROOT/%{python3_sitelib}/ pytest-%{python3_version}


%files -n python3-%{srcname}
%doc CHANGELOG.md README.rst
%license LICENSE
%{python3_sitelib}/google/api_core/
%{python3_sitelib}/google_api_core-*.egg-info/
%{python3_sitelib}/google_api_core-*-nspkg.pth

%changelog
* Fri Jun 19 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.21.0-1
- Update to 1.21.0

* Fri Jun 05 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.17.0-1
- Initial RPM release
