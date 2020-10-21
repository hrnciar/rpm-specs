# we build CUPS also with relro
%global _hardened_build 1

Summary: OpenPrinting CUPS filters and backends
Name:    cups-filters
Version: 1.28.2
Release: 2%{?dist}

# For a breakdown of the licensing, see COPYING file
# GPLv2:   filters: commandto*, imagetoraster, pdftops, rasterto*,
#                   imagetopdf, pstopdf, texttopdf
#         backends: parallel, serial
# GPLv2+:  filters: gstopxl, textonly, texttops, imagetops, foomatic-rip
# GPLv3:   filters: bannertopdf
# GPLv3+:  filters: urftopdf, rastertopdf
# LGPLv2+:   utils: cups-browsed
# MIT:     filters: gstoraster, pdftoijs, pdftoopvp, pdftopdf, pdftoraster
License: GPLv2 and GPLv2+ and GPLv3 and GPLv3+ and LGPLv2+ and MIT and BSD with advertising

Url:     http://www.linuxfoundation.org/collaborate/workgroups/openprinting/cups-filters
Source0: http://www.openprinting.org/download/cups-filters/cups-filters-%{version}.tar.xz

Patch01: cups-filters-init-buf.patch

Requires: cups-filters-libs%{?_isa} = %{version}-%{release}

# gcc and gcc-c++ is not in buildroot by default

# gcc for backends (implicitclass, parallel, serial, backend error handling)
# cupsfilters (colord, color manager...), filter (banners, 
# commandto*, braille, foomatic-rip, imagetoraster, imagetopdf, gstoraster e.g.),
# fontembed, cups-browsed
BuildRequires: gcc
# gcc-c++ for pdftoopvp, pdftopdf
BuildRequires: gcc-c++
# for autosetup
BuildRequires: git

BuildRequires: cups-devel
BuildRequires: pkgconf-pkg-config
# pdftopdf
BuildRequires: pkgconfig(libqpdf)
# pdftops
BuildRequires: poppler-utils
# pdftoijs, pdftoopvp, pdftoraster, gstoraster
BuildRequires: pkgconfig(poppler)
BuildRequires: poppler-cpp-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libtiff-devel
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: ghostscript
# libijs
BuildRequires: pkgconfig(ijs)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(lcms2)
# cups-browsed
BuildRequires: avahi-devel
BuildRequires: pkgconfig(avahi-glib)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: systemd

# Make sure we get postscriptdriver tags.
BuildRequires: python3-cups

# Testing font for test scripts.
BuildRequires: dejavu-sans-fonts

# autogen.sh
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gettext-devel
BuildRequires: libtool

# needed for systemd rpm macros in scriptlets
BuildRequires: systemd-rpm-macros

Requires: cups-filesystem
# if --with-pdftops is set to hybrid, we use poppler filters for several printers
# and for printing banners, for other printers we need gs - ghostscript
Requires: poppler-utils
# several filters calls 'gs' binary during filtering
Requires: ghostscript

# for getting ICC profiles for filters (dbus must run)
Requires: colord

# texttopdf
Requires: liberation-mono-fonts

# pstopdf
Requires: bc grep sed which

# cups-browsed
# cups-browsed needs to have cups.service to run
Requires: cups
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

# cups-browsed needs nss-mdns for resolving .local addresses of remote print queues
# or device during discovery for newer (2012+) devices - make it recommended together
# with avahi - needed for device discovery as well
Recommends: nss-mdns
# avahi is needed for device discovery
Recommends: avahi

# ipptool is used in driverless backend, not needed classic PPD based print queue
Recommends: cups-ipptool

%package libs
Summary: OpenPrinting CUPS filters and backends - cupsfilters and fontembed libraries
# LGPLv2: libcupsfilters
# MIT:    libfontembed
License: LGPLv2 and MIT

%package devel
Summary: OpenPrinting CUPS filters and backends - development environment
License: LGPLv2 and MIT
Requires: cups-filters-libs%{?_isa} = %{version}-%{release}

%description
Contains backends, filters, and other software that was
once part of the core CUPS distribution but is no longer maintained by
Apple Inc. In addition it contains additional filters developed
independently of Apple, especially filters for the PDF-centric printing
workflow introduced by OpenPrinting.

%description libs
This package provides cupsfilters and fontembed libraries.

%description devel
This is the development package for OpenPrinting CUPS filters and backends.

%prep
%autosetup -S git

%build
# work-around Rpath
./autogen.sh

# --with-pdftops=hybrid - use Poppler's pdftops instead of Ghostscript for
#                         Brother, Minolta, and Konica Minolta to work around
#                         bugs in the printer's PS interpreters
# --with-rcdir=no - don't install SysV init script
# --enable-driverless - enable PPD generator for driverless printing in 
#                       /usr/lib/cups/driver, it is for manual setup of 
#                       driverless printers with printer setup tool
# --disable-static - do not build static libraries (becuase of Fedora Packaging
#                    Guidelines)
# --enable-dbus - enable DBus Connection Manager's code
# --disable-silent-rules - verbose build output
# --disable-mutool - mupdf is retired in Fedora, use qpdf
# --enable-pclm - support for pclm language
# --with-remote-cups-local-queue-naming=RemoteName - name created local queues, which point to
#                                                    remote CUPS queue, by its name from the server

%configure --disable-static \
           --disable-silent-rules \
           --with-pdftops=hybrid \
           --enable-dbus \
           --with-rcdir=no \
           --disable-mutool \
           --enable-driverless \
           --enable-pclm \
           --with-remote-cups-local-queue-naming=RemoteName

%make_build

%install
%make_install

# Don't ship libtool la files.
rm -f %{buildroot}%{_libdir}/lib*.la

# Not sure what is this good for.
rm -f %{buildroot}%{_bindir}/ttfread

