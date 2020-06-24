%global debug_package %{nil}

Name:		pinta
Version:	1.6
Release:	16%{?dist}
Summary:	An easy to use drawing and image editing program

# the code is licensed under the MIT license while the icons are licensed as CC-BY
License:	MIT and CC-BY
URL:		http://pinta-project.com/

Source0:	http://github.com/PintaProject/Pinta/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.appdata.xml

# Mono only available on these:
ExclusiveArch:	%mono_arches

BuildRequires:	gcc
BuildRequires:	mono-devel
BuildRequires:	mono-addins-devel
BuildRequires:	gtk-sharp2-devel
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib
Requires:	hicolor-icon-theme
Requires:	mono-addins

%description
Pinta is an image drawing/editing program.
It's goal is to provide a simplified alternative to GIMP for casual users.

%prep
%setup -q

chmod -x readme.md
chmod -x license-mit.txt
chmod -x license-pdn.txt
chmod -x xdg/pinta.1
chmod -x xdg/pinta.xpm
chmod -x xdg/scalable/pinta.svg

sed -i 's/\r//' readme.md
sed -i 's/\r//' license-mit.txt
sed -i 's/\r//' license-pdn.txt
sed -i 's/\r//' pinta.in
sed -i 's/\r//' xdg/pinta.xpm
sed -i 's/\r//' xdg/pinta.1
sed -i 's/\r//' xdg/scalable/pinta.svg

# update the project and solution files for mono4
find . -name "*.sln" -print -exec sed -i 's/Format Version 10.00/Format Version 11.00/g' {} \;
find . \( -name "*.csproj" -o -name "*.proj" \) -print -exec sed -i 's#ToolsVersion="3.5"#ToolsVersion="4.0"#g; s#<TargetFrameworkVersion>.*</TargetFrameworkVersion>##g; s#<PropertyGroup>#<PropertyGroup><TargetFrameworkVersion>v4.5</TargetFrameworkVersion>#g; s#Mono.Posix, Version.*"#Mono.Posix"#g' {} \;


%build
%configure
%make_build


%install
%make_install

# Validate desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# Install AppData file
install -d %{buildroot}%{_datadir}/metainfo
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%find_lang %name


%files -f %{name}.lang
%license license-mit.txt license-pdn.txt
%doc readme.md
%{_libdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*
%{_datadir}/man/man1/%{name}*
%{_datadir}/pixmaps/%{name}*

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 25 2019 Andrea Musuruane <musuruan@gmail.com> - 1.6-15
- Rebuilt (BZ #1755274)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Andrea Musuruane <musuruan@gmail.com> - 1.6-11
- Added gcc dependency
- Added license tag
- Used new AppData directory
- Removed obsolete scriptlets
- Spec file clean up

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-6
- mono rebuild for aarch64 support

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Timotheus Pokorra <tpokorra@fedoraproject.org> 1.6-3
- More fixes for mono4

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.6-2
- Rebuild (mono4)

* Sat Mar 28 2015 Andrea Musuruane <musuruan@gmail.com> - 1.6-1
- Updated to v1.6
- Minor cleanup

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.5-2
- Add an AppData file for the software center

* Mon Oct 27 2014 Andrea Musuruane <musuruan@gmail.com> 1.5-1
- Updated to v1.5
- Updated Source0 tag
- Dropped obsolete Group tags
- Pinta doesn't build on arm (#992798)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 07 2012 Paul Lange <palango@gmx.de> - 1.4-1
- Update to 1.4

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 30 2012 Paul Lange <palango@gmx.de> - 1.3-1
- update to 1.3

* Wed Apr 18 2012 Paul Lange <palango@gmx.de> - 1.2-1
- update to 1.2

* Sat Feb 18 2012 Paul Lange <palango@gmx.de> - 1.1-4
- correct path in bin/pinta

* Sat Feb 11 2012 Paul Lange <palango@gmx.de> - 1.1-3
- Update libdir

* Fri Feb 10 2012 Paul Lange <palango@gmx.de> - 1.1-2
- Add intltool to BuildRequires

* Fri Feb 10 2012 Paul Lange <palango@gmx.de> - 1.1-1
- Update to 1.1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Apr 28 2011 Paul Lange <palango@gmx.de> - 1.0-1
- Upload right sources

* Tue Apr 19 2011 Dan Horák <dan[at]danny.cz> - 0.8-2
- updated the supported arch list

* Wed Apr 06 2011 Paul Lange <palango@gmx.de> - 0.8-1
- Update to version 0.8

* Thu Mar 03 2011 Paul Lange <palango@gmx.de> - 0.7-1
- Update to version 0.7

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 12 2011 Paul Lange <palango@gmx.de> - 0.6-1
- Update to version 0.6

* Thu Dec 09 2010 Paul Lange <palango@gmx.de> - 0.5-6
- Upload right sources

* Thu Dec 09 2010 Paul Lange <palango@gmx.de> - 0.5-5
- Fix build for x86_64

* Wed Dec 08 2010 Paul Lange <palango@gmx.de> - 0.5-4
- Fix issues from review

* Sun Dec 05 2010 Paul Lange <palango@gmx.de> - 0.5-3
- Fix build for x86_64

* Wed Dec 01 2010 Paul Lange <palango@gmx.de> - 0.5-2
- Fix rpmlint warnings

* Sat Nov 20 2010 Paul Lange <palango@gmx.de> - 0.5-1
- update to version 0.5

* Sun Aug 01 2010 Paul Lange <palango@gmx.de> - 0.4-3
- Fix links in /bin
- Improve patch naming and add upstream links
- Fix mimetype patch

* Thu Jul 29 2010 Paul Lange <palango@gmx.de> - 0.4-2
- Fix icon cache handling
- Add some Requires and BuildRequires
- Add docs
- Add patches from debian

* Sat May 08 2010 Paul Lange <palango@gmx.de> - 0.4-1
- Initial packaging
