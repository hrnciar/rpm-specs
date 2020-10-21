%{?mingw_package_header}

Name:           mingw-colorhug-client
Version:        0.2.6
Release:        13%{?dist}
Summary:        MinGW Tools for the Hughski ColorHug

License:        GPLv2+
URL:            http://www.hughski.com/
Source0:        http://people.freedesktop.org/~hughsient/releases/colorhug-client-%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-glib2
BuildRequires:  mingw32-libsoup
BuildRequires:  mingw64-libsoup
BuildRequires:  mingw32-colord-gtk
BuildRequires:  mingw64-colord-gtk
BuildRequires:  mingw32-libgusb >= 0.2.3
BuildRequires:  mingw64-libgusb >= 0.2.3
BuildRequires:  intltool
BuildRequires:  itstool

%description
The Hughski ColorHug colorimeter is a low cost open-source hardware
sensor used to calibrate screens.

This package includes the client tools which allows the user to upgrade
the firmware on the sensor or to access the sensor from command line
scripts.

This is the MinGW version of these tools.

%package -n mingw32-colorhug-client
Summary:        MinGW Tools for the Hughski ColorHug
Requires:       mingw32-adwaita-icon-theme
Requires:       mingw32-glib-networking
Requires:       mingw32-librsvg2
Requires:       mingw32-hicolor-icon-theme

%description -n mingw32-colorhug-client
The Hughski ColorHug colorimeter is a low cost open-source hardware
sensor used to calibrate screens.

This package includes the client tools which allows the user to upgrade
the firmware on the sensor or to access the sensor from command line
scripts.

This is the MinGW version of these tools.

%package -n mingw64-colorhug-client
Summary:        MinGW Tools for the Hughski ColorHug
Requires:       mingw64-adwaita-icon-theme
Requires:       mingw64-glib-networking
Requires:       mingw64-librsvg2
Requires:       mingw64-hicolor-icon-theme

%description -n mingw64-colorhug-client
The Hughski ColorHug colorimeter is a low cost open-source hardware
sensor used to calibrate screens.

This package includes the client tools which allows the user to upgrade
the firmware on the sensor or to access the sensor from command line
scripts.

This is the MinGW version of these tools.

%{?mingw_debug_package}


%prep
%setup -q -n colorhug-client-%{version}


%build
%mingw_configure                \
        --enable-release        \
        --disable-bash-completion \
        --without-pic
%mingw_make %{?_smp_mflags} V=1


%install
%mingw_make_install "DESTDIR=$RPM_BUILD_ROOT"

%mingw_find_lang colorhug-client

%post
/bin/touch --no-create %{mingw32_datadir}/icons/hicolor &>/dev/null || :
/bin/touch --no-create %{mingw64_datadir}/icons/hicolor &>/dev/null || :
glib-compile-schemas %{mingw32_datadir}/glib-2.0/schemas &> /dev/null || :
glib-compile-schemas %{mingw64_datadir}/glib-2.0/schemas &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{mingw32_datadir}/icons/hicolor &>/dev/null
    /bin/touch --no-create %{mingw64_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{mingw32_datadir}/icons/hicolor &>/dev/null || :
    /usr/bin/gtk-update-icon-cache %{mingw64_datadir}/icons/hicolor &>/dev/null || :
fi
glib-compile-schemas %{mingw32_datadir}/glib-2.0/schemas &> /dev/null || :
glib-compile-schemas %{mingw64_datadir}/glib-2.0/schemas &> /dev/null || :

%posttrans
/usr/bin/gtk-update-icon-cache %{mingw32_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/gtk-update-icon-cache %{mingw64_datadir}/icons/hicolor &>/dev/null || :


%files -n mingw32-colorhug-client -f mingw32-colorhug-client.lang
%doc AUTHORS COPYING README NEWS
%{mingw32_bindir}/*.exe
%{mingw32_datadir}/glib-2.0/schemas/com.hughski.colorhug-client.gschema.xml
%{mingw32_datadir}/icons/hicolor/*/apps/*
%{mingw32_datadir}/icons/hicolor/*/mimetypes/*

%files -n mingw64-colorhug-client -f mingw64-colorhug-client.lang
%doc AUTHORS COPYING README NEWS
%{mingw64_bindir}/*.exe
%{mingw64_datadir}/glib-2.0/schemas/com.hughski.colorhug-client.gschema.xml
%{mingw64_datadir}/icons/hicolor/*/apps/*
%{mingw64_datadir}/icons/hicolor/*/mimetypes/*

%changelog
* Wed Aug 12 13:35:38 GMT 2020 Sandro Mani <manisandro@gmail.com> - 0.2.6-13
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 0.2.6-11
- Rebuild (gettext)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 10 2015 Richard Hughes <richard@hughsie.com> - 0.2.6-1
- Update to latest upstream version

* Wed Nov 19 2014 Richard Hughes <richard@hughsie.com> - 0.2.4-1
- Initial packaging attempt
