%global theme_name     Greybird

Name:           greybird
Version:        3.22.12
Release:        2%{?dist}
Summary:        A clean minimalistic theme for Xfce, GTK+ 2 and 3

License:        GPLv2+ or CC-BY-SA
URL:            http://shimmerproject.org/project/%{name}/ 
Source0:        https://github.com/shimmerproject/%{theme_name}/archive/v%{version}.tar.gz

Patch0:         light_remove_unity.patch
Patch1:         dark_remove_unity.patch

BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  librsvg2-devel
BuildRequires:  meson
BuildRequires:  sassc
BuildRequires:  rubygem-sass

Requires:       gtk-murrine-engine

BuildArch:      noarch

Obsoletes:      greybird-gtk2-theme < 3.22.11
Obsoletes:      greybird-gtk3-theme < 3.22.11
Obsoletes:      greybird-metacity-theme < 3.22.11
Obsoletes:      greybird-xfce4-notifyd-theme < 3.22.11
Obsoletes:      greybird-xfwm4-themes < 3.22.11

Provides:       greybird = %{name}-%{release}

%description
Greybird is a theme for GTK2/3 and xfwm4/metacity started out on the basis of
Bluebird, but aims at reworking the intense blue tone to a more neutral
grey-ish look that will be more pleasant to look at in everyday use.

%package light-theme
Summary:        Greybird light themes

Requires:       gtk-murrine-engine

Obsoletes:      greybird-gtk2-theme < 3.22.11
Obsoletes:      greybird-gtk3-theme < 3.22.11
Obsoletes:      greybird-metacity-theme < 3.22.11
Obsoletes:      greybird-xfce4-notifyd-theme < 3.22.11
Obsoletes:      greybird-xfwm4-themes < 3.22.11
Provides:       greybird-dark-theme = %{name}-%{release}


%description light-theme
Light Themes as part of the Greybird theme.

%package dark-theme
Summary:        Greybird Dark themes

Requires:       gtk-murrine-engine

Obsoletes:      greybird-gtk2-theme < 3.22.11
Obsoletes:      greybird-gtk3-theme < 3.22.11
Obsoletes:      greybird-metacity-theme < 3.22.11
Obsoletes:      greybird-xfce4-notifyd-theme < 3.22.11
Obsoletes:      greybird-xfwm4-themes < 3.22.11
Provides:       greybird-dark-theme = %{name}-%{release}


%description dark-theme
Dark Themes as part of the Greybird theme.


%package metacity-theme
Summary:        Greybird Metacity themes
Requires:       metacity
Requires:       greybird-light-theme
Requires:       greybird-dark-theme

%description metacity-theme
Themes for Metacity as part of the Greybird theme.


%package xfwm4-theme
Summary:        Greybird Xfwm4 themes
Requires:       xfwm4
Requires:       greybird-light-theme
Requires:       greybird-dark-theme

%description xfwm4-theme
Themes for Xfwm4 as part of the Greybird theme.

%package xfce4-notifyd-theme
Summary:        Greybird Xfce4 notifyd theme
Requires:       xfce4-notifyd
Requires:       greybird-light-theme

%description xfce4-notifyd-theme
Themes for Xfce4 notifyd as part of the Greybird theme.

%package plank
Summary:        Greybird plank themes
Requires:       plank
Requires:       greybird-light-theme
Requires:       greybird-dark-theme

%description plank
Themes for plank as part of the Greybird theme.

%prep

%setup -q -n %{theme_name}-%{version}

# Cleanup
# Remove Unity theme
rm -fr light/unity
rm -fr dark/unity

%patch0 -p0
%patch1 -p0

%build
%meson

%meson_build

%install
%meson_install


%files light-theme
%doc LICENSE.GPL LICENSE.CC
%{_datadir}/themes/%{theme_name}/index.theme
%{_datadir}/themes/%{theme_name}/%{theme_name}.emerald
%{_datadir}/themes/%{theme_name}/gnome-shell/
%{_datadir}/themes/%{theme_name}/gtk-2.0/
%{_datadir}/themes/%{theme_name}/gtk-3.0/


%files dark-theme
%doc LICENSE.GPL LICENSE.CC
%{_datadir}/themes/%{theme_name}-dark/index.theme
%{_datadir}/themes/%{theme_name}-dark/%{theme_name}-dark.emerald
%{_datadir}/themes/%{theme_name}-dark/gnome-shell/
%{_datadir}/themes/%{theme_name}-dark/gtk-2.0/
%{_datadir}/themes/%{theme_name}-dark/gtk-3.0/


%files metacity-theme
%doc LICENSE.GPL LICENSE.CC
%dir %{_datadir}/themes/Greybird/
%{_datadir}/themes/%{theme_name}/metacity-1/
%{_datadir}/themes/%{theme_name}-dark/metacity-1/


%files xfwm4-theme
%doc LICENSE.GPL LICENSE.CC
%dir %{_datadir}/themes/Greybird/
%{_datadir}/themes/%{theme_name}-accessibility/xfwm4/
%{_datadir}/themes/%{theme_name}-dark-accessibility/xfwm4/
%{_datadir}/themes/%{theme_name}-dark/xfwm4/
%{_datadir}/themes/%{theme_name}/xfwm4/
%{_datadir}/themes/%{theme_name}-compact/xfwm4/

%files xfce4-notifyd-theme
%doc LICENSE.GPL LICENSE.CC
%dir %{_datadir}/themes/Greybird/
%{_datadir}/themes/%{theme_name}-bright/xfce-notify-4.0/
%{_datadir}/themes/%{theme_name}/xfce-notify-4.0/

