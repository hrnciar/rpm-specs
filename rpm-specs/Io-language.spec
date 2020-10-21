%filter_from_provides /libiovmall.so$/d
%filter_from_requires /libiovmall.so$/d
%filter_setup

%define _version 2013.12.04
 
Name:           Io-language
Version:        20151111
Release:        0.e64ff9%{?dist}.24
Summary:        Io is a small, prototype-based programming language
License:        BSD
URL:            http://www.iolanguage.com/
# To get this file do wget http://github.com/stevedekorte/io/tarball/%{_version}
# and rename to io-%{version}.tar.gz
#Source0:        %{name}-%{version}0-g23afbcc.tar.gz
Source0:	io-e64ff9.tar.gz
#Patch0:         AddonBuilder_io_libdir.patch
Patch1:         Io-2007-10-10-gcc43.patch
#Patch2:         Io-2007-10-10-missing-protos.patch
#Patch3:         Io-language-20080330-py27.patch
#Patch4:         Io-language-20110912-arm.patch
Patch5:         io-disable-simd.patch
Patch6:         Io-language-freeglut.patch
Patch7:         io-nosysctl.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  e2fsprogs-devel freeglut-devel gmp-devel
BuildRequires:  libedit-devel libevent-devel libjpeg-devel libpng-devel
BuildRequires:  libsamplerate-devel libsndfile-devel libtiff-devel
BuildRequires:  libxml2-devel ode-devel opensp-devel pcre-devel
BuildRequires:  portaudio-devel libpq-devel python3-devel soundtouch-devel
BuildRequires:  sqlite-devel taglib-devel ncurses-devel cairo-devel
BuildRequires:  libuuid-devel readline-devel cmake libogg-devel
BuildRequires:	mesa-libGLU-devel libffi-devel libdbi-devel loudmouth-devel
BuildRequires:	libmemcached-devel libgle-devel libtheora-devel
BuildRequires:	tokyocabinet-devel libvorbis-devel
BuildRequires:	yajl-devel >= 2
# Put back freetype-devel, clutter-devel, mysql-devel, qdbm-devel,
# openssl-devel when these extensions build


%description
Io is a small, prototype-based programming language. The ideas in
Io are mostly inspired by Smalltalk (all values are objects), Self
(prototype-based), NewtonScript (differential inheritance), Act1
(actors and futures for concurrency), LISP (code is a runtime
inspectable/modifiable tree) and Lua (small, embeddable).


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package graphics-and-sound
Summary:        Io graphics and sound support
Requires:       %{name} = %{version}-%{release}

%description graphics-and-sound
Io graphics and sound support, this package includes IO bindings needed to
write Io programs which want to display graphics and / or produce sound
(OpenGL, Image loading, PortAudio, etc.).


%package extras
Summary:        Io extra addons
Requires:       %{name} = %{version}-%{release}

%description extras
This package includes addons for Io which require additional libraries to be
installed. This includes the Python and Socket addons.


%package postgresql
Summary:        Io postgresql bindings
Requires:       %{name} = %{version}-%{release}

%description postgresql
Io postgresql bindings.


%package mysql
Summary:        Io mysql bindings
Requires:       %{name} = %{version}-%{release}

%description mysql
Io mysql bindings


%prep
%setup -q -n io-e64ff9
#%patch0 -p1
%patch1 -p1 -b .gcc43
#%patch2 -p1 -b .protos
#%patch3 -p1
#%patch4 -p0
%patch5 -p0
%patch6 -p0
%patch7 -p0
sed -i 's|/lib/io/addons|/%{_lib}/io/addons|g' libs/iovm/io/AddonLoader.io
# building Io while Io-language-devel is installed results in binaries getting
# linked against the installed version, instead of the just build one <sigh>
if [ -f /usr/include/io/IoVM.h ]; then
  echo "Error building Io while Io-language-devel is installed does not work!"
  exit 1
