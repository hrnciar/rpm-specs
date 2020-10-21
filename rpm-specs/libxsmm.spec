# Copyright (c) 2015, 2016  Dave Love, University of Liverpool
# Copyright (c) 2018  Dave Love, University of Manchester
# MIT licence, per Fedora policy

# Notes:
# The specific compiler flags used are presumably chosen sensibly for the
# code, and there's no likely security implication for this.

# ix86 isn't built -- see
# https://github.com/hfp/libxsmm/issues/103#issuecomment-256887962

# The el6 compiler is too old, but we build for el6 in copr from the
# same source, as koji doesn't have el6 devtoolset, and the el7 system
# compiler doesn't do avx512.
%if 0%{?el6}%{?el7}
%bcond_without devtoolset
%endif

# For historical reasons, these have been out of step with the ABI
# versioning used by the base source.  The soversion reflects the stable
# "base" functionality, while the rest is considered unstable upstream.
%global somajor 1
%global sominor 10
%global soupd 1

Name:		libxsmm
Version:	1.16
Release:	3%{?dist}
Summary:	Small dense or sparse matrix multiplications and convolutions for x86_64
License:	BSD
URL:		https://github.com/hfp/libxsmm
Source0:	https://github.com/hfp/libxsmm/archive/%version/%name-%version.tar.gz
BuildRequires:	%_bindir/python3 openblas-devel
%if %{with devtoolset}
# Release 6 supports avx512 and uses the same libgfortran version as
# the system compiler.
BuildRequires:	devtoolset-9-gcc-gfortran devtoolset-9-gcc-c++
%else
BuildRequires:	gcc-gfortran gcc-c++
%endif
ExclusiveArch:	x86_64

# Remove /bin/sh, /bin/bash dependencies from -doc (not actually
# required by packaging guidelines)
%global __requires_exclude /bin/.*sh$
%{?filter_setup:
%filter_from_requires /\/bin\/.*sh$/d
%filter_setup
}


%description
LIBXSMM is a library for small dense and small sparse matrix-matrix
multiplications, as well as for deep learning primitives such as small
convolutions targeting Intel Architecture (x86).  The library
generates code for the following instruction set extensions: Intel
SSE, Intel AVX, Intel AVX2, IMCI (KNCni) for Intel Xeon Phi
coprocessors ("KNC"), and Intel AVX‑512 as found in the Intel Xeon Phi
processor family ("KNL") and future Intel Xeon processors.  Small
convolutions are currently only optimized for Intel AVX‑512.
Historically the library was solely targeting the Intel Many
Integrated Core Architecture "MIC") using intrinsic functions.
Currently, optimized assembly code targets all aforementioned
instruction set extensions (static code generation), and Just‑In‑Time
(JIT) code generation targets Intel AVX and beyond.


%package	devel
Summary:	Development files for %name
Requires:	%name%{?_isa} = %version-%release
Requires:	pkgconfig

%description	devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package	doc
Summary:	Documentation for %name
BuildArch:	noarch

%description	doc
Documentation for %name.


%prep
%setup -q
# MS-Windows stuff that rpmlint would complain about
find samples -name \*.vcxproj | xargs rm
# README would clobber the main one, and the others would be dangling links
rm documentation/{README,LICENSE,CONTRIBUTING}.md

# documentation/gxm.md is a symlink, wrong when the doc is installed.
rm documentation/gxm.md
cp -p samples/deeplearning/gxm/README.md documentation/gxm.md


%build
%if %{with devtoolset}
. /opt/rh/devtoolset-9/enable
%endif
# OpenMP is only used by libxsmmext, so no need to turn it off.
# Avoid the ld hardening flags, which are taken care of by the library
# build system to the extent they don't affect perfromance.
# -lm and -ldl are neded for the test, for which the LDFLAGS need to be
# consistent.  PREFIX and POUTDIR are needed at build time to get the .pc
# files correct.  OMPLIB is necessary to avoid failure in epel7 trying to
# link -lgomp.so, which I haven't figured out.
%global makeflags STATIC=0 SYM=1 AVX=0 PYTHON=%_bindir/python3 PREFIX=%buildroot%_prefix POUTDIR=%_lib VERSION_API=1 OMPLIB=-lgomp
%make_build %makeflags


