Name:           latte-integrale
Version:        1.7.5
Release:        8%{?dist}
Summary:        Lattice point enumeration

%global tarver %(tr . _ <<< %{version})

License:        GPLv2+
URL:            https://www.math.ucdavis.edu/~latte/software.php
Source0:        https://github.com/latte-int/latte/releases/download/version_%{tarver}/%{name}-%{version}.tar.gz
# Fix warnings that indicate possible runtime problems.
Patch0:         %{name}-warning.patch
# Fix LiDIA warnings that indicate possible runtime problems.
Patch1:         lidia-warning.patch
# Upstream patch to fix division by zero with recent NTL versions
Patch2:         %{name}-ntl.patch

BuildRequires:  4ti2-devel
BuildRequires:  cddlib-devel
BuildRequires:  cddlib-tools
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  libtool
BuildRequires:  lrslib-utils
BuildRequires:  ntl-devel
BuildRequires:  perl-interpreter
BuildRequires:  sqlite-devel
BuildRequires:  TOPCOM

Requires:       cddlib-tools
Requires:       coreutils
Requires:       TOPCOM

Suggests:       lrslib-utils

# latte-integrale contains a copy of gnulib, which has been granted a bundling
# exception: https://fedoraproject.org/wiki/Packaging:No_Bundled_Libraries#Packages_granted_exceptions
Provides:       bundled(gnulib)

%description
LattE (Lattice point Enumeration) is a computer software dedicated to
the problems of counting lattice points and integration inside convex
polytopes.  LattE contains the first ever implementation of Barvinok's
algorithm.  The LattE macchiato version (by M. Köppe) incorporated
fundamental improvements and speed ups.  Now the latest version, LattE
integrale, has the ability to directly compute integrals of polynomial
functions over polytopes and in particular to do volume computations.

%prep
%setup -q

# Don't use bundled software
rm -f 4ti2* cddlib* glpk* gmp* ntl*

# Add a missing executable bit
chmod a+x ltmain.sh

# Unpack LiDia and latte-integrale
tar xzf lidia-base-2.3.0+latte-patches-2014-10-04.tar.gz
tar xzf lidia-FF-2.3.0+latte-patches-2014-10-04.tar.gz
tar xzf lidia-LA-2.3.0+latte-patches-2014-10-04.tar.gz
tar xzf latte-int-%{version}.tar.gz

# Patch latte-integrale
pushd latte-int-%{version}
%patch0
%patch2

# Fix the cddlib search path, lrslib binary name
sed -e "s|cdd\.h|cddlib/cdd.h|" -e "s/lrs1/lrs/" -i configure

# Fix the 4ti2 library search paths
sed -ri "s|\{?FORTYTWO_HOME\}?/include|&/4ti2|g" configure
if [ %{_lib} = "lib64" ]; then
  sed -i "s|{FORTYTWO_HOME}/lib|&64|" configure
fi

# Some tests fail because they timeout on slower processors.  Eliminate the
# timeouts and let koji kill us if a test infloops.  Also, use a consistent
# hostname for reproducibility.
sed -e 's/ulimit -t $MAXRUNTIME; //' \
    -e 's,.*HOSTNAME = `hostname`.*,$HOSTNAME = "build.fedoraproject.org";,' \
    -i code/test-suite/test.pl.in
popd

# Patch lidia and update the missing script
pushd lidia-2.3.0+latte-patches-2014-10-04
%patch1
cp -p %{_datadir}/libtool/build-aux/missing .
popd

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
# Make a place for a fake install of LiDIA
mkdir -p local%{_includedir}
ln -s lidia local%{_includedir}/LiDIA

# Build LiDia
pushd lidia-2.3.0+latte-patches-2014-10-04
%configure --disable-nf --disable-ec --disable-eco --disable-gec \
  CFLAGS="%{optflags} -fPIC -fno-strict-aliasing" \
  CXXFLAGS="%{optflags} -fPIC -fno-strict-aliasing"
sed -i 's/-m64/& -fPIC -fno-strict-aliasing/' libtool library/Makefile \
  library/base/Makefile library/linear_algebra/Makefile \
  library/finite_fields/Makefile
make %{?_smp_mflags}

