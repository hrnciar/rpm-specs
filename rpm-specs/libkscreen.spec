Name:           libkscreen
Epoch:          1
Version:        1.0.5
Release:        17%{?dist}
Summary:        Display configuration library

License:        GPLv2+
URL:            https://quickgit.kde.org/?p=%{name}.git

Source0:        http://download.kde.org/stable/libkscreen/%{version}/src/libkscreen-%{version}.tar.xz

## upstreamable patches
# already fixed upstream (to 1.0.6 now)
Patch0: libkscreen-1.0.5-VERSION_RELEASE.patch

## upstream patches
Patch4: 0004-Fix-crash-in-XRandr1.1-backend.patch
Patch5: 0005-Avoid-target-name-collision.patch
Patch6: 0006-Fix-quoting-problems-with-D-depending-on-required-cm.patch
Patch7: 0007-Fix-building-apps-that-use-kscreen-and-which-fail-wi.patch

BuildRequires:  kdelibs4-devel
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(QJson) >= 0.8.1

%description
LibKScreen is a library that provides access to current configuration
of connected displays and ways to change the configuration.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
# add qsjon dep to account for:
# LibKScreenTargetsWithPrefix-release.cmake:  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "Qt4::QtCore;-lpthread;KDE4__kdecore;qjson"
Requires:       pkgconfig(QJson)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} .. 
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%check
# verify pkgconfig version
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion kscreen)" = "%{version}"


%ldconfig_scriptlets

%files
%doc COPYING
%{_kde4_libdir}/libkscreen.so.1*
%{_kde4_libdir}/kde4/plugins/kscreen/

%files devel
%{_kde4_includedir}/kscreen/
%{_kde4_libdir}/libkscreen.so
%{_kde4_libdir}/cmake/LibKScreen/
%{_kde4_libdir}/pkgconfig/kscreen.pc


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Apr 20 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.0.5-9
- rebuild (qt)

* Mon Apr 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.0.5-8
- update URL

* Mon Apr 18 2016 Rex Dieter <rdieter@fedoraproject.org> 1.0.5-7
- rebuild (qt)

* Sun Feb 14 2016 Rex Dieter <rdieter@fedoraproject.org> 1.0.5-6
- cleanup, pull in upstream fixes, FTBFS (#1307727)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1:1.0.5-3
- Rebuilt for GCC 5 C++11 ABI change

* Sat Nov 01 2014 Rex Dieter <rdieter@fedoraproject.org> 1.0.5-2
- pkgconfig-style deps, -devel: +Requires: pkgconfig(QJson)

* Fri Oct 31 2014 Rex Dieter <rdieter@fedoraproject.org> 1.0.5-1
- 1.0.5

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 15 2014 Rex Dieter <rdieter@fedoraproject.org> 1:1.0.4-2
- update URL

* Tue May 13 2014 Rex Dieter <rdieter@fedoraproject.org> 1:1.0.4-1
- 1.0.4

* Tue Apr 22 2014 Daniel Vrátil <dvratil@redhat.com> - 1:1.0.2-3
- backport upstream crash fix
- Resolves: rhbz#998395 rhbz#1004558 rhbz#1016769 rhbz#1023816

* Mon Nov 25 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:1.0.2-2
- backport pkgconfig fix (verify in %%check)
- track soname
- fix changelog date

* Wed Nov 20 2013 Dan Vrátil <dvratil@redhat.com> - 1:1.0.2-1
 - libkscreen 1.0.2

* Thu Aug 01 2013 Dan Vrátil <dvratil@redhat.com> - 1:1.0.1-1
 - libkscreen 1.0.1

* Mon Jun 17 2013 Dan Vrátil <dvratil@redhat.com> - 1:1.0-1
 - libkscreen 1.0

* Thu May 02 2013 Dan Vrátil <dvratil@redhat.com> - 1:0.0.92-1
 - libkscreen 0.0.92

* Tue Apr 23 2013 Dan Vrátil <dvratil@redhat.com> - 1:0.0.82.git20130423-1
 - dev git build

* Wed Mar 27 2013 Dan Vrátil <dvratil@redhat.com> - 1:0.0.81-1
 - libkscreen 0.0.81

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.0.71-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 20 2013 Dan Vrátil <dvratil@redhat.com> 1:0.0.71-2
 - fix dependency of libkscreen-devel
 
* Sun Jan 20 2013 Dan Vrátil <dvratil@redhat.com> 1:0.0.71-1
 - update to 0.0.71 - first official release
 - remove kscreen-console, it's now shipped in kscreen package
 
* Wed Jan 09 2013 Rex Dieter <rdieter@fedoraproject.org> 0.9.0-2.20121228git
- remove redundant BR's
- BR: qjson-devel >= 0.8.1
- fix dir ownership

* Fri Dec 28 2012 Dan Vrátil <dvratil@redhat.com> 0.9.0-1.20121228git
 - Fixed versioning
 - Added instructions how to retrieve sources
 - Fixed URL
 - Removed 'rm -rf $RPM_BUILD_ROOT'

* Wed Dec 26 2012 Dan Vrátil <dvratil@redhat.com> 20121226gitecc8d1a-1
 - Initial SPEC
