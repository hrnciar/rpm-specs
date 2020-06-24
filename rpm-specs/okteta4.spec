Name:    okteta4
Summary: Binary/hex editor for KDE4
Version: 4.14.3
Release: 65%{?dist}

License: GPLv2+ and GFDL
URL:     https://projects.kde.org/projects/kde/kdesdk/okteta
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/%{version}/src/okteta-%{version}.tar.xz

%global components core gui libs designer kasten parts

Patch1: okteta-4.14.3-no_fake_mimetypes.patch

BuildRequires: desktop-file-utils
BuildRequires: kdelibs4-devel >= 4.14
BuildRequires: pkgconfig(qca2)

%description
Okteta is a binary/hex editor for KDE

%package libs
Summary: Runtime libraries and kpart plugins for %{name}
Provides:  okteta4-part = %{version}-%{release}
Provides:  okteta4-part%{?_isa} = %{version}-%{release}
%description libs
%{summary}.

%package devel
Summary: Developer files for %{name}
Requires:  %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
%{summary}.


%prep
%setup -q -n okteta-%{version}

%patch1 -p1 -b .no_fake_mimetypes


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

for i in %{?components} ; do
make %{?_smp_mflags} -C %{_target_platform}/$i/
done


%install
for i in %{?components} ; do
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}/$i/
done

## unpackaged files
rm -fv %{buildroot}%{_kde4_bindir}/struct2osd.sh
# conflict with kf5 okteta
rm -fv %{buildroot}%{_kde4_datadir}/config.kcfg/structviewpreferences.kcfg


%ldconfig_scriptlets libs

%files libs
# libs
%dir %{_kde4_appsdir}/okteta/
%{_kde4_appsdir}/okteta/structures/
%{_kde4_datadir}/config/okteta-structures.knsrc
%{_kde4_libdir}/libkasten*.so.*
%{_kde4_libdir}/libokteta*.so.*
%{_kde4_libdir}/kde4/plugins/designer/oktetadesignerplugin.so
# part
%{_kde4_appsdir}/oktetapart/
%{_kde4_libdir}/kde4/oktetapart.so
%{_kde4_datadir}/kde4/services/oktetapart.desktop
%{_kde4_libdir}/kde4/libkbytearrayedit.so
%{_kde4_datadir}/kde4/services/kbytearrayedit.desktop

%files devel
%{_kde4_includedir}/KDE/Okteta*/
%{_kde4_includedir}/okteta*/
%{_kde4_libdir}/libokteta*.so
%{_kde4_includedir}/KDE/Kasten*/
%{_kde4_includedir}/kasten*/
%{_kde4_libdir}/libkasten*.so


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-64
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-63
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-61
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 28 2016 Rex Dieter <rdieter@fedoraproject.org> - 4.14.3-57
- oktetapart.desktop: s|all/allfiles|application/octet-stream|

* Wed May 11 2016 Rex Dieter <rdieter@fedoraproject.org> - 4.14.3-56
- -libs: omit %%{_datadir}/config.kcfg/structviewpreferences.kcfg (conflict with okteta-libs)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.3-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14.3-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.14.3-53
- Rebuilt for GCC 5 C++11 ABI change

* Mon Apr 06 2015 Rex Dieter <rdieter@fedoraproject.org> 4.14.3-52
- -libs: drop conflicting struct2osd.sh
- simplify packaging, remove most conditionals

* Sun Apr 05 2015 Rex Dieter <rdieter@fedoraproject.org> 4.14.3-51
- drop needless Obsoletes, fix struct2osd.sh permissions

* Wed Apr 01 2015 Rex Dieter <rdieter@fedoraproject.org> - 4.14.3-8
- drop -part subpkg (include in -libs)
- more prep for okteta4 compat pkg

* Tue Mar 31 2015 Rex Dieter <rdieter@fedoraproject.org> 4.14.3-7
- move struct2osd.sh to main pkg, use Recommends for its runtime deps

* Tue Mar 31 2015 Rex Dieter <rdieter@fedoraproject.org> - 4.14.3-6
- -part: move kbytearray here
- -libs: move kasten resources/structures here, drop dep on main pkg

* Tue Mar 31 2015 Rex Dieter <rdieter@fedoraproject.org> 4.14.3-5
- -devel: Provides: okteta4-devel

* Sat Mar 21 2015 Rex Dieter <rdieter@fedoraproject.org> 4.14.3-4
- -part subpkg, Provides: okteta4-part

* Sat Feb 28 2015 Rex Dieter <rdieter@fedoraproject.org> 4.14.3-3
- lack of algorithms in checksum tool (#1197339)

* Sat Jan 17 2015 Rex Dieter <rdieter@fedoraproject.org> 4.14.3-2
- kde-applications fixes, cleanup

* Sun Nov 09 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.3-1
- 4.14.3

* Sun Oct 12 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.2-1
- 4.14.2

* Tue Sep 16 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.1-1
- 4.14.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 15 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.0-1
- 4.14.0

* Tue Aug 05 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.97-1
- 4.13.97

* Tue Jul 15 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.3-1
- 4.13.3

* Thu Jul 03 2014 Rex Dieter <rdieter@fedoraproject.org> 4.13.2-2
- optimize mimeinfo scriptlet

* Mon Jun 09 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.2-1
- 4.13.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 11 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.1-1
- 4.13.1

* Sat Apr 12 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.0-1
- 4.13.0

* Fri Apr 04 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.97-1
- 4.12.97

* Sun Mar 23 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.95-1
- 4.12.95

* Wed Mar 19 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.90-1
- 4.12.90

* Sun Mar 02 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.3-1
- 4.12.3

* Fri Jan 31 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.2-1
- 4.12.2

* Fri Jan 10 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.1-1
- 4.12.1

* Thu Dec 19 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.12.0-1
- 4.12.0

* Sun Dec 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.97-1
- 4.11.97

* Thu Nov 21 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.95-1
- 4.11.95

* Sat Nov 16 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.90-1
- 4.11.90

* Sat Nov 02 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.3-1
- 4.11.3

* Sat Sep 28 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.2-1
- 4.11.2

* Wed Sep 04 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.1-1
- 4.11.1

* Thu Aug 08 2013 Than Ngo <than@redhat.com> - 4.11.0-1
- 4.11.0

* Wed Aug 07 2013 Jan Grulich <jgrulich@redhat.com> - 4.10.97-2
- Remove epoch
- Add obsoletion for kdesdk-okteta < 4.10.80

* Mon Aug 05 2013 Jan Grulich <jgrulich@redhat.com> - 4.10.97-1
- Split off from kdesdk package
