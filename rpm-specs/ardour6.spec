# websockets in Fedora currently can't be used
%bcond_with websockets

# the test scripts seem to be broken
%bcond_with tests

# whether to do a verbose build
%bcond_without verbose_build
%if %{with verbose_build}
%global _verbose -v
%else
%global _verbose %{nil}
%endif

# whether to use system libraries
%bcond_without system_libs

%global backends jack,alsa,dummy,pulseaudio
%global default_backend jack

# Don't generate provides for internal shared objects and plugins
%global internal_libs_re (alsa_audiobackend|ardour.*|audiographer|canvas|dummy_audiobackend|evoral|gtkmm2ext|jack_audiobackend|midipp|pan[12]in2out|panbalance|panvbap|pbd|ptformat|pulseaudio_backend.so|qmdsp|temporal|timecode|waveview|widgets)
%global __provides_exclude_from ^%{_libdir}/(%{name}|lv2)/.*$
%global __requires_exclude ^lib%{internal_libs_re}\.so.*$

# This package is named ardour6 to allow parallel installation with older versions of Ardour.
Name:       ardour6
Version:    6.3.0

Release:    1%{?dist}
Summary:    Digital Audio Workstation

License:    GPLv3+
URL:        http://ardour.org
# Not available via direct download. Download via
# http://ardour.org/download.html
Source0: Ardour-%{version}.tar.bz2
# BSD 2/3-clause, ISC licenses and GPLv3+ license terms used in some code files
Source1:    LICENSING
Source2:    gpl-3.0.txt

# QM-DSP library is missing kiss-fft functions (#1494796)
Patch0:     %{name}-missing-kissfft.patch

BuildRequires:  boost-devel >= 1.39
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  fontconfig
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  graphviz
BuildRequires:  itstool >= 2.0.0
BuildRequires:  kernel-headers
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(aubio) >= 0.3.2
BuildRequires:  pkgconfig(cairo) >= 1.12.0
BuildRequires:  pkgconfig(cairomm-1.0) >= 1.8.4
BuildRequires:  pkgconfig(cppunit) >= 1.12.0
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(flac) >= 1.2.1
BuildRequires:  pkgconfig(fluidsynth) >= 2.0.1
BuildRequires:  pkgconfig(giomm-2.4) >= 2.32.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.28.0
BuildRequires:  pkgconfig(glibmm-2.4) >= 2.32.0
BuildRequires:  pkgconfig(gthread-2.0) >= 2.28.0
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.18
BuildRequires:  pkgconfig(gtkmm-2.4) >= 2.18
BuildRequires:  pkgconfig(hidapi-hidraw)
BuildRequires:  pkgconfig(jack) >= 1.9.10
BuildRequires:  pkgconfig(libarchive) >= 3.0.0
BuildRequires:  pkgconfig(libcurl) >= 7.0.0
BuildRequires:  pkgconfig(liblo) >= 0.26
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libusb-1.0)
%if %{with websockets}
BuildRequires:  pkgconfig(libwebsockets) >= 2.0.0
%endif
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(lilv-0) >= 0.24.2
BuildRequires:  pkgconfig(lrdf) >= 0.4.0
BuildRequires:  pkgconfig(ltc) >= 1.1.1
BuildRequires:  pkgconfig(lv2) >= 1.0.0
BuildRequires:  pkgconfig(ogg) >= 1.1.2
BuildRequires:  pkgconfig(pangoft2) >= 1.36.8
BuildRequires:  pkgconfig(pangomm-1.4) >= 1.4
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(rubberband) >= 1.0
BuildRequires:  pkgconfig(samplerate) >= 0.1.7
BuildRequires:  pkgconfig(serd-0) >= 0.14.0
BuildRequires:  pkgconfig(sigc++-2.0) >= 2.0
BuildRequires:  pkgconfig(sndfile) >= 1.0.18
BuildRequires:  pkgconfig(sord-0) >= 0.8.0
BuildRequires:  pkgconfig(soundtouch-1.0)
BuildRequires:  pkgconfig(sratom-0) >= 0.2.0
BuildRequires:  pkgconfig(suil-0) >= 0.6.0
BuildRequires:  pkgconfig(taglib) >= 1.6
BuildRequires:  pkgconfig(vamp-hostsdk) >= 2.1
BuildRequires:  pkgconfig(vamp-sdk) >= 2.1
BuildRequires:  pkgconfig(x11) >= 1.1
BuildRequires:  python3
BuildRequires:  python-unversioned-command
BuildRequires:  kiss-fft-static
BuildRequires:  qm-dsp-static
BuildRequires:  symlinks

Requires:       %{name}-backend%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Recommends:     %{name}-backend-%{default_backend}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       google-droid-sans-mono-fonts
Requires:       google-noto-sans-fonts

