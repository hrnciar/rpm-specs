Name:    liquidctl
Summary: Tool for controlling liquid coolers, case fans and RGB LED strips
License: GPLv3+

Version: 1.4.1
Release: 1%{?dist}

URL: https://github.com/jonasmalacofilho/liquidctl
Source0: %{URL}/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-docopt
# Upstream doesn't specify any version requirement,
# but the test suite fails with 0.7.99.post20
BuildRequires: python3-hidapi >= 0.9.0
BuildRequires: python3-pytest
BuildRequires: python3-pyusb
BuildRequires: python3-setuptools

%{?python_enable_dependency_generator}

# Require the python libs in the main package
Requires: python3-%{name} = %{version}-%{release}


%global supported_devices \
- Corsair Hydro H80i v2, H100i v2 and H115i \
- Corsair HX750i, HX850i, HX1000i and HX1200i \
- Corsair RM650i, RM750i, RM850i and RM1000i \
- EVGA CLC 120 (CL12), 240, 280 and 360 \
- NZXT Grid+ V3 \
- NZXT HUE 2 and Hue 2 Ambient \
- NZXT Kraken M22 \
- NZXT Kraken X42, X52, X62 and X72 \
- NZXT Smart Device V1 and V2 \


%global supported_devices_experimental \
- Corsair Hydro H80i GT, H100i GTX and H110i GTX  \
- Corsair Hydro H100i Platinum, H100i Platinum SE and H115i Platinum \
- Corsair Hydro H100i PRO XT and H115i PRO XT \
- Gigabyte RGB Fusion 2.0 Motherboards \
- NZXT E500, E650 and E850 PSUs \
- NZXT Kraken X31, X40, X41, X53, X60, X61, X63 and X73 \
- NXZT Kraken Z63 and Z73 \
- NZXT RGB & Fan Controller \


%description
liquidctl is a tool for controlling various settings of PC internals, such as:
- liquid cooler pump speed
- case fan speed
- RGB LED strip colors

Currently supported devices are: %{supported_devices}

Devices with experimental support: %{supported_devices_experimental}


%package -n python3-%{name}
BuildArch: noarch
Summary: Module for controlling liquid coolers, case fans and RGB LED devices

%description -n python3-%{name}
A python module providing classes for communicating with various cooling devices
and RGB LED solutions.

Currently supported devices are: %{supported_devices}

Devices with experimental support: %{supported_devices_experimental}


%prep
%setup -q -n %{name}-%{version}


%build
export DIST_NAME=$(source /etc/os-release && echo "${NAME} ${VERSION_ID}")
export DIST_PACKAGE="%{name}-%{version}-%{release}.%{_build_arch}"
%py3_build


%install
%py3_install

install -m 755 -d %{buildroot}%{_mandir}/man8/
install -m 644 -p %{name}.8 %{buildroot}%{_mandir}/man8/


%check
mkdir ./test-run-dir
XDG_RUNTIME_DIR=$(pwd)/test-run-dir pytest-3


%files
%doc CHANGELOG.md README.md
%doc docs/
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.*

%files -n python3-%{name}
%license LICENSE.txt
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*.egg-info/


%changelog
* Sat Aug 08 2020 Artur Iwicki <fedora@svgames.pl> - 1.4.1-1
- Update to latest upstream release

* Fri Jul 31 2020 Artur Iwicki <fedora@svgames.pl> - 1.4.0-1
- Update to latest upstream release
- Add a check section (upstream added a test suite)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.3-2
- Rebuilt for Python 3.9

* Tue Feb 18 2020 Artur Iwicki <fedora@svgames.pl> - 1.3.3-1
- Update to latest upstream release
- Update the list of supported devices in package description

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Artur Iwicki <fedora@svgames.pl> - 1.3.2-1
- Update to latest upstream release
- Preserve timestamp for the man page

* Mon Nov 18 2019 Artur Iwicki <fedora@svgames.pl> - 1.3.0-1
- Update to latest upstream release

* Sun Nov 03 2019 Artur Iwicki <fedora@svgames.pl> - 1.3.0-0.1rc1
- Update to latest upstream release candidate

* Sat Sep 28 2019 Artur Iwicki <fedora@svgames.pl> - 1.2.0-1
- Update to latest upstream release
- Update the list of supported devices in package description

* Thu Sep 19 2019 Artur Iwicki <fedora@svgames.pl> - 1.2.0-0.7rc4
- Update to latest upstream release candidate

* Sun Sep 15 2019 Artur Iwicki <fedora@svgames.pl> - 1.2.0-0.6rc3
- Update to latest upstream release candidate

* Thu Sep 12 2019 Artur Iwicki <fedora@svgames.pl> - 1.2.0-0.5rc2
- Update to latest upstream release candidate
- Include the version+release number in "Requires: python3-liquidctl"

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-0.3rc1
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.2rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Artur Iwicki <fedora@svgames.pl> - 1.2.0-0.1rc1
- Update to latest upstream pre-release
- Don't mention NZXT in package summary (support for other manufacturers added)
- Put the list of supported devices in a macro

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 05 2019 Artur Iwicki <fedora@svgames.pl> - 1.1.0-2
- Mark the package as noarch
- Split off the python libs into a python3-liquidctl subpackage
- Fix typos in summary and description

* Fri Dec 28 2018 Artur Iwicki <fedora@svgames.pl> - 1.1.0-1
- Initial packaging
