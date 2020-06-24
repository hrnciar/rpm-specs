# FC-5+ version

Name:		xkeycaps
Summary: 	Graphical front end to xmodmap
Version:	2.46
Release:	27%{?dist}
License:	MIT
Source0:	http://www.jwz.org/xkeycaps/%{name}-%{version}.tar.Z
Source1:	xkeycaps.desktop
Source2:	xkeycaps.png
URL:		http://www.jwz.org/xkeycaps/
BuildRequires:  gcc
BuildRequires:	xorg-x11-xbitmaps, libICE-devel, libXmu-devel, libSM-devel
BuildRequires:	libXaw-devel, imake, libXt-devel, xorg-x11-proto-devel
BuildRequires:	desktop-file-utils, libXext-devel
Requires:	xorg-x11-server-utils

%description
xkeycaps is a graphical front-end to xmodmap. It opens a window that 
looks like a keyboard; moving the mouse over a key shows what KeySyms 
and Modifier bits that key generates. Clicking on a key simulates 
KeyPress/KeyRelease events on the window of your choice. It is possible 
to change the KeySyms and Modifiers generated by a key through a 
mouse-based interface. This program can also write an input file for 
xmodmap to recreate your changes in future sessions.

%prep
%setup -q 

%build
xmkmf
sed -i -e 's/^\(\s*CFLAGS\s*=.*\)/\1 $(RPM_OPT_FLAGS)/' Makefile
make %{_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install INSTALL="install -p"
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m0644 -p xkeycaps.man $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -m0644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps
desktop-file-install                             \
        --dir ${RPM_BUILD_ROOT}%{_datadir}/applications         \
        %{SOURCE1}

%files
%doc README sgi-microsoft.txt
%{_bindir}/xkeycaps
%{_datadir}/applications/xkeycaps.desktop
%{_datadir}/pixmaps/xkeycaps.png
%{_mandir}/man1/*

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.46-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.46-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.46-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.46-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 2.46-23
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.46-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.46-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.46-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.46-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.46-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.46-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.46-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.46-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.46-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 2.46-13
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.46-12.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.46-11.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.46-10.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.46-9.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.46-8.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.46-7.3
- Autorebuild for GCC 4.3

* Mon Aug 27 2007 Tom "spot" Callaway <tcallawa@redhat.com> 2.46-6.2
- rebuild for BuildID

* Mon Aug  6 2007 Tom "spot" Callaway <tcallawa@redhat.com> 2.46-6.1
- license cleanup

* Tue Apr 10 2007 Tom "spot" Callaway <tcallawa@redhat.com> 2.46-6
- fix bugzilla 227229

* Mon Sep 11 2006 Tom "spot" Callaway <tcallawa@redhat.com> 2.46-5
- license isn't BSD-ish, its BSD
- bump for FC-6

* Tue Feb 28 2006 Tom "spot" Callaway <tcallawa@redhat.com> 2.46-4
- bump for FC-5

* Mon Jan 16 2006 Tom "spot" Callaway <tcallawa@redhat.com> 2.46-3
- fix FC-3/FC-4

* Mon Jan 16 2006 Tom "spot" Callaway <tcallawa@redhat.com> 2.46-2
- add missing BR
- fix missing desktop file

* Thu Dec 15 2005 Tom "spot" Callaway <tcallawa@redhat.com> 2.46-1
- Initial package for Fedora Extras
