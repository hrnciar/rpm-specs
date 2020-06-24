%global pypi_name past_time

Name:           past-time
Version:        0.2.0
Release:        5%{?dist}
Summary:        Visualizer for the days of the year

License:        MIT
URL:            https://github.com/fabaff/past-time
Source0:        https://github.com/fabaff/past-time/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-freezegun
BuildRequires:  python3-click
BuildRequires:  python3-tqdm

%description
A simple tool to visualize the progress of the year based on the past days.

%prep
%autosetup

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files
%doc README.rst
%license LICENSE
%{_bindir}/%{name}
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{pypi_name}

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-5
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 18 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.0-3
- Update files section

* Wed Dec 11 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.0-2
- Fix ownership (rhbz#1772664)

* Thu Nov 14 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.0-1
- Enable tests

* Wed Nov 13 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.0-1
- Initial package for Fedora
