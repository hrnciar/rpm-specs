%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:          gspiceui
Version:       1.1.00
Release:       4%{?dist}
Summary:       A frontend to Spice circuit similators

License:       GPLv2+
URL:           http://sourceforge.net/projects/gspiceui
Source0:       http://downloads.sourceforge.net/%{name}/%{name}-v%{version}.tar.gz
Source1:       %{name}.desktop
Source2:       %{name}-32x32.xpm


BuildRequires:  gcc-c++
BuildRequires: compat-wxGTK3-gtk2-devel desktop-file-utils
Requires:      ngspice geda-gnetlist geda-gschem
Requires:      electronics-menu
#Requires:      gwave

ExcludeArch:   ppc64

%description
GspiceUI is listed among the Fedora Electronic Lab (FEL) packages.

GNU Spice GUI is intended to provide a GUI to freely available
Spice electronic cicuit simulators eg.GnuCAP, Ng-Spice.
It uses gNetList to convert schematic files to net list files
and gWave to display simulation results.
gSchem is used as the schematic generation/viewing tool.

%prep
%setup -q -n %{name}-v%{version}

#wrong-file-end-of-line-encoding
sed -i 's/\r//' lib/*/*.mod

#spurious-executable-perm
chmod 0644 lib/*/*.mod
chmod 0644 sch/*/*.sch

reldocdir=$(echo %{_pkgdocdir} | sed -e 's|^%{_prefix}||')
sed -i "s|/share/gspiceui/html/gSpiceUI\.html|$reldocdir/gSpiceUI.html|g" src/main/HelpTasks.cpp

sed -i "s|/usr/X11R6/include|/usr/include/X11/|" src/Makefile

%build
%{__make} %{?_smp_mflags} CXXFLAGS="%{optflags} $(wx-config --cxxflags) -DNDEBUG" GSPICEUI_DBG=0 GSPICEUI_WXLIB=3.0


%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -pm 755 bin/%{name} %{buildroot}%{_bindir}/%{name}

install -d %{buildroot}%{_mandir}/man1/
install -pm 644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# Add/Manage desktop file
install -d %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -d %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -pm 0644 %{SOURCE2} \
    %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm
install -pm 0644 src/icons/%{name}-48x48.xpm \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.xpm

desktop-file-install --vendor "" \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE1}


#
# Adding gspiceui in the geda symbols directory structure
#

install -d %{buildroot}%{_datadir}/gEDA/sym/%{name}
cp -p lib/symbols/* %{buildroot}%{_datadir}/gEDA/sym/%{name}

#
# Creating a gafrc file which can automatically load those sym from the
# above directory structure
#
mkdir -p examples
cat > examples/gafrc << EOF
; gspiceui documentation symbols
(component-library "%{_datadir}/gEDA/sym/%{name}")
EOF


#
# Preparing examples
#
cp -pr lib/ examples
cp -pr sch/ examples

#
# Cleaning %%doc files
#
rm -f examples/*/Makefile
rm -rf examples/lib/sym





%files
%doc Authors License ReadMe ChangeLog ToDo
%doc examples html/gEDA-gSpiceUI.html
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/??x??/apps/*.xpm
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/gEDA/sym/%{name}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 08 2018 Scott Talbert <swt@techie.net> - 1.1.00-1
- New upstream release (#1217030) which fixes FTBFS (#1606894)
- Rebuild with wxWidgets 3.0 (GTK+ 2 build)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.98-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.98-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.98-20
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.98-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.98-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.98-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.98-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.98-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.98-14
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.98-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.98-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec  6 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.9.98-11
- Fix path to manual when doc dir is unversioned (#993809).
- Fix bogus date in %%changelog.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.98-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.98-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 27 2012 Adam Jackson <ajax@redhat.com> 0.9.98-8
- Rebuild for pangox removal

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.98-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.98-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 25 2011 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT com> - 0.9.98-5
- Commented Requires gwave

* Tue Oct 18 2011 Shakthi Kannan <shakthimaan@fedoraproject.org> - 0.9.98-4
- Added Requires gwave

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.98-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 0.9.98-2
- rebuilt against wxGTK-2.8.11-2

* Sun Oct 25 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT com> - 0.9.98-1
- Upstream Sources now includes missing opamp-3.sym
- upstream release 0.9.98

* Mon Sep 14 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT com> - 0.9.97-1
- New upstream release
- Added missing opamp-3.sym and corrected menu icon

* Thu Sep 03 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT com> - 0.9.65-6
- Fixes RHBZ #512076 - Build with wxGTK-devel not compat-wxGTK26-devel
- Added documentations: schematics and spice models

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.65-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.65-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 31 2008 Xavier Lamien <lxtnow[at]gmail.com> - 0.9.65-3
- Excluded ppc64 (gwave is not available on ppc64).

* Sat Jul 26 2008 Xavier Lamien <lxtnow[at]gmail.com> - 0.9.65-2
- Fix typo on desktop-file-install.

* Mon Jul 14 2008 Xavier Lamien <lxtnow[at]gmail.com> - 0.9.65-1
- Update release.

* Mon Dec 31 2007 Xavier Lamien < lxtnow[at]gmail.com > - 0.9.55-2
- Fixed typo in Requires.
- Improved %%description and desktop file.
- Fixed WxGTK config use.

* Sun Dec 30 2007 Xavier Lamien < lxtnow[at]gmail.com > - 0.9.55-1
- Updated Release.
- Built against WxGTK-2.6 libs.

* Wed Jul 04 2007 Xavier Lamien < lxtnow[at]gmail.com > - 0.8.90-2
- Enabled the fix that make it honor RPM_OPT_FLAGS.

* Wed Jul 04 2007 Xavier Lamien < lnxtnow[at]gmail.com > - 0.8.90-1
- Initial RPM Release.
