
%global framework libktorrent

Name:    kf5-libktorrent
Summary: Library providing torrent downloading code
Version: 2.1.1
Release: 3%{?dist}

License: GPLv2+
URL:     https://cgit.kde.org/%{framework}.git/ 
%global revision %(echo %{version} | cut -d. -f3)
%if 0%{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
#global minmic %(echo %{version} | cut -d. -f2,3)
%global minmic 1.2
Source0: http://download.kde.org/%{stable}/ktorrent/5.%{minmic}/%{framework}-%{version}.tar.xz

## upstream patches

BuildRequires: boost-devel
BuildRequires: gettext
BuildRequires: gmp-devel >= 6.0.0
BuildRequires: libgcrypt-devel >= 1.4.5
BuildRequires: cmake(Qca-qt5)
BuildRequires: cmake(Qt5Network)

# kf5 deps
BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Solid)

%description
%{summary}.

%package devel
Summary: Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: boost-devel
# mse/bigint.h:#include <gmp.h>
Requires: gmp-devel%{?_isa}
Requires: libgcrypt-devel
Requires: cmake(KF5Archive)
Requires: cmake(KF5Config)
Requires: cmake(KF5KIO)
Requires: cmake(Qt5Network)
%description devel
%{summary}.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang libktorrent5

%ldconfig_scriptlets

%files -f libktorrent5.lang
%doc ChangeLog
%license COPYING
%{_kf5_libdir}/libKF5Torrent.so.6*

%files devel
%{_kf5_includedir}/libktorrent/
%{_kf5_libdir}/libKF5Torrent.so
%{_kf5_libdir}/cmake/KF5Torrent/


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Jeff Law <law@redhat.com> 2.1.1-2
- Drop reference to non-existent patch file

* Wed Sep 11 2019 Rex Dieter <rdieter@fedoraproject.org> 2.1.1-1
- 2.1.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.1-2
- pull in upstream fix

* Wed Nov 29 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.1-1
- 2.1

* Tue Aug 22 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.0.90-1
- 2.0.90

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 2.0.1-7
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.0.1-5
- Requires: kf5-filesystem
- update URL
- %%license COPYING

* Wed Oct 19 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.0.1-4
- use upstreamable gmp fix/workaround

* Wed Oct 19 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.0.1-3
- more upstream fixes

* Fri Jun 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.0.1-2
- pull in upstream fixes

* Fri Apr 22 2016 Rex Dieter <rdieter@fedoraproject.org> -  2.0.1-1
- libktorrent-2.0.1
