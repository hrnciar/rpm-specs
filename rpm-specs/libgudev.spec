Name:           libgudev
Version:        232
Release:        7%{?dist}
Summary:        GObject-based wrapper library for libudev

License:        LGPLv2+
URL:            https://wiki.gnome.org/Projects/libgudev
Source0:        https://download.gnome.org/sources/libgudev/%{version}/libgudev-%{version}.tar.xz

Patch1:         https://git.gnome.org/browse/libgudev/patch/?id=bf8664a028d8cbc55f9dbc65fef926e2119b9579#/fix-test-assertion-with-umockdev.patch

BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  pkgconfig
BuildRequires:  libudev-devel
BuildRequires:  gtk-doc
BuildRequires:  umockdev-devel

# Upstream promises to remove libgudev from systemd before this version
Provides:       libgudev1 = %{version}-%{release}
Obsoletes:      libgudev1 < 230

%description
This library makes it much simpler to use libudev from programs
already using GObject. It also makes it possible to easily use libudev
from other programming languages, such as Javascript, because of
GObject introspection support.

%package devel
Summary:   Header files for %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}

Provides:       libgudev1-devel = %{version}-%{release}
Obsoletes:      libgudev1-devel < 230

%description devel
This package is necessary to build programs using %{name}.

%prep
%autosetup -p1

%build
%configure --enable-gtk-doc
%make_build V=1

%install
%make_install
rm %{buildroot}%{_libdir}/*.la

%check
make check

%ldconfig_scriptlets

%files
%license COPYING
%doc NEWS
%{_libdir}/libgudev-1.0.so.*
%{_libdir}/girepository-1.0/GUdev-1.0.typelib

%files devel
%{_libdir}/libgudev-1.0.so
%dir %{_includedir}/gudev-1.0
%dir %{_includedir}/gudev-1.0/gudev
%{_includedir}/gudev-1.0/gudev/*.h
%{_datadir}/gir-1.0/GUdev-1.0.gir
%dir %{_datadir}/gtk-doc/html/gudev
%{_datadir}/gtk-doc/html/gudev/*
%{_libdir}/pkgconfig/gudev-1.0*


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 232-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 232-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 232-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 232-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 24 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 232-3
- Pull in patch from upstream to fix build

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 232-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 232-2
- Switch to %%ldconfig_scriptlets

* Fri Sep 01 2017 Kalev Lember <klember@redhat.com> - 232-1
- Update to 232
- Enable self tests

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 230-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 230-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 230-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 230-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 230-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 31 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 230-1
- Initial packaging
