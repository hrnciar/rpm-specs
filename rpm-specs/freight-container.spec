%global githash d1d03aff8ca6ce7244a5113892a7facfde40e369
%global shortcommit	%(c=%{githash}; echo ${c:0:7})

Name: freight-container
Version: 0
Release: 0.9.20180613git%{shortcommit}%{?dist}
Summary: RPM macro set and commands for creating containers using rpm-build/mock
BuildArch: noarch

License: GPLv3
URL: https://github.com/nhorman/freight
Source0: %url/archive/%{githash}/freight-%{shortcommit}.tar.gz

Requires: rpm rpm-build mock bash dnf	

%description
Freight is a small container creation utility that allows you to build container
filesystems that use Systemd as a control mechanism and rpm as a container
package format.

%prep
%autosetup -n %{name}-%{githash}

%build
# No op - no building to be done

%install
mkdir -p %{buildroot}%{rpmmacrodir}
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/%{_datadir}/freight/examples/specs/
mkdir -p %{buildroot}/%{_datadir}/freight/examples/mock/
mkdir -p %{buildroot}/%{_mandir}/man1/

install -m 0644 rpm_macros/macros.freight %{buildroot}%{rpmmacrodir}
install -m 0755 scripts/freight-cmd %{buildroot}/usr/bin/
install -m 0644 examples/specs/* %{buildroot}/%{_datadir}/freight/examples/specs
install -m 0644 examples/mock/* %{buildroot}/%{_datadir}/freight/examples/mock
install -m 0644 doc/freight-cmd.1 %{buildroot}/%{_mandir}/man1/

%files
%doc README.md
%license COPYING
%{_bindir}/freight-cmd
%dir %{_datadir}/freight
%dir %{_datadir}/freight/examples
%{_datadir}/freight/examples/*
%{_mandir}/man1/*
%{rpmmacrodir}/macros.freight



%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20180613gitd1d03af
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20180613gitd1d03af
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20180613gitd1d03af
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20180613gitd1d03af
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20180613gitd1d03af
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Neil Horman <nhorman@tuxdriver.com> - 0-0.4.20180613gitd1d03af.fc28
- Updating chagelog

* Mon Jun 25 2018 Neil Horman <nhorman@tuxdriver.com> - 0-0.3.20180613gitd1d03af.fc28
- updated name to not conflict in fedora 
- Added man page for freight-cmd

* Tue Jun 19 2018 Neil Horman <nhorman@tuxdriver.com> - 0-0.2.20180613gitc72ed55.fc28
- Update spec file in response to review comments

* Wed Jun 13 2018 Neil Horman <nhorman@tuxdriver.com> - 0-0.1.20180613git5348089.fc28
- initial creation
