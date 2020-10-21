Name:           nightview
Version:        0.3.3
Release:        35%{?dist}
Summary:        A general astronomical software package to control of a CCD camera

License:        GPLv2
URL:            http://www.physics.muni.cz/mb/nightview/
Source0:        ftp://integral.physics.muni.cz/pub/nightview/%{name}-%{version}.tar.gz
Source1:        xnightview.desktop
Source2:        xmove.desktop
Source3:        nighthttpd.service
Source4:        telescoped.service
Patch0:         nightview-0.3.2-fitslib.patch
Patch2:         nightview-0.3.1-doc.patch
Patch3:         nightview-0.3.3-curl.patch
Patch4:         nightview-0.3.3-unistd.patch
# Sent by e-mail to Filip Hroch <hroch@physics.muni.cz>
Patch5:         nightview-0.3.3-formatsec.patch
Patch6:         nightview-0.3.3-wxwidgets3.0.patch

BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  cfitsio-devel
BuildRequires:  wxGTK3-devel
BuildRequires:  curl-devel
BuildRequires:  ImageMagick
BuildRequires:  texlive-jadetex
BuildRequires:  /usr/bin/dvipdf
BuildRequires:  docbook-style-dsssl
BuildRequires:  docbook-dtd42-xml
BuildRequires:  transfig
BuildRequires:  desktop-file-utils
BuildRequires:  tex(ulem.sty), tex(mlnames.sty), texlive-stmaryrd
BuildRequires:  tex(latex)

Requires:       nightview-server = %{version}
Requires:       nightview-cli = %{version}
Requires:       nightview-gui = %{version}
Requires:       nightview-doc = %{version}

%description
Nightview is a general astronomical software package to control of a CCD
camera together with a telescope. It provides an intuitive graphical
interface for getting of individual exposures and a telescope possitioning.
An advanced command line interface is also offered to support of a scripting
and a long time serie imaging.

Nightview is designed as a fully network transparent providing maximum
flexibility of its usage. Moreover, all components are prepared with
possibility to be simply superseded by an user's equivalent for support of
individual improvements and possible requested extendings.


%package server
Summary:        Server-side tools from NightView suite

Requires(post): systemd
Requires(preun): systemd

%description server
Server tools from NightView suite.
See description of "nightview" package for more details.


%package cli
Summary:        Non-GUI tools from NightView suite

%description cli
Text based tools from NightView suite.
See description of "nightview" package for more details.


%package gui
Summary:        GUI tools from NightView suite

%description gui
Graphically oriented tools from NightView suite.
See description of "nightview" package for more details.


%package doc
Summary:        Documentation for NightView suite

%description doc
Documentation files for NightView suite in PDF, PostScript and HTML.
See description of "nightview" package for more details.


%prep
%setup -q
%patch0 -p1 -b .fitslib
%patch2 -p1 -b .doc
%patch3 -p1 -b .curl
%patch4 -p1 -b .unistd
%patch5 -p1 -b .formatsec
%patch6 -p1 -b .wx3

%build
# configure.in has a typo, patching it would need regeneration of configure
# Real fix is s/ac_cv_header_curl_h/ac_cv_header_curl_curl_h/
export ac_cv_header_curl_h=yes
# Unfortunately *sad panda* SBIG protocols are not open
%configure --without-sbigudrv --disable-static --with-curl
# configure overrides CFLAGS to a value that does not make much sense
make %{?_smp_mflags} CFLAGS="%{optflags}" CXXFLAGS="%{optflags}"

# Build documentation (not _smp_mflags safe)
# We'll let this fail without issue, its not ideal, but eh. texlive. :P
make -C doc || :
make -C doc -f Makefile.nightview all

# Create Icon Theme Specification compilant icons
convert xnightview/xnightview-icon.xpm xnightview.png
convert xmove/xmove-icon.xpm xmove.png


%install
make install DESTDIR=%{buildroot}

# Directory structure
install -d %{buildroot}%{_datadir}/pixmaps
install -d %{buildroot}%{_datadir}/applications
install -d %{buildroot}%{_docdir}/nightview-doc
install -d %{buildroot}%{_unitdir}

# Icons and menu entries
install -pm 0644 xnightview.png xmove.png \
        %{buildroot}%{_datadir}/pixmaps
desktop-file-install %{SOURCE1} \
        --dir=%{buildroot}%{_datadir}/applications
desktop-file-install %{SOURCE2} \
        --dir=%{buildroot}%{_datadir}/applications

# Services
install -pm 0644 %{SOURCE3} %{SOURCE4} %{buildroot}%{_unitdir}

# Documentation
make -f Makefile.nightview -C doc install DESTDIR=%{buildroot} || :


%post server
%systemd_post nighthttpd.service telescoped.service

%preun server
%systemd_preun nighthttpd.service telescoped.service

%postun server
%systemd_postun nighthttpd.service telescoped.service


%ldconfig_scriptlets cli


