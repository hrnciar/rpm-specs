Name:     flatpak-xdg-utils
Summary:  Command-line tools for use inside Flatpak sandboxes
Version:  1.0.1
Release:  2%{?dist}
License:  LGPLv2+
URL:      https://github.com/flatpak/flatpak-xdg-utils
Source:   https://github.com/flatpak/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)

Requires: flatpak-spawn%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
This package contains a number of command-line utilities for use inside
Flatpak sandboxes. They work by talking to portals.

%package -n     flatpak-spawn
Summary:        Command-line frontend for the org.freedesktop.Flatpak service
License:        LGPLv2+
Conflicts:      flatpak-xdg-utils < 1.0.0-4

%description -n flatpak-spawn
This package contains the flatpak-spawn command-line utility. It can be
used to talk to the org.freedesktop.Flatpak service to spawn new sandboxes,
run commands on the host, or use one of the session or system helpers.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%license COPYING
%{_bindir}/xdg-email
%{_bindir}/xdg-open

%files -n flatpak-spawn
%license COPYING
%{_bindir}/flatpak-spawn

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 23 2020 Kalev Lember <klember@redhat.com> - 1.0.1-1
- Update to 1.0.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 15 2019 Kalev Lember <klember@redhat.com> - 1.0.0-5
- Fix the name of the new subpackage to actually be flatpak-spawn

* Fri Sep 13 2019 Debarshi Ray <rishi@fedoraproject.org> - 1.0.0-4
- Split flatpak-spawn into a separate sub-package

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Owen Taylor <otaylor@redhat.com> - 1.0.0-1
- Initial version