# custom variant of the clearlooks engine used by ardour
# version guessed (conservatively) by copyright of 2007
Provides:       bundled(gtk-theme-engine-clearlooks) = 2.9.0
# stripped down variant of libsmf, the complete version can be found at
# http://libsmf.sf.net
Provides:       bundled(libsmf) = 1.2
# lua 5.3.5 with custom C++ wrapper
Provides:       bundled(lua) = 5.3.5
# copylib: only a header
# https://github.com/vinniefalco/LuaBridge -- 1.0.2-111-g04b47d7
Provides:       bundled(LuaBridge) = 1.0.2
# libmidi++ and libpbd are internal to ardour, written by the main author
Provides:       bundled(midi++) = 4.1.0
Provides:       bundled(pbd) = 4.1.0

# Ardour 6 is backwards-compatible to version 5, obsolete it from Fedora 33 on
%if 0%{?fedora} >= 33
Obsoletes:      ardour5 < %{version}-%{release}
Conflicts:      ardour5 < %{version}-%{release}
%endif


%description
Ardour is a multi-channel digital audio workstation, allowing users to record,
edit, mix and master audio and MIDI projects. It is targeted at audio
engineers, musicians, soundtrack editors and composers.

# This macro creates a backend subpackage. Needs to be %%define, not %%global so that it's not
# expanded at definition time, but where it's used.
#   %%backend_package <backendname>
%define backend_package() \
%package backend-%{lua: print(string.lower(rpm.expand("%1")))}\
Summary:    %{1} backend for %{name}\
Requires:   %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}\
Provides:   %{name}-backend%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}\
%if 0%{?fedora} >= 33\
Obsoletes:  ardour5-audiobackend-%{lua: print(string.lower(rpm.expand("%1")))} < %{version}-%{release}\
Conflicts:  ardour5-audiobackend-%{lua: print(string.lower(rpm.expand("%1")))} < %{version}-%{release}\
%endif\
\
%description backend-%{lua: print(string.lower(rpm.expand("%1")))}\
This package provides the %{1} backend for Ardour.\
\
%files backend-%{lua: print(string.lower(rpm.expand("%1")))}\
%{_libdir}/%{name}/backends/lib%{lua: print(string.lower(rpm.expand("%1")))}_*backend.so

%backend_package ALSA
%backend_package JACK
%backend_package PulseAudio
%backend_package Dummy

%prep
%autosetup -S gendiff -p1 -n Ardour-%{version}

%if %{with system_libs}
# remove bundled library sources
for i in fluidsynth hidapi libltc qm-dsp; do
    find "libs/$i" \( -name \*.\[ch\] -o -name \*.cc -o -name \*.\[ch\]pp \) -delete
done
%endif

# use versionized name for man page
cp -p ardour.1 ardour6.1

cp %{SOURCE1} %{SOURCE2} .

%build
export LC_ALL=C.UTF-8
%set_build_flags
./waf configure \
%if %{with strict}
    --strict \
%endif
%if %{with tests}
    --test \
%endif
    --prefix="%_prefix" \
    --bindir="%_bindir" \
    --configdir="%_sysconfdir" \
    --datadir="%_datadir" \
    --includedir="%_includedir" \
    --libdir="%_libdir" \
    --mandir="%_mandir" \
    --docdir="%_docdir" \
    --docs \
    --lxvst \
    --nls \
    --noconfirm \
    --no-phone-home \
    --optimize \
%ifarch %ix86 x86_64
    --arch="%optflags -msse -mfpmath=sse -DUSE_XMMINTRIN" \
%else
    --arch="%optflags" \
%endif
%if %{with system_libs}
    --use-external-libs \
%endif
%if %{with cxx11}
    --cxx11 \
%endif
    --freedesktop \
    --with-backends=%{backends}

./waf build %{_verbose} %{?_smp_mflags}
./waf i18n %{_verbose} %{?_smp_mflags}

%install
./waf --destdir=%{buildroot} install %{_verbose}

# ArdourMono.ttf is really Droid Sans Mono
%if ! 0%{?fedora}%{?rhel} || 0%{?fedora} >= 32 || 0%{?rhel} >= 9
ln -snf ../fonts/google-droid-sans-mono-fonts/DroidSansMono.ttf \
    %{buildroot}%{_datadir}/%{name}/ArdourMono.ttf
%else
ln -snf ../fonts/google-droid/DroidSansMono.ttf %{buildroot}%{_datadir}/%{name}/ArdourMono.ttf
%endif

# ArdourSans.ttf is originally Noto Sans Regular
ln -snf ../fonts/google-noto/NotoSans-Regular.ttf %{buildroot}%{_datadir}/%{name}/ArdourSans.ttf

