Name:           nftables
Version:        0.9.3
Release:        4%{?dist}
# Upstream released a 0.100 version, then 0.4. Need Epoch to get back on track.
Epoch:          1
Summary:        Netfilter Tables userspace utillites

License:        GPLv2
URL:            https://netfilter.org/projects/nftables/
Source0:        %{url}/files/%{name}-%{version}.tar.bz2
Source1:        nftables.service
Source2:        nftables.conf

# https://bugzilla.redhat.com/show_bug.cgi?id=1834853
Patch0:         nftables-fix_json_events.patch

#BuildRequires: autogen
#BuildRequires: autoconf
#BuildRequires: automake
#BuildRequires: libtool
BuildRequires:  gcc
BuildRequires: flex
BuildRequires: bison
BuildRequires: libmnl-devel
BuildRequires: gmp-devel
BuildRequires: readline-devel
BuildRequires: libnftnl-devel
BuildRequires: systemd
BuildRequires: asciidoc
BuildRequires: iptables-devel
BuildRequires: jansson-devel
BuildRequires: python3-devel

%description
Netfilter Tables userspace utilities.

%package        devel
Summary:        Development library for nftables / libnftables
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       pkgconfig

%description devel
Development tools and static libraries and header files for the libnftables library.

%package -n     python3-nftables
Summary:        Python module providing an interface to libnftables
Requires:       %{name} = %{epoch}:%{version}-%{release}
%{?python_provide:%python_provide python3-nftables}

%description -n python3-nftables
The nftables python module provides an interface to libnftables via ctypes.

%prep
%autosetup -p1

%build
#./autogen.sh
%configure --disable-silent-rules --with-xtables --with-json \
	--enable-python --with-python-bin=%{__python3}
make %{?_smp_mflags}

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Don't ship static lib (for now at least)
rm -f $RPM_BUILD_ROOT/%{_libdir}/libnftables.a

chmod 644 $RPM_BUILD_ROOT/%{_mandir}/man8/nft*

mkdir -p $RPM_BUILD_ROOT/%{_unitdir}
cp -a %{SOURCE1} $RPM_BUILD_ROOT/%{_unitdir}/

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig
cp -a %{SOURCE2} $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/
chmod 600 $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/nftables.conf

