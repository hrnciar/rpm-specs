
Name:    kf5-audiocd-kio
Summary: KF5 Audiocd kio slave
Version: 20.04.2
Release: 1%{?dist}

# code GPLv2+, handbook/docs GFDL
License: GPLv2+
URL:     https://www.kde.org/applications/multimedia/

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/audiocd-kio-%{version}.tar.xz

# cdparanoia-devel not on all arches for RHEL8.
%if 0%{?rhel} == 8
ExclusiveArch: x86_64 ppc64le aarch64 %{arm}
%endif

BuildRequires: cdparanoia-devel cdparanoia
BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros

BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5KIO)

%global majmin_ver %(echo %{version} | cut -d. -f1,2)
#BuildRequires: kf5-libkcddb-devel >= %{majmin_ver}
#BuildRequires: kf5-libkcompactdisc-devel >= %{majmin_ver}
BuildRequires: cmake(KF5Cddb)
BuildRequires: cmake(KF5CompactDisc)

BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(flac)
BuildRequires: pkgconfig(phonon4qt5)
BuildRequires: pkgconfig(theora)
BuildRequires: pkgconfig(vorbis)

Requires:  %{name}-doc = %{version}-%{release}

# when conflicting /usr/share/config.kcfg/audiocd_vorbis_encoder.kcfg was dropped
Conflicts: audiocd-kio < 16.08.3-10

# translations moved here
Conflicts: kde-l10n < 17.03

%description
%{summary}.

%package devel
Summary:  Development files for %{name}
# libaudiocdplugins.so symlink conflict
Conflicts: audiocd-kio-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package doc
Summary: Documentation for %{name}
License: GFDL
Requires:  %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.


%prep
%autosetup -n audiocd-kio-%{version}


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

%make_build -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang %{name} --all-name --with-man
%find_lang %{name}-doc --all-name --with-html --without-mo


%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING*
%{_kf5_datadir}/qlogging-categories5/*
%{_kf5_metainfodir}/org.kde.kio_audiocd.*.xml
%{_kf5_libdir}/libaudiocdplugins.so.5*
%{_qt5_plugindir}/libaudiocd_encoder_flac.so
%{_qt5_plugindir}/libaudiocd_encoder_lame.so
%{_qt5_plugindir}/libaudiocd_encoder_opus.so
%{_qt5_plugindir}/libaudiocd_encoder_vorbis.so
%{_qt5_plugindir}/libaudiocd_encoder_wav.so
%{_qt5_plugindir}/kcm_audiocd.so
%{_kf5_plugindir}/kio/audiocd.so
%{_kf5_datadir}/config.kcfg/audiocd_*_encoder.kcfg
%dir %{_kf5_datadir}/konqsidebartng/
%dir %{_kf5_datadir}/konqsidebartng/virtual_folders
%dir %{_kf5_datadir}/konqsidebartng/virtual_folders/services/
%{_kf5_datadir}/konqsidebartng/virtual_folders/services/audiocd.desktop
%{_kf5_datadir}/kservices5/audiocd.desktop
%{_kf5_datadir}/kservices5/audiocd.protocol
%{_kf5_datadir}/solid/actions/solid_audiocd.desktop

%files devel
%{_kf5_libdir}/libaudiocdplugins.so
%{_includedir}/audiocdencoder.h
%{_includedir}/audiocdplugins_export.h

%files doc -f %{name}-doc.lang
%license COPYING.DOC


%changelog
* Fri Jun 12 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.2-1
- 20.04.2

* Wed May 27 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.1-1
- 20.04.1

* Fri Apr 24 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.0-1
- 20.04.0

* Sat Mar 07 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.3-1
- 19.12.3

* Tue Feb 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.2-1
- 19.12.2

* Fri Jan 31 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.1-1
- 19.12.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.08.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.3-1
- 19.08.3

* Thu Oct 17 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.2-1
- 19.08.2

* Fri Oct 04 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.1-1
- 19.08.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.3-1
- 19.04.3

* Tue Jun 04 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.2-1
- 19.04.2

* Fri Mar 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.3-1
- 18.12.3

* Thu Mar 07 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.2-2
- Conflicts: audiocd-kio < 16.08.3-10

* Tue Feb 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.2-1
- 18.12.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.1-1
- 18.12.1

* Sun Dec 16 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.12.0-1
- 18.12.0

* Tue Nov 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.3-1
- 18.08.3

* Wed Oct 10 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.2-1
- 18.08.2

* Sun Sep 16 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.1-1
- 18.08.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.3-1
- 18.04.3

* Wed Jun 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.2-1
- 18.04.2

* Wed May 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.1-1
- 18.04.1

* Thu Apr 19 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.0-1
- 18.04.0

* Tue Mar 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.3-1
- 17.12.3

* Thu Feb 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.2-1
- 17.12.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.1-1
- 17.12.1

* Thu Dec 28 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.12.0-1
- 17.12.0

* Wed Nov 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.3-1
- 17.08.3

* Wed Oct 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.2-1
- 17.08.2

* Thu Sep 28 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.1-1
- 17.08.1

* Thu Aug 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.3-1
- 17.04.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.04.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.2-1
- 17.04.2

* Sun May 21 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.1-1
- 17.04.1

* Thu Mar 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.3-1
- 16.12.3

* Thu Feb 23 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.2-2
- Conflicts: audiocd-kio < 16.08.3-2

* Sun Feb 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.2-1
- 16.12.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.12.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 13 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.1-5
- BR: alsa

* Fri Jan 13 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.1-4
- fix typo (KF5KDELibs4Support)

* Fri Jan 13 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.1-3
- update build deps

* Fri Jan 13 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.1-2
- remove -libs reference from scriptlets

* Thu Jan 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.1-1
- audiocd-kio-16.12.1

