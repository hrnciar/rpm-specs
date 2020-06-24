%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

# snapshot hg hash
%global snap 3ad14141c027

Name:           ogre-pagedgeometry
Epoch:          1
Version:        1.1.4
Release:        14.20131226hg%{snap}%{?dist}
Summary:        Ogre addon for realtime rendering of dense forests
License:        zlib
URL:            https://code.google.com/p/ogre-paged/
# Source is obtained by:
# hg clone https://code.google.com/p/ogre-paged-latest/
# cd ogre-paged-https://code.google.com/p/ogre-paged/latest
# hg archive ogre-pagedgeometry-hg3ad14141c027.tgz
# This includes a handful of post 1.1.4 fixes, mostly to get things
# to work with more recent versions of Ogre.
# Note that patches from https://code.google.com/p/ogre-paged-latest/
# haven't been brought back to https://code.google.com/p/ogre-paged/ but
# nothing has been added to https://code.google.com/p/ogre-paged/ since
# the fork.
Source0:        ogre-pagedgeometry-hg%{snap}.tgz
Patch0:         pagedgeometry-no-force-static.patch
# Examples 9, 10 and 11 don't build with Ogre 1.9 and since we aren't packaging
# the examples anyway, it's easiest to just skip them.
Patch1:         skip-ex.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ogre-devel
# For examples we aren't packaging (yet - need to use GLSL instead of Cg)
# If fixed a requires for ois and libX11 will be needed.
BuildRequires:  ois-devel
BuildRequires:  libX11-devel

Requires: ogre
# The library gets placed in a directory owned by ogre, but that dependency
# should be built automatically based on needed libraries.

%description
Real-time rendering of massive, dense forests, with not only trees, but 
bushes, grass, rocks, and other "clutter". Supports dynamic transitioned 
LOD between batched geometry and static impostors (extendable). 

%package        devel
Summary:        Development files for PagegGeometry
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    devel
The ogre-addons-pagedgeometry-devel package contains libraries and header 
files for developing applications that use the PagedGeometry OGRE Add-On.

%ifarch %{ix86}
%package        sse2
Summary:        Ogre addon for realtime rendering of dense forests using sse2 instructions
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    sse2
Real-time rendering of massive, dense forests, with not only trees, but 
bushes, grass, rocks, and other "clutter". Supports dynamic transitioned 
LOD between batched geometry and static impostors (extendable). sse2
instructions are enabled.
%endif

%prep
%setup -q -n ogre-pagedgeometry-hg%{snap}
%patch0 -p1 -b .shared
%patch1 -p0 -b .skip-ex
for file in GettingStarted.txt Todo.txt ; do
   mv $file timestamp && \
   iconv -f WINDOWS-1252 -t UTF-8 -o $file timestamp && \
   touch -r timestamp $file && \
   rm timestamp
done
mkdir build
mkdir sse2

%build
pushd build
  %cmake -DCMAKE_CXX_FLAGS_RELWITHDEBINFO:STRING= -DCMAKE_C_FLAGS_RELWITHDEBINFO:STRING= .. 
  # Builds out of order with _smp_mflags
  make VERBOSE=1
  mkdir lib
  mv ../lib/libPagedGeometry.so lib/
popd

# For x86 build a separate sse2 library that will be autodetected at runtime
%ifarch %{ix86}
pushd sse2
  %cmake -DCMAKE_CXX_FLAGS_RELWITHDEBINFO:STRING=-msse2 -DCMAKE_C_FLAGS_RELWITHDEBINFO:STRING=-msse2 ..
  make VERBOSE=1 %{?_smp_mflags}
  mkdir lib
  mv ../lib/libPagedGeometry.so lib/
