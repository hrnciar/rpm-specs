Name:           expliot
Version:        0.9.0
Release:        1%{?dist}
Summary:        Internet of Things Security Testing and Exploitation framework

License:        MIT
URL:            https://gitlab.com/expliot_framework/expliot
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
A Framework for security testing and exploiting IoT products and IoT
infrastructure. It provides a set of plugins (test cases) which are used to
perform the assessment and can be extended easily with new ones.

%prep
%autosetup

%build
%py3_build

%install
%py3_install

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
%{python3_sitelib}/*.egg-info/

%changelog
* Wed Sep 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.0-1
- Update to latest upstream release 0.9.0 (rhbz#1877321)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.0-3
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-2
- Rebuilt for Python 3.9

* Mon Mar 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.0-1
- Upgrade to latest upstream release 0.8.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 31 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.2-1
- Upgrade to latest upstream release 0.7.2

* Sat Dec 14 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.0-1
- Upgrade to latest upstream release 0.7.0

* Wed Dec 11 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-1
- Initial package for Fedora
