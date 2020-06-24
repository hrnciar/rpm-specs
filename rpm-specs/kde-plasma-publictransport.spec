
%global snapshot 20111204git

Name:           kde-plasma-publictransport 
Version:        0.10
Release:        0.24.%{snapshot}%{?dist}
Summary:        Public Transport plasma applet

License:        GPLv2+ 
URL:            http://publictransport.horizon-host.com/
Source0:        publictransport_%{snapshot}.tar.gz

## upstreamable patches
# fix qreal != double assumptions, fixes FTBFS on arm
Patch50: publictransport-20111204git-qreal_arm.patch

BuildRequires:  desktop-file-utils
BuildRequires:  kdelibs4-devel >= 4.6.0
BuildRequires:  kdelibs4-webkit-devel
BuildRequires:  kde-workspace-devel

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       kde-runtime%{?_kde4_version: >= %{_kde4_version}}

%description
PublicTransport is a plasma applet that shows a departure/arrival board 
for a given stop. It can also show journeys to or from the given "home stop".

%package libs
Summary:        Runtime libraries and icons for %{name}
%description libs
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package -n timetablemate
Summary:        Little IDE for publictransport plasmoid accessors
License:        GPLv2+ 
Requires:       kwebkitpart
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description -n timetablemate
A little IDE to create new scripts for the publictransport
Plasma data engine that adds support for new service providers.

%prep
%setup -cq -n publictransport-%{snapshot}

%patch50 -p1 -b .qreal_arm


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} .. -DINSTALL_ALL=on
popd
make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%check
desktop-file-validate %{buildroot}%{_kde4_datadir}/applications/kde4/timetablemate.desktop


%ldconfig_scriptlets libs

%files
%{_kde4_appsdir}/plasma_engine_publictransport
%{_kde4_appsdir}/plasma_applet_graphicaltimetableline
%{_kde4_appsdir}/plasma_applet_publictransport

%{_kde4_libdir}/kde4/*.so

%{_kde4_datadir}/kde4/services/plasma-applet-graphicaltimetableline.desktop
%{_kde4_datadir}/kde4/services/plasma-applet-publictransport.desktop
%{_kde4_datadir}/kde4/services/plasma-engine-openstreetmap.desktop
%{_kde4_datadir}/kde4/services/plasma-engine-publictransport.desktop
%{_kde4_datadir}/kde4/services/plasma-runner-publictransport.desktop
%{_kde4_datadir}/kde4/services/plasma-runner-publictransport_config.desktop
%{_kde4_datadir}/kde4/services/publictransporthelper.desktop
%{_kde4_datadir}/kde4/services/plasma-applet-flights.desktop

%{_kde4_configdir}/publictransport.knsrc

%doc applet/{CHANGELOG,AUTHORS,COPYING} 

%files libs
%{_kde4_libdir}/libpublictransporthelper*
%{_kde4_iconsdir}/hicolor/*/*/*

%files devel
%{_kde4_includedir}/publictransporthelper

%files -n timetablemate
%{_bindir}/timetablemate
%{_sysconfdir}/dbus-1/system.d/org.kde.timetablemate.conf
%{_kde4_libexecdir}/timetablematehelper
%{_kde4_datadir}/applications/kde4/timetablemate.desktop
%{_kde4_datadir}/config.kcfg/timetablemate.kcfg
%{_kde4_datadir}/dbus-1/system-services/org.kde.timetablemate.service
%{_kde4_datadir}/polkit-1/actions/org.kde.timetablemate.policy
%{_kde4_appsdir}/timetablemate

%doc timetablemate/{AUTHORS,CHANGELOG,COPYING}



%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-0.24.20111204git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-0.23.20111204git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-0.22.20111204git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-0.21.20111204git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-0.20.20111204git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.10-0.19.20111204git
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-0.18.20111204git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-0.17.20111204git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-0.16.20111204git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-0.15.20111204git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-0.14.20111204git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.10-0.13.20111204git
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-0.12.20111204git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Rex Dieter <rdieter@fedoraproject.org> 0.10-0.11.20111204git
- .spec cleanup, BR: kdelibs4-webkit-devel

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-0.10.20111204git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-0.9.20111204git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-0.8.20111204git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 02 2012 Rex Dieter <rdieter@fedoraproject.org> 0.10-0.7.20111204git
- respin qreal_arm patch

* Fri Nov 02 2012 Rex Dieter <rdieter@fedoraproject.org> 0.10-0.6.20111204git
- fix FTBFS on arm

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-0.5.20111204git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 20 2012 Gregor Tätzner <brummbq@fedoraproject.org> - 0.10-0.4.20111204git
- fix icon scriptlets

* Wed Jan 18 2012 Gregor Tätzner <brummbq@fedoraproject.org> - 0.10-0.3.20111204git
- apply icon scriptlets to the libs subpackage

* Wed Dec 21 2011 Gregor Tätzner <brummbq@fedoraproject.org> - 0.10-0.2.20111204git
- Simplified Requirement Versioning and small fixes

* Tue Dec 13 2011 Gregor Tätzner <brummbq@fedoraproject.org> - 0.10-0.1.20111204git
- trivial fixes

* Sun Dec 04 2011 Gregor Tätzner <brummbq@fedoraproject.org> - 0.10-0.0.20111204git
- Initial package for Fedora

