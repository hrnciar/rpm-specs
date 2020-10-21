%global backgrounds_kde_version 14.91.1

Name:		lovelock-kde-theme
Version:	14.92.1
Release:	14%{?dist}
Summary:	Lovelock KDE Theme

License:	GPLv2+ and CC-BY-SA

# We are upstream for this package
URL:		https://fedorahosted.org/fedora-kde-artwork/
Source0:	https://fedorahosted.org/releases/f/e/fedora-kde-artwork/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	kde-filesystem
Requires:	kde-filesystem
Requires:	system-logos
Requires:	lovelock-backgrounds-kde >= %{backgrounds_kde_version}

Provides:	lovelock-kdm-theme = %{version}-%{release}
Provides:	lovelock-ksplash-theme = %{version}-%{release}
Provides:	lovelock-plasma-desktoptheme = %{version}-%{release}

%if 0%{?fedora} == 15
Provides:	system-kde-theme = %{version}-%{release}
Provides:	system-kdm-theme = %{version}-%{release}
Provides:	system-ksplash-theme = %{version}-%{release}
Provides:	system-plasma-desktoptheme = %{version}-%{release}
%endif

%description
This is Lovelock KDE Theme Artwork containing KDM theme,
KSplash theme and Plasma Workspaces theme.


%prep
%setup -q


%build
# blank

%install
rm -rf %{buildroot}

### Plasma desktoptheme's
mkdir -p %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Lovelock/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Lovelock-netbook/ %{buildroot}%{_kde4_appsdir}/desktoptheme/

### KDM
mkdir -p %{buildroot}%{_kde4_appsdir}/kdm/themes/
cp -rp kdm/Lovelock/ %{buildroot}%{_kde4_appsdir}/kdm/themes/
pushd %{buildroot}%{_kde4_appsdir}/kdm/themes/Lovelock/
# system logo
ln -s ../../../../../pixmaps/system-logo-white.png system-logo-white.png
popd

## KSplash
mkdir -p %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
cp -rp ksplash/Lovelock/ %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
ln -s ../../../../../../backgrounds/lovelock/default/standard/lovelock.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Lovelock/2048x1536/
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Lovelock/1920x1200/
ln -s ../../../../../../backgrounds/lovelock/default/wide/lovelock.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Lovelock/1920x1200/lovelock.png
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Lovelock/1280x1024/
ln -s ../../../../../../backgrounds/lovelock/default/normalish/lovelock.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Lovelock/1280x1024/
 
# system logo 
ln -s ../../../../../../pixmaps/system-logo-white.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Lovelock/2048x1536/logo.png



%files
%doc README COPYING.CC-BY-SA COPYING.GPLv2
%{_kde4_appsdir}/desktoptheme/Lovelock/
%{_kde4_appsdir}/desktoptheme/Lovelock-netbook/
%{_kde4_appsdir}/kdm/themes/Lovelock/
%{_kde4_appsdir}/ksplash/Themes/Lovelock/

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 14.92.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 14.92.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 14.92.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 14.92.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 14.92.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 14.92.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 14.92.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 14.92.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 14.92.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.92.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.92.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 19 2013 Martin Briza <mbriza@redhat.com> 14.92.1-3
- Fixed the dependency on lovelock-backgrounds-kde

* Mon Aug 12 2013 Martin Briza <mbriza@redhat.com> 14.92.1-2
- Fixed the version

* Mon Aug 12 2013 Martin Briza <mbriza@redhat.com> 14.92.1-1
- Moved and extended the area for the caps lock warning

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.91.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.91.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.91.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.91.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 02 2011 Jaroslav Reznik <jreznik@redhat.com> 14.91.0-2
- provides only f15 system default theming

* Mon Mar 28 2011 Jaroslav Reznik <jreznik@redhat.com> 14.91.0-1
- update to 14.91.0-1
- use "wallpaper" instead of symlinked kdm backgrounds

* Thu Feb 10 2011 Jaroslav Reznik <jreznik@redhat.com> 14.90.1-1
- initial package
