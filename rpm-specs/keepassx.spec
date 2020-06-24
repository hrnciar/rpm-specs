Name:           keepassx
Epoch:          1
Version:        2.0.3
Release:        10%{?dist}
Summary:        Cross-platform password manager
License:        GPLv2+
URL:            http://www.keepassx.org/
Source0: https://github.com/keepassx/keepassx/archive/%{version}.tar.gz#/keepassx-%{version}.tar.gz
BuildRequires:  qt-devel >= 4.6, libXtst-devel, desktop-file-utils, libgcrypt-devel, zlib-devel, cmake >= 2.6.4
BuildRequires:  gettext
Requires:       hicolor-icon-theme, qt >= 4.6

%description
KeePassX is an application for people with extremly high demands on secure
personal data management.
KeePassX saves many different information e.g. user names, passwords, urls,
attachemts and comments in one single database. For a better management
user-defined titles and icons can be specified for each single entry.
Furthermore the entries are sorted in groups, which are customizable as well.
The integrated search function allows to search in a single group or the
complete database.
KeePassX offers a little utility for secure password generation. The password
generator is very customizable, fast and easy to use. Especially someone who
generates passwords frequently will appreciate this feature.
The complete database is always encrypted either with AES (alias Rijndael) or
Twofish encryption algorithm using a 256 bit key. Therefore the saved
information can be considered as quite safe. KeePassX uses a database format
that is compatible with KeePass Password Safe v2 for MS Windows.

%prep
%setup -qn keepassx-%{version}

sed -i s/keepassx/keepassx2/g CMakeLists.txt
sed -i s/keepassx/keepassx2/g share/linux/keepassx.desktop

%build
%cmake .

%install
%make_install

# Associate KDB files
cat > x-keepass.desktop << EOF
[Desktop Entry]
Comment=
Hidden=false
Icon=keepassx2.png
MimeType=application/x-keepass
Patterns=*.kdb;*.KDB;*.kdbx;*.KDBX
Type=MimeType
EOF
install -D -m 644 -p x-keepass.desktop \
  %{buildroot}%{_datadir}/mimelnk/application/x-keepass2.desktop

mv %{buildroot}%{_datadir}/applications/keepassx.desktop %{buildroot}%{_datadir}/applications/keepassx2.desktop
mv %{buildroot}%{_datadir}/mime/packages/keepassx.xml %{buildroot}%{_datadir}/mime/packages/keepassx2.xml
# Rename icons
for icon in `ls %{buildroot}%{_datadir}/icons/hicolor/*/apps/keepassx.*`; do
    mv ${icon} `dirname ${icon}`/`basename ${icon} | sed -e s/keepassx/keepassx2/g`
done

sed -i s/Name=KeePassX/Name=KeePassX\ 2/g %{buildroot}%{_datadir}/applications/keepassx2.desktop

ln -s %{_bindir}/keepassx2 %{buildroot}/%{_bindir}/keepassx

%find_lang keepassx --with-qt

%check
ctest -V %{?_smp_mflags}
desktop-file-validate %{_datadir}/applications/keepassx2.desktop &> /dev/null || :

%files -f keepassx.lang
%doc README.md CHANGELOG
%license COPYING LICENSE.*
%{_bindir}/keepassx
%{_bindir}/keepassx2
%{_libdir}/keepassx2/libkeepassx*.so
%{_datadir}/keepassx2/icons
%{_datadir}/applications/*.desktop
%{_datadir}/mimelnk/application/*.desktop
%{_datadir}/mime/packages/*.xml
%{_datadir}/icons/hicolor/*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Aurelien Bompard <abompard@fedoraproject.org> - 1:2.0.3-2
- Fix icon size (#1398706)

* Wed Oct 12 2016 Jon Ciesla <limburgher@gmail.com> - 1:2.0.3-1
- 2.0.3

* Tue Jun 14 2016 Jon Ciesla <limburgher@gmail.com> - 1:2.0.2-3
- Update description, desktop file display name.

* Mon Jun 13 2016 Jon Ciesla <limburgher@gmail.com> - 1:2.0.2-2
- Add symlink for /usr/bin/keepassx

* Mon Apr 25 2016 Jon Ciesla <limburgher@gmail.com> - 1:2.0.2-1
- Move back to 2.0.2, FESCO 1569.

* Wed Apr 13 2016 Jon Ciesla <limburgher@gmail.com> - 1:0.4.4-1
- Revert to 0.4.x, incompatible db change.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 23 2015 Francesco Frassinelli <fraph24@gmail.com> - 2.0.0-1
- Version bump
  Project moved to GitHub

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4.3-12
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Rex Dieter <rdieter@fedoraproject.org> 0.4.3-11
- update mime scriptlets

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 12 2013 Jon Ciesla <limburgher@gmail.com> - 0.4.3-7
- Drop desktop vendor tag.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 30 2012 Tom Callaway <spot@fedoraproject.org> - 0.4.3-5
- fix FTBFS on gcc 4.7

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-4
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Mar 14 2010 Aurelien Bompard <abompard@fedoraproject.org> -  0.4.3-1
- version 0.4.3

* Sun Jan 03 2010 Aurelien Bompard <abompard@fedoraproject.org> -  0.4.1-1
- version 0.4.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 18 2009 Aurelien Bompard <abompard@fedoraproject.org> 0.4.0-2
- add patch0 to fix bug 496035

* Thu Mar 26 2009 Aurelien Bompard <abompard@fedoraproject.org> 0.4.0-1
- version 0.4.0
- drop patch0 (upstream)

* Thu Mar 12 2009 Aurelien Bompard <abompard@fedoraproject.org> 0.3.4-3
- backport fix from upstream for bug #489820

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Nov 11 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.3.4-1
- version 0.3.4

* Sat Aug 23 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.3.3-2
- rebase patch for version 0.3.3

* Tue Aug 12 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.3.3-1
- version 0.3.3

* Mon Jul 21 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.3.2-1
- version 0.3.2

* Sun Mar 16 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.3.1-1
- version 0.3.1
- drop xdg patch, keepassx now uses QDesktopServices

* Wed Mar 05 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.3.0-3.a
- version 0.3.0a

* Wed Mar 05 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.3.0-2
- patch for gcc 4.3

* Sun Mar 02 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.3.0-1
- version 0.3.0
- drop helpwindow patch (feature dropped upstream)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.2.2-5
- Autorebuild for GCC 4.3

* Sun Oct 07 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.2.2-4
- use xdg-open instead of htmlview

* Sat Aug 25 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.2.2-3
- fix license tag
- rebuild for BuildID

* Wed Jun 27 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.2.2-2
- fix help button
- use htmlview instead of the hardcoded konqueror

* Sun Mar 04 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.2.2-1
- initial package
