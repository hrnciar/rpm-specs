Name:       lemonpos  
Version:    0.9.4  
Release:    22%{dist}  
Summary:    Point Of Sale Application For KDE4  
 
License:    GPLv2  
URL:        http://www.lemonpos.org/ 
Source0:    http://downloads.sourceforge.net/project/lemonpos/citronic/%{name}-%{version}-rc7.tar.bz2
Patch1:     locale.patch

BuildRequires: desktop-file-utils
BuildRequires: kdelibs4-devel
BuildRequires: qt-devel
BuildRequires: gettext
BuildRequires: oxygen-icon-theme
BuildRequires: hicolor-icon-theme

Requires: dbus-x11
Requires: qt 
Requires: qt-x11 
Requires: qt-mysql

%description  
Lemon is an open source POS (point of sale) for Linux, and other Unix.   
It is a general POS, not targeted to a specific business.  
  
It has been developed for ease of use and customization, and to support  
bar-code scanners and ticket printers. At this point, it has been tested  
with a parallel port ticket printer (Star Micronics, SP500).  
  
More information on:
http://www.lemonpos.org/  
http://sourceforge.net/apps/mediawiki/lemonpos/index.php?title=Main_Page

Authors:  
--------  
     Miguel Chávez Gamboa 
  
%prep  
%setup -q -n %{name}  
%patch1 -p1 -b .locale

%build  
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd
make %{?_smp_mflags} -C %{_target_platform}

%install  
rm -rf %{buildroot}
make install/fast -C %{_target_platform} DESTDIR=%{buildroot} 

%check
desktop-file-validate  %{buildroot}%{_kde4_datadir}/applications/kde4/lemon.desktop
desktop-file-validate  %{buildroot}%{_kde4_datadir}/applications/kde4/squeeze.desktop

%find_lang lemon
%find_lang squeeze
cat lemon.lang squeeze.lang > %{name}.lang

%ldconfig_scriptlets

%files -f %{name}.lang
%doc COPYING database_resources README NOTES USING
%{_kde4_bindir}/lemon  
%{_kde4_bindir}/squeeze  
%{_kde4_datadir}/applications/kde4/*.desktop  
%{_kde4_datadir}/icons/hicolor/*/*/*.png  
%{_kde4_datadir}/config.kcfg/*.kcfg 
%{_kde4_datadir}/config/lemonrc
%{_kde4_datadir}/kde4/apps/lemon  
%{_kde4_datadir}/kde4/apps/squeeze  
 
%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.4-12
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Nov 23 2013 siddharth <siddharth.kde@gmail.com> - 0.9.4-9
- rebuilt, adding dbus-x11 as Requires bz#922547

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 17 2013 siddharth <siddharths@fedoraproject.org> - 0.9.4-7
- Fix for bz#839081 bz#839090

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 15 2012 Siddharth Sharma <siddharth.kde@gmail.com> - 0.9.4-4
- Requires My SQL removed, not needed Bug 839082
- Added Extra info wiki link
- Added README and other Doc Files

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild


*Sun Oct 30 2011 siddharth sharma <siddharths@fedoraproject.org> - 0.9.4-2
 - Fixing source Url
 - Fixing BuildRequires

*Sat Oct 29 2011 siddharth sharma <siddharths@fedoraproject.org> - 0.9.4-1
 - Bump up release version
 - Fixing up spec for packaging
 - Fixing locale as upstream had bad locale setup ,cz to cs and redundancy with zh locale files

*Sat Jan 8 2011 siddharth Sharma <siddharths@fedoraproject.org> - 0.9.3-1
 - Initial Release 1
