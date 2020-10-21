Name:           glfw
Version:        3.3.2
Release:        6%{?dist}
Epoch:          1
Summary:        A cross-platform multimedia library
Summary(fr):    Une bibliothèque multimédia multi-plateforme
License:        zlib
URL:            http://www.glfw.org/index.html
Source0:        https://github.com/glfw/glfw/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)

%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  vulkan-devel
BuildRequires:  wayland-devel
%endif

%description
GLFW is a free, Open Source, multi-platform library for OpenGL application
development that provides a powerful API for handling operating system specific
tasks such as opening an OpenGL window, reading keyboard, mouse, joystick and
time input, creating threads, and more.

%description -l fr_FR
GLFW est un logiciel gratuit, Open Source, multi-plate-forme de bibliothèque
pour l'application OpenGL développement qui fournit une API puissante pour la
manipulation du système d'exploitation spécifique des tâches telles que
l'ouverture d'une fenêtre OpenGL, la lecture du clavier, souris, joystick et
entrée du temps, les discussions de créer, et plus encore.


%package        devel
Summary:        Development files for %{name}
Summary(fr):    Appui pour le développement d'application C
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       pkgconfig(dri)
Requires:       pkgconfig(glu)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xcursor)
Requires:       pkgconfig(xi)
Requires:       pkgconfig(xinerama)
Requires:       pkgconfig(xrandr)

%description devel
The glfw-devel package contains header files for developing glfw
applications.

%description devel -l fr_FR
Le paquet glfw-devel contient les fichiers d'entêtes pour développer
des applications utilisant glfw.


%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
The %{name}-doc package contains documentation for developing applications
with %{name}.


%prep
%setup -q
find . -type f | xargs sed -i 's/\r//'

%build
%cmake
%cmake_build --target all

%install
%cmake_install

%files
%license LICENSE.md
%doc README.md
%{_libdir}/libglfw.so.3*

%files devel
%{_includedir}/GLFW/
%{_libdir}/libglfw.so
%{_libdir}/pkgconfig/glfw3.pc
%{_libdir}/cmake/glfw3/

