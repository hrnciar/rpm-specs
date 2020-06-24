%global uuid    com.github.unrud.VideoDownloader

Name:           video-downloader
Version:        0.3.0
Release:        1%{?dist}
Summary:        Download videos from websites like YouTube and many others

License:        GPLv3+
URL:            https://github.com/Unrud/video-downloader
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  librsvg2-tools
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(glib-2.0)

Requires:       gtk3
Requires:       hicolor-icon-theme
Requires:       python3-xlib
Requires:       youtube-dl

%description
Download videos from websites with an easy-to-use interface. Provides the
following features:

- Convert videos to MP3
- Supports password-protected and private videos
- Download single videos or whole playlists
- Automatically selects a video format based on your preferred resolution

Based on youtube-dl.


%prep
%autosetup -p1


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
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/*.xml


%changelog
* Sat Jun 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.3.0-1
- Update to 0.3.0

* Sun Jun 14 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.10-1
- Update to 0.2.10

* Sun May 17 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.9-1
- Update to 0.2.9

* Sun May 03 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.8-1
- Update to 0.2.8

* Wed Apr 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.6-1
- Update to 0.2.6

* Wed Feb 19 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.5-1
- Update to 0.2.5

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.3-1
- Update to 0.2.3

* Sat Jan 11 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.2-1
- Update to 0.2.2

* Sat Jan 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.1-1
- Update to 0.2.1
- Upstream switched to GTK now

* Sun Sep 08 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.5-6
- Initial package