Name:           keepass
Version:        2.45
Release:        1%{?dist}
Summary:        Password manager

License:        GPLv2+
URL:            https://keepass.info/

# Created with, e.g.:
# version=2.32 tmpdir=`mktemp -d` && cd $tmpdir && curl -LRO https://downloads.sourceforge.net/project/keepass/KeePass%202.x/$version/KeePass-$version-Source.zip && curl -RO https://keepass.info/integrity/v2/KeePass-$version-Source.zip.asc && gpg2 --verify KeePass-$version-Source.zip.asc KeePass-$version-Source.zip && mkdir keepass-$version && unzip -d keepass-$version KeePass-$version-Source.zip && find keepass-$version -name "*dll" -delete && tar -cJf keepass-$version.tar.xz keepass-$version
Source0:        %{name}-%version.tar.xz
Source1:        %{name}.appdata.xml

# Upstream does not include a .desktop file, etc..
Patch0:         keepass-desktop-integration.patch

# Move XSL files to /usr/share/keepass:
Patch1:         keepass-fix-XSL-search-path.patch

ExclusiveArch:  %{mono_arches}
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  libgdiplus-devel
BuildRequires:  mono-devel
BuildRequires:  mono-winforms
BuildRequires:  mono-web
BuildRequires:  xorg-x11-server-Xvfb
Requires:       xdotool xsel hicolor-icon-theme
Requires:       mono-winforms
%if 0%{?fedora} >=24 || 0%{?rhel} >= 8
Recommends:     gtk2
Recommends:     libgcrypt
%endif


# The debuginfo package would be empty if created.
%global debug_package %{nil}


%description
KeePass is a free open source password manager, which helps you to
remember your passwords in a secure way. You can put all your passwords in
one database, which is locked with one master key or a key file.  You
only have to remember one single master password or select the key file
to unlock the whole database.


%prep
%autosetup -p1

# Work around libpng bug (https://bugzilla.redhat.com/show_bug.cgi?id=1276843):
find -name \*.png -print0 | xargs -0 mogrify -define png:format=png32


