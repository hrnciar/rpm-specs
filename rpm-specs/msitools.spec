#define _version_suffix

# The mingw* RPMs are noarch, and the wxi data files are
# arch independant, so it is a waste of CPU cycles to run
# validation on all arches. Just run on x86_64 since that
# has the fastest Fedora builders.
%ifarch x86_64
%define with_validate 1
%else
%define with_validate 0
%endif

Name:           msitools
Version:        0.100
Release:        4%{?dist}
Summary:        Windows Installer tools

License:        GPLv2+
URL:            http://ftp.gnome.org/pub/GNOME/sources/%{name}
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{version}/%{name}-%{version}%{?_version_suffix}.tar.xz

# Some patches from upstream post 0.100
Patch0001: 0001-data-wixl-remove-nss-nspr.patch
Patch0002: 0002-ilmbase.wxi-update-v2.4.patch
Patch0003: 0003-OpenEXR.wxi-path-fixes-for-v2.4.patch
Patch0004: 0004-adwaita-icon-theme.wxi-update-to-v3.34.3.patch
Patch0005: 0005-libvirt.wxi-depends-on-glib2-these-days.patch
Patch0006: 0006-data-update-adwaita-icon-theme.wxi.patch
Patch0007: 0007-data-update-atk.wxi.patch
Patch0008: 0008-data-update-gdk-pixbuf-deps.patch
Patch0009: 0009-Update-file-manifest-for-gstreamer1-plugins-bad-free.patch
# Non-upstream patch to fix tarball missing the brotli.wxi file
# Upstream fixed as side effect of the switch to meson.
Patch0010: 0010-Add-brotli-files-missing-in-upstream-release-tarball.patch
Patch0011: 0011-wixl-switch-spice-glib-back-to-dsound-driver.patch

Requires:       libgsf >= 1.14.24-2

