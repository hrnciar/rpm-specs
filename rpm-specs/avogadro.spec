# Avogadro supports Python2 only

%undefine _ld_as_needed

Name:           avogadro
Version:        1.2.0
Release:        31%{?dist}
Summary:        An advanced molecular editor for chemical purposes
License:        GPLv2
URL:            http://avogadro.openmolecules.net/
Source0:        https://github.com/cryos/avogadro/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml

## upstreamable patches
# Fix qmake mkspecs installation directory
Patch0:         %{name}-1.1.1-mkspecs-dir.patch
# Remove -Wl,-s from the compiler flags, fixes -debuginfo (#700080)
Patch1:         %{name}-1.1.1-no-strip.patch
# avogadro.pc missing eigen dependency
Patch2:         %{name}-%{version}-pkgconfig_eigen.patch

## upstreamable
# fix build with cmake-3.2+
# https://sourceforge.net/p/avogadro/bugs/746/
Patch10:        %{name}-cmake-3.2.patch

# fix build with recent boost
Patch12:        %{name}-1.1.1-Q_MOC_RUN.patch

# fix build with recent Qt
Patch14:        %{name}-1.1.1-qt.patch

Patch15:        %{name}-%{version}-libmsymfloat.patch

# Backport commit ca0094cb670513ac6d6da4d67ddcbc8e1d503592 for eigen3 >= 3.3.0 support,
# slightly improved, see https://github.com/cryos/avogadro/pull/894
Patch16:        %{name}_eigen3.patch

Patch18:        %{name}-%{version}-Allow_plot_axis_width_to_be_changed.patch

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-utils, docbook-utils-pdf
BuildRequires:  gcc-c++, gcc
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(glew) >= 1.5.0
BuildRequires:  pkgconfig(openbabel-2.0) >= 2.2.2
BuildRequires:  pkgconfig(QtGui) pkgconfig(QtNetwork) pkgconfig(QtOpenGL)
BuildRequires:  doxygen
BuildRequires:  libappstream-glib
%if 0%{?ENABLE_TESTS:1}
BuildRequires: dbus-x11 xorg-x11-server-Xvfb
%endif

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: povray%{?_isa}

%description
An advanced molecular editor designed for 
cross-platform use in computational chemistry,
molecular modeling, bioinformatics, materials science,
and related areas, which offers flexible rendering and
a powerful plugin architecture.

%package libs
Summary:        Shared libraries for Avogadro
%description libs
This package contains the shared libraries for the
molecular editor Avogadro.

%package devel
Summary:        Development files for Avogadro
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
This package contains files to develop applications using 
Avogadro libraries.

%package i18n
Summary:        Language packs for Avogadro
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description i18n
Language packs for Avogadro.

%prep
%autosetup -n %{name}-%{version} -p1

#Fix permissions
find . -type f -name "*.h" -exec chmod 0644 '{}' \;
find . -type f -name "*.cc" -exec chmod 0644 '{}' \;
find . -type f -name "*.c" -exec chmod 0644 '{}' \;

sed -e 's|@LIB_INSTALL_DIR@|lib@LIB_SUFFIX@|g' -i avogadro.pc.in

%build
mkdir build && pushd build
export LDFLAGS="%{__global_ldflags} -lm"
export CXXFLAGS="%{optflags} -Wno-cpp -I../libavogadro/src"
%cmake -DCMAKE_BUILD_TYPE:STRING=Release \
  -Wno-dev -Wno-cpp \
  -DENABLE_GLSL:BOOL=ON \
  -DENABLE_PYTHON:BOOL=OFF  \
  -DENABLE_RPATH:BOOL=ON \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=NO \
  -DCMAKE_SKIP_RPATH:BOOL=NO \
  -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="$LDFLAGS" \
  -DENABLE_VERSIONED_PLUGIN_DIR:BOOL=OFF \
  -DLIB_INSTALL_DIR:STRING=%{_libdir} \
  -D18N_INSTALL_DIR:STRING=share/avogadro/i18n \
  -DAvogadro_PLUGIN_INSTALL_DIR:STRING=%{_lib}/avogadro/plugins \
  -DINSTALL_LIB_DIR:STRING=%{_lib}/avogadro \
  -DAvogadro_STATIC_PLUGINS:STRING="bsdyengine;navigatetool;elementcolor" \
  -DENABLE_THREADEDGL:BOOL=ON \
  -DINSTALL_CMAKE_DIR:PATH=%{_lib}/libmsym/cmake ..
