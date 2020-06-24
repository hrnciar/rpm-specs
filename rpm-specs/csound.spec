%global has_luajit 0
%global luajit_version 2.1

Name:    csound
Version: 6.14.0
Release: 2%{?dist}
Summary: A sound synthesis language and library
URL:     http://csound.github.io/
License: LGPLv2+

Source0: https://github.com/csound/csound/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: https://github.com/csound/manual/archive/Csound%{version}_manual_html.zip

Patch1:  0001-Add-support-for-using-xdg-open-for-opening-help.patch
Patch2:  0002-Default-to-PulseAudio.patch
Patch3:  0003-use-standard-plugins-path.patch
Patch4:  0004-fix-naming-conflicts.patch
Patch5:  0005-add-extern-for-multiply-defined.patch

BuildRequires: gcc gcc-c++
BuildRequires: bison
BuildRequires: bluez-libs-devel
BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: CUnit-devel
BuildRequires: docbook-style-xsl
BuildRequires: dssi-devel
BuildRequires: eigen3-devel
BuildRequires: flex
BuildRequires: fltk-fluid
BuildRequires: fluidsynth-devel
BuildRequires: gettext-devel
BuildRequires: gmm-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: java-devel
BuildRequires: jpackage-utils
BuildRequires: libcurl-devel
BuildRequires: liblo-devel
BuildRequires: libpng-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: libvorbis-devel
BuildRequires: libxslt
%if 0%{?has_luajit}
BuildRequires: luajit-devel
%endif
BuildRequires: portaudio-devel
BuildRequires: portmidi-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-tkinter
BuildRequires: python3-pygments
BuildRequires: stk-devel
BuildRequires: swig
BuildRequires: wiiuse-devel

# These obsoletes can be removed in Fedora 31
Obsoletes: %{name}-javadoc < 6.10.0-1%{?dist}
Provides:  %{name}-javadoc = 6.10.0-1%{?dist}
Obsoletes: %{name}-lua < 6.10.0-1%{?dist}
Provides:  %{name}-lua = 6.10.0-1%{?dist}
# These obsoletes can be removed in Fedora 33
Obsoletes: %{name}-csoundac < 6.13.0-3%{?dist}
Provides:  %{name}-csoundac = 6.13.0-3%{?dist}
Obsoletes: python2-csound < 6.13.0-3%{?dist}
Obsoletes: python2-csound-devel < 6.13.0-3%{?dist}

%global luaver %(lua -v | sed -r 's/Lua ([[:digit:]]+\\.[[:digit:]]+).*/\\1/')

%description
Csound is a sound and music synthesis system, providing facilities for
composition and performance over a wide range of platforms. It is not
restricted to any style of music, having been used for many years in
at least classical, pop, techno, ambient...

%package devel
Summary: Csound development files and libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Contains headers and libraries for developing applications that use Csound.

%package -n python3-csound
%{?python_provide:%python_provide python3-csound}
Summary: Python Csound development files and libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: python3

%description -n python3-csound
Contains Python language bindings for developing Python applications that
use Csound.

%package java
Summary: Java Csound support
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: java-headless
Requires: jpackage-utils

%description java
Contains Java language bindings for developing and running Java
applications that use Csound.

%if 0%{?has_luajit}
%package lua
Summary: Lua Csound support
Requires: %{name}%{?_isa} = %{version}-%{release}

%description lua
Contains Lua language bindings for developing and running Lua
applications that use Csound.
%endif

%package fltk
Summary: FLTK plugins for Csound
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: fltk

%description fltk
Contains FLTK plugins for csound

%package jack
Summary: Jack Audio plugins for Csound
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: jack-audio-connection-kit

%description jack
Contains Jack Audio plugins for Csound

%package fluidsynth
Summary: Fluidsyth soundfont plugin for Csound
Requires: %{name}%{?_isa} = %{version}-%{release}

%description fluidsynth
Contains Fluidsynth soundfont plugin for Csound.

%package dssi
Summary: Disposable Soft Synth Interface (DSSI) plugin for Csound
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: dssi

%description dssi
Disposable Soft Synth Interface (DSSI) plugin for Csound