BuildRequires:  git
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  libgcab1-devel >= 0.2
BuildRequires:  libgsf-devel
BuildRequires:  libuuid-devel
BuildRequires:  vala
BuildRequires:  bison
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%if %{with_validate}
BuildRequires:  perl
BuildRequires:  perl-XML-XPath
BuildRequires:  mingw32-adwaita-icon-theme
BuildRequires:  mingw64-adwaita-icon-theme
BuildRequires:  mingw32-atk
BuildRequires:  mingw64-atk
BuildRequires:  mingw32-brotli
BuildRequires:  mingw64-brotli
BuildRequires:  mingw32-bzip2
BuildRequires:  mingw64-bzip2
BuildRequires:  mingw32-cairo
BuildRequires:  mingw64-cairo
BuildRequires:  mingw32-celt051
BuildRequires:  mingw64-celt051
BuildRequires:  mingw32-curl
BuildRequires:  mingw64-curl
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw32-expat
BuildRequires:  mingw64-expat
BuildRequires:  mingw32-fontconfig
BuildRequires:  mingw64-fontconfig
BuildRequires:  mingw32-freetype
BuildRequires:  mingw64-freetype
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-gdk-pixbuf
BuildRequires:  mingw64-gdk-pixbuf
BuildRequires:  mingw32-gettext
BuildRequires:  mingw64-gettext
BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-glib2
BuildRequires:  mingw32-glib-networking
BuildRequires:  mingw64-glib-networking
BuildRequires:  mingw32-gmp
BuildRequires:  mingw64-gmp
BuildRequires:  mingw32-gnutls
BuildRequires:  mingw64-gnutls
BuildRequires:  mingw32-gsm
BuildRequires:  mingw64-gsm
BuildRequires:  mingw32-gstreamer1-plugins-bad-free
BuildRequires:  mingw64-gstreamer1-plugins-bad-free
BuildRequires:  mingw32-gstreamer1-plugins-base
BuildRequires:  mingw64-gstreamer1-plugins-base
BuildRequires:  mingw32-gstreamer1-plugins-good
BuildRequires:  mingw64-gstreamer1-plugins-good
BuildRequires:  mingw32-gstreamer1
BuildRequires:  mingw64-gstreamer1
BuildRequires:  mingw32-gstreamer-plugins-bad-free
BuildRequires:  mingw64-gstreamer-plugins-bad-free
BuildRequires:  mingw32-gstreamer-plugins-base
BuildRequires:  mingw64-gstreamer-plugins-base
BuildRequires:  mingw32-gstreamer-plugins-good
BuildRequires:  mingw64-gstreamer-plugins-good
BuildRequires:  mingw32-gstreamer
BuildRequires:  mingw64-gstreamer
BuildRequires:  mingw32-gtk2
BuildRequires:  mingw64-gtk2
BuildRequires:  mingw32-gtk3
BuildRequires:  mingw64-gtk3
BuildRequires:  mingw32-gtk-vnc2
BuildRequires:  mingw64-gtk-vnc2
BuildRequires:  mingw32-gvnc
BuildRequires:  mingw64-gvnc
BuildRequires:  mingw32-harfbuzz
BuildRequires:  mingw64-harfbuzz
BuildRequires:  mingw32-hicolor-icon-theme
BuildRequires:  mingw64-hicolor-icon-theme
BuildRequires:  mingw32-icu
BuildRequires:  mingw64-icu
BuildRequires:  mingw32-ilmbase
BuildRequires:  mingw64-ilmbase
BuildRequires:  mingw32-jasper
BuildRequires:  mingw64-jasper
BuildRequires:  mingw32-json-glib
BuildRequires:  mingw64-json-glib
BuildRequires:  mingw32-libepoxy
BuildRequires:  mingw64-libepoxy
BuildRequires:  mingw32-libffi
BuildRequires:  mingw64-libffi
BuildRequires:  mingw32-libgcrypt
BuildRequires:  mingw64-libgcrypt
BuildRequires:  mingw32-libgovirt
BuildRequires:  mingw64-libgovirt
BuildRequires:  mingw32-libgpg-error
BuildRequires:  mingw64-libgpg-error
BuildRequires:  mingw32-libidn2
BuildRequires:  mingw64-libidn2
BuildRequires:  mingw32-libjpeg-turbo
BuildRequires:  mingw64-libjpeg-turbo
BuildRequires:  mingw32-libogg
BuildRequires:  mingw64-libogg
BuildRequires:  mingw32-libpng
BuildRequires:  mingw64-libpng
BuildRequires:  mingw32-libpsl
BuildRequires:  mingw64-libpsl
BuildRequires:  mingw32-libsoup
BuildRequires:  mingw64-libsoup
BuildRequires:  mingw32-libssh2
BuildRequires:  mingw64-libssh2
BuildRequires:  mingw32-libtasn1
BuildRequires:  mingw64-libtasn1
BuildRequires:  mingw32-libtheora
BuildRequires:  mingw64-libtheora
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw64-libtiff
BuildRequires:  mingw32-libunistring
BuildRequires:  mingw64-libunistring
BuildRequires:  mingw32-libusbx
BuildRequires:  mingw64-libusbx
BuildRequires:  mingw32-libvirt-glib
BuildRequires:  mingw64-libvirt-glib
BuildRequires:  mingw32-libvirt
BuildRequires:  mingw64-libvirt
BuildRequires:  mingw32-libvorbis
BuildRequires:  mingw64-libvorbis
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw64-libxml2
BuildRequires:  mingw32-nettle
BuildRequires:  mingw64-nettle
BuildRequires:  mingw32-OpenEXR
BuildRequires:  mingw64-OpenEXR
BuildRequires:  mingw32-openssl
BuildRequires:  mingw64-openssl
BuildRequires:  mingw32-opus
BuildRequires:  mingw64-opus
BuildRequires:  mingw32-orc
BuildRequires:  mingw64-orc
BuildRequires:  mingw32-p11-kit
BuildRequires:  mingw64-p11-kit
BuildRequires:  mingw32-pango
BuildRequires:  mingw64-pango
BuildRequires:  mingw32-pcre
BuildRequires:  mingw64-pcre
BuildRequires:  mingw32-pixman
BuildRequires:  mingw64-pixman
BuildRequires:  mingw32-portablexdr
BuildRequires:  mingw64-portablexdr
BuildRequires:  mingw32-readline
BuildRequires:  mingw64-readline
BuildRequires:  mingw32-rest
BuildRequires:  mingw64-rest
BuildRequires:  mingw32-SDL
BuildRequires:  mingw64-SDL
BuildRequires:  mingw32-speex
BuildRequires:  mingw64-speex
BuildRequires:  mingw32-spice-glib
BuildRequires:  mingw64-spice-glib
BuildRequires:  mingw32-spice-gtk3
BuildRequires:  mingw64-spice-gtk3
BuildRequires:  mingw32-sqlite
BuildRequires:  mingw64-sqlite
BuildRequires:  mingw32-termcap
BuildRequires:  mingw64-termcap
BuildRequires:  mingw32-usbredir
BuildRequires:  mingw64-usbredir
BuildRequires:  mingw32-wavpack
BuildRequires:  mingw64-wavpack
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw32-winpthreads
BuildRequires:  mingw64-winpthreads
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-zlib
%endif