%files doc
%doc %{_vpath_builddir}/docs/html/*

%changelog
* Fri Sep 04 2020 Till Hofmann <thofmann@fedoraproject.org> - 1:3.3.2-6
- Adapt to cmake out-of-source builds

* Tue Aug 04 2020 Dave Airlie <airlied@redhat.com> - 3.3.2-5
- Update cmake macros

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.3.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Till Hofmann <thofmann@fedoraproject.org> - 1:3.3.2-1
- Update to 3.3.2
- Switch to GitHub upstream source

* Sun Jan 05 2020 Till Hofmann <thofmann@fedoraproject.org> - 1:3.3.1-3
- Add doc sub-package

* Sun Jan 05 2020 Till Hofmann <thofmann@fedoraproject.org> - 1:3.3.1-2
- Switch to pkgconfig(*)-style build dependencies
- Add missing dependencies of the devel sub-package

* Sun Jan 05 2020 Till Hofmann <thofmann@fedoraproject.org> - 1:3.3.1-1
- Update to 3.3.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 20 2019 Till Hofmann <thofmann@fedoraproject.org> - 1:3.3-1
- Update to 3.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Björn Esser <besser82@fedoraproject.org> - 1:3.2.1-6
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 29 2017 Simone Caronni <negativo17@gmail.com> - 1:3.2.1-2
- Make it build also on epel 7.
- Add license macro.

* Thu Dec 01 2016 Dave Airlie <airlied@redhat.com> - 3.2.1-1
- Updated to 3.2.1 upstream release (to fix wayland bugs)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 08 2015 Martin Preisler <mpreisle@redhat.com> - 1:3.1.1-1
- Updated to 3.1.1 upstream release

* Mon Jan 19 2015 Martin Preisler <mpreisle@redhat.com> - 1:3.1-2
- Reorganized BuildRequires

* Mon Jan 19 2015 Martin Preisler <mpreisle@redhat.com> - 1:3.1-1
- Updated to 3.1 upstream release

* Sat Aug 23 2014 Martin Preisler <mpreisle@redhat.com> - 1:3.0.4-2
- Added accidentally removed dist tag back to Release

* Sat Aug 23 2014 Martin Preisler <mpreisle@redhat.com> - 1:3.0.4-1
- Downgraded to upstream latest stable release - 3.0.4
- Epoch bumped from 0 to 1 to ensure clean upgrade path
- Removed texlive-latex from BuildRequires, it is not used during build

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-0.32.20140310git5c23071
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-0.31.20140310git5c23071
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 10 2014 jonathan MERCIER <bioinfornatics@gmail.com> - 3.1-0.30.20140310git5c23071
- Update to version 3.1

* Mon Oct 28 2013 Jonathan MERCIER <bioinfornatics@gmail.com> - 3.0-0.29.20131028git0153dab
- Update to rev 0153dab

* Thu Oct 24 2013 Jonathan MERCIER <bioinfornatics@gmail.com> - 3.0-0.28.20131021gite309a78
- Update to rev e309a78

* Sat Aug 10 2013 "Jonathan Mercier" <"Jonathan Mercier at gmail dot org"> - 3.0-0.27.20130807git735bc2d
- Update to rev 735bc2d

* Sun Aug 04 2013 "Jonathan Mercier" <"Jonathan Mercier at gmail dot org"> - 3.0-0.26.20130730git63a191e
- Update to rev 63a191e

* Mon Jul 29 2013 Ville Skyttä <ville.skytta@iki.fi> - 3.0-0.25.20130626git2656bf8
- Drop unnecessary doc dir removal from %%install.

* Wed Jun 26 2013 Jonathan MERCIER <bioinfornatics at fedoraproject dot org> - 3.0-0.24.20130626git2656bf8
- Update to rev 2656bf8

* Mon Jun 24 2013 Jonathan MERCIER <bioinfornatics at fedoraproject dot org> - 3.0-0.23.20130624git4883073
- Update to rev 4883073

* Sun Jun 23 2013 Jonathan MERCIER <bioinfornatics at fedoraproject dot org> - 3.0-0.22.20130621git6591579
- Update to rev 6591579

* Sun Jun 09 2013 Jonathan MERCIER <bioinfornatics at fedoraproject dot org> - 3.0-0.21.20130609git52354bf
- Update to rev 52354bf

* Sun Jun 09 2013 Jonathan MERCIER <bioinfornatics at fedoraproject dot org> - 3.0-0.20.20130609git68b7ea8
- Update to rev 68b7ea8

* Fri May 24 2013 Jonathan MERCIER <bioinfornatics at fedoraproject dot org> - 3.0-0.19.20130523git98cbf6f
- Update to rev 98cbf6f

* Sat May 18 2013 Jonathan MERCIER <bioinfornatics at fedoraproject dot org> - 3.0-0.18.20130517git673d5b5
- put  libXrandr as required

* Fri May 17 2013 Jonathan MERCIER <bioinfornatics at fedoraproject dot org> - 3.0-0.17.20130517git673d5b5
- Update to rev 673d5b5

* Fri May 17 2013  <bioinfornatics at fedoraproject dot org> - 3.0-0.16.20130514gite20e8f9
- Update to rev e20e8f9

* Thu May 16 2013  <bioinfornatics at fedoraproject dot org> - 3.0-0.15.20130514gite20e8f9
- Update to rev e20e8f9

* Thu May 16 2013  <bioinfornatics at fedoraproject dot org> - 3.0-0.14.20130514gite20e8f9
- Update to rev e20e8f9

* Wed May 15 2013  <bioinfornatics at fedoraproject dot org> - 3.0-0.13.20130514gite20e8f9
- Update to rev e20e8f9

* Wed May 15 2013 Jonathan MERCIER - 3.0-0.12.20130502git475d10d
- Install .cmake file

* Thu May 09 2013 Jonathan MERCIER <bioinfornatics at gmail.com> - 3.0-0.11.20130502git475d10d
- Update to rev 475d10d

* Tue May 07 2013 Jonathan MERCIER <bioinfornatics at gmail.com> - 3.0-0.10.20120703git14c6978
- Update to rev 14c6978

* Tue May 07 2013 Jonathan MERCIER <bioinfornatics at gmail.com> - 3.0-0.9.20120703gita9ed5b1
- Update to rev 14c6978

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.8.20120812gita9ed5b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 26 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 3.0-0.7.20120812gita9ed5b1
- Fix both release/version format

* Fri Sep 21 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 3.0-6
- use %%{_prefix} instead of /usr
- remove this (debug?) line

* Fri Sep 21 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 3.0-5
- fix spec file

* Mon Aug 13 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 3.0-4
- update ti latest rev #a9ed5b1

* Mon Aug 13 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 3.0-3
- rebuilt

* Sat Aug 11 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 3.0-2
- Update and Fix glfw3

* Wed Apr 18 2012 Jonathan MERCIER <bioinfornatics at gmail.com> - 3.0.0-1
- Initial release
