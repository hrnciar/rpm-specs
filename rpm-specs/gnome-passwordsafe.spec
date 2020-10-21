# forked from https://build.opensuse.org/package/view_file/openSUSE:Factory/gnome-passwordsafe/gnome-passwordsafe.spec
# spec file for package gnome-passwordsafe
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

%global appname PasswordSafe
%global sysname passwordsafe
%global uuid    org.gnome.%{appname}

Name:           gnome-%{sysname}
Version:        3.99.2
Release:        2%{?dist}
Summary:        Password manager for GNOME

License:        GPLv3
URL:            https://gitlab.gnome.org/World/PasswordSafe
Source0:        %{url}/-/archive/%{version}/%{appname}-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.50.0
BuildRequires:  python3-devel >= 3.6.5
BuildRequires:  python3dist(pykeepass)
BuildRequires:  python3dist(setuptools)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.35.9
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.1
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(pwquality) >= 1.4.0

Requires:       hicolor-icon-theme
Requires:       libhandy1
Requires:       python3-crypto
Requires:       python3-pwquality
Requires:       python3-pykeepass >= 3.2.0

%description
Password Safe is a password manager which makes use of the KeePass v.4 format.
It integrates perfectly with the GNOME desktop and provides an easy and
uncluttered interface for the management of password databases.


%prep
%autosetup -n %{appname}-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{sysname}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{sysname}.lang
%license LICENSE
%doc README.md
%{_bindir}/gnome-%{sysname}
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/%{sysname}/
%{_metainfodir}/*.xml
%{python3_sitelib}/%{sysname}/


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.99.2-1
- Update to 3.99.2
- Built with libhandy-1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.99.1-5
- Rebuilt for Python 3.9

* Wed Feb 05 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.99.1-4
- Add dep: libhandy

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.99.1-2
- Deps fix

* Sun Jan 19 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.99.1-1
- Update to 3.99.1
- Mininum 'pykeepass' version now >= 3.2.0

* Tue Oct 29 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 3.32.0-3
- Add missed deps

* Wed Sep 25 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 3.32.0-2
- Packaging fixes

* Fri Jun 14 2019 Pavlo Rudyi <paulcarroty@fedoraproject.org> - 3.32-1
- initial build
