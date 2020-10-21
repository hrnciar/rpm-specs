Name:      storhaug
Summary:   High-Availability Add-on for NFS-Ganesha
Version:   1.0
Release:   6%{?prereltag:.%{prereltag}}%{?dist}
License:   GPLv2
URL:       https://github.com/gluster/storhaug
BuildArch: noarch
Obsoletes: storhaug-smb < 1.0
Source0:   https://github.com/gluster/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

Requires:  glusterfs-server
Requires:  ctdb

%description
High-Availability add-on for storage servers

### NFS (NFS-Ganesha)
%package nfs
Summary:   storhaug NFS-Ganesha module
Requires:  %{name} = %{version}-%{release}
Requires:  nfs-ganesha-gluster

%description nfs
High-Availability NFS add-on for NFS-Ganesha

%build

%prep
%setup -q -n %{name}-%{version}

%install
install -d -m 0755 %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_sysconfdir}/ctdb/nfs-checks-ganesha.d
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig/storhaug.d
install -m 0744 storhaug %{buildroot}%{_sbindir}/storhaug
install -m 0744 20.nfs-ganesha.check %{buildroot}%{_sysconfdir}/ctdb/nfs-checks-ganesha.d/
install -m 0744 nfs-ganesha-callout %{buildroot}%{_sysconfdir}/ctdb

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_sbindir}/storhaug
%dir %{_sysconfdir}/sysconfig/storhaug.d

%files nfs
%dir %{_sysconfdir}/ctdb/nfs-checks-ganesha.d
     %{_sysconfdir}/ctdb/nfs-checks-ganesha.d/20.nfs-ganesha.check
     %{_sysconfdir}/ctdb/nfs-ganesha-callout

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Kaleb S. KEITHLEY <kkeithle at redhat.com> 
- /etc/sysconfig/storhaug.d, Vendor

* Fri Jun 8 2018 Kaleb S. KEITHLEY <kkeithle at redhat.com> 1.0-1
- Reboot, Initial version