popd
%endif


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_includedir}/OGRE/PagedGeometry
cp -a include/* %{buildroot}%{_includedir}/OGRE/PagedGeometry
rm -f %{buildroot}%{_includedir}/OGRE/PagedGeometry/PagedGeometryConfig.h.in
cp -p build/include/* %{buildroot}%{_includedir}/OGRE/PagedGeometry
mkdir -p %{buildroot}%{_libdir}/OGRE
cp -p build/lib/libPagedGeometry.so %{buildroot}%{_libdir}/OGRE/
mkdir -p %{buildroot}%{_pkgdocdir}
cp -p GettingStarted.txt Todo.txt docs/*.odt %{buildroot}%{_pkgdocdir}
%ifarch %{ix86}
mkdir -p %{buildroot}%{_libdir}/sse2/OGRE
cp -p sse2/lib/libPagedGeometry.so %{buildroot}%{_libdir}/sse2/OGRE/
%endif

# Note: The examples are now being built by default, but they're pretty worthless without cg.
# So... I didn't package them. ~spot (21-Dec-2010)

%files
%{_libdir}/OGRE/libPagedGeometry.so

%ifarch %{ix86}
%files sse2
# Ogre doesn't do sse2 builds so doesn't own an sse2/OGRE directory
%{_libdir}/sse2/OGRE
%{_libdir}/sse2/OGRE/libPagedGeometry.so
%endif


%files devel
%doc %{_pkgdocdir}
%{_includedir}/OGRE/PagedGeometry

%ldconfig_scriptlets

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.4-14.20131226hg3ad14141c027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.4-13.20131226hg3ad14141c027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.4-12.20131226hg3ad14141c027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.4-11.20131226hg3ad14141c027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.4-10.20131226hg3ad14141c027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.4-9.20131226hg3ad14141c027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.4-8.20131226hg3ad14141c027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.4-7.20131226hg3ad14141c027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.4-6.20131226hg3ad14141c027
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 12 2015 Bruno Wolff III <bruno@wolff.to> - 1:1.1.4-5.20131226hg3ad14141c027
- Get updates for building with Ogre 1.9

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1:1.1.4-1
- 1.1.4 upstream release
- Cleanup spec

* Sun May 25 2014 Petr Machata <pmachata@redhat.com> - 1:1.1.0-12
- Rebuild for boost 1.55.0

* Sun Nov  3 2013 Ville Skyttä <ville.skytta@iki.fi> - 1:1.1.0-11
- Install docs to %%{_pkgdocdir} where available (#993998).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 10 2012 Bruno Wolff III <bruno@wolff.to> - 1:1.1.0-8
- Rebuild for ogre 1.8.1

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 05 2012 Bruno Wolff III <bruno@wolff.to> - 1:1.1.0-6
- Fix for bz 771772 PagedGeometryConfig.h was not included

* Sun May 15 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.0-5
- Rebuild for ogre 1.7.3

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 15 2011 Bruno Wolff III <bruno@wolff.to> - 1.1.0-3
- Self references need to use the epoch.

* Sat Jan 15 2011 Bruno Wolff III <bruno@wolff.to> - 1.1.0-2
- It turns out 1.1 < 1.05 so we need an epoch bump

* Tue Dec 21 2010 Tom Callaway <spot@fedoraproject.org> - 1.1.0-1
- update to 1.1.0

* Sat Nov 07 2009 Bruno Wolff III <bruno@wolff.to> - 1.05-4.2721svn
- Remove unnecessary option to cmake to request shared library build

* Fri Nov 06 2009 Bruno Wolff III <bruno@wolff.ro> - 1.05-3.2721svn
- Properly capitalize the include directory name
- The pkgconfig file isn't being installed so requires isn't needed

* Sun Nov 01 2009 Bruno Wolff III <bruno@wolff.ro> - 1.05-2.2721svn
- Bruno will take over as primary maintainer
- Switch to the latest svn to pick up some bug fixes
- Build an alternate sse2 library
- Keep cmake from adding compiler flags based on build type
- Keep cmake from adding -msse for gcc builds no matter the target
- Keep cmake from forcing a static library (this is very likely an upstream bug)

* Tue Sep 29 2009 Guido Grazioli <guido.grazioli@gmail.com> - 0-1.2698svn
- Initial packaging
