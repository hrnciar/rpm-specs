%global _license COPYING COPYING.LGPL-2.1 COPYING.LGPL-3.0 LICENSE_CCBYSA

Name:       yaru-theme
Version:    20.10.6.1
Release:    1%{?dist}
Summary:    Ubuntu community theme "yaru"
BuildArch:  noarch

License:    GPLv3+ and CC-BY-SA
URL:        https://community.ubuntu.com/c/desktop/theme-refresh
Source0:    https://github.com/ubuntu/yaru/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: meson >= 0.51
BuildRequires: sassc
BuildRequires: pkgconfig(appstream-glib)

Requires:   gnome-shell-theme-yaru
Requires:   yaru-gtk2-theme
Requires:   yaru-gtk3-theme
Requires:   yaru-icon-theme
Requires:   yaru-sound-theme

%global _description %{expand:
Yaru theme is the default theme for Ubuntu, entirely backed by the community.
This is the theme that is shaped by the community on the Ubuntu hub, turned into
the default theme starting from Ubuntu 18.10 Cosmic Cuttlefish.}

%description %{_description}


%package     -n gnome-shell-theme-yaru
Summary:        Yaru GNOME Shell Theme

Recommends:     yaru-gtk3-theme
Recommends:     yaru-icon-theme

Suggests:       yaru-sound-theme
Suggests:       yaru-theme

%description -n gnome-shell-theme-yaru %{_description}

This package contains GNOME Shell Theme.


%package     -n yaru-gtk2-theme
Summary:        GTK+ 2 support for the Yaru GTK Theme

Requires:       adwaita-gtk2-theme
Requires:       gtk-murrine-engine

Recommends:     yaru-gtk3-theme

%description -n yaru-gtk2-theme %{_description}

This package contains GTK+ 2 theme.


%package     -n yaru-gtk3-theme
Summary:        GTK+ 3 support for the Yaru GTK Theme

Requires:       gtk3

Recommends:     yaru-gtk2-theme

%description -n yaru-gtk3-theme %{_description}

This package contains GTK+ 3 theme.


%package     -n yaru-icon-theme
Summary:        Yaru icon theme
License:        CC-BY-SA

Requires:       hicolor-icon-theme
Requires:       humanity-icon-theme

Suggests:       gnome-shell-theme-yaru
Suggests:       yaru-gtk3-theme
Suggests:       yaru-sound-theme

%description -n yaru-icon-theme %{_description}

This package contains the icon theme.


%package     -n yaru-sound-theme
Summary:        Yaru sound theme
License:        CC-BY-SA

%description -n yaru-sound-theme %{_description}

This package contains the sound theme following the XDG theming specification.


%prep
%autosetup -n yaru-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install

rm  %{buildroot}%{_datadir}/glib-2.0/schemas/99_Yaru.gschema.override \
    %{buildroot}%{_datadir}/xsessions/Yaru.desktop \
    %{buildroot}%{_datadir}/wayland-sessions/Yaru-wayland.desktop \
    %{buildroot}%{_datadir}/gnome-shell/extensions/ubuntu-dock@ubuntu.com/yaru.css

touch %{buildroot}%{_datadir}/icons/Yaru/icon-theme.cache

%transfiletriggerin -- %{_datadir}/icons/Yaru
gtk-update-icon-cache --force %{_datadir}/icons/Yaru &>/dev/null || :


# Workaround for replace directory with symlink which was added in Yaru
# * https://docs.fedoraproject.org/en-US/packaging-guidelines/Directory_Replacement/#_scriptlet_to_replace_a_directory
%pretrans -p <lua> -n gnome-shell-theme-yaru
path = "%{_datadir}/themes/Yaru-dark/gnome-shell"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end


%files
%license %{_license}
%doc AUTHORS CONTRIBUTING.md README.md

%files -n gnome-shell-theme-yaru
%license %{_license}
%{_datadir}/gnome-shell/modes/yaru.json
%{_datadir}/gnome-shell/theme/Yaru-dark/
%{_datadir}/gnome-shell/theme/Yaru/
%{_datadir}/themes/Yaru-dark/gnome-shell
%{_datadir}/themes/Yaru-dark/index.theme
%{_datadir}/themes/Yaru-light/index.theme
%{_datadir}/themes/Yaru/gnome-shell
%{_datadir}/themes/Yaru/index.theme
%dir %{_datadir}/themes/Yaru
%dir %{_datadir}/themes/Yaru-dark
%dir %{_datadir}/themes/Yaru-light
%ghost %{_datadir}/themes/Yaru-dark/gnome-shell.rpmmoved/

%files -n yaru-gtk2-theme
%license %{_license}
%{_datadir}/themes/Yaru-dark/gtk-2.0/
%{_datadir}/themes/Yaru-light/gtk-2.0/
%{_datadir}/themes/Yaru/gtk-2.0/
%dir %{_datadir}/themes/Yaru
%dir %{_datadir}/themes/Yaru-dark
%dir %{_datadir}/themes/Yaru-light

%files -n yaru-gtk3-theme
%license %{_license}
%{_datadir}/themes/Yaru-dark/gtk-3.*/
%{_datadir}/themes/Yaru-light/gtk-3.*/
%{_datadir}/themes/Yaru/gtk-3.*/
%dir %{_datadir}/themes/Yaru
%dir %{_datadir}/themes/Yaru-dark
%dir %{_datadir}/themes/Yaru-light

%files -n yaru-icon-theme
%license %{_license}
%{_datadir}/icons/Yaru/
%ghost %{_datadir}/icons/Yaru/icon-theme.cache

%files -n yaru-sound-theme
%license %{_license}
%{_datadir}/sounds/Yaru/


%changelog
* Sun Oct 11 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 20.10.6.1-1
- build(update): 20.10.6.1

* Tue Oct  6 19:52:37 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 20.10.6-1
- build(update): 20.10.6

* Thu Sep 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 20.10.4-1
- Update to 20.10.4

* Fri Sep 11 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 20.10.3-1
- Update to 20.10.3
- Don't build yaru-unity-theme

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 20.04.6-3
- Workaround for replace directory with symlink which was added in Yaru | Thanks for tip @zawertun

* Sat Apr 18 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 20.04.6-2
- Add new 'yaru-unity-theme' subpackage

* Fri Apr 17 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 20.04.6-1
- Update to 20.04.6

* Thu Apr 16 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 20.04.5-1
- Update to 20.04.5

* Tue Mar 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 20.04.4-1
- Update to 20.04.4

* Fri Feb 07 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 20.04.1-1
- Update to 20.04.1

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 19.10.5-1
- Update to 19.10.5

* Thu Nov 21 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 19.10.4-1.20191118git1937b28
- Update to latest git snapshot which contain broken gnome-shell theme fix

* Fri Sep 27 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 19.10.3-1
- Update to 19.10.3
- Add new light variant
- Drop fdupes

* Tue Sep 10 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 19.10.1-2
- Update to 19.10.1

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.04.1-3.20190425git0ddb244
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 26 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 19.04.1-2.20190425git0ddb244
- Adapt for Fedora

* Fri Jan 18 10:30:30 UTC 2019 - dead_mozay@opensuse.org
- Update to version 19.04+20190117.f36189f4

* Wed Jan 02 11:51:35 UTC 2019 - dead_mozay@opensuse.org
- Update to version 18.10.7+20190101.1db0abb5
