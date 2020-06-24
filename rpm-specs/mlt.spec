%bcond_without ruby
%bcond_without php
%bcond_with    freeworld

%if (0%{?rhel} && 0%{?rhel} <= 7) || (0%{?fedora} && 0%{?fedora} <= 31)
%bcond_without python2
%else
%bcond_with python2
%endif

%if 0%{?fedora} >= 30 || 0%{?rhel} >= 8
%bcond_without python3
%else
%bcond_with    python3
%endif


#globals for https://github.com/mltframework/mlt/commit/ea973eb65c8ca79a859028a9e008360836ca4941
%global gitdate 20171213
%global commit ea973eb65c8ca79a859028a9e008360836ca4941
%global shortcommit %(c=%{commit}; echo ${c:0:7})
#global gver .%%{gitdate}git%%{shortcommit}

Name:           mlt
Version:        6.20.0
Release:        2%{?dist}
Summary:        Toolkit for broadcasters, video editors, media players, transcoders

# mlt/src/win32/fnmatch.{c,h} are BSD-licensed.
# but is not used in Linux
License:        GPLv3 and LGPLv2+
URL:            http://www.mltframework.org/
##Source0:        https://github.com/mltframework/mlt/archive/v%%{version}/%%{name}-%%{version}.tar.gz
Source0:        https://github.com/mltframework/mlt/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
##Patch1:         83eace8f2a384b46243597d6eb1fd5f0e5c9eb65.patch

BuildRequires:  frei0r-devel
BuildRequires:  opencv-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qt3d-devel
BuildRequires:  SDL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  gtk2-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libogg-devel
#Deprecated dv and kino modules are not built.
#https://github.com/mltframework/mlt/commit/9d082192a4d79157e963fd7f491da0f8abab683f
#BuildRequires:  libdv-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  ladspa-devel
BuildRequires:  libxml2-devel
BuildRequires:  sox-devel
# verion 3.0.11 needed for php7 IIRC
BuildRequires:  swig >= 3.0.11
%if %{with python2}
BuildRequires:  python2-devel
%endif
%if %{with python3}
BuildRequires:  python3-devel
%endif
BuildRequires:  freetype-devel
BuildRequires:  libexif-devel
BuildRequires:  fftw-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  vid.stab-devel
BuildRequires:  movit-devel
BuildRequires:  eigen3-devel
BuildRequires:  libebur128-devel
%if %{with freeworld}
BuildRequires:  ffmpeg-devel
BuildRequires:  xine-lib-devel
%endif

%if !%{with python2}
Obsoletes: python2-mlt < %{version}-%{release}
%endif

%if %{with ruby}
BuildRequires:  ruby-devel
BuildRequires:  ruby
%else
Obsoletes: mlt-ruby < %{version}-%{release}
%endif

%if %{with php}
BuildRequires: php-devel
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}%{php_extdir}/.*\\.so$
%endif

Requires:  opencv-core

%description
MLT is an open source multimedia framework, designed and developed for
television broadcasting.

It provides a toolkit for broadcasters, video editors,media players,
transcoders, web streamers and many more types of applications. The
functionality of the system is provided via an assortment of ready to use
tools, xml authoring components, and an extendible plug-in based API.

%package devel
Summary:        Libraries, includes to develop applications with %{name}
License:        LGPLv2+
Requires:       pkgconfig
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains the header files and static libraries for
building applications which use %{name}.

%package -n python2-mlt
%{?python_provide:%python_provide python2-mlt}
Obsoletes: %{name}-python < %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: Python 2 package to work with MLT

%description -n python2-mlt
This module allows to work with MLT using python 2.

%package -n python3-mlt
%{?python_provide:%python_provide python3-mlt}
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: Python package to work with MLT

%description -n python3-mlt
This module allows to work with MLT using python 3.

%package ruby
Requires: %{name}%{_isa} = %{version}-%{release}
Summary: Ruby package to work with MLT

%description ruby
This module allows to work with MLT using ruby.

%package php
Requires: php(zend-abi) = %{php_zend_api}
Requires: php(api) = %{php_core_api}
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: PHP package to work with MLT

%description php
This module allows to work with MLT using PHP.


%prep
%autosetup -p1 -n %{name}-%{version}

chmod 644 src/modules/qt/kdenlivetitle_wrapper.cpp
chmod 644 src/modules/kdenlive/filter_freeze.c
chmod -x demo/demo

# Don't overoptimize (breaks debugging)
sed -i -e '/fomit-frame-pointer/d' configure
sed -i -e '/ffast-math/d' configure

