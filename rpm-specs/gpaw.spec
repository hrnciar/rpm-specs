# Warning:
# Anyone editing this spec file please make sure the same spec file
# works on other fedora and epel releases, which are supported by this software.
# No quick Rawhide-only fixes will be allowed.

%if 0%{?el6} || 0%{?el7}
gpaw-1.5 requires numpy 1.9 or newer
%quit
%endif

%if 0%{?el6}
# Error: No Package found for mpich-devel on el6
ExcludeArch: ppc64
%endif

%if 0%{?fedora} >= 21 || 0%{?el7} || 0%{?el6}
%global blacs_libs 'mpiblacs'
%else
%global	blacs_libs 'mpiblacsCinit', 'mpiblacs'
%endif

Name:			gpaw
Version:		20.1.0
Release:		2%{?dist}
Summary:		A grid-based real-space PAW method DFT code

License:		GPLv3+
URL:			https://wiki.fysik.dtu.dk/gpaw/
# Note that this is aadc02d3791ca874ec683ab46f1af369d2c10dd1 due to https://gitlab.com/gpaw/gpaw/-/issues/266
Source0:		https://gitlab.com/%{name}/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz


BuildRequires:		time
BuildRequires:		libxc-devel
BuildRequires:		openblas-devel

BuildRequires:		python3-devel
BuildRequires:		python3-pytest
BuildRequires:		python3-scipy
BuildRequires:		python3-setuptools

BuildRequires:		python3-ase


BuildRequires:		%{name}-setups


%global desc_base \
GPAW is a density-functional theory (DFT) Python code based\
on the projector-augmented wave (PAW) method and the\
atomic simulation environment (ASE). It uses real-space uniform grids and\
multigrid methods or atom-centered basis-functions.

%global _description\
%{desc_base}

%description %_description

%package common
Summary:		%{name} - common files
Requires:		%{name}-setups
BuildArch:		noarch

%description common
%{desc_base}

This package contains the common data files.


%package -n python3-%{name}
Summary:		A grid-based real-space PAW method DFT code for Python 3
Requires:		python3-ase
Requires:		python3-scipy
Requires:		%{name}-common = %{version}-%{release}

%description -n python3-%{name}
%{desc_base}

%package -n python3-%{name}-openmpi
Summary:		python3-%{name} - openmpi version
BuildRequires:		openssh-clients
BuildRequires:		openmpi-devel
BuildRequires:		scalapack-openmpi-devel
BuildRequires:		blacs-openmpi-devel
Requires:		%{name}-common = %{version}-%{release}
%if 0%{?el6}
BuildRequires:		scalapack-openmpi
BuildRequires:		blacs-openmpi
%endif
%if 0%{?el7} || 0%{?el6}
Requires:		scalapack-openmpi
Requires:		blacs-openmpi
%endif

%description -n python3-%{name}-openmpi
%{desc_base}

This package contains the openmpi Python 3 version.

%package -n python3-%{name}-mpich
Summary:		python3-%{name} - mpich version
BuildRequires:		mpich-devel
BuildRequires:		scalapack-mpich-devel
BuildRequires:		blacs-mpich-devel
Requires:		%{name}-common = %{version}-%{release}
%if 0%{?el6}
BuildRequires:		scalapack-mpich
BuildRequires:		blacs-mpich
%endif
%if 0%{?el7} || 0%{?el6}
Requires:		scalapack-mpich
Requires:		blacs-mpich
%endif

%description -n python3-%{name}-mpich
%{desc_base}

This package contains the mpich Python 3 version.


%prep
%setup -qTc -a 0
pushd %{name}-%{version}
popd

mv %{name}-%{version} python3

# create siteconfig.py
cp python3/siteconfig_example.py python3/siteconfig.py
# replace Debian-centric naming of scalapack/blacs
sed -i "s/scalapack-openmpi/scalapack/" python3/siteconfig.py
sed -i "s/blacsCinit-openmpi/scalapack/" python3/siteconfig.py
sed -i "s/blacs-openmpi/scalapack/" python3/siteconfig.py

cp -p python3/LICENSE .

