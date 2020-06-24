%global commit 287007567ba3998b4b70119025c3def86bdef649
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           gdl
Version:        0.9.9
Release:        15.20190915git%{shortcommit}%{?dist}
Summary:        GNU Data Language

License:        GPLv2+
URL:            http://gnudatalanguage.sourceforge.net/
#Source0:        https://github.com/gnudatalanguage/gdl/archive/v%{version}/gdl-%{version}.tar.gz
Source0:        https://github.com/gnudatalanguage/gdl/archive/%{commit}/gdl-%{version}-git-%{shortcommit}.tar.gz
Source1:        gdl.csh
Source2:        gdl.sh
Source4:        xorg.conf
# Build with system antlr library.  Request for upstream change here:
# https://sourceforge.net/tracker/index.php?func=detail&aid=2685215&group_id=97659&atid=618686
Patch1:         gdl-antlr.patch
# Support python3
# https://github.com/gnudatalanguage/gdl/pull/468
Patch2:         gdl-python3.patch
# Fix conflict with std::vector and ALTIVEC vector
# https://github.com/gnudatalanguage/gdl/pull/535
Patch4:         gdl-std.patch

%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires:  gcc-c++
BuildRequires:  antlr-C++
BuildRequires:  antlr-tool
BuildRequires:  java-devel
%endif
%if 0%{?rhel} == 6
BuildRequires:  antlr
BuildRequires:  java
%endif
BuildRequires:  expat-devel, readline-devel, ncurses-devel
BuildRequires:  gsl-devel, plplot-devel, GraphicsMagick-c++-devel
BuildRequires:  netcdf-devel, hdf5-devel, libjpeg-devel
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  python%{python3_pkgversion}-devel, python%{python3_pkgversion}-numpy, python%{python3_pkgversion}-matplotlib
%else
BuildRequires:  python2-devel, python2-numpy, python2-matplotlib
%endif
BuildRequires:  shapelib-devel
BuildRequires:  fftw-devel, hdf-static
%if 0%{?fedora} || 0%{?rhel} >= 8
# eccodes not available on these arches
%ifnarch i686 ppc64 s390x armv7hl
BuildRequires:  eccodes-devel
%else
BuildRequires:  grib_api-devel
%endif
%else
# eccodes not available on these arches
%ifnarch i686 ppc64 s390x armv7hl aarch64
BuildRequires:  eccodes-devel
%else
BuildRequires:  grib_api-static
%endif
%endif
BuildRequires:  eigen3-static
BuildRequires:  libgeotiff-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtirpc-devel
#TODO - Build with mpi support
#BuildRequires:  mpich2-devel
BuildRequires:  pslib-devel
# qhull too old on Fedora 24 and EPEL7
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  qhull-devel
%global cmake_qhull -DQHULL=ON
%endif
BuildRequires:  udunits2-devel
BuildRequires:  wxGTK3-devel
BuildRequires:  cmake3
# For tests
BuildRequires:  xorg-x11-drv-dummy
BuildRequires:  metacity
# Needed to pull in drivers
Requires:       plplot
Requires:       %{name}-common = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}
# Need to match hdf5 compile time version
Requires:       hdf5 = %{_hdf5_version}


%description
A free IDL (Interactive Data Language) compatible incremental compiler
(i.e. runs IDL programs). IDL is a registered trademark of Research
Systems Inc.


%package        common
Summary:        Common files for GDL
Requires:       %{name}-runtime = %{version}-%{release}
BuildArch:      noarch

%description    common
Common files for GDL


%if 0%{?fedora} >= 29 || 0%{?rhel} >= 8
%package        -n python%{python3_pkgversion}-gdl
%{?python_provide:%python_provide python%{python3_pkgversion}-gdl}
# Remove before F30
Provides: %{name}-python = %{version}-%{release}
Provides: %{name}-python%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-python < %{version}-%{release}
Summary:        GDL python module
# Needed to pull in drivers
Requires:       plplot
Requires:       %{name}-common = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description    -n python%{python3_pkgversion}-gdl
%{summary}.
%else
%package        -n python2-gdl
%{?python_provide:%python_provide python2-gdl}
# Remove before F30
Provides: %{name}-python = %{version}-%{release}
Provides: %{name}-python%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-python < %{version}-%{release}
Summary:        GDL python module
# Needed to pull in drivers
Requires:       plplot
Requires:       %{name}-common = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description    -n python2-gdl
%{summary}.
%endif


