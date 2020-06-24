Name:		stxxl
Version:	1.4.1
Release:	12%{?dist}
Summary:	C++ STL drop-in replacement for extremely large data sets 

License:	Boost	
URL:		http://%{name}.sourceforge.net	
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

#Disable static library compilation, enable shared
Patch0: %{name}_%{version}-build_shared.patch
#Fix compilation, where ctime conflichts with sys/time
Patch1: %{name}_%{version}-ctime_conflict.patch
#Fix noexecpt warnings, using upstream commit
Patch2: %{name}_%{version}-6cf18ce60f-fix-noexcept.patch


%description
%{name} provides an STL replacement using an abstraction layer to
storage devices to allow for the optimal layout of data structures. This
allows for multi-terabyte data sets to be held and manipulated in standard
C++ data structures, whilst abstracting the complexity of managing this
behavior efficiently. %{name} utilises multi-disk I/O to speed up
I/O bound calculations. STXXL has been developed at the University
of Karlsruhe.

%package devel
Summary:	Provides development files for %{name} applications
Requires:	%{name} = %{version}-%{release}

%description devel
Development libraries for the %{name} library.

%package doc
Summary:	HTML documentation and tutorial for the %{name} applications

BuildArch:	noarch

BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	cmake, doxygen, graphviz, ghostscript

%description doc
This package contains the documentation in the HTML format of the %{name}
package.

%prep
%setup -q
%patch0
%patch1
%patch2

#Change the install directory for libraries to that 
# required by current arch
LIBVAL=`basename %{_libdir}`
sed -i 's@INSTALL_LIB_DIR "lib"@INSTALL_LIB_DIR "'${LIBVAL}'"@' CMakeLists.txt
sed -i 's@INSTALL_PKGCONFIG_DIR "lib/pkgconfig"@INSTALL_PKGCONFIG_DIR "'${LIBVAL}/pkgconfig'"@' CMakeLists.txt
sed -i 's@DEF_INSTALL_CMAKE_DIR "lib/cmake/stxxl"@DEF_INSTALL_CMAKE_DIR "'${LIBVAL}/cmake/stxxl'"@' CMakeLists.txt

%build
#in-source builds are not allowed, push a dir, then build
mkdir rpm_build
pushd rpm_build

%cmake -DCMAKE_BUILD_TYPE="Release" ..
make %{?_smp_mflags} DESTDIR=/usr/

popd

doxygen .



%install

pushd rpm_build
make install DESTDIR=%{buildroot}
popd

%ldconfig_scriptlets

%files
%license LICENSE_1_0.txt
%doc CHANGELOG TODO README
%{_libdir}/libstxxl.so*

%files devel
%{_includedir}/%{name}.h
%{_includedir}/%{name}/
%{_libdir}/libstxxl.so
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_bindir}/stxxl_tool

%files doc
%doc html/


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 <mycae(at)gmx.com> - 1.4.1-9
- Patch to fix bug #1606432
- Import patch from upstream to fix noexcept warnings

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 1.4.1-7
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 17 2017 Ville Skyttä <ville.skytta@iki.fi> - 1.4.1-2
- Use %%cmake macro, fixes -debuginfo
- Ship LICENSE* as %%license

* Sun Feb 12 2017 <mycae(at)gmx.com> - 1.4.1-1
- Update to upstream 1.4.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.1-5
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 24 2013 <mycae(a!t)gmx.com> 1.3.1-1
- Update to upstream 1.3.1

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-12
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun  3 2009 <denis.arnaud_fedora@m4x.org> 1.2.1-8
- Added a tab in the 'BuildArch:<tab>noarch' directive.

* Mon Jun  1 2009 <denis.arnaud_fedora@m4x.org> 1.2.1-7
- Enclosed the 'BuildArch: noarch' directive within F>=10 condition

* Sun May 31 2009 <denis.arnaud_fedora@m4x.org> 1.2.1-6
- Applied https://bugzilla.redhat.com/show_bug.cgi?id=474787#c12
  recommendations

* Thu May 28 2009 <mycae(a!t)yahoo.com> 1.2.1-5
- Re-enable documentation using suggested macros

* Sun May 24 2009 <mycae(a!t)yahoo.com> 1.2.1-4
- Used doc macro to install docs previously manually installed
- Added README and TROUBLESHOOTING to docs
- Added otpflags macro to build settings
- Use "install" program rather than cp for the install of lib

* Wed Jan 14 2009 <mycae(a!t)yahoo.com> 1.2.1-3
- Fixed devel summary to be concise
- Fixed Requires for devel subpackage, now requires stxxl
- Changed devel description to be unique from main
- Added defattr into devel package
- Fixed unowned dirs in subpackage

* Sat Dec 06 2008 <mycae(a!t)yahoo.com> 1.2.1-2
- Removed latex build & buildrequires
- Patched makefiles to provide shared instead of static libs
- made doxygen log to file, due to excessively verbose output

* Fri Dec 05 2008 <mycae(a!t)yahoo.com> 1.2.1-1
- Create spec file 

