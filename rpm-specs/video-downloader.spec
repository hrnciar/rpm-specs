%global uuid    com.github.unrud.VideoDownloader

Name:           video-downloader
Version:        0.5.8
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
Requires:       libhandy1 >= 0.90.0
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
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
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
* Sun Oct  4 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.8-1
- Update to 0.5.8

* Sun Sep 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.7-1
- Update to 0.5.7

* Sat Sep 19 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.6-1
- Update to 0.5.6

* Mon Sep  7 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.5-1
- Update to 0.5.5

* Mon Aug 31 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5.3-1
- Update to 0.5.3

* Wed Aug 26 19:19:37 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.1-1
- Update to 0.4.1

* Sun Aug 16 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.0-1
- Update to 0.4.0
- Add new dep: libhandy1

* Tue Aug 11 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.3.3-1
- Update to 0.3.3

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.3.2-1
- Update to 0.3.2

* Mon Jul 06 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.3.1-1
- Update to 0.3.1

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