%prep
%setup -q -n %{name}-%{commit}
rm -rf src/antlr
%patch1 -p1 -b .antlr
%patch2 -p1 -b .python3
%patch4 -p1 -b .std

pushd src
for f in *.g
do
  antlr $f
done
popd

%if 0%{?fedora} >= 29 || 0%{?rhel} >= 8
%global __python %{__python3}
%global python_sitearch %{python3_sitearch}
%else
%global __python %{__python2}
%global python_sitearch %{python2_sitearch}
%endif
%global cmake_opts \\\
   -DWXWIDGETS=ON \\\
   -DGEOTIFF_INCLUDE_DIR=%{_includedir}/libgeotiff \\\
   -DUDUNITS=ON \\\
   -DUDUNITS_INCLUDE_DIR=%{_includedir}/udunits2 \\\
   -DGRIB=ON \\\
   -DOPENMP=ON \\\
   -DPYTHON_EXECUTABLE=%{__python} \\\
   %{?cmake_qhull} \\\
%{nil}
# TODO - build an mpi version
#           INCLUDES="-I/usr/include/mpich2" \
#           --with-mpich=%{_libdir}/mpich2 \

%build
mkdir build build-python
#Build the standalone executable
pushd build
%cmake3 %{cmake_opts} ..
make #{?_smp_mflags}
popd
#Build the python module
pushd build-python
%cmake3 %{cmake_opts} -DPYTHON_MODULE=ON ..
make #{?_smp_mflags}
popd


%install
pushd build
make install DESTDIR=$RPM_BUILD_ROOT
popd
pushd build-python
make install DESTDIR=$RPM_BUILD_ROOT
# Install the python module in the right location
install -d -m 0755 $RPM_BUILD_ROOT/%{python_sitearch}
%if 0%{?fedora} >= 29 || 0%{?rhel} >= 8
%if "%{_lib}" != "lib"
mv $RPM_BUILD_ROOT%{_prefix}/lib/python*/site-packages/GDL.so \
  $RPM_BUILD_ROOT%{python_sitearch}/GDL.so
%endif
%else
mv $RPM_BUILD_ROOT%{_prefix}/lib/site-python/GDL.so \
  $RPM_BUILD_ROOT%{python_sitearch}/GDL.so
%endif
popd

# Install the profile file to set GDL_PATH
install -d -m 0755 $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d
install -m 0644 %SOURCE1 $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d
install -m 0644 %SOURCE2 $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d


%check
cd build
cp %SOURCE4 .
if [ -x /usr/libexec/Xorg ]; then
   Xorg=/usr/libexec/Xorg
elif [ -x /usr/libexec/Xorg.bin ]; then
   Xorg=/usr/libexec/Xorg.bin
else
   # Strip suid root
   cp /usr/bin/Xorg .
   Xorg=./Xorg
fi
$Xorg -noreset +extension GLX +extension RANDR +extension RENDER -logfile ./xorg.log -config ./xorg.conf -configdir . :99 &
export DISPLAY=:99

