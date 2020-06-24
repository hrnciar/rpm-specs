%global srcname wxWidgets
%global wxbasename wxBase
%global gtk3dir bld_gtk3
%global sover 3

Name:           wxGTK
Version:        3.1.3
Release:        1%{?dist}
Summary:        GTK port of the wxWidgets GUI library
License:        wxWidgets
URL:            https://www.wxwidgets.org/

Source0:        https://github.com/%{srcname}/%{srcname}/releases/download/v%{version}/%{srcname}-%{version}.tar.bz2
Source10:       wx-config
# https://bugzilla.redhat.com/show_bug.cgi?id=1225148
# remove abort when ABI check fails
# Backport from wxGTK
Patch0:         %{name}-3.0.3-abicheck.patch
Patch1:         disable-tests-failing-mock.patch
Patch2:         update-license-text.patch
Patch3:         fix-tests-ppc64le.patch
Patch4:         fix-tests-s390x.patch

BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel
BuildRequires:  webkit2gtk3-devel
BuildRequires:  zlib-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  expat-devel
BuildRequires:  SDL2-devel
BuildRequires:  libGLU-devel
BuildRequires:  libSM-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  GConf2-devel
BuildRequires:  gettext
BuildRequires:  cppunit-devel
BuildRequires:  libmspack-devel
BuildRequires:  doxygen
BuildRequires:  graphviz

Provides:       %{srcname} = %{version}-%{release}
Provides:       bundled(scintilla) = 3.7.2
Requires:       %{wxbasename}%{?_isa} = %{version}-%{release}
Requires:       %{name}-i18n = %{version}-%{release}

%description
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.


%package -n     %{wxbasename}-devel
Summary:        Development files for the wxBase3 library
Requires:       %{wxbasename}%{?_isa} = %{version}-%{release}
Requires(post): /usr/sbin/update-alternatives
Requires(postun): /usr/sbin/update-alternatives

%description -n %{wxbasename}-devel
This package include files needed to link with the wxBase3 library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.


%package        devel
Summary:        Development files for the wxGTK library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-gl = %{version}-%{release}
Requires:       %{name}-media = %{version}-%{release}
Requires:       %{name}-webview = %{version}-%{release}
Requires:       %{wxbasename} = %{version}-%{release}
Requires:       %{wxbasename}-devel%{?_isa} = %{version}-%{release}
Requires:       gtk3-devel
Requires:       libGLU-devel
Provides:       %{srcname}-devel = %{version}-%{release}

%description devel
This package include files needed to link with the wxGTK library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.


%package        gl
Summary:        OpenGL add-on for the wxWidgets library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description gl
OpenGL (a 3D graphics API) add-on for the wxWidgets library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.


%package        i18n
Summary:        i18n message catalogs for the wxWidgets library
BuildArch:      noarch

%description i18n
i18n message catalogs for the wxWidgets library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.


%package        media
Summary:        Multimedia add-on for the wxWidgets library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description media
Multimedia add-on for the wxWidgets library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.


%package        webview
Summary:        WebView add-on for the wxWidgets library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description webview
WebView add-on for the wxWidgets library.
wxWidgets is the GTK port of the C++ cross-platform wxWidgets
GUI library, offering classes for all common GUI controls as well as a
comprehensive set of helper classes for most common application tasks,
ranging from networking to HTML display and image manipulation.


%package -n     %{wxbasename}
Summary:        Non-GUI support classes from the wxWidgets library

%description -n %{wxbasename}
Every wxWidgets application must link against this library. It contains
mandatory classes that any wxWidgets code depends on (like wxString) and
portability classes that abstract differences between platforms. wxBase can
be used to develop console mode applications -- it does not require any GUI
libraries or the X Window System.


%package        docs
Summary:        Documentation for the wxGTK library
Requires:       %{name} = %{version}-%{release}
Provides:       %{srcname}-docs = %{version}-%{release}
BuildArch:      noarch

%description docs
This package provides documentation for the %{srcname} library.


%prep
%autosetup -n %{srcname}-%{version} -p1

# patch some installed files to avoid conflicts with 2.8.*
sed -i -e 's|aclocal)|aclocal/wxwin31.m4)|' Makefile.in
sed -i -e 's|wxstd.mo|wxstd31.mo|' Makefile.in
sed -i -e 's|wxmsw.mo|wxmsw31.mo|' Makefile.in

# fix plugin dir for 64-bit
sed -i -e 's|/usr/lib\b|%{_libdir}|' wx-config.in configure
sed -i -e 's|/lib|/%{_lib}|' src/unix/stdpaths.cpp


%build
%global _configure ../configure

mkdir %{gtk3dir}
pushd %{gtk3dir}
%configure \
  --with-gtk=3 \
  --with-opengl \
  --with-sdl \
  --with-libmspack \
  --enable-intl \
  --disable-rpath \
  --enable-ipv6

%make_build
popd

#Docs
WX_SKIP_DOXYGEN_VERSION_CHECK=1 docs/doxygen/regen.sh html
mv docs/doxygen/out/html .

