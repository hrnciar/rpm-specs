%define _legacy_common_support 1
Name:           xwota
Version:        0.4
Release:        31%{?dist}
Summary:        Who's On the Air Database interface

License:        GPL+
URL:            http://people.fabaris.it/iz0ete/xwota/
Source0:        http://people.fabaris.it/iz0ete/%{name}/%{name}-%{version}.tar.gz
Source1:        xwota.desktop
Source2:        xwota.png
Patch0:         xwota-0.4-overflow.patch
Patch1:         xwota-0.4-empty-fields.patch
Patch2:         xwota-c99.patch

BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  gtk2-devel
BuildRequires:  desktop-file-utils
#Requires:

%description
Xwota is intended for amateur radio operators who want to make use of the WOTA
database.

It can be used to find out who is on the air, the band and frequency they are
operating on, and their location by country, state, county, grid, and
latitude/longitude

It's very similar to a DX Cluster client, but it works with the WOTA database
and contains more informations.

If you don't known what is the WOTA database, please read some infos at
http://www.wotadb.org.

%prep
%setup -q
%patch0 -p1 -b .overflow
%patch1 -p1 -b .empty-fields
%patch2 -p1 -b .c99


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
# Don't include these twice
rm -rf $RPM_BUILD_ROOT%{_usr}/doc/
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/
cp %{SOURCE2} ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/%{name}.png
desktop-file-install \
        --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}



%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/*%{name}.desktop


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Apr 05 2020 Lucian Langa <lucilanga@gnome.eu.org> - 0.4-30
- add temporary gcc10 fix

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Florian Weimer <fweimer@redhat.com> - 0.4-28
- Fix building in C99 mode

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.4-12
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 14 2010 Lucian Langa <cooly@gnome.eu.org> - 0.4-10
- improve desktop file

* Thu Jan 14 2010 Lucian Langa <cooly@gnome.eu.org> - 0.4-9
- fix for bug (#555286)

* Mon Aug 03 2009 Lucian Langa <cooly@gnome.eu.org> - 0.4-8
- fix buffer overflow (#510918)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 07 2008 Lucian Langa <cooly@gnome.eu.org> - 0.4-5
- license fix
- desktop icon fix
- description fix

* Thu Aug 28 2008 Lucian Langa <cooly@gnome.eu.org> - 0.4-4
- added missing desktop/icon file

* Wed Aug 27 2008 Lucian Langa <cooly@gnome.eu.org> - 0.4-3
- preserve timestamps

* Tue Nov 20 2007 Robert 'Bob' Jensen <bob@bobjensen.com> 0.4-2
- Fix rpmlint errors
* Tue Nov 20 2007 Robert 'Bob' Jensen <bob@bobjensen.com> 0.4-1
- Initial SPEC

