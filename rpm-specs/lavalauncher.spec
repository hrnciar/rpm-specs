# -*-Mode: rpm-spec -*-

Name:     lavalauncher
Version:  1.7.0
Release:  1%{?dist}
Summary:  %{name} is a simple launcher for Wayland
License:  GPLv3
URL:      https://git.sr.ht/~leon_plickat/%{name}
Source0:  %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

# f-32 throws a multiple definition of `pointer_listener' at src/input.h:24
# upstream have been notified (no bug reporting system is in place)
Patch0:   lavalauncher-fix-f32-error.patch

BuildRequires: gcc
BuildRequires: cairo-devel
BuildRequires: meson
BuildRequires: scdoc
BuildRequires: wayland-devel
BuildRequires: wayland-protocols-devel

%description
LavaLauncher is a simple launcher for Wayland.

It serves a single purpose: Letting the user execute shell commands by
clicking on icons on a dynamically sized bar, placed at one of the
screen edges or in the center.

Unlike most popular launchers, LavaLauncher does not care about
.desktop files or icon themes. To create a button, you simply provide
the path to an image and a shell command. This makes LavaLauncher
considerably more flexible: You could have buttons not just for
launching applications, but also for ejecting your optical drive,
rotating your screen, sending your cat an email, playing a funny
sound, muting all audio, toggling your lamps, etc. You can turn
practically anything you could do in your shell into a button.

The configuration is done entirely via command flags. See the manpage
for details and an example.

LavaLauncher has been successfully tested with sway and wayfire.
%prep
%setup -n %{name}-v%{version}
%patch0 -p1 -R

%build
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/%{name}

%doc README.md
%{_mandir}/man1/%{name}.1.*

%license LICENSE

%changelog
* Sat May 16 2020 Bob Hepple <bob.hepple@gmail.com> - 1.7-1
- new version

* Thu Apr 09 2020 Bob Hepple <bob.hepple@gmail.com> - 1.6-4
- rebuilt for fedora review

* Wed Feb 19 2020 Bob Hepple <bob.hepple@gmail.com> - 1.6-3
- correct license to GPL3

* Tue Feb 18 2020 Bob Hepple <bob.hepple@gmail.com> - 1.6-2
- correct license to GPL2

* Mon Feb 17 2020 Bob Hepple <bob.hepple@gmail.com> - 1.6-1
- Initial version of the package
