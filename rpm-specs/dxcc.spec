Name:           dxcc
Version:        20080225
Release:        37%{?dist}
Summary:        Small utility which determines the ARRL DXCC entity of a ham radio callsign

License:        GPLv2+
URL:            http://fkurz.net/ham/dxcc.html
Source0:        http://fkurz.net/ham/dxcc/%{name}-%{version}.tar.gz
#add .desktop file
Source1:        %{name}.desktop
#temporary Icon
Source2:        %{name}.png
#fix install path
Patch0:         dxcc-20071205-makefile.patch
#separate core and gui
Patch1:         dxcc-20071205-gui.patch

BuildArch:      noarch

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
dxcc is a small utility which determines the ARRL DXCC entity of a ham radio
callsign, based on the cty.dat country file by Jim Reisert, AD1C. 

Optional GUI with a world map showing the DXCC's location available.

%package gui
Summary:       Optional GUI with a world map showing the DXCC's location
BuildRequires: desktop-file-utils
BuildRequires: perl-generators
Requires:      %{name} = %{version}-%{release}
Requires:      perl(Tk)

%description gui
dxcc-gui is a small utility which determines the ARRL DXCC entity of a amateur 
radio callsign, based on the cty.dat country file by Jim Reisert, AD1C. 

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
make %{?_smp_mflags}

%install
%make_install

# no upstream .desktop or icon yet
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/
cp %{SOURCE2} ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/%{name}.png
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}

%files
%doc ChangeLog COPYING README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/%{name}

%files gui
%doc COPYING
%{_bindir}/%{name}-gui
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/*%{name}.desktop

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 20080225-37
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20080225-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20080225-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 20080225-34
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20080225-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20080225-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 20080225-31
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20080225-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20080225-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 20080225-28
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20080225-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 20080225-26
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20080225-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080225-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 20080225-23
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 20080225-22
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080225-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080225-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 20080225-19
- Perl 5.18 rebuild

* Sun Feb 24 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 20080225-18
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines
- fix desktop file to follow specification

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080225-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080225-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 20080225-15
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080225-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 20080225-13
- Perl mass rebuild

* Fri Jun 10 2011 Marcela Mašláňová <mmaslano@redhat.com> - 20080225-12
- Perl 5.14 mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080225-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 2 2011 Randall 'Randy' Berry <dp67@fedoraproject.org> - 20080225-10
- Rebuild for broken deps

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 20080225-9
- Mass rebuild with perl-5.12.0

* Sun Apr 18 2010 Randall 'Randy' Berry <dp67@fedoraproject.org> - 20080225-8
- Change .desktop file categories per bug 530829
- correct file atributes per rpmlint
- spelling in spec intentional (per rpmlint wanrings)

* Fri Dec 4 2009 Stepan Kasal <kasal@redhat.com> - 20080225-7
- build against perl 5.10.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080225-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080225-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 26 2008 Robert 'Bob' Jensen - 20080225-4
- Rawhide rebuild

* Tue Feb 26 2008 Robert 'Bob' Jensen - 20080225-3
- Submit for review

* Tue Feb 26 2008 Robert 'Bob' Jensen - 20080225-2
- Add .desktop and icon for -gui package

* Tue Feb 26 2008 Robert 'Bob' Jensen - 20080225-1
- Version Update
- Verify patches still needed

* Mon Jan 07 2008 Robert 'Bob' Jensen - 20071210-1
- Version Update

* Mon Dec 10 2007 Sindre Pedersen Bjørdal - 20071205-1
- Initial build
