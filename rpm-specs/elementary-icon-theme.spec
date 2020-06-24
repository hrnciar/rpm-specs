%global srcname icons

Name:           elementary-icon-theme
Summary:        Icons from the Elementary Project
Version:        5.3.1
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/%{srcname}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  librsvg2-tools
BuildRequires:  meson
BuildRequires:  xorg-x11-apps

%description
This is an icon theme designed to be smooth, sexy, clear, and efficient.


%package        gimp-palette
Summary:        Icons from the Elementary Project (GIMP palette)
Requires:       %{name} = %{version}-%{release}
Requires:       gimp

%description    gimp-palette
This is an icon theme designed to be smooth, sexy, clear, and efficient.

This package contains a palette file for the GIMP.


%package        inkscape-palette
Summary:        Icons from the Elementary Project (inkscape palette)
Requires:       %{name} = %{version}-%{release}
Requires:       inkscape

%description    inkscape-palette
This is an icon theme designed to be smooth, sexy, clear, and efficient.

This package contains a palette file for inkscape.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
# Clean up executable permissions
for i in $(find -type f -executable); do
    chmod a-x $i;
done

%meson -Dvolume_icons=false
%meson_build


%install
%meson_install

# Create icon cache file
touch %{buildroot}/%{_datadir}/icons/elementary/icon-theme.cache


%check
# ignore validation until appstream-glib knows the "icon-theme" component type
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/io.elementary.icons.appdata.xml || :


%transfiletriggerin -- %{_datadir}/icons/elementary
gtk-update-icon-cache --force %{_datadir}/icons/elementary &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/elementary
gtk-update-icon-cache --force %{_datadir}/icons/elementary &>/dev/null || :


%files
%doc README.md
%license COPYING

%dir %{_datadir}/icons/elementary
%ghost %{_datadir}/icons/elementary/icon-theme.cache

%{_datadir}/icons/elementary/*/
%{_datadir}/icons/elementary/*@2x
%{_datadir}/icons/elementary/*@3x

%{_datadir}/icons/elementary/cursor.theme
%{_datadir}/icons/elementary/index.theme

%{_datadir}/metainfo/io.elementary.icons.appdata.xml

%files gimp-palette
%{_datadir}/gimp/2.0/palettes/elementary.gpl

%files inkscape-palette
%{_datadir}/inkscape/palettes/elementary.gpl


%changelog
* Tue May 12 2020 Fabio Valentini <decathorpe@gmail.com> - 5.3.1-1
- Update to version 5.3.1.

* Sun May 03 2020 Fabio Valentini <decathorpe@gmail.com> - 5.3.0-1
- Update to version 5.3.0.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 5.1.0-2
- Fix minor build issues.

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 5.1.0-1
- Update to version 5.1.0.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.4-1
- Update to version 5.0.4.

* Wed Feb 13 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.3-1
- Update to version 5.0.3.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Fabio Valentini <decathorpe@gmail.com> - 5.0.2-1
- Update to version 5.0.2.

* Fri Dec 07 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0.1-1
- Update to version 5.0.1.

* Thu Oct 18 2018 Fabio Valentini <decathorpe@gmail.com> - 5.0-1
- Update to version 5.0.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Fabio Valentini <decathorpe@gmail.com> - 4.3.1-2
- Add file triggers to replace scriptlets.

* Wed Oct 25 2017 Fabio Valentini <decathorpe@gmail.com> - 4.3.1-1
- Update to version 4.3.1.

* Thu Oct 05 2017 Fabio Valentini <decathorpe@gmail.com> - 4.3.0-1
- Update to version 4.3.0.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Fabio Valentini <decathorpe@gmail.com> - 4.2.0-1
- Update to version 4.2.0.

* Sat May 20 2017 Fabio Valentini <decathorpe@gmail.com> - 4.1.0-1
- Update to version 4.1.0.

* Mon Mar 20 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.3-1
- Update to version 4.0.3.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.2-2
- Correctly create icon cache.

* Thu Jan 19 2017 Fabio Valentini <decathorpe@gmail.com> - 4.0.2-1
- Update to version 4.0.2.
- Clean up spec file.

* Wed Dec 14 2016 Christopher Meng <rpm@cicku.me> - 4.0.1.1-1
- Update to 4.0.1.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 30 2013 Christopher Meng <rpm@cicku.me> - 3.1-1
- Update to 3.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 07 2013 Christopher Meng <rpm@cicku.me> - 3.0-1
- Update to 3.0(BZ#973917)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Apr 06 2011 Johannes Lips <johannes.lips@googlemail.com> - 2.7.1-1
- update to 2.7.1
- updated the source url

* Sun Mar 13 2011 Johannes Lips <johannes.lips@googlemail.com> - 2.5-1
- update to 2.5

* Wed Aug 18 2010 Tajidin Abd <tajidinabd@archlinux.us> - 2.4-6
- removed wildcards in created directory

* Tue Aug 17 2010 Tajidin Abd <tajidinabd@archlinux.us> - 2.4-5
- corrected to reflect timestamps
- corrected license
- made changes to documentation

* Tue Aug 10 2010 Tajidin Abd <tajidinabd@archlinux.us> - 2.4-4
- cleaned up files macro

* Mon Aug 09 2010 Tajidin Abd <tajidinabd@archlinux.us> - 2.4-3
- made corrections to prep macro
- version number is referenced from URL:

* Sun Aug 08 2010 Tajidin Abd <tajidinabd@archlinux.us> - 2.4-2
- Added Scriplets
- corrected tarname macro usage

* Fri Aug 06 2010 Tajidin Abd <tajidinabd@archlinux.us> - 2.4-1
- Intial rpm build Fedora

