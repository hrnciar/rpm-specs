%global uuid    com.github.bcedu.%{name}

Name:           vgrive
Version:        1.6.1
Release:        2%{?dist}
Summary:        Google Drive client for Linux

License:        GPLv3+
URL:            https://github.com/bcedu/VGrive
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(unity)

Requires:       hicolor-icon-theme

%description
VGrive is a client (back-end and front-end) for Google Drive made in vala.

- Start VGrive and sync your files with Google Drive through a clean and
  minimalist gui.
- Automaticlly detects changes in local and remote files and sync them.
- Choose the local path where VGrive syncs your files.


%prep
%autosetup -n VGrive-%{version}


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{uuid}

# HiDPI version equal to regular
rm -r %{buildroot}%{_datadir}/icons/hicolor/*@2


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{uuid}.lang
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/%{uuid}
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/*.xml


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 13 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6.1-1
- Update to 1.6.1

* Thu Apr 16 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6.0-1
- Update to 1.6.0

* Fri Apr 10 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.5.2-1
- Update to 1.5.2

* Sun Mar 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.5.0-1
- Update to 1.5.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 22 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.4.0-1
- Update to 1.4.0

* Fri Nov 08 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.3.0-1
- Update to 1.3.0

* Wed Nov 06 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.2.4-1
- Update to 1.2.4

* Sat Nov 02 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.2.3-1
- Update to 1.2.3

* Fri Nov 01 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.2.2-1
- Update to 1.2.2

* Wed Oct 30 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Tue Oct 29 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.10-1
- Initial package