fi
# libstdc++.so is searched and not found ...
#sed -i -e 's|dependsOnLib("stdc++")||g' addons/SoundTouch/build.io
# remove add-ons which we do not want to build ever
rm -fr addons/AVCodec
rm -rf addons/ODE
sed -i /ODE/d addons/CMakeLists.txt
# for %doc
#mv addons/OpenGL/docs OpenGL
iconv -f MACINTOSH -t UTF8 libs/basekit/license/bsd_license.txt > license.txt
sed -i 's/\r//g' license.txt `find OpenGL -type f`
# for debuginfo
chmod -x addons/NullAddon/source/IoNullAddon.?


%build
cmake . -DOpenGL_GL_PREFERENCE=GLVND ##-DCMAKE_INSTALL_PREFIX=$RPM_BUILD_ROOT%{_prefix}
make INSTALL_PREFIX=%{_prefix} OPTIMIZE="$RPM_OPT_FLAGS" \
  DLL_COMMAND='-shared -Wl,-soname="libiovmall.so.2"'
# not using smp_flags, parallel build is broken.

%install
rm -rf $RPM_BUILD_ROOT
# upstreams make install installs lots of unwanted parts of the addons, so DIY
#make install

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/io/addons
install -m 755 _build/binaries/io $RPM_BUILD_ROOT%{_bindir}
install -m 755 _build/binaries/io_static $RPM_BUILD_ROOT%{_bindir}


#rm $RPM_BUILD_ROOT%{_libdir}/libiovmall.so
install -m 755 _build/dll/libiovmall.so \
  $RPM_BUILD_ROOT%{_libdir}/libiovmall.so.2
ln -s libiovmall.so.2 $RPM_BUILD_ROOT%{_libdir}/libiovmall.so

install -m 755 _build/dll/libbasekit.so $RPM_BUILD_ROOT%{_libdir}/
install -m 755 _build/dll/libcoroutine.so $RPM_BUILD_ROOT%{_libdir}/
install -m 755 _build/dll/libgarbagecollector.so $RPM_BUILD_ROOT%{_libdir}/

mkdir -p $RPM_BUILD_ROOT%{_includedir}
cp -a _build/headers $RPM_BUILD_ROOT%{_includedir}/io

# Clean out addons that don't build.
rm -rf addons/Clutter
rm -rf addons/Font
rm -rf addons/GLFW
rm -rf addons/MySQL
rm -rf addons/QDBM
rm -rf addons/SecureSocket
rm -rf addons/AppleSensors

