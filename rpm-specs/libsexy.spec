Name:           libsexy
Version:        0.1.11
Release:        35%{?dist}
Summary:        Funky fresh graphical widgets for GTK+ 2

License:        LGPLv2+
URL:            http://www.chipx86.com/w/index.php/Libsexy
Source0:        http://releases.chipx86.com/%{name}/%{name}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-url-label.patch
Patch1:		%{name}-icon-name.patch
Patch2:         gtk2-single-include.patch

BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:	libxml2-devel
BuildRequires:	iso-codes-devel
Requires:	enchant


%description
Some funky fresh graphical widgets for GTK+ 2 applications.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:	pkgconfig
Requires:	gtk2-devel
Requires:	libxml2-devel


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1 -b .url-label
%patch1 -p1 -b .icon-name
%patch2 -p1 -b .gtk-single-include


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Copy the files from the tarball to avoid the IDs generated by gtk-doc being
# different on different builds
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/%{name}/
cp -a docs/reference/html/* $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/%{name}/



%ldconfig_scriptlets


%files
%doc COPYING AUTHORS NEWS
%{_libdir}/%{name}.so.*


%files devel
%{_datadir}/gtk-doc/html/%{name}
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 09 2011 Iain Arnell <iarnell@gmail.com> 0.1.11-18
- Rebuild to remove bogus libpng12 dep

* Fri Mar 25 2011 Dan Williams <dcbw@redhat.com> - 0.1.11-17
- Update for recent GTK+ 2.x

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec  5 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.1.11-15
- Update url.

* Sun Nov 15 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.1.11-14
- Backport patch that allows SexyIconEntry to support images using icon-name.

* Sun Nov 15 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.1.11-13
- Drop requires on hunspell-en dictionary. (#517804)

* Tue Aug 11 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.1.11-12
- Use bzipped upstream tarball.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep 21 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.1.11-9
- Backport fix for clipboard & color support in sexy-url-label.

* Fri May 16 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.1.11-8
- Add requires for libxml2-devel to devel. (#446842)

* Wed Apr  2 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.1.11-7
- Don't generate the gtk-doc docs, and use the ones in the tarball
  to avoid having different files in different builds, fixes
  multilib problems (#342361)

* Tue Mar 25 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.1.11-6
- Switch back require to enchant. (#437797)

* Mon Mar 24 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.1.11-5
- Update require from enchant to enchant-aspell.

* Fri Feb  8 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.1.11-4
- Rebuild for gcc-4.3.

* Tue Aug 21 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.11-3
- Rebuild.

* Sun Aug  5 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.11-2
- Update license tag.

* Sat Mar 31 2007 Brian Pepple <bpepple@fedoraproject.org> - 0.1.11-1
- Update to 0.1.11 (bugfix release).

* Thu Nov 23 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.1.10-2
- Update URL (#217073).

* Tue Sep  5 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.1.10-1
- Update to 0.1.10.

* Sat Sep  2 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.1.9-1
- Update to 0.1.9.
- Package COPYING, AUTHORS, and NEWS files.
- Add BR on iso-codes-devel.

* Mon Aug 28 2006 Brian Pepple <bpepple@fedoraproject.org> - 0.1.8-2
- Rebuild for FC6.

* Sat Mar 18 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.1.8-1
- Upstream update

* Thu Mar 16 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.1.7-1
- Upstream update

* Mon Feb 13 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.1.6-2
- Rebuild for Fedora Extras 5

* Sun Feb  5 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.1.6-1
- Upstream update

* Wed Nov  9 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.1.4-1
- Upstream update
- Build with enchant (#172577)

* Mon Oct 17 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.1.3-1
- Upstream update

* Thu Oct 13 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.1.1-1
- Initial RPM release
