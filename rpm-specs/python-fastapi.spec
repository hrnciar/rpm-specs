%global pypi_name fastapi

Name:           python-%{pypi_name}
Version:        0.61.1
Release:        2%{?dist}
Summary:        FastAPI - High Performance, Easy to Learn, Fast to Code, Production Ready

License:        MIT
URL:            https://github.com/tiangolo/fastapi
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(starlette)
BuildRequires:  python3dist(pydantic)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(python-jose)
BuildRequires:  python3dist(passlib)
BuildRequires:  python3dist(bcrypt)
BuildRequires:  python3dist(peewee)
BuildRequires:  python3dist(sqlalchemy)
BuildRequires:  python3dist(flask)
#BuildRequires:  python3dist(orjson)

%description
FastAPI framework, high performance, easy to learn, fast to code,
ready for production

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:  python3dist(starlette)
Requires:  python3dist(pydantic)
Requires:  python3dist(uvicorn)

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
FastAPI framework, high performance, easy to learn, fast to code,
ready for production

%prep
%autosetup -n %{pypi_name}-%{version}
#disable these tests for now
rm tests/test_tutorial/test_custom_response/test_tutorial001b.py
rm tests/test_tutorial/test_async_sql_databases/test_tutorial001.py
rm tests/test_default_response_class.py
rm tests/test_security_oauth2.py
rm tests/test_validate_response_recursive.py


%build
%py3_build

%install
%py3_install

%check
%pytest

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Oct  7 00:24:09 -03 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.61.1-2
- add missing deps.

* Wed Sep 30 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.61.1-1
- Initial package.
- Fix license TAG.