%files
%license COPYING
# Nothing external links against this so far, and this saves us
# from overhead of creating a useless devel package.
%exclude %{_libdir}/libccdnet.so
%exclude %{_libdir}/libccdnet.la
# This seems usless in a package
%exclude %{_sbindir}/nighthttpd_setup.sh
%exclude %{_sbindir}/telescoped_setup.sh
%exclude %{_bindir}/nightview-test
%exclude %{_mandir}/man1/nightview-test.1*


%files server
%license COPYING
%{_unitdir}/nighthttpd.service
%{_unitdir}/telescoped.service
%{_sbindir}/nighthttpd
%{_sbindir}/telescoped
%{_mandir}/man8/nighthttpd.8*
%{_mandir}/man8/telescoped.8*


%files cli
%license COPYING
%{_bindir}/night_batch
%{_bindir}/night_control
%{_bindir}/night_dark
%{_bindir}/night_darks
%{_bindir}/night_exposure
%{_bindir}/night_filter
%{_bindir}/night_flats
%{_bindir}/night_keylist
%{_bindir}/night_pointer
%{_bindir}/night_power
%{_bindir}/night_temperature
%{_bindir}/telescope
%{_libdir}/libccdnet.so.0
%{_libdir}/libccdnet.so.0.0.0
%{_mandir}/man1/night_batch.1*
%{_mandir}/man1/night_control.1*
%{_mandir}/man1/night_dark.1*
%{_mandir}/man1/night_darks.1*
%{_mandir}/man1/night_exposure.1*
%{_mandir}/man1/night_filter.1*
%{_mandir}/man1/night_flats.1*
%{_mandir}/man1/night_keylist.1*
%{_mandir}/man1/night_power.1*
%{_mandir}/man1/night_temperature.1*
%{_mandir}/man1/telescope.1*


%files gui
%license COPYING
%{_bindir}/xnightview
%{_bindir}/xmove
%{_mandir}/man1/xmove.1*
%{_mandir}/man1/xnightview.1*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*


%files doc
%license COPYING
%dir %{_docdir}/nightview-doc
%{_docdir}/nightview-doc/html
%{_docdir}/nightview-doc/nightview.pdf
%{_docdir}/nightview-doc/nightview.ps
# Do not include sources
%exclude %{_docdir}/nightview-doc/*.fig
%exclude %{_docdir}/nightview-doc/*.eps
%exclude %{_docdir}/nightview-doc/*.jpg
%exclude %{_docdir}/nightview-doc/*.png
%exclude %{_docdir}/nightview-doc/*.css
%exclude %{_docdir}/nightview-doc/*.xml


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 14 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.3-31
- Spec cleanups

* Mon Aug 15 2018 Scott Talbert <swt@techie.net> - 0.3.3-30
- Add patch for wxWidgets 3.0 support and rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 0.3.3-28
- rebuilt for cfitsio 3.450

* Fri Feb 23 2018 Christian Dersch <lupinix@mailbox.org> - 0.3.3-27
- rebuilt for cfitsio 3.420 (so version bump)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 21 2015 Lubomir Rintel <lkundrak@v3.sk> - 0.3.3-21
- Switch service management to systemd

* Fri Sep 18 2015 Richard Hughes <rhughes@redhat.com> - 0.3.3-20
- Remove no longer required AppData file

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.3-18
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.3.3-17
- Add an AppData file for the software center

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 15 2014 Lubomir Rintel <lkundrak@v3.sk> - 0.3.3-14
- Streamline BRs

* Fri Jan 10 2014 Orion Poplawski <orion@cora.nwra.com> - 0.3.3-13
- Rebuild for cfitsio 3.360

* Wed Dec 04 2013 Lubomir Rintel <lkundrak@v3.sk> - 0.3.3-12
- Fix build with -Werror=format-security

* Thu Oct 24 2013 Lubomir Rintel <lkundrak@v3.sk> - 0.3.3-11
- Bulk sad and useless attempt at consistent SPEC file formatting

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Jon Ciesla <limburgher@gmail.com> - 0.3.3-9
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 06 2012 Jon Ciesla <limburgher@gmail.com> - 0.3.3-6
- Fix FTBFS.

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-5
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 0.3.3-2
- rebuilt against wxGTK-2.8.11-2

* Mon Nov 09 2009 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 0.3.3-1
- Rebase on later release
- Upstream applied our gcc44 patch
- Do not own /usr/share/applications (Thomas Spura, #533347)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jul 12 2009 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.3.2-7
- Should not own /usr/share/pixmaps, as that directory is provided by the
  filesystem package.

* Tue Mar 24 2009 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 0.3.2-6
- Fix the categories

* Sun Mar 1 2009 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 0.3.2-5
- Update the gcc44 fix

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 22 2009 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 0.3.2-3
- Fix build with gcc44

* Thu Feb 05 2009 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 0.3.2-2
- Remove #478680 workaround

* Tue Jan 06 2009 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 0.3.2-1
- Bump to 0.3.2

* Mon Jan 05 2009 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 0.3.1-3
- Work around #478680

* Wed Nov 05 2008 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 0.3.1-2
- Fixes for problems found during review by Marek Mahut

* Sun Oct 26 2008 Lubomir Rintel (Fedora Astronomy) <lkundrak@v3.sk> - 0.3.1-1
- Initial packaging attempt
