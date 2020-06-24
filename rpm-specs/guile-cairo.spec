Name:           guile-cairo
Version:        1.4.0
Release:        26%{?dist}
Summary:        The Cairo graphics library for Guile Scheme

License:        LGPLv2+

URL:            http://home.gna.org/guile-cairo
Source0:        http://download.gna.org/guile-cairo/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  guile-devel, libpng-devel
BuildRequires:  cairo-devel


%description
Guile-Cairo wraps the Cairo graphics library for Guile Scheme


%package        devel
Summary:        Libraries and header files for %{name}

Requires:       %{name} = %{version}-%{release}
Requires:       cairo-devel, guile-devel
Requires:       pkgconfig

%description    devel
Package %{name}-devel contains libraries and header files for
developing applications that use %{name}.



%prep
%setup -q

# Update CAIRO_FONT_TYPE fonction
sed -i 's|CAIRO_FONT_TYPE_ATSUI|CAIRO_FONT_TYPE_QUARTZ|g' %{name}/%{name}-enum-types.c


%build
%configure --disable-static

#Remove Rpath
sed -i 's|^hardcode_libdir_flag_spec="\\${wl}--rpath \\${wl}\\$libdir"|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make INSTALL="install -p" DESTDIR=$RPM_BUILD_ROOT install


#Remove .la files
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

#Remove unneeded file
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%files
%doc AUTHORS COPYING README ChangeLog HACKING TODO NEWS
%{_libdir}/lib%{name}.so.*
%{_datadir}/guile/site/cairo.scm
%{_datadir}/guile/site/cairo
%{_infodir}/%{name}.info.*

%files  devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/guile-cairo.pc




%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 1.4.0-24
- Remove hardcoded gzip suffix from GNU info pages

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Apr 07 2008 Xavier Lamien <lxtnow[at]gmail.com> - 1.4.0-6
- Updated guile-cairo-enum-type fonction #440805

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.4.0-5
- Autorebuild for GCC 4.3

* Sat Aug 04 2007 Xavier Lamien <lxtnow[at]gmail.com> - 1.4.0-4
- Fixed typo on pkgconfig.

* Wed Aug 01 2007 Xavier Lamien <lxtnow[at]gmail.com> - 1.4.0-3
- Added missing Requires.

* Wed Aug 01 2007 Xavier Lamien <lxtnow[at]gmail.com> - 1.4.0-2
- Minor Fixes.

* Tue Jul 24 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.4.0-1
- Initial Package
