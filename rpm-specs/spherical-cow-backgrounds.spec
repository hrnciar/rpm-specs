Name:           spherical-cow-backgrounds
Version:        18.0.0
Release:        14%{?dist}
Summary:        Spherical Cow desktop backgrounds

License:        CC-BY-SA
URL:            https://fedoraproject.org/wiki/F18_Artwork
Source0:        https://fedorahosted.org/released/design-team/%{name}-%{version}.tar.xz

BuildArch:      noarch

# for %%_kde4_* macros
BuildRequires:  kde-filesystem
Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}


%description
This package contains desktop backgrounds for the Spherical Cow theme.
Pulls in both Gnome and KDE themes.

%package        single
Summary:        Single screen images for Spherical Cow Backgrounds
License:        CC-BY-SA

%description    single
This package contains single screen images for Spherical Cow
Backgrounds.

%package        kde
Summary:        Spherical Cow Wallpapers for KDE

Requires:       %{name}-single = %{version}-%{release}
Requires:       kde-filesystem

%description    kde
This package contains KDE desktop wallpapers for the Spherical Cow
theme.

%package        gnome
Summary:        Spherical Cow Wallpapers for Gnome

Requires:       %{name}-single = %{version}-%{release}

%description    gnome
This package contains Gnome desktop wallpapers for the Spherical Cow
theme.

%package        xfce
Summary:        Spherical Cow Wallpapers for XFCE4

Requires:       %{name}-single = %{version}-%{release}
Requires:       xfdesktop

%description    xfce
This package contains XFCE4 desktop wallpapers for the Spherical Cow
theme.

%package        extras-single
Summary:        Single screen images for Spherical Cow Extras Backrounds
License:        CC-BY and CC-BY-SA

%description    extras-single
This package contains single screen images for Spherical Cow supplemental
wallpapers.

%package        extras-gnome
Summary:        Extra Spherical Cow Wallpapers for Gnome

Requires:       %{name}-extras-single

%description    extras-gnome
This package contains Spherical Cow supplemental wallpapers for Gnome

%package        extras-kde
Summary:        Extra Spherical Cow Wallpapers for KDE

Requires:       %{name}-extras-single

%description    extras-kde
This package contains Spherical Cow supplemental wallpapers for Gnome

%package        extras-xfce
Summary:        Extra Spherical Cow Wallpapers for XFCE

Requires:       %{name}-extras-single

%description    extras-xfce
This package contains Spherical Cow supplemental wallpapers for XFCE


%prep
%setup -q


%build
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc

%files single
%doc CC-BY-SA?3.0 Attribution
%dir %{_datadir}/backgrounds/spherical-cow
%dir %{_datadir}/backgrounds/spherical-cow/default
%{_datadir}/backgrounds/spherical-cow/default/normalish
%{_datadir}/backgrounds/spherical-cow/default/standard
%{_datadir}/backgrounds/spherical-cow/default/wide

%files kde
%{_kde4_datadir}/wallpapers/Spherical_Cow/

%files gnome
%{_datadir}/backgrounds/spherical-cow/default/spherical-cow.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-spherical-cow.xml

%files xfce
%{_datadir}/xfce4/backdrops/spherical-cow.png

%files extras-single
%doc CC-BY-SA?3.0 CC-BY-SA?2.0 CC-BY?2.0 Attribution-Extras
%{_datadir}/backgrounds/spherical-cow/extras/*.jpg

%files extras-gnome
%{_datadir}/backgrounds/spherical-cow/extras/spherical-cow-extras.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-spherical-cow-extras.xml

%files extras-kde
%{_kde4_datadir}/wallpapers/Spherical_Cow_*/

%files extras-xfce
%{_datadir}/xfce4/backdrops/*.jpg

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 18.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 18.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 18.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 18.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 21 2013 Martin Sourada - 18.0.0-2
- Fix a mistake in %%changelog

* Thu Feb 21 2013 Martin Sourada - 18.0.0-1
- New release
- Improved resolution for some extras images
- Fix build on F19

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 17.92.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 25 2012 Martin Sourada <mso@fedoraproject.org> - 17.92.0-1
- Add extras

* Tue Aug 14 2012 Martin Sourada <mso@fedoraproject.org> - 17.91.0-2
- Spec cleanup WRT changes to guideline since we first released
  backgrounds package...

* Sun Aug 12 2012 Martin Sourada <mso@fedoraproject.org> - 17.91.0-1
- Updated design

* Sat Aug 11 2012 Martin Sourada <mso@fedoraproject.org> - 17.90.2-1
- Another iteration

* Fri Aug 10 2012 Martin Sourada <mso@fedoraproject.org> - 17.90.1-1
- First release
