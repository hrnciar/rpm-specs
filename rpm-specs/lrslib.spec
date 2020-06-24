# TODO: Package mplrs, the MPI version.

# Upstream sometimes releases new tarballs that contain the same version
# number but a later date.  In that case, upstream uses a letter ('a', 'b',
# etc.) to distinguish the new tarballs from the previous tarballs.
%global vsuffix a

Name:           lrslib
Version:        7.0
Release:        6%{?dist}
Summary:        Reverse search for vertex enumeration/convex hull problems

%global upver 0%(sed 's/\\.//' <<< %{version})
%global lrsdir %(sed 's/[[:alpha:]]//' <<< %{upver})

License:        GPLv2+
URL:            http://cgm.cs.mcgill.ca/~avis/C/lrs.html
Source0:        http://cgm.cs.mcgill.ca/~avis/C/%{name}/archive/%{name}-%{upver}%{?vsuffix}.tar.gz
# These man pages were written by Jerry James.  Text from the sources was used,
# therefore the man pages have the same copyright and license as the sources.
Source1:        %{name}-man.tar.xz
# This patch was sent upstream on 31 May 2011.  It fixes some miscellaneous
# bugs and adapts to the naming scheme we choose for installation.
Patch0:         %{name}-fixes.patch
# Adapt to GCC 10's default of -fno-common, sent upstream 22 Jan 2020.
Patch1:         %{name}-common.patch

BuildRequires:  boost-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel

%description
%{name} is a self-contained ANSI C implementation as a callable library
of the reverse search algorithm for vertex enumeration/convex hull
problems and comes with a choice of three arithmetic packages.  Input
file formats are compatible with Komei Fukuda's cdd package (cddlib).
All computations are done exactly in either multiple precision or fixed
integer arithmetic.  Output is not stored in memory, so even problems
with very large output sizes can sometimes be solved.

%package devel
Summary:        Header files and libraries for developing with %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}

%description devel
Header files and libraries for developing with %{name}.

%package utils
Summary:        Sample programs that use %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description utils
Sample programs that use %{name}.

%prep
%autosetup -n %{name}-%{lrsdir}
%setup -q -n %{name}-%{lrsdir} -T -D -a 1

# Remove spurious executable bits
find -O3 . -type f -exec chmod a-x {} \+

%build
# The Makefile is too primitive to use.  For one thing, it only builds
# binaries, not libraries.  We do our own thing here.
# Recent changes to the Makefile make it less primitive, but it still does not
# work well for building on a mixture of 32-bit and 64-bit architectures.

# Upstream wants to use 0.0.0 as the soname version number for now.
%global sover 0
%global ver 0.0.0

CFLAGS="${RPM_OPT_FLAGS} -DMA -I. -I%{_includedir}/boost"

# Build the individual objects
gcc $CFLAGS -fPIC -DSAFE -DLRSLONG -c -o lrslong1.o lrslong.c
gcc $CFLAGS -fPIC -DSAFE -DLRSLONG -c -o lrslib1.o lrslib.c
gcc $CFLAGS -fPIC -DGMP -c -o lrslibgmp.o lrslib.c
gcc $CFLAGS -fPIC -DGMP -c -o lrsgmp.o lrsgmp.c
gcc $CFLAGS -fPIC -c -o lrsdriver.o lrsdriver.c
if [ %{__isa_bits} = "64" ]; then
  gcc $CFLAGS -fPIC -DSAFE -DLRSLONG -DB128 -c -o lrslong2.o lrslong.c
  gcc $CFLAGS -fPIC -DSAFE -DLRSLONG -DB128 -c -o lrslib2.o lrslib.c
fi

# Build the library
if [ %{__isa_bits} = "64" ]; then
  gcc $CFLAGS $RPM_LD_FLAGS -fPIC -shared -Wl,-soname,liblrs.so.%{sover} \
    -o liblrs.so.%{ver} lrslong1.o lrslong2.o lrslib1.o lrslib2.o lrslibgmp.o \
    lrsgmp.o lrsdriver.o -lgmp
