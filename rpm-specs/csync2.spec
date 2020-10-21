Summary:        Cluster synchronization tool
Name:           csync2
Version:        1.34
Release:        27%{?dist}
License:        GPLv2+
URL:            http://oss.linbit.com/csync2/
Source0:        http://oss.linbit.com/csync2/%{name}-%{version}.tar.gz

Source1:        csync2-README.quickstart
Patch0:         csync2-fix-xinetd.patch
Patch1:         csync2-1.34-cfg.patch
Patch2:         0001-use-native-gnutls-drop-openssl-wrappers.patch
Patch3:         0001-don-t-hardcode-autofoo-version.patch
Patch4:         0001-Fix-gnutls-configure.ac-section.patch
Patch5:         0001-Fix-gnutls-Makefile.am-section.patch
Patch6:         csync2-1.34-librsync-1.0.0.patch

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  sqlite2-devel
BuildRequires:  gnutls-devel
BuildRequires:  librsync-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  openssl
BuildRequires:  byacc
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  libtasn1-devel

Requires:       xinetd


%description
Csync2 is a cluster synchronization tool. It can be used to keep files on
multiple hosts in a cluster in sync. Csync2 can handle complex setups with
much more than just 2 hosts, handle file deletions and can detect conflicts.
It is expedient for HA-clusters, HPC-clusters, COWs and server farms.

%prep
%setup -q
%patch0 -p1 -b .fix-xinetd
%patch1 -p1 -b .cfg
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1 -b .librsync-1.0.0
install -p -m 0644 %{SOURCE1} README.quickstart


%build
./autogen.sh
%configure --sysconfdir=%{_sysconfdir}/csync2
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_var}/lib/csync2
install -D -p -m 0644 csync2.xinetd %{buildroot}%{_sysconfdir}/xinetd.d/csync2

# We need these empty files to be able to %%ghost them
touch %{buildroot}%{_sysconfdir}/csync2/csync2_ssl_key.pem
touch %{buildroot}%{_sysconfdir}/csync2/csync2_ssl_cert.pem


%post
umask 077
if [ ! -f %{_sysconfdir}/csync2/csync2_ssl_key.pem ]; then
/usr/bin/openssl genrsa -rand /proc/apm:/proc/cpuinfo:/proc/dma:/proc/filesystems:/proc/interrupts:/proc/ioports:/proc/pci:/proc/rtc:/proc/uptime 1024 > %{_sysconfdir}/csync2/csync2_ssl_key.pem 2>/dev/null
fi

FQDN=`hostname`
if [ "x${FQDN}" = "x" ]; then
   FQDN=localhost.localdomain
fi

if [ ! -f %{_sysconfdir}/csync2/csync2_ssl_cert.pem ]; then
cat << EOF | /usr/bin/openssl req -new -key %{_sysconfdir}/csync2/csync2_ssl_key.pem -x509 -days 3000 -out %{_sysconfdir}/csync2/csync2_ssl_cert.pem 2>/dev/null
--
SomeState
SomeCity
SomeOrganization



EOF
fi

%preun
# Cleanup all databases upon last removal
if [ $1 -eq 0 ]; then
  %{__rm} -f %{_var}/lib/csync2/*
fi


%files
%doc README.quickstart paper.pdf
%dir %{_sysconfdir}/csync2/
%config(noreplace) %{_sysconfdir}/csync2/csync2.cfg
%config(noreplace) %{_sysconfdir}/xinetd.d/csync2
%ghost %config %{_sysconfdir}/csync2/csync2_ssl_key.pem
%ghost %config %{_sysconfdir}/csync2/csync2_ssl_cert.pem
%{_sbindir}/csync2
%{_sbindir}/csync2-compare
%{_mandir}/man1/csync2.1*
%dir %{_var}/lib/csync2/


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 03 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.34-18
- Spec clean up

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 01 2015 Robert Scheck <robert@fedoraproject.org> 1.34-15
- Rebuild for librsync 1.0.0 (#1126712)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 24 2012 Angus Salkeld <asalkeld@redhat.com> - 1.34-10
- Fix the gnutls ac_define (bz 849795)

* Mon Aug 20 2012  Simon Piette <piette.simon@gmail.com> - 1.34-9
- Fix the application of gnutls (bz 849795)
- Actually compiles gnutls in

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.34-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 16 2011 Angus Salkeld <asalkeld@redhat.com> - 1.34-6
- Cherry pick upstream commit that uses native gnutls and drops openssl wrapper
- Fix the discovery of the gnutils package

* Wed Nov 28 2007 Matthias Saou <http://freshrpms.net/> 1.34-5
- Include cfg patch to include pointers to local doc and better defaults.

* Tue Nov 13 2007 Matthias Saou <http://freshrpms.net/> 1.34-4
- Change configuration directory to be /etc/csync2/ since the program requires
  quite a few files, and putting all of them in /etc/ was messy.
- Include certificate generation upon package installation, based on mod_ssl.
- Rewrite the csync2-README.quickstart file.
- Remove db files upon last removal.

* Tue Nov 13 2007 Matthias Saou <http://freshrpms.net/> 1.34-1
- Take ownership of the package.
- Update to 1.34.

* Tue Mar 27 2007 <ruben@rubenkerkhof.com> 1.33-5
- Fix ownership of documentation directory (bz 233954)

* Thu Jan 25 2007 <ruben@rubenkerkhof.com> 1.33-4
- Included a README.fedora with instructions on how to create a self-signed
  certificate
- Included a mkcert.sh script to create a self-signed certificate
- Removed the creation of ssl certificate from the %%install section

* Mon Jan 22 2007 <ruben@rubenkerkhof.com> 1.33-3
- Fixed the xinetd file so there's no need to specify the port in /etc/services
- Create ssl certificates

* Mon Jan 22 2007 <ruben@rubenkerkhof.com> 1.33-2
- Some cleanups as per bz review 223633

* Sat Jan 20 2007 <ruben@rubenkerkhof.com> 1.33-1
- Initial import

