%global tilp_version 1.18

Name:           gfm
Version:        1.08
Release:        11%{?dist}
Summary:        Texas Instruments handheld(s) file manipulation program

License:        GPLv2+
URL:            https://sourceforge.net/projects/tilp/
Source0:        http://sourceforge.net/projects/tilp/files/tilp2-linux/tilp2-%{tilp_version}/%{name}-%{version}.tar.bz2

# This file was omitted from upstream gfm.
Source1:        https://raw.githubusercontent.com/debrouxl/tilp_and_gfm/1.18/gfm/trunk/acinclude.m4

BuildRequires:  gcc, gcc-c++
BuildRequires:  glib2-devel, pkgconfig, gtk2-devel, libglade2-devel,
BuildRequires:  groff, gettext, libXinerama-devel, libappstream-glib
BuildRequires:  desktop-file-utils, dconf, libticalcs2-devel, gettext

BuildRequires:  autoconf, automake, libtool, gettext-devel

%description
The GFM is an application allowing for the manipulation of
single/group/tigroup files from Texas Instruments handhelds.
It can create a new file, open an existing file, save file,
rename variables, remove variables, create folders, group files
into a group/tigroup file, and ungroup a group/tigroup file
into single files.

%prep
%setup -q
rm po/fr.gmo

cp %SOURCE1 .
autoreconf --force --install

# Sadly, we need to patch this locally.
sed 's/comical.desktop/gfm.desktop/' -i desktop/gfm.appdata.xml

%build
%configure --with-xinerama --disable-rpath
make %{?_smp_mflags}
make -C po fr.gmo
sed -i 's/\r$//' README

%install
make install DESTDIR=%{buildroot}
desktop-file-validate %{buildroot}%{_datadir}/applications/gfm.desktop
%find_lang %{name}
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

%files -f %{name}.lang
%{_bindir}/gfm
%{_mandir}/man1/gfm.1*
%{_datadir}/gfm/
%{_datadir}/applications/gfm.desktop
%{_datadir}/appdata/gfm.appdata.xml

%doc README AUTHORS ChangeLog
%license COPYING

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.18-2
- Fix appstream file to refer to the correct desktop file.

* Sat Nov 05 2016 Ben Rosser <rosser.bjr@gmail.com> 1.08-1
- Update to latest upstream release.

* Thu Feb 04 2016 Ben Rosser <rosser.bjr@gmail.com> 1.07-5
- Added dependency on groff for man-page generation.
- Changed files directive to include wildcard version of manpage.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 03 2015 'Ben Rosser' <rosser.bjr@gmail.com> 1.07-3
- Added patch to ship a png version of the gfm icon file.

* Tue Jul 14 2015 'Ben Rosser' <rosser.bjr@gmail.com> 1.07-2
- Added a French translation to the appdata file.
- Moved desktop-utils dependency to BuildRequires.
- Added dconf requires to silence a warning.

* Wed Jul 08 2015 'Ben Rosser' <rosser.bjr@gmail.com> 1.07-1
- Switched to using gettext and find_lang.
- Correctly flagged COPYING as a license file.
- Switched define to global macro.
- Added appdata XML file.
- Added update-desktop-database commands for the desktop file.
- Added --with-xinerama --disable-rpath options to the configure line.

* Sat Apr 20 2013 'Ben Rosser' <rosser.bjr@gmail.com> 1.07-0
- Updated to latest upstream tilp version

* Wed Sep 12 2012 'Ben Rosser' <rosser.bjr@gmail.com> 1.06-1
- Fixed spelling error in description

* Thu Jul 05 2012 'Ben Rosser' <rosser.bjr@gmail.com> 1.06-0
- Updated package to 1.06, vastly improved specfile

* Sat Jul 30 2011 'Ben Rosser' <rosser.bjr@gmail.com> 1.05-0
- Initial version of the package