%description
msitools is a collection of utilities to inspect and create Windows
Installer files.  It is useful in a cross-compilation environment such
as fedora-mingw.

%package -n libmsi1
Summary:        A library to manipulate Windows .MSI files
License:        LGPLv2+

%description -n libmsi1
libmsi is a GObject library to work with Windows Installer files.  It is
a port from the MSI library of the Wine project.

%package -n libmsi1-devel
Summary:        A library to manipulate Windows .MSI files
License:        LGPLv2+
Requires:       libmsi1%{?_isa} = %{version}-%{release}

%description -n libmsi1-devel
The libmsi1-devel package includes the header files for libmsi.

%prep
%autosetup -S git_am -n msitools-%{version}%{?_version_suffix}

%build
autoreconf -i -f
%configure --enable-fast-install
make %{?_smp_mflags} V=1


%install
%make_install

rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*.la

%find_lang %{name}

%if %{with_validate}
%check
make -C data check-wxi
%endif

%ldconfig_scriptlets -n libmsi1

%files
%doc COPYING NEWS README.md TODO
%{_bindir}/msibuild
%{_bindir}/msidiff
%{_bindir}/msidump
%{_bindir}/msiextract
%{_bindir}/msiinfo
%{_bindir}/wixl
%{_bindir}/wixl-heat
%{_datadir}/bash-completion/completions/msitools
%{_datadir}/wixl-%{version}%{?_version_suffix}

%files -n libmsi1 -f %{name}.lang
%doc COPYING.LIB
%{_libdir}/girepository-1.0/Libmsi-1.0.typelib
%{_libdir}/libmsi.so.0*

