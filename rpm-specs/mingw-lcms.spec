%{?mingw_package_header}

%global mingw_pkg_name lcms

Name:           mingw-%{mingw_pkg_name}
Version:        1.19
Release:        15%{?dist}
Summary:        MinGW Color Management System
License:        MIT
URL:            http://www.littlecms.com/
Source0:        http://downloads.sourceforge.net/%{mingw_pkg_name}/%{mingw_pkg_name}-%{version}.tar.gz
Patch0:         lcms-1.19-rhbz675186.patch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw32-libjpeg
BuildRequires:  mingw64-libjpeg
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw64-libtiff
BuildRequires:  pkgconfig
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-zlib
BuildArch:      noarch


%description
LittleCMS intends to be a small-footprint, speed optimized color management
engine in open source form.

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:                %{summary}

%description -n mingw32-%{mingw_pkg_name}
LittleCMS intends to be a small-footprint, speed optimized color management
engine in open source form.

%package -n mingw32-%{mingw_pkg_name}-static
Summary:  Static libraries for mingw32-%{mingw_pkg_name} development
Requires: mingw32-%{mingw_pkg_name} = %{version}-%{release}

%description -n mingw32-%{mingw_pkg_name}-static
The mingw32-%{mingw_pkg_name}-static package contains static library for
mingw32-%{mingw_pkg_name} development.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:                %{summary}

%description -n mingw64-%{mingw_pkg_name}
LittleCMS intends to be a small-footprint, speed optimized color management
engine in open source form.

%package -n mingw64-%{mingw_pkg_name}-static
Summary:  Static libraries for mingw64-%{mingw_pkg_name} development
Requires: mingw64-%{mingw_pkg_name} = %{version}-%{release}

%description -n mingw64-%{mingw_pkg_name}-static
The mingw64-%{mingw_pkg_name}-static package contains static library for
mingw64-%{mingw_pkg_name} development.

%{?mingw_debug_package}

%prep
%setup -q -n %{mingw_pkg_name}-%{version}
pushd samples
%patch0 -p0
popd
rm -f include/icc34.h

find . -name \*.[ch] | xargs chmod -x
chmod 0644 AUTHORS COPYING ChangeLog NEWS README.1ST doc/TUTORIAL.TXT doc/LCMSAPI.TXT

# Convert not UTF-8 files
pushd doc
mkdir -p __temp
for f in LCMSAPI.TXT TUTORIAL.TXT ;do
cp -p $f __temp/$f
iconv -f ISO-8859-1 -t UTF-8 __temp/$f > $f
touch -r __temp/$f $f
done
rm -rf __temp
popd


%build
%mingw_configure --without-python --enable-shared

# remove rpath from libtool
#sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
#sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=${RPM_BUILD_ROOT} INSTALL="install -p"
find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'
find ${RPM_BUILD_ROOT} -type f -name "*.exe" -exec rm -f {} ';'
rm -rf ${RPM_BUILD_ROOT}/%{mingw32_mandir}
rm -rf ${RPM_BUILD_ROOT}/%{mingw64_mandir}

%files -n mingw32-%{mingw_pkg_name}
%doc README.1ST doc/TUTORIAL.TXT AUTHORS COPYING NEWS doc/LCMSAPI.TXT
%{mingw32_includedir}/*
%{mingw32_libdir}/liblcms.dll.a
%{mingw32_bindir}/liblcms-1.dll
%{mingw32_libdir}/pkgconfig/%{mingw_pkg_name}.pc

%files -n mingw32-%{mingw_pkg_name}-static
%{mingw32_libdir}/liblcms.a

%files -n mingw64-%{mingw_pkg_name}
%doc README.1ST doc/TUTORIAL.TXT AUTHORS COPYING NEWS doc/LCMSAPI.TXT
%{mingw64_includedir}/*
%{mingw64_libdir}/liblcms.dll.a
%{mingw64_bindir}/liblcms-1.dll
%{mingw64_libdir}/pkgconfig/%{mingw_pkg_name}.pc

%files -n mingw64-%{mingw_pkg_name}-static
%{mingw64_libdir}/liblcms.a

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan  5 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.19-3
- BR mingw{32,64}-filesystem >= 95

* Tue Nov 20 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.19-2
- fix according to Greg Hellings' reviewer comments

* Thu Aug 23 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 1.19-1
- created from native spec file