%install
pushd %{gtk3dir}
%make_install
popd

# install our multilib-aware wrapper
##Remove installed
rm %{buildroot}%{_bindir}/wx-config
##Install new and symlink
install -p -D -m 755 %{SOURCE10} %{buildroot}%{_libexecdir}/%{name}/wx-config
sed -i -e 's|=/usr|=%{_prefix}|' %{buildroot}%{_libexecdir}/%{name}/wx-config
ln -s ../..%{_libexecdir}/%{name}/wx-config %{buildroot}%{_bindir}/wx-config-3.1
touch %{buildroot}%{_bindir}/wx-config

#Alternatives setup with wxrc
mv %{buildroot}%{_bindir}/wxrc* %{buildroot}%{_libexecdir}/%{name}
ln -s ../..%{_libexecdir}/%{name}/wxrc-3.1 %{buildroot}%{_bindir}/wxrc-3.1
touch %{buildroot}%{_bindir}/wxrc

# move bakefiles to avoid conflicts with 2.8.*
mkdir %{buildroot}%{_datadir}/bakefile/presets/wx31
mv %{buildroot}%{_datadir}/bakefile/presets/*.* %{buildroot}%{_datadir}/bakefile/presets/wx31

%find_lang wxstd31
%find_lang wxmsw31
cat wxmsw31.lang >> wxstd31.lang

%check
pushd %{gtk3dir}/tests
make %{?_smp_mflags}
LD_LIBRARY_PATH=%{buildroot}%{_libdir} TZ=UTC ./test
popd

%post -n %{wxbasename}-devel
if [ -f %{_bindir}/wx-config ] && [ ! -h %{_bindir}/wx-config ] ; then
  rm %{_bindir}/wx-config
fi
/usr/sbin/update-alternatives --install %{_bindir}/wx-config \
  wx-config %{_libexecdir}/%{name}/wx-config 25
/usr/sbin/update-alternatives --install %{_bindir}/wxrc \
  wxrc %{_libexecdir}/%{name}/wxrc 25

%postun -n %{wxbasename}-devel
if [ $1 -eq 0 ] ; then
  /usr/sbin/update-alternatives --remove wx-config %{_libexecdir}/%{name}/wx-config
  /usr/sbin/update-alternatives --remove wxrc %{_libexecdir}/%{name}/wxrc
fi

%files
%doc docs/changes.txt docs/readme.txt
%license docs/gpl.txt docs/lgpl.txt docs/licence.txt docs/licendoc.txt
%license docs/preamble.txt
%{_libdir}/libwx_gtk3u_adv-*.so.%{sover}*
%{_libdir}/libwx_gtk3u_aui-*.so.%{sover}*
%{_libdir}/libwx_gtk3u_core-*.so.%{sover}*
%{_libdir}/libwx_gtk3u_html-*.so.%{sover}*
%{_libdir}/libwx_gtk3u_propgrid-*.so.%{sover}*
%{_libdir}/libwx_gtk3u_qa-*.so.%{sover}*
%{_libdir}/libwx_gtk3u_ribbon-*.so.%{sover}*
%{_libdir}/libwx_gtk3u_richtext-*.so.%{sover}*
%{_libdir}/libwx_gtk3u_stc-*.so.%{sover}*
%{_libdir}/libwx_gtk3u_xrc-*.so.%{sover}*

%files -n %{wxbasename}-devel
%ghost %{_bindir}/wx-config
%ghost %{_bindir}/wxrc
%{_bindir}/wxrc-3.1
%{_bindir}/wx-config-3.1
%{_includedir}/wx-3.1
%{_libdir}/libwx_baseu*.so
%dir %{_libdir}/wx
%dir %{_libdir}/wx/config
%dir %{_libdir}/wx/include
%{_datadir}/aclocal/wxwin31.m4
%{_datadir}/bakefile/presets/wx31
%{_libexecdir}/%{name}

%files devel
%{_libdir}/libwx_gtk3u_*.so
%{_libdir}/wx/config/gtk3-unicode-3.1
%{_libdir}/wx/include/gtk3-unicode-3.1

%files gl
%{_libdir}/libwx_gtk3u_gl-*.so.%{sover}*

%files i18n -f wxstd31.lang

%files media
%{_libdir}/libwx_gtk3u_media-*.so.%{sover}*

%files webview
%{_libdir}/libwx_gtk3u_webview-*.so.%{sover}*
%dir %{_libdir}/wx
%{_libdir}/wx/%{version}

%files -n %{wxbasename}
%doc docs/changes.txt docs/readme.txt
%license docs/gpl.txt docs/lgpl.txt docs/licence.txt docs/licendoc.txt
%license docs/preamble.txt
%{_libdir}/libwx_baseu-*.so.*
%{_libdir}/libwx_baseu_net-*.so.%{sover}*
%{_libdir}/libwx_baseu_xml-*.so.%{sover}*

%files docs
%doc html

%changelog
* Tue Mar 03 2020 Scott Talbert <swt@techie.net> - 3.1.3-1
- Initial packaging of wxWidgets 3.1.x (dev version) (#1714714)
