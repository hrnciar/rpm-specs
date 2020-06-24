# The timestamp on files inside the archive
%global release_date 1441092191

Name:           bliss
Version:        0.73
Release:        10%{?dist}
Summary:        Compute automorphism groups and canonical labelings of graphs

License:        LGPLv3
URL:            http://www.tcs.hut.fi/Software/bliss/
Source0:        http://www.tcs.hut.fi/Software/bliss/%{name}-%{version}.zip
# Man page written by Jerry James using text borrowed from the sources.
# The man page therefore has the same copyright and license as the sources.
Source1:        bliss.1
# Sent upstream 28 Oct 2011.  Don't call exit() in library code.
Patch0:         bliss-error.patch
# Patch from Thomas Rehn, also sent upstream.  Fix one bug and add one
# performance enhancement.
Patch1:         bliss-rehn.patch

BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%global sover %(echo %{version} | cut -d. -f1)

%description
Bliss is an open source tool for computing automorphism groups and
canonical forms of graphs.  It has both a command line user interface as
well as C++ and C programming language APIs. 

%package devel
Summary:        Headers and library files for developing with bliss
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}
Provides:       bundled(jquery)

%description devel
Headers and library files needed to develop applications that use the
bliss library.

%package libs
Summary:        Compute automorphism groups and canonical labelings of graphs

%description libs
A command-line bliss tool to access the functionality of the bliss
library.

%prep
%setup -q
%patch0
%patch1

%build
# The Makefile creates a static library, so we roll our own shared library
# here instead.  Also, avoid an unused direct dependency on libm.
g++ $RPM_OPT_FLAGS -DBLISS_USE_GMP -DSOURCE_DATE_EPOCH=%release_date -fPIC \
  -shared -o libbliss.so.%{version} -Wl,-soname,libbliss.so.%{sover} defs.cc \
  graph.cc partition.cc orbit.cc uintseqhash.cc heap.cc timer.cc utils.cc \
  bliss_C.cc -Wl,--as-needed $RPM_LD_FLAGS -lgmp
ln -s libbliss.so.%{version} libbliss.so.%{sover}
ln -s libbliss.so.%{sover} libbliss.so

# The Makefile doesn't know how to link the binary against a shared library.
# Also, once again avoid an unused direct dependency on libm.
g++ $RPM_OPT_FLAGS -DBLISS_USE_GMP -DSOURCE_DATE_EPOCH=%release_date -o bliss \
  bliss.cc -Wl,--as-needed $RPM_LD_FLAGS -L. -lbliss -lgmp

# Build the documentation
doxygen

%install
# The Makefile has no install target.

# Install the library
mkdir -p %{buildroot}%{_libdir}
cp -a libbliss.* %{buildroot}%{_libdir}

# Install the header files
mkdir -p %{buildroot}%{_includedir}/bliss
cp -p *.h *.hh %{buildroot}%{_includedir}/bliss

# Install the binary
mkdir -p %{buildroot}%{_bindir}
cp -p bliss %{buildroot}%{_bindir}

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
sed 's/@VERSION@/%{version}/' %{SOURCE1} > %{buildroot}%{_mandir}/man1/bliss.1
touch -r %{SOURCE1} %{buildroot}%{_mandir}/man1/bliss.1

%ldconfig_scriptlets libs

%files
%{_bindir}/bliss
%{_mandir}/man1/bliss.1*

%files devel
%doc html
%{_includedir}/bliss
%{_libdir}/libbliss.so

%files libs
%license COPYING COPYING.LESSER
%{_libdir}/libbliss.so.*

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 19 2015 Jerry James <loganjerry@gmail.com> - 0.73-1
- New upstream version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.72-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.72-12
- Rebuilt for GCC 5 C++11 ABI change

* Fri Mar  6 2015 Jerry James <loganjerry@gmail.com> - 0.72-11
- Link with RPM_LD_FLAGS

* Wed Feb 11 2015 Jerry James <loganjerry@gmail.com> - 0.72-10
- Note bundled jquery
- Use license macro

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.72-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.72-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.72-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.72-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.72-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 16 2012 Jerry James <loganjerry@gmail.com> - 0.72-4
- Apply bug fix and performance enhancement patch from Thomas Rehn

* Fri Jan  6 2012 Jerry James <loganjerry@gmail.com> - 0.72-3
- Rebuild for GCC 4.7.

* Tue Nov 15 2011 Jerry James <loganjerry@gmail.com> - 0.72-2
- Add patch to avoid calling exit() in the library

* Wed Jul 20 2011 Jerry James <loganjerry@gmail.com> - 0.72-1
- Initial RPM