%package osc
Summary: Open Sound Control (OSC) plugin for Csound
Requires: %{name}%{?_isa} = %{version}-%{release}

%description osc
Open Sound Control (OSC) plugin for Csound

%package portaudio
Summary: PortAudio plugin for Csound
Requires: %{name}%{?_isa} = %{version}-%{release}

%description portaudio
PortAudio plugin for Csound

%package stk
Summary: STK (Synthesis ToolKit in C++) plugin for Csound
Requires: %{name}%{?_isa} = %{version}-%{release}

%description stk
STK (Synthesis ToolKit in C++) plugin for Csound

%package virtual-keyboard
Summary: Virtual MIDI keyboard plugin for Csound
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: fltk

%description virtual-keyboard
A virtual MIDI keyboard plugin for Csound

%package wiimote
Summary: Wiimote plugin for Csound
Requires: %{name}%{?_isa} = %{version}-%{release}

%description wiimote
A Wiimote plugin for Csound

%package manual
Summary: Csound manual
License: GFDL
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description manual
Canonical Reference Manual for Csound.


%prep
%autosetup -p1
# setup the manual
%setup -q -T -D -a 1

# Fix luajit version
find ./ -name CMakeLists.txt -exec sed -i 's|luajit-2.0|luajit-%{luajit_version}|g' {} \;

# Fix end of line encodings
%define fix_line_encoding() \
  sed -i.orig 's/\\r\\n/\\n/;s/\\r/\\n/g' %1; \
  touch -r %1.orig %1; \
  rm -f %1.orig;

for csd in $(find html/examples -name \*.csd); do
  %fix_line_encoding $csd
done

%fix_line_encoding html/examples/128,8-torus
%fix_line_encoding html/examples/128-spiral-8,16,128,2,1over2
%fix_line_encoding html/examples/128-stringcircular
%fix_line_encoding html/examples/string-128.matrix

# Fix spurious executable bits
chmod a-x html/examples/*

%build
%if "%{_libdir}" == "%{_prefix}/lib64"
    %global uselib64 ON
%else
    %global uselib64 OFF
%endif

# Terrible hack
%ifarch %{arm}
sed -i 's*//#define PFFFT_SIMD_DISABLE*#define PFFFT_SIMD_DISABLE*' OOps/pffft.c
%endif

%cmake -DUSE_LIB64:BOOL=%{uselib64} -DBUILD_JAVA_INTERFACE:BOOL=ON \
       -DSWIG_ADD_LIBRARY:BOOL=OFF -DBUILD_JACK_OPCODES:BOOL=ON \
       -DPYTHON_MODULE_INSTALL_DIR:STRING="%{python3_sitearch}" \
%if 0%{?has_luajit}
       -DLUA_MODULE_INSTALL_DIR:STRING="%{libdir}/lua/%{luaver}" \
%endif
       -DBUILD_CSOUND_AC:BOOL=ON -DBUILD_CSOUND_AC_PYTHON_INTERFACE:BOOL=ON \
%ifarch %{x86}
       -DHAS_SSE2:BOOL=OFF -DHAS_FPMATH_SSE:BOOL=OFF \
%endif
%ifarch %{arm}
       -DHAVE_NEON:BOOL=OFF \
%endif
       -DBUILD_STK_OPCODES:BOOL=ON -DBUILD_PADSYNTH_OPCODES:BOOL=OFF \
       -DUSE_PORTMIDI:BOOL=OFF -DNEED_PORTTIME:BOOL=OFF

%make_build

%install
%make_install

# Fix the Java installation
install -dm 755 %{buildroot}%{_javadir}
(cd %{buildroot}%{_javadir}; ln -s %{_libdir}/%{name}/java/csnd.jar .)

# Help the debuginfo generator
ln -s ../csound_orclex.c Engine/csound_orclex.c
ln -s ../csound_prelex.c Engine/csound_prelex.c

rm -rf %{buildroot}%{_datadir}/cmake/Csound/

%find_lang %{name}6

%ldconfig_scriptlets

%ldconfig_scriptlets -n python3-csound

%ldconfig_scriptlets csoundac

%check
# make csdtests

