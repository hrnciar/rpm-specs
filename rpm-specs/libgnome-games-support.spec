Name:           libgnome-games-support
Version:        1.6.1
Release:        1%{?dist}
Summary:        Support library for GNOME games

License:        LGPLv3+
URL:            https://gitlab.gnome.org/GNOME/libgnome-games-support/
Source0:        https://download.gnome.org/sources/libgnome-games-support/1.6/libgnome-games-support-%{version}.tar.xz


BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gio-2.0) >= 2.40
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.19
BuildRequires:  pkgconfig(gee-0.8)

# Retired in F25
Obsoletes:      libgames-support < 1.1.90


%description
libgnome-games-support is a small library intended for internal use
by GNOME Games, but it may be used by others. 
The API will only break with the major version number.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Retired in F25
Obsoletes:      libgames-support-devel < 1.1.90

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%doc README
%license COPYING.LESSER
%{_libdir}/libgnome-games-support-1.so.3*

%files devel
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/*.vapi
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Fri Mar 27 2020 Kalev Lember <klember@redhat.com> - 1.6.1-1
- Update to 1.6.1

* Thu Mar 05 2020 Kalev Lember <klember@redhat.com> - 1.6.0.1-1
- Update to 1.6.0.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan  4 2020 Yanko Kaneti <yaneti@declera.com> - 1.5.90-1
- Update to 1.5.90. Switch to meson

* Tue Sep 03 2019 Kalev Lember <klember@redhat.com> - 1.4.4-1
- Update to 1.4.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Yanko Kaneti <yaneti@declera.com> - 1.4.3-1
- Update to 1.4.3

* Wed Aug 22 2018 Yanko Kaneti <yaneti@declera.com> - 1.4.2-1
- Update to 1.4.2
- Change url to gitlab.gnome.org

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 22 2018 Kalev Lember <klember@redhat.com> - 1.4.1-1
- Update to 1.4.1

* Sat Mar 10 2018 Yanko Kaneti <yaneti@declera.com> - 1.4.0-1
- Update to 1.4.0

* Mon Feb 19 2018 Yanko Kaneti <yaneti@declera.com> - 1.3.90-1
- Update to 1.3.90
- Soname change
- New ldconfig scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep  9 2017 Yanko Kaneti <yaneti@declera.com> - 1.2.3-1
- Update to 1.2.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 16 2017 Yanko Kaneti <yaneti@declera.com> - 1.2.2-1
- Update to 1.2.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 25 2016 Yanko Kaneti <yaneti@declera.com> - 1.2.1-1
- Update to 1.2.1

* Mon Sep 19 2016 Yanko Kaneti <yaneti@declera.com> - 1.2.0-1
- Update to 1.2.0

* Mon Aug 29 2016 Kalev Lember <klember@redhat.com> - 1.1.91-1
- Update to 1.1.91

* Thu Aug 18 2016 Yanko Kaneti <yaneti@declera.com> - 1.1.90-3
- Move  libgames-support-devel obsoletes to -devel

* Thu Aug 18 2016 Yanko Kaneti <yaneti@declera.com> - 1.1.90-2
- Add libgames-support obsoltes

* Thu Aug 18 2016 Yanko Kaneti <yaneti@declera.com> - 1.1.90-1
- Renamed libgames-support for review.
