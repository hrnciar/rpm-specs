%global srcname netdisco

Name:           python-netdisco
Version:        2.8.2
Release:        1%{?dist}
Summary:        Python library to scan local network for services and devices

License:        MIT
URL:            https://github.com/home-assistant/netdisco
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-zeroconf
BuildRequires:  python3-requests
BuildRequires:  python3-pytest

%description
NetDisco is a Python 3 library to discover local devices and services. It
allows to scan on demand or offer a service that will scan the network in
the background in a set interval.

Current methods of scanning:
- mDNS (includes Chromecast, Homekit)
- uPnP
- Plex Media Server using Good Day Mate protocol
- Logitech Media Server discovery protocol
- Daikin discovery protocol
- Web OS discovery protocol

%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       python3-zeroconf
Requires:       python3-requests
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{srcname}
NetDisco is a Python 3 library to discover local devices and services. It
allows to scan on demand or offer a service that will scan the network in
the background in a set interval.

Current methods of scanning:
- mDNS (includes Chromecast, Homekit)
- uPnP
- Plex Media Server using Good Day Mate protocol
- Logitech Media Server discovery protocol
- Daikin discovery protocol
- Web OS discovery protocol

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests

%files -n python3-%{srcname}
%doc README.md
%license LICENSE.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}*.egg-info

%changelog
* Tue Aug 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.8.2-1
- Update to latest upstream release 2.8.2 (rhbz#1852280)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.7.1-1
- Update to latest upstream release 2.7.1 (rhbz#1848247)

* Sat Jun 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.7.0-1
- Update to latest upstream release 2.7.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 05 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.6.0-2
- Remove requirement

* Wed Apr 10 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.6.0-1
- Update to latest upstream release 2.6.0

* Mon Mar 18 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.5.0-1
- Update to latest upstream release 2.5.0

* Mon Mar 11 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.4.0-1
- Update to latest upstream release 2.4.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Fabian Affolter <mail@fabian-affolter.ch> - 2.2.0-1
- Update to latest upstream release 2.2.0

* Wed Aug 08 2018 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.0-1
- Update to latest upstream release 2.0.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-2
- Rebuilt for Python 3.7

* Sat Jun 16 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.0-1
- Update to latest upstream release 1.5.0

* Mon Jun 11 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.1-1
- Update to latest upstream release 1.4.1

* Tue May 29 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.0-2
- Fix check

* Mon Mar 05 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.0-1
- Initial package
