%global pypi_name convertdate
# See https://bugzilla.redhat.com/show_bug.cgi?id=1748948
%{?python_disable_dependency_generator}

Name:           python-%{pypi_name}
Version:        2.2.0
Release:        4%{?dist}
Summary:        Python module to convert date formats and calculating holidays


License:        MIT
URL:            https://github.com/fitnr/convertdate
Source0:        https://github.com/fitnr/convertdate/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Converts between Gregorian dates and other calendar systems. Calendars 
included: Baha'i, French Republican, Hebrew, Indian Civil, Islamic, ISO, 
Julian, Mayan and Persian.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytz
BuildRequires:  python3-pyephem
BuildRequires:  python3-pymeeus

Requires:       python3-pytz
Requires:       python3-pyephem
Requires:       python3-pymeeus
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Converts between Gregorian dates and other calendar systems. Calendars 
included: Baha'i, French Republican, Hebrew, Indian Civil, Islamic, ISO, 
Julian, Mayan and Persian.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} tests

%files -n python3-%{pypi_name}
%doc HISTORY.rst README.md
%license LICENSE
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{pypi_name}/

%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.2.0-2
- Add additional requirements manually (rhbz#1792034)

* Tue Oct 29 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.2.0-1
- Update to latest upstream release 2.2.0

* Thu Sep 05 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.3-2
- Update summary (rhbz#1748938)

* Tue Sep 03 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.3-1
- Initial package for Fedora
