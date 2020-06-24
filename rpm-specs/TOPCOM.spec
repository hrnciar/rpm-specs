Name:           TOPCOM
Version:        0.17.8
Release:        11%{?dist}
Summary:        Triangulations Of Point Configurations and Oriented Matroids

License:        GPLv2+
URL:            http://www.rambau.wm.uni-bayreuth.de/TOPCOM/
Source0:        http://www.rambau.wm.uni-bayreuth.de/Software/%{name}-%{version}.tar.gz
# Man pages, written by Jerry James using text from the sources.  Therefore,
# these man pages have the same copyright and license as the sources.
Source1:        %{name}-man.tar.xz
# A replacement Makefile.  See the %%build section for more information.
Source2:        %{name}-Makefile

BuildRequires:  cddlib-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%global topcom_major $(echo %{version} | cut -d. -f1)
%global topcom_minor $(echo %{version} | cut -d. -f2)

%description
TOPCOM is a package for computing Triangulations Of Point Configurations
and Oriented Matroids.  It was very much inspired by the maple program
PUNTOS, which was written by Jesus de Loera.  TOPCOM is entirely written
in C++, so there is a significant speed up compared to PUNTOS.

%package devel
Summary:        Header files needed to build with %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       cddlib-devel%{?_isa}
Requires:       gmp-devel%{?_isa}

%description devel
Header files needed to build applications that use the %{name} library.

%package libs
Summary:        Core %{name} functionality in a library

%description libs
Command line tools that expose %{name} library functionality.

%package examples
Summary:        Example inputs and outputs for TOPCOM
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description examples
Example input and output files for TOPCOM.

%prep
%setup -q -n topcom-%{version}
%setup -q -n topcom-%{version} -T -D -a 1

# Fix character encoding
iconv -f iso8859-1 -t utf8 -o README.utf8 README
touch -r README README.utf8
mv -f README.utf8 README

# Mimic upstream's modification of gmpxx.h, using the system gmpxx.h
mkdir -p external/include
sed "s|// \(q\.canonicalize\)|\1|" %{_includedir}/gmpxx.h > \
  external/include/gmpxx.h

%build
# We cannot use upstream's build system.  It has the following problems.
# (1) It builds two static libraries, libTOPCOM.a and libCHECKREG.a, then
#     includes both libraries in each of the 38 binaries that it installs in
#     %%{_bindir}.
# (2) Each of libTOPCOM.a and libCHECKREG.a refers to symbols defined by the
#     other.
# (3) It builds static gmp and cddlib libraries, which are also linked into
#     all of the constructed binaries.  There is no way to make it use the
#     installed versions of those libraries instead.
# We could fix (3) with a little build system hackery.  We could fix (1) by
# building shared libraries, but that doesn't help with (2).  Instead, we pull
# in our own evilly constructed Makefile to build a single shared library
# containing all of the object files in both libTOPCOM.a and libCHECKREG.a,
# and link the binaries against that and the system gmp and cddlib libraries.
sed -e "s|@RPM_OPT_FLAGS@|${RPM_OPT_FLAGS}|" \
    -e "s|@RPM_LD_FLAGS@|${RPM_LD_FLAGS}|" \
    -e "s|@bindir@|%{_bindir}|" \
    -e "s|@libdir@|%{_libdir}|" \
    -e "s|@mandir@|%{_mandir}|" \
    -e "s|@includedir@|%{_includedir}|" \
    -e "s|@version@|%{version}|" \
    -e "s|@major@|%{topcom_major}|" \
    -e "s|@minor@|%{topcom_minor}|" \
    -e "s|#version#|@version@|" \
    %{SOURCE2} > Makefile
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

# Get rid of the Makefiles in the examples dir before packaging
rm -f examples/Makefile*

# Rename binaries with common names
for bin in cross cube cyclic hypersimplex lattice; do
  mv $RPM_BUILD_ROOT%{_bindir}/$bin $RPM_BUILD_ROOT%{_bindir}/TOPCOM-$bin
done

%ldconfig_scriptlets libs

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man7/*

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so

%files libs
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/*.so.*

%files examples
%doc examples

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 13 2018 Jerry James <loganjerry@gmail.com> - 0.17.8-8
- Rebuild for cddlib 0.94j

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 28 2017 Jerry James <loganjerry@gmail.com> - 0.17.8-5
- Rebuild for cddlib

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 28 2016 Jerry James <loganjerry@gmail.com> - 0.17.8-1
- New upstream release

* Wed Jul 13 2016 Jerry James <loganjerry@gmail.com> - 0.17.7-1
- New upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Jerry James <loganjerry@gmail.com> - 0.17.6-2
- Rename some binaries (bz 1297088)

* Thu Oct 15 2015 Jerry James <loganjerry@gmail.com> - 0.17.6-1
- New upstream release

* Wed Sep 16 2015 Jerry James <loganjerry@gmail.com> - 0.17.5-4
- Link with RPM_LD_FLAGS

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.17.5-2
- Rebuilt for GCC 5 C++11 ABI change

* Thu Jan  8 2015 Jerry James <loganjerry@gmail.com> - 0.17.5-1
- New upstream release
- Use license macro

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep  3 2013 Jerry James <loganjerry@gmail.com> - 0.17.4-4
- Split examples into a noarch subpackage, due to their size

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug  8 2012 Jerry James <loganjerry@gmail.com> - 0.17.4-1
- New upstream release
- Drop upstreamed GCC 4.7 patch
- Adapt to upstream modification of gmpxx.h
- Move man page installation to the Makefile

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 29 2012 Jerry James <loganjerry@gmail.com> - 0.17.1-3
- Preserve timestamps when installing
- Move most of the doc files to the -libs subpackage

* Wed Mar 28 2012 Jerry James <loganjerry@gmail.com> - 0.17.1-2
- Fix build failure due to restricted C++ lookups in GCC 4.7

* Tue Oct 18 2011 Jerry James <loganjerry@gmail.com> - 0.17.1-1
- Initial RPM