# fix the shebangs python version in the scripts
find python3/tools -type f | xargs sed -i '1s|^#!/usr/bin/env python.*|#!%{_bindir}/python3|'


%build
%set_build_flags

# To avoid replicated code define a macro
%global dobuild() \
cat siteconfig.py \
${PYTHON} setup.py build && \
mv build build$MPI_SUFFIX && \
${PYTHON} setup.py clean

# disable scalapack
sed -i 's/# scalapack =.*/scalapack = False/' python3/siteconfig.py
# enable openblas
echo "libraries += ['openblas']" >> python3/siteconfig.py
# force -fPIC
echo "extra_compile_args += ['-fPIC']" >> python3/siteconfig.py
# specify MPI_INCLUDE (use /usr/include for serial build)
echo "import os" >> python3/siteconfig.py
echo "include_dirs += [os.environ.get('MPI_INCLUDE', '/usr/include')]" >> python3/siteconfig.py

# build serial version
pushd python3
MPI_SUFFIX=_serial PYTHON=python3 %dobuild
popd

# build openmpi version
%{_openmpi_load}
# enable scalapack
sed -i 's/.*scalapack =.*/scalapack = True/' python3/siteconfig.py
%if 0%{?fedora} < 32
sed -i "s/'scalapack'/%{blacs_libs}, 'scalapack'/" python3/siteconfig.py
%endif
# force mpicc
sed -i 's/# compiler =.*/compiler = "mpicc"/' python3/siteconfig.py
which mpicc
mpicc --version
mpicc foo.c --showme
pushd python3
PYTHON=python3 %dobuild
popd
%{_openmpi_unload}

# build mpich version
%{_mpich_load}
# enable scalapack
sed -i 's/.*scalapack =.*/scalapack = True/' python3/siteconfig.py
%if 0%{?fedora} < 32
sed -i "s/'scalapack'/%{blacs_libs}, 'scalapack'/" python3/siteconfig.py
%endif
# force mpicc
sed -i 's/# compiler =.*/compiler = "mpicc"/' python3/siteconfig.py
which mpicc
mpicc --version
mpicc -compile_info
mpicc -link_info
pushd python3
PYTHON=python3 %dobuild
popd
%{_mpich_unload}


%install

