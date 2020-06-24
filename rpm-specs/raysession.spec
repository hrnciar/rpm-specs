Name:               raysession
Version:            0.8.3
Release:            1%{?dist}
Summary:            Session manager for audio software
BuildArch:          noarch


# The entire source code is GPLv2

License:            GPLv2
URL:                https://github.com/Houston4444/RaySession
Source0:            %{url}/archive/v%{version}/RaySession-%{version}.tar.gz
# https://github.com/Houston4444/RaySession/issues/44
Source1:            README-wayland
# https://github.com/Houston4444/RaySession/issues/38
Patch0:             %{name}-0001-fix-invalid-category.patch
# https://github.com/Houston4444/RaySession/issues/39
Patch1:             %{name}-0002-remove-unnecessary-shebang.patch

BuildRequires:      python3-qt5
BuildRequires:      qt5-linguist
BuildRequires:      desktop-file-utils
Requires:           python3 
Requires:           python3-qt5
Requires:           python3-pyliblo
Requires:           hicolor-icon-theme
Requires:           shared-mime-info
Recommends:         wmctrl
Recommends:         git
Recommends:         jack-audio-connection-kit

%description
Ray Session is a GNU/Linux session manager for audio programs as Ardour,
Carla, QTractor, Non-Timeline, etc...

It uses the same API as Non Session Manager, so programs compatible with NSM
are also compatible with Ray Session. As Non Session Manager, the principle
is to load together audio programs, then be able to save or close all
documents together.

Ray Session offers a little more:

 - Factory templates for NSM and LASH compatible applications
 - Possibility to save any client as template
 - Save session as template
 - Name files with a prettier way
 - remember if client was started or not
 - Abort session almost anytime
 - Change Main Folder of sessions on GUI
 - Possibility to KILL client if clean exit is too long
 - Open Session Folder button (open default file manager)

 Ray Session is being developed by houston4444, using Python3 and Qt5.

%prep
%autosetup -p 1 -n RaySession-%{version}
/usr/bin/cp %{SOURCE1} ./
#remove space in "snapshots explain" https://github.com/Houston4444/RaySession/issues/40
mv snapshots\ explain snapshots-explain

%build
%{set_build_flags}
make LRELEASE=lrelease-qt5 %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc README.md
%doc TODO
%doc TRANSLATORS
%doc snapshots-explain
%doc README-wayland
%license COPYING
%{_bindir}/ray-daemon
%{_bindir}/ray_control
%{_bindir}/raysession
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.*
# No manpages, developer is aware https://github.com/Houston4444/RaySession/issues/40

%changelog
* Sat Feb 8 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 0.8.3-1
- Initial release for Fedora