sed -i -e 's|qmake|qmake-qt5|' src/modules/qt/configure

# mlt/src/win32/fnmatch.{c,h} are BSD-licensed.
# be sure that aren't used
rm -r src/win32/

%if 0%{?fedora} >= 25
sed -i 's|-php5|-php7|g' src/swig/php/build
sed -i 's|mlt_wrap.cpp|mlt_wrap.cxx|g' src/swig/php/build
%endif

%if %{with python3}
cp -a src/swig/python src/swig/python3
find src/swig/python3 -name '*.py' | xargs sed -i '1s|^#!/usr/bin/env python3|#!%{__python3}|'
%endif
%if %{with python2}
find src/swig/python -name '*.py' | xargs sed -i '1s|^#!/usr/bin/env python3|#!%{__python2}|'
sed -i -e 's|-python3|-python2|' src/swig/python/build
%else
rm -rf src/swig/python
%endif

%build
#export STRIP=/bin/true
%configure \
        --enable-gpl                            \
        --enable-gpl3                            \
        --enable-motion-est                     \
        --enable-vorbis                     \
%ifnarch %{ix86} x86_64
        --disable-mmx                           \
        --disable-sse                           \
%endif
        --disable-xine                          \
        --rename-melt=%{name}-melt              \
        --swig-languages="%{?with_python2: python}%{?with_python3: python3}%{?with_php: php}%{?with_ruby: ruby}"

%make_build


%install
%make_install

# manually do what 'make install' skips
%if %{with python2}
install -D -pm 0644 src/swig/python/mlt.py %{buildroot}%{python2_sitelib}/mlt.py
install -D -pm 0755 src/swig/python/_mlt.so %{buildroot}%{python2_sitearch}/_mlt.so
%endif
%if %{with python3}
install -D -pm 0644 src/swig/python3/mlt.py %{buildroot}%{python3_sitelib}/mlt.py
install -D -pm 0755 src/swig/python3/_mlt.so %{buildroot}%{python3_sitearch}/_mlt.so
%endif

%if %{with ruby}
install -D -pm 0755 src/swig/ruby/play.rb %{buildroot}%{ruby_vendorlibdir}/play.rb
install -D -pm 0755 src/swig/ruby/thumbs.rb %{buildroot}%{ruby_vendorlibdir}/thumbs.rb
install -D -pm 0755 src/swig/ruby/mlt.so %{buildroot}%{ruby_vendorarchdir}/mlt.so
%endif

%if %{with php}
install -D -pm 0755 src/swig/php/mlt.so %{buildroot}%{php_extdir}/mlt.so
install -d %{buildroot}%{_sysconfdir}/php.d
cat > %{buildroot}%{_sysconfdir}/php.d/mlt.ini << 'EOF'
; Enable mlt extension module
extension=mlt.so
EOF
%endif

mv src/modules/motion_est/README README.motion_est


%check
# verify pkg-config version sanity
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion mlt-framework)" = "%{version}"
test "$(pkg-config --modversion mlt++)" = "%{version}"

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog NEWS README*
%license COPYING GPL
%{_bindir}/mlt-melt
%{_libdir}/mlt/
%{_libdir}/libmlt++.so.*
%{_libdir}/libmlt.so.*
%{_datadir}/mlt/

%if %{with python2}
%files -n python2-mlt
%{python2_sitelib}/mlt.py*
%{python2_sitearch}/_mlt.so
%endif

%if %{with python3}
%files -n python3-mlt
%{python3_sitelib}/mlt.py*
%{python3_sitearch}/_mlt.so
%{python3_sitelib}/__pycache__/mlt.*
%endif

%if %{with ruby}
%files ruby
%{ruby_vendorlibdir}/play.rb
%{ruby_vendorlibdir}/thumbs.rb
%{ruby_vendorarchdir}/mlt.so
%endif

%if %{with php}
%files php
%config(noreplace) %{_sysconfdir}/php.d/mlt.ini
%{php_extdir}/mlt.so
%endif