%install
%if %{with devtoolset}
. /opt/rh/devtoolset-9/enable
%endif
# Supply STATIC etc. since this actually builds stuff (a bug?),
# and otherwise we end up with bits built wrongly.
make install %makeflags
mkdir -p %buildroot%_fmoddir %buildroot%_libdir/pkgconfig
mv %buildroot%_includedir/libxsmm.mod %buildroot%_fmoddir
mv %buildroot%_prefix/lib/*.pc %buildroot%_libdir/pkgconfig
sed -i -e 's|^prefix=.*$|prefix=%_prefix|' %buildroot%_libdir/pkgconfig/*.pc
rm -r %buildroot%_datadir/libxsmm

# Build artefacts
find samples -name .make | xargs rm
cp Makefile.inc samples		# included by the sub-directories
echo "These are set up to be built in the original source tree.
You will have to adjust the make files to use an installed version." >samples/README

%check
# Fixme: the test gives numerical errors inconsistently with openblas
# 0.3.1/gcc 8.1 on koji when the thread count isn't 1; sometimes 2
# works.
OMP_NUM_THREADS=1 make test-cp2k %makeflags
rm -r samples/cp2k/{.make,.state,cp2k-dbcsr,cp2k-collocate,cp2k-test.txt}
# For some reason this only seems necessary for el8
rm -rf samples/cp2k/obj

%ldconfig_scriptlets


%files
%license LICENSE.md
%_libdir/libxsmm*.so.%{somajor}*

%files devel
%doc README.md
%_libdir/libxsmm*.so
%_includedir/*
%_bindir/libxsmm_gemm_generator
# Get the module directory owned.  Currently in Fedora, gfortran owns
# %%_fmoddir, but not %%_fmoddir/..
# In el6, el7 it doesn't own either
%if 0%{?el6}%{?el7}
%dir %_fmoddir
%endif
%_fmoddir/libxsmm.mod
%_libdir/pkgconfig/*.pc


%files doc
%doc README.md documentation/*.md documentation/*.pdf samples CONTRIBUTING.md
%license LICENSE.md


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Dave Love <loveshack@fedoraproject.org> - 1.16-2
- Clean samples/cp2k/obj
- Maybe use devtoolset-9, not -6

* Fri Jun 19 2020 Dave Love <loveshack@fedoraproject.org> - 1.16-1
- New version

* Sat Mar 14 2020 Dave love <loveshack@fedoraproject.org> - 1.15-1
- New version
- Drop _legacy_common_support
- Remove installed modules file
- Fix cleanup in %%check
- Define OMPLIB for backport to EL7

* Wed Feb  5 2020 Dave love <loveshack@fedoraproject.org> - 1.14-3
- Fix FTBFS with GCC 10

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 25 2019 Dave love <loveshack@fedoraproject.org> - 1.14-1
- New version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Dave Love <loveshack@fedoraproject.org> - 1.13-1
- New version

* Thu May 23 2019 Dave Love <loveshack@fedoraproject.org> - 1.12.1-1
- New version

* Mon May 13 2019 vagrant <vagrant@localhost.localdomain> - 1.12-1
- New version

* Mon Apr 29 2019 Dave Love <loveshack@fedoraproject.org> - 1.11-1
- New version
- Drop patch

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 23 2018 Dave Love <loveshack@fedoraproject.org> - 1.10-1
- New version
- Patch builddir out of pkgconfig

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul  4 2018 Dave Love <loveshack@fedoraproject.org> - 1.9-2
- Use python2 exlicitly in scripts
- Use single thread in %%check to fix FTBFS
- Use ldconfig_scriptlets
- Don't define LDFLAGS

* Wed Mar 21 2018 Dave Love <loveshack@fedoraproject.org> - 1.9-1
- Update to 1.9 (#1557708)
- Use devtoolset-6, not -7 for EPEL
- Don't avoid SSE (assumes sse3, which seems unlikely to cause problems)
- BR python2, per new policy
- Set VERSION_UPDATE for soname to avoid going backwards
- Fix issues with doc files

* Thu Mar  8 2018 Dave Love <loveshack@fedoraproject.org> - 1.8.3-1
- Update to 1.8.3 (#1528828)
- Fix running test
- Modify %%files for distribution changes and to specify lib soversion

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 19 2017 Dave Love <loveshack@fedoraproject.org> - 1.8.1-4
- Don't run test
- Update possible devtoolset usage

* Sun Oct 29 2017 Dave Love <loveshack@fedoraproject.org> - 1.8.1-3
- Fix spurious executable permission
- Reinstate %%check
- Build with AVX=0

* Fri Oct 27 2017 Dave Love <loveshack@fedoraproject.org> - 1.8.1-2
- Fix bogus specification of soversion
  Actually kept at 1.8, not the intended 2.0, despite a few ABI differences
  from version 1.8.

* Thu Oct 26 2017 Dave Love <loveshack@fedoraproject.org> - 1.8.1-1
- New version
- Drop libxsmm-make.patch

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.8-2
- Rebuild due to bug in RPM (RHBZ #1468476)

* Tue May  2 2017 Dave Love <loveshack@fedoraproject.org> - 1.8-1
- Update soversion
- Ship libxsmm_convwino_generator
- New version

* Mon Feb 13 2017 Dave Love <loveshack@fedoraproject.org> - 1.6.3-1
- New version
  (Moving past 1.6.3 means more serious ABI changes.)

* Sun Feb 05 2017 Kalev Lember <klember@redhat.com> - 1.6.1-2
- Rebuilt for libgfortran soname bump

* Wed Dec  7 2016 Dave Love <loveshack@fedoraproject.org> - 1.6.1-1
- New version
- Some ABI incompatibility, but kept major sover as not made stable yet
  and in view of https://github.com/hfp/libxsmm/issues/120

* Wed Nov  9 2016 Dave Love <loveshack@fedoraproject.org> - 1.5.2-2
- Remove -doc dependencies

* Fri Nov  4 2016 Dave Love <loveshack@fedoraproject.org> - 1.5.2-1
- New version

* Thu Nov  3 2016 Dave Love <loveshack@fedoraproject.org> - 1.5.1-2
- Clean samples .make files too
- Use OMP build default
- Define FCFLAGS, LDFLAGS

* Mon Oct 31 2016 Dave Love <loveshack@fedoraproject.org> - 1.5.1-1
- New version, fixing interface bug
- Spec fixes from review
- Add samples to doc

* Wed Oct 26 2016 Dave Love <loveshack@fedoraproject.org> - 1.5-4
- Don't install .mod file directly in _includedir
- Don't build for ix86
- BR python

* Tue Oct 11 2016 Dave Love <loveshack@fedoraproject.org> - 1.5-3
- Install with STATIC=0
- Avoid sse3
- Fix Fortran modules installation and %%_fmoddir ownership

* Wed Oct  5 2016 Dave Love <loveshack@fedoraproject.org> - 1.5-2
- Fix installation of libraries

* Wed Oct  5 2016 Dave Love <loveshack@fedoraproject.org> - 1.5-1
- New version
- Remove %%check (run in %%build)

* Sat Aug 20 2016 Dave Love <loveshack@fedoraproject.org> - 1.4.4-2
- Drop devtoolset on el6 (not needed)

* Thu Aug 18 2016 Dave Love <loveshack@fedoraproject.org> - 1.4.4-1
- New version, with bumped soname
- Drop patch
- Modify install section

* Sat May 21 2016 Dave Love <loveshack@fedoraproject.org> - 1.4.3-1
- New version
- Fix debuginfo

* Mon May  9 2016 Dave Love <loveshack@fedoraproject.org> - 1.4.1-1
- New version
- Link --as-needed

* Mon Apr 25 2016 Dave Love <loveshack@fedoraproject.org> - 1.4-2
- Use PREFETCH=1

* Wed Apr  6 2016 Dave Love <loveshack@fedoraproject.org> - 1.4-1
- New version

* Fri Apr  1 2016 Dave Love <loveshack@fedoraproject.org> - 1.3-2
- Install README.md, and maybe README.EPEL6

* Fri Apr  1 2016 Dave Love <loveshack@fedoraproject.org> - 1.3-1
- New version
- Sanitize spec a bit

* Mon Feb 22 2016 Dave Love <loveshack@fedoraproject.org> - 1.2-1
- New version

* Sun Jan 24 2016 Dave Love <loveshack@fedoraproject.org> - 1.1.1-2
- Install Fortran module in %%_fmoddir

* Wed Dec 30 2015 Dave Love <loveshack@fedoraproject.org> - 1.1.1-1
- New version
- Add check
- BR python
- Make it serial, not openmp, for now
- Add doc subpackage

* Wed Dec  2 2015 Dave Love <loveshack@fedoraproject.org> - 1.0.1-1
- New version

* Wed Oct  7 2015 Dave Love <loveshack@fedoraproject.org> - 0.9.1-1
- Initial packaging
