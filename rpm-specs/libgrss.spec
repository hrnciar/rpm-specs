Name:          libgrss
Version:       0.7.0
Release:       10%{?dist}
Summary:       Library for easy management of RSS/Atom/Pie feeds

License:       LGPLv3+
URL:           https://wiki.gnome.org/Projects/Libgrss
Source0:       https://download.gnome.org/sources/%{name}/0.7/%{name}-%{version}.tar.xz

BuildRequires: gcc
BuildRequires: intltool
BuildRequires: gtk-doc
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(libxml-2.0)

%description
libgrss is a Glib abstaction to handle feeds in RSS, Atom and other formats.

%package       devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description   devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup

%build
%configure --disable-static --disable-silent-rules --enable-gtk-doc
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/%{name}.la

%ldconfig_scriptlets

%files
%license COPYING
%{_libdir}/%{name}.so.*
%{_libdir}/girepository-1.0/Grss-0.7.typelib

%files devel
%{_libdir}/%{name}.so
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gir-1.0/Grss-0.7.gir
%{_datadir}/gtk-doc/html/%{name}/

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 19 2015 Igor Gnatenko <ignatenko@src.gnome.org> - 0.7.0-1
- 0.7.0

* Tue Jul 14 2015 Igor Gnatenko <ignatenko@src.gnome.org> - 0.6-2
- Add patch for fix gobject-introspection

* Tue Jul 07 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.6-1
- Initial package
