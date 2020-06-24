Name:       mbpfan
Version:    2.2.1
Release:    3%{?dist}
Summary:    A simple daemon to control fan speed on all MacBook/MacBook Pros
License:    GPLv3
URL:        https://github.com/linux-on-mac/mbpfan
Source0:    https://github.com/linux-on-mac/mbpfan/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros

ExclusiveArch:  x86_64

%description
This is an enhanced version of Allan McRae mbpfan

mbpfan is a daemon that uses input from coretemp module and sets the
fan speed using the applesmc module. This enhanced version assumes any
number of processors and fans (max. 10).

* It only uses the temperatures from the processors as input.
* It requires coretemp and applesmc kernel modules to be loaded.
* It requires root use
* It daemonizes or stays in foreground
* Verbose mode for both syslog and stdout
* Users can configure it using the file /etc/mbpfan.conf

%prep
%setup -q

%build
%set_build_flags
%make_build

%install
# Installing the binary
install -Dpm 0755 -t %{buildroot}%{_sbindir}/ bin/%{name}

# Installing the systemd service
install -Dpm 0644 -t %{buildroot}%{_unitdir}/ %{name}.service

# Installing the configuration file
install -Dpm 0644 -t %{buildroot}/etc/ %{name}.conf

# Installing the manual
install -Dpm 0644 -t %{buildroot}%{_mandir}/man8/ %{name}.8.gz

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service
%{_mandir}/man8/mbpfan.8.*
%config(noreplace) /etc/%{name}.conf
%doc README.md AUTHORS
%license COPYING

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 10 2019 Lyes Saadi <fedora@lyes.eu> - 2.2.1-2
- Improving the spec file, thanks to Robert-André Mauchin:
  - Adding Systemd scriptlets to automatically enable the mbpfan service.
  - Adding Fedora's build flags.
  - Ensuring that installed files are not executables.


* Sun Nov 24 2019 Lyes Saadi <fedora@lyes.eu> - 2.2.1-1
- Updating to 2.2.1.
- For additional information, see https://github.com/linux-on-mac/mbpfan/releases/tag/v2.2.1

* Sat Nov 09 2019 Lyes Saadi <fedora@lyes.eu> - 2.2.0-3
- Improving the spec file, thanks to Dominik 'Rathann' Mierzejewski.

* Fri Nov 01 2019 Lyes Saadi <fedora@lyes.eu> - 2.2.0-2
- Making the spec file compliant to Fedora Packaging Guidelines.
- Adding manpages.

* Fri Nov 01 2019 Lyes Saadi <fedora@lyes.eu> - 2.2.0-1
- Updating to 2.2.0.
- For additional information, see https://github.com/linux-on-mac/mbpfan/releases/tag/v2.2.0

* Fri Oct 04 2019 Lyes Saadi <fedora@lyes.eu> - 2.1.1-2
- Adding path for systemd.

* Thu Oct 03 2019 Lyes Saadi <fedora@lyes.eu> - 2.1.1-1
- Creating the spec file.
