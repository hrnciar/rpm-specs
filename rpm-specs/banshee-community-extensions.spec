%define		debug_package %{nil}

Name:		banshee-community-extensions
Version:	2.4.0
Release:	26%{?dist}
Summary:	Collection of extensions for the media player Banshee
License:	GPLv2+ and MIT
URL:		http://banshee-project.org/download/extensions/
Source0:	http://download.banshee-project.org/banshee-community-extensions/%{version}/%{name}-%{version}.tar.bz2
Patch0:		banshee-community-extensions-2.4.0-mono4.patch
Patch1:		banshee-community-extensions-2.4.0-gstreamer1-lastfmfingerprint.patch
Patch2:		banshee-community-extensions-2.4.0-gstreamer1-mirage.patch
Requires:	banshee
#Requires:	clutter-gtk010
BuildRequires:  gcc-c++
BuildRequires:	mono-devel, banshee-devel
BuildRequires:	intltool, gnome-sharp-devel
#BuildRequires:	clutter-gtk010-devel
#BuildRequires:	clutter-sharp-devel
BuildRequires:	fftw-devel, libsamplerate-devel, gstreamer1-devel, gstreamer1-plugins-base-devel
BuildRequires:	notify-sharp-devel
#BuildRequires:	webkit-sharp-devel
BuildRequires:	gnome-doc-utils, lirc-devel
BuildRequires:	autoconf, automake, libtool, GConf2-devel

# no need to provide banshee-mirage since no other package requires it
Obsoletes:	banshee-mirage < 0.6.1
Requires:	banshee

# Mono only available on these:
ExclusiveArch: %ix86 x86_64 ppc ppc64 ia64 %{arm} sparcv9 alpha s390x

%description
The Banshee Community Extensions contains a set of useful extensions
for the media player Banshee. 

%prep
%setup -q
%patch0 -p1 -b .mono4
%patch1 -p1 -b .lastfmfingerprint
%patch2 -p1 -b .mirage
sed -i "s#gstreamer-0.10#gstreamer-1.0#g" build/m4/extensions/mirage.m4 build/m4/extensions/lastfmfingerprint.m4
sed -i "s#gstreamer-base-0.10#gstreamer-base-1.0#g" build/m4/extensions/mirage.m4 build/m4/extensions/lastfmfingerprint.m4
sed -i "s#gstreamer-plugins-base-0.10#gstreamer-plugins-base-1.0#g" build/m4/extensions/mirage.m4 build/m4/extensions/lastfmfingerprint.m4
find . -name \* -type f -exec sed -i "s#libgstreamer-0.10.so.0#libgstreamer-1.0.so.0#g" {} \; -print
autoreconf -ifv

%build
sed -i "s#dbus-sharp-1.0#dbus-sharp-2.0#g" configure.ac
sed -i "s#dbus-sharp-glib-1.0#dbus-sharp-glib-2.0#g" configure.ac
%configure	--enable-gnome --disable-schemas-install \
		--enable-alarmclock \
		--enable-ampache \
		--disable-appindicator \
		--enable-awn \
		--disable-clutterflow \
		--enable-coverwallpaper \
		--disable-jamendo \
		--enable-lastfmfingerprint \
		--enable-lcd \
		--enable-lirc \
		--enable-liveradio \
		--disable-lyrics \
		--enable-magnatune \
		--enable-mirage \
		--disable-openvp \
		--enable-radiostationfetcher \
		--enable-randombylastfm \
		--enable-stream-recorder \
		--enable-telepathy  \
		--disable-zeitgeistdataprovider \
		--disable-karaoke
make V=1 %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install-strip
chmod 644 `find $RPM_BUILD_ROOT%{_libdir}/banshee/Extensions -name '*.dll.config'`