rm -f %{buildroot}%{_pkgdocdir}/INSTALL
mkdir -p %{buildroot}%{_pkgdocdir}/fontembed/
cp -p fontembed/README %{buildroot}%{_pkgdocdir}/fontembed/

# systemd unit file
mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 utils/cups-browsed.service %{buildroot}%{_unitdir}

# LSB3.2 requires /usr/bin/foomatic-rip,
# create it temporarily as a relative symlink
ln -sf %{_cups_serverbin}/filter/foomatic-rip %{buildroot}%{_bindir}/foomatic-rip

# Don't ship urftopdf for now (bug #1002947).
rm -f %{buildroot}%{_cups_serverbin}/filter/urftopdf
sed -i '/urftopdf/d' %{buildroot}%{_datadir}/cups/mime/cupsfilters.convs

# Don't ship pdftoopvp for now (bug #1027557).
rm -f %{buildroot}%{_cups_serverbin}/filter/pdftoopvp
rm -f %{buildroot}%{_sysconfdir}/fonts/conf.d/99pdftoopvp.conf


%check
make check

%post
%systemd_post cups-browsed.service

# put UpdateCUPSQueuesMaxPerCall and PauseBetweenCUPSQueueUpdates into cups-browsed.conf
# for making cups-browsed work more stable for environments with many print queues
# remove this after 1-2 releases
for directive in "UpdateCUPSQueuesMaxPerCall" "PauseBetweenCUPSQueueUpdates"
do
    found=`%{_bindir}/grep "^[[:blank:]]*$directive" %{_sysconfdir}/cups/cups-browsed.conf`
    if [ -z "$found" ]
    then
        if [ "x$directive" == "xUpdateCUPSQueuesMaxPerCall" ]
        then
            %{_bindir}/echo "UpdateCUPSQueuesMaxPerCall 20" >> %{_sysconfdir}/cups/cups-browsed.conf
        else
            %{_bindir}/echo "PauseBetweenCUPSQueueUpdates 5" >> %{_sysconfdir}/cups/cups-browsed.conf
        fi
    fi
done

%preun
%systemd_preun cups-browsed.service

%postun
%systemd_postun_with_restart cups-browsed.service 

%ldconfig_scriptlets libs


