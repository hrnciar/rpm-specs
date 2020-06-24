Name:           gloobus-preview
Version:        0.4.1
Release:        39%{?dist}
Summary:        A Gnome extension to enable previews for any kind of file

License:        GPLv3
URL:            https://launchpad.net/gloobus-preview
Source0:        http://launchpad.net/gloobus/gloobus-0.4/%{version}/+download/%{name}-%{version}.tar.gz
Source1:        README.fedora.tar.gz

# This patch fixes problems with autotools not respecting install directories
# it also includes the rebuild of the autotools scripts required
Patch0:         gloobus-location-prereconf.patch
Patch1:         gloobus-page-render-to-pixbuf.patch


BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  gvfs-devel
BuildRequires:  gstreamer-plugins-base-devel
BuildRequires:  cairomm-devel
BuildRequires:  taglib-devel
BuildRequires:  poppler-glib-devel
BuildRequires:  libgnomeui-devel
BuildRequires:  unoconv
BuildRequires:  gtksourceview2-devel
BuildRequires:  clutter-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libtool
BuildRequires:  autoconf
Requires: GConf2

%description
Gloobus Preview allows instant access to a variety of file types without the 
need to open their default applications.

%prep
%setup -q
%setup -q -D -T -a 1
%patch0 -p1
%patch1 -p1
find . -name '*.cpp' -exec chmod -x {} \;
find . -name '*.h' -exec chmod -x {} \;
libtoolize
autoreconf -if

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_libdir}/gloobus
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop

%doc README AUTHORS COPYING THANKS README.fedora

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 0.4.1-38
- Rebuild for poppler-0.84.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.1-33
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4.1-27
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 16 2012 Marek Kasik <mkasik@redhat.com> - 0.4.1-21
- Rebuild (poppler-0.20.0)

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-20
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 28 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.4.1-18
- rebuild(poppler)

* Fri Sep 30 2011 Marek Kasik <mkasik@redhat.com> - 0.4.1-17
- Rebuild (poppler-0.18.0)

* Mon Sep 19 2011 Marek Kasik <mkasik@redhat.com> - 0.4.1-16
- Rebuild (poppler-0.17.3)

* Mon Aug  8 2011 Marek Kasik <mkasik@redhat.com> - 0.4.1-15
- Workaround missing function
- Resolves: #698159

* Sun Jul 17 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.4.1-14
- rebuild (poppler)

* Sun Mar 13 2011 Marek Kasik <mkasik@redhat.com> - 0.4.1-13
- Rebuild (poppler-0.16.3)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 02 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.4.1-11
- rebuild (poppler)

* Wed Dec 15 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.4.1-10
- rebuild (poppler)

* Sat Nov 06 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.4.1-9
- rebuilt (poppler)

* Wed Oct  6 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.4.1-8
- rebuild (poppler)

* Thu Aug 19 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.4.1-7
- rebuild (poppler)

* Tue Jun 22 2010 Matthias Clasen <mclasen@redhat.com> 0.4.1-6
- Rebuild against new poppler

* Mon Feb 8 2010 Patrick Dignan <dignan.patrick, at gmail.com> 0.4.1-5
- Added scriptlets for updating icon cache, and added libtool as a BR
* Mon Feb 8 2010 Patrick Dignan <dignan.patrick, at gmail.com> 0.4.1-4
- Fixed location of .desktop file
* Sun Feb 7 2010 Patrick Dignan <dignan.patrick, at gmail.com> 0.4.1-3
- Simplified removal of .la files, removed unnecessary flags
* Thu Jan 28 2010 Patrick Dignan <dignan.patrick at, gmail.com> 0.4.1-2
- Simplified chmod statement
* Fri Dec 18 2009 Patrick Dignan <dignan.patrick at, gmail.com> 0.4.1-1
- Initial package.
