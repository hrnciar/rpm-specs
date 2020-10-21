Name:             tntnet
Version:          2.2.1
Release:          20%{?dist}
Summary:          A web application server for web applications
Epoch:            1

# GPLv2+: framework/common/gcryptinit.c
# zlib:   framework/common/unzip.h
License:          LGPLv2+ and GPLv2+ and zlib
URL:              http://www.tntnet.org/
Source0:          http://www.tntnet.org/download/%{name}-%{version}.tar.gz
# http://sourceforge.net/tracker/?func=detail&aid=3542704&group_id=119301&atid=684050
Source1:          %{name}.service
Patch0:           missing-call-to-setgroups-before-setuid.patch

BuildRequires:    gcc
BuildRequires:    gcc-c++
BuildRequires:    kernel-headers
BuildRequires:    openssl-devel
BuildRequires:    cxxtools-devel >= 2.2.1
BuildRequires:    perl-generators
BuildRequires:    zip
BuildRequires:    zlib-devel
BuildRequires:    systemd-units
Requires(pre):    shadow-utils
Requires(post):   systemd-units
Requires(preun):  systemd-units
Requires(postun): systemd-units

%description
%{summary}

%package          devel
Summary:          Development files for %{name}
Requires:         %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:         cxxtools-devel%{?_isa} >= 2.2.1

%description devel
Development files for %{name}

%prep
%setup -q
%patch0 -p0

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# Systemd unit files
# copy tntnet.service to unitdir /lib/systemd/system
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/
install -Dpm 644 %{SOURCE1} $RPM_BUILD_ROOT/%{_unitdir}/%{name}.service

# Find and remove all la files
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

# remove sysv init script
rm  $RPM_BUILD_ROOT/etc/init.d/%{name}

%check
utest/utest

%pre
getent group %{name} > /dev/null || groupadd -r %{name}
getent passwd %{name} > /dev/null || \
    useradd -r -g %{name} -d %{_localstatedir}/lib/%{name} -s /sbin/nologin \
    -c "User" %{name}
exit 0

%post
/sbin/ldconfig
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service
/sbin/ldconfig

%files
%doc AUTHORS ChangeLog README
%license COPYING
%dir %{_sysconfdir}/tntnet
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.xml
%{_unitdir}/%{name}.service
%{_bindir}/ecppc
%{_bindir}/ecppl
%{_bindir}/ecppll
%{_bindir}/tntnet
%{_libdir}/libtntnet*.so.*
%{_libdir}/tntnet/
%{_datadir}/tntnet/
%{_mandir}/man1/ecppc.1.gz
%{_mandir}/man1/ecppl.1.gz
%{_mandir}/man1/ecppll.1.gz
%{_mandir}/man1/tntnet-config.1.gz
%{_mandir}/man7/ecpp.7.gz
%{_mandir}/man7/tntnet.xml.7.gz
%{_mandir}/man7/tntnet.properties.7.gz
%{_mandir}/man8/tntnet.8.gz

%files devel
%{_bindir}/tntnet-config
%{_libdir}/libtntnet*.so
%{_includedir}/tnt/

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.1-16
- Fix FTBFS due missing BR gcc-c++ (RHBZ#1606528)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu May 12 2016 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.1-10
- Added missing-call-to-setgroups-before-setuid.patch
- Mark license files as %%license where available

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.1-8
- Added epoch for cxxtools-devel

* Thu Sep 24 2015 Martin Gansser <martinkg@fedoraproject.org> - 2.2.1-7
- Rebuilt
- added epoch to allow upgrade to older release

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.1-5
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Jan 25 2014 Ville Skyttä <ville.skytta@iki.fi> - 2.2.1-2
- Own the %%{_datadir}/tntnet dir.
- Run unit tests during build.

* Mon Jan 20 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.2.1-1
- New release

* Sun Sep 22 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 2.2-8
- Add missing dependency on cxxtools-devel in tntnet-devel (#896003).
- Add missing /sbin/ldconfig calls in %%post and %%postun.
- Using %%defattr is not needed anymore.

* Thu Aug 08 2013 Petr Pisar <ppisar@redhat.com> - 2.2-7
- Perl 5.18 rebuild

* Wed Aug 07 2013 Petr Pisar <ppisar@redhat.com> - 2.2-6
- Perl 5.18 rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 2.2-4
- Perl 5.18 rebuild

* Fri May 10 2013 Martin Gansser <martinkg@fedoraproject.org> - 2.2-3
- Corrected bogus date format in %%changelog
- Fixed typos in tntnet spec file
- Added minimal cxxtools version requirement

* Thu May 9 2013 Martin Gansser <martinkg@fedoraproject.org> - 2.2-2
- Corrected requirements
- Rebuild

* Fri May 3 2013 Martin Gansser <martinkg@fedoraproject.org> - 2.2-1
- New release
- Spec file cleanup

* Thu Aug 23 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-15
- Fixed typos in tntnet spec file

* Wed Aug 22 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-14
- Fix for "Introduce new systemd-rpm macros in tntnet spec file" (#850341)

* Thu Jul 26 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-13
- Added missing BuildRequires systemd-units 

* Thu Jul 26 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-12
- Spec file cleanup
- Changed changelog readability

* Wed Jul 18 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-11
- Added missing build requirement kernel-headers

* Fri Jul 13 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-10
- Added upstream link for gcc 4.7 patch
- Changed license type
- Make install preserve timestamps 

* Tue Jul 3 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-9
- Removed rm in install section
- Removed systemd readme file
- Added link to upstream systemd patch

* Sun Jun 24 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-8
- Removed group and user apache from tntnet.conf
- Added own group tntnet to tntnet.conf
- Added creation of users and groups in pre section

* Thu Jun 21 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-7
- Added systemd-fedora-readme

* Wed Jun 20 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-6
- Changed group and user for fedora to apache

* Sun Jun 17 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-5
- Fixed more missing slash in path
- Fixed missing system unit file

* Sun Jun 17 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-4
- Fixed missing slash in path

* Sat Jun 16 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-3
- Added gcc-4.7 patch
- Added systemd service file
- Removed sysv init stuff
- Cleanup spec file 

* Tue May 29 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-2
- Removed license comment
- Removed empty files
- Fixed Requires and Group tag

* Sun Apr 29 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-1
- New release

* Mon Sep 19 2011 Sebastian Vahl <fedora@deadbabylon.de> - 2.0-2
- Cleanup spec a bit

* Sun Sep 18 2011 Sebastian Vahl <fedora@deadbabylon.de> - 2.0-1
- Initial release
