Name:		quazip
Version:	0.7.6
Release:	7%{?dist}
Summary:	Qt/C++ wrapper for the minizip library
License:	GPLv2+ or LGPLv2+
URL:		https://github.com/stachenov/quazip
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         quazip-0.7.6-fix_static.patch
Patch1:         quazip-0.7.6-install-right-prefix.patch
BuildRequires: 	cmake
BuildRequires: 	gcc-c++
BuildRequires:	qt4-devel
BuildRequires:	qt5-qtbase-devel
BuildRequires:	doxygen graphviz


%description
QuaZIP is a simple C++ wrapper over Gilles Vollant's ZIP/UNZIP package that
can be used to access ZIP archives. It uses Trolltech's Qt toolkit.

QuaZIP allows you to access files inside ZIP archives using QIODevice API,
and - yes! - that means that you can also use QTextStream, QDataStream or
whatever you would like to use on your zipped files.

QuaZIP provides complete abstraction of the ZIP/UNZIP API, for both reading
from and writing to ZIP archives.

%package devel
Summary:		Development files for %{name}
Requires:		%{name}%{?_isa} = %{version}-%{release}
Requires:		qt4-devel%{?_isa}
Requires:		zlib-devel%{?_isa}

%description devel
The %{name}-devel package contains libraries, header files and documentation
for developing applications that use %{name}. 

%package qt5
Summary: Qt5 wrapper for the minizip library
%description qt5
QuaZIP is a simple C++ wrapper over Gilles Vollant's ZIP/UNZIP package that
can be used to access ZIP archives. It uses Trolltech's Qt toolkit.

QuaZIP allows you to access files inside ZIP archives using QIODevice API,
and - yes! - that means that you can also use QTextStream, QDataStream or
whatever you would like to use on your zipped files.

QuaZIP provides complete abstraction of the ZIP/UNZIP API, for both reading
from and writing to ZIP archives.

%package qt5-devel
Summary:		Development files for %{name}
Requires:		%{name}-qt5%{?_isa} = %{version}-%{release}
Requires:               qt5-qtbase-devel%{?_isa}
Requires:               zlib-devel%{?_isa}

%description qt5-devel
The %{name}-devel package contains libraries, header files and documentation
for developing applications that use %{name}.


%prep
%autosetup -p1

%build
mkdir build-qt4
pushd build-qt4
%cmake .. -DBUILD_WITH_QT4:BOOL=ON

%make_build
popd

mkdir build-qt5
pushd build-qt5
%cmake .. -DBUILD_WITH_QT4:BOOL=OFF

%make_build
popd

doxygen Doxyfile
for file in doc/html/*; do
	touch -r Doxyfile $file
done

%install
make install/fast DESTDIR=%{buildroot} -C build-qt5
make install/fast DESTDIR=%{buildroot} -C build-qt4

%ldconfig_scriptlets

%files
%doc NEWS.txt README.md
%license COPYING
%{_libdir}/libquazip.so.1*

%files devel
%doc doc/html
%{_includedir}/quazip/
%{_libdir}/libquazip.so
%{_datadir}/cmake/Modules/FindQuaZip.cmake

%files qt5
%doc NEWS.txt README.md
%license COPYING
%{_libdir}/libquazip5.so.1*

%files qt5-devel
%doc doc/html
%{_includedir}/quazip5/
%{_libdir}/libquazip5.so
%{_datadir}/cmake/Modules/FindQuaZip5.cmake


%changelog
* Wed Mar 04 2020 Sandro Mani <manisandro@gmail.com> - 0.7.6-7
- Fix cmake module install path

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 21 2019 Felipe Borges <feborges@redhat.com> - 0.7.6-5
- Add patch to fix FindQuaZip.cmake install path

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 Nicolas Chauvet <kwizart@gmail.com> - 0.7.6-3
- Add zlib-devel - rhbz#1634468

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.7.6-1
- Update to 0.7.6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Nicolas Chauvet <kwizart@gmail.com> - 0.7.3-1
- Update to 0.7.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Apr 12 2016 Nicolas Chauvet <kwizart@gmail.com> - 0.7.2-1
- Update to 0.7.2
- Add patch to fix build with qt5 (disable static version)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 19 2015 Rex Dieter <rdieter@fedoraproject.org> 0.7.1-2
- quazip qt5 support (#1197484)

* Thu Jan 08 2015 Nicolas Chauvet <kwizart@gmail.com> - 0.7.1-1
- Update to 0.7.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 29 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.7-1
- Update to 0.7.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 12 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.6.2-1
- Update to 0.6.2

* Sun Jan 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.6.1-1
- Update to 0.6.1
- Clean spec file

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.5.1-1
- Update to 0.5.1

* Sun Sep 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.5-1
- Update to 0.5

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 16 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.4.4-1
- Update to 0.4.4

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 17 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.4.3-1
- Update to 0.4.3

* Fri Aug 19 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.4.2-1
- Update to 0.4.2
- Rebase ld patch

* Mon Jul 25 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.4.1-1
- Update to 0.4.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 24 2010 Chen Lei <supercyper@163.com> - 0.3-2
- add BR:graphviz for building apidocs

* Sat Jul 24 2010 Chen Lei <supercyper@163.com> - 0.3-1
- update to 0.3

* Wed Feb  3 2010 Chen Lei <supercyper@163.com> - 0.2.3-5
- quazip-devel must Requires minizip-devel

* Sun Jan 31 2010 Chen Lei <supercyper@163.com> - 0.2.3-4
- change license to GPLv2+ or LGPLv2+

* Sun Jan 31 2010 Chen Lei <supercyper@163.com> - 0.2.3-3
- use %%doc for packaging documentations

* Sun Jan 31 2010 Chen Lei <supercyper@163.com> - 0.2.3-2
- use system-wide minizip library

* Sun Jan 31 2010 Chen Lei <supercyper@163.com> - 0.2.3-1
- initial rpm build
