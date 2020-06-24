# Review at https://bugzilla.redhat.com/show_bug.cgi?id=549593

%global minorversion 0.2

Name:           tumbler
Version:        0.2.8
Release:        3%{?dist}
Summary:        D-Bus service for applications to request thumbnails

License:        GPLv2+ and LGPLv2+
URL:            http://git.xfce.org/xfce/tumbler/
#VCS git:git://git.xfce.org/xfce/tumbler
Source0:        https://archive.xfce.org/src/xfce/tumbler/%{minorversion}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  freetype-devel
BuildRequires:  gettext
BuildRequires:  gtk2-devel >= 2.10.0
BuildRequires:  intltool
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  poppler-glib-devel
# extra thumbnailers
BuildRequires:  gstreamer1-plugins-base-devel
%{?fedora:BuildRequires: libgsf-devel}
%{?fedora:BuildRequires: libopenraw-gnome-devel}


%description
Tumbler is a D-Bus service for applications to request thumbnails for various
URI schemes and MIME types. It is an implementation of the thumbnail
management D-Bus specification described on
http://live.gnome.org/ThumbnailerSpec written in an object-oriented fashion

Additional thumbnailers can be found in the tumbler-extras package


%package extras
Summary:       Additional thumbnailers for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description extras
This package contains additional thumbnailers for file types, which are not used
very much and require additional libraries to be installed.


%package devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries and header files for developing applications 
that use %{name}.


%prep
%setup -q


%build
%configure --disable-static

# Omit unused direct shared library dependencies.
sed --in-place --expression 's! -shared ! -Wl,--as-needed\0!g' libtool

# Remove rpaths.
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install

# fix permissions for installed libs
chmod 755 $RPM_BUILD_ROOT/%{_libdir}/*.so

find %{buildroot} -type f -name "*.la" -delete

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%config(noreplace) %{_sysconfdir}/xdg/tumbler/
%{_datadir}/dbus-1/services/org.xfce.Tumbler.*.service
%{_libdir}/libtumbler-*.so.*
%{_libdir}/tumbler-*/
%exclude %{_libdir}/tumbler-*/plugins/tumbler-gst-thumbnailer.so
%exclude %{?fedora: %{_libdir}/tumbler-*/plugins/tumbler-raw-thumbnailer.so}


%files extras
%{_libdir}/tumbler-*/plugins/tumbler-gst-thumbnailer.so
%{?fedora:%{_libdir}/tumbler-*/plugins/tumbler-raw-thumbnailer.so}


%files devel
%{_libdir}/libtumbler-*.so
%{_libdir}/pkgconfig/%{name}-1.pc

%doc %{_datadir}/gtk-doc/

%dir %{_includedir}/%{name}-1
%{_includedir}/%{name}-1/tumbler


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 0.2.8-2
- Rebuild for poppler-0.84.0

* Sat Dec 21 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.8-1
- Update to 0.2.8
- Fix tarball source

* Mon Aug 12 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.7-1
- Update to 0.2.7

* Mon Jul 29 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.6-1
- Update to 0.2.6

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.5-1
- Update to 0.2.5

* Sat May 18 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.4-1
- Update to 0.2.4

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.3-1
- Update to 0.2.3

* Sat Sep 08 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.2-1
- Update to 0.2.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 01 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1
- Drop upstreamed patches
- Modernize spec

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Kevin Fenzi <kevin@scrye.com> - 0.2.0-1
- Update to 0.2. Fixes bug #1472022

* Fri Jul 07 2017 Kevin Fenzi <kevin@scrye.com> - 0.1.32-1
- Update to 0.1.32. Fixes bug #1468767

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 30 2016 Kevin Fenzi <kevin@scrye.com> - 0.1.31-5
- Conditionalize libopenraw patch for f26 and newer only