# copy python scripts and modules
%global doinstall() \
mkdir -p $RPM_BUILD_ROOT/$MPI_BIN&& \
install -p -m 755 build$MPI_SUFFIX/scripts-*/* $RPM_BUILD_ROOT/$MPI_BIN/&& \
mkdir -p $RPM_BUILD_ROOT/$MPI_PYTHON3_SITEARCH&& \
cp -rp build$MPI_SUFFIX/lib.*/%{name} $RPM_BUILD_ROOT/$MPI_PYTHON3_SITEARCH/&& \
install -p -m 755 build$MPI_SUFFIX/lib.*/*.so $RPM_BUILD_ROOT/$MPI_PYTHON3_SITEARCH/

# install serial version
pushd python3
PYTHON=python3 MPI_SUFFIX="_serial" MPI_BIN=%{_bindir} MPI_PYTHON3_SITEARCH=%{python3_sitearch} %doinstall
popd

# install openmpi version
%{_openmpi_load}
pushd python3
PYTHON=python3 %doinstall
popd
%{_openmpi_unload}

# install mpich version
%{_mpich_load}
pushd python3
PYTHON=python3 %doinstall
popd
%{_mpich_unload}


%check

export NPROC_PARALLEL=2 # test on 4 cores (scalapack test needs that)

export TIMEOUT_OPTS='--preserve-status --kill-after 10 1800'

# To avoid replicated code define a macro
%global docheck() \
GPAW_PLATFORM=$($PYTHON -c "from distutils import util, sysconfig; print(util.get_platform()+'-'+sysconfig.get_python_version())")&& \
export PYTHONPATH=`pwd`/build$MPI_SUFFIX/lib.${GPAW_PLATFORM} \
PATH=`pwd`/tools:${PATH} \
timeout ${TIMEOUT_OPTS} time $GPAW_EXECUTABLE -m ci -v 2>&1 | tee gpaw-test${NPROC}$MPI_SUFFIX.log

# check serial version
pushd python3
MPI_SUFFIX="_serial" PYTHON="python3" GPAW_EXECUTABLE="pytest" NPROC=1 %docheck
popd

# check openmpi version
%{_openmpi_load}
pushd python3
PYTHON="python3" GPAW_EXECUTABLE="mpiexec -np ${NPROC_PARALLEL} pytest" NPROC=${NPROC_PARALLEL} %docheck
popd
%{_openmpi_unload}

# this will fail for mpich2 on el6 - mpd would need to be started ...
# check mpich version
%{_mpich_load}
pushd python3
PYTHON="python3" GPAW_EXECUTABLE="mpiexec -np ${NPROC_PARALLEL} pytest" NPROC=${NPROC_PARALLEL} %docheck
popd
%{_mpich_unload}


%files common
%doc LICENSE
%{_bindir}/%{name}*


%files -n python3-%{name}
%exclude %{_bindir}/%{name}*
%{python3_sitearch}/%{name}
%{python3_sitearch}/_%{name}*.so


%files -n python3-%{name}-openmpi
%exclude %{_libdir}/openmpi/bin
%{python3_sitearch}/openmpi/%{name}
%{python3_sitearch}/openmpi/_%{name}*.so


%files -n python3-%{name}-mpich
%exclude %{_libdir}/mpich/bin
%{python3_sitearch}/mpich/%{name}
%{python3_sitearch}/mpich/_%{name}*.so


%changelog
* Thu Sep 10 2020 Marcin Dulak <Marcin.Dulak@gmail.com> - 20.1.0-2
- Use timeout to kill hanging tests

* Sun Sep 06 2020 Marcin Dulak <Marcin.Dulak@gmail.com> - 20.1.0-1
- New upstream release
- No more gpaw-python binaries
- Instead mpi shared objects and py files are under site-packages/mpi
- Get rid of %%{?_opt_cc_suffix} since mpi modules don't use it for mpi python
- Remove hdf5 dependency
- Copy files instead of python setup.py install
- Add explicit python3-setuptools br
- Print the used siteconfig.py
- Add MPI_INCLUDE to include_dirs (not sure why this is suddenly needed)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.8.1-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 19.8.1-7
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 19.8.1-5
- Fix inline vs static inline issue for gcc-10

* Sun Nov 17 2019 Tom Callaway <spot@fedoraproject.org> - 19.8.1-4
- rebuild for scalapack 2.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 19.8.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 19.8.1-2
- Rebuilt for Python 3.8

* Thu Aug 15 2019 Marcin Dulak <Marcin.Dulak@gmail.com> - 19.8.1-1
- new upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 2019 Marcin Dulak <Marcin.Dulak@gmail.com> - 1.5.2-1
- explicit mpi related requires on epel7/epel6
- new upstream release
- remove python2 build process

* Wed Mar 27 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-12
- Subpackage python2-gpaw has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com> - 1.4.0-11
- Rebuild for hdf5 1.10.5

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 1.4.0-10
- Rebuild for openmpi 3.1.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 23 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.4.0-8
- Still a problem for python2 in previous commit.

* Sun Dec 23 2018 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.4.0-7
- Switch to openblas on s390x as well.
- Fix shebangs (BZ #1661785).

* Sun Jul 15 2018 Marcin Dulak <Marcin.Dulak@gmail.com> - 1.4.0-6
- explicitly use python3/python2, including gpaw-pythonX

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Marcin Dulak <Marcin.Dulak@gmail.com> - 1.4.0-4
- dummy commit to rebuild with f29-python

* Wed Jun 27 2018 Marcin Dulak <Marcin.Dulak@gmail.com> - 1.4.0-3
* patch https://gitlab.com/gpaw/gpaw/issues/147

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-2
- Rebuilt for Python 3.7

* Fri Jun 08 2018 Marcin Dulak <Marcin.Dulak@gmail.com> - 1.4.0-1
- new upstream release
- drop rhel7 support: Numpy 1.9 is required for python-ase
- requires scipy
- no more git commit in tar directory name

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 23 2017 Susi Lehtola <susi.lehtola@iki.fi> - 1.2.0-6
- Rebuild against libxc 4.

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.0-5
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.0-4
- Python 2 binary package renamed to python2-gpaw
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 14 2017 Marcin Dulak <Marcin.Dulak@gmail.com> - 1.2.0-1
- gpaw-1.2.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-28
- Rebuild for Python 3.6

* Fri Oct 21 2016 Orion Poplawski <orion@cora.nwra.com> - 1.1.0-27
- Rebuild for openmpi 2.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-26
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jul 14 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.0-25
- openblas supported on Power64

* Wed Jul 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.0-24
- aarch64 has openblas now
- simplify arch conditionals

* Wed Jul  6 2016 Marcin Dulak <Marcin.Dulak@gmail.com> - 1.1.0-23
- gpaw-1.1.0

* Sat Jun 18 2016 Marcin Dulak <Marcin.Dulak@gmail.com> - 1.0.0-23
- upstream moved to gitlab, upstream update
- python3 package (bug #1323264)

* Thu Apr 21 2016 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.11.0.13004-22
- Rebuild against libxc 3.0.0.

* Sat Feb 13 2016 Marcin Dulak <Marcin.Dulak@gmail.com> - 0.11.0.13004-21
- explicit Requires are needed for scalapack, blacs and hdf5 on el6 (bug #1301922)
- ppc64le needs -std=c99

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0.13004-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Orion Poplawski <orion@cora.nwra.com> - 0.11.0.13004-19
- Rebuild for hdf5 1.8.16

* Thu Dec 17 2015 Marcin Dulak <Marcin.Dulak@gmail.com> - 0.11.0.13004-18
- get rid of old mpich globals

* Mon Dec 14 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 0.11.0.13004-17
- Fix build on aarch64 (#1291383)

* Wed Sep 16 2015 Orion Poplawski <orion@cora.nwra.com> - 0.11.0.13004-16
- Rebuild for openmpi 1.10.0

* Sun Jul 26 2015 Sandro Mani <manisandro@gmail.com> - 0.11.0.13004-15
- Rebuild for RPM MPI Requires Provides Change

* Wed Jul 22 2015 Marcin Dulak <Marcin.Dulak@gmail.com> - 0.11.0.13004-14
- upstream update
- files-attr

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0.11364-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 21 2015 Marcin Dulak <Marcin.Dulak@gmail.com> - 0.10.0.11364-12
- mpi versions Require gpaw

* Sun May 17 2015 Orion Poplawski <orion@cora.nwra.com> - 0.10.0.11364-11
- Rebuild for hdf5 1.8.15

* Sun May  3 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.10.0.11364-10
- Rebuild for changed mpich

* Wed Jan 07 2015 Orion Poplawski <orion@cora.nwra.com> - 0.10.0.11364-9
- Rebuild for hdf5 1.8.14

* Thu Nov 20 2014 Marcin Dulak <Marcin.Dulak@gmail.com> - 0.10.0.11364-8
- new style of linking blacs on EL6
v
* Thu Oct 23 2014 Marcin Dulak <Marcin.Dulak@gmail.com> - 0.10.0.11364-7
- mpich version 3 in EL6
- use atlas on aarch64
- ppc64 on EL7

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0.11364-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Marcin Dulak <Marcin.Dulak@gmail.com> - 0.10.0.11364-5
- explicit Requires

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0.11364-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Marcin Dulak <Marcin.Dulak@gmail.com> 0.10.0.11364-3
- consistent usage of RPM_BUILD_ROOT/RPM_OPT_FLAGS
- hdf5 enabled
- blacs-2.0.2 on fedora >= 21

* Fri May 2 2014 Marcin Dulak <Marcin.Dulak@gmail.com> 0.10.0.11364-2
- %%arm and ppc64 added
- more explicit globs in %%files
- gcc BR removed
- permissions of _gpaw.so fixed

* Tue Apr 8 2014 Marcin Dulak <Marcin.Dulak@gmail.com> 0.10.0.11364-1
- initial version for Fedora
