Name:           cardpeek
Version:        0.8.4
Release:        17%{?dist}
Summary:        Tool to read the contents of smart cards

License:        GPLv3+
URL:            http://pannetrat.com/Cardpeek
Source0:        http://downloads.pannetrat.com/install/cardpeek-%{version}.tar.gz

# Backported from upstream
Patch0:         cardpeek-appdata-fixes.patch

BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  gtk3-devel
BuildRequires:  libcurl-devel
BuildRequires:  lua-devel
BuildRequires:  openssl-devel
BuildRequires:  pcsc-lite-devel
BuildRequires:  readline-devel

%description
Cardpeek is a tool to read the contents of ISO7816 smart cards. It
features a GTK GUI to represent card data is a tree view, and is
extendable with a scripting language (LUA).

The tool currently reads the contents of:
    * EMV cards
    * Calypso public transport cards (such as Navigo)
    * Moneo ePurse cards
    * Vitale 2 French health cards.


%prep
%autosetup -p1


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# remove docs from a wrong place
rm -rf $RPM_BUILD_ROOT%{_docdir}/cardpeek/

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/cardpeek.desktop


%files
%license COPYING
%doc AUTHORS ChangeLog README
%doc doc/cardpeek_ref*.pdf
%{_bindir}/cardpeek
%{_datadir}/appdata/cardpeek.appdata.xml
%{_datadir}/applications/cardpeek.desktop
%{_datadir}/icons/hicolor/*/apps/cardpeek-logo.png
%{_mandir}/man1/cardpeek.1*


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-17
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.4-13
- Rebuild for readline 8.0

* Thu Jan 31 2019 Kalev Lember <klember@redhat.com> - 0.8.4-12
- Fix wrong application name in the appdata file

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.4-8
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.8.4-4
- Rebuild for readline 7.x

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 20 2015 Kalev Lember <kalevlember@gmail.com> - 0.8.4-1
- Update to 0.8.4
- Update the URL
- Use license macro for the COPYING file

* Mon Aug 18 2014 Kalev Lember <kalevlember@gmail.com> - 0.8.3-1
- Update to 0.8.3
- New source URL

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 12 2013 Kalev Lember <kalevlember@gmail.com> - 0.8-1
- Update to 0.8
- Build with gtk3
- Drop the lua 5.2 patch

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 13 2013 Tom Callaway <spot@fedoraproject.org> - 0.7.2-2
- rebuild for lua 5.2

* Tue Apr 02 2013 Kalev Lember <kalevlember@gmail.com> - 0.7.2-1
- Update to 0.7.2

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 14 2012 Kalev Lember <kalevlember@gmail.com> - 0.7.1-1
- Update to 0.7.1
- Drop upstreamed patch

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 09 2011 Kalev Lember <kalevlember@gmail.com> - 0.7-2
- Rebuilt for libpng 1.5
- Patch to fix build with glib 2.31 single includes policy

* Mon Sep 05 2011 Kalev Lember <kalevlember@gmail.com> - 0.7-1
- Update to 0.7
- Clean up the spec file of cruft not needed with current rpmbuild

* Wed Apr 06 2011 Kalev Lember <kalev@smartlink.ee> - 0.6-1
- Update to 0.6
- Dropped upstreamed patches

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May 03 2010 Kalev Lember <kalev@smartlink.ee> - 0.5-2
- Set StartupNotify=true in desktop file
- Use INSTALL="install -p" to keep timestamps
- Updated description

* Mon Apr 26 2010 Kalev Lember <kalev@smartlink.ee> - 0.5-1
- Initial RPM release