# Do a fake install of LiDia for building latte-integrale
make install DESTDIR=$PWD/../local
sed -i "s,%{_libdir},$PWD/../local&," ../local%{_libdir}/*.la
popd

# Now build latte-integrale itself
pushd latte-int-%{version}
%configure --enable-DATABASE --enable-shared --disable-static \
  --with-4ti2=%{_prefix} --with-lidia=$PWD/../local/%{_prefix} \
  CPPFLAGS="-I%{_includedir}/4ti2 -I%{_includedir}/cddlib -D_GNU_SOURCE=1 -DNTL_STD_CXX" \
  LDFLAGS="-L$PWD/../local%{_libdir} $RPM_LD_FLAGS"

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

make %{?_smp_mflags}

%install
# Install latte-integrale
pushd latte-int-%{version}
%make_install

# Some binaries have too-generic names
for bin in count integrate triangulate; do
  mv %{buildroot}%{_bindir}/$bin %{buildroot}%{_bindir}/latte-$bin
done

# We don't need or want libtool files
rm -f %{buildroot}%{_libdir}/*.la

# Internal libraries only; don't install the .so since there are no headers
rm -f %{buildroot}%{_libdir}/lib{latte,normalize}.so

# We don't want documentation in _datadir
mv %{buildroot}%{_datadir}/latte-int _docs_staging

# Install missing documentation files
cp -p AUTHORS TODO _docs_staging
popd

%ldconfig_scriptlets

%check
export LD_LIBRARY_PATH=$PWD/local%{_libdir}:$PWD/latte-int-%{version}/code/latte/.libs:$PWD/latte-int-%{version}/code/latte/normalize/.libs

# Check LattE
pushd latte-int-%{version}
make check
popd

%files
%doc latte-int-%{version}/_docs_staging/*
%license latte-int-%{version}/COPYING
%{_bindir}/*
%{_libdir}/liblatte.so.0
%{_libdir}/liblatte.so.0*
%{_libdir}/libnormalize.so.0
%{_libdir}/libnormalize.so.0*

%changelog
* Tue Jul 28 2020 Jeff Law <law@redhat.com> - 1.7.5-8
- Force C++14 as this code is not C++17 ready

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  9 2020 Jerry James <loganjerry@gmail.com> - 1.7.5-5
- Rebuild for ntl 11.4.3

* Tue Sep 24 2019 Jerry James <loganjerry@gmail.com> - 1.7.5-4
- Rebuild for ntl 11.3.4
- Add -ntl patch to prevent division by zero with recent ntl versions

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct  9 2018 Jerry James <loganjerry@gmail.com> - 1.7.5-1
- New upstream release

* Sat Aug 25 2018 Jerry James <loganjerry@gmail.com> - 1.7.3b-13
- Apply upstream's patch for out of bounds vector accesses in 4ti2

* Fri Aug 10 2018 Jerry James <loganjerry@gmail.com> - 1.7.3b-12
- Rebuild for ntl 11.2.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3b-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul  3 2018 Jerry James <loganjerry@gmail.com> - 1.7.3b-10
- Rebuild for ntl 11.1.0

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 1.7.3b-9
- Rebuild for ntl 11.0.0 and glpk 4.65

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3b-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 28 2017 Jerry James <loganjerry@gmail.com> - 1.7.3b-7
- Rebuild for ntl 10.5.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3b-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3b-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3b-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Wed Apr  5 2017 Jerry James <loganjerry@gmail.com> - 1.7.3b-3
- Rebuild for ntl 10.3.0 and glpk 4.61

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 20 2016 Jerry James <loganjerry@gmail.com> - 1.7.3b-1
- New upstream release

* Mon Sep  5 2016 Jerry James <loganjerry@gmail.com> - 1.7.3-14
- Rebuild for ntl 9.11.0

* Mon Jul 25 2016 Jerry James <loganjerry@gmail.com> - 1.7.3-13
- Rebuild for ntl 9.10.0

* Thu Jun  2 2016 Jerry James <loganjerry@gmail.com> - 1.7.3-12
- Rebuild for ntl 9.9.1

* Wed Apr 27 2016 Jerry James <loganjerry@gmail.com> - 1.7.3-11
- Rebuild for ntl 9.8.0
- Build with LiDIA; it is available under the GPLv2

* Fri Mar 18 2016 Jerry James <loganjerry@gmail.com> - 1.7.3-10
- Rebuild for ntl 9.7.0

* Sat Mar 12 2016 Jerry James <loganjerry@gmail.com> - 1.7.3-9
- Rebuild for glpk 4.59

* Sat Feb 20 2016 Jerry James <loganjerry@gmail.com> - 1.7.3-8
- Rebuild for ntl 9.6.4 and glpk 4.58

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec  4 2015 Jerry James <loganjerry@gmail.com> - 1.7.3-6
- Rebuild for ntl 9.6.2 and lrslib 061

* Fri Oct 16 2015 Jerry James <loganjerry@gmail.com> - 1.7.3-5
- Rebuild for ntl 9.4.0

* Sat Sep 19 2015 Jerry James <loganjerry@gmail.com> - 1.7.3-4
- Rebuild for ntl 9.3.0 and lrslib 060

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Jerry James <loganjerry@gmail.com> - 1.7.3-2
- Rebuild for ntl 9.1.1 and cddlib 094h

* Sat May  9 2015 Jerry James <loganjerry@gmail.com> - 1.7.3-1
- New upstream release

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.7.2-3.1
- Rebuilt for GCC 5 C++11 ABI change

* Mon Feb  2 2015 Jerry James <loganjerry@gmail.com> - 1.7.2-3
- Rebuild for ntl 8.1.2

* Thu Jan 15 2015 Jerry James <loganjerry@gmail.com> - 1.7.2-2
- Rebuild for ntl 8.1.0

* Mon Nov 10 2014 Jerry James <loganjerry@gmail.com> - 1.7.2-1
- New upstream release

* Tue Oct 28 2014 Jerry James <loganjerry@gmail.com> - 1.7.1-6
- Rebuild for ntl 6.2.1

* Thu Aug 21 2014 Jerry James <loganjerry@gmail.com> - 1.7.1-5
- Fix mass rebuild failure
- Fix license handling

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Jerry James <loganjerry@gmail.com> - 1.7.1-4
- Rebuild to fix internal 4ti2 dependencies

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr  2 2014 Jerry James <loganjerry@gmail.com> - 1.7.1-3
- Rebuild for ntl 6.1.0

* Tue Feb 11 2014 Jerry James <loganjerry@gmail.com> - 1.7.1-2
- There is a dist tag for a reason; use it on the 4ti2 packages

* Mon Feb 10 2014 Jerry James <loganjerry@gmail.com> - 1.7.1-1
- New upstream release
- Drop upstreamed 4ti2-glpk patch
- Fix documentation snafu caused by the docdir change

* Tue Jan  7 2014 Jerry James <loganjerry@gmail.com> - 1.7-2
- Bump and rebuild (releng ticket 5827)

* Mon Jan  6 2014 Jerry James <loganjerry@gmail.com> - 1.7-1
- New upstream release

* Tue Sep 10 2013 Jerry James <loganjerry@gmail.com> - 1.6-1
- New upstream release
- Drop upstreamed 4ti2-gaussian and 4ti2-gcc47 patches
- Remove incorrect Obsoletes/Provides for 4ti2

* Fri Aug  2 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.5.3-10
- Use special %%doc to install docs in order to honor %%{_docdir_fmt}.

* Wed Jul 31 2013 Jerry James <loganjerry@gmail.com> - 1.5.3-9
- Add 4ti2-glpk.patch to fix build with new glpk

* Mon May  6 2013 Jerry James <loganjerry@gmail.com> - 1.5.3-8
- Add 4ti2-gaussian.patch to fix a segfault (bz 911437)
- Rename some too-generically named binaries (bz 913684)

* Sat Feb  2 2013 Jerry James <loganjerry@gmail.com> - 1.5.3-7
- Rebuild for new glpk

* Tue Jan 22 2013 Jerry James <loganjerry@gmail.com> - 1.5.3-6
- Build with _GNU_SOURCE defined to get long options, too
- Remove test timeouts so tests don't die spuriously on ARM (bz 893158)

* Mon Dec 10 2012 Jerry James <loganjerry@gmail.com> - 1.5.3-5
- Fix the name of the private bin directory too (bz 882574)

* Wed Dec  5 2012 Jerry James <loganjerry@gmail.com> - 1.5.3-4
- Fix the name of the environment module (bz 882574)

* Wed Nov 21 2012 Jerry James <loganjerry@gmail.com> - 1.5.3-3
- Add Obsoletes and Provides for the old 4ti2 package

* Mon Nov 19 2012 Jerry James <loganjerry@gmail.com> - 1.5.3-2
- Fix 4ti2 subpackage dependencies on 4ti2-libs
- Convert 4ti2's NEWS to utf-8
- Add missing doc files to the main package
- BR TOPCOM to get points2triangs and point2placingtriang

* Sat Oct  6 2012 Jerry James <loganjerry@gmail.com> - 1.5.3-1
- Initial RPM
