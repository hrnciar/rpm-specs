Summary:        Free firewire audio driver library
Name:           libffado
Version:        2.4.3
Release:        2%{?dist}
# src/libutil/float_cast.h is LGPLv2+.
# The rest is (GPLv2 or GPLv3)
License:        LGPLv2+ and (GPLv2 or GPLv3)
URL:            http://www.ffado.org/
Source0:        http://www.ffado.org/files/%{name}-%{version}.tgz
# The trunk is tarballed as follows:
# bash libffado-snapshot.sh 2088
# The fetch script
Source9:        libffado-snapshot.sh

BuildRequires:  alsa-lib-devel
BuildRequires:  dbus-c++-devel
BuildRequires:  dbus-devel
BuildRequires:  python3-dbus
BuildRequires:  python3-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  glibmm24-devel
BuildRequires:  graphviz
BuildRequires:  libappstream-glib
BuildRequires:  libconfig-devel
BuildRequires:  libiec61883-devel
BuildRequires:  libraw1394-devel
BuildRequires:  libxml++-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-devel
BuildRequires:  python3-scons
BuildRequires:  subversion
ExcludeArch:    s390 s390x
Requires:       udev

%description
The FFADO project aims to provide a generic, open-source solution for the
support of FireWire based audio devices for the Linux platform. It is the
successor of the FreeBoB project.

%package devel
Summary:        Free firewire audio driver library development headers
License:        GPLv2 or GPLv3
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files needed to build applications against libffado.

%package -n ffado
Summary:        Free firewire audio driver library applications and utilities
# support/tools/* is GPLv3
# Some files in support/mixer-qt4/ffado are GPLv3+
# The rest is GPLv2 or GPLv3
License:        GPLv3 and GPLv3+ and (GPLv2 or GPLv3)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dbus
# the following got renamed to python2-dbus on F28. We are using the backward-compatible Provides
Requires:       python3-dbus
Requires:       python3-qt5

%description -n ffado
Applications and utilities for use with libffado.


%prep
%setup -q

# Work around a bug in scons < 3.0.2
if %{__python3} -c 'import SCons; import sys; sys.exit(not tuple(int(d) for d in SCons.__version__.split(".")) < (3, 0, 2))'; then
    sed -i '/^CacheDir/d' SConstruct
fi

# We don't want to install all tests
sed -i '/Install/d' tests/{,*/}SConscript

# Use standard icon name
sed -i 's|hi64-apps-ffado.png|ffado.png|' support/mixer-qt4/ffado/ffadowindow.py