metacity &
sleep 2
# bytscl - https://github.com/gnudatalanguage/gdl/issues/159
# device - Failed on EL7
# fft_leak - https://github.com/gnudatalanguage/gdl/issues/147
# file_delete - https://github.com/gnudatalanguage/gdl/issues/148
# file_test - https://github.com/gnudatalanguage/gdl/issues/534
# fix - https://github.com/gnudatalanguage/gdl/issues/149
# formats - https://github.com/gnudatalanguage/gdl/issues/144
# get_screen_size - Failed on EL7
# n_tags - https://github.com/gnudatalanguage/gdl/issues/150
# parse_url - https://github.com/gnudatalanguage/gdl/issues/153
# resolve_routine - https://github.com/gnudatalanguage/gdl/issues/146
# rounding - https://github.com/gnudatalanguage/gdl/issues/154
# total - https://github.com/gnudatalanguage/gdl/issues/155
failing_tests='test_(bytscl|device|fft_leak|file_(delete|test)|finite|fix|formats|get_screen_size|idlneturl|make_dll|n_tags|parse_url|resolve_routine|rounding|total|wait)'
%ifarch aarch64 ppc %{power64}
# test_fix fails currently on arm
# https://sourceforge.net/p/gnudatalanguage/bugs/622/
# https://bugzilla.redhat.com/show_bug.cgi?id=990749
failing_tests="$failing_tests|test_(fix|hdf5)"
%endif
%ifarch aarch64
# new test failues - indgen, list - https://github.com/gnudatalanguage/gdl/issues/372
# Bug tests hang on F28
failing_tests="$failing_tests|test_(bug_(3104209|3104326|3147733)|file_lines|indgen|list|l64|step|xdr)"
%endif
%ifarch %{arm}
# These fail on 32-bit: test_formats test_xdr
failing_tests="$failing_tests|test_(file_lines|fix|formats|hdf5|indgen|list|l64|xdr)"
%endif
%ifarch %{ix86}
# binfmt - https://github.com/gnudatalanguage/gdl/issues/332
# These fail on 32-bit: test_formats test_xdr
failing_tests="$failing_tests|test_(formats|l64|sem|xdr)"
%endif
%ifarch ppc64
# new test failues - indgen, list - https://github.com/gnudatalanguage/gdl/issues/372
failing_tests="$failing_tests|test_(bug_(635|3104209|3147733)|file_lines|indgen|list|save_restore|window_background)"
%endif
%ifarch ppc64le
# ppc64le - test_file_lines https://github.com/gnudatalanguage/gdl/issues/373
failing_tests="$failing_tests|test_(angles|bug_(3104209|3104326)|container|file_lines|hdf5|hist_2d|indgen|list|random)"
%endif
%ifarch s390x
failing_tests="$failing_tests|test_(bug_635|deriv|file_lines|hdf5|indgen|list|save_restore|tic_toc|window_background)"
%endif
make check VERBOSE=1 ARGS="-V -E '$failing_tests'"
%ifnarch ppc64 s390x
# test_save_restore hangs on ppc64 s390x
make check VERBOSE=1 ARGS="-V -R '$failing_tests' --timeout 600" || :
%endif
kill %1 || :
cat xorg.log


%files
%license COPYING
%doc AUTHORS ChangeLog HACKING NEWS README
%config(noreplace) %{_sysconfdir}/profile.d/gdl.*sh
%{_bindir}/gdl
%{_mandir}/man1/gdl.1*

%files common
%{_datadir}/gnudatalanguage/

%if 0%{?fedora} >= 29 || 0%{?rhel} >= 8
%files -n python%{python3_pkgversion}-gdl
%else
%files -n python2-gdl
%endif
%{python_sitearch}/GDL.so


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.9-15.20190915git2870075
- Rebuilt for Python 3.9

* Thu Apr 02 2020 Björn Esser <besser82@fedoraproject.org> - 0.9.9-14.20190915git2870075
- Fix string quoting for rpm >= 4.16
- Add BR: expat-devel

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-13.20190915git2870075
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 29 2019 Orion Poplawski <orion@nwra.com> - 0.9.9-12.20190915git2870075
- Rebuild for plplot 5.15

* Tue Sep 17 2019 Orion Poplawski <orion@nwra.com> - 0.9.9-11.20190915git2870075
- Update to latest git

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.9.9-10
- Rebuilt for GSL 2.6.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.9-9
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com> - 0.9.9-7
- Rebuild for hdf5 1.10.5

