Name:           usbtop
Version:        1.0
Release:        4%{?dist}
Summary:        Utility to show USB bandwidth
License:        BSD
URL:            https://github.com/aguinet/usbtop
Source0:        %{url}/archive/release-%{version}/usbtop-%{version}.tar.gz

BuildRequires:  systemd-rpm-macros
BuildRequires:  make
BuildRequires:  cmake >= 2.8
BuildRequires:  gcc-c++
BuildRequires:  libpcap-devel
BuildRequires:  boost-devel >= 1.48.0


%description
usbtop is a top-like utility that shows an estimated instantaneous bandwidth on
USB buses and devices.


%prep
%autosetup -n usbtop-release-%{version}
rm -rf third-party


%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build


%install
%cmake_install
install -d %{buildroot}%{_modulesloaddir}
echo usbmon > %{buildroot}%{_modulesloaddir}/usbtop.conf


%post
modprobe usbmon &> /dev/null || :


%files
%license LICENSE
%doc README.md CHANGELOG
%{_sbindir}/usbtop
%{_modulesloaddir}/usbtop.conf


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 04 2019 Carl George <carl@george.computer> - 1.0-2
- BuildRequires systemd-rpm-macros and use %%_modulesloaddir
- Use %%autosetup

* Tue Sep 03 2019 Carl George <carl@george.computer> - 1.0-1
- Initial package rhbz#1748678
