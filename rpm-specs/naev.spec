%define _legacy_common_support 1

Name:           naev
Version:        0.7.0
Release:        12%{?dist}
Summary:        2d action, RPG space game
License:        GPLv3
URL:            http://naev.org
Source:         http://sourceforge.net/projects/naev/files/%{name}-%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  gcc
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  libxml2-devel
BuildRequires:  freetype-devel
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  openal-soft-devel
BuildRequires:  desktop-file-utils
BuildRequires:  SDL2_mixer-devel
BuildRequires:  compat-lua-devel
BuildRequires:  readline-devel
BuildRequires:  suitesparse-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  libzip-devel
BuildRequires:  libappstream-glib
Requires:       %{name}-data = %{version}


%description
NAEV is a 2D space trading and combat game, in a similar vein to Escape
Velocity.

NAEV is played from a top-down perspective, featuring fast-paced combat, many
ships, a large variety of equipment and a large galaxy to explore. The game is
highly open-ended, letting you proceed at your own pace.

%prep
%setup -q -n %{name}-%{version}

# Remove built-in libraries
rm -rf lib/lua lib/csparse
# Patch configure to use system cxsparse
sed -i "s/\"\$have_csparse_lib\" = \"yes\" -a \"\$have_cxsparse_lib\" = \"yes\"/\"\$have_csparse_lib\" = \"yes\" -o \"\$have_cxsparse_lib\" = \"yes\""/g configure
sed -i s/"-lcsparse -lcxsparse"/"-lcxsparse"/g configure
# Patch configure for Fedora compat-lua
sed -i 's/lua5\.1/lua-5.1/g' configure
# Fix undefined reference to symbol 'vorbis_comment_query'
sed -i 's/vorbisfile/& vorbis/g' configure

%build
# note the ndata-path needs to point directly to the file
%configure --with-ndata-path=%{_datadir}/%{name}/ndata-%{version}.zip --enable-lua=shared --disable-shave --enable-debug=no
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

# Copy high quality 256x256 icon rather than default 32x32
rm -f %{buildroot}%{_datadir}/pixmaps/naev.png
install -m 644 extras/logos/naev.png %{buildroot}%{_datadir}/pixmaps/naev.png

# docs get installed to wrong location
rm -rf %{buildroot}%{_docdir}/naev

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

%files
%doc AUTHORS LICENSE README TODO
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/pixmaps/*.png
%{_datadir}/naev/naev-confupdate.sh
%{_mandir}/man6/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 03 2020 Jonathan Dieter <jdieter@gmail.com> - 0.7.0-11
- Work around GCC 10 build failure

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Jonathan Dieter <jdieter@gmail.com> - 0.7.0-6
- Add BuildRequires: gcc

* Thu Feb 08 2018 Jonathan Dieter <jdieter@gmail.com> - 0.7.0-5
- Remove obsolete Group tag

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 15 2017 Jonathan Dieter <jdieter@lesbg.com> - 0.7.0-1
- New release with new missions

* Tue Feb 28 2017 Remi Collet <remi@fedoraproject.org> - 0.6.1-4
- rebuild for new libzip

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 14 2015 Jonathan Dieter <jdieter@lesbg.com> - 0.6.1-1
- Update to 0.6.1 with improved AI and new missions

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Nils Philippsen <nils@redhat.com> - 0.6.0-4
- rebuild for suitesparse-4.4.4

* Wed May 06 2015 Remi Collet <remi@fedoraproject.org> - 0.6.0-3
- rebuild for new libzip

* Sat Mar 21 2015 Jonathan Dieter <jdieter@lesbg.com> - 0.6.0-2
- Remove debug logs in stdout

* Wed Mar 18 2015 Jonathan Dieter <jdieter@lesbg.com> - 0.6.0-1
- Update to 0.6.0 which includes:
  + Greatly expanded galaxy
  + New missions
  + Hidden jumps

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug 07 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.5.3-8
- Build with compat-lua (#992318, #1106264)
- Fix missing reference to libvorbis

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 06 2013 Nils Philippsen <nils@redhat.com> - 0.5.3-6
- rebuild (suitesparse)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 30 2012 Tom Callaway <spot@fedoraproject.org> - 0.5.3-3
- rebuild for new suitesparse

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Jonathan Dieter <jdieter@lesbg.com> - 0.5.3-1
- Update to 0.5.3 - with new missions and bugfixes

* Fri Mar  2 2012 Jonathan Dieter <jdieter@lesbg.com> - 0.5.1-1
- Test FTBFS failure
- Update to 0.5.1 - with new missions, a new faction and other improvements

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.5.0-4
- Rebuild for new libpng

* Tue Jun 28 2011 Jonathan Dieter <jdieter@lesbg.com> - 0.5.0-3
- Remove unneeded defattr

* Mon Jun 27 2011 Jonathan Dieter <jdieter@lesbg.com> - 0.5.0-2
- Clean up spec

* Sun Jun  5 2011 Jonathan Dieter <jdieter@lesbg.com> - 0.5.0-1
- Convert openSUSE Build Service RPM to Fedora RPM
- Split data into separate source rpm

* Wed Jun  9 2010 dbuck <noone@example.com> - 0.4.2-1
- initial build
