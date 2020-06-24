Name:           gcolor3
Version:        2.3.1
Release:        6%{?dist}
Summary:        A simple color chooser written in GTK3 (like gcolor2)

License:        GPLv2+
URL:            https://www.hjdskes.nl/projects/gcolor3/

Source0:        https://gitlab.gnome.org/World/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Patch0:         meson-disable-werror.patch
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  gnome-common
BuildRequires:  gtk3-devel >= 3.12.0
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
Requires:       hicolor-icon-theme

%description
Gcolor3 is a color selection dialog written in GTK+ 3. It is much alike Gcolor2,
but uses the newer GTK+ version to better integrate into your modern desktop.
It has the same feature set as Gcolor2, except that recent versions of Gcolor3
use an .ini style file to save colors (older versions use the same file as
Gcolor2).

%prep
%autosetup -n %{name}-v%{version}

%build
%meson
%meson_build

%install
%meson_install

%find_lang gcolor3
desktop-file-validate %{buildroot}%{_datadir}/applications/nl.hjdskes.gcolor3.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/nl.hjdskes.gcolor3.appdata.xml

%files -f gcolor3.lang
%doc README.md
%license LICENSE
%{_bindir}/gcolor3
%{_datadir}/applications/nl.hjdskes.gcolor3.desktop
%{_datadir}/icons/hicolor/scalable/apps/nl.hjdskes.gcolor3.svg
%{_metainfodir}/nl.hjdskes.gcolor3.appdata.xml
%{_mandir}/man1/gcolor3.1*

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 28 2019 Timothée Floure <fnux@fedoraproject.org> - 2.3.1-5
- Disable -Werror compilation flag due to deprecation warnings in F30+

* Thu Sep 19 2019 Kalev Lember <klember@redhat.com> - 2.3.1-4
- Fix typo in hicolor-icon-theme requires

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 30 2019 Timothée Floure <fnux@fedoraproject.org> - 2.3.1-2
  - Add missing dependency on hicoler-icon-theme

* Mon Sep 03 2018 Timothée Floure <fnux@fedoraproject.org> - 2.3.1-1
  - New upstream release (2.3.1)
  - Use meson to build the application
  - Update project homepage
  - Update project URL

* Tue Jun 26 2018 Timothée Floure <fnux@fedoraproject.org> - 2.2-5
  - Fix compilation for F28+ (patch1)

* Sun Sep 03 2017 Timothée Floure <timothee.floure@fnux.ch> - 2.2-4
  - Update license field from GPLv2 to GPLv2+
  - Use the --nonet flag in gcolor3.appdata.xml's validation
  - Add an empty line between each changelog entry

* Wed Aug 09 2017 Timothée Floure <timothee.floure@fnux.ch> - 2.2-3
  - Patch and validate gcolor3.appdata.xml
  - Use the license macro instead of the doc macro for the LICENSE file
  - Remove the deprecated RPM Group
  - use the make_build macro instead of make %{?_smp_mflags}
  - Add minimal version for gtk3-devel (in BuildRequires)
  - Use a more explicit name for the source file

* Sun Apr 23 2017 Timothée Floure <timothee.floure@fnux.ch> - 2.2-2
  - Improve specfile in order to comply with the "Fedora Packaging Guidelines"

