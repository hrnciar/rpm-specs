%global appname io.elementary.switchboard

Name:           switchboard
Summary:        Modular Desktop Settings Hub
Version:        2.4.0
Release:        2%{?dist}
License:        LGPLv2+

URL:            https://github.com/elementary/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite) >= 5.4.0
BuildRequires:  pkgconfig(gtk+-3.0)

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

Requires:       hicolor-icon-theme

%description
Extensible System Settings application.


%package        libs
Summary:        Modular Desktop Settings Hub (shared library)
%description    libs
Extensible System Settings application.

This package contains the shared library.


%package        devel
Summary:        Modular Desktop Settings Hub (development files)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel
Extensible System Settings application.

This package contains the files required for developing plugs for
switchboard.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}

# create plug directories
mkdir -p %{buildroot}/%{_libdir}/%{name}

mkdir -p %{buildroot}/%{_libdir}/%{name}/hardware
mkdir -p %{buildroot}/%{_libdir}/%{name}/network
mkdir -p %{buildroot}/%{_libdir}/%{name}/personal
mkdir -p %{buildroot}/%{_libdir}/%{name}/system


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{appname}.lang
%doc README.md
%license COPYING

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml


%files libs
%doc README.md
%license COPYING

%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/*

%{_libdir}/lib%{name}-2.0.so.0
%{_libdir}/lib%{name}-2.0.so.2.0


%files devel
%doc README.md
%license COPYING

%{_includedir}/%{name}-2.0/

%{_libdir}/lib%{name}-2.0.so
%{_libdir}/pkgconfig/%{name}-2.0.pc

%{_datadir}/vala/vapi/%{name}-2.0.deps
%{_datadir}/vala/vapi/%{name}-2.0.vapi


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 07 2020 Fabio Valentini <decathorpe@gmail.com> - 2.4.0-1
- Update to version 2.4.0.

* Wed Apr 01 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.9-1
- Update to version 2.3.9.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.8-1
- Update to version 2.3.8.

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.7-1
- Update to version 2.3.7.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.6-1
- Update to version 2.3.6.

* Fri Nov 30 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.5-1
- Update to version 2.3.5.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4-1
- Update to version 2.3.4.

* Fri Oct 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.3-1
- Update to version 2.3.3.

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 2.3.2-2
- Rebuild with fixed binutils

* Sun Jul 29 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.2-1
- Update to version 2.3.2.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.1-2
- Rebuild for granite5 soname bump.

* Wed Jun 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.1-1
- Update to version 2.3.1.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.0-4
- Clean up .spec file.

* Sat Nov 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3.0-3
- Rebuild for granite soname bump.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Fri Jul 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.3.0-1
- Update to version 2.3.0.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.1-2
- Rename bundled icon.

* Wed Feb 01 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.1-1
- Update to version 2.2.1.
- Remove patch, the new version fixes this.

* Wed Jan 25 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0-6
- Include icon to fix appstream metadata generation.

* Wed Jan 11 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0-5
- Add patch to fix pkgconfig file.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0-4
- Split off -libs subpackage.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.2.0-3
- Clean up spec file.

* Sat Dec 24 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.0-2
- Enable libunity support.

* Thu Dec 08 2016 Fabio Valentini <decathorpe@gmail.com> - 2.2.0-1
- Update to version 2.2.0.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-4
- Mass rebuild.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-3
- Spec file cleanups.

* Mon Sep 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-2
- Spec file cosmetics.

* Wed Aug 10 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0-1
- Update to version 2.1.0.