popd
%make_build -C build


%install
%make_install -C build

# Install/check appdata file.
install -pm 644 -D %{SOURCE1} \
                     %{buildroot}%{_metainfodir}/avogadro.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
#

rm -rf %{buildroot}%{_datadir}/libavogadro/*.rpmmoved

%find_lang libavogadro --with-qt --without-mo
%find_lang avogadro --with-qt --without-mo

%check
# Version key is wrong and useless
desktop-file-edit --remove-key=Version --remove-category=Education %{buildroot}%{_datadir}/applications/avogadro.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/avogadro.desktop

%ldconfig_scriptlets libs

## Replacement of directories with symlinks
## https://fedoraproject.org/wiki/Packaging:Scriptlets?rd=Packaging:ScriptletSnippets#The_.25pretrans_Scriptlet
## https://fedoraproject.org/wiki/Packaging:Directory_Replacement 
%pretrans libs -p <lua>
print("Replacement of out position directories with symlinks to the python's directories")
path = "/usr/share/libavogadro/extensionScripts"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end
path = "/usr/share/libavogadro/engineScripts"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end

%files -f avogadro.lang
%{_bindir}/avogadro
%{_bindir}/avopkg
%{_bindir}/qube
%dir %{_datadir}/avogadro
%{_datadir}/avogadro/builder/
%{_datadir}/avogadro/crystals/
%{_datadir}/avogadro/fragments/
%{_datadir}/pixmaps/avogadro-icon.png
%{_datadir}/applications/avogadro.desktop
%{_metainfodir}/avogadro.appdata.xml
%{_mandir}/man1/avogadro.1*
%{_mandir}/man1/avopkg.1*

%files devel
%{_includedir}/avogadro/
%{_includedir}/libmsym/
%{_libdir}/libavogadro.so
%{_libdir}/libavogadro_OpenQube.so
%{_libdir}/pkgconfig/avogadro.pc
%{_libdir}/avogadro/*.cmake
%{_libdir}/avogadro/cmake/
%{_libdir}/libmsym/cmake/
%{_qt4_prefix}/mkspecs/features/avogadro.prf

%files libs -f libavogadro.lang
%doc AUTHORS README
%license COPYING
%{_datadir}/libavogadro/
%{_libdir}/libavogadro.so.1*
%{_libdir}/libavogadro_OpenQube.so.0*
%{_libdir}/avogadro/

%files i18n
%dir %{_datadir}/avogadro
%{_datadir}/avogadro/i18n/

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.2.0-30
- Remove SIP dependency (Python enterely disabled)

* Sun Jan 19 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.2.0-29
- Remove explicit sip-api requirement

* Fri Nov 15 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.2.0-28
- Fix desktop file's categories
- Remove rpmmoved files

* Fri Nov 15 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.2.0-27
- Remove all Python2 references

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.2.0-25
- Add more specific CMake variables
- Add two patches from upstream

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 27 2019 Jonathan Wakely <jwakely@redhat.com> - 1.2.0-23
- Rebuilt for Boost 1.69

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 1.2.0-22
- Rebuilt for Boost 1.69

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-21
- Rebuilt for glew 2.1.0

* Sat Aug 04 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.2.0-20
- Replacement of out-position directories with symlinks to the python's directories via scriptlet

* Wed Aug 01 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.2.0-19
- Install Python modules in python_sitearch

* Thu Jul 19 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.2.0-18
- Add 'povray' dependency (bz#1556808)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 01 2018 Jonathan Wakely <jwakely@redhat.com> - 1.2.0-16
- Add BuildRequires: boost-python2-devel

* Thu Feb 15 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.2.0-15
- Use %%ldconfig_scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 1.2.0-13
- Rebuilt for Boost 1.66

* Wed Jan 03 2018 Sandro Mani <manisandro@gmail.com> - 1.2.0-12
* Build against eigen3

* Wed Dec 20 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.2.0-11
- Appdata file moved into metainfo data directory

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 1.2.0-8
- Rebuilt for Boost 1.64

* Wed Jul 05 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.2.0-7
- rebuild (sip)

* Tue Feb 07 2017 Kalev Lember <klember@redhat.com> - 1.2.0-6
- Rebuilt for Boost 1.63

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 1.2.0-5
- Rebuild for glew 2.0.0

* Sun Jan 01 2017 Rex Dieter <rdieter@math.unl.edu> - 1.2.0-4
- rebuild (sip)

* Thu Dec 22 2016 Sandro Mani <manisandro@gmail.com> - 1.2.0-3
- Build against eigen2 (upstream does not support eigen3 >= 3.3.0)

* Fri Oct 14 2016 Dominik Mierzejewski <rpm@greysector.net> - 1.2.0-2
- rebuild for openbabel-2.4.1

* Tue Sep 27 2016 Antonio Trande <sagitter@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0 (bz#1347064) (bz#1347416)
- Make an i18n sub-package
- Patches updated
- Install an appdata file

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-19
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Feb 20 2016 Dominik Mierzejewski <rpm@greysector.net> - 1.1.1-18
- Rebuild for openbabel
- Fix build (gcc-6/Qt?)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 1.1.1-16
- Rebuild for glew 1.13

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.1.1-15
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.1.1-13
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 16 2015 Rex Dieter <rdieter@fedoraproject.org> 1.1.1-11
- rebuild (gcc5)

* Sun Mar 29 2015 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.1.1-10
- apply OpenMandriva patch to fix Eigen3 support
- build against Eigen3: change BuildRequires, pkgconfig_eigen patch

* Wed Mar 25 2015 Rex Dieter <rdieter@fedoraproject.org> 1.1.1-9
- rebuild (gcc5)

* Wed Feb 25 2015 Rex Dieter <rdieter@fedoraproject.org> 1.1.1-8
- rebuild (gcc5)

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.1.1-7
- Rebuild for boost 1.57.0

* Mon Sep 22 2014 Rex Dieter <rdieter@fedoraproject.org> 1.1.1-6
- pull in upstream fix for qreal/arm issues

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.1.1-3
- Rebuild for boost 1.55.0

* Sun Mar 16 2014 Rex Dieter <rdieter@fedoraproject.org> 1.1.1-2
- rebuild(sip)

* Sat Jan 25 2014 Rex Dieter <rdieter@fedoraproject.org> 1.1.1-1
- avogadro-1.1.1
- ExcludeArch: arm

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 1.0.3-21
- rebuilt for GLEW 1.10

* Wed Oct 16 2013 Rex Dieter <rdieter@fedoraproject.org> 1.0.3-20
- rebuild (sip)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 1.0.3-18
- Rebuild for boost 1.54.0

* Mon Jun 17 2013 Rex Dieter <rdieter@fedoraproject.org> 1.0.3-17
- rebuild (sip)

* Mon Feb 11 2013 Rex Dieter <rdieter@fedoraproject.org> 1.0.3-16
- drop boost patch, qt/moc has workaround now

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.0.3-15
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.0.3-14.1
- Rebuild for Boost-1.53.0

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 1.0.3-13.1
- Rebuild for glew 1.9.0

* Mon Oct 01 2012 Rex Dieter <rdieter@fedoraproject.org> 1.0.3-12
- rebuild (sip)

* Thu Aug 09 2012 Rex Dieter <rdieter@fedoraproject.org> - 1.0.3-11
- rebuild (boost)

* Fri Jul 27 2012 Rex Dieter <rdieter@fedoraproject.org> - 1.0.3-10
- rebuild (glew)
- pkgconfig-style deps

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-8
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 23 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.3-6
- rebuild (sip/PyQt4)

* Tue Nov 22 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.3-5
- Rebuild for boost 1.48

* Thu Jul 21 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.3-4
- rebuild (boost)

* Mon Jun 20 2011 ajax@redhat.com - 1.0.3-3
- Rebuild for new glew soname

* Wed Apr 27 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.0.3-2
- remove -Wl,-s from the compiler flags, fixes -debuginfo (#700080)

* Tue Apr 26 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.0.3-1
- update to 1.0.3
- drop all patches (fixed upstream)
- fix qmake mkspecs installation directory (broken in 1.0.3)

* Fri Apr 08 2011 Jaroslav Reznik <jreznik@redhat.com> - 1.0.1-15
- rebuild for new boost (1.46.1)

* Tue Mar 22 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.0.1-14
- fix forcefield extension with OpenBabel 2.3.0 (#680292, upstream patch)
- fix autooptimization tool with OpenBabel 2.3.0 (#680292, patch by lg)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Thomas Spura <tomspur@fedoraproject.org> - 1.0.1-12
- rebuild for new boost

* Thu Nov 25 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.0.1-11
- rebuild for new openbabel (2.3.0)

* Tue Nov 23 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.0.1-10
- fix crash with current SIP and Python 2.7 (#642248)

* Wed Sep 29 2010 jkeating - 1.0.1-9
- Rebuilt for gcc bug 634757

* Tue Sep 14 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.0.1-8
- fix FTBFS with SIP 4.11 (Gentoo#335644)

* Thu Sep 09 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.0.1-7
- rebuild(sip)

* Sun Aug 22 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.0.1-6
- -devel: Requires: glew-devel python-devel boost-devel

* Sun Aug 22 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.0.1-5
- use CMAKE_SKIP_RPATH because we end up with rpaths otherwise
- disable tests because they don't work in Koji anyway

* Sun Aug 22 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.0.1-4
- fix paths in AvogadroConfig.cmake
- fix packaging of translations

* Wed Aug 04 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 1.0.1-3
- Rebuild for Boost soname bump

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon May 24 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.0.1-1
- avogadro-1.0.1
- -devel: move cmake-related files here
- -devel: Req: qt4-devel
- %%files: track lib sonames
- %%check section

* Wed Feb 10 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.0.0-6
- reenable plugin builds and libs subpackage
- fix their build with sip 4.10

* Fri Jan 08 2010 Sebastian Dziallas <sebastian@when.com> - 1.0.0-5
- disable plugin builds and libs subpackage

* Thu Jan 07 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-4
- rebuild (sip)

* Mon Nov 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-3 
- rebuild (for qt-4.6.0-rc1, f13+)

* Mon Nov 16 2009 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-2 
- -libs: Requires: sip-api(%%_sip_api_major) >= %%_sip_api (#538124)
- Requires: %%{name}-libs ...

* Thu Oct 29 2009 Sebastian Dziallas <sebastian@when.com> 1.0.0-1
- update to new upstream release

* Tue Oct 20 2009 Rex Dieter <rdieter@fedoraproject.org> 0.9.8-3 
- rebuild (eigen2)

* Sat Sep 26 2009 Sebastian Dziallas <sebastian@when.com> 0.9.8-2
- fix typo in file list

* Sat Sep 26 2009 Sebastian Dziallas <sebastian@when.com> 0.9.8-1
- update to new upstream release
- enable python and glsl support again

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 06 2009 Sebastian Dziallas <sebastian@when.com> 0.9.6-1
- new upstream release to fix issue with qt 4.5.0 and earlier

* Wed Jun 03 2009 Sebastian Dziallas <sebastian@when.com> 0.9.5-3
- remove remaining python parts
- fix files section finally

* Wed Jun 03 2009 Sebastian Dziallas <sebastian@when.com> 0.9.5-2
- disable python and glsl for now
- fix files section

* Wed Jun 03 2009 Sebastian Dziallas <sebastian@when.com> 0.9.5-1
- update to new release

* Tue May 12 2009 Sebastian Dziallas <sebastian@when.com> 0.9.4-1
- update to new release

* Fri Apr 10 2009 Sebastian Dziallas <sebastian@when.com> 0.9.3-1
- update to new release

* Sat Mar 21 2009 Sebastian Dziallas <sebastian@when.com> 0.9.2-2
- get desktop file properly installed

* Sat Mar 14 2009 Sebastian Dziallas <sebastian@when.com> 0.9.2-1
- update to new release

* Wed Feb 25 2009 Sebastian Dziallas <sebastian@when.com> 0.9.1-1
- update to new release

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 22 2009 Sebastian Dziallas <sebastian@when.com> 0.9.0-1
- update to new release

* Sun Sep 14 2008 Sebastian Dziallas <sebastian@when.com> 0.8.1-6
- add handbook to docs

* Sun Sep 14 2008 Sebastian Dziallas <sebastian@when.com> 0.8.1-5
- add build requirements and fix group names

* Wed Aug 13 2008 Sebastian Dziallas <sebastian@when.com> 0.8.1-4
- fix typos

* Sat Aug  9 2008 Sebastian Dziallas <sebastian@when.com> 0.8.1-3
- reorganize spec file

* Sat Aug  9 2008 Sebastian Dziallas <sebastian@when.com> 0.8.1-2
- rename shared library package and structure spec file

* Sun Aug  3 2008 Sebastian Dziallas <sebastian@when.com> 0.8.1-1
- initial pacakging release based on PackMan release

