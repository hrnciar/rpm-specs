
Name:    lucene++
Summary: A high-performance, full-featured text search engine written in C++
Version: 3.0.7
Release: 24%{?dist}

License: ASL 2.0 or LGPLv3+
Url:     https://github.com/luceneplusplus/LucenePlusPlus
Source:  https://github.com/luceneplusplus/LucenePlusPlus/archive/rel_%{version}.tar.gz#/%{name}-%{version}.tar.gz

## upstream patches
Patch1: 0001-Fix-FSDirectory-sync-to-sync-writes-to-disk.patch
Patch2: 0002-minor-fix-to-allow-full-lines-to-be-input-to-demo-qu.patch
Patch5: 0005-Use-maxSize-of-BooleanQuery-as-base-for-the-queue-si.patch
Patch6: 0006-Fix-packageconfig-path.patch
Patch7: 0007-boost-1.58-variant.patch


BuildRequires: boost-devel
BuildRequires: cmake >= 2.8.6
BuildRequires: gcc-c++
BuildRequires: pkgconfig
BuildRequires: subversion

%description
An up to date C++ port of the popular Java Lucene library, a high-performance, full-featured text search engine.

%package devel
Summary: Development files for lucene++
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for lucene++, a high-performance, full-featured text search engine written in C++


%prep
%autosetup -p1 -n LucenePlusPlus-rel_%{version}


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%cmake .. \
  -DCMAKE_BUILD_TYPE:String="release"

%make_build lucene++ lucene++-contrib
popd


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%ldconfig_scriptlets

%files
%doc AUTHORS README* REQUESTS
%license COPYING APACHE.license GPL.license LGPL.license
%{_libdir}/liblucene++.so.0*
%{_libdir}/liblucene++.so.%{version}
%{_libdir}/liblucene++-contrib.so.0*
%{_libdir}/liblucene++-contrib.so.%{version}

%files devel
%{_includedir}/lucene++/
%{_libdir}/liblucene++.so
%{_libdir}/liblucene++-contrib.so
%{_libdir}/pkgconfig/liblucene++.pc
%{_libdir}/pkgconfig/liblucene++-contrib.pc


%changelog
* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 3.0.7-24
- Rebuilt for Boost 1.73

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 3.0.7-20
- Rebuilt for Boost 1.69

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.0.7-18
- BR: gcc-c++, use %%license %%make_build

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 3.0.7-16
- Rebuilt for Boost 1.66

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 3.0.7-13
- Rebuilt for s390x binutils bug

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 3.0.7-12
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 3.0.7-10
- Rebuilt for Boost 1.63

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 3.0.7-9
- Rebuilt for linker errors in boost (#1331983)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 3.0.7-7
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 3.0.7-6
- Rebuilt for Boost 1.59

* Wed Aug 05 2015 Jonathan Wakely <jwakely@redhat.com> 3.0.7-5
- Patch for changes to Boost.Variant in Boost 1.58

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 3.0.7-3
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Rex Dieter <rdieter@fedoraproject.org> 3.0.7-1
- 3.0.7

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 3.0.6-2
- Rebuild for boost 1.57.0

* Wed Nov 05 2014 Rex Dieter <rdieter@fedoraproject.org> 3.0.6-1
- fedora-ize opensuse .spec

* Sun Oct 19 2014 andreas.stieger@gmx.de
- fixes for .pc files in lucene++-3.0.6-pc_files_fix.patch
- add upstream patch lucene++-3.0.6-multiarch.patch to work with
  %%cmake makro
- fix build for openSUSE 12.3

* Sat Oct 18 2014 andreas.stieger@gmx.de
- lucene++ 3.0.6, a high-performance, full-featured text search
  engine written in C++,
- upstream patches:
  * lucene++-3.0.6-pc_files_fix.patch - fix pkgconfig files
  * lucene++-3.0.6-fix_installing_headers.patch fix header install
