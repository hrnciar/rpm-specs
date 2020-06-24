%global gtk3_version          %(pkg-config --modversion gtk+-3.0 2>/dev/null || echo bad)
%global gtk4_version          %(pkg-config --modversion gtk4 2>/dev/null || echo bad)
%global glib2_version         %(pkg-config --modversion glib-2.0 2>/dev/null || echo bad)
%global nm_version            1:1.8.0
%global mbp_version           0.20090602
%global old_libnma_version    1.8.27

%global rpm_version 1.8.28
%global real_version 1.8.28
%global release_version 1

%global real_version_major %(printf '%s' '%{real_version}' | sed -n 's/^\\([1-9][0-9]*\\.[1-9][0-9]*\\)\\.[1-9][0-9]*$/\\1/p')

%bcond_with libnma_gtk4

Name:           libnma
Summary:        NetworkManager GUI library
Version:        %{rpm_version}
Release:        %{release_version}%{?dist}
# The entire source code is GPLv2+ except some files in shared/ which are LGPLv2+
License:        GPLv2+ and LGPLv2+
URL:            https://gitlab.gnome.org/GNOME/libnma/
Source0:        https://download.gnome.org/sources/libnma/%{real_version_major}/%{name}-%{real_version}.tar.xz

Patch1:         0001-nm-applet-no-notifications.patch

Requires:       mobile-broadband-provider-info >= %{mbp_version}

Conflicts:      libnma < %{old_libnma_version}

BuildRequires:  gcc
BuildRequires:  NetworkManager-libnm-devel >= %{nm_version}
BuildRequires:  ModemManager-glib-devel >= 1.0
BuildRequires:  glib2-devel >= 2.32
BuildRequires:  gtk3-devel >= 3.10
%if %{with libnma_gtk4}
BuildRequires:  gtk4-devel >= 3.96
%endif
BuildRequires:  gobject-introspection-devel >= 0.10.3
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig
BuildRequires:  meson
BuildRequires:  gtk-doc
BuildRequires:  iso-codes-devel
BuildRequires:  gcr-devel
BuildRequires:  mobile-broadband-provider-info-devel >= %{mbp_version}

%description
This package contains the library used for integrating GUI tools with
NetworkManager.


%package devel
Summary:        Header files for NetworkManager GUI library
Requires:       NetworkManager-libnm-devel >= %{nm_version}
Obsoletes:      NetworkManager-gtk-devel < 1:0.9.7
Requires:       libnma%{?_isa} = %{version}-%{release}
Requires:       gtk3-devel%{?_isa}
Requires:       pkgconfig
Conflicts:      libnma < %{old_libnma_version}

%description devel
This package contains header and pkg-config files to be used for integrating
GUI tools with NetworkManager.


%package gtk4
Summary:        Experimental GTK 4 version of NetworkManager GUI library
Requires:       gtk4%{?_isa} >= %{gtk4_version}
Requires:       mobile-broadband-provider-info >= %{mbp_version}
Conflicts:      libnma < %{old_libnma_version}

%description gtk4
This package contains the experimental GTK4 version of library used for
integrating GUI tools with NetworkManager.


%package gtk4-devel
Summary:        Header files for experimental GTK4 version of NetworkManager GUI library
Requires:       NetworkManager-libnm-devel >= %{nm_version}
Requires:       libnma-gtk4%{?_isa} = %{version}-%{release}
Requires:       gtk4-devel%{?_isa}
Requires:       pkgconfig
Conflicts:      libnma < %{old_libnma_version}

%description gtk4-devel
This package contains the experimental GTK4 version of header and pkg-config
files to be used for integrating GUI tools with NetworkManager.


%prep
%autosetup -p1 -n "%{name}-%{real_version}"


%build
%meson \
        -Dgcr=true \
        -Ddisable-static=true \
        -Dvapi=false \
%if %{with libnma_gtk4}
        -Dlibnma_gtk4=true
%else
        -Dlibnma_gtk4=false
%endif
%meson_build


%install
%meson_install
%find_lang %{name}


%check
%meson_test


%files -f %{name}.lang
%{_libdir}/libnma.so.*
%{_libdir}/girepository-1.0/NMA-1.0.typelib
%{_datadir}/glib-2.0/schemas/org.gnome.nm-applet.gschema.xml
%doc NEWS CONTRIBUTING
%license COPYING


%files devel
%{_includedir}/libnma
%{_libdir}/pkgconfig/libnma.pc
%{_libdir}/libnma.so
%{_datadir}/gir-1.0/NMA-1.0.gir
%{_datadir}/gtk-doc


%if %{with libnma_gtk4}
%files gtk4
%{_libdir}/libnma-gtk4.so.*
%{_libdir}/girepository-1.0/NMA4-1.0.typelib
%license COPYING


%files gtk4-devel
%{_includedir}/libnma
%{_libdir}/pkgconfig/libnma-gtk4.pc
%{_libdir}/libnma-gtk4.so
%{_datadir}/gir-1.0/NMA4-1.0.gir
%endif


%changelog
* Fri Mar  6 2020 Thomas Haller <thaller@redhat.com> - 1.8.28-1
- Update to 1.8.28 release
- move org.gnome.nm-applet.gschema.xml from network-manager-applet to here.
- introduce wireless security dialogs

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.8.26-3
- Clarify licensing
- Add a missing mobile-broadband-provider-info provide

* Fri Nov 08 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.8.26-2
- Fixes suggested in review by Matthew Krupcale (#1763285):
- Add gcc BR
- Fixed the libnma-gtk4 conditional
- Made dependencies arch-specific where relevant
- Dropped obsolete macros
- Install license file with libnma-gtk4

* Fri Oct 18 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.8.26-1
- Initial package split from nm-connection-editor