%build
( cd Build && sh PrepMonoDev.sh )
find . -name "*.sln" -print -exec sed -i 's/Format Version 10.00/Format Version 11.00/g' {} \;
xbuild /target:KeePass /property:TargetFrameworkVersion=v$(ls -d /usr/lib/mono/*-api | cut -d/ -f5 | cut -d- -f1 | sort -Vr | head -1) /property:Configuration=Release
for subdir in Images_App_HighRes Images_Client_16 Images_Client_HighRes; do
    xvfb-run -a mono Build/KeePass/Release/KeePass.exe -d:`pwd`/Ext/$subdir --makexspfile `pwd`/KeePass/Resources/Data/$subdir.bin
done
xbuild /target:KeePass /property:TargetFrameworkVersion=v$(ls -d /usr/lib/mono/*-api | cut -d/ -f5 | cut -d- -f1 | sort -Vr | head -1) /property:Configuration=Release

%install
install -d %{buildroot}/%{_prefix}/lib/%{name} %{buildroot}/%{_datadir}/%{name} %{buildroot}/%{_datadir}/%{name}/XSL %{buildroot}/%{_datadir}/applications %{buildroot}/%{_bindir} %{buildroot}/%{_datadir}/mime/packages %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps %{buildroot}/%{_datadir}/icons/hicolor/16x16/apps %{buildroot}/%{_mandir}/man1 %{buildroot}/%{_docdir}/%{name} %{buildroot}/%{_datadir}/appdata
install -p -m 0644 Build/KeePass/Release/KeePass.exe Ext/KeePass.config.xml Ext/KeePass.exe.config %{buildroot}/%{_prefix}/lib/%{name}
install -p -m 0644 Ext/XSL/KDBX_Common.xsl Ext/XSL/KDBX_DetailsFull_HTML.xsl Ext/XSL/KDBX_DetailsLight_HTML.xsl Ext/XSL/KDBX_PasswordsOnly_TXT.xsl Ext/XSL/KDBX_Tabular_HTML.xsl %{buildroot}/%{_datadir}/%{name}/XSL
install -p -m 0644 -T Ext/Icons_15_VA/KeePass_Round/KeePass_Round_512.png %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
install -p -m 0644 -T Ext/Icons_15_VA/KeePass_Round/KeePass_Round_256.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
install -p -m 0644 -T Ext/Icons_15_VA/KeePass_Round/KeePass_Round_128.png %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
install -p -m 0644 -T Ext/Icons_15_VA/KeePass_Round/KeePass_Round_64.png %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -p -m 0644 -T Ext/Icons_15_VA/KeePass_Round/KeePass_Round_48.png %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -p -m 0644 -T Ext/Icons_15_VA/KeePass_Round/KeePass_Round_32.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -p -m 0644 -T Ext/Icons_15_VA/KeePass_Round/KeePass_Round_16.png %{buildroot}/%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
desktop-file-install --dir=%{buildroot}/%{_datadir}/applications dist/%{name}.desktop
install -p -m 0644 dist/%{name}.xml %{buildroot}/%{_datadir}/mime/packages
install -p -m 0644 dist/%{name}.1 %{buildroot}/%{_mandir}/man1
install -p -m 0644 %{SOURCE1} %{buildroot}/%{_datadir}/appdata
install -p dist/%{name} %{buildroot}/%{_bindir}
sed 's/\r$//' Docs/History.txt > %{buildroot}/%{_docdir}/%{name}/History.txt
sed 's/\r$//' Docs/License.txt > %{buildroot}/%{_docdir}/%{name}/License.txt


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml


%files
%dir %{_docdir}
%doc %{_docdir}/%{name}/History.txt
%doc %{_docdir}/%{name}/License.txt
%{_bindir}/%{name}
%{_prefix}/lib/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_mandir}/man1/%{name}.1*
%{_datadir}/appdata/%{name}.appdata.xml


%changelog
* Sat May  9 2020 Peter Oliver <rpm@mavit.org.uk> - 2.45-1
- Update to version 2.45.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Peter Oliver <rpm@mavit.org.uk> - 2.44-1
- Update to version 2.44.

* Sun Sep 15 2019 Peter Oliver <rpm@mavit.org.uk> - 2.43-1
- Update to version 2.43.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.42.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May  7 2019 Peter Oliver <rpm@mavit.org.uk> - 2.42.1-2
- Always build against latest available Mono framework version.

* Tue May  7 2019 Peter Oliver <rpm@mavit.org.uk> - 2.42.1-1
- Update to version 2.42.1.

* Thu May  2 2019 Peter Oliver <rpm@mavit.org.uk> - 2.42-1
- Update to version 2.42.

* Mon Apr 29 2019 Peter Oliver <rpm@mavit.org.uk> - 2.41-3
- Build against framework version 4.7.1 for Mono 5.18.  Fixes #1680388.
- Require mono-winforms.  Works around #1700892.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 13 2019 Peter Oliver <rpm@mavit.org.uk> - 2.41-1
- Update to version 2.41.

* Thu Sep 20 2018 Peter Oliver <rpm@mavit.org.uk> - 2.40-1
- Update to version 2.40.
- Drop keepass-doc subpackage, since we need Python 2 to build it.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.39.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 13 2018 Peter Oliver <rpm@mavit.org.uk> - 2.39.1-1
- Update to version 2.39.1.

* Sun May  6 2018 Peter Oliver <rpm@mavit.org.uk> - 2.39-1
- Update to version 2.39.
- Suggest documentation.

* Mon Mar 19 2018 Vasiliy Glazov <vascom@fedoraproject.org> - 2.38-6
- Correct directory owning.

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.38-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.38-4
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Peter Oliver <rpm@mavit.org.uk> - 2.38-2
- Remove icon cache scriptlets, to keep up with latest packaging guidelines.

* Wed Jan 10 2018 Peter Oliver <rpm@mavit.org.uk> - 2.38-1
- Update to version 2.38.

* Sat Oct 14 2017 Peter Oliver <rpm@mavit.org.uk> - 2.37-1
- Update to version 2.37.
- Recommend gtk2 and libgcrypt packages (for theming and key derivation,
  respectively).

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Peter Oliver <rpm@mavit.org.uk> - 2.36-1
- Update to version 2.36.

* Tue Feb 21 2017 Peter Oliver <rpm@mavit.org.uk> - 2.35-3
- Workaround for crash when pressing Super key.  Fixes #1424852.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Peter Oliver <rpm@mavit.org.uk> - 2.35-1
- Update to 2.35.

* Sat Jan  7 2017 Peter Oliver <rpm@mavit.org.uk> - 2.34-3
- Validate appdata.

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.34-2
- mono rebuild for aarch64 support

* Sun Aug 28 2016 Peter Oliver <rpm@mavit.org.uk> - 2.34-1
- Update to version 2.34.

* Mon Aug 22 2016 Peter Oliver <rpm@mavit.org.uk> - 2.33-2
- Update AppStream XML.
- Remove scriptlets replaced by triggers in Fedora 24.
- Remove scriptlets replaced by triggers in Fedora 25.

* Sat May 21 2016 Peter Oliver <rpm@mavit.org.uk> - 2.33-1
- Update to version 2.33.

* Sat May 21 2016 Peter Oliver <rpm@mavit.org.uk> - 2.32-3
- Remove now-unneeded workaround for BOM-handling bug in grep.

* Thu Mar 10 2016 Peter Oliver <rpm@mavit.org.uk> - 2.32-2
- Update to version 2.32.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Peter Oliver <rpm@mavit.org.uk> - 2.31-1
- Update to version 2.31.

* Sun Jan 10 2016 Peter Oliver <rpm@mavit.org.uk> - 2.30-6
- Add keyword to .desktop file.

* Tue Jan  5 2016 Peter Oliver <rpm@mavit.org.uk> - 2.30-5
- Remove workaround for #1251756, which is now fixed.

* Sun Nov 22 2015 Peter Oliver <rpm@mavit.org.uk> - 2.30-4
- Ensure .png files are repacked into .bin files at build time.
- Work around missing icons.  Fixes #1276843.

* Fri Oct 23 2015 Peter Oliver <rpm@mavit.org.uk> - 2.30-3
- Set StartupWMClass, so that desktops can match the .desktop file with the windows mapped by the application.  Fixes #1266312.

* Sun Aug  9 2015 Peter Oliver <rpm@mavit.org.uk> - 2.30-2
- Add workaround for #1251756.

* Sun Aug  9 2015 Peter Oliver <rpm@mavit.org.uk> - 2.30-1
- Update to 2.30.  Fixes #1222120.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 19 2015 Peter Robinson <pbrobinson@fedoraproject.org> 2.29-1
- Update to 2.29
- Rebuild (mono4)

* Sat Oct 04 2014 Dan Horák <dan[at]danny.cz> - 2.27-4
- switch to ExclusiveArch, but seems FTBFS even on x86_64

* Mon Aug 18 2014 Rex Dieter <rdieter@fedoraproject.org> 2.27-3
- update mime scriptlets

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 18 2014 Peter Oliver <rpm@mavit.org.uk> - 2.27-1
- Update to version 2.27.

* Fri Jul 18 2014 Peter Oliver <rpm@mavit.org.uk> - 2.26-10
- Add missing %%u to Exec line in .desktop.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Peter Oliver <rpm@mavit.org.uk> - 2.26-7
- Mono crashes on ARM builders, so exclude that architecture.

* Thu May 22 2014 Peter Oliver <rpm@mavit.org.uk> - 2.26-6
- Depend on hicolor-icon-theme.
- The "%%{__python2}" macro requires python-devel.

* Thu May 22 2014 Peter Oliver <rpm@mavit.org.uk> - 2.26-5
- Use "*" rather than ".gz" as the man page suffix, in case the
  compression format changes.
- Use "doc" rather than "-n %%{name}-doc" in subpackages.
- Use "%%{__python2}" macro.

* Sun May 18 2014 Peter Oliver <rpm@mavit.org.uk> - 2.26-4
- Install .desktop file via desktop-file-install.
- Don't recreate the build-root.
- Own documentation directory.
- Own icon and mime directories.
- Make the -doc subpackage noarch.
- Preserve timestamps when installing files.

* Sun Apr 20 2014 Peter Oliver <rpm@mavit.org.uk> - 2.26-3
- Reliable clipboard handling requires xsel.

* Sun Apr 20 2014 Peter Oliver <rpm@mavit.org.uk> - 2.26-2
- Build a documentation subpackage.
- For auto-type, xdotool is required.
- Include an AppData file.

* Fri Apr 18 2014 Peter Oliver <rpm@mavit.org.uk> - 2.26-1
- New package, based in part on the Debian package.
