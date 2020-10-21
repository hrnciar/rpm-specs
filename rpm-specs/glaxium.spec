Name:           glaxium
Version:        0.5
Release:        35%{?dist}
Summary:        An OpenGL space shooter
License:        GPLv2+
URL:            http://xhosxe.free.fr/glaxium/
Source0:        http://xhosxe.free.fr/glaxium/%{name}_%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
Source3:        %{name}.appdata.xml
Patch0:         %{name}-0.5-fixes.patch
Patch1:         %{name}_0.5-allow-running-when-dsp-busy.patch
Patch2:         %{name}_0.5-glutInit.patch
Patch3:         %{name}_0.5-rh553067.patch
Patch4:         %{name}_0.5-64bit-crash.patch
Patch5:         %{name}_0.5-fighter2_meshes-fix.patch
# Fix crash with freeglut >= 3.0 (rhbz#1293048)
Patch6:         0001-Stop-mixing-glut-and-SDL-usage.patch
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  SDL_mixer-devel libpng-devel automake
BuildRequires:  desktop-file-utils libappstream-glib
Requires:       hicolor-icon-theme opengl-games-utils

%description
Glaxium is an OpenGL-based space-ship "shoot-em-up" styled game.
It is designed to provide the same feel as the old 2D games 
of that type, but with 3D for the special effects.

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
autoreconf -ivf
sed -i 's|/games/glaxium|/glaxium|g' configure* Makefile.in
sed -i 's/\r//g' CHANGES.txt LICENSE README.txt


%build
%configure
make %{?_smp_mflags}


%install
# make install DESTDIR=$RPM_BUILD_ROOT doesn't work
mkdir -p $RPM_BUILD_ROOT%{_bindir}
%makeinstall
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-wrapper

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml



%files
%doc CHANGES.txt LICENSE README.txt
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6.gz
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-35
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.5-30
- Rebuild with fixed binutils

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5-27
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 31 2015 Hans de Goede <hdegoede@redhat.com> - 0.5-22
- Fix crash when activating the special weapon (rhbz#1293048)
- Add an appdata file

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5-20
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.5-16
- Drop desktop vendor tag.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May  3 2012 Hans de Goede <hdegoede@redhat.com> - 0.5-13
- Fix occasional crash caused by a bufferoverflow (#815826)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.5-11
- Rebuild for new libpng

* Thu Jun 16 2011 Hans de Goede <hdegoede@redhat.com> 0.5-10
- Fix crash on 64 bit machines

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 16 2010 Hans de Goede <hdegoede@redhat.com> 0.5-8
- Fix FTBFS (#564699)

* Thu Jan  7 2010 Hans de Goede <hdegoede@redhat.com> 0.5-7
- Fix crash when the level of the game with tanks is reached (#553067)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.5-4
- Autorebuild for GCC 4.3

* Mon Dec 31 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.5-3
- Fix glaxium exiting when pressing space (bz 427048)

* Sat Oct  6 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.5-2
- Add patch from packman which allows running when sound is not available
- Minor .desktop file improvements

* Thu Oct  4 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.5-1
- Initial Fedora package
