Name:		laughlin-kde-theme
Version:	14.0.1
Release:	11%{?dist}
Summary:	Laughlin KDE Theme

License:	GPLv2+ and CC-BY-SA

# We are upstream for this package
URL:		https://fedorahosted.org/fedora-kde-artwork/
Source0:	https://fedorahosted.org/releases/f/e/fedora-kde-artwork/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	kde-filesystem
Requires:	kde-filesystem
Requires:	system-logos
Requires:	laughlin-backgrounds-kde >= 14.0.0

Provides:	laughlin-kdm-theme = %{version}-%{release}
Provides:	laughlin-ksplash-theme = %{version}-%{release}
Provides:       laughlin-plasma-desktoptheme = %{version}-%{release}

%if 0%{?fedora} == 14
Provides:       system-kde-theme = %{version}-%{release}
Provides:       system-kdm-theme = %{version}-%{release}
Provides:       system-ksplash-theme = %{version}-%{release}
Provides:       system-plasma-desktoptheme = %{version}-%{release}
%endif

%description
This is Laughlin KDE Theme Artwork containing
KDM theme, KSplash theme, Plasma desktop, and Plasma netbook theme.


%prep
%setup -q


%build
# blank

%install
rm -rf %{buildroot}

### Plasma desktoptheme's
mkdir -p %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Laughlin/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Laughlin-netbook/ %{buildroot}%{_kde4_appsdir}/desktoptheme/

### KDM
mkdir -p %{buildroot}%{_kde4_appsdir}/kdm/themes/
cp -rp kdm/Laughlin/ %{buildroot}%{_kde4_appsdir}/kdm/themes/
pushd %{buildroot}%{_kde4_appsdir}/kdm/themes/Laughlin/
ln -s ../../../../../backgrounds/laughlin/default/standard/laughlin.png laughlin-640x480.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/laughlin/default/wide/laughlin.png laughlin-800x480.png
ln -s ../../../../../backgrounds/laughlin/default/standard/laughlin.png laughlin-800x600.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/laughlin/default/wide/laughlin.png laughlin-1024x600.png
ln -s ../../../../../backgrounds/laughlin/default/standard/laughlin.png laughlin-1024x768.png
ln -s ../../../../../backgrounds/laughlin/default/wide/laughlin.png laughlin-1152x720.png
ln -s ../../../../../backgrounds/laughlin/default/standard/laughlin.png laughlin-1152x864.png
ln -s ../../../../../backgrounds/laughlin/default/standard/laughlin.png laughlin-1200x900.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/laughlin/default/wide/laughlin.png laughlin-1280x720.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/laughlin/default/wide/laughlin.png laughlin-1280x768.png
ln -s ../../../../../backgrounds/laughlin/default/wide/laughlin.png laughlin-1280x800.png
ln -s ../../../../../backgrounds/laughlin/default/standard/laughlin.png laughlin-1280x960.png
ln -s ../../../../../backgrounds/laughlin/default/normalish/laughlin.png laughlin-1280x1024.png

# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/laughlin/default/wide/laughlin.png laughlin-1366x768.png
ln -s ../../../../../backgrounds/laughlin/default/wide/laughlin.png laughlin-1440x900.png
ln -s ../../../../../backgrounds/laughlin/default/standard/laughlin.png laughlin-1440x1080.png
ln -s ../../../../../backgrounds/laughlin/default/standard/laughlin.png laughlin-1600x1200.png
ln -s ../../../../../backgrounds/laughlin/default/normalish/laughlin.png laughlin-1600x1280.png
ln -s ../../../../../backgrounds/laughlin/default/wide/laughlin.png laughlin-1680x1050.png
# That one's not really 8:5, but it's the closest...
ln -s ../../../../../backgrounds/laughlin/default/wide/laughlin.png laughlin-1920x1080.png
ln -s ../../../../../backgrounds/laughlin/default/wide/laughlin.png laughlin-1920x1200.png
ln -s ../../../../../backgrounds/laughlin/default/standard/laughlin.png laughlin-1920x1440.png
ln -s ../../../../../backgrounds/laughlin/default/standard/laughlin.png laughlin-2048x1536.png
# KDM falls back to this one if there's no match
ln -s ../../../../../backgrounds/laughlin/default/standard/laughlin.png laughlin.png
# system logo
ln -s ../../../../../pixmaps/system-logo-white.png system-logo-white.png
popd

## KSplash
mkdir -p %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
cp -rp ksplash/Laughlin/ %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
ln -s ../../../../../../backgrounds/laughlin/default/standard/laughlin.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Laughlin/2048x1536/
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Laughlin/1920x1200/
ln -s ../../../../../../backgrounds/laughlin/default/wide/laughlin.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Laughlin/1920x1200/laughlin.png
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Laughlin/1280x1024/
ln -s ../../../../../../backgrounds/laughlin/default/normalish/laughlin.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Laughlin/1280x1024/
 
# system logo 
ln -s ../../../../../../pixmaps/system-logo-white.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Laughlin/2048x1536/logo.png



%files
%doc README COPYING.CC-BY-SA COPYING.GPLv2
%{_kde4_appsdir}/desktoptheme/Laughlin/
%{_kde4_appsdir}/desktoptheme/Laughlin-netbook/
%{_kde4_appsdir}/kdm/themes/Laughlin/
%{_kde4_appsdir}/ksplash/Themes/Laughlin/

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 14.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 14.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 14.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 14.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 14.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 14.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 14.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 14.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 12 2013 Martin Briza <mbriza@redhat.com> 14.0.1-1
- Moved and extended the area for the caps lock warning

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Mar 12 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 14.0.0-3
- drop Provides: system-* on F15+

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 14 2010 Rex Dieter <rdieter@fedoraproject.org> 14.0.0-1
- include Laughlin,Laughlin-netbook plasma desktoptheme

* Thu Sep 30 2010 Rex Dieter <rdieter@fedoraproject.org> 13.92.0-2
- fix errant symlinks

* Thu Sep 30 2010 Rex Dieter <rdieter@fedoraproject.org> 13.92.0-1
- avoid ksplashx crasher, adjust size dirs to match reality (#632814)
- add 1280x1024 symlink to normalish/laughlin.png

* Mon Aug 02 2010 Jaroslav Reznik <jreznik@redhat.com> 13.91.0-1
- initial package
