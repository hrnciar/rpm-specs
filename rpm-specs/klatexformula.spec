# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 1

%global _hardened_build 1
%global debug_package %{nil}

Name:             klatexformula
Version:          4.0.0
Release:          8%{?dist}
Summary:          Application for easy image creating from a LaTeX equation
License:          GPLv2+
URL:              http://klatexformula.sourceforge.net/
Source0:          http://downloads.sourceforge.net/klatexformula/%{name}-%{version}.tar.bz2
Patch0:           ftbfs_missing_include.patch
BuildRequires:    qt5-qtbase-devel
BuildRequires:    kf5-plasma-devel
BuildRequires:    qt5-qttools-static qt5-qtsvg-devel qt5-qtx11extras-devel
BuildRequires:    desktop-file-utils
BuildRequires:    doxygen
BuildRequires:    help2man
BuildRequires:    graphviz
Requires:         texlive-latex
Requires:         hicolor-icon-theme

%description
This application is especially designed for generating an image
(e.g. PNG) from a LaTeX equation, this using a nice GUI. Support
for Copy-Paste, Save as image/pdf/ps and drag-and-drop is included.
The program has two modes, shrinked and expanded mode. Shrinked
mode is straightforward, and expanded mode lets you to specify
a few options. You can use KLatexFormula in command-line mode
(eg. for scripts) by invoking klatexformula_cmdl executable.
Type klatexformula_cmdl --help for more information.

%package devel
Summary:          Development files for %{name}
Requires:         qt5-qtbase-devel
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n libklfbackend
Summary:          Library for integration KLatexFormula functionality

%description -n libklfbackend
This package includes the library KLFBackend to integrate
KLatexFormula functionality into your programs.

%package -n libklfbackend-devel
Summary:          Development files for libklfbackend
Requires:         qt5-qtbase-devel
Requires:         libklfbackend%{?_isa} = %{version}-%{release}

%description -n libklfbackend-devel
Development files for the libklfbackend.

%prep
%autosetup -p1

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} \
        -DCMAKE_SKIP_RPATH=ON \
        -DKLF_LIBKLFAPP_STATIC=OFF \
        -DKLF_LIBKLFBACKEND_STATIC=OFF \
        -DKLF_LIBKLFTOOLS_STATIC=OFF \
        -DKLF_INSTALL_POST_UPDATEMIMEDATABASE=OFF \
        -DKLF_INSTALL_SHARE_PIXMAPS_DIR="" \
        -DKLF_NO_CMU_FONT=ON \
        -DKLF_INSTALL_LIB_DIR=%{_libdir} \
        -DKLF_INSTALL_KLFTOOLSDESPLUGIN=YES \
        -DKLF_INSTALL_ICON_THEME=%{_datadir}/icons/hicolor/ \
        -DKLF_INSTALL_DESKTOP_CATEGORIES="Qt;Office;" \
        -DKLF_INSTALL_DESKTOP_ICON="%{name}" \
        -DKLF_INSTALL_DESPLUGIN_DIR=%{_qt5_plugindir}/designer/ \
        ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%ldconfig_scriptlets
%ldconfig_scriptlets -n libklfbackend

%files
%doc AUTHORS README
%license COPYING
%{_bindir}/%{name}*
%{_docdir}/%{name}/*
%{_libdir}/libklftools.so.*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/mime/packages/klatexformula-mime.xml
%{_mandir}/man1/klatexformula*
%{_qt5_plugindir}/designer/*.so

%files devel
%doc README
%{_libdir}/libklftools.so
%{_includedir}/klftools


%files -n libklfbackend
%doc AUTHORS README
%license COPYING
%{_libdir}/libklfbackend*.so.*

%files -n libklfbackend-devel
%doc README
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_includedir}/klfbackend
%{_includedir}/klftools

%changelog
* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 4.0.0-8
- cleanup qt5 deps (mostly replacing qt5-devel with qt5-qtbase-devel)
- tighten subpkg dep with %%{?_isa}

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 20 2018 Filipe Rosset <rosset.filipe@gmail.com> - 4.0.0-4
- added graphviz as BR

* Thu Sep 20 2018 Filipe Rosset <rosset.filipe@gmail.com> - 4.0.0-3
- Fix FTBFS rhbz #1604508 (thanks to Juhani Numminen)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 11 2018 Filipe Rosset <rosset.filipe@gmail.com> - 4.0.0-1
- New upstream release 4.0.0
- Build with qt5
- Spec cleanup / modernization
- Fixes rhbz #1136243 and rhbz #1423816

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.2.10-10
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.2.10-4
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Rex Dieter <rdieter@fedoraproject.org> 3.2.10-3
- minor .spec cleanup, update scriptlets

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 28 2014 Alexey Kurov <nucleo@fedoraproject.org> - 3.2.10-1
- klatexformula 3.2.10

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jun  4 2014 Alexey Kurov <nucleo@fedoraproject.org> - 3.2.9-2
- rebuild

* Thu May 15 2014 Filipe Rosset <rosset.filipe@gmail.com> - 3.2.9-1
- New upstream version 3.2.9 + spec cleanup
- Removed patches (already included in upstream)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan  5 2012 Alexey Kurov <nucleo@fedoraproject.org> - 3.2.3-4
- fix build with gcc-4.7.0

* Tue Apr 26 2011 Dan Horák <dan[at]danny.cz> - 3.2.3-3
- the buildsystem sets the proper 64/32-bit compile flags (fixes build on s390)

* Wed Apr 13 2011 Alexey Kurov <nucleo@fedoraproject.org> - 3.2.3-2
- require qt4 version used at build time

* Wed Apr 13 2011 Alexey Kurov <nucleo@fedoraproject.org> - 3.2.3-1
- update to 3.2.3

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec  4 2010 Alexey Kurov <nucleo@fedoraproject.org> - 3.2.2-1
- update to 3.2.2
- set KLF_NO_CMU_FONT for using system fonts by default
- BR: help2man

* Sun Oct 10 2010 Alexey Kurov <nucleo@fedoraproject.org> - 3.2.1-1
- update to 3.2.1

* Wed Sep 29 2010 Alexey Kurov <nucleo@fedoraproject.org> - 3.2.0-1
- update to 3.2.0
- added devel and ktexteditor-plugin subpackages

* Sun Nov 22 2009 Alexey Kurov <nucleo@fedoraproject.org> - 3.1.2-1
- update to 3.1.2

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May  5 2009 Alexey Kurov <nucleo@fedoraproject.org> - 3.0.1-3
- build with shared libraries
- fixed license tag
- libklfbackend subpackage
- fix build with GCC 4.4

* Mon May  4 2009 Alexey Kurov <nucleo@fedoraproject.org> - 3.0.1-2
- changed Requires to texlive-latex
- added Requires hicolor-icon-theme
- removed license tag in devel subpackage
- added Provides -static in devel subpackage

* Mon May  4 2009 Alexey Kurov <nucleo@fedoraproject.org> - 3.0.1-1
- Initial RPM release
