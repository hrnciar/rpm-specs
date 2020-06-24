Name:           tilp2
Version:        1.18
Release:        10%{?dist}
Summary:        Texas Instruments handheld(s) <-> PC communication program

License:        GPLv2+
URL:            https://sourceforge.net/projects/tilp/
Source0:        http://sourceforge.net/projects/tilp/files/tilp2-linux/%{name}-%{version}/%{name}-%{version}.tar.bz2

# This file was omitted from the release tarball of tilp2 1.18 by accident.
Source1:        https://raw.githubusercontent.com/debrouxl/tilp_and_gfm/1.18/tilp/trunk/acinclude.m4

BuildRequires:  gcc, gcc-c++
BuildRequires:  glib2-devel, pkgconfig, bison, flex, texinfo, groff, xdg-utils, gettext
BuildRequires:  gtk2-devel, SDL-devel, autoconf, automake, zlib-devel, libusb1, libticalcs2-devel
BuildRequires:  intltool, desktop-file-utils, libappstream-glib, dconf, libXinerama-devel
BuildRequires:  libarchive-devel, libglade2-devel

BuildRequires:  autoconf, automake, gettext-devel, libtool

%description
TiLP2 is a Texas Instruments handhelds <-> PC communication
program for Linux. It is able to use any type of link cable
(Gray/Black/Silver/Direct Link) with any calculator. See
http://lpg.ticalc.org/.

With TiLP, you can transfer files from your PC to your Texas
Instruments calculator, and vice-versa. You can also make a
screen dump, send/receive data, backup/restore contents,
install FLASH applications, or upgrade the  OS.

%prep
%setup -q

cp %SOURCE1 .
autoreconf --force --install

# Sadly, we need to patch this locally.
sed 's/comical.desktop/tilp.desktop/' -i desktop/tilp.appdata.xml

%build
%configure --disable-rpath --with-xinerama
make %{?_smp_mflags}
make -C po fr.gmo
sed -i 's/\r$//' README README.linux AUTHORS RELEASE

%install
make install DESTDIR=%{buildroot}
desktop-file-validate %{buildroot}%{_datadir}/applications/tilp.desktop
%find_lang %{name}
#mkdir -p %{buildroot}%{_datadir}/appdata
#install -p -m 644 %SOURCE1 %{buildroot}%{_datadir}/appdata/
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

%files -f %{name}.lang
%{_bindir}/tilp
%{_mandir}/man1/tilp.1.gz
%{_datadir}/tilp2/
%{_datadir}/applications/tilp.desktop
%{_datadir}/mime/packages/tilp.xml
%{_datadir}/appdata/tilp.appdata.xml

%doc README README.linux RELEASE NEWS AUTHORS ChangeLog
%license COPYING

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.18-2
- Fix appstream file to refer to the correct desktop file.

* Fri Nov 04 2016 Ben Rosser <rosser.bjr@gmail.com> - 1.18-1
- Update to latest upstream release, with support for newer calculators like the 84+CE.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 08 2015 'Ben Rosser' <rosser.bjr@gmail.com> 1.17-4
- Updated desktop scriplets.

* Tue Sep 08 2015 'Ben Rosser' <rosser.bjr@gmail.com> 1.17-3
- Provided patch (that is going upstream also) to remove AC_PROG_LIBTOOL in favor of LT_INIT.
- Added scriplets to update the desktop database.
- Switched to using "cp -p" to install files manually.

* Sun Aug 30 2015 'Ben Rosser' <rosser.bjr@gmail.com> 1.17-2
- Updated appstream appdata file with French translations.
- Changed tilp2 desktop file to use a PNG icon for appdata.

* Tue Jul 28 2015 'Ben Rosser' <rosser.bjr@gmail.com> 1.17-1
- Switched to using find_lang macro.
- Moved COPYING file to license tag.
- Fixed file line endings on documentation files.
- Added an appdata XML file.
- Added Xinerama dependency.

* Sat Apr 20 2013 'Ben Rosser' <rosser.bjr@gmail.com> 1.17-0
- Updated to latest upstream tilp version

* Wed Sep 12 2012 'Ben Rosser' <rosser.bjr@gmail.com> 1.16-1
- Fixed spelling errors in specfile

* Thu Jul 05 2012 'Ben Rosser' <rosser.bjr@gmail.com> 1.16-0
- Updated package to version 1.16
- Vastly improved specfile

* Sat Jul 30 2011 'Ben Rosser' <rosser.bjr@gmail.com> 1.15-0
- Initial version of the package
