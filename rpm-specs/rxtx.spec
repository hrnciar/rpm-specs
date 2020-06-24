%global upver	2.2
%global uprel	20100211

%global jni	%{_libdir}/%{name}

Summary:	Parallel communication for the Java Development Toolkit
Name:		rxtx
Version:	%{upver}
Release:	0.25.%{uprel}%{?dist}
License:	LGPLv2+
URL:		http://rxtx.qbang.org/
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  cvs -d:pserver:anonymous@qbang.org:/var/cvs/cvsroot co -r commapi-0-0-1 -D "2010-02-11" -d rxtx-%%{uprel} rxtx-devel
#  tar cjvf rxtx-%%{uprel}.tar.bz2 --exclude CVS --exclude .cvsignore rxtx-%%{uprel}
Source0:	%{name}-%{uprel}.tar.bz2
Source1:	README.distro
Source2:	rxtx-osgi.bnd
Patch1:		rxtx-2.2-loadlibrary.patch
Patch2:		rxtx-sys_io_h_check.patch
Patch3:		rxtx-2.2-fhs_lock.patch
Patch4:		rxtx-2.2-lock.patch
Patch5:		rxtx-2.2-Add-Arduino-driver-ttyACM-rxtxcomm-as-device.patch
Patch6:		rxtx-2.2-java-version-fix.patch
Patch7:		rxtx-2.2-convert-strcpy-to-strncpy.patch
Patch8:		rxtx-2.2-minor.patch

BuildRequires:	libtool automake
BuildRequires:	ant
BuildRequires:	ant-junit
BuildRequires:	junit
BuildRequires:	aqute-bnd
BuildRequires:	javapackages-local

%description
rxtx is an full implementation of java commapi which aims to support RS232
IEEE 1284, RS485, I2C and RawIO.

%prep
%setup -q -n rxtx-%{uprel}
sed -e 's|@JNIPATH@|%{jni}|' %{PATCH1} | patch -s -b --suffix .p1 -p1
%patch2 -p1
%patch3 -p1
%if 0%{?fedora} || 0%{?rhel} > 6
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%endif
%patch8 -p1
# remove prebuild binaries
find . -name '*.jar' -exec rm {} \;
find . -name '*.hqx' -exec rm {} \;
cp -a %{SOURCE1} .

# Don't need to install jar file, mvn_install will do it
sed -i -e '/JHOME/d' Makefile.in

%build
export JAVA_HOME=%{java_home}
%configure
# parallel make fails with make %%{?_smp_mflags}
make
iconv -f ISO_8859-1 -t UTF-8 ChangeLog >ChangeLog.utf-8
mv ChangeLog.utf-8 ChangeLog

# Inject OSGi metadata
bnd wrap -p %{SOURCE2} -v %{version} -o RXTXcomm-bnd.jar RXTXcomm.jar
mv RXTXcomm-bnd.jar RXTXcomm.jar

%install
mkdir -p %{buildroot}%{jni}
make RXTX_PATH=%{buildroot}%{jni} install
find %{buildroot} -name '*.la' -exec rm {} \;

%mvn_artifact org.rxtx:rxtx:%{version} RXTXcomm.jar
%mvn_file org.rxtx:rxtx:%{version} RXTXcomm
%mvn_install