# install man page
install -d -m755 %{buildroot}%{_mandir}/man1
install -p -m644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# install icons to freedesktop locations
for s in 16 22 32 48 256 512; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps
    ln -s ../../../../%{name}/resources/Ardour-icon_${s}px.png \
       %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png
done

# tweak and install desktop file
mkdir -p %{buildroot}%{_datadir}/applications/
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
    --set-key=Name --set-value="Ardour %{version}" \
    --set-generic-name="Digital Audio Workstation" \
    --set-key=X-GNOME-FullName \
    --set-value="Ardour v%{version} (Digital Audio Workstation)" \
    --set-comment="Record, mix and master audio" \
    --remove-category=AudioEditing \
    --add-category=X-AudioEditing \
    build/gtk2_ardour/%{name}.desktop

# install mime entry
mkdir -p %{buildroot}%{_datadir}/mime/packages/
install -p -m 0644 gtk2_ardour/ardour-mime-info.xml %{buildroot}%{_datadir}/mime/packages/%{name}.xml

# install appdata file
mkdir -p %{buildroot}%{_datadir}/appdata/
install -p -m 0644 build/gtk2_ardour/%{name}.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

# Delete zero length file (probably needed to keep empty dir in GIT)
rm %{buildroot}%{_datadir}/%{name}/templates/.stub

%find_lang %{name}
%find_lang gtk2_%{name}
%find_lang gtkmm2ext3

# Collect non-locale data files and (all) directories
find %{buildroot}%{_datadir}/%{name} | \
    sed 's|^%{buildroot}||g' | \
    while read f; do
        # *sigh*
        if [ "$f" = "${f/ /}" ]; then
            _f="$f"
        else
            _f="\"${f}\""
        fi

        if [ -d "%{buildroot}${f}" ]; then
            echo "%%dir ${_f}"
        else
            if [ "${f}" = "${f#%{_datadir}/%{name}/locale}" ]; then
                echo "${_f}"
            fi
        fi
    done > %{name}-datafiles.list

# Convert dangling absolute symlinks to resolvable ones
find %{buildroot} -type l | while read src; do
    tgt="$(readlink "$src")"
    if [ "${tgt#/}" != "$tgt" -a "${tgt#%{buildroot}/}" = "$tgt" ]; then
        ln -snf "%{buildroot}${tgt}" "$src"
    fi
done

# Convert absolute to relative symlinks
symlinks -r -c %{buildroot}

%check
%if %{with tests}
WAFTPATH="$PWD/doc/waft"
pushd libs/ardour
sh "$WAFTPATH" --targets=libardour-tests && LV2_PATH= ./run-tests.sh
popd
%endif

# check appdata file
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml

rm -f %{buildroot}%{_bindir}/run-tests

%files -f %{name}.lang -f gtk2_%{name}.lang -f gtkmm2ext3.lang -f %{name}-datafiles.list
%license COPYING gpl-3.0.txt LICENSING
%{_bindir}/%{name}
%{_bindir}/%{name}-copy-mixer
%{_bindir}/%{name}-export
%{_bindir}/%{name}-fix_bbtppq
%{_bindir}/%{name}-lua
%{_bindir}/%{name}-new_empty_session
%{_bindir}/%{name}-new_session
%config(noreplace) %{_sysconfdir}/%{name}
%{_libdir}/%{name}
%exclude %{_libdir}/%{name}/backends/*
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/appdata/%{name}.appdata.xml
%{_mandir}/man1/%{name}.1*

%changelog
* Sat Sep 26 2020 Nils Philippsen <nils@tiptoe.de> - 6.3.0-1
- version 6.3.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Nils Philippsen <nils@tiptoe.de> - 6.2.0-1
- version 6.2.0
- versionize obsoletes/conflicts

* Mon Jun 22 2020 Nils Philippsen <nils@tiptoe.de> - 6.0.0-5
- obsolete Ardour 5 packages to ensure upgrade

* Wed Jun 03 2020 Nils Philippsen <nils@tiptoe.de> - 6.0.0-4
- fix building on ppc64

* Sun May 31 2020 Nils Philippsen <nils@tiptoe.de> - 6.0.0-3
- remove leftover files at the right stage

* Wed May 27 2020 Nils Philippsen <nils@tiptoe.de> - 6.0.0-2
- simplify release field
- better explain %%backend_package macro
- remove some leftover files

* Tue May 26 2020 Nils Philippsen <nils@tiptoe.de> - 6.0.0-1
- version 6.0.0
- use correct original font file for Droid Sans
- only skip broken tests

* Sat Apr 25 2020 Nils Philippsen <nils@tiptoe.de> - 6.0-0.1.rc1.104
- initial package for a snapshot post 6.0-rc1, based on ardour5
