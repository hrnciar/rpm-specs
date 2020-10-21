Name:           collada-dom
Version:        2.5.0
Release:        13%{?dist}
Summary:        COLLADA Document Object Model Library

License:        MIT
URL:            http://www.collada.org

Source0:        https://github.com/rdiankov/collada-dom/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         collada-dom.include-zlib.patch

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  libxml2-devel
BuildRequires:  minizip-devel
BuildRequires:  pcre-devel
BuildRequires:  zlib-devel

%description
COLLADA is a royalty-free XML schema that enables digital asset exchange
within the interactive 3D industry. The COLLADA Document Object Model
(COLLADA DOM) is an application programming interface (API) that provides
a C++ object representation of a COLLADA XML instance document.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}-%{version}
rm -rf dom/external-libs
dos2unix README.rst
dos2unix licenses/dom_license_e.txt
dos2unix licenses/license_e.txt


%build
%cmake -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON
%cmake_build


%install
%cmake_install

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
mv $RPM_BUILD_ROOT%{_libdir}/cmake/collada_dom-* $RPM_BUILD_ROOT%{_libdir}/cmake/collada_dom


%files
%doc README.rst licenses/dom_license_e.txt licenses/license_e.txt
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/collada_dom/


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 2.5.0-11
- Rebuilt for Boost 1.73

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 23 2019 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 2.5.0-8
- Remove dependency on minizip-compat (#1632171)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 2.5.0-6
- Rebuilt for Boost 1.69

* Tue Sep 04 2018 Pavel Raiskup <praiskup@redhat.com> - 2.5.0-5
- rebuild for new compat BR (rhbz#1609830, rhbz#1615381)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 2.5.0-2
- Rebuilt for Boost 1.66

* Sat Oct 21 2017 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 2.5.0-1
- Update to 2.5.0

* Sun Aug 06 2017 Björn Esser <besser82@fedoraproject.org> - 2.4.4-10
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 2.4.4-7
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 2.4.4-5
- Rebuilt for Boost 1.63

* Wed Feb 24 2016 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 2.4.4-4
- Add patch to build with GCC6 (type conversion fix)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 2.4.4-2
- Rebuilt for Boost 1.60

* Fri Oct 23 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 2.4.4-1
- Update to upstream version 2.4.4
- Switch from git snapshot to github tar release
- Remove upstreamed patches

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2.4.3-11
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 2.4.3-9
- Rebuild for boost 1.58.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 2.4.3-7
- Add patch to fix incorrect cmake paths
- Use CMAKE_SKIP_INSTALL_RPATH instead of CMAKE_SKIP_RPATH

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.4.3-6
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 2.4.3-5
- Rebuild for boost 1.57.0

* Fri Jan 16 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 2.4.3-4
- add patch to fix typos in pkgconfig file

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jun 05 2014 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 2.4.3-1
- Update to 2.4.3 release

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 2.4.2-4
- Rebuild for boost 1.55.0

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 2.4.2-3
- rebuild for boost 1.55.0

* Tue Mar 11 2014 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 2.4.2-2
- Change Source URL following https://fedoraproject.org/wiki/Packaging:SourceURL?rd=Packaging/SourceURL#Github

* Tue Mar 11 2014 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 2.4.2-1
- Update to 2.4.2 release

* Sun Jan 19 2014 Tim Niemueller <tim@niemueller.de> - 2.4.0-2
- Fix hardcoded path

* Sun Jan 19 2014 Tim Niemueller <tim@niemueller.de> - 2.4.0-1
- Update to 2.4.0 release
  (Patch provided by Till Hofmann, bz #1049997)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 2.3.1-9
- Rebuild for boost 1.54.0

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 2.3.1-8
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 2.3.1-7
- Rebuild for Boost-1.53.0

* Sun Aug 12 2012 Kevin Fenzi <kevin@scrye.com> - 2.3.1-6
- Rebuild for new boost

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 2.3.1-4
- Rebuild against PCRE 8.30

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 04 2011 Tim Niemueller <tim@niemueller.de> - 2.3.1-2
- Rebuild for new Boost version

* Thu Jul 21 2011 Tim Niemueller <tim@niemueller.de> - 2.3.1-1
- Update to 2.3.1

* Wed Apr 06 2011 Tim Niemueller <tim@niemueller.de> - 2.3-3
- Rebuild for new Boost version

* Fri Mar 25 2011 Tim Niemueller <tim@niemueller.de> - 2.3-2
- Use now-official tarball from project
- Drop upstreamed patch

* Mon Mar 21 2011 Tim Niemueller <tim@niemueller.de> - 2.3-1
- Initial package

