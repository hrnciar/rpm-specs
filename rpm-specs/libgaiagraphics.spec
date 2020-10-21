# The author is aware of the exit calls in the library.
# He adopted it from libGD code. (July 2012)
Name:           libgaiagraphics
Version:        0.5
Release:        18%{?dist}
Summary:        Graphics canvas for GIS rendering

License:        LGPLv3+
URL:            https://www.gaia-gis.it/fossil/libgaiagraphics
Source0:        http://www.gaia-gis.it/gaia-sins/%{name}-%{version}.tar.gz

# Buildroot and the likes are left in place for ELGIS 5

BuildRequires:  libtool automake autoconf
BuildRequires:  cairo-devel
BuildRequires:  libgeotiff-devel 
BuildRequires:  libjpeg-devel 
BuildRequires:  libpng-devel
BuildRequires:  libxml2-devel
# Is only checked for, but not actually used
BuildRequires:  proj-devel

%description
Libgaiagraphics wraps raster- and vector graphics, to implement a reasonably
abstract and platform independent graphics canvas for GIS rendering.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

%build
# Informed the author about BZ 925732 (April 2014)
autoreconf -fi
%configure --disable-static

# Remove links to unused libraries
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

# Delete libtool archives, because we don't ship them
find %{buildroot} -name '*.la' -exec rm -f {} ';'



%ldconfig_scriptlets


%files
%doc AUTHORS COPYING
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/gaiagraphics.h
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/gaiagraphics.pc

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 11 2015 Devrim Gündüz <devrim@gunduz.org> - 0.5-7
- Rebuilt for Proj 4.9.1

* Mon Aug 25 2014 Devrim Gündüz <devrim@gunduz.org> - 0.5-6
- Rebuilt for libgeotiff

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 26 2014 Volker Fröhlich <volker27@gmx.at> - 0.5-3
- Allow aarch64 builds (BZ 925732) by running autoreconf

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr  4 2013 Volker Fröhlich <volker27@gmx.at> - 0.5-1
- New upstream version 0.5

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4b-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 0.4b-4
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.4b-3
- rebuild against new libjpeg

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 11 2012 Volker Fröhlich <volker27@gmx.at> - 0.4b-1
- Update for new release
- Update URL and source URL
- Drop LGPL source, upstream includes the proper license now
- Drop libgeotiff patch, configure now searches in 
  include/libgeotiff now as well
- Subsequently drop BR autoconf

* Wed Nov 23 2011 Volker Fröhlich <volker27@gmx.at> - 0.4-3
- Replace wrong license file

* Sun Oct 30 2011 Volker Fröhlich <volker27@gmx.at> - 0.4-2
- Place isa in devel package's Requires
- Correct license to LPGLv3+
- Correct spelling of the name in description
- More specific file list
- Add Requires for pkgconfig to devel sub-package (EPEL 5)
- Switch to name and version macro in source URL
- Remove zlib-devel as BR; libpng-devel already requires it

* Tue Jan 18 2011 Volker Fröhlich <volker27@gmx.at> - 0.4-1
- Initial packaging
