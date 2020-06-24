Name:          qwtpolar
Version:       1.1.1
Release:       14%{?dist}
Summary:       Qwt/Qt Polar Plot Library
License:       LGPLv2 with exceptions
URL:           http://qwtpolar.sourceforge.net
Source0:       http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2

# use system qt_install paths
Patch0:        qwtpolar-1.1.1-qt_install_paths.patch
# add pkgconfig support
Patch1:        qwtpolar-1.1.1-pkgconfig.patch
BuildRequires: qwt-devel

%description
The QwtPolar library contains classes for displaying values on a polar
coordinate system. It is an add-on package for the Qwt Library.

%package devel
Summary:        Development Libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the files necessary
to develop applications using QwtPolar.

%package doc
Summary:        Developer documentation for %{name}
BuildArch:      noarch

%description doc
This package contains developer documentation for QwtPolar.


%prep
%setup -q
%patch0 -p1 -b .qt_install_paths
%patch1 -p1 -b .pkgconfig

rm -rf doc/man
chmod 644 COPYING


%build
%{qmake_qt4}
make %{?_smp_mflags}


%install
make install INSTALL_ROOT=%{buildroot}

mv %{buildroot}/%{_qt4_docdir}/html/html \
   %{buildroot}/%{_qt4_docdir}/html/%{name}


%ldconfig_scriptlets


%files 
%doc COPYING CHANGES
%{_libdir}/libqwtpolar.so.1*
%{?_qt4_plugindir}/designer/libqwt_polar_designer_plugin.so

%files devel
%{_includedir}/qwt_polar*.h
%{_libdir}/libqwtpolar.so
%{_libdir}/pkgconfig/qwtpolar.pc
%{_qt4_libdir}/qt4/mkspecs/features/%{name}*

%files doc
%doc examples
# Own these to avoid needless dep on qt/qt-doc
%dir %{_qt4_docdir}
%dir %{_qt4_docdir}/html/
%{_qt4_docdir}/html/%{name}/


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> 1.1.1-5
- use %%qmake_qt4 macro

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.1-3
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 18 2015 Dave Johansen <davejohansen@gmail.com> 1.1.1-2
- Rebuild for gcc 5.0 C++ ABI change

* Tue Sep 23 2014 Volker Fröhlich <volker27@gmx.at> 1.1.1-1
- New upstream release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.4.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.3.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov 08 2013 Rex Dieter <rdieter@fedoraproject.org> 1.1.0-0.2.rc1
- qwtpolar-1.1.0-rc1

* Tue Oct 29 2013 Rex Dieter <rdieter@fedoraproject.org> 1.1.0-0.1.rc0
- qwtpolar-1.1.0-rc0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 18 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-1.1
- fix qreal != double assumptions (for arm)

* Sat Nov 24 2012 Volker Fröhlich <volker27@gmx.at> 1.0.1-1
- New upstream release
- Move designer plug-in to main package
- Split off doc sub-package
- Add isa macro to Requires of devel
- Make better use of qt macros

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 11 2011 Volker Fröhlich <volker27@gmx.at> 0.1.0-5
- Don't build with multiple workers

* Thu Jul 07 2011 Volker Fröhlich <volker27@gmx.at> 0.1.0-4
- Replace optimization on linker call and remove pthread link
- Explicit make call
- Produce proper developer documentation
- Drop defattr lines

* Mon Jun 06 2011 Volker Fröhlich <volker27@gmx.at> 0.1.0-3
- Removed waste word from description

* Sat May 21 2011 Volker Fröhlich <volker27@gmx.at> 0.1.0-2
- Use upstream's summary

* Sat May 21 2011 Volker Fröhlich <volker27@gmx.at> 0.1.0-1
- Initial packaging for Fedora
