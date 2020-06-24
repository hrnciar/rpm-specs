Name:           cagibi
Summary:        SSDP (UPnP discovery) cache/proxy daemon
Version:        0.2.0
Release:        19%{?dist}

License:        GPLv2+ and LGPLv2+
URL:            http://www.kde.org/
Source0:        ftp://ftp.kde.org/pub/kde/stable/cagibi/%{name}-%{version}.tar.bz2

BuildRequires: automoc
BuildRequires: cmake
BuildRequires: pkgconfig(QtDBus)
BuildRequires: pkgconfig(QtNetwork)
BuildRequires: pkgconfig(QtXml)

%description
Cagibi is a cache/proxy daemon for SSDP (the discovery part of UPnP).


%prep
%setup -q


%build
mkdir %{_target_platform}
pushd %{_target_platform}
# disable copious debug output,  http://bugzilla.redhat.com/865964
export CXXFLAGS="%{optflags} -DQT_NO_DEBUG_OUTPUT"
%{cmake} ..
popd

%make_build  -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# unpackaged files
rm -f %{buildroot}%{_libdir}/pkgconfig/cagibi.pc


%files
%license COPYING COPYING.LIB
%config(noreplace) %{_sysconfdir}/cagibid.conf
%{_sysconfdir}/dbus-1/system.d/org.kde.Cagibi.conf
%{_bindir}/cagibid
%{_datadir}/dbus-1/interfaces/org.kde.Cagibi.*.xml
%{_datadir}/dbus-1/system-services/org.kde.Cagibi.service


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.2.0-16
- .spec cleanup

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.2.0-9
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 13 2012 Rex Dieter <rdieter@fedoraproject.org> - 0.2.0-4
- cagibi spams /var/logs/messages via dbus-daemon (#865964)
- pkgconfig-style deps

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 03 2011 Rex Dieter <rdieter@fedoraproject.org> 0.2.0-1
- 0.2.0

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 12 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.1.1-2
- omit pkgconfig file (for now)

* Tue Aug 10 2010 Jaroslav Reznik <jreznik@redhat.com> - 0.1.1-1
- Update to 0.1.1
- Added pkgconfig file

* Wed Aug 04 2010 Jaroslav Reznik <jreznik@redhat.com> - 0.1.0-2
- Fixed changelog entry
- COPYING.LIB in docs

* Wed Jul 28 2010 Jaroslav Reznik <jreznik@redhat.com> - 0.1.0-1
- Initial package
