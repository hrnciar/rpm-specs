%global pypi_name pygatt
%{?python_disable_dependency_generator}

Name:           python-pygatt
Version:        4.0.5
Release:        4%{?dist}
Summary:        A Python Module for Bluetooth LE Generic Attribute Profile

License:        ASL 2.0
URL:            https://github.com/peplin/pygatt
Source0:        https://github.com/peplin/pygatt/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-coverage

Requires:       bluez

%description
This Module allows reading and writing to GATT descriptors on devices such as
fitness trackers, sensors, and anything implementing standard GATT Descriptor
behavior.

pygatt wraps BlueZ's 'gatttool' command-line utility with a Pythonic API.

%package -n python3-%{pypi_name}
Summary:        %{summary}
Requires:       python3-pexpect
Requires:       python3-pyserial
Requires:       bluez
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This Module allows reading and writing to GATT descriptors on devices such as
fitness trackers, sensors, and anything implementing standard GATT Descriptor
behavior.

pygatt wraps BlueZ's 'gatttool' command-line utility with a Pythonic API.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/*.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.5-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Fabian Affolter <mail@fabian-affolter.ch> - 4.0.5-1
- Update to latest upstream release 4.0.5 (rhbz#1751057)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Fabian Affolter <mail@fabian-affolter.ch> - 4.0.3-2
- Disable dependency generator (rhbz#1720235)
- Update source URL

* Thu May 09 2019 Fabian Affolter <mail@fabian-affolter.ch> - 4.0.3-1
- Update to latest upstream release 4.0.3 (rhbz#1694397)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.2.0-6
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.2.0-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.2.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 17 2017 Fabian Affolter <mail@fabian-affolter.ch> - 3.2.0-1
- Update to latest upstream release 3.2.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 18 2017 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.1-2
- Fix requirement

* Mon Apr 03 2017 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.1-1
- Update to latest upstream release 3.1.1
- Update BR

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.0-3
- Fix BR

* Tue Jan 17 2017 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.0-2
- Change source URL
- Update requirements

* Thu Nov 17 2016 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.0-1
- Update to latest Python guidelines

* Fri Sep 16 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.0-1
- Update to latest upstream release 2.1.0

* Tue Mar 22 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.1-1
- Update py3
- Update to latest upstream release 2.0.1

* Wed Jun 03 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.1-1
- Update to latest upstream release 1.0.1

* Thu Mar 12 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.0-1
- Initial spec
