%define _legacy_common_support 1
%define tarver	251
%define snap    021118

Name:		gabedit
Summary:	GUI for computational chemistry
Version:	2.5.1
Release:	5%{?dist}
Source0:        https://sites.google.com/site/allouchear/Home/gabedit/download/GabeditSrc%{tarver}%{?snap:_%{snap}}.tar.gz
# fix csh shebang
Patch2:		%{name}-csh.patch
# fix bug #774594 and other crashes
Patch4:		%{name}-strlen.patch
URL:		http://gabedit.sourceforge.net/home.html
License:	MIT
BuildRequires:  gcc
BuildRequires:	desktop-file-utils
BuildRequires:	gl2ps-devel >= 1.3.5
BuildRequires:	gtk2-devel
BuildRequires:	gtkglext-devel
BuildRequires:	libGLU-devel
BuildRequires:	libjpeg-devel
Requires:	hicolor-icon-theme

%description
Gabedit is a Graphical User Interface to Gamess-US, Gaussian, Molcas,
Molpro and MPQC computational chemistry packages. Gabedit includes
graphical facilities for generating keywords and options, molecule
specifications and their input sections for even the most advanced
calculation types. Gabedit includes an advanced Molecule Builder. You
can use it to rapidly sketch in molecules and examine them in three
dimensions. You can build molecules by atom, ring, group, amino acid and
nucleoside. You can also read geometry from a file. Most major molecular
file formats are supported.

%prep
%setup -q -n GabeditSrc%{tarver}%{?snap:_%{snap}}
%patch2 -p1
%patch4 -p1 -b .strlen
# remove Win32-specific files
rm -r utils/InnosSetupScriptWin32 utils/Others/gabedit64.bat
echo "external_gtkglarea=1" >> CONFIG
echo "external_gl2ps=1" >> CONFIG

pushd utils/Others
tr -d '\r' < isotopNIST.txt > isotopNIST.txt.unix && touch -r isotopNIST.txt isotopNIST.txt.unix && mv isotopNIST.txt.unix isotopNIST.txt
popd

%build
%{__make} %{?_smp_mflags} COMMONCFLAGS="$RPM_OPT_FLAGS -DENABLE_OMP -fopenmp -DDRAWGEOMGL -DENABLE_DEPRECATED"

%install
install -d %{buildroot}/%{_bindir}
install -pm755 %{name} %{buildroot}/%{_bindir}

install -d %{buildroot}%{_datadir}/applications
desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications \
	utils/Others/gabedit.desktop

for size in 16 24 32 48 ; do
	install -d %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps
	install -pm644 icons/Gabedit$size.png %{buildroot}/%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png
done

%files
%license License
%doc ChangeLog utils
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png

%changelog
* Sun Mar 29 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.5.1-5
- fix FTBS rhbz#1799382

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 04 2018 Dominik Mierzejewski <rpm@greysector.net> 2.5.1-1
- update to 2.5.1 (#1643659)
- drop redundant icon cache scriptlets

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 11 2017 Dominik Mierzejewski <rpm@greysector.net> 2.5.0-1
- update to 2.5.0 (#1469316)
- use https in Source URL
- drop obsolete defattr clause and use license macro

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb 16 2014 Dominik Mierzejewski <rpm@greysector.net> 2.4.8-1
- update to 2.4.8
- drop upstreamed patches
- drop obsolete specfile parts
- add missing Requires on hicolor-icon-theme for directory ownership

* Mon Oct 14 2013 Dominik Mierzejewski <rpm@greysector.net> 2.4.7-3
- drop the gtk patch and build with -DENABLE_DEPRECATED
- fix crashes when user doesn't select any folder in dialog

* Sun Oct 13 2013 Dominik Mierzejewski <rpm@greysector.net> 2.4.7-2
- drop some erroneous hunks from gtk patch

* Sat Oct 12 2013 Dominik Mierzejewski <rpm@greysector.net> 2.4.7-1
- updated to latest development version (2.4.7)
- rebased and updated -gtk patch
- fixed some compiler warnings (missing includes)
- attempt to fix bug #774594

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 08 2013 Jon Ciesla <limburgher@gmail.com> 2.4.6-2
- Drop desktop vendor tag.

* Mon Mar 25 2013 Dominik Mierzejewski <rpm@greysector.net> 2.4.6-1
- updated to latest development version (2.4.6)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 18 2012 Dominik Mierzejewski <rpm@greysector.net> 2.4.5-1
- updated to latest development version (2.4.5)
- dropped -ld patch (obsolete)
- rebased and updated -gtk patch

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 05 2011 Dominik Mierzejewski <rpm@greysector.net> 2.4.0-1
- updated to latest stable version (2.4.0)
- include 24px icon

* Mon Jul 18 2011 Dominik Mierzejewski <rpm@greysector.net> 2.3.9-1
- updated to latest development version (2.3.9)
- rebased patches

* Sun Mar 06 2011 Dominik Mierzejewski <rpm@greysector.net> 2.3.6-1
- updated to latest development version (2.3.6)
- rebased patches

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 21 2010 Dominik Mierzejewski <rpm@greysector.net> 2.3.2-1
- updated to latest development version (2.3.2)
- rebased gtk patch
- upstream switched from gtkglarea to gtkglext, adjust BRs

* Thu Aug 26 2010 Dominik Mierzejewski <rpm@greysector.net> 2.3.0-1
- updated to latest stable version (2.3.0)
- rebased gtk patch

* Mon May 24 2010 Dominik Mierzejewski <rpm@greysector.net> 2.2.12-1
- updated to latest development version (2.2.12)
- fixed build with gtk2-2.20 (replaced deprecated macro calls)
- fixed wrong end-of-line-encoding rpmlint warning

* Mon Feb 15 2010 Dominik Mierzejewski <rpm@greysector.net> 2.2.9-2
- fixed FTBFS with the new ld (rhbz#564993)

* Sat Jan 16 2010 Dominik Mierzejewski <rpm@greysector.net> 2.2.9-1
- updated to latest development version (2.2.9)

* Fri Aug 21 2009 Dominik Mierzejewski <rpm@greysector.net> 2.2.4-1
- updated to latest version (2.2.4)
- shortened the description field
- desktop file has been upstreamed

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Dominik Mierzejewski <rpm@greysector.net> 2.1.17-1
- updated to latest development version (2.1.17)
- dropped obsolete patches
- use new icon cache scriptlets

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep 25 2008 Dominik Mierzejewski <rpm@greysector.net> 2.1.8-1
- updated to latest stable version (2.1.8)
- fixed build with gtk2-2.14
- use system gl2ps

* Fri Jun 13 2008 Dominik Mierzejewski <rpm@greysector.net> 2.1.7-1
- updated to latest development version (2.1.7)
- dropped obsolete patches

* Mon May 19 2008 Dominik Mierzejewski <rpm@greysector.net> 2.1.4-2
- standardized SourceForge source URL
- made _smp_flags usage optional
- don't install bundled pre-built binaries
- don't install Win32-specific files
- use proper csh path in a script in utils

* Mon Apr 28 2008 Dominik Mierzejewski <rpm@greysector.net> 2.1.4-1
- adapted Mandriva specfile
- updated to 2.1.4
- patched to use system gtkglarea