%files -f .mfiles
%license COPYING
%doc AUTHORS ChangeLog README TODO README.distro
%{jni}

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.25.20100211
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 02 2019 Lubomir Rintel <lkundrak@v3.sk> - 2.2-0.24.20100211
- Fix an undefined symbol error (rh #1645856, patch from Serge Droz)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.23.20100211
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.22.20100211
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.21.20100211
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.20.20100211
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.19.20100211
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.18.20100211
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Mat Booth <mat.booth@redhat.com> - 2.2-0.17.20100211
- Make the readme file distro agnostic, since this RPM may be built for many
  distros

* Wed May 03 2017 Mat Booth <mat.booth@redhat.com> - 2.2-0.16.20100211
- Patch to build on all architectures (thanks to debian)

* Fri Mar 31 2017 Mat Booth <mat.booth@redhat.com> - 2.2-0.15.20100211
- Add OSGi metadata
- Minor spec file cleanup

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.14.20100211.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-0.14.20100211.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 02 2015 Rafael Fonseca <rdossant@redhat.com> - 2.2-0.14.20100211.2
- Fix compilation on ppc64le (#1252860)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-0.14.20100211.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 01 2015 Alec Leamas <leamas.alec@gmail.com> - 2.2-0.14.20100211
- Apply patch from bug #1208453 (strcpy -> strncpy).

* Wed Mar 18 2015 Alec Leamas <leamas.alec@gmail.com> - 2.2-0.13.20100211
- Patch java library version string to match the so-libs's 2.2pre2.

* Tue Mar 10 2015 Alec Leamas <leamas.alec@gmail.com> - 2.2-0.12.20100211
- Add Arduino ttyACM + rxtxcomm devices patch

* Thu Feb 26 2015 Alec Leamas  <leamas.alec@gmail.com> - 2.2-0.11.20100211
- Use mvn_artifact et. al. instead to provide maven metadata.
- Fix packaging bug with jni-related jar in /usr/share/java.

* Tue Sep 16 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.2-0.10.20100211
- Bump to fix NVR

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-0.9.20100211.2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 04 2014 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 2.2-0.8.20100211.2.2
- Handle lack of sys/io.h on AArch64

* Wed Jul 30 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.2-0.8.20100211.2.1
- Update deps to fix FTBFS

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-0.7.20100211.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 2.2-0.7.20100211.2
- Use Requires: java-headless rebuild (#1067528)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-0.7.20100211.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Levente Farkas <lfarkas@lfarkas.org> - 2.2-0.7.20100211
- add patch for #926466 by Dennis Gilmore

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-0.6.20100211.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-0.6.20100211.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-0.6.20100211.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 17 2011 Levente Farkas <lfarkas@lfarkas.org> - 2.2-0.6.20100211
- fix lock dir #731218

* Fri Jul 15 2011 Levente Farkas <lfarkas@lfarkas.org> - 2.2-0.5.20100211
- fix doc #722353

* Thu Mar 17 2011 Levente Farkas <lfarkas@lfarkas.org> - 2.2-0.4.20100211
- fix fhs_lock #666761

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-0.3.20100211.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov  9 2010 Levente Farkas <lfarkas@lfarkas.org> - 2.2-0.3.20100211
- fix lock dir location #650849

* Tue Mar 30 2010 Dennis Gilmore <dennis@ausil.us> - 2.2-0.2.20100211
- apply patch from Patrick Ale excluding the inclusion of sys/io.h on sparc

* Thu Feb 11 2010 Levente Farkas <lfarkas@lfarkas.org> - 2.2-0.1.20100211
- update to the latest cvs to fix #555219

* Wed Aug 12 2009 Ville Skyttä <ville.skytta@iki.fi> - 2.1-0.8.7r2
- Use upstream gzipped tarball instead of zip.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-0.7.7r2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun  2 2009 Dan Horak <dan[at]danny.cz> - 2.1-0.6.7r2
- add s390/s390x to ExcludeArch

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-0.5.7r2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Levente Farkas <lfarkas@lfarkas.org> - 2.1-0.4.7r2
- bump release number

* Fri Feb 13 2009 Levente Farkas <lfarkas@lfarkas.org> - 2.1-0.3.7r2
- fix new libtool compile bug

* Thu Sep 25 2008 Levente Farkas <lfarkas@lfarkas.org> - 2.1-0.2.7r2
- a few more spec file cleanup

* Mon Sep 15 2008 Levente Farkas <lfarkas@lfarkas.org> - 2.1-0.1.7r2
- update as requested by fedora

* Mon Jul 21 2008 Gergo Csontos <gergo.csontos@gmail.com> - 2.1
- Initial release
