# what it's called on pypi
%global srcname uvicorn
# what it's imported as
%global libname %{srcname}
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{srcname}

%global common_description %{expand:
Uvicorn is a lightning-fast ASGI server implementation, using uvloop and
httptools.  Until recently Python has lacked a minimal low-level
server/application interface for asyncio frameworks.  The ASGI specification
fills this gap, and means we are now able to start building a common set of
tooling usable across all asyncio frameworks.  Uvicorn currently supports
HTTP/1.1 and WebSockets.  Support for HTTP/2 is planned.}

%bcond_without  tests


Name:           python-%{pkgname}
Version:        0.11.8
Release:        1%{?dist}
Summary:        The lightning-fast ASGI server
License:        BSD
URL:            https://www.uvicorn.org
# PyPI tarball doesn't have tests
Source0:        https://github.com/encode/uvicorn/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch


%description %{common_description}


%package -n python3-%{pkgname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
%if %{with tests}
BuildRequires:  %{py3_dist pytest requests}
BuildRequires:  %{py3_dist click h11 httptools uvloop websockets wsproto watchgod}
%endif
%{?python_provide:%python_provide python3-%{pkgname}}


%description -n python3-%{pkgname} %{common_description}


%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{eggname}.egg-info


%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
%pytest --verbose
%endif


%files -n python3-%{pkgname}
%license LICENSE.md
%doc README.md
%{_bindir}/uvicorn
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Aug 18 2020 Carl George <carl@george.computer> - 0.11.8-1
- Latest upstream

* Thu Jun 04 2020 Carl George <carl@george.computer> - 0.11.5-1
- Initial package
