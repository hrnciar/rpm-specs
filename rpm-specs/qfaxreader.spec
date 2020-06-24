Name:         qfaxreader
License:      GPLv2+
Version:      0.3.2
Release:      14%{dist}
Summary:      A multipage monochrome/color TIFF/FAX viewer
Source:       http://downloads.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Patch0:       libtiff3.patch
URL:          http://qfaxreader.sourceforge.net/
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libtiff-devel, gdbm-devel
%if  ( "0%{?dist}" >= "0.fc20" ) || ( "0%{?dist}" >= "0.el6" )
BuildRequires:  qt3-devel 
%else
BuildRequires:  qt-devel
%endif
BuildRequires:  desktop-file-utils
%if ( "0%{?dist}" >= "0.fc20" ) || ( "0%{?dist}" == "0.el7" )
BuildRequires:  cmake
%else
%if "0%{?dist}" <= "0.el6"
BuildRequires:  cmake28
%endif
%endif
Requires:     hicolor-icon-theme

%description
QFaxReader is a monochrome/color multipage .TIFF files
visualisation utility designed for viewing faxes.
   
Features:
* multi-page monochrome/color tiff/fax file support
* fullscreen mode
* correctly display fax images in any resolution
* an aliases database for replacing fax IDs with real names
* image transformation (left or right rotation, vertical flipping)
* image export into any format supported by the Qt installation
* auto-refresh and notification of new facsimiles
* a sidebar for easy directory navigation
* printing monocrome and color tiffs
* arbitrary scaling (normal/smooth)
* internationalization support
* CID support

%prep
%setup -q
#RHEL <=6 has libtiff v3 which works just fine
%patch0 -p1 -b .libtiff

%build
mkdir build
cd build

%if ( "0%{?dist}" >= "0.fc20" ) || ( "0%{?dist}" == "0.el7" )
%cmake .. -DQT_PREFIX_DIR=%{_libdir}/qt-3.3 -DQT_LIBRARY_DIR=%{_libdir}/qt-3.3/lib -DWITH_GDBM=ON
%else
%if "0%{?dist}" <= "0.el6"
%cmake28 .. -DQT_PREFIX_DIR=%{_libdir}/qt-3.3 -DQT_LIBRARY_DIR=%{_libdir}/qt-3.3/lib -DWITH_GDBM=ON
%endif
%endif
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} -C build

#mkdir -p %{buildroot}/%{_datadir}/applications
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/16x16/apps
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/22x22/apps
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps
#install -p -m 644 kde/qfaxreader.desktop %{buildroot}/%{_datadir}/applications
install -p -m 644 kde/icon-16.png %{buildroot}/%{_datadir}/icons/hicolor/16x16/apps/qfaxreader.png
install -p -m 644 kde/icon-22.png %{buildroot}/%{_datadir}/icons/hicolor/22x22/apps/qfaxreader.png
install -p -m 644 kde/icon-32.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/qfaxreader.png

desktop-file-install                                    \
%if 0%{?fedora} && 0%{?fedora} < 19
        --vendor "fedora"                               \
%else
%if 0%{?rhel} && 0%{?rhel} == 5
        --vendor "fedora"                               \
%endif
%endif
        --remove-category Application                   \
        --dir %{buildroot}/%{_datadir}/applications     \
        kde/qfaxreader.desktop

%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_datadir}/man/man1/*
%{_bindir}/*
%{_datadir}/icons/*/*/apps/*
%{_datadir}/applications/*


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.2-4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 11 2014 Manuel "lonely wolf" Wolfshant <wolfy@fedoraproject.org> - 0.3.2-2
- Cosmetic cleanup

* Mon Jun 09 2014 Manuel "lonely wolf" Wolfshant <wolfy@fedoraproject.org> - 0.3.2-1
- New upstream release; requires cmake 2.8
- Single spec for all RHEL and Fedora supported releases

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec 03 2013 Manuel "lonely wolf" Wolfshant <wolfy@fedoraproject.org> - 0.3.1-20
- Build with  "-Werror=format-security" flag

* Mon Aug 05 2013 Manuel "lonely wolf" Wolfshant <wolfy@fedoraproject.org> - 0.3.1-19
- Fix unversioned docdir

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 25 2013 manuel "lonely wolf" wolfshant <wolfy[AT]fedoraproject.org> - 0.3.1-18
- Remove dep. on perl-Carp, it was a perl bug ( #924938 )

* Sat Mar 23 2013 manuel "lonely wolf" wolfshant <wolfy[AT]fedoraproject.org> - 0.3.1-17
- Add support for newer autoconf and ARM64

* Fri Feb 22 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.1-16
- Remove --vendor from desktop-file-install https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-15.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-14.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-13.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-12.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-11.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-10.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Apr 01 2008 manuel "lonely wolf" wolfshant <wolfy[AT]fedoraproject.org> - 0.3.1-9.3
- the program does not build with qt4 yet

* Sat Feb 09 2008 manuel "lonely wolf" wolfshant <wolfy[AT]fedoraproject.org> - 0.3.1-9.2
- wrong date for previous changelog entry

* Fri Jan 04 2008 manuel "lonely wolf" wolfshant <wolfy[AT]fedoraproject.org> - 0.3.1-9.1
- rebuilt for gcc-4.3.0

* Fri Jan 04 2008 manuel wolfshant <wolfy[AT]fedoraproject.org> - 0.3.1-9
- As recommended by the software author, add patch fixing configure 
in order to make it compile with gcc-4.3.0

* Wed Aug 22 2007 manuel wolfshant <wolfy[AT]fedoraproject.org> - 0.3.1-8.1
- Rebuilt

* Tue Aug 14 2007 manuel wolfshant <wolfy[AT]fedoraproject.org> - 0.3.1-8
- License clarification

* Tue Jul 24 2007 manuel wolfshant <wolfy[AT]fedoraproject.org> - 0.3.1-7
- Parallel build, take two (yet another patch)

* Mon Jul 23 2007 manuel wolfshant <wolfy[AT]fedoraproject.org> - 0.3.1-6
- Adding automake as BR

* Mon Jul 23 2007 manuel wolfshant <wolfy[AT]fedoraproject.org> - 0.3.1-5
- More cleanup
- Reenable SMP

* Mon Jul 23 2007 manuel wolfshant <wolfy[AT]fedoraproject.org> - 0.3.1-4
- Spec file cleanup
- Disabled parallel build, it does not seem to work.

* Mon Jun 13 2007 manuel wolfshant <wolfy[AT]fedoraproject.org> - 0.3.1-3
- Removes the no longer valid application category at desktop-file-install time
rather than patch the file

* Mon Jun 11 2007 manuel wolfshant <wolfy[AT]fedoraproject.org> - 0.3.1-2
- Requires: hicolor-icon-theme
- Replaced some paths with macros
- Use gtk-update-icon-cache to show up installed icons in GNOME menus

* Mon May 28 2007 manuel wolfshant <wolfy[AT]fedoraproject.org> - 0.3.1-1
- Initial Fedora build based on the spec available on the application's website

