%global url_ver	%%(echo %{version}|cut -d. -f1,2)
%global libgtop2_version 2.37.2

Name:		gnome-usage
Version:	3.33.2
Release:	2%{?dist}
Summary:	A GNOME app to view information about use of system resources

License:	GPLv3+
URL:		https://wiki.gnome.org/Apps/Usage
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	meson
BuildRequires:	pkgconfig(accountsservice)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libdazzle-1.0)
BuildRequires:	pkgconfig(libgtop-2.0) >= %{libgtop2_version}
BuildRequires:  pkgconfig(tracker-sparql-2.0)
BuildRequires:	vala
BuildRequires:	yelp-tools

Requires:	adwaita-icon-theme
Requires:	libgtop2%{?_isa} >= %{libgtop2_version}

%description
gnome-usage lets you easily visualize the use of system resources such as
CPU, memory, and storage.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} --with-gnome

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Usage.desktop

%files -f %{name}.lang
%license LICENSE
%doc AUTHORS README.md NEWS
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Usage.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Usage.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Usage.svg
%{_datadir}/metainfo/org.gnome.Usage.appdata.xml

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jul 30 2019 Felipe Borges <feborges@redhat.com> - 3.33.2-1
- Update to 3.33.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Felipe Borges <feborges@redhat.com> - 3.33.1-1
- Update to 3.33.1

* Fri Mar 22 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 25 2018 Feliep Borges <feborges@redhat.com> - 3.30.1-1
- Update to 3.30.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Fri Mar 09 2018 Felipe Borges <feborges@redhat.com> - 3.27.92-1
- Initial import
