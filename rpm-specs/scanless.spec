%global pypi_name scanless

Name:           %{pypi_name}
Version:        2.1.3
Release:        1%{?dist}
Summary:        An online port scan scraper

License:        Unlicense
URL:            https://github.com/vesche/scanless
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

Requires:       python3-%{pypi_name} = %{version}-%{release}

%description
scanless is a Python 3 command-line utility and library for using websites
that can perform port scans on your behalf.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
scanless is a Python 3 command-line utility and library for using websites
that can perform port scans on your behalf.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n %{pypi_name}
%{_bindir}/%{pypi_name}

%files -n python3-%{pypi_name}
%doc README.md
%{_bindir}/scanless
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sun Jun 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.3-1
- Fix for requirement no longer needed
- Update to latest upstream release 2.1.3

* Sat Jun 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.2-2
- Fix requirement (rhbz#1844803)

* Sun Jun 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.2-1
- Initial package for Fedora
