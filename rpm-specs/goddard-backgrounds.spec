Name:           goddard-backgrounds
Version:        13.0.0
Release:        17%{?dist}
Summary:        Goddard desktop backgrounds

License:        CC-BY-SA
URL:            https://fedoraproject.org/wiki/F12_Artwork
Source0:        https://fedorahosted.org/released/design-team/%{name}-%{version}.tar.lzma

BuildArch:      noarch

# for %%_kde4_* macros
BuildRequires:  kde-filesystem
Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}


%description
This package contains desktop backgrounds for the Goddard theme. Pulls in both
Gnome and KDE themes.

%package        single
Summary:        Single screen images for Goddard Backgrounds

%description    single
This package contains Single screen images for Goddard Backgrounds

%package        kde 
Summary:        Goddard Wallpapers for KDE 
%if 0%{?fedora} == 13
Provides:       system-backgrounds-kde
%endif

Requires:       %{name}-single = %{version}-%{release} 
Requires:       kde-filesystem

%description    kde 
This package contains KDE desktop wallpapers for the Goddard theme.

%package        gnome 
Summary:        Goddard Wallpapers for Gnome 

Requires:       %{name}-single = %{version}-%{release} 
%if 0%{?fedora} == 13
# FIXME: Which provides I should use?
Provides:        system-backgrounds
#Provides:        system-backgrounds-gnome
%endif

%description    gnome 
This package contains Gnome desktop wallpapers for the Goddard theme.


%prep
%setup -q


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc

%files single
%doc COPYING Credits
#There'll be also dual wallpapers in dual subpackage in the future, hence the 
# %%dir ownership is separated
%dir %{_datadir}/backgrounds/goddard
%dir %{_datadir}/backgrounds/goddard/default
%{_datadir}/backgrounds/goddard/default/normalish
%{_datadir}/backgrounds/goddard/default/standard
%{_datadir}/backgrounds/goddard/default/wide

%files kde
%{_kde4_datadir}/wallpapers/Goddard/

%files gnome
%{_datadir}/backgrounds/goddard/default/goddard.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-goddard.xml


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 30 2010 Martin Sourada <mso@fedoraproject.org> - 13.0.0-2
- Provide system-backgrounds* only on F13

* Fri Apr 16 2010 Martin Sourada <mso@fedoraproject.org> - 13.0.0-1
- Update to final version

* Thu Feb 18 2010 Martin Sourada <mso@fedoraproject.org> - 12.91.0-2
- system-backgrounds* provides should be for >= f13 (till f14 theme starts 
  existing)

* Wed Feb 17 2010 Martin Sourada <mso@fedoraproject.org> - 12.91.0-1
- Initial backgrounds package for F13 Goddard

