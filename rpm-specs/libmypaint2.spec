%global prerel beta.1
Name: libmypaint2
Version: 2.0.0
Release: 0.8.%{prerel}%{?dist}
Summary: MyPaint brush engine library

# Compute some version related macros.
# Ugly, need to get quoting percent signs straight.
%global major %(ver=%{version}; echo ${ver%%%%.*})
%global minor %(ver=%{version}; ver=${ver#%major.}; echo ${ver%%%%.*})
%global micro %(ver=%{version}; ver=${ver#%major.%minor.}; echo ${ver%%%%.*})

License: ISC and BSD
URL: https://github.com/mypaint/libmypaint
Source0: https://github.com/mypaint/libmypaint/archive/v%{version}-%{prerel}/libmypaint-%{version}-%{prerel}.tar.gz

Patch0: %{name}-0001-use-python3-to-generate-headers.patch
# https://github.com/mypaint/libmypaint/pull/135
Patch1: %{name}-0002-build-with-and-require-gegl-0.4.patch
Patch2: %{name}-0003-set-api-version-for-libmypaint-gegl.patch
# https://github.com/mypaint/libmypaint/pull/136
Patch3: %{name}-0004-fix-imgpath-instead-of-pngmath-in-sphinx-doc.patch

BuildRequires: babl-devel
BuildRequires: gcc
BuildRequires: doxygen
BuildRequires: gegl04-devel
BuildRequires: glib2-devel
BuildRequires: gobject-introspection-devel
BuildRequires: autoconf
BuildRequires: intltool
BuildRequires: json-c-devel
BuildRequires: python3-sphinx
BuildRequires: python3-breathe

%description
This is the brush library used by MyPaint.

%package devel
Summary: Development files for libmypaint
Requires: %{name}%{?isa} = %{version}-%{release}

%description devel
This package contains files needed for development with %{name}.

%prep
%autosetup -p1 -n libmypaint-%{version}-%{prerel}
chmod a-x README.md

%build
./autogen.sh
%configure --enable-docs --enable-introspection=yes --enable-gegl
%make_build

%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -delete -print

%check
make check

%find_lang libmypaint-%{major}.%{minor}

%ldconfig_scriptlets

%files -f libmypaint-%{major}.%{minor}.lang
%license COPYING
%doc README.md
%{_libdir}/libmypaint-*%{major}.%{minor}.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/MyPaint-%{major}.%{minor}.typelib
%{_libdir}/girepository-1.0/MyPaintGegl-%{major}.%{minor}.typelib

%files devel
%doc doc/build/*
%{_libdir}/libmypaint-*%{major}.%{minor}.so
%{_includedir}/libmypaint-%{major}.%{minor}
%{_includedir}/libmypaint-gegl-%{major}.%{minor}
%{_libdir}/pkgconfig/libmypaint-%{major}.%{minor}.pc
%{_libdir}/pkgconfig/libmypaint-gegl-%{major}.%{minor}.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/MyPaint-%{major}.%{minor}.gir
%{_datadir}/gir-1.0/MyPaintGegl-%{major}.%{minor}.gir

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.8.beta.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 2.0.0-0.7.beta.1
- Rebuild (json-c)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.6.beta.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 31 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.0.0-0.5.beta.1
- Update to 2.0.0-beta.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-0.4.alpha.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.0.0-0.3.alpha.2
- Update to 2.0.0-alpha.2

* Tue Feb 19 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.0.0-0.2.alpha.1
- Fix build with new sphinx (where ext.pngmath has been removed)

* Tue Feb 12 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.0.0-0.1.alpha.1
- Update to 2.0.0-alpha.1

* Wed Jan 30 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 2.0.0-0.1.alpha.0
- Initial release of 2.0.0 alpha
