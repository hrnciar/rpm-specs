%{?mingw_package_header}

%global pkgname libgeotiff

Name:      mingw-%{pkgname}
Version:   1.6.0
Release:   2%{?dist}
Summary:   MinGW Windows %{pkgname} library

License:   MIT
URL:       http://trac.osgeo.org/geotiff/
BuildArch: noarch
Source0:   http://download.osgeo.org/geotiff/%{pkgname}/%{pkgname}-%{version}.tar.gz
# - Add -no-undefined to linker flags
# - Fix include directory
# Patch0:    libgeotiff_buildsys.patch

BuildRequires: autoconf automake libtool

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw32-libtiff
BuildRequires: mingw32-libjpeg
BuildRequires: mingw32-proj
BuildRequires: mingw32-zlib

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-binutils
BuildRequires: mingw64-libtiff
BuildRequires: mingw64-libjpeg
BuildRequires: mingw64-proj
BuildRequires: mingw64-zlib


%description
%{summary}.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
%{summary}.


%package -n mingw32-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-static
%{summary}.


%package -n mingw32-%{pkgname}-tools
Summary:       Tools for the MinGW Windows %{pkgname} library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-tools
%{summary}.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
%{summary}.


%package -n mingw64-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-static
%{summary}.


%package -n mingw64-%{pkgname}-tools
Summary:       Tools for the MinGW Windows %{pkgname} library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-tools
%{summary}.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
./autogen.sh
%{mingw_configure} --with-proj --with-jpeg --with-zip
%{mingw_make} %{?_smp_mflags}


%install
%{mingw_make} install DESTDIR=%{buildroot}

# install pkgconfig files
mkdir -p %{buildroot}%{mingw32_libdir}/pkgconfig/
cat > %{buildroot}%{mingw32_libdir}/pkgconfig/%{pkgname}.pc <<EOF
prefix=%{mingw32_prefix}
exec_prefix=%{mingw32_prefix}
libdir=%{mingw32_libdir}
includedir=%{mingw32_includedir}/%{pkgname}

Name: %{pkgname}
Description: GeoTIFF file format library
Version: %{version}
Libs: -L${libdir} -lgeotiff
Cflags: -I${includedir}
EOF

mkdir -p %{buildroot}%{mingw64_libdir}/pkgconfig/
cat > %{buildroot}%{mingw64_libdir}/pkgconfig/%{pkgname}.pc <<EOF
prefix=%{mingw64_prefix}
exec_prefix=%{mingw64_prefix}
libdir=%{mingw64_libdir}
includedir=%{mingw64_includedir}/%{pkgname}

Name: %{pkgname}
Description: GeoTIFF file format library
Version: %{version}
Libs: -L${libdir} -lgeotiff
Cflags: -I${includedir}
EOF

# Remove static libraries
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files -n mingw32-%{pkgname}
%doc ChangeLog README
%license COPYING
%{mingw32_bindir}/libgeotiff-5.dll
%{mingw32_includedir}/*
%{mingw32_datadir}/*
%{mingw32_libdir}/libgeotiff.dll.a
%{mingw32_libdir}/pkgconfig/libgeotiff.pc

%files -n mingw32-%{pkgname}-static
%{mingw32_libdir}/libgeotiff.a

%files -n mingw32-%{pkgname}-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-%{pkgname}
%doc ChangeLog README
%license COPYING
%{mingw64_bindir}/libgeotiff-5.dll
%{mingw64_includedir}/*
%{mingw64_datadir}/*
%{mingw64_libdir}/libgeotiff.dll.a
%{mingw64_libdir}/pkgconfig/libgeotiff.pc

%files -n mingw64-%{pkgname}-static
%{mingw64_libdir}/libgeotiff.a

%files -n mingw64-%{pkgname}-tools
%{mingw64_bindir}/*.exe


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 12 2020 Sandro Mani <manisandro@gmail.com> - 1.6.0-1
- Update to 1.6.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 16 2019 Sandro Mani <manisandro@gmail.com> - 1.5.1-1
- Update to 1.5.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Sandro Mani <manisandro@gmail.com> - 1.4.3-3
- Rebuild (proj)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Sandro Mani <manisandro@gmail.com> - 1.4.3-1
- Update to 1.4.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Sandro Mani <manisandro@gmail.com> - 1.4.2-2
- Rebuild (proj)

* Sat Oct 15 2016 Sandro Mani <manisandro@gmail.com> - 1.4.2-1
- Update to 1.4.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 11 2015 Sandro Mani <manisandro@gmail.com> - 1.4.0-4
- Rebuild (proj)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 10 2013 Sandro Mani <manisandro@gmail.com> - 1.4.0-2
- Fix descriptions

* Thu Aug 08 2013 Sandro Mani <manisandro@gmail.com> - 1.4.0-1
- Update to 1.4.0
- Enable mingw64 packages
- Spec cleanup

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-0.9.svn1664
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-0.8.svn1664
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 25 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.3.0-0.7.svn1664
- Rebuild against latest libtiff

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-0.6.svn1664
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 07 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.3.0-0.5.svn1664
- Renamed the source package to mingw-libgeotiff (RHBZ #800905)
- Use mingw macros without leading underscore
- Dropped unneeded RPM tags
- Dropped empty devel subpackage

* Tue Feb 28 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.3.0-0.4.svn1664
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-0.3.svn1664
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-0.2.svn1664
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 15 2009 David Ludlow <dave@adsllc.com> - 1.3.0-1.svn1664
- Fedora packaging updates

* Wed Sep 9 2009 David Ludlow <dave@adsllc.com> - 1.2.5-4
- Initial creation of mingw32 package