%files -f %{name}6.lang
%license COPYING
%doc README.md Release_Notes
%{_bindir}/atsa
%{_bindir}/cs
%{_bindir}/csanalyze
%{_bindir}/csb64enc
%{_bindir}/csbeats
%{_bindir}/csdebugger
%{_bindir}/csound
%{_bindir}/cvanal
%{_bindir}/dnoise
%{_bindir}/cs-envext
%{_bindir}/cs-extract
%{_bindir}/cs-extractor
%{_bindir}/het_export
%{_bindir}/het_import
%{_bindir}/hetro
%{_bindir}/lpanal
%{_bindir}/lpc_export
%{_bindir}/lpc_import
%{_bindir}/makecsd
%{_bindir}/cs-mixer
%{_bindir}/pvanal
%{_bindir}/pv_export
%{_bindir}/pv_import
%{_bindir}/pvlook
%{_bindir}/cs-scale
%{_bindir}/cs-scot
%{_bindir}/scsort
%{_bindir}/sdif2ad
%{_bindir}/cs-sndinfo
%{_bindir}/cs-srconv
%{_bindir}/cs-src_conv
%{_libdir}/lib%{name}64.so.6.0
%dir %{_libdir}/%{name}/plugins-6.0
%{_libdir}/%{name}/plugins-6.0/libampmidid.so
%{_libdir}/%{name}/plugins-6.0/libarrayops.so
%{_libdir}/%{name}/plugins-6.0/libbeosc.so
%{_libdir}/%{name}/plugins-6.0/libbuchla.so
%{_libdir}/%{name}/plugins-6.0/libcellular.so
%{_libdir}/%{name}/plugins-6.0/libchua.so
%{_libdir}/%{name}/plugins-6.0/libcontrol.so
%{_libdir}/%{name}/plugins-6.0/libcs_date.so
%{_libdir}/%{name}/plugins-6.0/libdoppler.so
%{_libdir}/%{name}/plugins-6.0/libemugens.so
%{_libdir}/%{name}/plugins-6.0/libexciter.so
%{_libdir}/%{name}/plugins-6.0/libfareygen.so
%{_libdir}/%{name}/plugins-6.0/libfractalnoise.so
%{_libdir}/%{name}/plugins-6.0/libframebuffer.so
%{_libdir}/%{name}/plugins-6.0/libftsamplebank.so
%{_libdir}/%{name}/plugins-6.0/libgetftargs.so
%{_libdir}/%{name}/plugins-6.0/libgtf.so
%{_libdir}/%{name}/plugins-6.0/libimage.so
%{_libdir}/%{name}/plugins-6.0/libipmidi.so
%{_libdir}/%{name}/plugins-6.0/libjoystick.so
%{_libdir}/%{name}/plugins-6.0/libliveconv.so
%{_libdir}/%{name}/plugins-6.0/libmixer.so
%{_libdir}/%{name}/plugins-6.0/libplaterev.so
%{_libdir}/%{name}/plugins-6.0/libpvsops.so
%{_libdir}/%{name}/plugins-6.0/libquadbezier.so
%{_libdir}/%{name}/plugins-6.0/librtalsa.so
%{_libdir}/%{name}/plugins-6.0/librtpulse.so
%{_libdir}/%{name}/plugins-6.0/libscansyn.so
%{_libdir}/%{name}/plugins-6.0/libscugens.so
%{_libdir}/%{name}/plugins-6.0/libserial.so
%{_libdir}/%{name}/plugins-6.0/libselect.so
%{_libdir}/%{name}/plugins-6.0/libsignalflowgraph.so
%{_libdir}/%{name}/plugins-6.0/libstackops.so
%{_libdir}/%{name}/plugins-6.0/libstdutil.so
%{_libdir}/%{name}/plugins-6.0/libsystem_call.so
%{_libdir}/%{name}/plugins-6.0/liburandom.so

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}64.so
%{_libdir}/libcsnd6.so