# delete unneeded *.(l)a files
find $RPM_BUILD_ROOT -name '*.la' -or -name '*.a' -exec rm -f {} \;

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING README NEWS
%{_libdir}/banshee/Extensions/*
%{_datadir}/gnome/help/banshee/*/*
#%{_datadir}/banshee-community-extensions/icons/hicolor/22x22/categories/jamendo.png


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 11 2020 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.4.0-25
- fixes to build with gstreamer1.0 using patches included in Ubuntu 18.04

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 26 2017 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 2.4.0-19
- Use dbus-sharp 2
- Disable jamendo, lyrics and karaoke. Require missing Banshee.WebBrowser

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-15
- mono rebuild for aarch64 support

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Tom Callaway <spot@fedoraproject.org> - 2.4.0-13
- fix compile in rawhide

* Tue Jan 26 2016 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 2.4.0-12
- Rebuild for taglib-sharp 2.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.4.0-10
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 18 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 2.4.0-8
- Remove obsolete BR (#1105994)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 17 2012 Kalev Lember <kalevlember@gmail.com> - 2.4.0-4
- Really rebuild with banshee 2.6.0

* Thu Oct 11 2012 Christian Krause <chkr@fedoraproject.org> - 2.4.0-3
- Rebuilt against banshee 2.6.0

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 09 2012 Christian Krause <chkr@fedoraproject.org> - 2.4.0-1
- Update to stable release 2.4.0

* Mon Mar 26 2012 Christian Krause <chkr@fedoraproject.org> - 2.2.0-3
- Rebuilt against banshee 2.4.0

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 18 2011 Christian Krause <chkr@fedoraproject.org> - 2.2.0-1
- Update to stable release 2.2.0
- Disable clutter support for now (clutter-gtk is linked against gtk3,
  but banshee / gtk-sharp is still using gtk2)

* Fri Oct 14 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 2.0.1-3
- rebuild for clutter-gtk010

* Sun May 08 2011 Christian Krause <chkr@fedoraproject.org> - 2.0.1-2
- Require clutter-gtk010

* Fri May 06 2011 Christian Krause <chkr@fedoraproject.org> - 2.0.1-1
- Update to stable release 2.0.1

* Tue Apr 05 2011 Christian Krause <chkr@fedoraproject.org> - 2.0.0-1
- Update to stable release 2.0.0

* Wed Mar 30 2011 Christian Krause <chkr@fedoraproject.org> - 1.9.6-1
- Update to development release 1.9.6

* Thu Mar 10 2011 Christian Krause <chkr@fedoraproject.org> - 1.9.5-1
- Update to development release 1.9.5
- Remove upstreamed patch

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 06 2011 Christian Krause <chkr@fedoraproject.org> - 1.9.3-1
- Update to development release 1.9.3

* Tue Feb  1 2011 Dan Horák <dan[at]danny.cz> - 1.9.2-2
- updated the supported arch list

* Sat Jan 15 2011 Christian Krause <chkr@fedoraproject.org> - 1.9.2-1
- Update to development release 1.9.2

* Tue Jan 11 2011 Christian Krause <chkr@fedoraproject.org> - 1.9.1-1
- Update to development release 1.9.1

* Mon Nov 01 2010 Christian Krause <chkr@fedoraproject.org> - 1.8.0-4
- Rebuilt against new clutter-sharp build

* Fri Oct 29 2010 Christian Krause <chkr@fedoraproject.org> - 1.8.0-3
- Rebuilt against Mono 2.8

* Sun Oct 03 2010 Nathaniel McCallum <nathaniel@natemccallum.com> - 1.8.0-2
- Fix permissions on dll.config files

* Sun Oct 03 2010 Nathaniel McCallum <nathaniel@natemccallum.com> - 1.8.0-1
- Update to 1.8.0
- Remove ipod-sharp and ndesk-dbus BR

* Wed Aug 18 2010 Christian Krause <chkr@fedoraproject.org> - 1.7.4-2
- Enable clutterflow extensions

* Tue Aug 17 2010 Christian Krause <chkr@fedoraproject.org> - 1.7.4-1
- Update to 1.7.4
- Add necessary BR

* Tue Jun 01 2010 Christian Krause <chkr@fedoraproject.org> - 1.6.0-2
- Rebuilt against new mono-addins

* Wed Mar 31 2010 Christian Krause <chkr@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0 release
- Remove upstreamed patch

* Sun Mar 28 2010 Christian Krause <chkr@fedoraproject.org> - 1.5.5-1
- Initial spec file
