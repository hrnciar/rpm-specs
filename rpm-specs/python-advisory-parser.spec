%global pypi_name advisory-parser

Name:           python-%{pypi_name}
Version:        1.10
Release:        1%{?dist}
Summary:        Security flaw parser for upstream security advisories

License:        LGPLv3+
URL:            https://github.com/mprpic/advisory-parser
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This library allows you to parse data from security advisories of certain
projects to extract information about security issues. The parsed information
includes metadata such as impact, CVSS score, summary, description, and
others; for a full list, see the advisory_parser/flaw.py file.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This library allows you to parse data from security advisories of certain
projects to extract information about security issues. The parsed information
includes metadata such as impact, CVSS score, summary, description, and
others; for a full list, see the advisory_parser/flaw.py file.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests

%files -n python3-%{pypi_name}
%license LICENSE COPYRIGHT
%doc README.rst
%{python3_sitelib}/advisory_parser
%{python3_sitelib}/advisory_parser-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Jul 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.10-1
- Initial package for Fedora