%files plank
%doc LICENSE.GPL LICENSE.CC
%{_datadir}/themes/%{theme_name}/plank/
%{_datadir}/themes/%{theme_name}-dark/plank/

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 23 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.22.12-1
- Update to 3.22.12

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> = 3.22.11-1
- Update to 3.22.11

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 09 2019 Kevin Fenzi <kevin@scrye.com> - 3.22.10-1
- Update to 3.22.10. Fixes bug #1674179

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 28 2018 Kevin Fenzi <kevin@scrye.com> - 3.22.9-2
- Apply patch with 3 small post release fixes. 

* Sat Dec 01 2018 Kevin Fenzi <kevin@scrye.com> - 3.22.9-1
- Update to 3.22.9.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 28 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.22.8-1
- Update to 3.22.8

* Wed Mar 21 2018 Kevin Fenzi <kevin@scrye.com> - 3.22.7-1
- Update to 3.22.7. Fixes bug #1559201

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb 04 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.22.6-1
- Update to 3.22.6

* Sun Sep 10 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.22.5-1
- Update to 3.22.5

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 16 2017 Kevin Fenzi <kevin@scrye.com> - 3.22.4-1
- Update to 3.22.4. Fixes bug #1462199

* Sat Apr 08 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.22.3-1
- Update to 3.22.3

* Sat Mar 11 2017 Kevin Fenzi <kevin@scrye.com> - 3.22.2-1
- Update to 3.22.2. Fixes bug #1431346

* Sat Feb 11 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.22.1-1
- Update to 3.22.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 15 2016 Kevin Fenzi <kevin@scrye.com> - 3.22.0-1
- Update to 3.22.0

* Tue Sep 13 2016 Kevin Fenzi <kevin@scrye.com> - 3.20.1-1
- Update to 3.20.1

* Thu Aug 18 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.20.0-2
- Fix files section

* Thu Aug 18 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 3.20.0-1
- Update to latest version
- gtk-3.20 support

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 08 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.6.2-1
- Update to 1.6.2

* Mon Jul 27 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.6-1
- Update to version 1.6
- Removed tooltip patch

* Sun Jun 21 2015 Kevin Fenzi <kevin@scrye.com> 1.5.3-4
- Add patch to fix tooltips in firefox dark themes. Fixes bug #1208888

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.5.3-2
- re-enabled GTK-3 lightdm greeter theme

* Wed Feb 18 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.5.3-1
- Update to 1.5.3

* Wed Feb 11 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.5.2-1
- Update to 1.5.2

* Sat Jan 17 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.5.1-1
- Update to 1.5.1

* Sat Jan 10 2015 Kevin Fenzi <kevin@scrye.com> 1.5-1
- Update to 1.5, drop upstreamed patches

* Thu Nov 06 2014 poma <poma@gmail.com> 1.4-3
- Upstream fix for checkboxes and radios in gtk3.14
- The "shadow" is re-enabled, the full size of the app menu in the system tray
  is resolved upstream - gtkmenu: fix unnecessary scroll buttons gtk-3-14
  https://git.gnome.org/browse/gtk+/commit/?h=gtk-3-14&id=695ff38
- The same applies to the Shimmer Project Desktop Suites for Xfce as a whole, 
  i.e. Greybird, Bluebird and Albatross.
- With these two corrections bugs #1114161, #1139190 and #1139187 
  are solved completely.

* Fri Oct 03 2014 Kevin Fenzi <kevin@scrye.com> 1.4-2
- Add patch to fix gtk3 issues. Thanks poma
- Fixes bug #1114161

* Sun Aug 03 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.4-1
- Updated to 1.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 30 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.3.4-1
- Update to upstream release 1.3.4

* Tue Mar 18 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.3.3-1
- Updated to 1.3.3

* Fri Mar 14 2014 Luis Bazan <lbazan@fedoraproject.org> - 1.3.2-1
- Update to 1.3.2

* Sun Feb 23 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.3.1-1
- Updated to 1.3.1
- Fixed the source URL to directly download from github

* Wed Sep 18 2013  Athmane Madjoudj <athmane@fedoraproject.org> 1.2.2-1
- Update to 1.2.2

* Thu Aug 08 2013  Athmane Madjoudj <athmane@fedoraproject.org> 1.2-1
- Update to 1.2
- Use sed to remove unity deps instead of a patch

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jan 24 2013 Athmane Madjoudj <athmane@fedoraproject.org> 1.0.8-1
- Update to 1.0.8

* Sun Nov 11 2012 Athmane Madjoudj <athmane@fedoraproject.org> 1.0.7-1
- Update to 1.0.7
- Cleanup the spec

* Wed Jul 25 2012 Athmane Madjoudj <athmane@fedoraproject.org> 0.9-1
- Update to the new release.
- Remove unico engine dep.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Athmane Madjoudj 0.8.2-4
- Remove unity import in gtk3 css.

* Tue May 22 2012 Athmane Madjoudj <athmane@fedoraproject.org> 0.8.2-3
- Fix version number since upstream tagged the last commit
- Add xfce4-notifyd-theme sub-package

* Mon May 21 2012 Athmane Madjoudj <athmane@fedoraproject.org> 0.8.1-2
- Spec cleanup
- Require gtk-unico-engine >= 1.0.2 to fix gtk3 theme

* Sun May 20 2012 Athmane Madjoudj <athmane@fedoraproject.org> 0.8.1-1
- Initial spec (based on Zukitwo theme)
