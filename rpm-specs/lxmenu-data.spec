# Review:       https://bugzilla.redhat.com/487973

Name:           lxmenu-data
Version:        0.1.5
Release:        8%{?dist}
Summary:        Data files for the LXDE menu

License:        LGPLv2+
URL:            http://lxde.org
Source0:        http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
Source1:        lxmenu-data-0.1-COPYING
Patch0:         lxmenu-data-0.1.1-menu.patch

BuildRequires:  gcc
BuildRequires:  intltool >= 0.40.0
Requires:       redhat-menus
BuildArch:      noarch

%description
The lxmenu-data contains files used to build the menu in LXDE according to 
the freedesktop-org menu spec. Currently it's used by LXPanel and LXLauncher.


%prep
%setup -q
%patch0 -p1 -b .orig
# install correct license
rm -f COPYING
cp %{SOURCE1} COPYING


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT



%files
#FIXME: add changelog when there is one
%doc AUTHORS README TODO
%license COPYING
%config(noreplace) %{_sysconfdir}/xdg/menus/lxde-applications.menu
%{_datadir}/desktop-directories/lxde-*.directory


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Mar  1 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.5-1
- 0.1.5

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.4-1
- 0.1.4

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 06 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.1-3
- Move Accessibility to Utilities

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 06 2009 Christoph Wickert <cwickert@fedoraproject.org> 0.1.1-1
- Update to 0.1.1

* Sun Mar 22 2009 Christoph Wickert <cwickert@fedoraproject.org> 0.1-2
- Change menu structure to vendor default
- Fix license

* Fri Dec 12 2008 Christoph Wickert <cwickert@fedoraproject.org> 0.1-1
- Initial Fedora package
