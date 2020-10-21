Name:           jack-mixer
Version:        14
Release:        1%{?dist}
Summary:        JACK Audio Mixer

# nsmclient.py is expat, everything else is GPLv2
License:        GPLv2 and MIT

URL:            https://rdio.space/jackmixer/
Source0:        https://github.com/%{name}/jack_mixer/archive/release-%{version}/%{name}-%{version}.tar.gz

# Build fails on these archs, upstream doesn't care.
ExcludeArch:    armv7hl
ExcludeArch:    i686

BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  python3-gobject-devel
BuildRequires:  python3dist(pycairo)
BuildRequires:  python3dist(pygobject)
BuildRequires:  python3-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  glib2-devel
BuildRequires:  desktop-file-utils
# jack-audio-connection-kit must be explicitly called for pipewire-jack compatibility
Requires:       jack-audio-connection-kit
Requires:       hicolor-icon-theme

%description
jack_mixer is an audio mixer for JACK with a look similar to its hardware
counterparts. Many features are available, here is a short list:

 - Mix any number of input channels (mono or stereo).
 - Control balance and faders with MIDI commands.
 - Handle session management with LASH.
 - Create as many outputs as necessary.
 - Quickly monitor inputs (PFL) and outputs.

%prep
%setup -q -n jack_mixer-release-%{version}


%build
NOCONFIGURE=1 ./autogen.sh
%configure
%make_build


%install
%make_install
rm %{buildroot}%{python3_sitelib}/jack_mixer_c.la
mkdir -p %{buildroot}%{python3_sitearch}
mv %{buildroot}%{python3_sitelib}/* %{buildroot}%{python3_sitearch}
desktop-file-validate %{buildroot}%{_datadir}/applications/jack_mixer.desktop
%py3_shebang_fix %{buildroot}%{_bindir}/jack_mixer.py

%files
%license COPYING
%doc README.md NEWS
%{_bindir}/jack_mix_box
%{_bindir}/jack_mixer
%{_bindir}/jack_mixer.py
%{python3_sitearch}/*
%{_datadir}/applications/jack_mixer.desktop
%{_datadir}/icons/hicolor/*/apps/jack_mixer.*
%{_datadir}/jack_mixer/


%changelog
* Thu Oct 15 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 14-1
- New upstream release
- Changes to channel fader/meter layout and features:
  - Added K20 and K14 scales.
  - Added tick marks for left/center/right on balance slider and add tooltip
    displaying left/right value.
  - Added maximum width for control group labels. Labels are ellipsized if too
    long and a tooltip with the full name is added.
- Channel add/property dialogs usability improvements:
  - Remember last used settings for new input/outut channel dialogs (MIDI CCs
    are always initialized with -1 by default, so they can be auto-assigned).
  - Channel name is pre-filled in with "Input" or "output" and an
    auto-incremented number suffix.
  - Add mnemonics for all input/output channel dialog fields.
- When running under NSM, closing the main window only hides UI and the "Quit"
  menu entry is replaced with a "Hide" entry.
- Added a global option to always ask for confirmation when quitting
  jack_mixer.
- Allow drag'n'drop to change channel positions.
- Added ability to shrink/expand width of input and output channels.
- The font color of control group labels automatically adapts to their
  background color for better contrast and readability.
- Fixed: Ctrl-click on volume fader sets it to 0.0 dbFS, not 1.0.
- Fixed: some issues with channel monitoring.
- Fixed: don't create empty project file on new NSM session.
- Fixed: on project load, give input focus to fader of last added channel and
  deselect volume entry widget so keyboard input doesn't accidentally change
  the value.

* Sat Oct 10 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 13-1
- New package for Fedora
