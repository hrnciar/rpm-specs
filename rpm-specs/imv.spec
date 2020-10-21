Name:           imv
Version:        4.1.0
Release:        3%{?dist}
Summary:        Image viewer for X11 and Wayland

License:        MIT
URL:            https://github.com/eXeC64/imv
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         imv-unbundle-inih-library.patch

BuildRequires:  asciidoc
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  inih-devel
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(icu-io)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(xkbcommon)
# wayland
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
# x11
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon-x11)
# backends
BuildRequires:  freeimage-devel
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.44
BuildRequires:  pkgconfig(libturbojpeg)

%description
imv is a command line image viewer intended for use with tiling window managers.
Features:
 - Native Wayland and X11 support
 - Support for dozens of image formats including: PNG, JPEG, animated GIFs, SVG,
    TIFF, various RAW formats, Photoshop PSD files
 - Configurable key bindings and behavior
 - Highly scriptable with IPC via imv-msg


%prep
%autosetup -p1


%build
# enable libjpeg-turbo support
sed -i 's/LIBJPEG=.*$/LIBJPEG=yes/' config.mk
%set_build_flags
%make_build

%install
%make_install
# install platform-specific manuals
for manfile in %{name}-wayland.1 %{name}-x11.1; do
    ln -sf %{name}.1 %{buildroot}%{_mandir}/man1/$manfile
done


%check
%set_build_flags
%make_build check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop


%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/%{name}_config
%{_bindir}/%{name}
%{_bindir}/%{name}-msg
%{_bindir}/%{name}-wayland
%{_bindir}/%{name}-x11
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}*
%{_mandir}/man5/%{name}*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 16 2020 Pete Walter <pwalter@fedoraproject.org> - 4.1.0-2
- Rebuild for ICU 67

* Wed Mar 25 2020 Aleksei Bavshin <alebastr89@gmail.com> - 4.1.0-1
- Initial package (#1812761)
