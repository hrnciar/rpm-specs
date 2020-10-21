Name:		tango-icon-theme-extras
Version:	0.1.0
Release:	21%{?dist}
Summary:	Extra Icons from the Tango Project

License:	CC-BY-SA
URL:		http://tango.freedesktop.org/Tango_Desktop_Project

Source0:	http://tango.freedesktop.org/releases/%{name}-%{version}.tar.gz

# https://bugs.freedesktop.org/show_bug.cgi?id=45803
Patch0:         tango-icon-theme-extras-0.1.0-rsvg-convert.patch
Patch1:         tango-icon-theme-extras-0.1.0-rsvg-convert-configure.patch

BuildArch:	noarch

BuildRequires:	icon-naming-utils >= 0.7.2
BuildRequires:	ImageMagick-devel >= 5.5.7
BuildRequires:  librsvg2-devel >= 2.35.2
BuildRequires:  librsvg2-tools
BuildRequires:	pkgconfig >= 0.19

Requires:	tango-icon-theme

## Much of this is from the included README file...
%description
Contains extra icons for from the Tango Project. Currently this includes Tango
icons for iPod Digital Audio Player (DAP) devices and the Dell Pocket DJ DAP.


%prep
%setup -q 
%patch0 -p1
%patch1 -p1


%build
%configure --enable-png-creation
make


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}



%post
touch --no-create %{_datadir}/icons/Tango 2> /dev/null ||:
gtk-update-icon-cache -q %{_datadir}/icons/Tango 2> /dev/null ||:


%postun
touch --no-create %{_datadir}/icons/Tango 2> /dev/null ||:
gtk-update-icon-cache -q %{_datadir}/icons/Tango 2> /dev/null ||:


%files
%{_datadir}/icons/Tango/*
%doc AUTHORS ChangeLog COPYING README 


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 24 2013 Peter Oliver <rpm@mavit.org.uk> - 0.1.0-9
- Build with rsvg-convert.  Fixes #992775.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.1.0-2
- fix license tag

* Sat Jan 13 2007 Peter Gordon <peter@thecodergeek.com> - 0.1.0-1
- Initial packaging for Fedora Extras, based heavily on the tango-icon-theme
  spec already in Extras (created by Piotr Drąg).
