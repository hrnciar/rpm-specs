# -*-Mode: rpm-spec -*-

%global commit 6388a49e0f431d6d5fcbd152b8ae4fa8e87884ee
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global _hardened_build 1

Name:     wshowkeys
Version:  0
Release:  3.20200727git%{shortcommit}%{?dist}
Summary:  Displays key presses on screen on supported Wayland compositors
License:  GPLv3
URL:      https://git.sr.ht/~sircmpwn/wshowkeys
Source0:  %{url}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: libinput-devel
BuildRequires: libudev-devel
BuildRequires: meson
BuildRequires: pango-devel
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: wayland-protocols-devel

%description
Displays key presses on screen on supported Wayland compositors
(requires wlr_layer_shell_v1 support eg sway).

Usage

wshowkeys [-b|-f|-s #RRGGBB[AA]] [-F font] [-t timeout]
    [-a top|left|right|bottom] [-m margin] [-o output]

    -b #RRGGBB[AA]: set background color
    -f #RRGGBB[AA]: set foreground color
    -s #RRGGBB[AA]: set color for special keys
    -F font: set font (Pango format, e.g. 'monospace 24')
    -t timeout: set timeout before clearing old keystrokes
    -a top|left|right|bottom: anchor the keystrokes to an edge.
       May be specified twice.
    -m margin: set a margin (in pixels) from the nearest edge
    -o output: request wshowkeys is shown on the specified
       output (unimplemented)

%prep
%autosetup -n %{name}-%{commit}

%build
%meson
%meson_build

%install
%meson_install

%files
%attr (4711,root,root) %{_bindir}/%{name}

%doc README.md

%license LICENSE

%changelog
* Wed Jul 29 2020 Bob Hepple <bob.hepple@gmail.com> - 0-3.20200727git6388a49
- rebuilt

* Wed Jul 29 2020 Bob Hepple <bob.hepple@gmail.com> - 0-2.20200727git6388a49
- rebuilt

* Mon Jul 27 2020 Bob Hepple <bob.hepple@gmail.com> - 1.20200727git6388a49
- Initial version of the package
