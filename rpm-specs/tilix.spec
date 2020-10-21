%global gtkd_version 3.8.5

Name:           tilix
Version:        1.9.3
Release:        6%{?dist}
Summary:        Tiling terminal emulator

# The tilix source code is MPLv2.0,
# source/gx/gtk/x11.d is GPLv2+,
# source/secret is LGPLv3+,
# source/x11 and com.gexperts.Tilix.gschema.xml are GPLv3+,
# icons are CC-BY-SA.
# This makes the combined license:
License:        MPLv2.0 and GPLv3+ and CC-BY-SA
URL:            https://github.com/gnunn1/tilix
Source0:        https://github.com/gnunn1/tilix/archive/%{version}/%{name}-%{version}.tar.gz
# Fix the build with latest ldc
Patch0:         0001-Avoid-calling-values-on-a-shared-object.patch

ExclusiveArch:  %{ldc_arches}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  glib2-devel
BuildRequires:  ldc
BuildRequires:  pkgconfig(gtkd-3) >= %{gtkd_version}
BuildRequires:  pkgconfig(vted-3) >= %{gtkd_version}
BuildRequires:  pkgconfig(x11)
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  /usr/bin/po4a-translate

# For directory ownership
Requires:       dbus
Requires:       hicolor-icon-theme

Requires:       gtkd%{?_isa} >= %{gtkd_version}

# Upgrade path from terminix copr
Obsoletes:      terminix < 1.5.4
Provides:       terminix = %{version}-%{release}

%description
Tilix is a tiling terminal emulator with the following features:

 - Layout terminals in any fashion by splitting them horizontally or vertically
 - Terminals can be re-arranged using drag and drop both within and between
   windows
 - Terminals can be detached into a new window via drag and drop
 - Input can be synchronized between terminals so commands typed in one
   terminal are replicated to the others
 - The grouping of terminals can be saved and loaded from disk
 - Terminals support custom titles
 - Color schemes are stored in files and custom color schemes can be created by
   simply creating a new file
 - Transparent background
 - Supports notifications when processes are completed out of view

The application was written using GTK 3 and an effort was made to conform to
GNOME Human Interface Guidelines (HIG).


%package        nautilus
Summary:        Tilix extension for Nautilus
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       nautilus-python%{?_isa}

# Upgrade path from terminix copr
Obsoletes:      terminix-nautilus < 1.5.4
Provides:       terminix-nautilus = %{version}-%{release}

%description    nautilus
This package provides a Nautilus extension that adds the 'Open in Tilix'
option to the right-click context menu in Nautilus.


%prep
%autosetup -p1

%if 0%{?flatpak}
sed -i -e "/^Exec=/ s|/usr/bin|%{_bindir}|" data/dbus/com.gexperts.Tilix.service
%endif


%build
NOCONFIGURE=1 ./autogen.sh
%configure DCFLAGS="%{_d_optflags} -version=StdLoggerDisableTrace"
%make_build

%if 0%{?flatpak}
gcc %optflags %__global_ldflags -o tilix-flatpak-toolbox experimental/flatpak/tilix-flatpak-toolbox.c
%endif

# Rename license files so that we can include them in %%license
cp -a data/icons/LICENSE LICENSE-data-icons
cp -a source/x11/LICENSE LICENSE-source-x11


%install
%make_install

%if 0%{?flatpak}
install -m 755 tilix-flatpak-toolbox $RPM_BUILD_ROOT%{_bindir}
%endif

%find_lang tilix


%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/com.gexperts.Tilix.appdata.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/com.gexperts.Tilix.desktop


%files -f tilix.lang
%license LICENSE*
%doc README.md
%{_bindir}/tilix
%if 0%{?flatpak}
%{_bindir}/tilix-flatpak-toolbox
%endif
%{_datadir}/applications/com.gexperts.Tilix.desktop
%{_datadir}/dbus-1/services/com.gexperts.Tilix.service
%{_datadir}/glib-2.0/schemas/com.gexperts.Tilix.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/com.gexperts.Tilix.svg
%{_datadir}/icons/hicolor/scalable/apps/com.gexperts.Tilix-symbolic.svg
%{_datadir}/metainfo/com.gexperts.Tilix.appdata.xml
%{_datadir}/tilix/
%{_mandir}/man1/tilix.1*
%lang(cs) %{_mandir}/cs/man1/tilix.1*
%lang(de) %{_mandir}/de/man1/tilix.1*
%lang(es) %{_mandir}/es/man1/tilix.1*
%lang(fr) %{_mandir}/fr/man1/tilix.1*
%lang(it) %{_mandir}/it/man1/tilix.1*
%lang(nl) %{_mandir}/nl/man1/tilix.1*
%lang(nb_NO) %{_mandir}/nb_NO/man1/tilix.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/tilix.1*
%lang(ru) %{_mandir}/ru/man1/tilix.1*
%lang(sr) %{_mandir}/sr/man1/tilix.1*
%lang(uk) %{_mandir}/uk/man1/tilix.1*
%lang(zh_Hant) %{_mandir}/zh_Hant/man1/tilix.1*

