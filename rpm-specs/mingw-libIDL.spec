%?mingw_package_header

Summary:        MinGW Windows IDL Parsing Library
Name:           mingw-libIDL
Version:        0.8.14
Release:        13%{?dist}
License:        LGPLv2 or MPLv1.1
URL:            ftp://ftp.gnome.org/pub/GNOME/sources/libIDL
Source:         ftp://ftp.gnome.org/pub/GNOME/sources/libIDL/0.8/libIDL-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-pkg-config
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-pkg-config
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils

BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  libtool
BuildRequires:  autoconf automake libtool


%description
MinGW Windows IDL Parsing Library.


# Win32
%package -n mingw32-libIDL
Summary:        MinGW Windows IDL Parsing Library

%description -n mingw32-libIDL
MinGW Windows IDL Parsing Library.

%package -n mingw32-libIDL-static
Summary:        Static version of the MinGW Windows IDL Parsing Library
Requires:       mingw32-libIDL = %{version}-%{release}

%description -n mingw32-libIDL-static
Static version of the MinGW Windows IDL Parsing Library

# Win64
%package -n mingw64-libIDL
Summary:        MinGW Windows IDL Parsing Library

%description -n mingw64-libIDL
MinGW Windows IDL Parsing Library.

%package -n mingw64-libIDL-static
Summary:        Static version of the MinGW Windows IDL Parsing Library
Requires:       mingw64-libIDL = %{version}-%{release}

%description -n mingw64-libIDL-static
Static version of the MinGW Windows IDL Parsing Library


%?mingw_debug_package


%prep
%setup -q -n libIDL-%{version}
autoreconf -i -f

%build
%mingw_configure --enable-shared --enable-static libIDL_cv_long_long_format=I64
sed -e '1,1d' -i libIDL.def
cp libIDL.def build_win32
cp libIDL.def build_win64
%mingw_make


%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{mingw64_datadir}/idl
mkdir -p $RPM_BUILD_ROOT%{mingw32_datadir}/idl

rm -rf $RPM_BUILD_ROOT%{mingw64_infodir}
rm -rf $RPM_BUILD_ROOT%{mingw32_infodir}

find $RPM_BUILD_ROOT -name '*.la' -delete


# Win32
%files -n mingw32-libIDL
%doc COPYING README ChangeLog
%{mingw32_bindir}/libIDL-2-0.dll
%dir %{mingw32_datadir}/idl
%{mingw32_bindir}/libIDL-config-2
%{mingw32_includedir}/libIDL-2.0/
%{mingw32_libdir}/libIDL-2.dll.a
%{mingw32_libdir}/pkgconfig/libIDL-2.0.pc

%files -n mingw32-libIDL-static
%{mingw32_libdir}/libIDL-2.a

# Win64
%files -n mingw64-libIDL
%doc COPYING README ChangeLog
%{mingw64_bindir}/libIDL-2-0.dll
%dir %{mingw64_datadir}/idl
%{mingw64_bindir}/libIDL-config-2
%{mingw64_includedir}/libIDL-2.0/
%{mingw64_libdir}/libIDL-2.dll.a
%{mingw64_libdir}/pkgconfig/libIDL-2.0.pc

%files -n mingw64-libIDL-static
%{mingw64_libdir}/libIDL-2.a


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 0.8.14-12
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Greg Hellings <greg.hellings@gmail.com> - 0.8.14-3
- Update spec file name

* Fri Dec 13 2013 Greg Hellings <greg.hellings@gmail.com> - 0.8.14-2
- Review improvements.

* Wed Aug 22 2012 Greg Hellings <greg.hellings@gmail.com> - 0.8.14-1
- Initial import