%files
%{_pkgdocdir}/README
%{_pkgdocdir}/ABOUT-NLS
%{_pkgdocdir}/AUTHORS
%{_pkgdocdir}/NEWS
%config(noreplace) %{_sysconfdir}/cups/cups-browsed.conf
%{_cups_serverbin}/filter/cgmtopdf
%{_cups_serverbin}/filter/cmxtopdf
%{_cups_serverbin}/filter/emftopdf
%{_cups_serverbin}/filter/imagetoubrl
%{_cups_serverbin}/filter/svgtopdf
%{_cups_serverbin}/filter/textbrftoindexv4
%{_cups_serverbin}/filter/vectortoubrl
%{_cups_serverbin}/filter/wmftopdf
%{_cups_serverbin}/filter/xfigtopdf
%attr(0755,root,root) %{_cups_serverbin}/filter/bannertopdf
%attr(0755,root,root) %{_cups_serverbin}/filter/brftoembosser
%attr(0755,root,root) %{_cups_serverbin}/filter/brftopagedbrf
%attr(0755,root,root) %{_cups_serverbin}/filter/commandtoescpx
%attr(0755,root,root) %{_cups_serverbin}/filter/commandtopclx
%attr(0755,root,root) %{_cups_serverbin}/filter/foomatic-rip
%attr(0755,root,root) %{_cups_serverbin}/filter/gstopdf
%attr(0755,root,root) %{_cups_serverbin}/filter/gstopxl
%attr(0755,root,root) %{_cups_serverbin}/filter/gstoraster
%attr(0755,root,root) %{_cups_serverbin}/filter/imagetobrf
%attr(0755,root,root) %{_cups_serverbin}/filter/imagetopdf
%attr(0755,root,root) %{_cups_serverbin}/filter/imagetops
%attr(0755,root,root) %{_cups_serverbin}/filter/imagetoraster
%attr(0755,root,root) %{_cups_serverbin}/filter/imageubrltoindexv3
%attr(0755,root,root) %{_cups_serverbin}/filter/imageubrltoindexv4
%attr(0755,root,root) %{_cups_serverbin}/filter/musicxmltobrf
%attr(0755,root,root) %{_cups_serverbin}/filter/pdftopdf
%attr(0755,root,root) %{_cups_serverbin}/filter/pdftops
%attr(0755,root,root) %{_cups_serverbin}/filter/pdftoraster
%attr(0755,root,root) %{_cups_serverbin}/filter/rastertoescpx
%attr(0755,root,root) %{_cups_serverbin}/filter/rastertopclm
%attr(0755,root,root) %{_cups_serverbin}/filter/rastertopclx
%attr(0755,root,root) %{_cups_serverbin}/filter/rastertopdf
%attr(0755,root,root) %{_cups_serverbin}/filter/rastertops
%attr(0755,root,root) %{_cups_serverbin}/filter/sys5ippprinter
%attr(0755,root,root) %{_cups_serverbin}/filter/textbrftoindexv3
%attr(0755,root,root) %{_cups_serverbin}/filter/texttobrf
%attr(0755,root,root) %{_cups_serverbin}/filter/texttopdf
%attr(0755,root,root) %{_cups_serverbin}/filter/texttops
%attr(0755,root,root) %{_cups_serverbin}/filter/texttotext
%attr(0755,root,root) %{_cups_serverbin}/filter/vectortobrf
%attr(0755,root,root) %{_cups_serverbin}/filter/vectortopdf
# all backends needs to be run only as root because of kerberos
%attr(0700,root,root) %{_cups_serverbin}/backend/parallel
# Serial backend needs to run as root (bug #212577#c4).
%attr(0700,root,root) %{_cups_serverbin}/backend/serial
# implicitclass backend must be run as root
%attr(0700,root,root) %{_cups_serverbin}/backend/implicitclass
%attr(0700,root,root) %{_cups_serverbin}/backend/beh
# cups-brf needs to be run as root, otherwise it leaves error messages
# in journal
%attr(0700,root,root) %{_cups_serverbin}/backend/cups-brf
%{_bindir}/foomatic-rip
%{_bindir}/driverless
%{_bindir}/driverless-fax
%{_cups_serverbin}/backend/driverless
%{_cups_serverbin}/backend/driverless-fax
%{_cups_serverbin}/driver/driverless
%{_cups_serverbin}/driver/driverless-fax
%{_datadir}/cups/banners
%{_datadir}/cups/braille
%{_datadir}/cups/charsets
%{_datadir}/cups/data/*
# this needs to be in the main package because of cupsfilters.drv
%{_datadir}/cups/ppdc/pcl.h
%{_datadir}/cups/ppdc/braille.defs
%{_datadir}/cups/ppdc/fr-braille.po
%{_datadir}/cups/ppdc/imagemagick.defs
%{_datadir}/cups/ppdc/index.defs
%{_datadir}/cups/ppdc/liblouis.defs
%{_datadir}/cups/ppdc/liblouis1.defs
%{_datadir}/cups/ppdc/liblouis2.defs
%{_datadir}/cups/ppdc/liblouis3.defs
%{_datadir}/cups/ppdc/liblouis4.defs
%{_datadir}/cups/ppdc/media-braille.defs
%{_datadir}/cups/drv/cupsfilters.drv
%{_datadir}/cups/drv/generic-brf.drv
%{_datadir}/cups/drv/generic-ubrl.drv
%{_datadir}/cups/drv/indexv3.drv
%{_datadir}/cups/drv/indexv4.drv
%{_datadir}/cups/mime/cupsfilters.types
%{_datadir}/cups/mime/cupsfilters.convs
%{_datadir}/cups/mime/cupsfilters-ghostscript.convs
%{_datadir}/cups/mime/cupsfilters-poppler.convs
%{_datadir}/cups/mime/braille.convs
%{_datadir}/cups/mime/braille.types
%{_datadir}/ppd/cupsfilters
%{_sbindir}/cups-browsed
%{_unitdir}/cups-browsed.service
%{_mandir}/man8/cups-browsed.8.gz
%{_mandir}/man5/cups-browsed.conf.5.gz
%{_mandir}/man1/foomatic-rip.1.gz
%{_mandir}/man1/driverless.1.gz

%files libs
%dir %{_pkgdocdir}/
%{_pkgdocdir}/COPYING
%dir %{_pkgdocdir}/fontembed
%{_pkgdocdir}/fontembed/README
%{_libdir}/libcupsfilters.so.1*
%{_libdir}/libfontembed.so.1*

%files devel
%{_includedir}/cupsfilters
%{_includedir}/fontembed
%{_datadir}/cups/ppdc/escp.h
%{_libdir}/pkgconfig/libcupsfilters.pc
%{_libdir}/pkgconfig/libfontembed.pc
%{_libdir}/libcupsfilters.so
%{_libdir}/libfontembed.so

%changelog
* Thu Sep 17 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.28.2-2
- 1879147 - driverless cannot generate ppd for dns-sd based uris

* Tue Sep 15 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.28.2-1
- 1.28.2

* Thu Sep 03 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.28.1-2
- revert previous commit - systemd-resolved doesn't work with avahi right now
  because missing link in NetworkManager

* Mon Aug 31 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.28.1-2
- MDNS resolving should be done by systemd-resolved now

* Thu Aug 27 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.28.1-1
- 1.28.1 - added driverless fax support

* Fri Aug 21 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.27.5-7
- use configure option instead of downstream, cups-browsed.conf editing, patch
- the exact path in cups-browsed manpage was removed, use the patch removing it instead of downstream one
- use configure option to dont save queues between restarts instead of downstream patch reverting the issue
- memory leaks patch is from upstream too

* Wed Aug 19 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.27.5-6
- 1867412 - cups-browsed leaks memory

* Thu Aug 06 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.27.5-5
- require ipptool explicitly
- remove buildrequire on ipptool

* Wed Aug 05 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.27.5-4
- use %%make_build and %%make_install according FPG
- own 'new' directories

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.27.5-2
- 1848575 - [cups, cups-filters] PPD generators creates invalid cupsManualCopies entry

* Mon Jun 08 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.27.5-1
- 1.27.5

* Tue Apr 14 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.27.4-1
- 1.27.4

* Wed Apr 08 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.27.3-3
- memory issues in cups-browsed

* Mon Apr 06 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.27.3-2
- make nss-mdns and avahi recommended

* Mon Mar 23 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.27.3-1
- 1.27.3

* Fri Mar 13 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.27.2-2
- fix leaks in cups-browsed
- add require on nss-mdns

* Mon Mar 02 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.27.2-1
- 1.27.2

* Tue Feb 25 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.27.1-2
- 1806862 - foomatic-rip handles empty files in bad way

* Tue Feb 18 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.27.1-1
- 1.27.1

* Tue Feb 18 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.27.0-2
- 1802969 - Service "cups-browsed" is crashing all the time

* Tue Jan 28 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.27.0-1
- 1.27.0
- add post scriptlet for update

* Wed Jan 22 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.22.5-13
- fix build with GCC 10 and remove old obsoletes

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 1.22.5-11
- Rebuild for poppler-0.84.0

* Wed Jan 15 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1.22.5-11
- add buildrequires fro systemd-rpm-macros

* Tue Nov 26 2019 Zdenek Dohnal <zdohnal@redhat.com> - 1.22.5-10
- 1776271 - Updated cups-browsed in RHEL 7.7 leaks sockets

* Tue Nov 19 2019 Zdenek Dohnal <zdohnal@redhat.com> - 1.22.5-9
- rebuilt for qpdf-9.1.0

* Tue Oct 22 2019 Zdenek Dohnal <zdohnal@redhat.com> - 1.22.5-8
- 1756726 - Epson ET 7700 reports pwg support, but pwg does not work

* Wed Oct 09 2019 Zdenek Dohnal <zdohnal@redhat.com> - 1.22.5-7
- gs 9.27 now uses setfilladjust2

* Tue Sep 17 2019 Zdenek Dohnal <zdohnal@redhat.com> - 1.22.5-6
- ftbfs with qpdf-9.0.0
- pdftopdf output should not be encrypted

* Wed Sep 11 2019 Zdenek Dohnal <zdohnal@redhat.com> - 1.22.5-5
- require colord, because it is needed for ICC profiles for filters

* Tue Aug 13 2019 Zdenek Dohnal <zdohnal@redhat.com> - 1.22.5-4
- 1740122 - foomatic-rip segfaults when env variable PRINTER is not defined

* Wed Aug 07 2019 Zdenek Dohnal <zdohnal@redhat.com> - 1.22.5-3
- remove unneeded scriptlet

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 08 2019 Zdenek Dohnal <zdohnal@redhat.com> - 1.22.5-1
- 1.22.5

* Tue Mar 26 2019 Zdenek Dohnal <zdohnal@redhat.com> - 1.22.3-1
- 1.22.3

* Fri Feb 01 2019 Zdenek Dohnal <zdohnal@redhat.com> - 1.22.0-4
- cups-brf needs to be run as root

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Marek Kasik <mkasik@redhat.com> - 1.22.0-2
- Rebuild for poppler-0.73.0

* Fri Jan 25 2019 Zdenek Dohnal <zdohnal@redhat.com> - 1.22.0-1
- 1.22.0

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 1.21.6-2
- Rebuilt for libcrypt.so.2 (#1666033)

* Tue Jan 08 2019 Zdenek Dohnal <zdohnal@redhat.com> - 1.21.6-1
- 1.21.6

* Thu Dec 13 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.21.5-1
- 1.21.5

* Mon Nov 12 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.21.2-4
- links in manpages are wrong

* Mon Sep 24 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.21.2-3
- 1632267 - cups-filters needs to obsolete ghostscript-cups and foomatic-filters
- rebuilt for qpdf-8.2.1

* Fri Sep 21 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.21.2-2
- 1628255 - cups-filters: Sticky EOF behavior in glibc breaks descriptor concatenation using dup2 (breaks printing)

* Mon Sep 10 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.21.2-1
- 1.21.2

* Tue Aug 14 2018 Marek Kasik <mkasik@redhat.com> - 1.20.3-7
- Rebuild for poppler-0.67.0

* Tue Jul 24 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.20.3-6
- correcting license

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.20.3-4
- rebuilt for new qpdf-8.1.0

* Tue Jun 12 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.20.3-3
- hybrid pdftops filter requires poppler and ghostscript for run

* Tue Jun 12 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.20.3-2
- cups-browsed needs to have cups.service to run

* Fri Apr 13 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.20.3-1
- 1.20.3

* Wed Apr 04 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.20.2-1
- 1.20.2
- fixing discovering of remote CUPS queues and LDAP queues
- dependency on poppler-utils is now only recommended

* Fri Mar 23 2018 Marek Kasik <mkasik@redhat.com> - 1.20.1-4
- Rebuild for poppler-0.63.0

* Wed Mar 07 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.20.1-3
- Rebuilt for qpdf-8.0.2

* Mon Mar 05 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.20.1-2
- 1.20.1

* Wed Feb 28 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.20.0-8
- add explicit soname -> warning about soname change

* Wed Feb 21 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.20.0-7
- libjpeg is shipped in libjpeg-turbo and pkgconfig in pkgconf-pkg-config

* Mon Feb 19 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.20.0-6
- gcc and gcc-c++ is no longer in buildroot by default

* Wed Feb 14 2018 David Tardon <dtardon@redhat.com> - 1.20.0-5
- rebuild for poppler 0.62.0

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.20.0-4
- Escape macros in %%changelog

* Thu Feb 08 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.20.0-3
- remove old stuff https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/MRWOMRZ6KPCV25EFHJ2O67BCCP3L4Y6N/

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.20.0-1
- Rebase to 1.20.0

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.19.0-2
- Rebuilt for switch to libxcrypt

* Tue Jan 16 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.19.0-1
- Rebase to 1.19.0

* Thu Jan 11 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.17.9-5
- adding build dependency on ghostscript because of its package changes

* Tue Jan 02 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1.17.9-4
- 1529680 - set CreateIPPPrintQueues to ALL and LocalRemoteCUPSQueueNaming to RemoteName

* Mon Nov 20 2017 Zdenek Dohnal <zdohnal@redhat.com> - 1.17.9-3
- fixing patch for upstream issue 1413

* Wed Nov 08 2017 David Tardon <dtardon@redhat.com> - 1.17.9-2
- rebuild for poppler 0.61.0

* Wed Oct 18 2017 Zdenek Dohnal <zdohnal@redhat.com> - 1.17.9-1
- rebase to 1.17.9

* Mon Oct 09 2017 Zdenek Dohnal <zdohnal@redhat.com> - 1.17.8-4
- removing Provides ghostscript-cups and foomatic-filters

* Fri Oct 06 2017 David Tardon <dtardon@redhat.com> - 1.17.8-3
- rebuild for poppler 0.60.1

* Fri Oct 06 2017 Zdenek Dohnal <zdohnal@redhat.com> - 1.17.8-2
- upstream 1413 - Propagation of location doesn't work

* Tue Oct 03 2017 Zdenek Dohnal <zdohnal@redhat.com> - 1.17.8-1
- rebase to 1.17.8

* Tue Sep 19 2017 Zdenek Dohnal <zdohnal@redhat.com> - 1.17.7-1
- rebase to 1.17.7

* Fri Sep 08 2017 David Tardon <dtardon@redhat.com> - 1.17.2-2
- rebuild for poppler 0.59.0

* Wed Sep 06 2017 Zdenek Dohnal <zdohnal@redhat.com> - 1.17.2-1
- rebase to 1.17.2

* Tue Aug 22 2017 Zdenek Dohnal <zdohnal@redhat.com> - 1.16.3-1
- rebase to 1.16.3

* Mon Aug 14 2017 Zdenek Dohnal <zdohnal@redhat.com> - 1.16.1-1
- rebase to 1.16.1

* Thu Aug 10 2017 Zdenek Dohnal <zdohnal@redhat.com> - 1.16.0-2
- rebuilt for qpdf-libs

* Mon Aug 07 2017 Zdenek Dohnal <zdohnal@redhat.com> - 1.16.0-1
- rebase to 1.16.0

* Thu Aug 03 2017 David Tardon <dtardon@redhat.com> - 1.14.1-5
- rebuild for poppler 0.57.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 1.14.1-2
- Rebuilt for Boost 1.64

* Fri Jun 30 2017 Zdenek Dohnal <zdohnal@redhat.com> - 1.14.1-1
- rebase to 1.14.1

* Thu Jun 29 2017 Zdenek Dohnal <zdohnal@redhat.com> - 1.14.0-3
- update python Requires/BuildRequires accordingly to Fedora Guidelines for Python (python-cups -> python3-cups)

* Wed May 31 2017 Zdenek Dohnal <zdohnal@redhat.com> - 1.14.0-2
- removing BuildRequires: mupdf

* Wed May 17 2017 Zdenek Dohnal <zdohnal@redhat.com> - 1.14.0-1
- rebase to 1.14.0

* Fri Apr 28 2017 Zdenek Dohnal <zdohnal@redhat.com> - 1.13.5-1
- rebase to 1.13.5

* Tue Mar 28 2017 David Tardon <dtardon@redhat.com> - 1.13.4-2
- rebuild for poppler 0.53.0

* Fri Feb 24 2017 Zdenek Dohnal <zdohnal@redhat.com> - 1.13.4-1
- rebase to 1.13.4
- 1426567 - Added queues are not marked as remote ones

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.13.3-3
- Rebuilt for Boost 1.63

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.13.3-2
- Rebuilt for Boost 1.63

* Thu Jan 19 2017 Zdenek Dohnal <zdohnal@redhat.com> - 1.13.3-1
- rebase to 1.13.3

* Mon Jan 02 2017 Zdenek Dohnal <zdohnal@redhat.com> - 1.13.2-1
- rebase to 1.13.2

* Mon Dec 19 2016 Zdenek Dohnal <zdohnal@redhat.com> - 1.13.1-1
- rebase to 1.13.1

* Fri Dec 16 2016 David Tardon <dtardon@redhat.com> - 1.13.0-2
- rebuild for poppler 0.50.0

* Mon Dec 12 2016 Zdenek Dohnal <zdohnal@redhat.com> - 1.13.0-1
- rebase to 1.13.0

* Fri Dec 02 2016 Zdenek Dohnal <zdohnal@redhat.com> - 1.12.0-2
- adding new sources

* Fri Dec 02 2016 Zdenek Dohnal <zdohnal@redhat.com> - 1.12.0-1
- rebase to 1.12.0

* Wed Nov 23 2016 David Tardon <dtardon@redhat.com> - 1.11.6-2
- rebuild for poppler 0.49.0

* Fri Nov 11 2016 Zdenek Dohnal <zdohnal@redhat.com> - 1.11.6-1
- rebase to 1.11.6

* Mon Oct 31 2016 Zdenek Dohnal <zdohnal@redhat.com> - 1.11.5-1
- rebase to 1.11.5

* Fri Oct 21 2016 Marek Kasik <mkasik@redhat.com> - 1.11.4-2
- Rebuild for poppler-0.48.0

* Tue Sep 27 2016 Zdenek Dohnal <zdohnal@redhat.com> - 1.11.4-1
- rebase to 1.11.4 

* Tue Sep 20 2016 Zdenek Dohnal <zdohnal@redhat.com> - 1.11.3-1
- rebase to 1.11.3

* Tue Aug 30 2016 Zdenek Dohnal <zdohnal@redhat.com> - 1.11.2-1
- rebase to 1.11.2, adding cupsfilters-poppler.convs and cupsfilters-mupdf.convs into package

* Wed Aug 03 2016 Jiri Popelka <jpopelka@redhat.com> - 1.10.0-3
- %%{_defaultdocdir}/cups-filters/ -> %%{_pkgdocdir}

* Mon Jul 18 2016 Zdenek Dohnal <zdohnal@redhat.com> - 1.10.0-2
- adding new sources cups-filters-1.10.0 

* Mon Jul 18 2016 Zdenek Dohnal <zdohnal@redhat.com> - 1.10.0-1
- rebase 1.10.0, include missing ppd.h

* Mon Jul 18 2016 Marek Kasik <mkasik@redhat.com> - 1.9.0-2
- Rebuild for poppler-0.45.0

* Fri Jun 10 2016 Jiri Popelka <jpopelka@redhat.com> - 1.9.0-1
- 1.9.0

* Tue May  3 2016 Marek Kasik <mkasik@redhat.com> - 1.8.3-2
- Rebuild for poppler-0.43.0

* Thu Mar 24 2016 Zdenek Dohnal <zdohnal@redhat.com> - 1.8.3-1
- Update to 1.8.3, adding cupsfilters-ghostscript.convs to %%files

* Fri Feb 12 2016 Jiri Popelka <jpopelka@redhat.com> - 1.8.2-1
- 1.8.2

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Marek Kasik <mkasik@redhat.com> - 1.8.1-2
- Rebuild for poppler-0.40.0

* Fri Jan 22 2016 Jiri Popelka <jpopelka@redhat.com> - 1.8.1-1
- 1.8.1

* Thu Jan 21 2016 Jiri Popelka <jpopelka@redhat.com> - 1.8.0-1
- 1.8.0

* Tue Jan 19 2016 Jiri Popelka <jpopelka@redhat.com> - 1.7.0-1
- 1.7.0

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.6.0-2
- Rebuilt for Boost 1.60

* Thu Jan 14 2016 Jiri Popelka <jpopelka@redhat.com> - 1.6.0-1
- 1.6.0

* Fri Dec 18 2015 Jiri Popelka <jpopelka@redhat.com> - 1.5.0-1
- 1.5.0

* Tue Dec 15 2015 Jiri Popelka <jpopelka@redhat.com> - 1.4.0-1
- 1.4.0

* Wed Dec 09 2015 Jiri Popelka <jpopelka@redhat.com> - 1.3.0-1
- 1.3.0

* Fri Nov 27 2015 Jiri Popelka <jpopelka@redhat.com> - 1.2.0-1
- 1.2.0

* Wed Nov 11 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.0-2
- Rebuild (qpdf-6)

* Tue Oct 27 2015 Jiri Popelka <jpopelka@redhat.com> - 1.1.0-1
- 1.1.0 (version numbering change: minor version = feature, revision = bugfix)

* Sun Sep 13 2015 Jiri Popelka <jpopelka@redhat.com> - 1.0.76-1
- 1.0.76

* Tue Sep 08 2015 Jiri Popelka <jpopelka@redhat.com> - 1.0.75-1
- 1.0.75

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.0.74-2
- Rebuilt for Boost 1.59

* Wed Aug 26 2015 Jiri Popelka <jpopelka@redhat.com> - 1.0.74-1
- 1.0.74

* Wed Aug 19 2015 Jiri Popelka <jpopelka@redhat.com> - 1.0.73-1
- 1.0.73 - new implicitclass backend

* Fri Jul 24 2015 David Tardon <dtardon@redhat.com> - 1.0.71-3
- rebuild for Boost 1.58 to fix deps

* Thu Jul 23 2015 Orion Poplawski <orion@cora.nwra.com> - 1.0.71-2
- Add upstream patch for poppler 0.34 support

* Wed Jul 22 2015 Marek Kasik <mkasik@redhat.com> - 1.0.71-2
- Rebuild (poppler-0.34.0)

* Fri Jul 03 2015 Jiri Popelka <jpopelka@redhat.com> - 1.0.71-1
- 1.0.71

* Mon Jun 29 2015 Jiri Popelka <jpopelka@redhat.com> - 1.0.70-1
- 1.0.70

* Mon Jun 22 2015 Tim Waugh <twaugh@redhat.com> - 1.0.69-3
- Fixes for glib source handling (bug #1228555).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.69-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Jiri Popelka <jpopelka@redhat.com> - 1.0.69-1
- 1.0.69

* Fri Jun  5 2015 Marek Kasik <mkasik@redhat.com> - 1.0.68-2
- Rebuild (poppler-0.33.0)

* Tue Apr 14 2015 Jiri Popelka <jpopelka@redhat.com> - 1.0.68-1
- 1.0.68

* Wed Mar 11 2015 Jiri Popelka <jpopelka@redhat.com> - 1.0.67-1
- 1.0.67

* Mon Mar 02 2015 Jiri Popelka <jpopelka@redhat.com> - 1.0.66-1
- 1.0.66

* Mon Feb 16 2015 Jiri Popelka <jpopelka@redhat.com> - 1.0.65-1
- 1.0.65

* Fri Jan 23 2015 Marek Kasik <mkasik@redhat.com> - 1.0.61-3
- Rebuild (poppler-0.30.0)

* Thu Nov 27 2014 Marek Kasik <mkasik@redhat.com> - 1.0.61-2
- Rebuild (poppler-0.28.1)

* Fri Oct 10 2014 Jiri Popelka <jpopelka@redhat.com> - 1.0.61-1
- 1.0.61 

* Tue Oct 07 2014 Jiri Popelka <jpopelka@redhat.com> - 1.0.60-1
- 1.0.60

* Sun Sep 28 2014 Jiri Popelka <jpopelka@redhat.com> - 1.0.59-1
- 1.0.59

* Thu Aug 21 2014 Jiri Popelka <jpopelka@redhat.com> - 1.0.58-1
- 1.0.58

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 15 2014 Jiri Popelka <jpopelka@redhat.com> - 1.0.55-2
- Use %%_defaultdocdir instead of %%doc

* Mon Jul 28 2014 Jiri Popelka <jpopelka@redhat.com> - 1.0.55-1
- 1.0.55

* Fri Jun 13 2014 Tim Waugh <twaugh@redhat.com> - 1.0.54-4
- Really fix execmem issue (bug #1079534).

* Wed Jun 11 2014 Jiri Popelka <jpopelka@redhat.com> - 1.0.54-3
- Remove (F21) pdf-landscape.patch

* Wed Jun 11 2014 Tim Waugh <twaugh@redhat.com> - 1.0.54-2
- Fix build issue (bug #1106101).
- Don't use grep's -P switch in pstopdf as it needs execmem (bug #1079534).
- Return work-around patch for bug #768811.

* Mon Jun 09 2014 Jiri Popelka <jpopelka@redhat.com> - 1.0.54-1
- 1.0.54

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.53-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun 03 2014 Jiri Popelka <jpopelka@redhat.com> - 1.0.53-3
- Remove BuildRequires pkgconfig(lcms). pkgconfig(lcms2) is enough.

* Tue May 13 2014 Marek Kasik <mkasik@redhat.com> - 1.0.53-2
- Rebuild (poppler-0.26.0)

* Mon Apr 28 2014 Jiri Popelka <jpopelka@redhat.com> - 1.0.53-1
- 1.0.53

* Wed Apr 23 2014 Jiri Popelka <jpopelka@redhat.com> - 1.0.52-2
- Remove pdftoopvp and urftopdf in %%install instead of not building them.

* Tue Apr 08 2014 Jiri Popelka <jpopelka@redhat.com> - 1.0.52-1
- 1.0.52

* Wed Apr 02 2014 Jiri Popelka <jpopelka@redhat.com> - 1.0.51-1
- 1.0.51 (#1083327)

* Thu Mar 27 2014 Jiri Popelka <jpopelka@redhat.com> - 1.0.50-1
- 1.0.50

* Mon Mar 24 2014 Jiri Popelka <jpopelka@redhat.com> - 1.0.49-1
- 1.0.49

* Wed Mar 12 2014 Jiri Popelka <jpopelka@redhat.com> - 1.0.48-1
- 1.0.48

* Tue Mar 11 2014 Jiri Popelka <jpopelka@redhat.com> - 1.0.47-2
- Don't ship pdftoopvp (#1027557) and urftopdf (#1002947).

* Tue Mar 11 2014 Jiri Popelka <jpopelka@redhat.com> - 1.0.47-1
- 1.0.47: CVE-2013-6473 CVE-2013-6476 CVE-2013-6474 CVE-2013-6475 (#1074840)

* Mon Mar 10 2014 Jiri Popelka <jpopelka@redhat.com> - 1.0.46-3
- BuildRequires: pkgconfig(foo) instead of foo-devel

* Tue Mar  4 2014 Tim Waugh <twaugh@redhat.com> - 1.0.46-2
- The texttopdf filter requires a TrueType monospaced font
  (bug #1070729).

* Thu Feb 20 2014 Jiri Popelka <jpopelka@redhat.com> - 1.0.46-1
- 1.0.46

* Fri Feb 14 2014 Jiri Popelka <jpopelka@redhat.com> - 1.0.45-1
- 1.0.45

* Mon Jan 20 2014 Jiri Popelka <jpopelka@redhat.com> - 1.0.44-1
- 1.0.44

* Tue Jan 14 2014 Jiri Popelka <jpopelka@redhat.com> - 1.0.43-2
- add /usr/bin/foomatic-rip symlink, due to LSB3.2 (#1052452)

* Fri Dec 20 2013 Jiri Popelka <jpopelka@redhat.com> - 1.0.43-1
- 1.0.43: upstream fix for bug #768811 (pdf-landscape)

* Sat Nov 30 2013 Jiri Popelka <jpopelka@redhat.com> - 1.0.42-1
- 1.0.42: includes foomatic-rip (obsoletes foomatic-filters package)

* Tue Nov 19 2013 Tim Waugh <twaugh@redhat.com> - 1.0.41-4
- Adjust filter costs so application/vnd.adobe-read-postscript input
  doesn't go via pstotiff (bug #1008166).

* Thu Nov 14 2013 Jaromír Končický <jkoncick@redhat.com> - 1.0.41-3
- Fix memory leaks in cups-browsed (bug #1027317).

* Wed Nov  6 2013 Tim Waugh <twaugh@redhat.com> - 1.0.41-2
- Include dbus so that colord support works (bug #1026928).

* Wed Oct 30 2013 Jiri Popelka <jpopelka@redhat.com> - 1.0.41-1
- 1.0.41 - PPD-less printing support

* Mon Oct 21 2013 Tim Waugh <twaugh@redhat.com> - 1.0.40-4
- Fix socket leaks in the BrowsePoll code (bug #1021512).

* Wed Oct 16 2013 Tim Waugh <twaugh@redhat.com> - 1.0.40-3
- Ship the gstoraster MIME conversion rule now we provide that filter
  (bug #1019261).

* Fri Oct 11 2013 Tim Waugh <twaugh@redhat.com> - 1.0.40-2
- Fix PDF landscape printing (bug #768811).

* Fri Oct 11 2013 Jiri Popelka <jpopelka@redhat.com> - 1.0.40-1
- 1.0.40
- Use new "hybrid" pdftops renderer.

* Thu Oct 03 2013 Jaromír Končický <jkoncick@redhat.com> - 1.0.39-1
- 1.0.39
- Removed obsolete patches "pdf-landscape" and "browsepoll-notifications"

* Tue Oct  1 2013 Tim Waugh <twaugh@redhat.com> - 1.0.38-4
- Use IPP notifications for BrowsePoll when possible (bug #975241).

* Tue Oct  1 2013 Tim Waugh <twaugh@redhat.com> - 1.0.38-3
- Fixes for some printf-type format mismatches (bug #1014093).

* Tue Sep 17 2013 Tim Waugh <twaugh@redhat.com> - 1.0.38-2
- Fix landscape printing for PDFs (bug #768811).

* Wed Sep 04 2013 Jiri Popelka <jpopelka@redhat.com> - 1.0.38-1
- 1.0.38

* Thu Aug 29 2013 Jaromír Končický <jkoncick@redhat.com> - 1.0.37-1
- 1.0.37.

* Tue Aug 27 2013 Jaromír Končický <jkoncick@redhat.com> - 1.0.36-5
- Added build dependency - font required for running tests

* Tue Aug 27 2013 Jaromír Končický <jkoncick@redhat.com> - 1.0.36-4
- Added checking phase (make check)

* Wed Aug 21 2013 Tim Waugh <twaugh@redhat.com> - 1.0.36-3
- Upstream patch to re-work filter costs (bug #998977). No longer need
  text filter costs patch as paps gets used by default now if
  installed.

* Mon Aug 19 2013 Marek Kasik <mkasik@redhat.com> - 1.0.36-2
- Rebuild (poppler-0.24.0)

* Tue Aug 13 2013 Tim Waugh <twaugh@redhat.com> - 1.0.36-1
- 1.0.36.

* Tue Aug 13 2013 Tim Waugh <twaugh@redhat.com> - 1.0.35-7
- Upstream patch to move in filters from ghostscript.

* Tue Jul 30 2013 Tim Waugh <twaugh@redhat.com> - 1.0.35-6
- Set cost for text filters to 200 so that the paps filter gets
  preference for the time being (bug #988909).

* Wed Jul 24 2013 Tim Waugh <twaugh@redhat.com> - 1.0.35-5
- Handle page-label when printing n-up as well.

* Tue Jul 23 2013 Tim Waugh <twaugh@redhat.com> - 1.0.35-4
- Added support for page-label (bug #987515).

* Thu Jul 11 2013 Jiri Popelka <jpopelka@redhat.com> - 1.0.35-3
- Rebuild (qpdf-5.0.0)

* Mon Jul 01 2013 Jiri Popelka <jpopelka@redhat.com> - 1.0.35-2
- add cups-browsed(8) and cups-browsed.conf(5)
- don't reverse lookup IP address in URI (#975822)

* Wed Jun 26 2013 Jiri Popelka <jpopelka@redhat.com> - 1.0.35-1
- 1.0.35

* Mon Jun 24 2013 Marek Kasik <mkasik@redhat.com> - 1.0.34-9
- Rebuild (poppler-0.22.5)

* Wed Jun 19 2013 Jiri Popelka <jpopelka@redhat.com> - 1.0.34-8
- fix the note we add in cups-browsed.conf

* Wed Jun 12 2013 Jiri Popelka <jpopelka@redhat.com> - 1.0.34-7
- Obsolete cups-php (#971741)

* Wed Jun 05 2013 Jiri Popelka <jpopelka@redhat.com> - 1.0.34-6
- one more cups-browsed leak fixed (#959682)

* Wed Jun 05 2013 Jiri Popelka <jpopelka@redhat.com> - 1.0.34-5
- perl is actually not required by pstopdf, because the calling is in dead code

* Mon Jun 03 2013 Jiri Popelka <jpopelka@redhat.com> - 1.0.34-4
- fix resource leaks and other problems found by Coverity & Valgrind (#959682)

* Wed May 15 2013 Jiri Popelka <jpopelka@redhat.com> - 1.0.34-3
- ship ppdc/pcl.h because of cupsfilters.drv

* Tue May 07 2013 Jiri Popelka <jpopelka@redhat.com> - 1.0.34-2
- pstopdf requires bc (#960315)

* Thu Apr 11 2013 Jiri Popelka <jpopelka@redhat.com> - 1.0.34-1
- 1.0.34

* Fri Apr 05 2013 Fridolin Pokorny <fpokorny@redhat.com> - 1.0.33-1
- 1.0.33
- removed cups-filters-1.0.32-null-info.patch, accepted by upstream

* Thu Apr 04 2013 Fridolin Pokorny <fpokorny@redhat.com> - 1.0.32-2
- fixed segfault when info is NULL

* Thu Apr 04 2013 Fridolin Pokorny <fpokorny@redhat.com> - 1.0.32-1
- 1.0.32

* Fri Mar 29 2013 Jiri Popelka <jpopelka@redhat.com> - 1.0.31-3
- add note to cups-browsed.conf

* Thu Mar 28 2013 Jiri Popelka <jpopelka@redhat.com> - 1.0.31-2
- check cupsd.conf existence prior to grepping it (#928816)

* Fri Mar 22 2013 Jiri Popelka <jpopelka@redhat.com> - 1.0.31-1
- 1.0.31

* Tue Mar 19 2013 Jiri Popelka <jpopelka@redhat.com> - 1.0.30-4
- revert previous change

* Wed Mar 13 2013 Jiri Popelka <jpopelka@redhat.com> - 1.0.30-3
- don't ship banners for now (#919489)

* Tue Mar 12 2013 Jiri Popelka <jpopelka@redhat.com> - 1.0.30-2
- move BrowsePoll from cupsd.conf to cups-browsed.conf in %%post

* Fri Mar 08 2013 Jiri Popelka <jpopelka@redhat.com> - 1.0.30-1
- 1.0.30: CUPS browsing and broadcasting in cups-browsed

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jan 19 2013 Rex Dieter <rdieter@fedoraproject.org> 1.0.29-3
- backport upstream buildfix for poppler-0.22.x

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1.0.29-2
- rebuild due to "jpeg8-ABI" feature drop

* Thu Jan 03 2013 Jiri Popelka <jpopelka@redhat.com> 1.0.29-1
- 1.0.29

* Wed Jan 02 2013 Jiri Popelka <jpopelka@redhat.com> 1.0.28-1
- 1.0.28: cups-browsed daemon and service

* Thu Nov 29 2012 Jiri Popelka <jpopelka@redhat.com> 1.0.25-1
- 1.0.25

* Fri Sep 07 2012 Jiri Popelka <jpopelka@redhat.com> 1.0.24-1
- 1.0.24

* Wed Aug 22 2012 Jiri Popelka <jpopelka@redhat.com> 1.0.23-1
- 1.0.23: old pdftopdf removed

* Tue Aug 21 2012 Jiri Popelka <jpopelka@redhat.com> 1.0.22-1
- 1.0.22: new pdftopdf (uses qpdf instead of poppler)

* Wed Aug 08 2012 Jiri Popelka <jpopelka@redhat.com> 1.0.20-4
- rebuild

* Thu Aug 02 2012 Jiri Popelka <jpopelka@redhat.com> 1.0.20-3
- commented multiple licensing breakdown (#832130)
- verbose build output

* Thu Aug 02 2012 Jiri Popelka <jpopelka@redhat.com> 1.0.20-2
- BuildRequires: poppler-cpp-devel (to build against poppler-0.20)

* Mon Jul 23 2012 Jiri Popelka <jpopelka@redhat.com> 1.0.20-1
- 1.0.20

* Tue Jul 17 2012 Jiri Popelka <jpopelka@redhat.com> 1.0.19-1
- 1.0.19

* Wed May 30 2012 Jiri Popelka <jpopelka@redhat.com> 1.0.18-1
- initial spec file