* Fri Feb 22 2019 Orion Poplawski <orion@nwra.com> - 0.9.9-6
- test_bug_635 fails on F28 ppc64

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.9-5
- Rebuild for readline 8.0

* Wed Feb 13 2019 Orion Poplawski <orion@nwra.com> - 0.9.9-4
- Use eccodes where available
- Add patches to fix build
- Use cmake3 for EPEL7 compat

* Wed Feb 13 2019 Orion Poplawski <orion@nwra.com> - 0.9.9-3
- Rebuild for plplot 5.14

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 1 2018 Orion Poplawski <orion@nwra.com> - 0.9.9-1
- Update to 0.9.9

* Wed Oct 31 2018 Orion Poplawski <orion@nwra.com> - 0.9.8-7.20180919gitd892ee5
- Really use eccodes by fixing typo (bug #1644928)

* Thu Sep 20 2018 Orion Poplawski <orion@nwra.com> - 0.9.8-6.20180919gitd892ee5
- Update to latest git
- Port to python 3

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.9.8-5.20180723gitf3b6e01
- Rebuild with fixed binutils

* Mon Jul 23 2018 Orion Poplawski <orion@nwra.com> - 0.9.8-4.20180723gitf3b6e01
- Update to latest git
- Switch to eccodes from grib_api for Fedora 28+

* Sun Jul 22 2018 Scott Talbert <swt@techie.net> - 0.9.8-3
- Rebuild with wxWidgets 3.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 20 2018 Orion Poplawski <orion@cora.nwra.com> - 0.9.8-1
- Update to 0.9.8
- Drop parallel make for now
- Use libtirpc
- Switch to Xorg dummy driver for tests, fail build on test failure
- Add patch to fix ppc64 altivec vector usage
- Add patches to fix various warnings

* Thu Mar 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.7-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 21 2018 Orion Poplawski <orion@cora.nwra.com> - 0.9.7-10
- Explicitly use python2
- Build with libtirpc

* Tue Feb 20 2018 Orion Poplawski <orion@cora.nwra.com> - 0.9.7-10
- Rebuild for hdf5 1.8.20

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9.7-8
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9.7-7
- Python 2 binary package renamed to python2-gdl
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 23 2017 Tom Callaway <spot@fedoraproject.org> - 0.9.7-4
- rebuild for plplot 5.12.0

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 1 2017 Orion Poplawski <orion@cora.nwra.com> - 0.9.7-1
- Update to 0.9.7

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.9.6-10
- Rebuild for readline 7.x

* Wed Dec 28 2016 Rich Mattes <richmattes@gmail.com> - 0.9.6-9
- Rebuild for eigen3-3.3.1

* Mon Sep 26 2016 Orion Poplawski <orion@cora.nwra.com> - 0.9.6-8
- Keep tabs on failing tests

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 29 2016 Orion Poplawski <orion@cora.nwra.com> - 0.9.6-6
- Rebuild for hdf5 1.8.17

* Thu Mar 3 2016 Orion Poplawski <orion@cora.nwra.com> - 0.9.6-5
- Add patch to build with gcc 6

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 0.9.6-4
- Rebuild for gsl 2.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Orion Poplawski <orion@cora.nwra.com> - 0.9.6-2
- Rebuild for netcdf 4.4.0

* Thu Jan 7 2016 Orion Poplawski <orion@cora.nwra.com> - 0.9.6-1
- Update to 0.9.6
- Drop setting -DH5_USE_16_API and -fPIC
- Drop plplot patch applied upstream
- Add patch to fix file_move test
- Run tests with Xvfb and metacity
- Use %%license

* Sun Oct 04 2015 Rex Dieter <rdieter@fedoraproject.org> - 0.9.5-10
- rebuild (GraphicsMagick)

* Wed Jul 15 2015 Orion Poplawski <orion@cora.nwra.com> - 0.9.5-9
- Rebuild for grib_api 1.14.0 soname bump

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 17 2015 Orion Poplawski <orion@cora.nwra.com> - 0.9.5-7
- Rebuild for hdf5 1.8.15

* Fri Apr 24 2015 Orion Poplawski <orion@cora.nwra.com> - 0.9.5-6
- Add patch for plplot 5.11.0 support

* Mon Mar 09 2015 Rex Dieter <rdieter@fedoraproject.org> 0.9.5-5
- rebuild (GraphicsMagick)

* Wed Jan 07 2015 Orion Poplawski <orion@cora.nwra.com> - 0.9.5-4
- Rebuild for hdf5 1.8.4

* Tue Nov 18 2014 Orion Poplawski <orion@cora.nwra.com> - 0.9.5-3
- Exclude test_zip

* Fri Oct 31 2014 Orion Poplawski <orion@cora.nwra.com> - 0.9.5-2
- No longer need cmake28 on RHEL6

* Wed Oct 8 2014 Orion Poplawski <orion@cora.nwra.com> - 0.9.5-1
- Update to 0.9.5

* Fri Oct 3 2014 Orion Poplawski <orion@cora.nwra.com> - 0.9.4-7
- Re-enable openmp.  Appears to be working now.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 23 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.9.4-5
- Disable tests which fail on aarch64 (#990749)

* Tue Jun 10 2014 Orion Poplawski <orion@cora.nwra.com> - 0.9.4-4
- Fix python find_package usage

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Dec 28 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9.4-2
- Rebuild for hdf5 1.8.12

* Tue Oct 8 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9.4-1
- Disable openmp for now due to issues with eigen3 matrix multiply

* Fri Oct 4 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9.4-1
- Add patch to fix use of dynamically sized matrices with Eigen3
- Add patch to fix -Wreorder warnings
- Update gsl patch to match current cvs

* Mon Sep 30 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9.4-1
- Update to 0.9.4
- Update build patch - drop automake components
- New python patch to fix python build
- Add patch to fix gsl usage
- Add patch for test debugging

* Tue Aug 27 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9.3-10.cvs20130804
- Add patch to support new width() method in plplot

* Fri Aug 23 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9.3-10.cvs20130804
- Build with shared grib_api

* Sun Aug 4 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9.3-9.cvs20130804
- Update cvs patch to current cvs
- Drop test_ce patch, enable test_ce

* Wed Jul 31 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9.3-8.cvs20130731
- Update cvs patch to current cvs
- Add patch to fix segfault in test_ce
- Cleanup test excludes, note bugs for failing tests

* Thu May 16 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9.3-7.cvs20130516
- Update cvs patch to current cvs
- Drop test_ce,tests, netcdf, and python patch applied upstream
- Rebuild for hdf5 1.8.11
- Switch to GraphicsMagick

* Fri Mar 22 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9.3-6.cvs20130321
- Update cvs patch to current cvs
- Add patch to use python 2 with cmake

* Wed Mar 20 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9.3-5
- Add patch to handle netcdf better with cmake
- BR netcdf-devel instead of netcdf-cxx-devel

* Fri Mar 15 2013 Orion Poplawski <orion@cora.nwra.com> - 0.9.3-4
- Change to use cmake
- Update to current cvs via patch
- Add patches to fix tests under cmake
- Build with eigen3

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 0.9.3-2
- rebuild due to "jpeg8-ABI" feature drop

* Thu Dec 27 2012 Orion Poplawski <orion@cora.nwra.com> - 0.9.3-1
- Update to 0.9.3
- Rebase antlr-auto patch

* Mon Dec 3 2012 Orion Poplawski <orion@cora.nwra.com> - 0.9.2-10.cvs20120717
- Rebuild for hdf5 1.8.10

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-9.cvs20120717
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 17 2012 Orion Poplawski <orion@cora.nwra.com> - 0.9.2-8.cvs20120717
- Update to current cvs
- Drop env patch fixed upstream

* Mon Jul 16 2012 Orion Poplawski <orion@cora.nwra.com> - 0.9.2-7.cvs20120716
- Update to current cvs

* Tue May 15 2012 Orion Poplawski <orion@cora.nwra.com> - 0.9.2-6.cvs20120515
- Update to current cvs
- Add patch for testsuite make check to work in build directory
- Add patch to fix pythongdl.c compile
- Run the testsuite properly with make check

* Wed Mar 21 2012 Orion Poplawski <orion@cora.nwra.com> - 0.9.2-5
- Rebuild antlr generated files
- Rebuild for ImageMagick

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-4
- Rebuilt for c++ ABI breakage

* Sat Jan 7 2012 Orion Poplawski <orion@cora.nwra.com> - 0.9.2-3
- Build with pslib

* Wed Nov 16 2011 Orion Poplawski <orion@cora.nwra.com> - 0.9.2-2
- Rebuild for hdf5 1.8.8

* Fri Nov 11 2011 Orion Poplawski <orion@cora.nwra.com> - 0.9.2-1
- Update to 0.9.2
- Drop upstreamed patches
- Drop hdf support from python module, add patch to force building of python
  shared library

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-5
- Rebuilt for glibc bug#747377

* Thu Aug 18 2011 Orion Poplawski <orion@cora.nwra.com> - 0.9.1-4
- Rebuild for plplot 5.9.8
- Add upstream patch to fix strsplit and str_sep
- Add patch to fix compile issues with string
- Add patch to change plplot SetOpt to setopt

* Tue May 17 2011 Orion Poplawski <orion@cora.nwra.com> - 0.9.1-3
- Rebuild for hdf5 1.8.7

* Thu Mar 31 2011 Orion Poplawski <orion@cora.nwra.com> - 0.9.1-2
- Rebuild for netcdf 4.1.2

* Tue Mar 29 2011 Orion Poplawski <orion@cora.nwra.com> - 0.9.1-1
- Update to 0.9.1
- Drop numpy and wx patches fixed upstream

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 11 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-5
- Rebuild for plplot 5.9.7

* Wed Sep 29 2010 jkeating - 0.9-4
- Rebuilt for gcc bug 634757

* Wed Sep 15 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-3
- Fix GDL_PATH in profile scripts (bug #634351)

* Wed Sep 15 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-2
- Rebuild for new ImageMagick

* Mon Aug 30 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-1
- Update to 0.9 final

* Thu Aug 26 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.17.rc4
- Add initial patch to build the python module with numpy rather than
  numarray.  Doesn't work yet, but the python module is mostly dead anyway

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.9-0.16.rc4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 0.9-0.15.rc4
- rebuilt against wxGTK-2.8.11-2

* Wed Jul 7 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.14.rc4
- Update to today's cvs
- Drop wx-config patch
- Re-instate wx patch to avoid segfault on test exit

* Thu Jun 3 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.13.rc4
- Update to today's cvs
- Drop GLDLexer and python patches
- BR antlr-C++ on Fedora 14+

* Mon Mar 22 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.12.rc4
- Drop unused BR on proj-devel (bug #572616)

* Mon Mar 8 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.11.rc4
- Rebuild for new ImageMagick

* Wed Feb 17 2010 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.10.rc4
- Update to 0.9rc4
- Enable grib, udunits2, and wxWidgets support
- Build python module and add sub-package for it
- Use %%global instead of %%define

* Tue Dec  8 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 0.9-0.9.rc3
- Explicitly BR hdf-static in accordance with the Packaging
  Guidelines (hdf-devel is still static-only).

* Wed Nov 11 2009 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.8.rc3
- Rebuild for netcdf-4.1.0

* Thu Oct 15 2009 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.7.rc3
- Update to 0.9rc3
- Drop gcc43, ppc64, friend patches fixed upstream
- Add source for makecvstarball
- Rebase antlr patch, add automake source version
- Add conditionals for EPEL builds
- Add %%check section

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-0.6.rc2.20090312
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 16 2009 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.5.rc2.20090312
- Back off building python module until configure macro is updated

* Thu Mar 12 2009 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.4.rc2.20090312
- Update to 0.9rc2 cvs 20090312
- Rebase antlr patch
- Rebuild for new ImageMagick

* Thu Feb 26 2009 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.3.rc2.20090224
- Build python module
- Move common code to noarch common sub-package

* Tue Feb 24 2009 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.2.rc2.20090224
- Update to 0.9rc2 cvs 20090224
- Fix release tag
- Drop ImageMagick patch fixed upstream
- Add patch to compile with gcc 4.4.0 - needs new friend statement
- Don't build included copy of antlr, use system version

* Fri Jan 23 2009 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.rc2.1
- Update to 0.9rc2 based cvs

* Sun Nov 30 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.9-0.rc1.4.1
- Rebuild for Python 2.6

* Fri Sep  5 2008 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.rc1.4
- Add a requires on plplot to pull in drivers (bug#458277)

* Fri May 16 2008 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.rc1.3
- Update to latest cvs
- Add patch to handle new ImageMagick
- Update netcdf locations

* Mon Apr 28 2008 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.rc1.2
- Rebuild for new ImageMagick

* Sat Apr  5 2008 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.rc1.1
- Update to 0.9rc1

* Mon Mar 17 2008 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre6.2
- Update cvs patch to latest cvs

* Tue Mar 4 2008 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre6.1
- Rebuild for gcc 4.3, and add patch for gcc 4.3 support
- Add patch to build against plplot 5.9.0
- Add cvs patch to update to latest cvs

* Fri Nov  2 2007 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre6
- Update to 0.9pre6

* Tue Aug 21 2007 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre5.2
- Add patch to fix build on ppc64

* Tue Aug 21 2007 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre5.1
- Update license tag to GPLv2+
- Rebuild for BuildID

* Mon Jul  9 2007 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre5
- Update to 0.9pre5

* Tue May 22 2007 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre4.2
- Rebuild for netcdf 3.6.2 with shared libraries

* Tue Jan  9 2007 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre4.1
- Package the library routines and point to them by default

* Fri Jan  5 2007 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre4
- Update to 0.9pre4

* Mon Dec 18 2006 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre3.4
- Add patch for configure to handle python 2.5

* Thu Dec 14 2006 - Jef Spaleta <jspaleta@gmail.com> - 0.9-0.pre3.3
- Bump and build for python 2.5

* Wed Nov 22 2006 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre3.2
- Update to 0.9pre3

* Wed Oct  4 2006 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre3.1
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Sep 18 2006 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre3
- Rebuild for FC6
- Add patch for specialization error caught by gcc 4.1.1

* Thu Jun 29 2006 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre2
- Update to 0.9pre2

* Sun Jun 11 2006 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre.1
- Rebuild for ImageMagick so bump

* Mon Apr  3 2006 Orion Poplawski <orion@cora.nwra.com> - 0.9-0.pre
- Update to 0.9pre

* Fri Feb 24 2006 Orion Poplawski <orion@cora.nwra.com> - 0.8.11-4
- Add --with-fftw to configure

* Thu Feb  2 2006 Orion Poplawski <orion@cora.nwra.com> - 0.8.11-3
- Enable hdf for ppc
- Change fftw3 to fftw

* Tue Jan  3 2006 Orion Poplawski <orion@cora.nwra.com> - 0.8.11-2
- Rebuild

* Mon Nov 21 2005 Orion Poplawski <orion@cora.nwra.com> - 0.8.11-1
- Upstream 0.8.11
- Remove hdf patch fixed upstream
- Remove X11R6 lib path - not needed with modular X

* Wed Nov 16 2005 Orion Poplawski <orion@cora.nwra.com> - 0.8.10-4
- Update for new ImageMagick version

* Thu Sep 22 2005 Orion Poplawski <orion@cora.nwra.com> - 0.8.10-3
- Disable hdf with configure on ppc

* Thu Sep 22 2005 Orion Poplawski <orion@cora.nwra.com> - 0.8.10-2
- Don't include hdf support on ppc

* Fri Aug 19 2005 Orion Poplawski <orion@cora.nwra.com> - 0.8.10-1
- Initial Fedora Extras version
