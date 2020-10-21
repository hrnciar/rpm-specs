# hmod_mat addon checkout information; this is used by eclib
%global hm_user fredrik-johansson
%global hm_name hmod_mat
%global hm_commit 75378f4af0f0b558385a8bf28d6b4b8ca5f0f568
%global hm_shortcommit %(c=%{hm_commit}; echo ${c:0:7})
%global hm_date 20140328

Name:           flint
Version:        2.6.3
Release:        1%{?dist}
Summary:        Fast Library for Number Theory

# Flint itself is LGPLv2+.  The hmod_mat extension is GPLv2+.
License:        LGPLv2+ and GPLv2+
URL:            http://www.flintlib.org/
Source0:        http://www.flintlib.org/%{name}-%{version}.tar.gz
Source1:        https://github.com/%{hm_user}/%{hm_name}/archive/%{hm_commit}/%{hm_name}-%{hm_shortcommit}.tar.gz
# Make the hmod_mat extension use gmp instead of mpir
Patch0:         %{name}-hmod_mat.patch
# Use the popcnt instruction when available
Patch1:         %{name}-popcnt.patch


BuildRequires:  flexiblas-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  ntl-devel
BuildRequires:  pkgconfig(bdw-gc)
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  tex(latex)

%description
FLINT is a C library for doing number theory, written by William Hart
and David Harvey.


%package        devel
Summary:        Development files for FLINT
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}
Requires:       mpfr-devel%{?_isa}
Requires:       ntl-devel%{?_isa}


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        static
Summary:        Static libraries for FLINT
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}


%description    static
The %{name}-static package contains static libraries for
developing applications that use %{name}.


%prep
%setup -q -c
%setup -q -T -D -a 1

fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Use gmp instead of mpir with hmod_mat
for fil in $(grep -Frl mpir.h hmod_mat-%{hm_commit}); do
  sed -i.orig 's/mpir\.h/gmp.h/' $fil
  fixtimestamp $fil
done

mv hmod_mat-%{hm_commit} %{name}-%{version}/hmod_mat
pushd %{name}-%{version}

%autopatch -p0

# Do not use rpaths.  Use flexiblas instead of openblas
sed -i '/ -Wl,-rpath,[^"]*\("\)/d;s/openblas/flexiblas/' configure

# sanitize header files
ln -sf $PWD flint
# sanitize references to external headers
for fil in $(find . -name \*.c -o -name \*.h -o -name \*.in); do
  sed -ri.orig 's/"((gc|gmp|limits|math|stdlib|string)\.h)"/<\1>/' $fil
  fixtimestamp $fil
