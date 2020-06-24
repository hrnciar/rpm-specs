# -*-Mode: rpm-spec -*-

%global commit c7c3643760caea4bd26b1d56ed033a52f6e34124
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:     bookworm
Version:  1.1.3
Release:  0.1.20200414git.%{shortcommit}%{?dist}
Summary:  Simple, focused eBook reader
License:  GPLv3
URL:      https://github.com/babluboy/bookworm
Source0:  %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch0:   bookworm-patch0-python3.patch

BuildRequires: gcc
BuildRequires: granite-devel
BuildRequires: gtk3-devel
BuildRequires: libgee-devel
BuildRequires: meson
BuildRequires: poppler-glib-devel
BuildRequires: vala
BuildRequires: webkit2gtk3-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

Requires:      hicolor-icon-theme

%description

Read the books you love without having to worry about the different
format complexities like epub, pdf, mobi, cbr, etc. This version
supports EPUB, MOBI, FB2, PDF, FB2 and Comics (CBR and CBZ) formats
with support for more formats to follow soon.

Check the Bookworm website for details on features, shortcuts,
installation guides for supported distros :
https://babluboy.github.io/bookworm/

%prep
%setup -q -n %{name}-%{commit}
%patch0 -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang com.github.babluboy.bookworm
desktop-file-validate %{buildroot}/%{_datadir}/applications/com.github.babluboy.bookworm.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/com.github.babluboy.bookworm.appdata.xml

%files -f com.github.babluboy.bookworm.lang
%{_bindir}/com.github.babluboy.bookworm
%{_datadir}/com.github.babluboy.bookworm/
%{_datadir}/applications/com.github.babluboy.bookworm.desktop
%{_datadir}/glib-2.0/schemas/com.github.babluboy.bookworm.gschema.xml
%{_datadir}/icons/hicolor/*/apps/com.github.babluboy.bookworm.svg
%{_metainfodir}/com.github.babluboy.bookworm.appdata.xml

%doc README.md

%license COPYING

%changelog
* Tue Apr 14 2020 Bob Hepple <bob.hepple@gmail.com> - 1.1.3-0.1.20200414git.c7c3643
- pre-release of 0.1.3

* Wed Apr 08 2020 Bob Hepple <bob.hepple@gmail.com> - 1.1.2-4
- resolve RHBZ#1822231

* Tue Mar 31 2020 Bob Hepple <bob.hepple@gmail.com> - 1.1.2-3
- changes per RHBZ#1812411

* Wed Mar 11 2020 Bob Hepple <bob.hepple@gmail.com> - 1.1.2-2
- fix Source0

* Sat Feb 22 2020 Bob Hepple <bob.hepple@gmail.com> - 1.1.2-1
- Initial version of the package
