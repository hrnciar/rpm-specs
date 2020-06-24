Name:           butt
Version:        0.1.19
Release:        1%{?dist}
Summary:        Broadcast using this tool
License:        GPLv2+
URL:            https://danielnoethen.de

Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        butt.appdata.xml

BuildRequires:  gcc-c++
BuildRequires:  fltk-devel
BuildRequires:  portaudio-devel
BuildRequires:  lame-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libogg-devel
BuildRequires:  flac-devel
BuildRequires:  opus-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  fdk-aac-free-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  libX11-devel
BuildRequires:  desktop-file-utils
BuildRequires:  autoconf
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme


%description
butt (broadcast using this tool) is an easy to use, multi OS streaming tool.
It supports ShoutCast and IceCast and runs on Linux, MacOS and Windows.  The
main purpose of butt is to stream live audio data from your computers Mic or
Line input to an Shoutcast or Icecast server. Recording is also possible.  It
is NOT intended to be a server by itself or automatically stream a set of audio
files.


%prep
%autosetup -p 1
autoreconf -ifv


%build
%configure LIBS=-lX11
%make_build


%install
%make_install

# desktop file
desktop-file-install --dir %{buildroot}%{_datadir}/applications usr/share/applications/butt.desktop
# icons
for size in 16 22 24 32 48 64 96 128 256 512; do
    path=icons/hicolor/${size}x${size}/apps/butt.png
    install -Dpm 0644 usr/share/$path %{buildroot}%{_datadir}/$path
done
install -Dpm 0644 usr/share/icons/hicolor/scalable/apps/butt.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/butt.svg
# pixmaps
for size in 16 32; do
    path=pixmaps/butt$size.xpm
    install -Dpm 0644 usr/share/$path %{buildroot}%{_datadir}/$path
done
# appdata
appstream-util validate-relax --nonet %{S:1}
install -Dpm 0644 %{S:1} %{buildroot}%{_metainfodir}/butt.appdata.xml


%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS
%{_bindir}/butt
%{_datadir}/applications/butt.desktop
%{_datadir}/icons/hicolor/*/apps/butt.*
%{_datadir}/pixmaps/butt*.xpm
%{_metainfodir}/butt.appdata.xml


%changelog
* Tue Mar 17 2020 Carl George <carl@george.computer> - 0.1.19-1
- Latest upstream

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 12 2019 Carl George <carl@george.computer> - 0.1.18-1
- Latest upstream

* Tue Apr 09 2019 Carl George <carl@george.computer> - 0.1.17-3
- Re-enable s390x via patch0

* Sun Apr 07 2019 Carl George <carl@george.computer> - 0.1.17-2
- Exclude s390x rhbz#1697142

* Fri Apr 05 2019 Carl George <carl@george.computer> - 0.1.17-1
- Initial package