# install the addons
for i in addons/*; do
  # skip unbuild addons
  if [ -d $i/_build ]; then
    ADDON=`basename $i`
    mkdir -p $RPM_BUILD_ROOT%{_libdir}/io/addons/$ADDON/_build/dll
    install -m 755 $i/_build/dll/libIo$ADDON.so \
      $RPM_BUILD_ROOT%{_libdir}/io/addons/$ADDON/_build/dll
    install -p -m 644 $i/depends $RPM_BUILD_ROOT%{_libdir}/io/addons/$ADDON
    # Io doesn't find the addon if this file isn't present
    touch $RPM_BUILD_ROOT%{_libdir}/io/addons/$ADDON/build.io
  fi
done



%ldconfig_scriptlets


%files
%doc license.txt
%{_bindir}/io
%{_bindir}/io_static
%{_libdir}/libiovmall.so.2
%{_libdir}/libbasekit.so
%{_libdir}/libcoroutine.so
%{_libdir}/libgarbagecollector.so


%dir %{_libdir}/io
%dir %{_libdir}/io/addons
%{_libdir}/io/addons/AsyncRequest
%{_libdir}/io/addons/BigNum
%{_libdir}/io/addons/Bitly
%{_libdir}/io/addons/Blowfish
%{_libdir}/io/addons/Box
%{_libdir}/io/addons/Cairo
#%{_libdir}/io/addons/CFFI
%{_libdir}/io/addons/CGI
%{_libdir}/io/addons/ContinuedFraction
#%{_libdir}/io/addons/Curses
%{_libdir}/io/addons/DBI
%{_libdir}/io/addons/DistributedObjects
%{_libdir}/io/addons/EditLine
%{_libdir}/io/addons/Facebook
%{_libdir}/io/addons/Flux
%{_libdir}/io/addons/Fnmatch
%{_libdir}/io/addons/GoogleSearch
%{_libdir}/io/addons/HttpClient
%{_libdir}/io/addons/LZO
%{_libdir}/io/addons/Libxml2
%{_libdir}/io/addons/Loki
%{_libdir}/io/addons/Loudmouth
%{_libdir}/io/addons/MD5
%{_libdir}/io/addons/Memcached
#%{_libdir}/io/addons/NetworkAdapter
%{_libdir}/io/addons/NotificationCenter
#%{_libdir}/io/addons/NullAddon
%{_libdir}/io/addons/Obsidian
%{_libdir}/io/addons/Random
%{_libdir}/io/addons/Range
%{_libdir}/io/addons/Rational
%{_libdir}/io/addons/ReadLine
%{_libdir}/io/addons/Regex
%{_libdir}/io/addons/SGML
%{_libdir}/io/addons/SHA1
%{_libdir}/io/addons/SQLite3
%{_libdir}/io/addons/SqlDatabase
%{_libdir}/io/addons/Syslog
%{_libdir}/io/addons/SystemCall
%{_libdir}/io/addons/Thread
%{_libdir}/io/addons/TokyoCabinet
%{_libdir}/io/addons/Twitter
%{_libdir}/io/addons/UUID
%{_libdir}/io/addons/User
%{_libdir}/io/addons/VertexDB
%{_libdir}/io/addons/Volcano
%{_libdir}/io/addons/Yajl
%{_libdir}/io/addons/Zlib

%files devel
%doc docs/*
%{_libdir}/libiovmall.so
%{_includedir}/io

%files graphics-and-sound
#%{_libdir}/io/addons/Font
%{_libdir}/io/addons/Image
%{_libdir}/io/addons/LibSndFile
%{_libdir}/io/addons/Ogg
%{_libdir}/io/addons/OpenGL
#%{_libdir}/io/addons/PortAudio
#%{_libdir}/io/addons/TagLib
%{_libdir}/io/addons/Theora
%{_libdir}/io/addons/Vorbis

%files extras
%{_libdir}/io/addons/Python
#%{_libdir}/io/addons/SampleRateConverter
%{_libdir}/io/addons/Socket
#%{_libdir}/io/addons/SoundTouch

%files postgresql
%{_libdir}/io/addons/Postgre*

%files mysql
#%{_libdir}/io/addons/MySQL


%changelog
* Tue Sep 15 2020 Gwyn Ciesla <gwync@protonmail.com> - 20151111-0.e64ff9.24
- Libevent rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20151111-0.e64ff9.23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 20151111-0.e64ff9.22
- Rebuilt for Python 3.9

* Mon May 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 20151111-0.e64ff9.21
- Patch for removal of sysctl.h

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20151111-0.e64ff9.20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Gwyn Ciesla <gwync@protonmail.com> - 20151111-0.e64ff9.19
- Rebuilt for new freeglut

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 20151111-0.e64ff9.18
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20151111-0.e64ff9.17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 20151111-0.e64ff9.16
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20151111-0.e64ff9.15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Petr Pisar <ppisar@redhat.com> - 20151111-0.e64ff9.14
- Rebuild against patched libpcreposix library (bug #1667614)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20151111-0.e64ff9.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 20151111-0.e64ff9.12
- Rebuilt for Python 3.7

* Mon Feb 19 2018 Gwyn Ciesla <limburgher@gmail.com> - 2015111-0.e64ff9.11
- libevent rebuild.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20151111-0.e64ff9.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Gwyn Ciesla <limburgher@gmail.com> - 2015111-0.e64ff9.9
- soundtouch rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20151111-0.e64ff9.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20151111-0.e64ff9.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 20151111-0.e64ff9.6
- Rebuild due to bug in RPM (RHBZ #1468476)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20151111-0.e64ff9.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 20151111-0.e64ff9.4
- Rebuild for readline 7.x

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 20151111-0.e64ff9.3
- Rebuild for Python 3.6

* Wed Apr 06 2016 Jon Ciesla <limburgher@gmail.com> - 2015111-0.e64ff9.2
- Explicitly switch to Python 3, BZ 1323243.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20151111-0.e64ff9.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 24 2016 Jon Ciesla <limburgher@gmail.com> - 2015111-0.e64ff9
- Fix FTBFS, BZ 1239343.

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20131204-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 30 2014 Jon Ciesla <limburgher@gmail.com> - 20131204-1
- Fix FTBFS, BZ 1105914.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110912-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110912-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 22 2014 Jon Ciesla <limburgher@gmail.com> - 20110912-12
- Rebuild for new libdbi.

* Mon Aug 05 2013 Jon Ciesla <limburgher@gmail.com> - 20110912-11
- Fix FTBFS, BZ 991934.

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110912-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110912-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 20110912-8
- rebuild due to "jpeg8-ABI" feature drop

* Mon Jan 07 2013 Adam Tkac <atkac redhat com> - 20110912-7
- rebuild against new libjpeg

* Sat Sep 22 2012 Jon Ciesla <limburgher@gmail.com> - 20110912-6
- libmemcached rebuild.

* Tue Sep 18 2012 Jon Ciesla <limburgher@gmail.com> - 20110912-5
- Fix ARM FTBFS.

* Mon Jul 23 2012 Jon Ciesla <limburgher@gmail.com> - 20110912-4
- Re-rebuild for old libdbi.

* Mon Jul 23 2012 Jon Ciesla <limburgher@gmail.com> - 20110912-3
- Rebuild for new libdbi.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110912-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 10 2012 Jon Ciesla <limburgher@gmail.com> - 20110912-1
- Latest upstream.

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 20080330-9.2
- Rebuild against PCRE 8.30

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080330-8.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 20080330-7.2
- Rebuild for new libpng

* Fri Oct 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 20080330-6.2
- rebuild with new gmp without compat lib

* Wed Oct 12 2011 Peter Schiffer <pschiffe@redhat.com> - 20080330-6.1
- rebuild with new gmp

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 20080330-6
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Mon Feb 14 2011 Jon Ciesla <limb@jcomserv.net> - 20080330-5
- Rebuild for libevent.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080330-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 31 2010 Hans de Goede <hdegoede@redhat.com> - 20080330-3
- Fix compilation of python addon with python 2.7

* Fri Jul 30 2010 Hans de Goede <hdegoede@redhat.com> - 20080330-2
- Rebuild for python 2.7

* Fri Jan 15 2010 Hans de Goede <hdegoede@redhat.com> - 20080330-1
- Rebase to latest upstream release 20080330
- Bump soname because of ABI change
- Fix FTBFS (#511617)

* Fri Jan 15 2010 Caolán McNamara <caolanm@redhat.com> - 20071010-12
- Resolves: rhbz#511617 FTBFS

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071010-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071010-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 15 2009 Hans de Goede <hdegoede@redhat.com> - 20071010-9
- rebuild for new soundtouch

* Sat Jan 24 2009 Caolán McNamara <caolanm@redhat.com> - 20071010-8
- rebuild for dependencies

* Sun Nov 30 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 20071010-7
- Rebuild for Python 2.6

* Sun Jun 29 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 20071010-6
- Rebuild for new libevent

* Sun Mar 30 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 20071010-5
- Fix missing prototype compiler warnings

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 20071010-4
- Autorebuild for GCC 4.3

* Thu Jan 24 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 20071010-3
- Rebuild for new libevent

* Sat Jan 12 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 20071010-2
- Fix compilation with gcc 4.3
- Enable Cairo addon

* Sun Nov 11 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 20071010-1
- New (official!) upstream release 2007-10-10
- API changed, soname bumped to libiovmall.so.1

* Wed Sep 12 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 20070710-2
- Reshuffle which docs to include and in which subpackages to include them
  (bz 284151)

* Sun Sep  9 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 20070710-1
- Adapted Packman spec file for Fedora

* Sat Sep 08 2007 Toni Graffy <toni@links2linux.de> 20070528-0.pm.2
- openSUSE-10.3 build, using libode(-devel)

* Sun Jun 03 2007 Toni Graffy <toni@links2linux.de> 20070528-0.pm.1
- update to 20070528
- added patches for 64bit (thx Detlef)
- switched to portaudio

* Sun May 27 2007 Toni Graffy <toni@links2linux.de> 20070430-0.pm.1
- initial package 20070430