done
# sanitize references to flintxx headers
sed_expr=$(ls -1 flintxx/*.h | \
  sed -r 's,flintxx/(.*)\.h,\1,' | \
  awk '/START/{if (x) print x;x="";next}{x=(!x)?$0:x"|"$0;}END{print x;}')
for fil in $(find . -name \*.c -o -name \*.h); do
  sed -ri.orig "s@\"(flintxx/)?(($sed_expr)\.h)\"@<flint/flintxx/\2>@" $fil
  fixtimestamp $fil
done
# sanitize references to all other headers
for fil in $(find . -name \*.c -o -name \*.h); do
  sed -ri.orig 's@"(\.\./)?([^"]+\.h])"@<flint/\2>@' $fil
  fixtimestamp $fil
done
# "

# Use the classic sphinx theme
sed -i "s/'default'/'classic'/" doc/source/conf.py

# Rename hmod_mat files for doc
cp -p hmod_mat/LICENSE LICENSE.hmod_mat
cp -p hmod_mat/README.md README.hmod_mat.md
popd

# Prepare to build two versions of the library
cp -a %{name}-%{version} %{name}-%{version}-gc
for fil in $(grep -Frl libflint %{name}-%{version}-gc); do
  sed -i 's/libflint/libflint-gc/' $fil
done


%build
export CFLAGS="%{build_cflags} -fwrapv -D_FILE_OFFSET_BITS=64"
# We set HAVE_FAST_COMPILER to 0 on i686, ARM, s390, and 32-bit MIPS because
# otherwise the tests exhaust virtual memory.  If other architectures run out
# of virtual memory while building flintxx/test/t-fmpzxx.cpp, then do likewise.
%ifarch %{ix86} %{arm} s390 %{mips32}
CFLAGS="$CFLAGS -DHAVE_FAST_COMPILER=0"
%endif
export CXXFLAGS="$CFLAGS"

# Build the non-gc version
pushd %{name}-%{version}
OS=Linux \
MACHINE=%{_arch} \
sh -x ./configure \
    --prefix=%{_prefix} \
    --with-gmp=%{_prefix} \
    --with-mpfr=%{_prefix} \
    --with-blas=%{_libdir} \
    --with-ntl=%{_prefix} \
    --enable-cxx \
    --extensions=$PWD/hmod_mat \
    CFLAGS="$CFLAGS" \
    CXXFLAGS="$CXXFLAGS"

# FIXME: %%{?_smp_mflags} sometimes fails
make verbose LDFLAGS="%{build_ldflags}" LIBDIR=%{_lib}

# Build the documentation
make -C doc html
popd

# Build the gc version
pushd %{name}-%{version}-gc
OS=Linux \
MACHINE=%{_arch} \
sh -x ./configure \
    --prefix=%{_prefix} \
    --with-gmp=%{_prefix} \
    --with-mpfr=%{_prefix} \
    --with-blas=%{_libdir} \
    --with-ntl=%{_prefix} \
    --with-gc=%{_prefix} \
    --enable-cxx \
    CFLAGS="$CFLAGS" \
    CXXFLAGS="$CXXFLAGS"

# FIXME: %%{?_smp_mflags} sometimes fails
make verbose LDFLAGS="%{build_ldflags}" LIBDIR=%{_lib}
popd


%install
# Install the gc version
pushd %{name}-%{version}-gc
%make_install LIBDIR=%{_lib}
popd

# Install the non-gc version
pushd %{name}-%{version}
%make_install LIBDIR=%{_lib}

# Fix permissions
chmod 0755 %{buildroot}%{_libdir}/libflint*.so.*

# Install CPimport.txt
mkdir -p %{buildroot}%{_datadir}/flint
cp -p qadic/CPimport.txt %{buildroot}%{_datadir}/flint
popd


%ifnarch %{arm} %{ix86}
# Tests temporarily disabled on 32-bit builders.
# See https://github.com/wbhart/flint2/issues/786
%check
pushd %{name}-%{version}
export LD_LIBRARY_PATH=$PWD
make check QUIET_CC= QUIET_CXX= QUIET_AR= \
  LDFLAGS="%{build_ldflags}" LIBDIR=%{_lib}
popd
%endif


%files
%doc %{name}-%{version}/AUTHORS
%doc %{name}-%{version}/NEWS
%doc %{name}-%{version}/README
%doc %{name}-%{version}/README.hmod_mat.md
%license %{name}-%{version}/LICENSE %{name}-%{version}/LICENSE.hmod_mat
%{_libdir}/libflint.so.14*
%{_libdir}/libflint-gc.so.14*
%{_datadir}/flint


%files devel
%doc %{name}-%{version}/doc/build/html
%{_includedir}/flint/
%{_libdir}/libflint.so
%{_libdir}/libflint-gc.so


%files static
%{_libdir}/libflint.a
%{_libdir}/libflint-gc.a


%changelog
* Wed Aug 12 2020 Jerry James <loganjerry@gmail.com> - 2.6.3-1
- Version 2.6.3

* Fri Jul 31 2020 Jerry James <loganjerry@gmail.com> - 2.6.2-1
- Version 2.6.2

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Jerry James <loganjerry@gmail.com> - 2.6.1-1
- Version 2.6.1
- Drop patches added in 2.6.0-1
- Drop no longer needed -latex patch

* Wed Jul 22 2020 Tom Stellard <tstellar@redhat.com> - 2.6.0-2
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Wed Jul  8 2020 Jerry James <loganjerry@gmail.com> - 2.6.0-1
- Version 2.6.0
- Add upstream patches to fix bugs discovered after release:
  -fmpq-poly-add-fmpq.patch, -nmod-mpolyn-interp-crt-lg-poly.patch,
  -fmpz-mpoly-div-monagan-pearce.patch, -fmpz-poly-factor.patch,
  -fmpz-mod-poly-gcdiv-euclidean.patch
- Disable tests on 32-bit arches until upstream can diagnose a failure

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  9 2020 Jerry James <loganjerry@gmail.com> - 2.5.2-30
- Rebuild for ntl 11.4.3

* Wed Oct  9 2019 Jerry James <loganjerry@gmail.com> - 2.5.2-29
- Rebuild for mpfr 4

* Tue Sep 24 2019 Jerry James <loganjerry@gmail.com> - 2.5.2-28
- Rebuild for ntl 11.3.4
- Add -pie-hardening-conflict patch from sagemath

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 30 2019 Jerry James <loganjerry@gmail.com> - 2.5.2-26
- Drop the workaround for bz 1555151, now fixed

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 13 2018 Jerry James <loganjerry@gmail.com> - 2.5.2-24
- Rebuild for ntl 11.3.0
- Build with openblas instead of atlas

* Fri Aug 10 2018 Jerry James <loganjerry@gmail.com> - 2.5.2-23
- Rebuild for ntl 11.2.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul  3 2018 Jerry James <loganjerry@gmail.com> - 2.5.2-21
- Rebuild for ntl 11.1.0

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 2.5.2-20
- Rebuild for ntl 11.0.0
- Add i686 to the architectures with slow compilers due to FTBFS (bz 1555753)
- Work around apparent compiler bug on 32-bit arm (bz 1555151)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 28 2017 Jerry James <loganjerry@gmail.com> - 2.5.2-18
- Rebuild for ntl 10.5.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr  5 2017 Jerry James <loganjerry@gmail.com> - 2.5.2-15
- Rebuild for ntl 10.3.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 20 2016 Jerry James <loganjerry@gmail.com> - 2.5.2-13
- Rebuild for ntl 10.1.0

* Wed Aug 31 2016 Jerry James <loganjerry@gmail.com> - 2.5.2-12
- Rebuild for ntl 9.11.0

* Thu Aug 11 2016 Michal Toman <mtoman@fedoraproject.org> - 2.5.2-11
- HAVE_FAST_COMPILER=0 on 32-bit MIPS (bz 1366672)

* Mon Jul 25 2016 Jerry James <loganjerry@gmail.com> - 2.5.2-10
- Rebuild for ntl 9.10.0

* Thu Jun  2 2016 Jerry James <loganjerry@gmail.com> - 2.5.2-9
- Rebuild for ntl 9.9.1

* Fri Apr 29 2016 Jerry James <loganjerry@gmail.com> - 2.5.2-8
- Rebuild for ntl 9.8.0

* Fri Mar 18 2016 Jerry James <loganjerry@gmail.com> - 2.5.2-7
- Rebuild for ntl 9.7.0

* Sat Feb 20 2016 Jerry James <loganjerry@gmail.com> - 2.5.2-6
- Rebuild for ntl 9.6.4

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec  4 2015 Jerry James <loganjerry@gmail.com> - 2.5.2-4
- Rebuild for ntl 9.6.2

* Fri Oct 16 2015 Jerry James <loganjerry@gmail.com> - 2.5.2-3
- Rebuild for ntl 9.4.0

* Sat Oct 10 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.5.2-2
- Correct detection of gcc 5 as a fast compiler (#1270271)

* Sat Sep 19 2015 Jerry James <loganjerry@gmail.com> - 2.5.2-1
- New upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Jerry James <loganjerry@gmail.com> - 2.4.5-4
- Rebuild for ntl 9.1.1

* Sat May  9 2015 Jerry James <loganjerry@gmail.com> - 2.4.5-3
- Rebuild for ntl 9.1.0

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.4.5-2
- Rebuilt for GCC 5 C++11 ABI change

* Fri Mar 20 2015 Jerry James <loganjerry@gmail.com> - 2.4.5-1
- New upstream release

* Mon Feb  2 2015 Jerry James <loganjerry@gmail.com> - 2.4.4-6
- Rebuild for ntl 8.1.2

* Mon Jan 12 2015 Jerry James <loganjerry@gmail.com> - 2.4.4-5
- Rebuild for ntl 8.1.0

* Mon Sep 22 2014 Jerry James <loganjerry@gmail.com> - 2.4.4-4
- Rebuild for ntl 6.2.1
- Fix license handling

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 28 2014 Jakub Čajka <jcajka@redhat.com> - 2.4.4-2
- Disable tests that exhaust memory on s390 (bz 1123757)

* Mon Jul 21 2014 Jerry James <loganjerry@gmail.com> - 2.4.4-1
- New upstream release

* Wed Jul 16 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 2.4.2-4
- Fix FTBFS with GMP 6.0 (#1107245)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr  2 2014 Jerry James <loganjerry@gmail.com> - 2.4.2-2
- Rebuild for ntl 6.1.0
- The -devel subpackage requires ntl-devel

* Mon Mar 17 2014 Jerry James <loganjerry@gmail.com> - 2.4.2-1
- New upstream release

* Mon Feb 10 2014 Jerry James <loganjerry@gmail.com> - 2.4.1-1
- New upstream release
- Enable C++ interface
- Tests now work on 32-bit systems
- Minimize the set of LaTeX BRs
- Enable verbose build
- Link with Fedora LDFLAGS
- On ARM arches, disable tests that exhaust virtual memory while compiling
- Add -fno-strict-aliasing to the test program builds, due to violations of
  the strict aliasing rules in some of the C++ tests

* Mon Aug  5 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.3-1.20130801git4b383e2
- Update to pre 2.4 snapshot that supports gmp, required by sagemath 5.10

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May  6 2013 Jerry James <loganjerry@gmail.com> - 1.6-7
- Rebuild for ntl 6.0.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 1 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.6-4
- Build with ntl support to have all symbols resolved.
- Force -fPIC in CFLAGS to avoid ntl link failures.

* Mon May  7 2012 Jerry James <loganjerry@gmail.com> - 1.6-3
- Update warning patch to fix bz 819333

* Mon Jan  9 2012 Jerry James <loganjerry@gmail.com> - 1.6-2
- Rebuild for GCC 4.7

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.6-1.2
- rebuild with new gmp without compat lib

* Mon Oct 10 2011 Peter Schiffer <pschiffe@redhat.com> - 1.6-1.1
- rebuild with new gmp

* Mon Jul 18 2011 Jerry James <loganjerry@gmail.com> - 1.6-1
- New upstream release
- Build against the system zn_poly instead of the included sources
- Make sure there is no PIC code in the static archive
- Link mpQS against the shared library instead of including the library
- Fix build errors and scary warnings with gcc 4.6
- Remove unnecessary spec file elements (BuildRoot, etc.)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jun 26 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.5.2-1
- update to new version
- renew both patches

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 10 2009 Conrad Meyer <konrad@tylerc.org> - 1.2.0-1
- Bump to 1.2.0.

* Fri Mar 6 2009 Conrad Meyer <konrad@tylerc.org> - 1.0.21-1
- Bump to 1.0.21.
- Build static subpackage.

* Sat Dec 6 2008 Conrad Meyer <konrad@tylerc.org> - 1.0.18-1
- Bump to 1.0.18.
- Patches apply with --fuzz=0.

* Sat Nov 29 2008 Conrad Meyer <konrad@tylerc.org> - 1.0.17-1
- Initial package.