%files -n libmsi1-devel
%{_datadir}/gir-1.0/Libmsi-1.0.gir
%{_datadir}/vala/vapi/libmsi-1.0.vapi
%{_includedir}/libmsi-1.0/*
%{_libdir}/libmsi.so
%{_libdir}/pkgconfig/libmsi-1.0.pc


%changelog
* Thu May 14 2020 Daniel P. Berrangé <berrange@redhat.com> - 0.100-4
- Switch spice back to dsound instead of wasapi

* Thu Apr 23 2020 Daniel P. Berrangé <berrange@redhat.com> - 0.100-3
- Re-enable wix validation
- Fix bugs in multiple wxi manifests

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.100-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.100-1
- new version

* Mon Aug 12 2019 Fabiano Fidêncio <fidencio@redhat.com> - 0.99-4
- Remove mingw*-gtk-vnc dependency
- Temporarily disable wxi validation
- Update ilmbase and OpenEXR to 2.3.0 release, rhbz#1736147

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 19 2019 Daniel P. Berrangé <berrange@redhat.com> - 0.99-2
- Validate wxi files during build

* Fri Feb 15 2019 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.99-1
- new version

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 0.98-3
- Update BRs for vala packaging changes

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 02 2018 Victor Toso <victortoso@redhat.com> - 0.98-1
- Update to 0.98

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.97-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.97-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jul 31 2017 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.97-2
- Add a patch to fix spice packaging

* Mon Jul 31 2017 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.97-1
- Upstream release 0.97

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 09 2016 Fabiano Fidêncio <fidencio@redhat.com> - 0.96-1

* Wed Jun 22 2016 Fabiano Fidêncio <fidencio@redhat.com> - 0.95-5
- Add libpcre as glib dependency

* Mon May 02 2016 Fabiano Fidêncio <fidencio@redhat.com> - 0.95-4
- Fix libvirt-glib's translations
- Add adwaita-icon-theme

* Tue Feb 23 2016 Fabiano Fidêncio <fidencio@redhat.com> - 0.95-3
- Add libvirt-glib.wxi
- Update nettle to 3.2.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 01 2015 Fabiano Fidêncio <fidencio@redhat.com> - 0.95-1
- Upstream release 0.95

* Fri Jun 19 2015 Fabiano Fidêncio <fidencio@redhat.com> - 0.94-2
- Add libepoxy.wxi
- Add libepoxy as gtk3 dep

* Tue Jun 16 2015 Fabiano Fidêncio <fidencio@redhat.com> - 0.94-1
- Upstream release 0.94

* Mon Jan  5 2015 Fabiano Fidêncio <fidencio@redhat.com> - 0.93.75-2
- Update spice-glib.wxi to use gstreamer1

* Wed Dec 10 2014 Fabiano Fidêncio <fidencio@redhat.com> - 0.93.75-1
- Update to upstream msitool-0.93.75-f89b

* Tue Oct  7 2014 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.93.43-1
- Set the ALLUSERS=1 property when the install scope is perMachine, rhbz#1146586

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93.40-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.93.40-2
- Rebuilt for gobject-introspection 1.41.4

* Mon Jun  9 2014 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.93.40-1
- Update nettle.wxi for f20, rhbz#1106437

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 10 2014 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.93.28-1
- Update libvirt.wxi for f20

* Tue Dec 17 2013 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.93.24-1
- Update libpng for f20

* Sat Nov  9 2013 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.93.20-1
- Fix component id stability
- Fix libmsi crash, rhbz#1027256

* Tue Aug 13 2013 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.93.6-1
- Update to upstream 0.93.6-74a2, fixes RegLocator

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 11 2013 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.93-1
- Upstream release 0.93

* Fri Apr 12 2013 Marc-André Lureau <marcandre.lureau@gmail.com> - 0.92.26-1
- 0.92.26 snapshot from upstream, fix f19 includes
- Add x64 build support

* Thu Apr 11 2013 Marc-André Lureau <marcandre.lureau@gmail.com> - 0.92-5
- Forgot a patch

* Fri Apr  5 2013 Marc-André Lureau <marcandre.lureau@gmail.com> - 0.92-4
- More f19 wxi updates

* Thu Apr  4 2013 Marc-André Lureau <marcandre.lureau@gmail.com> - 0.92-3
- Remove obsolete file in glib.wxi

* Wed Apr  3 2013 Marc-André Lureau <marcandre.lureau@gmail.com> - 0.92-2
- Add a glib.wxi workaround for win64

* Thu Mar  7 2013 Marc-André Lureau <marcandre.lureau@gmail.com> - 0.92-1
- New upstream release.
- Add msidump & msidiff tools.
- Add translations.

* Fri Feb 15 2013 Paolo Bonzini <pbonzini@redhat.com> - 0.91-3
- Add dependency of libmsi1-devel on libmsi1, reformatted descriptions.

* Thu Feb 14 2013 Paolo Bonzini <pbonzini@redhat.com> - 0.91-2
- Remove invalid characters from package names, added vala-tools
  BuildRequires.

* Mon Jan 28 2013 Paolo Bonzini <pbonzini@redhat.com> - 0.91-1
- New upstream version.

* Wed Jan 16 2013 Paolo Bonzini <pbonzini@redhat.com> - 0.90-1
- Added wixl and devel packages.

* Thu Dec 6 2012 Paolo Bonzini <pbonzini@redhat.com> - 0.01-1
- Initial version.
