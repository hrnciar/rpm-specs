%global uuid    com.leinardi.%{name}

Name:           gwe
Version:        0.15.2
Release:        1%{?dist}
Summary:        System utility designed to provide information of NVIDIA card

License:        GPLv3+
URL:            https://gitlab.com/leinardi/gwe
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        README.fedora.md
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.45.1
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.56.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.30

Requires:       dbus-common
Requires:       hicolor-icon-theme
Requires:       libdazzle
Requires:       python3-gobject
Requires:       python3-injector >= 0.18.2
Requires:       python3-matplotlib-gtk3 >= 3.1.1
Requires:       python3-peewee >= 3.13.3
Requires:       python3-py3nvml >= 0.2.6
Requires:       python3-pyxdg >= 0.26
Requires:       python3-requests
Requires:       python3-rx >= 3.0.1
Requires:       python3-xlib >= 0.26

# Conditional dep for GNOME
Recommends:     (gnome-shell-extension-appindicator if gnome-shell)

Recommends:     libappindicator-gtk3

%description
GWE is a GTK system utility designed to provide information, control the fans
and overclock your NVIDIA video card and graphics processor.

This package require NVIDIA driver. Please read included README.Fedora file:

  xdg-open %{_docdir}/%{name}/README.fedora.md


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
install -m0644 -Dp %{SOURCE1} %{buildroot}%{_docdir}/%{name}/README.fedora.md

# Remove HiDPI version PNG icons since we have SVG version here
rm -r %{buildroot}%{_datadir}/icons/hicolor/*@2x/


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license COPYING.txt
%doc CHANGELOG.md README.md README.fedora.md RELEASING.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/symbolic/*/*.svg
%{_metainfodir}/*.xml
%{python3_sitelib}/%{name}/


%changelog
* Sun Oct 18 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.15.2-1
- build(update): 0.15.2

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.15.1-1
- Update to 0.15.1

* Mon Jun 08 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.15.0-1
- Update to 0.15.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.14.1-3
- Rebuilt for Python 3.9

* Sat Apr 11 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.14.1-2
- Add dep 'libdazzle'

* Fri Apr 10 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.14.1-1
- Update to 0.14.1

* Sun Feb 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.14.0-1
- Update to 0.14.0

* Wed Feb 19 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.13.3-8
- Add 'libappindicator-gtk3' as weak dep

* Wed Feb 19 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.13.3-7
- Add conditional deps for GNOME desktop

* Tue Jan 28 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.13.3-6
- Improve description

* Sun Jan 26 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.13.3-3
- Minor packaging fixes

* Wed Jan 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.13.3-2
- Update to 0.13.3

* Sun Sep 01 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.13.0-1
- Update to 0.13.0

* Tue Mar 12 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.12.3-7
- Updated spec file

* Tue Mar 12 2019 Dead Mozay <dead_mozay@opensuse.org> - 0.12.3-1
- Initial package
