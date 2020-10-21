%global srcname cachelib

Name:           python-%{srcname}
Version:        0.1.1
Release:        1%{?dist}
Summary:        A collection of cache libraries with a common API

License:        BSD
URL:            https://pypi.org/project/cachelib/
Source0:        %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
A collection of cache libraries with a common API.

Extracted from Werkzeug.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/


%changelog
* Fri Jul 31 2020 Matěj Grabovský <mgrabovs@redhat.com> - 0.1.1-1
- Initial package
