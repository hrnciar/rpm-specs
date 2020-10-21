Name:      freexl
Version:   1.0.6
Release:   1%{?dist}
Summary:   Library to extract data from within an Excel spreadsheet 
License:   MPLv1.1 or GPLv2+ or LGPLv2+
URL:       http://www.gaia-gis.it/FreeXL
Source0:   http://www.gaia-gis.it/gaia-sins/%{name}-sources/%{name}-%{version}.tar.gz 
BuildRequires:  gcc
BuildRequires: doxygen

%description
FreeXL is a library to extract valid data
from within an Excel spreadsheet (.xls)

Design goals:
    * simple and lightweight
    * stable, robust and efficient
    * easily and universally portable
    * completely ignore any GUI-related oddity

%package devel
Summary:  Development Libraries for FreeXL
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --enable-gcov=no --disable-static
make %{?_smp_mflags}

# Mailed the author on Dec 5th 2011
# Preserve date of header file
sed -i 's/^INSTALL_HEADER = \$(INSTALL_DATA)/& -p/' headers/Makefile.in

# Generate HTML documentation and clean unused installdox script
doxygen
rm -f html/installdox


%check
make check

# Clean up
pushd examples
  make clean
popd


%install
make install DESTDIR=%{buildroot}

# Delete undesired libtool archives
rm -f %{buildroot}%{_libdir}/lib%{name}.la


%ldconfig_scriptlets


%files 
%doc COPYING AUTHORS README
%{_libdir}/lib%{name}.so.*

%files devel
%doc examples html
%{_includedir}/freexl.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/freexl.pc


%changelog
* Sun Aug 02 2020 Volker Fröhlich <volker27@gmx.at> - 1.0.6-1
- New upstream release

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 22 2018 Volker Fröhlich <volker27@gmx.at> - 1.0.5-1
- New upstream release

* Thu Feb 08 2018 Volker Fröhlich <volker27@gmx.at> - 1.0.4-3
- Remove Group keyword

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 08 2017 Volker Fröhlich <volker27@gmx.at> - 1.0.4-1
- New release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Volker Fröhlich <volker27@gmx.at> 1.0.3-1
- New release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Volker Froehlich <volker27@gmx.at> - 1.0.2-2
- Release bump to work around the f23 build being wrongly tagged for f24

* Wed Jul 15 2015 Volker Fröhlich <volker27@gmx.at> 1.0.2-1
- New release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 22 2015 Volker Fröhlich <volker27@gmx.at> 1.0.1-1
- New release

* Fri Mar  6 2015 Volker Fröhlich <volker27@gmx.at> 1.0.0i-1
- New release with security fixes

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0f-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0f-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Nov 30 2013 Volker Fröhlich <volker27@gmx.at> 1.0.0f-1
- Drop obsolete patch for aarch64

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0d-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr  2 2013 Volker Fröhlich <volker27@gmx.at> 1.0.0d-4
- Add patch for aarch64

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0d-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0d-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Volker Fröhlich <volker27@gmx.at> 1.0.0d-1
- New upstream bugfix release

* Fri Jan 13 2012 Volker Fröhlich <volker27@gmx.at> 1.0.0a-3
- Remove coverage tests and BR for lcov (fail in Rawhide)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jan 08 2012 Volker Fröhlich <volker27@gmx.at> 1.0.0a-1
- Correct versioning scheme to post-release
- Correct Source and setup macro accordingly

* Fri Nov 18 2011 Volker Fröhlich <volker27@gmx.at> 1.0.0-0.1.a
- Move development lib symlink to devel
- Don't build static lib
- Add README
- Build with enable-gcov
- BR lcov and doxygen
- Shorten description and summary
- Use macros in Source tag
- Add check section
- Change version and release
- Correct URL
- Correct to multiple licensing scenario
- Drop defattr
- Add pkgconfig and isa macro to devel's BR
- Use upstream tarball, as file size is different
- Remove EPEL 5 specific elements

* Fri Nov 26 2010 Peter Hopfgartber <peter.hopfgartner@r3-gis.com> 1.0.0a-0.1
- Initial packaging
