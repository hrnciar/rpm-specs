Name: cozy
%global rtld_name com.github.geigi.cozy

Summary: Modern audiobook player
License: GPLv3+ and ASL 2.0

Version: 0.7.2
Release: 2%{?dist}

URL: https://cozy.geigi.de
Source0: https://github.com/geigi/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

Patch0: %{name}--unbundle-inject.patch

BuildArch: noarch

BuildRequires: desktop-file-utils
BuildRequires: gtk3-devel >= 3.22
BuildRequires: libappstream-glib
BuildRequires: meson >= 0.40.0
BuildRequires: python3-devel
BuildRequires: xmlstarlet

%global with_tests 1

%if 0%{?with_tests}
BuildRequires: gstreamer1-plugins-base

BuildRequires: python3dist(apsw)
BuildRequires: python3dist(distro)
BuildRequires: python3dist(inject) >= 4.3.1
BuildRequires: python3dist(mutagen)
BuildRequires: python3dist(peewee) >= 3.9.6
BuildRequires: python3dist(pygobject)
BuildRequires: python3dist(pytest-runner)
BuildRequires: python3dist(pytest-mock)
BuildRequires: python3dist(pytz)
BuildRequires: python3dist(requests)
%endif

Requires: file
Requires: glib2
Requires: gstreamer1-plugins-bad-free
Requires: gstreamer1-plugins-good
Requires: gstreamer1-plugins-ugly-free
Requires: hicolor-icon-theme

# Not available in official Fedora repos
# Requires: gstreamer1-libav


%description
Cozy is a modern audiobook player for Linux.

Here are some of the current features:
- Import your audiobooks into Cozy to browse them comfortably
- Sort your audio books by author, reader & name
- Remembers your playback position
- Sleep timer
- Playback speed control
- Search your library
- Offline Mode! This allows you to keep an audio book on your internal storage
  if you store your audiobooks on an external or network drive.
  Perfect for listening on the go!
- Add mulitple storage locations
- Drag & Drop to import new audio books
- Support for DRM free mp3, m4a (aac, ALAC, …), flac, ogg, opus, wav files
- Mpris integration (Media keys & playback info for desktop environment)


%prep
%setup -q

# Unbundle inject
%patch0 -p1
rm -rf cozy/ext/inject

# Add a nonsensical <p> tag at the beginning of <description> for every
# <release> in the appdata XML - needed to pass validation
xmlstarlet ed \
	--insert component/releases/release/description/ul \
	--type elem -n p -v 'List of changes:' \
	< "data/%{rtld_name}.appdata.xml.in" > appdata.patched
mv ./appdata.patched "data/%{rtld_name}.appdata.xml.in"


%build
%meson
%meson_build
%meson_build com.github.geigi.cozy-update-po
%meson_build extra-update-po


%install
%meson_install
%find_lang %{rtld_name}


%check
%if 0%{?with_tests}
%pytest
%endif
appstream-util validate --nonet %{buildroot}/%{_datadir}/metainfo/%{rtld_name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rtld_name}.desktop


%files -f %{rtld_name}.lang
%doc README.md
%license LICENSE
%{_bindir}/%{rtld_name}
%{_datadir}/%{rtld_name}/
%{_datadir}/applications/%{rtld_name}.desktop
%{_datadir}/glib-2.0/schemas/%{rtld_name}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{rtld_name}.svg
%{_datadir}/icons/hicolor/scalable/actions/*-symbolic.svg
%{_metainfodir}/%{rtld_name}.appdata.xml
%{python3_sitelib}/%{name}/


%changelog
* Thu Oct 01 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.7.2-2
- Unbundle python3-inject

* Mon Sep 28 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.7.2-1
- Update to latest release
- Use python3dist() for specifying dependencies

* Fri Sep 25 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.7.1-1
- Update to latest release

* Fri Sep 25 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.7-1
- Update to latest release
- Put tests behind an enable/disable macro

* Fri Sep 11 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.6.19-1
- Initial packaging

