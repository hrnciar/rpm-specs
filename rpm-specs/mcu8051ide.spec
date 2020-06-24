Name:           mcu8051ide
Version:        1.4.9
Release:        10%{?dist}
Summary:        IDE for MCS-51 based microcontrollers

License:        GPLv2+
URL:            http://mcu8051ide.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  cmake tk-devel tkimg tcllib bwidget rxvt-unicode
BuildRequires:  itcl >= 3.4
BuildRequires:  tdom >= 0.8
BuildRequires:  desktop-file-utils
Requires:       electronics-menu
Requires:       tkimg itcl tdom tcllib bwidget rxvt-unicode sdcc tclx

%description
Integrated Development Enviroment for some MCS-51 based microcontrollers 
(e.g. AT89S8253). Supported languages are assembly and C.

%prep
%setup -q

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} .
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
desktop-file-install --vendor ""  \
--add-category "Electronics"      \
--delete-original                 \
--remove-category "Development"   \
--dir %{buildroot}%{_datadir}/applications/    \
%{buildroot}%{_datadir}/applications/%{name}.desktop

chmod 0755 `find %{buildroot} -name \*.tcl`

%files
%doc README ChangeLog LICENSE TODO
%doc demo/
%{_datadir}/%{name}/
%{_bindir}/%{name}
%{_datadir}/applications/mcu8051ide.desktop
%{_datadir}/man/man1/mcu8051ide.1.gz
%{_datadir}/pixmaps/mcu8051ide.png
%{_datadir}/mime/packages/application-x-mcu8051ide.xml
%{_datadir}/appdata/mcu8051ide.appdata.xml

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 23 2014 Jaromir Capik <jcapik@redhat.com> - 1.4.9-1
- Updating to 1.4.9 (#1152077)
- Cleaning the spec

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 1.4.7-5
- add/update mime scriptlet

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 29 2013 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> - 1.4.7-3
- Fix build with unversioned docdir using _pkgdocdir (#992217)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 15 2013 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> - 1.4.7-1
- Updated package to 1.4.7 upstream release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec  8 2012 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> - 1.4.6-1
- Updated package to 1.4.6 upstream release

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 30 2011 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> - 1.4.2-1
- Updated package to 1.4.2 upstream release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 09 2010 Shakthi Kannan <shakthimaan [AT] fedoraproject DOT org> - 1.3.11-1
- Updated package to 1.3.11 upstream release

* Tue Nov 16 2010 Shakthi Kannan <shakthimaan [AT] fedoraproject DOT org> - 1.3.10-1
- Updated package to 1.3.10 upstream release

* Fri Sep 24 2010 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.3.9-1
- Updated package to 1.3.9 upstream release

* Sat Sep 11 2010 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.3.8-1
- Updated package to 1.3.8 upstream release

* Mon Jun 14 2010 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.3.7-1
- Updated package to 1.3.7 upstream release

* Tue Apr 13 2010 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.3.5-1
- Updated package to 1.3.5 upstream release

* Tue Mar 30 2010 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.3.4-1
- Updated package to 1.3.4 upstream release

* Sun Nov 15 2009 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.3.3-1
- Updated package to 1.3.3 upstream release

* Sat Nov 07 2009 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.3-2
- Updated package to 1.3-2 upstream release

* Sun Oct 25 2009 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.3.1-1
- Updated package to 1.3.1-1 upstream release

* Mon Aug 24 2009 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.3-1
- Updated Release, Version
- Removed earlier patches that were applied in 1.2 upstream
- Re-applied mcu8051-1.1-desktop-exec-path-fix.patch
- Added tclx as Requires dependency

* Thu Aug 06 2009 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.2-1
- Updated Release, Version
- Removed earlier patches that have now been applied in 1.2 upstream
- Removed manual removal of lib/.tex* lib/.html files in setup stage
- Added patch to add shebang to lib/itcl.tcl script
- Added itcl, tdom explicit package dependency BuildRequires

* Tue Jun 09 2009 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.1-4
- Added Requires: sdcc

* Wed May 27 2009 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.1-3
- Added BuildArch: noarch
- Fixed rpmlint errors
- Make all tcl scripts as executable
- Added patch1 for install.sh spelling mistakes and using -p with cp
- Removed tcl-devel as tk-devel already depends on it

* Tue May 26 2009 Shakthi Kannan <shakthimaan [AT] gmail DOT com> - 1.1-2
- Packaged upstream 1.1 version
- Patch removes Path entry and fixes Exec entry in desktop file

* Wed May 20 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.1-1
- Initial Package