mkdir -m 700 -p $RPM_BUILD_ROOT/%{_sysconfdir}/nftables
chmod 600 $RPM_BUILD_ROOT/%{_sysconfdir}/nftables/*.nft
chmod 700 $RPM_BUILD_ROOT/%{_sysconfdir}/nftables

# make nftables.py use the real library file name
# to avoid nftables-devel package dependency
sofile=$(readlink $RPM_BUILD_ROOT/%{_libdir}/libnftables.so)
sed -i -e 's/\(sofile=\)".*"/\1"'$sofile'"/' \
	$RPM_BUILD_ROOT/%{python3_sitelib}/nftables/nftables.py

%post
%systemd_post nftables.service
%ldconfig_post

%preun
%systemd_preun nftables.service

%postun
%systemd_postun_with_restart nftables.service
%ldconfig_postun

%files
%license COPYING
%config(noreplace) %{_sysconfdir}/nftables/
%config(noreplace) %{_sysconfdir}/sysconfig/nftables.conf
%{_sbindir}/nft
%{_libdir}/libnftables.so.*
%{_mandir}/man5/libnftables-json.5*
%{_mandir}/man8/nft*
%{_unitdir}/nftables.service
%{_docdir}/nftables/examples/*.nft

%files devel
%{_libdir}/libnftables.so
%{_libdir}/pkgconfig/libnftables.pc
%{_includedir}/nftables/libnftables.h
%{_mandir}/man3/libnftables.3*

%files -n python3-nftables
%{python3_sitelib}/nftables-*.egg-info
%{python3_sitelib}/nftables/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:0.9.3-4
- Rebuilt for Python 3.9

* Fri May 15 2020 root <hobbes1069@gmail.com> - 1:0.9.3-3
- Add patch for json performance with ipsets, fixes RHBZ#1834853.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Phil Sutter <psutter@redhat.com> - 1:0.9.3-1
- Update to 0.9.3. Fixes bug #1778959

* Tue Oct 01 2019 Phil Sutter <psutter@redhat.com> - 1:0.9.2-3
- Drop unneeded docbook2X build dependency
- Add python3-nftables sub-package

* Fri Aug 23 2019 Kevin Fenzi <kevin@scrye.com> - 0.9.2-2
- Move libnftables section 3 man page to devel package.

* Fri Aug 23 2019 Kevin Fenzi <kevin@scrye.com> - 0.9.2-1
- Update to 0.9.2. Fixes bug #1743223

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Kevin Fenzi <kevin@scrye.com> - 0.9.1-2
- Add some filters to nftables.conf

* Tue Jun 25 2019 Kevin Fenzi <kevin@scrye.com> - 0.9.1-1
- Update to 0.9.1. Fixes bug #1723515

* Mon Jun 17 2019 Kevin Fenzi <kevin@scrye.com> - 0.9.0-7
- Rebuild for new libnftnl.

* Sat Mar 16 2019 Kevin Fenzi <kevin@scrye.com> - 1:0.9.0-6
- Fix permissions. Bug #1685242

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:0.9.0-5
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 04 2018 Kevin Fenzi <kevin@scrye.com> - 0.9.0-3
- Fix config file to have correct include names. Fixes bug #1642103

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Kevin Fenzi <kevin@scrye.com> - 0.9.0-1
- Update to 0.9.0. Fixes bug #1589404

* Fri May 11 2018 Kevin Fenzi <kevin@scrye.com> - 0.8.5-1
- Update to 0.8.5. Fixes bug #1576802

* Sun May 06 2018 Kevin Fenzi <kevin@scrye.com> - 0.8.4-2
- Fix devel package to require the Epoch too.
- Fix libraries split

* Fri May 04 2018 Kevin Fenzi <kevin@scrye.com> - 0.8.4-1
- Update to 0.8.4. Fixes bug #1574096

* Sat Mar 03 2018 Kevin Fenzi <kevin@scrye.com> - 0.8.3-1
- Update to 0.8.3. Fixes bug #1551207

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Kevin Fenzi <kevin@scrye.com> - 0.8.2-1
- Update to 0.8.2. Fixes bug #1541582

* Tue Jan 16 2018 Kevin Fenzi <kevin@scrye.com> - 0.8.1-1
- Update to 0.8.1. Fixes bug #1534982

* Sun Oct 22 2017 Kevin Fenzi <kevin@scrye.com> - 0.8-1
- Update to 0.8. 

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1:0.7-2
- Rebuild for readline 7.x

* Thu Dec 22 2016 Kevin Fenzi <kevin@scrye.com> - 0.7-1
- Update to 0.7

* Fri Jul 15 2016 Kevin Fenzi <kevin@scrye.com> - 0.6-2
- Rebuild for new glibc symbols

* Thu Jun 02 2016 Kevin Fenzi <kevin@scrye.com> - 0.6-1
- Update to 0.6.

* Sun Apr 10 2016 Kevin Fenzi <kevin@scrye.com> - 0.5-4
- Add example config files and move config to /etc/sysconfig. Fixes bug #1313936

* Fri Mar 25 2016 Kevin Fenzi <kevin@scrye.com> - 0.5-3
- Add systemd unit file. Fixes bug #1313936

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 17 2015 Kevin Fenzi <kevin@scrye.com> 0.5-1
- Update to 0.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 10 2015 Kevin Fenzi <kevin@scrye.com> 0.4-2
- Add patch to fix nft -f dep gen.

* Fri Dec 26 2014 Kevin Fenzi <kevin@scrye.com> 0.4-1
- Update to 0.4
- Add Epoch to fix versioning. 

* Wed Sep 03 2014 Kevin Fenzi <kevin@scrye.com> 0.100-4.20140903git
- Update to 20140903 snapshot

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.100-4.20140704git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 04 2014 Kevin Fenzi <kevin@scrye.com> 0.100-3.20140704git
- Update to new snapshot

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.100-2.20140426git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 26 2014 Kevin Fenzi <kevin@scrye.com> 0.100-1.20140426git
- Update t0 20140426

* Sun Mar 30 2014 Kevin Fenzi <kevin@scrye.com> 0.100-1.20140330git
- Update to 20140330 snapshot
- Sync versions to be post 0.100 release.

* Wed Mar 26 2014 Kevin Fenzi <kevin@scrye.com> 0-0.7.20140326git
- Update to 20140326 snapshot
- Fix permissions on man pages. 

* Mon Mar 24 2014 Kevin Fenzi <kevin@scrye.com> 0-0.6.20140324git
- Update to 20140324 snapshot

* Fri Mar 07 2014 Kevin Fenzi <kevin@scrye.com> 0-0.5.20140307git
- Update to 20140307

* Sat Jan 25 2014 Kevin Fenzi <kevin@scrye.com> 0-0.4.20140125git
- Update to 20140125 snapshot

* Sat Jan 18 2014 Kevin Fenzi <kevin@scrye.com> 0-0.3.20140118git
- Update to 20140118 snapshot
- Fixed License tag to be correct
- Fixed changelog
- nft scripts now use full path for nft
- Fixed man page building
- Dropped unneeded rm in install
- Patched build to not be silent. 

* Tue Dec 03 2013 Kevin Fenzi <kevin@scrye.com> 0-0.2.20131202git
- Use upstream snapshots for source.
- Use 0 for version. 

* Sat Nov 30 2013 Kevin Fenzi <kevin@scrye.com> 0-0.1
- initial version for Fedora review