# Fix Python shebangs
sed -i 's|/usr/bin/.*python$|/usr/bin/python3|' \
    admin/*.py doc/SConscript tests/python/*.py tests/*.py \
    support/mixer-qt4/ffado-mixer* support/mixer-qt4/SConscript \
    support/tools/*.py support/tools/SConscript

sed -i 's|-m32||' SConstruct

%build
export CFLAGS="%{optflags} -ffast-math"
export CXXFLAGS="%{optflags} -ffast-math --std=gnu++11"
export LDFLAGS="%{build_ldflags}"
scons-3 %{?_smp_mflags} \
      ENABLE_SETBUFFERSIZE_API_VER=True \
      ENABLE_OPTIMIZATIONS=True \
      CUSTOM_ENV=True \
      BUILD_DOC=user \
      PREFIX=%{_prefix} \
      LIBDIR=%{_libdir} \
      MANDIR=%{_mandir} \
      UDEVDIR=%{_prefix}/lib/udev/rules.d/ \
      PYPKGDIR=%{python3_sitelib}/ffado/ \
      PYTHON_INTERPRETER=/usr/bin/python3 \
      BUILD_TESTS=1

%install
# Exporting flags so that the install does not trigger another build
export CFLAGS="%{optflags} -ffast-math"
export CXXFLAGS="%{optflags} -ffast-math --std=gnu++11"
export LDFLAGS="%{build_ldflags}"
scons-3 DESTDIR=%{buildroot} PREFIX=%{_prefix}\
      install

# We need to install the xdg stuff manually
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
                     --add-category="Settings" \
                     --set-icon=ffado \
                     support/xdg/ffado.org-ffadomixer.desktop
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
ln -s ../../../../libffado/icons/hi64-apps-ffado.png \
    %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/ffado.png

# Install ffado-test RHBZ#805940
install -m 755 tests/ffado-test %{buildroot}%{_bindir}

%ldconfig_scriptlets

%check
desktop-file-validate \
      %{buildroot}%{_datadir}/applications/ffado.org-ffadomixer.desktop
appstream-util validate-relax --nonet \
      %{buildroot}%{_datadir}/metainfo/ffado-mixer.appdata.xml

%files
%license LICENSE.*
%doc AUTHORS ChangeLog README
%{_libdir}/libffado.so.*
%dir %{_datadir}/libffado/
%{_datadir}/libffado/configuration
%{_prefix}/lib/udev/rules.d/*
%{_libdir}/libffado/static_info.txt

%files devel
%doc doc/reference/html/
%{_includedir}/libffado/
%{_libdir}/pkgconfig/libffado.pc
%{_libdir}/libffado.so

%files -n ffado
%{_mandir}/man1/ffado-*.1*
%{_bindir}/*
%{_datadir}/libffado/*.xml
%{_datadir}/libffado/icons/
%{_datadir}/dbus-1/services/org.ffado.Control.service
%{_datadir}/applications/ffado.org-ffadomixer.desktop
%{_datadir}/icons/hicolor/64x64/apps/ffado.png
%{_datadir}/metainfo/ffado-mixer.appdata.xml
%{python3_sitelib}/ffado/


%changelog
* Sat May 30 2020 Nils Philippsen <nils@tiptoe.de> - 2.4.3-2
- work around a bug in scons < 3.0.2

* Fri May 29 2020 Nils Philippsen <nils@tiptoe.de> - 2.4.3-1
- version 2.4.3

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.1-11
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 18 2019 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 2.4.1-9
- Convert the package from Python2 to Python3

* Sat Aug 03 2019 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 2.4.1-8
- scons renamed to scons-2 in the recent Fedora package

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 07 2019 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 2.4.1-6
- Added BR: python2-rpm-macros

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Tom Callaway <spot@fedoraproject.org> - 2.4.1-4
- rebuild for new libconfig

* Thu Jul 19 2018 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 2.4.1-3
- Fixed Python shebangs
- Added BR: python2-enum34

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 25 2018 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 2.4.1-1
- Update to 2.4.1
- Drop upstreamed patches

* Wed Apr 18 2018 Iryna Shcherbina <shcherbina.iryna@gmail.com> - 2.4.0-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Feb 10 2018 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 2.4.0-5
- Build with RPM_LD_FLAGS exported in install section as well

* Fri Feb  9 2018 Florian Weimer <fweimer@redhat.com> - 2.4.0-4
- Use LDFLAGS from redhat-rpm-config

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.4.0-2
- Switch to %%ldconfig_scriptlets

* Fri Jan 05 2018 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 2.4.0-1
- Update to 2.4.0
- Drop upstreamed patches

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.3.0-8
- Remove obsolete scriptlets

* Mon Nov 06 2017 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 2.3.0-7
- Build against scons3
- Build against newer gcc/glibc

* Thu Aug 10 2017 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 2.3.0-6
- Fix FTBFS on F27
- Backported fixes from trunk for various compilation warnings
- MIPS support RHBZ#1366701

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Thu Feb 16 2017 Jonathan Wakely <jwakely@redhat.com> - 2.3.0-2
- Patch invalid code to build with GCC 7

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 08 2016 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 2.3.0-1
- Update to 2.3.0.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Mar 01 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 2.2.1-8
- Fix FTBFS with GCC 6 (#1307721)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Lubomir Rintel <lkundrak@v3.sk> - 2.2.1-6
- Fix FTBFS

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.1-4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jun 01 2014 Brendan Jones <brendan.jones.it@gmail.com> 2.2.1-1
- Update to 2.2.1
- Remove incorporated udev rules patch

* Mon Sep 30 2013 Brendan Jones <brendan.jones.it@gmail.com> 2.1.0-4
- Corrrect udev rules RFBZ#999580
- Correct changelog

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Sep 20 2012 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 2.1.0-1
- Update to 2.1.0.
- Drop upstreamed & old patches, README.Fedora file.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-0.10.20120325.svn2088
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 2.1.0-0.9.20120325.svn2088
- Fix multilib confict RHBZ#831405
- Fix DSO linking #ticket 355

* Sun Mar 25 2012 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 2.1.0-0.8.20120325.svn2088
- Update to svn2088.
- Drop upstreamed gcc-4.7 patch.

* Thu Mar 22 2012 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 2.1.0-0.7.20111030.svn2000
- Include the ffado-test executable RHBZ#805940
- Fix .desktop file warning

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-0.6.20111030.svn2000
- Rebuilt for c++ ABI breakage

* Tue Jan 10 2012 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 2.1.0-0.5.20111030.svn2000
- gcc-4.7 compile fix

* Sun Oct 30 2011 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 2.1.0-0.4.20111030.svn2000
- Update to svn2000.
- Drop the gold linker patch. The issue is properly solved upstream. See upstream tracker #293

* Tue Apr 26 2011 Brendan Jones <brendan.jones.it@gmail.com> - 2.1.0-0.3.20110426.svn1983
- Update to svn1983
- Clean up redundant patches
- Patch to rebuild using gold linker. Fixes RHBZ#684392

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-0.2.20101015.svn1913
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct 15 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 2.1.0-0.1.20101015.svn1913
- Update to svn1913. Fixes RHBZ#635315
- Drop upstreamed patches

* Thu Aug 26 2010 Dan Horák <dan[at]danny.cz> - 2.0.1-5.20100706.svn1864
- no Firewire on s390(x)

* Thu Jul 29 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 2.0.1-4.20100706.svn1864
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 14 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 2.0.1-3.20100706.svn1864
- Remove ENABLE_ALL
- Improve the libffado-dont-use-bundled-libs.patch
- Drop BR: expat-devel libavc1394-devel
- Move configuration file to the library package
- Minor enhancement in the .desktop file
- Add links to upstream tickets for patches
- Add -ffast-math to the compiler flags
- Add patch to compile against libconfig-1.4.5

* Tue Jul 13 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 2.0.1-2.20100706.svn1864
- Add ENABLE_ALL flag to support more devices
- Don't bundle tests
- Include some preliminary documentation for the tools until the manpages arrive
- Patch out bundled libraries. Also fixes some rpmlints
- Improve the instructions how to create the tarball

* Wed Jul 07 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 2.0.1-1.20100706.svn1864
- Update to trunk, post 2.0.1.

* Sat Jun 05 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 2.0.0-1.20100605.svn1845
- Update to trunk, post 2.0.0.

* Mon May 18 2009 Jarod Wilson <jarod@redhat.com> - 2.0-0.4.rc2
- Update to 2.0.0-rc2

* Thu Nov 06 2008 Jarod Wilson <jarod@redhat.com> - 2.0-0.3.beta7
- Update to beta7
- Put arch-dependent helper/test binaries in libexecdir instead of datadir

* Sun Aug 10 2008 Jarod Wilson <jwilson@redhat.com> - 2.0-0.2.beta6
- Review clean-ups (#456353)

* Tue Jul 22 2008 Jarod Wilson <jwilson@redhat.com> - 2.0-0.1.beta6
- Initial Fedora build of libffado