else
  gcc $CFLAGS $RPM_LD_FLAGS -fPIC -shared -Wl,-soname,liblrs.so.%{sover} \
    -o liblrs.so.%{ver} lrslong1.o lrslib1.o lrslibgmp.o lrsgmp.o lrsdriver.o \
    -lgmp
fi
ln -s liblrs.so.%{ver} liblrs.so.%{sover}
ln -s liblrs.so.%{sover} liblrs.so

# Build the binaries
if [ %{__isa_bits} = "64" ]; then
  gcc $CFLAGS -DB128 -DSAFE lrs.c -o lrs $RPM_LD_FLAGS -L. -llrs
  gcc $CFLAGS -DB128 lrs.c -o lrsn $RPM_LD_FLAGS -L. -llrs
  gcc $CFLAGS -DB128 redund.c -o lrs-redund $RPM_LD_FLAGS -L. -llrs
else
  gcc $CFLAGS -DSAFE lrs.c -o lrs $RPM_LD_FLAGS -L. -llrs
  gcc $CFLAGS lrs.c -o lrsn $RPM_LD_FLAGS -L. -llrs
  gcc $CFLAGS redund.c -o lrs-redund $RPM_LD_FLAGS -L. -llrs
fi
gcc $CFLAGS -DGMP lrs.c -o lrsgmp $RPM_LD_FLAGS -L. -llrs -lgmp
gcc $CFLAGS -DGMP redund.c -o lrs-redundgmp $RPM_LD_FLAGS -L. -llrs
gcc $CFLAGS -DGMP lrsnash.c lrsnashlib.c -o lrsnash $RPM_LD_FLAGS -L. -llrs \
  -lgmp
gcc $CFLAGS -DLRSLONG -DSAFE lrsnash.c lrsnashlib.c -o lrsnash1 $RPM_LD_FLAGS \
  -L. -llrs
if [ %{__isa_bits} = "64" ]; then
  gcc $CFLAGS -DLRSLONG -DSAFE -DB128 lrsnash.c lrsnashlib.c -o lrsnash2 \
    $RPM_LD_FLAGS -L. -llrs
fi
gcc $CFLAGS 2nash.c -o lrs-2nash $RPM_LD_FLAGS
gcc $CFLAGS buffer.c -o lrs-buffer $RPM_LD_FLAGS
gcc $CFLAGS -DGMP fourier.c -o lrs-fourier $RPM_LD_FLAGS -L. -llrs -lgmp
gcc $CFLAGS -DGMP setupnash.c -o lrs-setupnash $RPM_LD_FLAGS -L. -llrs
gcc $CFLAGS -DGMP setupnash2.c -o lrs-setupnash2 $RPM_LD_FLAGS -L. -llrs
gcc $CFLAGS -DLRSMP -Dcopy=copy_dict_1 -Dlrs_mp_init=lrs_mp_init_1 -Dpmp=pmp_1 \
  -Drattodouble=rattodouble_1 -Dreadrat=readrat_1 rat2float.c -o lrs-rat2float \
  $RPM_LD_FLAGS -L. -llrs
gcc $CFLAGS float2rat.c -o lrs-float2rat $RPM_LD_FLAGS

%install
# Install the library
mkdir -p %{buildroot}%{_libdir}
cp -a liblrs.so* %{buildroot}%{_libdir}
chmod 0755 %{buildroot}%{_libdir}/lib*.so.%{ver}

# Install the binaries
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 lrs lrsn lrsgmp lrsnash lrsnash1 lrs-* %{buildroot}%{_bindir}
if [ %{__isa_bits} = "64" ]; then
  install -p -m 0755 lrsnash2 %{buildroot}%{_bindir}
fi

# Install the header files, but fix up the include directives.
mkdir -p %{buildroot}%{_includedir}/%{name}
sed -r 's|"(lrs.*\.h)"|<lrslib/\1>|' lrslib.h > \
    %{buildroot}%{_includedir}/%{name}/lrslib.h
