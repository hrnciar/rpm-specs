Name:		alsamixergui
Summary:	GUI mixer for ALSA sound devices
Version:	0.9.0
Release:	0.30.rc2%{?dist}
License:	GPLv2+
# This is where the source used to live, but this upstream is dead.
# Source0:	ftp://www.iua.upf.es/pub/mdeboer/projects/alsamixergui/%%{name}-%%{version}rc1-2.tar.gz
# This tarball was taken from Debian, and is the most recent version as far as I know.
Source0:	http://ftp.de.debian.org/debian/pool/main/a/alsamixergui/alsamixergui_0.9.0rc2-1.orig.tar.gz
Source1:	alsamixergui.desktop
Source2:	alsamixergui.png
# This site is dead and gone.
URL:		ftp://www.iua.upf.es/pub/mdeboer/projects/alsamixergui
BuildRequires:  gcc-c++
BuildRequires:	fltk-devel, libstdc++-devel
BuildRequires:	alsa-lib-devel, desktop-file-utils
BuildRequires:	libtool
# This is debian's patch, taken 2013-04-01
Patch0:		alsamixergui_0.9.0rc2-1-9.1.diff

%description
alsamixergui is a FLTK based frontend for alsamixer. It is written
directly on top of the alsamixer source, leaving the original source
intact, only adding a couple of ifdefs, and some calls to the gui
part, so it provides exactly the same functionality, but with a
graphical userinterface.

%prep
%setup -q -n %{name}-%{version}rc2-1.orig
%patch0 -p1 -b .debian
autoreconf -i
chmod +x configure

%build
%configure
make %{?_smp_mflags}

%install
%make_install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -m0644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}

%files
%doc README AUTHORS COPYING ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-0.30.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-0.29.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-0.28.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-0.27.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-0.26.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-0.25.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-0.24.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-0.23.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-0.22.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-0.21.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.0-0.20.rc2
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 0.9.0-0.19.rc2
- rebuild (fltk)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-0.18.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-0.17.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-0.16.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr  1 2013 Tom Callaway <spot@fedoraproject.org> - 0.9.0-0.15.rc2
- update debian patch (fixes possible FTBFS)

* Sat Feb 09 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.9.0-0.14.rc2
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-0.13.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-0.12.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat May 28 2011 Tom Callaway <spot@fedoraproject.org> - 0.9.0-0.11.rc2
- rebuild against new fltk

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-0.10.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 17 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9.0-0.9.rc2
- fix buildrequires

* Mon Aug 17 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9.0-0.8.rc2
- fix debian patch to apply (i swear, it applied just a second ago)

* Mon Aug 17 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9.0-0.7.rc2
- update to rc2, last known update

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-0.6.rc1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-0.5.rc1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.0-0.4.rc1.2
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.0-0.3.rc1.2
- rebuild for BuildID

* Sun Sep 10 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.0-0.3.rc1
- bump for fc6

* Mon Jan 16 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.0-0.2.rc1
- add desktop entry

* Mon Jan 16 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.0-0.1.rc1
- Initial package for Fedora Extras
