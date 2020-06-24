%global pypi_name pgcli

Name:           %{pypi_name}
Version:        3.0.0
Release:        3%{?dist}
Summary:        CLI for Postgres Database. With auto-completion and syntax highlighting

License:        BSD
URL:            http://pgcli.com
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(cli-helpers) >= 1.2
BuildRequires:  python3dist(click) >= 4.1
BuildRequires:  python3dist(configobj) >= 5.0.6
BuildRequires:  python3dist(humanize) >= 0.5.1
#BuildRequires:  python3dist(keyring) >= 12.2
BuildRequires:  python3dist(prompt-toolkit)
BuildRequires:  python3dist(psycopg2) >= 2.8
BuildRequires:  python3dist(pygments) >= 2
BuildRequires:  python3dist(setproctitle) >= 1.1.9
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sqlparse)

Requires:       python3dist(cli-helpers) >= 1.2
Requires:       python3dist(click) >= 4.1
Requires:       python3dist(configobj) >= 5.0.6
Requires:       python3dist(humanize) >= 0.5.1
#Requires:       python3dist(keyring) >= 12.2
Requires:       python3dist(prompt-toolkit)
Requires:       python3dist(psycopg2) >= 2.8
Requires:       python3dist(pygments) >= 2
Requires:       python3dist(setproctitle) >= 1.1.9
Requires:       python3dist(sqlparse)

%{?python_provide:%python_provide python3-%{pypi_name}}

#BuildRequires for tests
BuildRequires:  python3dist(pytest) >= 2.7.0
BuildRequires:  python3dist(pgspecial) >= 1.11.8
BuildRequires:  python3dist(click) >= 4.1
BuildRequires:  python3dist(pygments) >= 2.0
BuildRequires:  python3dist(prompt-toolkit)
BuildRequires:  python3dist(psycopg2) >= 2.8
BuildRequires:  python3dist(sqlparse) >= 0.3.0
BuildRequires:  python3dist(configobj) >= 5.0.6
BuildRequires:  python3dist(humanize) => 0.5.1
BuildRequires:  python3dist(cli-helpers) >= 1.2.0

BuildRequires:  python3dist(setproctitle) >= 1.1.9
BuildRequires:  python3dist(mock) >= 1.0.1
BuildRequires:  python3dist(behave) >= 1.2.4
BuildRequires:  python3dist(pexpect) >= 3.3
BuildRequires:  python3dist(keyring) >= 11.0.0

%description
CLI for Postgres Database. With auto-completion and syntax highlighting

%prep
%autosetup
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=build/lib/ py.test-3

%files
%license LICENSE.txt
%doc README.rst changelog.rst
%{_bindir}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Jun 2 2020 Dick Marinus <dick@mrns.nl> - 3.0.0-3
- Add tests

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-2
- Rebuilt for Python 3.9

* Mon May 04 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 3.0.0-1
- Initial package.
- fix autosetup macro usage
