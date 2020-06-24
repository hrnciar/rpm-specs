Name:           clearlooks-compact-gnome-theme
Version:        1.5
Release:        19%{?dist}
Summary:        GNOME Desktop theme optimized for small displays

License:        LGPLv2+
URL:            http://martin.ankerl.com/2007/11/04/clearlooks-compact-gnome-theme/
Source0:        http://martin.ankerl.com/files/ClearlooksCompact-%{version}.tar.bz2
BuildArch:      noarch

Requires:       gtk2-engines
# Just for convenience
Provides:       clearlooks-compact = %{version}-%{release}

%description
Compact version of Clearlooks theme, especially great on small screens like
the Eee PC, or for intense applications like Eclipse.


%prep
%setup -q -c
# Backup file, apparently forgotten there by upstream
rm Clearlooks\ Compact/gtk-2.0/gtkrc~


%build


%install
install -d $RPM_BUILD_ROOT%{_datadir}/themes
cp -ap Clearlooks\ Compact $RPM_BUILD_ROOT%{_datadir}/themes/
rm -f $RPM_BUILD_ROOT%{_datadir}/themes/Clearlooks\ Compact/COPYING


%files
%{_datadir}/themes/*
# This only works with rpm >= 4.11
%doc "Clearlooks Compact/COPYING"


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 11 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.5-10
- Reflect rpm's behavioral changes on paths with whitespaces
  (FTBFS, RHBZ #1106055)
- Modernize spec.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 13 2009 Lubomir Rintel <lkundrak@v3.sk> - 1.5-2
- Require gtk-engines

* Sat Apr 11 2009 Lubomir Rintel <lkundrak@v3.sk> - 1.5-1
- New upstream version

* Sun Apr 05 2009 Lubomir Rintel <lkundrak@v3.sk> - 1.4-1
- Versioning change (no epoch bump since noone uses this now anyways :)
- Upstream included our theme.index, drop it
- Upstream clarified the license

* Thu Apr 02 2009 Lubomir Rintel <lkundrak@v3.sk> - 20080411-1
- Initial package creation
