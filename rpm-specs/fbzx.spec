Name:           fbzx
Version:        4.0.0
Release:        4%{?dist}
Summary:        A ZX Spectrum emulator for FrameBuffer

License:        GPLv3+
URL:            http://www.rastersoft.com/programas/fbzx.html
Source0:        %{name}-%{version}-noroms.tar.gz
# The above file is derived from:
# https://gitlab.com/rastersoft/fbzx/-/archive/4.0.0/fbzx-4.0.0.tar.gz
# This file contains Spectrum ROMs and cannot be shipped in Fedora. 
# Therefore we use this script to remove them before shipping it. 
# Download the upstream tarball and invoke this script while in 
# the tarball's directory:
# ./fbzx-generate-tarball.sh 4.0.0
Source1:        %{name}-generate-tarball.sh
Source2:        README_%{name}.Fedora
# Debian man page
Source3:        %{name}.1

BuildRequires:  gcc-c++
BuildRequires:  SDL2-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
FBZX is a Sinclair Spectrum emulator, designed to work at full screen using 
the FrameBuffer or under X-Windows. 


%prep
%setup -q

# Fix Makefile
sed -i 's/$(CC) -o/$(CC) $(CFLAGS) -o/' src/Makefile


%build
%set_build_flags
export CPPFLAGS=$CXXFLAGS
%make_build


%install
%make_install PREFIX=%{_prefix} NOROMS=1

# remove obsolete pixmap
rm -rf %{buildroot}%{_datadir}/pixmaps
install -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 data/%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps

# fix desktop file
desktop-file-install \
  --delete-original \
  --add-category Emulator \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

# verify AppData file
appstream-util validate-relax --nonet \
  %{buildroot}%{_datadir}/appdata/*.appdata.xml

# install man page
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 %{SOURCE3} %{buildroot}%{_mandir}/man1/

# install Fedora README
install -p -m 644 %{SOURCE2} %{buildroot}%{_pkgdocdir}


%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/*
%doc %{_pkgdocdir}
%exclude %{_pkgdocdir}/COPYING
%license COPYING


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Andrea Musuruane <musuruan@gmail.com> - 4.0.0-1
- Updated to new upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 03 2018 Andrea Musuruane <musuruan@gmail.com> - 3.9.1-1
- Updated to new upstream release
- Updated to latest Debian man page

* Wed Feb 21 2018 Andrea Musuruane <musuruan@gmail.com> - 3.8.0-6
- Added gcc dependency
- Fixed LDFLAGS usage
- Minor clean up

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.8.0-4
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 11 2017 Andrea Musuruane <musuruan@gmail.com> - 3.8.0-1
- Updated to new upstream release

* Sun Mar 05 2017 Andrea Musuruane <musuruan@gmail.com> - 3.7.0-1
- Updated to new upstream release

* Sat Feb 18 2017 Andrea Musuruane <musuruan@gmail.com> - 3.6.0-1
- Updated to new upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 09 2016 Andrea Musuruane <musuruan@gmail.com> - 3.1.0-1
- Updated to new upstream release
- Added man page from Debian
- Spec file cleanup

* Sat Sep 05 2015 Andrea Musuruane <musuruan@gmail.com> - 3.0.0-1
- Updated to new upstream release

* Sat Apr 04 2015 Andrea Musuruane <musuruan@gmail.com> - 2.11.1-1
- Updated to new upstream release
- Appdata file is now provided by upstream
- Dropped obsolete Group, Buildroot, %%clean and %%defattr
- Dropped cleaning at the beginning of %%install

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 2.10.0-6
- Add an AppData file for the software center

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 08 2012 Andrea Musuruane <musuruan@gmail.com> 2.10.0-1
- Updated to new upstream release

* Wed May 23 2012 Andrea Musuruane <musuruan@gmail.com> 2.9.0-1
- Updated to new upstream release
- More consistent macro usage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 09 2011 Andrea Musuruane <musuruan@gmail.com> 2.7.0-1
- Updated to new upstream release

* Thu Apr 07 2011 Andrea Musuruane <musuruan@gmail.com> 2.5.0-1
- Updated to new upstream release

* Sat Apr 02 2011 Andrea Musuruane <musuruan@gmail.com> 2.4.3-1
- Updated to new upstream release

* Thu Feb 17 2011 Andrea Musuruane <musuruan@gmail.com> 2.4.2-1
- Updated to new upstream release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Mar 20 2010 Andrea Musuruane <musuruan@gmail.com> 2.4.1-1
- Updated to new upstream release

* Sun Feb 21 2010 Andrea Musuruane <musuruan@gmail.com> 2.4.0-1
- Updated to new upstream release

* Sun Dec 27 2009 Andrea Musuruane <musuruan@gmail.com> 2.3.0-1
- Updated to new upstream release

* Sat Dec 26 2009 Andrea Musuruane <musuruan@gmail.com> 2.2.0-1
- Updated to new upstream release

* Wed Aug 12 2009 Andrea Musuruane <musuruan@gmail.com> 2.1b-2
- Icon is now installed into %%{_datadir}/icons/hicolor/scalable/apps
- Added missing desktop-file-utils to BuildRequires
- Added missing hicolor-icon-theme to Requires
- Preserved timestamps

* Sat Jul 25 2009 Andrea Musuruane <musuruan@gmail.com> 2.1b-1
- First release

