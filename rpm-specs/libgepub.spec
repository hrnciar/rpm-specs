%global apiver 0.6

Name:           libgepub
Version:        0.6.0
Release:        5%{?dist}
Summary:        Library for epub documents

License:        LGPLv2+
URL:            https://git.gnome.org/browse/libgepub
Source0:        https://download.gnome.org/sources/libgepub/0.6/libgepub-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

%description
libgepub is a GObject based library for handling and rendering epub
documents.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install


%files
%license COPYING
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Gepub-%{apiver}.typelib
%{_libdir}/libgepub-%{apiver}.so.0*

%files devel
%{_includedir}/libgepub-%{apiver}/
%{_libdir}/libgepub-%{apiver}.so
%{_libdir}/pkgconfig/libgepub-%{apiver}.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Gepub-%{apiver}.gir


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Kalev Lember <klember@redhat.com> - 0.6.0-1
- Update to 0.6.0
- Remove ldconfig scriptlets

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 0.5.3-1
- Update to 0.5.3
- Switch to the meson build system

* Thu Feb 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.2-2
- Switch to %%ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 09 2017 Kalev Lember <klember@redhat.com> - 0.5.2-1
- Update to 0.5.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Kalev Lember <klember@redhat.com> - 0.5-1
- Update to 0.5

* Thu Mar 30 2017 Bastien Nocera <bnocera@redhat.com> - 0.4-3
+ libgepub-0.4-3
- Add guards to public API

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 01 2016 Kalev Lember <klember@redhat.com> - 0.4-1
- Update to 0.4

* Mon Aug 22 2016 Kalev Lember <klember@redhat.com> - 0.3-0.1.git395779e
- Initial Fedora build
