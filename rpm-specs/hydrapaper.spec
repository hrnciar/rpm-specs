%global uuid    org.gabmus.%{name}

Name:           hydrapaper
Version:        1.11
Release:        2%{?dist}
Summary:        Set two different backgrounds for each monitor on GNOME

License:        GPLv3+
URL:            https://gitlab.com/gabmus/HydraPaper
Source0:        %{url}/-/archive/%{version}/HydraPaper-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  libhandy-devel
BuildRequires:  meson >= 0.50.0
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20

Requires:       dbus-common
Requires:       glib2
Requires:       hicolor-icon-theme
Requires:       libhandy
Requires:       python3-pillow

%description
GTK utility to set two different backgrounds for each monitor on GNOME (which
lacks this feature).


%prep
%autosetup -n HydraPaper-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license COPYING LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/*.xml
%{python3_sitelib}/%{name}/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.11-2
- Rebuilt for Python 3.9

* Wed May 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.11-1
- Update to 1.11

* Sat Apr 11 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.10-1
- Update to 1.10

* Sat Mar 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.9.9-2
- Remove 'libwnck3'

* Sat Mar 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.9.9-1
- Update to 1.9.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 08 2019 Kalev Lember <klember@redhat.com> - 1.9.8-2
- Add missing libhandy requires

* Tue Dec 03 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.9.8-1
- Update to 1.9.8
- Minor spec file fixes

* Mon Sep 16 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.9.4-1
- Update to 1.9.4

* Wed Sep 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.9.2-1
- Update to 1.9.2

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9-2
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.9-1
- Update to 1.9

* Wed Jul 31 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.7.3-1
- Initial package
