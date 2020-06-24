%global theme_name Clearlooks-Phenix

Name: clearlooks-phenix
Version: 7.0.1
Release: 8%{?dist}
Summary: %{theme_name} theme
BuildArch: noarch

License: GPLv3+
URL: https://github.com/jpfleury/clearlooks-phenix
Source0: https://github.com/jpfleury/clearlooks-phenix/archive/%{version}.tar.gz#/clearlooks-phenix-theme-%{version}.tar.xz
Patch0: fix-nautilus-bg-image.patch

%description
%{theme_name} is a GTK+ 3 port of Clearlooks, the default theme
for GNOME 2. Style is also included for GTK2, Unity and for Metacity,
Openbox and Xfwm4 window managers.

%package common
Summary: Files common to %{theme_name} themes

%description common
Files which are common to all %{theme_name} themes.


%package gtk2-theme
Summary: %{theme_name} GTK+2 themes
Requires: %{name}-common = %{version}-%{release}, gtk2-engines

%description gtk2-theme
Themes for GTK+2 as part of the %{theme_name} theme.


%package gtk3-theme
Summary: %{theme_name} GTK+3 themes
Requires: %{name}-common = %{version}-%{release}, gtk3

%description gtk3-theme
Themes for GTK+3 as part of the %{theme_name} theme.


%package xfwm4-theme
Summary: %{theme_name} Xfwm4 themes
Requires: %{name}-common = %{version}-%{release}, xfwm4

%description xfwm4-theme
Themes for Xfwm4 as part of the %{theme_name} theme.


%package metacity-theme
Summary: %{theme_name} Metacity themes
Requires: %{name}-common = %{version}-%{release}, metacity

%description metacity-theme
Themes for Metacity as part of the %{theme_name} theme.


%package openbox-theme
Summary: %{theme_name} Openbox themes
Requires: %{name}-common = %{version}-%{release}, openbox

%description openbox-theme
Themes for Openbox as part of the %{theme_name} theme.


%prep
%setup -q
%patch0 -p1

%build

%install
mkdir -p %{buildroot}%{_datadir}/themes/%{theme_name}/
for dir in gtk-2.0 gtk-3.0 metacity-1 openbox-3 wallpapers xfwm4; do
  cp -R $dir %{buildroot}%{_datadir}/themes/%{theme_name}/
done
install -Dpm 0644 index.theme %{buildroot}%{_datadir}/themes/%{theme_name}/

%files common
%doc COPYING README.md doc/*.png
%{_datadir}/themes/%{theme_name}

%files gtk2-theme
%{_datadir}/themes/%{theme_name}/gtk-2.0/

%files gtk3-theme
%{_datadir}/themes/%{theme_name}/gtk-3.0/

%files xfwm4-theme
%{_datadir}/themes/%{theme_name}/xfwm4/

%files metacity-theme
%{_datadir}/themes/%{theme_name}/metacity-1/

%files openbox-theme
%{_datadir}/themes/%{theme_name}/openbox-3/


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 25 2016 Lubomir Rintel <lkundrak@v3.sk> - 7.0.1-1
- Version bump

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 25 2015 Richard Marko <rmarko@fedoraproject.org> - 6.0.3-3
- Fix Firefox tooltip transparency

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec 12 2014 Richard Marko <rmarko@fedoraproject.org> - 6.0.3-1
- Version bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jan 26 2013 Richard Marko <rmarko@fedoraproject.org> - 3.0.15-1
- Version bump
- Splitting to multiple subpackages

* Sat Jan 26 2013 Richard Marko <rmarko@fedoraproject.org> - 3.0.14-1
- Initial packaging
