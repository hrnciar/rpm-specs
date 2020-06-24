%global readers_dir %(pkg-config libpcsclite --variable=usbdropdir)


Name:		pcsc-cyberjack
Summary:	PC/SC driver for REINER SCT cyberjack USB chip card reader
Version:	3.99.5final.SP13
%global version_prefix %(c=%{version}; echo ${c:0:6})
%global version_suffix %(c=%{version}; echo ${c:12:4})
Release:	3%{?dist}
License:	GPLv2+ and LGPLv2+
URL:		http://www.reiner-sct.de/
Source0:	http://support.reiner-sct.de/downloads/LINUX/V%{version_prefix}_%{version_suffix}/%{name}_%{version}.tar.gz
Source1:	pcsc-cyberjack-3.99.5final.SP09-README-FEDORA
# this patch replaces the obsoleted AC_PROG_LIBTOOLT macro with LT_INIT
# the patch is sent to upstream per email (20160528)
Patch0:		pcsc-cyberjack-3.99.5final.SP09-configure.patch
Patch1:		pcsc-cyberjack-3.99.5final.SP09-gcc10.patch
Requires:	udev, pcsc-lite
%if 0%{?rhel} && 0%{?rhel} <= 6
Requires(post): /sbin/service
Requires(postun): /sbin/service
%endif

BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	libusb1-devel
BuildRequires:	readline-devel
BuildRequires:	libsysfs-devel
BuildRequires:	pcsc-lite-devel >= 1.3.0

%package cjflash
Summary:	Flash tool for cyberJack
Requires:	%{name} = %{version}

%package examples
Summary:	Sample code
Requires:	%{name} = %{version}
License:	GPLv2+

%description
REINER SCT cyberJack USB chip card reader user space driver.

This package includes the IFD driver for the cyberJack non-contact (RFID)
and contact USB chip card reader.

For more information regarding installation under Linux see the README.txt
in the documentation directory, esp. regarding compatibility with host
controllers.

For more information about the reader, software updates and a shop see
http://www.reiner-sct.com/

%description cjflash
Tool to flash Reiner SCT cyberJack card readers.

%description examples
sample code to use/test SCardControl() API by Ludovic Rousseau

%prep
%setup -q
%patch0 -p1
%patch1 -p1
autoreconf --force --install

# README-FEDORA
install -pm 644 %{SOURCE1} README-FEDORA.txt

%build
# while the docs say --enable-udev will create udev files, I get no rule
# in etc/udev, so making my own, based on debian one
# maybe this will change after 3.99.5final.SP03
%configure --disable-static \
	--mandir=%{_mandir}/man8 \
	--enable-pcsc \
	--sysconfdir="%{_sysconfdir}" \
	--with-usbdropdir="%{readers_dir}" \
	--enable-release \
	--enable-udev \
	--enable-hal=no

%make_build
pushd doc
iconv -f iso8859-1 -t utf-8 LIESMICH.txt > LIESMICH.txt.conv && mv -f LIESMICH.txt.conv LIESMICH.txt
iconv -f iso8859-1 -t utf-8 README.txt > README.txt.conv && mv -f README.txt.conv README.txt
popd

# cjflash does not get built automatically
pushd tools/cjflash
%make_build
popd

%install
%make_install
rm %{buildroot}%{readers_dir}/libifd-cyberjack.bundle/Contents/Linux/libifd-cyberjack.la
mv %{buildroot}/etc/cyberjack.conf.default %{buildroot}/etc/cyberjack.conf

# udev rule based on the file from debian sub-folder
# we need the devices to be in group cyberjack
sed -i 's/GROUP="pcscd"/GROUP="cyberjack"/' debian/libifd-cyberjack6.udev
install -Dm 644 debian/libifd-cyberjack6.udev %{buildroot}/usr/lib/udev/rules.d/93-cyberjack.rules

# cjflash does not get installed automatically
pushd tools/cjflash
make DESTDIR=%{buildroot} install
popd

# we do not want /usr/lib*/cyberjack/pcscd_init.diff
rm -rf %{buildroot}%{_libdir}/cyberjack/pcscd_init.diff

%pre
getent group cyberjack >/dev/null || groupadd -r cyberjack

%post
#/sbin/ldconfig
udevadm control --reload-rules
%if 0%{?rhel} && 0%{?rhel} <= 6
  /sbin/service pcscd condrestart > /dev/null 2>&1 || :
%else
  /usr/bin/systemctl try-restart pcscd.socket
%endif
exit 0

%postun
#/sbin/ldconfig
udevadm control --reload-rules
if [ $1 = 0 ]; then
%if 0%{?rhel} && 0%{?rhel} <= 6
  /sbin/service pcscd condrestart > /dev/null 2>&1 || :
%else
  /usr/bin/systemctl try-restart pcscd.socket
%endif
fi
exit 0

%files
%{!?_licensedir:%global license %doc}

