Name:		  lxcfs
Version:	  4.0.4
Release:	  1%{?dist}
Summary:	  FUSE based filesystem for LXC
License:	  ASL 2.0
URL:		  https://linuxcontainers.org/lxcfs
Source0:	  https://linuxcontainers.org/downloads/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	  gcc
BuildRequires:	  gawk
BuildRequires:	  make
BuildRequires:	  fuse-devel
BuildRequires:	  help2man
BuildRequires:	  systemd
Requires(post):	  systemd
Requires(preun):  systemd
Requires(postun): systemd
# for /usr/share/lxc/config/common.conf.d:
Requires:	  lxc-templates


%description
LXCFS is a small FUSE filesystem written with the intention of making
Linux containers feel more like a virtual machine. It started as a
side-project of LXC but is usable by any runtime.

LXCFS will take care that the information provided by crucial files in
procfs are container aware such that the values displayed (e.g. in
/proc/uptime) really reflect how long the container is running and not
how long the host is running.


%prep
%autosetup


%build
%configure --with-init-script=systemd
make %{?_smp_mflags}


%install
%make_install SYSTEMD_UNIT_DIR=%{_unitdir}
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}


%post
%systemd_post %{name}.service


%preun
%systemd_preun %{name}.service


%postun
%systemd_postun %{name}.service


%files
%doc AUTHORS
# empty:
#doc ChangeLog NEWS README
%license COPYING
%{_bindir}/lxcfs
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/lib%{name}.so
%exclude %{_libdir}/%{name}/lib%{name}.la
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/lxc.mount.hook
%{_datadir}/%{name}/lxc.reboot.hook
%{_mandir}/man1/%{name}.1*
%{_unitdir}/%{name}.service
%{_datadir}/lxc/config/common.conf.d/00-lxcfs.conf
%dir %{_sharedstatedir}/%{name}


%changelog
* Sat Jun 20 2020 Thomas Moschny <thomas.moschny@gmx.de> - 4.0.4-1
- Update to 4.0.4.

* Fri Apr 24 2020 Thomas Moschny <thomas.moschny@gmx.de> - 4.0.3-1
- Update to 4.0.3.

* Fri Apr 10 2020 Thomas Moschny <thomas.moschny@gmx.de> - 4.0.2-1
- Update to 4.0.2.

* Sat Mar 21 2020 Thomas Moschny <thomas.moschny@gmx.de> - 4.0.1-1
- Update to 4.0.1.

* Sat Mar  7 2020 Thomas Moschny <thomas.moschny@gmx.de> - 4.0.0-1
- Update to 4.0.0.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 15 2019 Thomas Moschny <thomas.moschny@gmx.de> - 3.1.2-1
- Update to 3.1.2.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul  7 2019 Thomas Moschny <thomas.moschny@gmx.de> - 3.0.4-1
- Update to 3.0.4.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 23 2018 Thomas Moschny <thomas.moschny@gmx.de> - 3.0.3-2
- Explicitly set the init system in the configure step.

* Fri Nov 23 2018 Thomas Moschny <thomas.moschny@gmx.de> - 3.0.3-1
- Update to 3.0.3.

* Fri Aug 17 2018 Thomas Moschny <thomas.moschny@gmx.de> - 3.0.2-1
- Update to 3.0.2.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun  2 2018 Thomas Moschny <thomas.moschny@gmx.de> - 3.0.1-1
- Update to 3.0.1.

* Wed Apr  4 2018 Thomas Moschny <thomas.moschny@gmx.de> - 3.0.0-1
- New package.
