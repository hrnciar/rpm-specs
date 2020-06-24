Name:           meshmagick
Version:        0.6.0
Release:        42.svn2898%{?dist}
Summary:        Command line manipulation tool for Ogre meshes

License:        MIT
URL:            http://www.ogre3d.org/tikiwiki/MeshMagick
# The source for this package was pulled from upstream's svn.  Use the
# following commands to generate the tarball:
#  svn export -r 2898 https://svn.code.sf.net/p/ogreaddons/code/trunk/meshmagick meshmagick
#  tar cjf meshmagick-0.6.0-r2898.tar.bz2 meshmagick
Source0:        %{name}-%{version}-r2898.tar.bz2
Patch0:         meshmagick-version.patch
Patch1:         meshmagick-multilib.patch
# Based on http://www.ogre3d.org/forums/download/file.php?id=5869&sid=127fa0b4be759e78d23b8a5f264a197f
# I needed to strip CRs out of the file to get patch to take it
# Since src/MmOptimiseTool.cpp had CRLF line endings and was affected 
# by this patch, I needed to change them to LF during setup.
Patch2:         meshmagick-ogre19.patch
Patch3:         meshmagick-boost-DSO.patch

BuildRequires:  gcc-c++
BuildRequires:  ogre-devel
BuildRequires:  cmake

%description
MeshMagick is a manipulation tool for Ogre meshes (and skeletons). It
allows the user to query interesting information and to transform binary
meshes (and skeletons) in many ways.


%package        libs
Summary:        Libraries for %{name}

%description    libs
The %{name}-libs package contains libraries that are needed for
running applications that use %{name}.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs = %{version}-%{release} pkgconfig ogre-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}
sed -i "s|\r||g" src/MmOptimiseTool.cpp
%patch0
%patch1
%patch2
%patch3


%build
%cmake . -DSTATIC_BUILD=FALSE -DLIB:STRING=%{_lib} -DCMAKE_SKIP_RPATH=TRUE
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/lib%{name}.la



%ldconfig_scriptlets libs


%files
%doc AUTHORS README LICENSE.txt
%{_bindir}/%{name}

%files libs
%{_libdir}/lib%{name}.so.*

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-42.svn2898
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-41.svn2898
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-40.svn2898
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Jonathan Wakely <jwakely@redhat.com> - 0.6.0-39.svn2898
- Rebuilt for Boost 1.69

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-38.svn2898
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.0-37.svn2898
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-36.svn2898
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-35.svn2898
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-34.svn2898
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 0.6.0-33.svn2898
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-32.svn2898
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Jonathan Wakely <jwakely@redhat.com> - 0.6.0-31.svn2898
- Rebuilt for Boost 1.63

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-30.svn2898
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.6.0-29.svn2898
- Rebuilt for Boost 1.59

* Wed Aug 05 2015 Jonathan Wakely <jwakely@redhat.com> 0.6.0-28.svn2898
- Rebuilt for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-27.svn2898
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 Bruno Wolff III <bruno@wolff.to> - 0.6.0-26.svn2898
- Rebuild against latest Ogre to see if FTBFS issue is resolved

* Tue Feb 10 2015 Bruno Wolff III <bruno@wolff.to> - 0.6.0-25.svn2898
- Rebuild for boost update

* Tue Nov 18 2014 Bruno Wolff III <bruno@wolff.to> - 0.6.0-24.svn2898
- Use sed instead of dos2unix for building

* Sun Nov 16 2014 Bruno Wolff III <bruno@wolff.to> - 0.6.0-23.svn2898
- Apply patch from Ogre forums to get it to build for Ogre 1.9

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-22.svn2898
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 11 2014 Bruno Wolff III <bruno@wolff.to> - 0.6.0-21.svn2898
- Rebuild for Ogre 1.9

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-20.svn2898
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 0.6.0-19.svn2898
- rebuild for boost 1.55.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-18.svn2898
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Petr Machata <pmachata@redhat.com> - 0.6.0-17.svn2898
- Rebuild for boost 1.54.0
- Drop -mt from boost_system-mt (meshmagick-boost-DSO.patch)

* Sun Feb 24 2013 Bruno Wolff III <bruno@wolff.to> - 0.6.0-16.svn2898
- Fix ogre / boost_system-mt DSO issue with a bigger hammer

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-15.svn2898
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 09 2012 Bruno Wolff III <bruno@wolff.to> - 0.6.0-14.svn2898
- Rebuild for Ogre 1.8
- Adjust for ms_Singleton to msSingleton function name change

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-13.svn2898
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 01 2012 Bruno Wolff III <bruno@wolff.to> - 0.6.0-12.svn2898
- Rebuild for ogre 1.7.4

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-11.svn2898
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-10.svn2898
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun May 15 2011 Bruno Wolff III <bruno@wolff.to> - 0.6.0-9.svn2898
- Rebuild for ogre 1.7.3

* Sun Mar 06 2011 Bruno Wolff III <bruno@wolff.to> - 0.6.0-8.svn2898
- I think I finally have the multilib stuff fixed.
- The license has changed to MIT.

* Sun Feb 20 2011 Bruno Wolff III <bruno@wolff.to> - 0.6.0-7.svn2898
- Still working on multilib
- Drop buildrequires for autotool stuff

* Sun Feb 20 2011 Bruno Wolff III <bruno@wolff.to> - 0.6.0-6.svn2898
- Still working on multilib

* Sun Feb 20 2011 Bruno Wolff III <bruno@wolff.to> - 0.6.0-5.svn2898
- The libdir fix is a bit trickier than I thought

* Sun Feb 20 2011 Bruno Wolff III <bruno@wolff.to> - 0.6.0-4.svn2898
- Have cmake use %%{_libdir} so multilib works.

* Sun Feb 20 2011 Bruno Wolff III <bruno@wolff.to> - 0.6.0-3.svn2898
- Update for Ogre 1.7
- Switch to using cmake build
- Update library versions to 0.6.0 to match meshmagick version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2.20090529svn2698
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 12 2009 Alexey Torkhov <atorkhov@gmail.com> - 0.6.0-1.20090529svn2698
- Update

* Mon Sep 28 2009 Alexey Torkhov <atorkhov@gmail.com> - 0.5.2-7.20090124svn2618
- Rebuilt for new OGRE

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-6.20090124svn2618
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 06 2009 Alexey Torkhov <atorkhov@gmail.com> - 0.5.2-5.20090124svn2618
- Rebuild for new OGRE

* Wed Mar 04 2009 Alexey Torkhov <atorkhov@gmail.com> - 0.5.2-4.20090124svn2618
- Polishing the Requires

* Wed Mar 04 2009 Alexey Torkhov <atorkhov@gmail.com> - 0.5.2-3.20090124svn2618
- Split shared library to -libs subpackage for correct work in multilib
  environment
- Add patch for generating full debuginfo

* Tue Mar 03 2009 Alexey Torkhov <atorkhov@gmail.com> - 0.5.2-2.20090124svn2618
- Renamed package to simply "meshmagick"
- Clarified commands to get source
- Minor fixes

* Sat Feb 28 2009 Alexey Torkhov <atorkhov@gmail.com> - 0.5.2-1.20090124svn2618
- Update to post 0.5.2

* Mon Nov 03 2008 Alexey Torkhov <atorkhov@gmail.com> - 0.4.0-0.1.20080731svn2488
- Initial package
