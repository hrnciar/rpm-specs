Name:           goverlay
Version:        0.3.5
Release:        1%{?dist}
Summary:        Project that aims to create a Graphical UI to help manage Linux overlays

License:        GPLv3+
URL:            https://github.com/benjamimgois/goverlay
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         goverlay-enable-debuginfo-generation.patch
ExclusiveArch:  %{fpc_arches}

BuildRequires:  desktop-file-utils
BuildRequires:  fpc-srpm-macros
BuildRequires:  lazarus
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(gtk+-3.0)

Requires:       hicolor-icon-theme
Requires:       mangohud%{?_isa}

Recommends:     mesa-demos%{?_isa}
Recommends:     vulkan-tools%{?_isa}

# TODO: WIP. Packaging stalled because of Meson port.
%dnl Recommends:     vkBasalt%{?_isa}

%description
GOverlay is an open source project aimed to create a Graphical UI to manage
Linux overlays. It is still in early development, so it lacks a lot of features.

This project was only possible thanks to the other maintainers and contributors
that have done the hard work. I am just a Network Engineer that really likes
Linux and Gaming.


%prep
%autosetup -p1


%build
lazbuild -B %{name}.lpi


%install
install -Dp -m0755 %{name} -t %{buildroot}%{_bindir}/
install -Dp -m0644 data/%{name}.desktop -t %{buildroot}%{_datadir}/applications/
install -Dp -m0644 data/icons/512x512/%{name}.png -t %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/
install -Dp -m0644 data/%{name}.metainfo.xml -t %{buildroot}%{_metainfodir}/


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop



%files
%license LICENSE
%doc README.md
%{_bindir}/{%name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_metainfodir}/*.xml


%changelog
* Mon Jun 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.3.5-1
- Update 0.3.5

* Sat Jun 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.3.4-1
- Update 0.3.4

* Fri May 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.3.3-1
- Update 0.3.3

* Fri Apr 10 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.3.1-1
- Update 0.3.1

* Sat Apr 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.3-1
- Update 0.3
- Add few weak deps
- Update description to sync with upstream

* Sun Mar 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.4-1
- Update 0.2.4

* Thu Mar 26 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.3-1
- Update 0.2.3

* Mon Mar 16 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.1-2
- Enable debuinfo generation. Thanks to Artur Iwicki for help with packaging.

* Sat Mar 14 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.1-1
- Initial package
