# To get the gmp-api commit to use, run:
# rm -rf gmp-api;make gmp-bootstrap;cd gmp-api;git rev-parse HEAD
%global commit1 c5f1d0f3213178818cbfb3e16f31d07328980560
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

%global openh264_version 2.1.1
%global gst_version 1.16.2

Name:           openh264
Version:        %{openh264_version}
# Also bump the Release tag for gstreamer1-plugin-openh264 down below
Release:        1%{?dist}
Summary:        H.264 codec library

License:        BSD
URL:            http://www.openh264.org/
Source0:        https://github.com/cisco/openh264/archive/v%{openh264_version}/openh264-%{openh264_version}.tar.gz
Source1:        https://github.com/mozilla/gmp-api/archive/%{commit1}/gmp-api-%{shortcommit1}.tar.gz
# The source is:
# http://gstreamer.freedesktop.org/src/gst-plugins-bad/gst-plugins-bad-%%{gst_version}.tar.xz
# modified with gst-p-bad-cleanup.sh from SOURCE3
Source2:        gst-plugins-bad-openh264-%{gst_version}.tar.xz
Source3:        gst-p-bad-cleanup.sh

# https://gitlab.freedesktop.org/gstreamer/common/-/merge_requests/4
# https://bugzilla.redhat.com/show_bug.cgi?id=1799497
Patch0:         gstreamer1-plugins-bad-build-adapt-to-backwards-incompatible-change.patch

BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  chrpath
BuildRequires:  gettext-devel
BuildRequires:  gstreamer1-devel >= %{gst_version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{gst_version}
BuildRequires:  libtool
BuildRequires:  nasm

%description
OpenH264 is a codec library which supports H.264 encoding and decoding. It is
suitable for use in real time applications such as WebRTC.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{openh264_version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package     -n mozilla-openh264
Summary:        H.264 codec support for Mozilla browsers
Requires:       %{name}%{?_isa} = %{openh264_version}-%{release}
Requires:       mozilla-filesystem%{?_isa}

%description -n mozilla-openh264
The mozilla-openh264 package contains a H.264 codec plugin for Mozilla
browsers.


%package     -n gstreamer1-plugin-openh264
Version:        %{gst_version}
Release:        2%{?dist}
Summary:        GStreamer H.264 plugin
Supplements:    totem%{?_isa}

%description -n gstreamer1-plugin-openh264
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains the H.264 plugin.


%prep
%setup -q

# Extract gmp-api archive
tar -xf %{S:1}
mv gmp-api-%{commit1} gmp-api

# Extract gst-plugins-bad-free archive
tar -xf %{S:2}
pushd gst-plugins-bad-%{gst_version}
%patch0 -p1
popd

# Update the makefile with our build options
sed -i -e 's|^CFLAGS_OPT=.*$|CFLAGS_OPT=%{optflags}|' Makefile
sed -i -e 's|^PREFIX=.*$|PREFIX=%{_prefix}|' Makefile
sed -i -e 's|^LIBDIR_NAME=.*$|LIBDIR_NAME=%{_lib}|' Makefile
sed -i -e 's|^SHAREDLIB_DIR=.*$|SHAREDLIB_DIR=%{_libdir}|' Makefile
sed -i -e '/^CFLAGS_OPT=/i LDFLAGS=%{__global_ldflags}' Makefile


%build
# First build the openh264 libraries
make %{?_smp_mflags}

# ... then build the mozilla plugin
make plugin %{?_smp_mflags}

# ... and finally build the gstreamer plugin against the previously built
# openh264 libraries
pushd gst-plugins-bad-%{gst_version}
ln -s ../codec/api/svc wels
export OPENH264_CFLAGS="-I."
export OPENH264_LIBS="-L`pwd`/.. -lopenh264"
autoreconf --force --install
%configure \
    --with-package-name="Fedora gstreamer1-plugin-openh264 package" \
    --with-package-origin="http://www.openh264.org/" \
    --disable-static \
    --disable-gl \
    --disable-hls \
    --enable-openh264
make V=1 %{?_smp_mflags}
popd


%install
%make_install

# Install mozilla plugin
mkdir -p $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins/gmp-gmpopenh264/system-installed
cp -a libgmpopenh264.so* gmpopenh264.info $RPM_BUILD_ROOT%{_libdir}/mozilla/plugins/gmp-gmpopenh264/system-installed/

mkdir -p $RPM_BUILD_ROOT%{_libdir}/firefox/defaults/pref
cat > $RPM_BUILD_ROOT%{_libdir}/firefox/defaults/pref/gmpopenh264.js << EOF
pref("media.gmp-gmpopenh264.autoupdate", false);
pref("media.gmp-gmpopenh264.version", "system-installed");
EOF

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
cat > $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/gmpopenh264.sh << EOF
MOZ_GMP_PATH="%{_libdir}/mozilla/plugins/gmp-gmpopenh264/system-installed"
export MOZ_GMP_PATH
EOF

# Remove static libraries
rm $RPM_BUILD_ROOT%{_libdir}/*.a

# Install the gstreamer plugin
pushd gst-plugins-bad-%{gst_version}
%make_install

# Register as an AppStream component to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/gstreamer-openh264.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2015 Kalev Lember <klember@redhat.com> -->
<component type="codec">
  <id>gstreamer-openh264</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>GStreamer Multimedia Codecs - H.264</name>
  <summary>Multimedia playback for H.264</summary>
  <description>
    <p>
      This addon includes a codec for H.264 playback and encoding.
    </p>
    <p>
      These codecs can be used to encode and decode media files where the
      format is not patent encumbered.
    </p>
    <p>
      A codec decodes audio and video for playback or editing and is also
      used for transmission or storage.
      Different codecs are used in video-conferencing, streaming media and
      video editing applications.
    </p>
  </description>
  <url type="homepage">http://gstreamer.freedesktop.org/</url>
  <url type="bugtracker">https://bugzilla.gnome.org/enter_bug.cgi?product=GStreamer</url>
  <url type="help">http://gstreamer.freedesktop.org/documentation/</url>
  <url type="donation">http://www.gnome.org/friends/</url>
  <update_contact><!-- upstream-contact_at_email.com --></update_contact>
</component>
EOF

# Remove libtool .la files
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Remove unwanted gst-plugins-bad files
rm -rf $RPM_BUILD_ROOT%{_includedir}/gstreamer-1.0/
rm -rf $RPM_BUILD_ROOT%{_libdir}/girepository-1.0/Gst*.typelib
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig/gstreamer-*.pc
rm -rf $RPM_BUILD_ROOT%{_libdir}/libgst*.so*
rm -rf $RPM_BUILD_ROOT%{_datadir}/gir-1.0/Gst*.gir
rm -rf $RPM_BUILD_ROOT%{_datadir}/gstreamer-1.0/
rm -rf $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/gst-plugins-bad*/
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*/*/gst-plugins-bad-1.0.mo

# Only keep libgstopenh264.so
find $RPM_BUILD_ROOT%{_libdir}/gstreamer-1.0/ -not -name 'libgstopenh264.so' -type f | xargs rm

# Kill rpath
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/gstreamer-1.0/libgstopenh264.so
popd


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license LICENSE
%doc README.md
%{_libdir}/libopenh264.so.6
%{_libdir}/libopenh264.so.%{openh264_version}

%files devel
%{_includedir}/wels/
%{_libdir}/libopenh264.so
%{_libdir}/pkgconfig/openh264.pc

%files -n mozilla-openh264
%{_sysconfdir}/profile.d/gmpopenh264.sh
%dir %{_libdir}/firefox
%dir %{_libdir}/firefox/defaults
%dir %{_libdir}/firefox/defaults/pref
%{_libdir}/firefox/defaults/pref/gmpopenh264.js
%{_libdir}/mozilla/plugins/gmp-gmpopenh264/

%files -n gstreamer1-plugin-openh264
%{_datadir}/appdata/*.appdata.xml
%{_libdir}/gstreamer-1.0/libgstopenh264.so


%changelog
* Fri May 22 2020 Kalev Lember <klember@redhat.com> - 2.1.1-1
- Update to 2.1.1
- Add totem supplements to gstreamer1-plugin-openh264

* Tue Mar 10 2020 Kalev Lember <klember@redhat.com> - 2.1.0-1
- Update to 2.1.0
- Update gstreamer plugin to 1.16.2

* Mon Jun 17 2019 Kalev Lember <klember@redhat.com> - 2.0.0-1
- Update openh264 to 2.0.0
- Update gstreamer plugin to 1.16.0

* Fri Feb 22 2019 Kalev Lember <klember@redhat.com> - 1.8.0-3
- Update gstreamer plugin to 1.15.1

* Wed Sep 12 2018 Kalev Lember <klember@redhat.com> - 1.8.0-2
- Update gstreamer plugin to 1.14.2

* Wed Jun 27 2018 Kalev Lember <klember@redhat.com> - 1.8.0-1
- Update openh264 to 1.8.0
- Update gstreamer plugin to 1.14.1

* Tue Mar 06 2018 Kalev Lember <klember@redhat.com> - 1.7.0-6
- Update gstreamer plugin to 1.13.90

* Sat Dec 16 2017 Kalev Lember <klember@redhat.com> - 1.7.0-5
- Update gstreamer plugin to 1.12.4

* Tue Sep 19 2017 Kalev Lember <klember@redhat.com> - 1.7.0-4
- Update gstreamer plugin to 1.12.3

* Thu Jul 20 2017 Kalev Lember <klember@redhat.com> - 1.7.0-3
- Update gstreamer plugin to 1.12.2

* Tue Jun 20 2017 Kalev Lember <klember@redhat.com> - 1.7.0-2
- Update gstreamer plugin to 1.12.1

* Fri Jun 16 2017 Kalev Lember <klember@redhat.com> - 1.7.0-1
- Update openh264 to 1.7.0
- Update gstreamer plugin to 1.12.0

* Mon Mar 06 2017 Kalev Lember <klember@redhat.com> - 1.6.0-5
- Update gstreamer plugin to 1.10.4

* Mon Jan 30 2017 Kalev Lember <klember@redhat.com> - 1.6.0-4
- Update gstreamer plugin to 1.10.3

* Mon Dec 05 2016 Kalev Lember <klember@redhat.com> - 1.6.0-3
- Update gstreamer plugin to 1.10.2

* Fri Sep 02 2016 Kalev Lember <klember@redhat.com> - 1.6.0-2
- Update gstreamer plugin to 1.9.2

* Thu Aug 25 2016 Kalev Lember <klember@redhat.com> - 1.6.0-1
- Update openh264 to 1.6.0
- Update gstreamer plugin to 1.8.3

* Thu Apr 28 2016 Kalev Lember <klember@redhat.com> - 1.5.3-0.1.git2706e36
- Update openh264 to 1.5.3 git snapshot
- Update gstreamer plugin to 1.8.1

* Mon Mar 21 2016 Dennis Gilmore <dennis@ausil.us> - 1.5.2-0.4.git21e44bd
- move the mozila-openh264 definition before gstreamer1-plugin-openh264
- gstreamer1-plugin-openh264 redefines version and release messing up requires

* Mon Nov 30 2015 Kalev Lember <klember@redhat.com> - 1.5.2-0.3.git21e44bd
- Include the gstreamer plugin in gstreamer1-plugin-openh264 subpackage

* Thu Nov 26 2015 Kalev Lember <klember@redhat.com> - 1.5.2-0.2.git21e44bd
- Pass Fedora LDFLAGS to the build to get full relro (#1285338)

* Tue Nov 24 2015 Kalev Lember <klember@redhat.com> - 1.5.2-0.1.git21e44bd
- Initial Fedora packaging
