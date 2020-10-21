%global _hardened_build 1

Name:		tayga
Version:	0.9.2
Release:	14%{?dist}
Summary:	Simple, no-fuss NAT64

License:	GPLv2+
URL:		http://www.litech.org/%{name}/
Source0:	http://www.litech.org/%{name}/%{name}-%{version}.tar.bz2

#		Patches are sent upstream. 
#		No issue tracker nor mailing list available
Patch0:		tayga-0.9.2_redhat_initscripts_and_systemd.patch
Patch1:		tayga-0.9.2_cflags_override.patch

Requires:	iproute

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	coreutils

%if 0%{?fedora} >= 18 || 0%{?rhel} >=7 
Requires(post):		systemd
Requires(preun):	systemd
BuildRequires:		systemd
%else
Requires(post):		initscripts
Requires(preun):	initscripts
%endif



%description
TAYGA is an out-of-kernel stateless NAT64 implementation for Linux that uses
the TUN driver to exchange IPv4 and IPv6 packets with the kernel. It is
intended to provide production-quality NAT64 service for networks where
dedicated NAT64 hardware would be overkill.


%prep
%setup -q
%patch0 -p1
%patch1 -p0


%build

# Some hardening on epel5,6
%if 0%{?rhel} == 5 || 0%{?rhel} == 6 
CFLAGS="%{optflags} -fPIE"
LDFLAGS="$LDFLAGS -Wl,-z,now" 
export CFLAGS
export LDFLAGS
%endif

%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"
echo %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mv %{buildroot}%{_sysconfdir}/%{name}.conf.example %{buildroot}%{_sysconfdir}/%{name}/default.conf
sed -i 's, /var/db/tayga, /var/lib/tayga/default,g;' %{buildroot}%{_sysconfdir}/%{name}/default.conf
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
install -p -D -m 0644 %{name}.service %{buildroot}%{_unitdir}/%{name}@.service
install -p -D -m 0644 tayga.tmpfilesd.conf %{buildroot}%{_tmpfilesdir}/%{name}.conf
%else
install -p -D -m 0755 tayga.initrc.redhat %{buildroot}%{_initrddir}/%{name}
install -d -m 0755 %{buildroot}%{_localstatedir}/run/%{name}
%endif


%post
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
%tmpfiles_create %{_tmpfilesdir}/tayga.conf
%else
/sbin/chkconfig --add tayga
%endif


%preun
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
%systemd_preun %{name}@.service
%else
/sbin/service %{name} stop > /dev/null 2>&1
/sbin/chkconfig --del %{name}
%endif


%files
%doc README README.redhat
%if 0%{?fedora} >= 22 || 0%{?rhel} >= 7
%license COPYING
%else
%doc COPYING
%endif
%config(noreplace) %{_sysconfdir}/%{name}/default.conf
%{_sbindir}/%{name}
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_sharedstatedir}/%{name}
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
%{_unitdir}/%{name}@.service
%{_tmpfilesdir}/tayga.conf
%else
%{_initrddir}/tayga
%attr(0755,root,root) %dir %{_localstatedir}/run/tayga
%endif


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar  8 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 0.9.2-11
- Remove obsolete requirement for %%postun scriptlet

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 0.9.2-3
- Added defattr tag for epel6
- Removed the example systemd service symlink
- Fixed "-fPIE" and "-Wl,-z,now" for epel-6-pp64
- Added buildroot macro for epel5
- No macro make_install on epel5
- Clean buildroot before install for epel5
- Added simple symlink instance support for epel
- Added a README.redhat describing how to create separate instances of tayga

* Wed Sep 30 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> 0.9.2-2
- Added simple cflags override patch
- Added _hardened_build macro for fedora
- Added hardening flags for el6, except on ppc64, where PIE fails
- Added some simple instance support in el6 init script
- Added explicit buildrequires for gcc, make, and coreutils

* Wed Sep 02 2015 Ingvar Hagelund <ingvar@redpill-linpro.com> 0.9.2-1
- First wrap of tayga for Fedora, including sysvinit and systemd start scripts
