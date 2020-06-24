%global icon_theme Monochrome

Name:           monochrome-icon-theme
Version:        0.0.49
Release:        13%{?dist}
Summary:        Icons for the panel, designed in a simplified monochrome style

License:        CC-BY-SA
URL:            https://launchpad.net/ubuntu-mono
Source0:        %{name}-%{version}.tar.xz
# Ubuntu Mono icon theme contains copyrighted Ubuntu logo icons. Therefore we
# use this script to delete these files and remove any reference to the Ubuntu
# trademark before shipping it. Download the upstream tarball and invoke this
# script while in the tarball's directory
Source1:        %{name}-generate-tarball.sh

Requires:       humanity-icon-theme
BuildArch:      noarch

%description
Dark and Light panel icons to make your desktop beautiful.


%prep
%setup -q


%build


%install
install -dm 0755 $RPM_BUILD_ROOT%{_datadir}/icons/
cp -a LoginIcons/ $RPM_BUILD_ROOT%{_datadir}/icons/
cp -a %{icon_theme}-dark/ $RPM_BUILD_ROOT%{_datadir}/icons/
cp -a %{icon_theme}-light/ $RPM_BUILD_ROOT%{_datadir}/icons/

# SVG desktop icons reference the Ubuntu default wallpaper, not available in
# Fedora and too heavy to be rendered inside a SVG file. Use the PNG icons
# instead, as done in the Ubuntu package
rm $RPM_BUILD_ROOT%{_datadir}/icons/%{icon_theme}-*/places/*/*desktop.svg
cp -r debian/places/* $RPM_BUILD_ROOT%{_datadir}/icons/%{icon_theme}-dark/places/
cp -r debian/places/* $RPM_BUILD_ROOT%{_datadir}/icons/%{icon_theme}-light/places/
for d in $RPM_BUILD_ROOT%{_datadir}/icons/%{icon_theme}-*/places/*/; do
  pushd $d
  ln -s user-desktop.png desktop.png
  popd
done


%post
for i in LoginIcons %{icon_theme}-dark %{icon_theme}-light; do
  /bin/touch --no-create %{_datadir}/icons/$i/ &>/dev/null || :
done


%postun
if [ $1 -eq 0 ]; then
  for i in LoginIcons %{icon_theme}-dark %{icon_theme}-light; do
    /bin/touch --no-create %{_datadir}/icons/$i/ &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/$i/ &>/dev/null || :
  done
fi


%posttrans
for i in LoginIcons %{icon_theme}-dark %{icon_theme}-light; do
  /usr/bin/gtk-update-icon-cache %{_datadir}/icons/$i/ &>/dev/null || :
done


%files
%doc debian/{changelog,copyright}
%{_datadir}/icons/LoginIcons/
%{_datadir}/icons/%{icon_theme}-dark/
%{_datadir}/icons/%{icon_theme}-light/


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.49-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.49-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.49-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.49-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.49-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.49-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.49-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.49-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.49-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.49-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 24 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.0.49-2
- Update to 0.0.49

* Fri Sep 21 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.0.45-1
- Update to 0.0.45

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 16 2012 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.0.39-1
- Update to 0.0.39

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 19 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.0.38-1
- Update to 0.0.38

* Mon Oct 17 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.0.37-4
- Fix description

* Wed Oct 12 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.0.37-3
- Rename the package to monochrome-icon-theme (mono-icon-theme already exists in
  the repositories)
- Remove remaining Ubuntu trademarks and proprietary icons

* Tue Oct 11 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.0.37-2
- Rename the package to mono-icon-theme
- Remove dependency on fedora-logos

* Sun Oct 09 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.0.37-1
- Initial RPM release
