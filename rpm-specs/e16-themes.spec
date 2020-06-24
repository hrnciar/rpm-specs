Summary:   Themes for Enlightenment, DR16
Name:      e16-themes
Version:   1.0.1
Release:   15%{?dist}
License:   MIT with advertising
URL:       http://www.enlightenment.org/
#
# Use create-clean-tarball.sh script to create the cleaned tarball
# from the original tarball:
#   http://downloads.sourceforge.net/enlightenment/e16-themes-%{version}.tar.gz
#
Source0:   e16-themes-cleaned-%{version}.tar.gz
Source1:   create-clean-tarball.sh
BuildArch: noarch
Requires:  e16 >= 1.0.0

%description
The BlueSteel, BrushedMetal-Tigert, Ganymede and ShinyMetal themes
for Enlightenment, DR16.  

This is part of the Enlightenment distribution.

%prep
%setup -q

%build
%configure --enable-fsstd
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot} INSTALL="%{__install} -p"
%{__rm} -rfv %{buildroot}%{_datadir}/e16/themes/ShinyMetal/epplets/images/.xvpics
%{__chmod} 0755 %{buildroot}%{_datadir}/e16/themes/Ganymede/ACTIVATE_BUTTONS
# symlink all font configs to default theme
for theme in BlueSteel BrushedMetal-Tigert Ganymede ShinyMetal ; do
    %{__rm} -f %{buildroot}%{_datadir}/e16/themes/$theme/fonts.theme.cfg
    %{__ln_s} ../winter/fonts.theme.cfg \
       %{buildroot}%{_datadir}/e16/themes/$theme/fonts.theme.cfg
done
# Remove refs to removed fonts
%{__sed} -i -r -e 's/face=(aircut3,ganymede|rothwell|vixar|zirkle)/face=Vera/g' \
    %{buildroot}%{_datadir}/e16/themes/*/ABOUT/MAIN

%files
%doc AUTHORS COPYING
%{_datadir}/e16/themes

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 18 2011 Terje Rosten <terje.rosten@ntnu.no> - 1.0.1-1
- 1.0.1
- Remove fonts (bz #477378)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 07 2009 Terje Rosten <terjeros@phys.ntnu.no> - 1.0.0-1
- 1.0.0

* Fri Jul 31 2009 Terje Rosten <terjeros@phys.ntnu.no> - 0.16.8.0.2-5
- Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.8.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Terje Rosten <terjeros@phys.ntnu.no> - 0.16.8.0.2-3
- Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.8.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Mar 27 2008 Terje Rosten <terjeros@phys.ntnu.no> - 0.16.8.0.2-1
- 0.16.8.0.2
- Fix license

* Mon Aug 20 2007 Terje Rosten <terjeros@phys.ntnu.no> - 0.16.8.0.1-1
- Initial build (based on upstream spec, thanks! :-)
