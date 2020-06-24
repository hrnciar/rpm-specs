
%{!?_licensedir:%global license %%doc}

Name:    libkdegames4
Summary: Common code and data for many KDE4 games
Version: 14.12.3
Release: 21%{?dist}

# libKF5KDEGames is LGPLv2, libKF5KDEGamesPrivate is GPLv2+
License: LGPLv2 and GPLv2+
URL:     https://projects.kde.org/projects/kde/kdegames/libkdegames
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/libkdegames-%{version}.tar.xz

BuildRequires: kdelibs4-devel >= 4.14
BuildRequires: pkgconfig(openal)
BuildRequires: pkgconfig(sndfile)

# Upgrade path for older versions
Obsoletes: kdegames-libs < 6:4.9.60
Provides:  kdegames-libs = 6:%{version}-%{release}
Provides:  kdegames-libs%{?_isa} = 6:%{version}-%{release}
%{?kdelibs4_requires}

# filter out qml modules
%filter_provides_in %{_kde4_libdir}/kde4/imports/org/kde
%filter_setup

%description
%{summary}.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: kdelibs4-devel
# # Upgrade path for older versions
Obsoletes: kdegames-devel < 6:4.9.60
Provides:  kdegames-devel = 6:%{version}-%{release}
Provides:  kdegames4-devel = %{version}-%{release}
%description devel
%{summary}.


%prep
%setup -q -n libkdegames-%{version}


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%ldconfig_scriptlets

%files
%doc README TODO
%license COPYING
%{_kde4_libdir}/libkdegames.so.6*
%{_kde4_libdir}/libkdegamesprivate.so.1*
%dir %{_kde4_libdir}/kde4/imports/org/
%dir %{_kde4_libdir}/kde4/imports/org/kde/
%{_kde4_libdir}/kde4/imports/org/kde/games/
%{_kde4_appsdir}/carddecks/
%{_kde4_appsdir}/kconf_update/kgthemeprovider-migration.upd

%files devel
%{_kde4_includedir}/*.h
%{_kde4_includedir}/highscore/
%{_kde4_includedir}/KDE/*
%{_kde4_includedir}/libkdegamesprivate/
%{_kde4_libdir}/cmake/KDEGames/
%{_kde4_libdir}/libkdegames.so
%{_kde4_libdir}/libkdegamesprivate.so


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 14.12.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 14.12.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 14.12.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 14.12.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 14.12.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 14.12.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 14.12.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 14.12.3-14
- Rebuild due to bug in RPM (RHBZ #1468476)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 14.12.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 14.12.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.12.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 16 2015 Rex Dieter <rdieter@fedoraproject.org> 14.12.3-10
- libkdegames4 compat pkg
