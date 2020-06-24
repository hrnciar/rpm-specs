# -*-Mode: rpm-spec -*-

Name:     wdisplays
Version:  1.0
Release:  1%{?dist}
Summary:  GUI display configurator for wlroots compositors
License:  MIT and GPLv3+ and CC0 and CC-BY-SA
URL:      https://github.com/cyclopsian/wdisplays

Source:  %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gtk3-devel
BuildRequires: meson
BuildRequires: wayland-devel
BuildRequires: wlroots-devel

Conflicts: wlroots < 0.7.0
Requires:  hicolor-icon-theme

%description

wdisplays is a graphical application for configuring displays in
Wayland compositors. It borrows some code from kanshi. It should work
in any compositor that implements the
wlr-output-management-unstable-v1 protocol, including sway. The goal
of this project is to allow precise adjustment of display settings in
kiosks, digital signage, and other elaborate multi-monitor setups.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
desktop-file-install --dir %{buildroot}/%{_datadir}/applications \
    --set-icon %{name} \
    --set-key=Terminal --set-value=false \
    --remove-key=Version \
    --add-category=Settings --add-category=HardwareSettings \
    %{_target_platform}/resources/network.cycles.%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/icons/*

%doc README.md

%license LICENSES/*

%changelog
* Fri May 15 2020 Bob Hepple <bob.hepple@gmail.com> - 1.0-1
- new release

* Tue May 05 2020 Bob Hepple <bob.hepple@gmail.com> - 0.9-0.4.20200504git0faafdc
- added hicolor-icon-theme

* Tue May 05 2020 Bob Hepple <bob.hepple@gmail.com> - 0.9-0.3.20200504git0faafdc
- rebuilt to use desktop-file-install to modify the desktop file instead of patching

* Mon May 04 2020 Bob Hepple <bob.hepple@gmail.com> - 0.9-0.2.20200504git.0faafdc
- rebuilt for RHBZ#1830870

* Mon May 04 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1-0.1.20200504git.0faafdc
- prepare for Fedora review

* Wed Feb 19 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1-0.1.20200219git.ba331ca
- Initial version of the package
