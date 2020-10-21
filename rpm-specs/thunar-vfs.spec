# Review at https://bugzilla.redhat.com/show_bug.cgi?id=660159

%global minorversion 1.2

Name:           thunar-vfs
Version:        1.2.0
Release:        27%{?dist}
Summary:        Virtual filesystem shipped with Thunar 1.0 and earlier releases

License:        LGPLv2+
URL:            http://thunar.xfce.org
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2
Patch1:         http://ausil.fedorapeople.org/aarch64/thunar-vcs-plugin/thunar-vcs-plugin-aarch64.patch

BuildRequires:  gcc
BuildRequires:  libxfce4util-devel >= 4.6.0
BuildRequires:  exo-devel >= 0.5.4
BuildRequires:  dbus-glib-devel 
BuildRequires:  gamin-devel
BuildRequires:  GConf2-devel
BuildRequires:  startup-notification-devel >= 0.4
BuildRequires:  freetype-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel >= 2:1.2.2-16
BuildRequires:  intltool gettext
BuildRequires:  desktop-file-utils
Conflicts:      Thunar < 1.1.0
# Add until perl / perl-Carp is fixed. 
BuildRequires:  perl-Carp

%description
This package contains the virtual filesystem shipped with Thunar 1.0 and earlier
releases. It provides compatibility for applications that still use thunar-vfs 
while Thunar was ported to GVFS.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup


%build
%configure --disable-static --disable-gtk-doc
%make_build


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%find_lang %{name}
# remove duplicate docs
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

%check
make tests

%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README 
%doc docs/ThumbnailersCacheFormat.txt docs/README.volumes
%{_libdir}/*.so.*
%{_libdir}/thunar-vfs-*/
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/thunar-vfs-font-thumbnailer-1.desktop

%files devel
%doc HACKING TODO
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/thunar-vfs-*.pc

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 11 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.2.0-22
- spec cleanup + spec modernization
- Fix FTBFS by disabling regeneration of documentation at build time. This is
                    because gtkdoc-mktmpl has been removed as of gtk-doc-1.26

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 28 2015 Kevin Fenzi <kevin@scrye.com> 1.2.0-15
- Rebuild for Xfce 4.12

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 23 2013 Kevin Fenzi <kevin@scrye.com> 1.2.0-11
- Add patch for aarch64 support. Fixes bug #926631

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 1.2.0-9
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.2.0-8
- rebuild against new libjpeg

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 04 2012 Kevin Fenzi <kevin@scrye.com> - 1.2.0-6
- Rebuild for Xfce 4.10

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.2.0-4
- Rebuild for new libpng

* Tue Apr 26 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.2.0-3
- No longer BuildRequire hal-devel

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 16 2011 Kevin Fenzi <kevin@tummy.com> - 1.2.0-1
- Update to 1.2.0

* Mon Nov 08 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.1-1
- Initial package