%files devel
%doc docs/* demo/
%{_libdir}/pkgconfig/mlt-framework.pc
%{_libdir}/pkgconfig/mlt++.pc
%{_libdir}/libmlt.so
%{_libdir}/libmlt++.so
%{_includedir}/mlt/
%{_includedir}/mlt++/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 6.20.0-2
- Rebuilt for Python 3.9
- Rebuild for OpenCV 4.3

* Mon Feb 17 2020 Martin Gansser <martinkg@fedoraproject.org> - 6.20.0-1
- Update to 6.20.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.18.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 6.18.0-3
- F-32: rebuild against ruby27

* Mon Dec 23 2019 Sérgio Basto <sergio@serjux.com> - 6.18.0-2
- Remove python2-mlt subpackage once flowblade is switched to Python 3 (#1738074)
- Nothing provides python3-mlt needed by flowblade-2.4 on F30 (#1785934)
- Enable audio support with vorbis (#1724862)

* Tue Nov 12 2019 Sérgio Basto <sergio@serjux.com> - 6.18.0-1
- Update to 6.18.0

* Sun Nov 03 2019 Sérgio Basto <sergio@serjux.com> - 6.16.0-4
- Fix build on rawhide with Python 3.8

* Tue Oct 22 2019 Sérgio Basto <sergio@serjux.com> - 6.16.0-3
- Couple of fixes from upstream for kdenlive
- Add python3-mlt in addition to python2-mlt, document Python 2 exception

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 11 2019 Sérgio Basto <sergio@serjux.com> - 6.16.0-1
- Update MLT to 6.16.0

* Tue May 07 2019 Sérgio Basto <sergio@serjux.com> - 6.14.0-2
- Flowblade requires python2-mlt until version 2.4, 2.4 will be the first
  Python3 supporting version https://github.com/jliljebl/flowblade/issues/597

* Sun Apr 28 2019 Sérgio Basto <sergio@serjux.com> - 6.14.0-1
- Update to 6.14.0 and switch to python3 on F30+

* Mon Mar 04 2019 Martin Gansser <martinkg@fedoraproject.org> - 6.12.0-7
- Add mlt-null-pointer-crash.patch again

* Sun Mar 03 2019 Martin Gansser <martinkg@fedoraproject.org> - 6.12.0-6
- Re-Add mlt-python2 subpackage

* Sat Feb 02 2019 Martin Gansser <martinkg@fedoraproject.org> - 6.12.0-5
- Add mlt-null-pointer-crash.patch fixes (RHBZ #1669010)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 6.12.0-3
- F-30: rebuild against ruby26

* Fri Jan 04 2019 Miro Hrončok <mhroncok@redhat.com> - 6.12.0-2
- Remove the Python 2 subpackage (#1628684)

* Thu Nov 29 2018 Martin Gansser <martinkg@fedoraproject.org> - 6.12.0-1
- Update to 6.12.0

* Thu Oct 11 2018 Remi Collet <remi@remirepo.net> - 6.10.0-5
- Rebuild for https://fedoraproject.org/wiki/Changes/php73

* Wed Aug 22 2018 Martin Gansser <martinkg@fedoraproject.org> - 6.10.0-4
- Rebuilt

* Wed Aug 22 2018 Sérgio Basto <sergio@serjux.com> - 6.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 13 2018 Martin Gansser <martinkg@fedoraproject.org> - 6.10.0-2
- Revert Revert-Prefer-qimage-over-pixbuf.patch
- Add 'if' conditions to fix missing python2 on Fedora 29

* Tue Jul 03 2018 Martin Gansser <martinkg@fedoraproject.org> - 6.10.0-1
- Update to 6.10.0

* Sat Jun 16 2018 Martin Gansser <martinkg@fedoraproject.org> - 6.8.0-2
- Add Revert-Prefer-qimage-over-pixbuf.patch to prevent flowblade segfault

* Sat May 12 2018 Martin Gansser <martinkg@fedoraproject.org> - 6.8.0-1
- Update to 6.8.0

* Mon Mar 05 2018 Adam Williamson <awilliam@redhat.com> - 6.6.0-7
- Rebuild for opencv soname bump

* Fri Mar 02 2018 Sérgio Basto <sergio@serjux.com> - 6.6.0-6
- Enable SDL1 and SDL2 as requested by flowblade authors
  https://github.com/jliljebl/flowblade/blob/master/flowblade-trunk/docs/SDL_2_AND_MLT_6_6_0.md

* Sun Feb 11 2018 Iryna Shcherbina <ishcherb@redhat.com> - 6.6.0-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Sérgio Basto <sergio@serjux.com> - 6.6.0-3
- Rebuild (movit-1.6.0)

* Sun Jan 28 2018 Sérgio Basto <sergio@serjux.com> - 6.6.0-2
- Try a fix for kdenlive: There is "Use GPU processing (Movit library)... "
  GPU processing needs MLT compiled with Movit and RTaudio modules
  It is greyed, can not select.

* Thu Jan 25 2018 Sérgio Basto <sergio@serjux.com> - 6.6.0-1
- Update to 6.6.0

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 6.5.0-0.9.20171213gitea973eb
- Rebuilt for switch to libxcrypt

* Fri Jan 05 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 6.5.0-0.8.20171213gitea973eb
- F-28: rebuild for ruby25

* Sat Dec 23 2017 Sérgio Basto <sergio@serjux.com> - 6.5.0-0.7.20171213gitea973eb
- Update snapshot

* Fri Nov 17 2017 Sérgio Basto <sergio@serjux.com> - 6.5.0-0.6.20171114git73bfefd
- Update snapshot

* Sun Nov 05 2017 Sérgio Basto <sergio@serjux.com> - 6.5.0-0.5.20171105gitddc40aa
- Update snapshot

* Tue Oct 10 2017 Sérgio Basto <sergio@serjux.com> - 6.5.0-0.4
- Add vid.stab support

* Tue Oct 03 2017 Remi Collet <remi@fedoraproject.org> - 6.5.0-0.3
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Sat Sep 30 2017 Sérgio Basto <sergio@serjux.com> - 6.5.0-0.2
- Enable movit support

* Sat Sep 30 2017 Sérgio Basto <sergio@serjux.com> - 6.5.0-0.1
- Update to 6.5.0 pre-version also fix some bugs (#1497386)
- Switch to SDL2

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.4.1-10
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.4.1-9
- Python 2 binary package renamed to python2-mlt
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 03 2017 Sérgio Basto <sergio@serjux.com> - 6.4.1-6
- Rebuild (opencv)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Sérgio Basto <sergio@serjux.com> - 6.4.1-4
- Better swig handler for el7 support

* Sat Jan 14 2017 Sérgio Basto <sergio@serjux.com> - 6.4.1-3
- Enable php extension, swig already support php7 (#1356985)

* Thu Jan 12 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 6.4.1-2
- F-26: rebuild for ruby24

* Tue Nov 29 2016 Sérgio Basto <sergio@serjux.com> - 6.4.1-1
- New upstream vesion, 6.4.1
- Fix license, win32 not used in Linux
- Clean trailing white spaces
- Move provides_exclude_from php into php clause

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jun 30 2016 Sérgio Basto <sergio@serjux.com> - 6.2.0-2
- Disable the php extension, for now, the PHP 7 landed in rawhide

* Wed May 25 2016 Sérgio Basto <sergio@serjux.com> - 6.2.0-1
- Initial MLT spec on Fedora.

* Tue Mar 29 2016 Sérgio Basto <sergio@serjux.com> - 6.0.0-3
- Use upstream patch to compile Ruby bindings

* Sun Feb 21 2016 Sérgio Basto <sergio@serjux.com> - 6.0.0-2
- Add license tag.
- More spec modernizations and rpmlint fixes.
- Configure conditional build for Ruby.
- Remove old BuilRequires that aren't needed anymore.
- Remove old config options (avformat-swscale and qimage-libdir) that no longer
  exist in configure.
- Fix Ruby build.

* Fri Feb 19 2016 Sérgio Basto <sergio@serjux.com> - 6.0.0-1
- Update 6.0.0 (This is a bugfix and minor enhancement release. Note that our
  release versioning scheme has changed. We were approaching 1.0 but decided to
  synchronize release version with the C library ABI version, which is currently
  at v6)
- Switch to qt5 to fix rfbz #3810 and copy some BRs from Debian package.

* Wed Nov 18 2015 Sérgio Basto <sergio@serjux.com> - 0.9.8-1
- Update MLT to 0.9.8

* Mon May 11 2015 Sérgio Basto <sergio@serjux.com> - 0.9.6-2
- Workaround #3523

* Thu May 07 2015 Sérgio Basto <sergio@serjux.com> - 0.9.6-1
- Update mlt to 0.9.6 .
- Added BuildRequires of libexif-devel .

* Thu May 07 2015 Sérgio Basto <sergio@serjux.com> - 0.9.2-4
- Added BuildRequires of opencv-devel, rfbz #3523 .

* Mon Oct 20 2014 Sérgio Basto <sergio@serjux.com> - 0.9.2-3
- Rebuilt for FFmpeg 2.4.3

* Fri Sep 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.9.2-2
- Rebuilt for FFmpeg 2.4.x

* Mon Sep 15 2014 Sérgio Basto <sergio@serjux.com> - 0.9.2-1
- New upstream release.

* Thu Aug 07 2014 Sérgio Basto <sergio@serjux.com> - 0.9.0-6
- Rebuilt for ffmpeg-2.3

* Sat Jul 26 2014 Sérgio Basto <sergio@serjux.com> - 0.9.0-5
- Rebuild for new php, need by mlt-php

* Sun Mar 30 2014 Sérgio Basto <sergio@serjux.com> - 0.9.0-4
- Rebuilt for ffmpeg-2.2 and fix for freetype2 changes.

* Wed Dec 04 2013 Sérgio Basto <sergio@serjux.com> - 0.9.0-3
- Update License tag .

* Wed Nov 20 2013 Sérgio Basto <sergio@serjux.com> - 0.9.0-2
- Enable gplv3 as asked in rfbz #3040
- Fix a changelog date.
- Fix Ruby warning with rpmbuild "Use RbConfig instead of obsolete and deprecated Config".
- Remove obsolete tag %%clean and rm -rf

* Mon Oct 07 2013 Sérgio Basto <sergio@serjux.com> - 0.9.0-1
- Update to 0.9.0

* Wed Oct 02 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.8.8-7
- Rebuilt

* Thu Aug 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.8.8-6
- Rebuilt for FFmpeg 2.0.x

* Mon Jun 10 2013 Rex Dieter <rdieter@fedoraproject.org> 0.8.8-5
- mlt-ruby FTBFS, omit until fixed (#2816)

* Sun May 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.8.8-4
- Rebuilt for x264/FFmpeg

* Sun Apr 28 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.8.8-3
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Feb 1  2013 Ryan Rix <ry@n.rix.si> - 0.8.8-1
- Fix ABI requirement to Ruby 1.9

* Fri Feb 1  2013 Ryan Rix <ry@n.rix.si> - 0.8.8-1
- Update to 0.8.8

* Wed Jan 30 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.8.6-2
- Rebuilt for ffmpeg

* Sun Dec 30 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.8.6-1
- Update to 0.8.6

* Sat Nov 24 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.8.0-3
- Rebuilt for FFmpeg 1.0

* Tue Jun 26 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.8.0-2
- Rebuilt for FFmpeg

* Tue Jun 19 2012 Richard Shaw <hobbes1069@gmail.com> - 0.8.0-1
- Update to latest upstream release.

* Thu Jun 14 2012 Remi Collet <remi@fedoraproject.org> 0.7.8-3
- fix filter

* Thu Jun 14 2012 Remi Collet <remi@fedoraproject.org> 0.7.8-2
- update PHP requirement for PHP Guildelines
- add php extension configuration file
- filter php private shared so

* Tue May 08 2012 Rex Dieter <rdieter@fedoraproject.org> 0.7.8-1
- 0.7.8

* Tue May 08 2012 Rex Dieter <rdieter@fedoraproject.org> 0.7.6-8
- rebuild (sox)

* Fri Mar 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.7.6-7
- Rebuilt for c++ ABI breakage

* Tue Feb 28 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.7.6-6
- Rebuilt for x264/FFmpeg

* Fri Jan 27 2012 Ryan Rix <ry@n.rix.si> 0.7.6-5
- Include patch to fix building on gcc47 (upstreaming)

* Wed Jan 25 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 29 2011 Ryan Rix <ry@n.rix.si> 0.7.6-3
- s/%%[?_isa}/%%{?_isa}

* Tue Nov 15 2011 Rex Dieter <rdieter@fedoraproject.org> 0.7.6-2
- rebuild

* Fri Nov 11 2011 Rex Dieter <rdieter@fedoraproject.org> 0.7.6-1
- 0.7.6
- track files/sonames closer
- tighten subpkg deps via %%{?_isa}
- drop dup'd %%doc items

* Mon Sep 26 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.7.4-2
- Rebuilt for ffmpeg-0.8

* Thu Jul 21 2011 Ryan Rix <ry@n.rix.si> - 0.7.4-1
- New upstream

* Sun Apr 10 2011 Ryan Rix <ry@n.rix.si> - 0.7.0-2
- Add SDL_image-devel BR per Kdenlive wiki page

* Thu Apr 7 2011 Ryan Rix <ry@n.rix.si> - 0.7.0-1
- New upstream

* Tue Dec 21 2010 Ryan Rix <ry@n.rix.si> - 0.5.4-2
- Fix build, needed a patch from mlt's git repo.

* Sat Nov 20 2010 Nicolas Chauvet <kwizart@gmail.com> - 0.5.4-1.1
- rebuilt - was missing in repo

* Wed Apr 21 2010 Ryan Rix <ry@n.rix.si> - 0.5.4-1
- New upstream version to fix reported crashes against Kdenlive

* Fri Feb 19 2010 Zarko Pintar <zarko.pintar@gmail.com> - 0.5.0-2
- disabled xine module for PPC arch.

* Thu Feb 18 2010 Zarko Pintar <zarko.pintar@gmail.com> - 0.5.0-1
- new version

* Wed Dec 09 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.4.10-1
- new version
- added subpackage for ruby

* Wed Oct 07 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.4.6-1
- new version
- added subpackages for: python, PHP

* Mon Sep 07 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.4.4-1
- new version
- renamed melt binary to mlt-melt

* Wed May 20 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.4.2-1
- new version
- removed obsolete patches

* Wed May 20 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.4.0-3
- added linker and license patches
- set license of MLT devel subpackage to LGPLv2+ 

* Wed May 20 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.4.0-2
- some PPC clearing

* Mon May 18 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.4.0-1
- update to 0.4.0

* Wed May 13 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.3.9-2
- spec cleaning

* Mon May 11 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.3.9-1
- new release
- MLT++  is now a part of this package

* Fri May  8 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.3.8-3
- unused-direct-shlib-dependency fix

* Fri Apr 17 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.3.8-2
- spec clearing
- added patches for resolving broken lqt-config, lib64 and execstack

* Wed Apr 15 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.3.8-1
- New release

* Thu Apr  9 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.3.6-3
- Enabled MMX support (not for PPC & PPC64)
- include demo files
- some spec cosmetics

* Thu Mar 12 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.3.6-2
- Change URL address
- devel Requires: pkgconfig

* Fri Feb 20 2009 Levente Farkas <lfarkas@lfarkas.org> - 0.3.6-1
- Update to 0.3.6

* Wed Nov  5 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 0.3.1-0.1.svn1180
- update to upstream r1180
- add --avformat-swscale configure option

* Tue Nov  4 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 0.3.0-5
- rebuilt with proper qt4 paths

* Mon Oct 13 2008 jeff <moe@blagblagblag.org> - 0.3.0-4
- Build without fomit-frame-pointer ffmath
- Add BuildRequires: prelink
- clear-execstack libmltgtk2.so
- Don't strip binaries
- Group: Development/Libraries
- Prefix albino, humperdink, and miracle binaries with mlt-

* Sun Oct  5 2008 jeff <moe@blagblagblag.org> - 0.3.0-3
- License: GPLv2+ and LGPLv2+
- Group: Development/Tools
- ExcludeArch: x86_64 s390 s390x ppc ppc64
- %%defattr(-,root,root)
- %%doc docs/
- %%{_libdir}/%%{name} to main package


* Sun Aug 24 2008 jeff <moe@blagblagblag.org> - 0.3.0-2
- Change BuildRoot:
- Full source URL
- ExcludeArch: x86_64
- -devel Requires: pkgconfig, Requires: %%{name} = %%{version}-%%{release}

* Sun Aug 24 2008 jeff <moe@blagblagblag.org> - 0.3.0-1
- Update to 0.3.0
- --enable-gpl
- mlt-filehandler.patch

* Tue Jul  8 2008 jeff <moe@blagblagblag.org> - 0.2.5-0.svn1155.0blag.f10
- Build for blaghead

* Mon Jul  7 2008 jeff <moe@blagblagblag.org> - 0.2.5-0.svn1155.0blag.f9
- Update to svn r1155
- Remove sox-st.h.patch
- Add configure --disable-sox as it breaks build

* Sun Nov 11 2007 jeff <moe@blagblagblag.org> - 0.2.4-0blag.f7
- Update to 0.2.4
- Clean up spec

* Sat Jun 23 2007 jeff <moe@blagblagblag.org> - 0.2.3-0blag.f7
- Update to 0.2.3

* Sat Dec 30 2006 jeff <moe@blagblagblag.org> - 0.2.2-0blag.fc6
- Rebuild for 60k
- Remove --disable-sox
- Add mlt-0.2.2-sox-st.h.patch

* Sat Oct 21 2006 jeff <moe@blagblagblag.org> - 0.2.2-0blag.fc5
- Update to 0.2.2

* Sat Oct 21 2006 jeff <moe@blagblagblag.org> - 0.2.1-0blag.fc5
- BLAG'd
- Removed "olib" from path, name, etc.
- Add changelog
- Update summary/description