# AUTHORS is 0 length and will not be packaged therefore
%doc etc/cyberjack.conf.default README-FEDORA.txt ChangeLog debian/changelog
%doc doc/README.txt doc/README.pdf doc/README.html
%doc doc/LIESMICH.txt doc/LIESMICH.pdf doc/LIESMICH.html
%license COPYING COPYRIGHT.GPL COPYRIGHT.LGPL

/usr/lib/udev/rules.d/93-cyberjack.rules
%{readers_dir}/*

%config(noreplace) %{_sysconfdir}/cyberjack.conf


%files cjflash
%{!?_licensedir:%global license %doc}
%{_bindir}/cjflash
%license COPYING

%files examples
%doc doc/verifypin_ascii.c doc/verifypin_fpin2.c

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff law <law@redhta.com> - 3.99.5final.SP13-2
- Fix narrowing convesion problem caught by gcc-10

* Sun Sep 01 2019 Robert Scheck <robert@fedoraproject.org> - 3.99.5final.SP13-1
- Update to new upstream version SP13 (#1554806)
- Drop requirements for 'initscripts' from specfile (#1592381)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP12-1
- new upstream version
- man8/cyberjack.8 no longer present it seems

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Jens Lody <fedora@jenslody.de> - 3.99.5final.SP11-3
- Added BuildRequires for gcc and gcc-c++.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 11 2017 Jens Lody <fedora@jenslody.de> - 3.99.5final.SP11-1
- New upstream release, fixes #1480509.
- Create source-url dynamically, so it can be used by
  upstream-release-monitoring.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri May 27 2016 Jens Lody <fedora@jenslody.de> - 3.99.5final.SP09-1
- New upstream, which fixes an usb-bug.
- Gui finally removed by upstream, was not build/packaged anyway.
- The cyberjack binary, used for troubleshooting the install, was also
  removed upstream.

* Fri Feb 05 2016 Jens Lody <fedora@jenslody.de> - 3.99.5final.SP08-4
- Add patch to build with gcc6 on rawhide.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 10 2015 Jens Lody <fedora@jenslody.de> - 3.99.5final.SP08-2
- The devices created by udev have to be in group "cyberjack", not in "pcscd"

* Mon Dec 07 2015 Jens Lody <fedora@jenslody.de> - 3.99.5final.SP08-2
- new upstream
- cleaned up spec-file to follow actual guidelines
- remove unneeded stuff from spec-file

* Sat Jul 18 2015 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP07-3
- adjusted patch, submitted by Jens, this one works on epel6 as well [1195002]

* Tue Jul 14 2015 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP07-2
- include Jens' PIN_VERIFY_MODIFY_STRUCTURE patch [1195002]

* Fri Jul 10 2015 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP07-1
- new upstream version
- not calling autoconf

* Tue Jun 23 2015 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP05-4
- added autoconf to build requires

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.99.5final.SP05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.99.5final.SP05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 23 2014 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP05-1
- new upstream version
- when working past midnight, do not only look at day number when writing changelog date. Fixed two bogus dates.

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.99.5final.SP03-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jul 31 2013 Ville Skyttä <ville.skytta@iki.fi> - 3.99.5final.SP03-14
- Fix build with unversioned %%{_docdir_fmt}.

* Thu Apr 25 2013 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP03-13
- removed /usr/lib64/cyberjack/pcscd_init.diff (#956604)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.99.5final.SP03-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jan 19 2013 Robert Scheck <robert@fedoraproject.org> 3.99.5final.SP03-11
- allow same package to be built on Red Hat Enterprise Linux

* Mon Oct 22 2012 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP03-10
- moved udev rule

* Mon Oct 22 2012 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP03-9
- added link to fedora-15-cyberjack-kartenleser-in-betrieb-nehmen to README-FEDORA.txt
- removed redirect of sysctl output to dev null
- fixed typos in description
- set the udev rule to be a non-replaced config

* Sun Oct 14 2012 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP03-8
- move to systemd

* Sat Jun 2 2012 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP03-7
- use %%{_mandir} in configure

* Fri Jun 1 2012 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP03-6
- added unistd patch

* Wed Feb 29 2012 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP03-5
- using /sbin/service again so this works on F16, F17, RHEL5 and RHEL6

* Sat Feb 25 2012 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP03-4
- gui now only built if withGUI set

* Sat Feb 25 2012 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP03-3
- back out man page patch
- change configure flags to match http://sources.gentoo.org/cgi-bin/viewvc.cgi/gentoo-x86/dev-libs/cyberjack/cyberjack-3.99.5_p02-r1.ebuild?view=markup

* Fri Feb 24 2012 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP03-2
- cleanup of the spec file from upstream tarball for Fedora 16
- tarball version strings contains 'final', so adding --enable-release
- enforcing build of cjflash
- brutal patch to have man page in correct place, my automake-fu is non-existent
- what is that empty gui package defined in the orifginal spec file?
- debian/copyright says it's LGPLv2+

* Tue Jun 14 2011 09:53:20 +0200 - Frank Neuber <sct@kernelport.com>
+ pcsc-cyberjack-3.99.5final.SP02
- released 3.99.5final.SP02
- see changelog in debian/changelog in the source package