%files nautilus
%{_datadir}/nautilus-python/extensions/open-tilix.py*


%changelog
* Fri Aug 21 2020 Kalev Lember <klember@redhat.com> - 1.9.3-6
- Rebuilt for ldc 1.23

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Kalev Lember <klember@redhat.com> - 1.9.3-4
- Rebuilt for ldc 1.20

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 2019 Kalev Lember <klember@redhat.com> - 1.9.3-1
- Update to 1.9.3

* Tue Apr 09 2019 Kalev Lember <klember@redhat.com> - 1.9.0-2
- Rebuilt for ldc 1.15

* Mon Mar 18 2019 Kalev Lember <klember@redhat.com> - 1.9.0-1
- Update to 1.9.0

* Mon Feb 18 2019 Kalev Lember <klember@redhat.com> - 1.8.9-3
- Rebuilt for ldc 1.14

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 Kalev Lember <klember@redhat.com> - 1.8.9-1
- Update to 1.8.9

* Fri Jan 04 2019 Kalev Lember <klember@redhat.com> - 1.8.7-1
- Update to 1.8.7

* Wed Nov 07 2018 Kalev Lember <klember@redhat.com> - 1.8.5-1
- Update to 1.8.5

* Sun Oct 14 2018 Kalev Lember <klember@redhat.com> - 1.8.3-3
- Rebuilt for ldc 1.12

* Mon Sep 03 2018 Kalev Lember <klember@redhat.com> - 1.8.3-2
- Add missing python2-gobject dependency to tilix-nautilus (#1539039)

* Tue Aug 21 2018 Kalev Lember <klember@redhat.com> - 1.8.3-1
- Update to 1.8.3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Kalev Lember <klember@redhat.com> - 1.8.1-2
- Rebuilt for ldc 1.11

* Sun May 27 2018 Kalev Lember <klember@redhat.com> - 1.8.1-1
- Update to 1.8.1

* Wed May 16 2018 James Ye <jye836@gmail.com> - 1.7.9-1
- Update to 1.7.9

* Mon Mar 19 2018 Kalev Lember <klember@redhat.com> - 1.7.7-1
- Update to 1.7.7
- Remove no longer needed icon cache scriptlets

* Mon Feb 19 2018 Kalev Lember <klember@redhat.com> - 1.7.5-3
- Rebuilt for ldc 1.8

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Kalev Lember <klember@redhat.com> - 1.7.5-1
- Update to 1.7.5

* Sun Dec 17 2017 Kalev Lember <klember@redhat.com> - 1.7.3-1
- Update to 1.7.3
- Set minimum required gtkd version

* Sat Nov 11 2017 Vadim Rutkovsky <vrutkovs@redhat.com> - 1.7.1-1
- Update to 1.7.1

* Thu Oct 12 2017 Kalev Lember <klember@redhat.com> - 1.6.4-5
- Rebuilt for gtkd 3.6.6

* Wed Sep 13 2017 Kalev Lember <klember@redhat.com> - 1.6.4-4
- Rebuilt for ldc 1.4

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Kalev Lember <klember@redhat.com> - 1.6.4-1
- Update to 1.6.4

* Tue Jun 13 2017 Kalev Lember <klember@redhat.com> - 1.6.1-1
- Update to 1.6.1

* Mon Apr 10 2017 Kalev Lember <klember@redhat.com> - 1.5.6-1
- Update to 1.5.6
- Obsolete terminix-nautilus for upgrade path from terminix copr

* Mon Mar 20 2017 Kalev Lember <klember@redhat.com> - 1.5.4-4
- Include data/icons/LICENSE and source/x11/LICENSE as %%license (#1434003)

* Mon Mar 20 2017 Kalev Lember <klember@redhat.com> - 1.5.4-3
- Update licensing breakdown (#1434003)
- Add explicit dbus and hicolor-icon-theme deps for directory ownership

* Mon Mar 20 2017 Kalev Lember <klember@redhat.com> - 1.5.4-2
- Use _d_optflags and disable debug print to stderr

* Mon Mar 20 2017 Kalev Lember <klember@redhat.com> - 1.5.4-1
- Initial Fedora packaging
