Summary: Macromolecular coordinate superposition library
Name: ssm
Version: 1.4
Release: 12%{?dist}
License: LGPLv3
URL: ftp://ftp.ccp4.ac.uk/opensource/
Source0: ftp://ftp.ccp4.ac.uk/opensource/%{name}-%{version}.tar.gz
Patch0: ssm-configure.ac.patch
Patch1: ssm-makefile.am.patch
BuildRequires:  gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: mmdb2-devel
BuildRequires: libccp4-devel

%description
SSM is a macromolecular coordinate superposition library, written by 
Eugene Krissinel.

The library implements the SSM algorithm of protein structure
comparison in three dimensions, which includes an original procedure
of matching graphs built on the protein's secondary-structure
elements, followed by an iterative three-dimensional alignment of
protein backbone Calpha atoms. 

The algorithm implemented by the software is described in:
E. Krissinel & K. Henrick (2004) Secondary-structure matching (SSM), a
new tool for fast protein structure alignment in three dimensions.
Acta Crystallogr D Biol Crystallogr. 60, 2256-68.

This package contains the shared library components needed for programs
that have been compiled with the ssm library. 

%package devel
Summary: Header files and library for developing programs with ssm
Requires: %{name} = %{version}-%{release}
Requires: mmdb2-devel
Requires: pkgconfig

%description devel
This package contains libraries and header files needed for program
development using SSM.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
aclocal
libtoolize --automake --copy
autoconf
automake --copy --add-missing --gnu

%build
%configure --enable-shared --disable-static --enable-ccp4
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'

# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING.LESSER
%{_bindir}/superpose
%{_libdir}/libssm.so.2.0.0
%{_libdir}/libssm.so.2

%files devel
%{_libdir}/libssm.so
%{_includedir}/ssm/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.4-2
- Rebuilt for GCC 5 C++11 ABI change

* Sun Jan 18 2015 Tim Fenn <tim.fenn@gmail.com> - 1.4-1
- update to 1.4

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 20 2013 Tim Fenn <tim.fenn@gmail.com> - 1.3-1
- update to 1.3
- update to new upstream URL

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Feb 25 2011 Tim Fenn <fenn@stanford.edu> - 1.1-2
- include patches

* Fri Feb 25 2011 Tim Fenn <fenn@stanford.edu> - 1.1-1
- update to 1.1
- update download locations

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 19 2009 Tim Fenn <fenn@stanford.edu> - 1.0-1
- update to 1.0

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 22 2008 Tim Fenn <fenn@stanford.edu> - 0.1-11
- fix libtoolize

* Sat Nov 22 2008 Tim Fenn <fenn@stanford.edu> - 0.1-10
- update to reflect mmdb changes

* Mon Nov 10 2008 Tim Fenn <fenn@stanford.edu> - 0.1-9
- include makefile patch to correspond with configure patch
- fix license tag
- fix buildrequires (add mmdb-devel)
- fix configure/make install
- docs only in main package

* Sat Oct 25 2008 Tim Fenn <fenn@stanford.edu> - 0.1-8
- change name libssm to ssm
- add smp make macro
- fix buildrequires

* Thu May 29 2008 Tim Fenn <fenn@stanford.edu> - 0.1-7
- fix Requires, post, postun

* Wed May 28 2008 Tim Fenn <fenn@stanford.edu> - 0.1-6
- fix ldconfig, requires, buildroot, naming scheme

* Tue May 27 2008 Tim Fenn <fenn@stanford.edu> - 0.1-5
- remove static libs

* Mon May 26 2008 Tim Fenn <fenn@stanford.edu> - 0.1-4
- spec cleanup

* Tue Feb 26 2008 Tim Fenn <fenn@stanford.edu> - 0.1-3
- update using fedora packaging conventions

* Sun Sep 02 2007 Morten Kjeldgaard <mok@bioxray.dk> - 0.1
- Spec file part of ssm distro, split devel files and shared library 
  into separate packages.

####
