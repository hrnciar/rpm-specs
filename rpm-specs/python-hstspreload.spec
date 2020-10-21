%global pypi_name hstspreload

Name:           python-%{pypi_name}
Version:        2020.10.20
Release:        1%{?dist}
Summary:        Chromium HSTS Preload list

License:        BSD
URL:            https://github.com/sethmlarson/hstspreload
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Chromium HSTS Preload list as a Python package. The package provides a
single function: in_hsts_preload() which takes an IDNA-encoded host and
returns either True or False regarding whether that host should be only
accessed via HTTPS.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Chromium HSTS Preload list as a Python package. The package provides a
single function: in_hsts_preload() which takes an IDNA-encoded host and
returns either True or False regarding whether that host should be only
accessed via HTTPS.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Oct 20 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2020.10.20-1
- Update to new upstream release 2020.10.20 (#1889570)

* Tue Oct 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2020.10.6-1
- Update to new upstream release 2020.10.6 (#1885451)

* Tue Sep 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2020.9.29-1
- Update to new upstream release 2020.9.29 (#1883393)

* Fri Sep 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2020.9.25-1
- Update to new upstream release 2020.9.25 (#1881756)

* Thu Sep 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2020.9.23-1
- Update to new upstream release 2020.9.23 (#1881756)

* Thu Sep 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2020.9.23-1
- Update to new upstream release 2020.9.23 (#1881756)

* Tue Sep 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2020.9.22-1
- Update to new upstream release 2020.9.22 (#1881267)

* Tue Sep 15 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2020.9.15-1
- Update to new upstream release 2020.9.15 (#1878942)

* Wed Sep 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2020.9.9-1
- Update to new upstream release 2020.9.9 (#1877191)

* Wed Sep 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2020.9.2-1
- Update to new upstream release 2020.9.2 (#1874701)

* Tue Aug 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2020.8.18-1
- Update to new upstream release 2020.8.18

* Wed Aug 12 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2020.8.12-1
- Update to new upstream release 2020.8.12

* Sun Aug 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2020.8.8-1
- Update to new upstream release 2020.8.8

* Fri Jul 31 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2020.7.29-1
- Update to new upstream release 2020.7.29

* Tue Jul 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2020.7.22-1
- Update to new upstream release 2020.7.22

* Mon Jul 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2020.7.7-1
- Update to new upstream release 2020.7.7

* Fri Jul 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2020.6.30-1
- Update to new upstream release 2020.6.30

* Sat Jun 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2020.6.23-1
- Update to new upstream release 2020.6.23

* Fri Jun 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2020.6.16-1
- Update to new upstream release 2020.6.16

* Fri Jun 05 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2020.6.5-1
- Initial package for Fedora