%files -n python3-csound
%{_libdir}/libcsnd6.so.6.0
%{_libdir}/%{name}/plugins-6.0/libpy.so
%{python3_sitearch}/_csnd*
%{python3_sitearch}/csnd*
%{python3_sitearch}/*csound.py*
%{python3_sitearch}/__pycache__/

%if 0%{?has_luajit}
%files lua
%{_libdir}/%{name}/plugins-6.0/libLuaCsound.so
%{_libdir}/lua/%{luaver}/*
%endif

%files java
%{_libdir}/lib_jcsound6.so
%{_libdir}/csnd6.jar
%{_javadir}/csnd.jar

%files fltk
%{_libdir}/%{name}/plugins-6.0/libwidgets.so

%files jack
%{_libdir}/%{name}/plugins-6.0/libjacko.so
%{_libdir}/%{name}/plugins-6.0/librtjack.so
%{_libdir}/%{name}/plugins-6.0/libjackTransport.so

%files fluidsynth
%{_libdir}/%{name}/plugins-6.0/libfluidOpcodes.so

%files dssi
%{_libdir}/%{name}/plugins-6.0/libdssi4cs.so

%files osc
%{_libdir}/%{name}/plugins-6.0/libosc.so

%files portaudio
%{_libdir}/%{name}/plugins-6.0/librtpa.so

%files stk
%{_libdir}/%{name}/plugins-6.0/libstkops.so

%files virtual-keyboard
%{_libdir}/%{name}/plugins-6.0/libvirtual.so

%files wiimote
%{_libdir}/%{name}/plugins-6.0/libwiimote.so

%files manual
%doc html/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 6.14.0-2
- Rebuilt for Python 3.9

* Tue Feb 18 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 6.14.0-1
- Update to 6.14.0

* Mon Feb 17 2020 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 6.13.0-7
- Rebuild against fluidsynth2
- Fix FTBFS RHBZ#1794443

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 6.13.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 6.13.0-4
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Peter Robinson <pbrobinson@fedoraproject.org> 6.13.0-3
- Move to python3, upstream seems to have fixed it with the current release
- Minor cleanups

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Peter Robinson <pbrobinson@fedoraproject.org> 6.13.0-1
- Update to Csound 6.13.0

* Sun Jun  9 2019 Peter Robinson <pbrobinson@fedoraproject.org> 6.12.2-1
- Update to Csound 6.12.2

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 25 2018 Peter Robinson <pbrobinson@fedoraproject.org> 6.10.0-2
- Fix upgrade path

* Sun Feb 25 2018 Peter Robinson <pbrobinson@fedoraproject.org> 6.10.0-1
- Update to Csound 6.10.0
- Obsolete javadocs support (deprecated upstream)
- Packaging updates from Hlöðver Sigurðsson

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.03.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.03.2-16
- Python 2 binary package renamed to python2-csound
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.03.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.03.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.03.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 29 2016 Igor Gnatenko <ignatenko@redhat.com> - 6.03.2-12
- Rebuild for LuaJIT 2.1.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.03.2-11
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.03.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 19 2015 Kalev Lember <klember@redhat.com> - 6.03.2-9
- Rebuilt for libwiiuse soname bump

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.03.2-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 6.03.2-7
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.03.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 6.03.2-5
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 6.03.2-4
- Rebuild for boost 1.57.0

* Tue Sep 30 2014 Dan Horák <dan[at]danny.cz> - 6.03.2-3
- luajit available only on selected arches

* Wed Sep 24 2014 Peter Robinson <pbrobinson@fedoraproject.org> 6.03.2-2
- Fix separation of jack into it's subpackage

* Tue Sep 16 2014 Jerry James <loganjerry@gmail.com> - 6.03.2-1
- Update to 6.03.2
- Fix installation
- Fix license handling
- Add wiimote subpackage, wiiuse-devel BR, and bluez-libs-devel BR (bz 1142457)

* Fri Aug 29 2014 Peter Robinson <pbrobinson@fedoraproject.org> 6.03.1-1
- Update to 6.03.1
- Spec file fixups

* Mon Jul 28 2014 Jerry James <loganjerry@gmail.com> - 6.03.0-1
- Update to 6.03.0 (bz 1094866; fixes bzs 1057580, 1067182, and 1106095)
- Change project URL to github page
- Update BRs and reorganize for readability
- Bring back the manual sources; the manual subpackage has the GFDL license
- Obsolete the -gui and -tk subpackages (no longer supported upstream)
- Add -csoundac, -lua, -portaudio, and -stk subpackages