touch -r lrslib.h %{buildroot}%{_includedir}/%{name}/lrslib.h

sed -e 's|"gmp.h"|<gmp.h>|' lrsgmp.h > \
    %{buildroot}%{_includedir}/%{name}/lrsgmp.h
touch -r lrsgmp.h %{buildroot}%{_includedir}/%{name}/lrsgmp.h

cp -p lrsdriver.h lrslong.h lrsmp.h lrsnashlib.h \
  %{buildroot}%{_includedir}/%{name}

# Install the man pages
mkdir -p %{buildroot}%{_mandir}/man1
cd man
for f in *.1; do
  sed "s/@VERSION@/%{upver}/" $f > %{buildroot}%{_mandir}/man1/$f
  touch -r $f %{buildroot}%{_mandir}/man1/$f
done

%files
%doc README
%license COPYING
%{_libdir}/liblrs.so.0
%{_libdir}/liblrs.so.0.*

%files devel
%doc chdemo.c lpdemo.c lpdemo1.c lpdemo2.c nashdemo.c vedemo.c
%{_includedir}/%{name}
%{_libdir}/liblrs.so

%files utils
%{_bindir}/lrs*
%{_mandir}/man1/lrs*
%{_mandir}/man1/plrs*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Jerry James <loganjerry@gmail.com> - 7.0-5
- Add -common patch to fix build with -fcommon, for GCC 10

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Jerry James <loganjerry@gmail.com> - 7.0-3
- Update to version 070a

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 20 2018 Jerry James <loganjerry@gmail.com> - 7.0-1
- New upstream release
- Major spec file overhaul due to upstream combining all 3 versions of the
  library into a single library

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar  3 2018 Jerry James <loganjerry@gmail.com> - 6.2-10
- BR gcc-c++ instead of gcc

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb  1 2018 Jerry James <loganjerry@gmail.com> - 6.2-8
- Rebuild for Boost 1.66

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 6.2-5
- Rebuilt for s390x binutils bug

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 6.2-4
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 6.2-2
- Rebuilt for Boost 1.63

* Fri May 27 2016 Jerry James <loganjerry@gmail.com> - 6.2-1
- New upstream release

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 6.1-4
- Rebuilt for linker errors in boost (#1331983)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 6.1-2
- Rebuilt for Boost 1.60

* Fri Dec  4 2015 Jerry James <jamesjer@diannao.jamezone.org> - 6.1-1
- New upstream release

* Sat Sep 19 2015 Jerry James <loganjerry@gmail.com> - 6.0-1
- New upstream release

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 5.1-7
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 5.1-5
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 5.1-3
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 04 2015 Petr Machata <pmachata@redhat.com> - 5.1-2
- Bump for rebuild.

* Mon Feb  2 2015 Jerry James <loganjerry@gmail.com> - 5.1-1
- New upstream release

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 5.0a-2
- Rebuild for boost 1.57.0

* Thu Jan 15 2015 Jerry James <loganjerry@gmail.com> - 5.0a-1
- New upstream release

* Mon Nov 10 2014 Jerry James <loganjerry@gmail.com> - 5.0-1
- New upstream release
- Drop upstreamed -memleak patch
- Link with RPM_LD_FLAGS
- Fix license handling

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 13 2012 Jerry James <loganjerry@gmail.com> - 4.3-1
- New upstream release

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2c-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 16 2012 Jerry James <loganjerry@gmail.com> - 4.2c-4
- Apply patch from Thomas Rehn to fix a memory leak

* Tue Feb 14 2012 Jerry James <loganjerry@gmail.com> - 4.2c-3
- Change subpackage structure based on review

* Wed Aug 24 2011 Jerry James <loganjerry@gmail.com> - 4.2c-2
- Use %%{name} more liberally.
- Use %%global instead of %%define.
- Add man pages.

* Wed Jul 20 2011 Jerry James <loganjerry@gmail.com> - 4.2c-1
- Initial RPM