* Sat Dec 03 2016 Kevin Fenzi <kevin@scrye.com> - 0.1.31-4
- Rebuild for new libopenrawgnome

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 28 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.1.31-1
- Update to version 0.1.31

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 26 2014 Kevin Fenzi <kevin@scrye.com> 0.1.30-1
- Update to 0.1.30

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 05 2013 Kevin Fenzi <kevin@scrye.com> 0.1.29-1
- Update to 0.1.29

* Sun May 05 2013 Kevin Fenzi <kevin@scrye.com> 0.1.28-1
- Update to 0.1.28

* Sun Mar 31 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.27-3
- Make -extras package for GStreamer and RAW plugins
- Mark tumbler.rc as %%config(noreplace)

* Sun Mar 24 2013 Kevin Fenzi <kevin@scrye.com> 0.1.27-2
- Modify gstreamer BuildRequires (fixes bug #927011)
- Add new tumbler.rc file.

* Sun Mar 17 2013 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.27-1
- Update to 0.1.27

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 0.1.26-2
- rebuild due to "jpeg8-ABI" feature drop

* Sun Dec 09 2012 Kevin Fenzi <kevin@scrye.com> 0.1.26-1
- Update to 0.1.26

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 16 2012 Marek Kasik <mkasik@redhat.com> - 0.1.25-2
- Rebuild (poppler-0.20.0)

* Sun Apr 29 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.25-1
- Update to 0.1.25 (Xfce 4.10 final)
- Add VCS key

* Tue Apr 03 2012 Kevin Fenzi <kevin@scrye.com> - 0.1.24-1
- Update to 0.1.24

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 08 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.23-1
- Update to 0.1.23

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.1.22-5
- Rebuild for new libpng

* Sun Oct 16 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.22-4
- Fix thumbnail generation of the GStreamer plugin (#746110)
- Fix ownership race conditions when started twice (bugzilla.xfce.org #8001)

* Fri Sep 30 2011 Marek Kasik <mkasik@redhat.com> - 1.22-3
- Rebuild (poppler-0.18.0)

* Wed Sep 21 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.22-2
- Build the new GStreamer video thumbnailer

* Wed Sep 21 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.22-1
- Update to 1.22

* Mon Sep 19 2011 Marek Kasik <mkasik@redhat.com> - 1.21-3
- Rebuild (poppler-0.17.3)

* Fri Jul 15 2011 Marek Kasik <mkasik@redhat.com> - 1.21-2
- Rebuild (poppler-0.17.0)

* Mon Feb 14 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.21-1
- Update to 1.21

* Sat Feb 12 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.20-1
- Update to 1.20

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 16 2011 Kevin Fenzi <kevin@tummy.com> - 0.1.6-1
- Update to 0.1.6

* Sun Dec 05 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.5-1
- Update to 0.1.5

* Thu Nov 18 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4

* Wed Nov 03 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.3-1
- Update to 0.1.3
- Enable PDF thumbnails (BR poppler-glib-devel)

* Sat Jul 17 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2
- Own %%{_datadir}/gtk-doc/{html/} (#604169)
- Include NEWS in %%doc

* Thu Feb 25 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0.1.1-2
- Fix thumbnail support by including necessary BR's

* Fri Jan 15 2010 Debarshi Ray <rishi@fedoraproject.org> - 0.1.1-1
- Version bump to 0.1.1.
  * New fast JPEG thumbnailer with EXIF support
  * Report unsupported flavors back to clients via error signals
  * Translation updates: Swedish, Catalan, Galician, Japanese, Danish,
    Portuguese, Chinese
- Added 'BuildRequires: gtk2-devel'.
- Use sed instead of chrpath to remove rpaths. Remove 'BuildRequires: chrpath'.

* Tue Dec 22 2009 Rahul Sundaram <sundaram@fedoraproject.org> - 0.1.0-2
- Updated spec for review

* Sun Dec 20 2009 Debarshi Ray <rishi@fedoraproject.org> - 0.1.0-1
- Initial build.
