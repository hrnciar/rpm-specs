%global pypi_name litecli

Name:           %{pypi_name}
Version:        1.4.1
Release:        2%{?dist}
Summary:        CLI for SQLite databases

License:        BSD
URL:            https://github.com/dbcli/litecli
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(cli-helpers)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(configobj)
BuildRequires:  python3dist(prompt-toolkit)
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sqlparse)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
litecli is a command-line client for SQLite databases that has auto-completion
and syntax highlighting.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
litecli is a command-line client for SQLite databases that has auto-completion
and syntax highlighting.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files
%{_bindir}/litecli

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sun Oct 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.1-2
- Update check section

* Sun Oct 11 2020 José Lemos Neto <LemosJoseX@protonmail.com> - 1.4.1-1
- Update to version 1.4.1

* Tue Jul 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.2-1
- Initial package for Fedora
