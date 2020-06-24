%if 0%{?rhel} && 0%{?rhel} >= 8
%global with_python3 1
%global with_python2 0
%endif

%if 0%{?rhel} && 0%{?rhel} < 8
%global with_python3 1
%global with_python2 1
%global dts devtoolset-8-
BuildRequires: %{?dts}gcc, %{?dts}gcc-c++, cmake3
BuildRequires: %{?dts}gcc-gfortran
%endif

%if 0%{?fedora}
%global with_python3 1
%endif

%global with_mpich 1
%global with_openmpi 1

%global petscver 3.13.0
%global pypi_name petsc4py

Name:           %{pypi_name}
Version:        3.13.0
Release:        2%{?dist}
Summary:        Python bindings for MPI PETSc
License:        BSD
URL:            https://bitbucket.org/petsc/%{pypi_name}
Source0:        https://bitbucket.org/petsc/%{pypi_name}/downloads/%{pypi_name}-%{version}.tar.gz

# Set directories where MPI libraries are
Patch0:         %{name}-openmpi_set_dir.patch
Patch1:         %{name}-mpich_set_dir.patch

%if 0%{?with_python3_other}
BuildRequires:  python%{python3_other_pkgversion}-devel
%endif

%description
This package provides Python bindings for PETSc,
the Portable, Extensible Toolkit for Scientific Computation.

%if 0%{?with_openmpi}
%if 0%{?with_python2}
%package -n     python2-%{pypi_name}-openmpi
Summary:        Python2 bindings for OpenMPI PETSc
%{?python_provide:%python_provide python2-%{pypi_name}-openmpi}

BuildRequires:  python2-devel
BuildRequires:  hdf5-openmpi-devel
BuildRequires:  scalapack-openmpi-devel
BuildRequires:  ptscotch-openmpi-devel
BuildRequires:  petsc-openmpi-devel >= %{petscver}
BuildRequires:  python2-numpy, python2-Cython
Requires:       petsc-openmpi%{?_isa} >= %{petscver}
Requires:       hdf5-openmpi%{?_isa}
Requires:       scalapack-openmpi%{?_isa}
Requires:       ptscotch-openmpi%{?_isa}
Requires:       openmpi%{?_isa}
Requires:       MUMPS-openmpi%{?_isa}

%description -n python2-%{pypi_name}-openmpi
This package provides Python2 bindings for OpenMPI PETSc,
the Portable, Extensible Toolkit for Scientific Computation.
%endif

%package -n     %{pypi_name}-openmpi-devel
Summary:        %{pypi_name} devel files

%description -n %{pypi_name}-openmpi-devel
This package provides header files of Python OpenMPI PETsc.

%if 0%{?with_python3}
%package -n     python%{python3_pkgversion}-%{pypi_name}-openmpi
Summary:        Python3 bindings for OpenMPI PETSc
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}-openmpi}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  hdf5-openmpi-devel
BuildRequires:  scalapack-openmpi-devel
BuildRequires:  ptscotch-openmpi-devel
BuildRequires:  petsc-openmpi-devel >= %{petscver}
BuildRequires:  python%{python3_pkgversion}-numpy, python%{python3_pkgversion}-Cython
Requires:       petsc-openmpi%{?_isa} >= %{petscver}
Requires:       hdf5-openmpi%{?_isa}
Requires:       scalapack-openmpi%{?_isa}
Requires:       ptscotch-openmpi%{?_isa}
Requires:       openmpi%{?_isa}
Requires:       MUMPS-openmpi%{?_isa}

%description -n python%{python3_pkgversion}-%{pypi_name}-openmpi
This package provides Python3 bindings for OpenMPI PETSc,
the Portable, Extensible Toolkit for Scientific Computation.

%if 0%{?with_python3_other}
%package -n python%{python3_other_pkgversion}-%{pypi_name}-openmpi
Summary:        Python%{python3_other_pkgversion} bindings for OpenMPI PETSc
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{pypi_name}-openmpi}

BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  hdf5-openmpi-devel
BuildRequires:  scalapack-openmpi-devel
BuildRequires:  ptscotch-openmpi-devel
BuildRequires:  petsc-openmpi-devel >= %{petscver}
BuildRequires:  python%{python3_other_pkgversion}-numpy, python%{python3_other_pkgversion}-Cython
Requires:       petsc-openmpi%{?_isa} >= %{petscver}
Requires:       hdf5-openmpi%{?_isa}
Requires:       scalapack-openmpi%{?_isa}
Requires:       ptscotch-openmpi%{?_isa}
Requires:       openmpi%{?_isa}
Requires:       MUMPS-openmpi%{?_isa}

%description -n python%{python3_other_pkgversion}-%{pypi_name}-openmpi
Python%{python3_other_pkgversion} bindings for OpenMPI PETSc.
%endif
%endif
%endif

%if 0%{?with_mpich}
%if 0%{?with_python2}
%package -n     python2-%{pypi_name}-mpich
Summary:        Python2 bindings for MPICH PETSc
%{?python_provide:%python_provide python2-%{pypi_name}-mpich}

BuildRequires:  python2-devel
BuildRequires:  hdf5-mpich-devel
BuildRequires:  scalapack-mpich-devel
BuildRequires:  ptscotch-mpich-devel
BuildRequires:  petsc-mpich-devel >= %{petscver}
BuildRequires:  python2-numpy, python2-Cython
Requires:       petsc-mpich%{?_isa} >= %{petscver}
Requires:       hdf5-mpich%{?_isa}
Requires:       scalapack-openmpi%{?_isa}
Requires:       ptscotch-mpich%{?_isa}
Requires:       mpich%{?_isa}
Requires:       MUMPS-mpich%{?_isa}

%description -n python2-%{pypi_name}-mpich
This package provides Python2 bindings for MPICH PETSc,
the Portable, Extensible Toolkit for Scientific Computation.
%endif

%package -n     %{pypi_name}-mpich-devel
Summary:        %{pypi_name} devel files

%description -n %{pypi_name}-mpich-devel
This package provides header files of Python MPICH PETsc.

%if 0%{?with_python3}
%package -n     python%{python3_pkgversion}-%{pypi_name}-mpich
Summary:        Python3 bindings for MPICH PETSc
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}-mpich}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  hdf5-mpich-devel
BuildRequires:  scalapack-mpich-devel
BuildRequires:  ptscotch-mpich-devel
BuildRequires:  petsc-mpich-devel >= %{petscver}
BuildRequires:  python%{python3_pkgversion}-numpy, python%{python3_pkgversion}-Cython
Requires:       petsc-mpich%{?_isa} >= %{petscver}
Requires:       hdf5-mpich%{?_isa}
Requires:       scalapack-openmpi%{?_isa}
Requires:       ptscotch-mpich%{?_isa}
Requires:       mpich%{?_isa}
Requires:       MUMPS-mpich%{?_isa}

%description -n python%{python3_pkgversion}-%{pypi_name}-mpich
This package provides Python3 bindings for MPICH PETSc,
the Portable, Extensible Toolkit for Scientific Computation.

%if 0%{?with_python3_other}
%package -n python%{python3_other_pkgversion}-%{pypi_name}-mpich
Summary:        Python%{python3_other_pkgversion} bindings for MPICH PETSc
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{pypi_name}-mpich}

BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  hdf5-mpich-devel
BuildRequires:  scalapack-mpich-devel
BuildRequires:  ptscotch-mpich-devel
BuildRequires:  petsc-mpich-devel >= %{petscver}
BuildRequires:  python%{python3_other_pkgversion}-numpy, python%{python3_other_pkgversion}-Cython
Requires:       petsc-mpich%{?_isa} >= %{petscver}
Requires:       hdf5-mpich%{?_isa}
Requires:       scalapack-mpich%{?_isa}
Requires:       ptscotch-mpich%{?_isa}
Requires:       mpich%{?_isa}
Requires:       MUMPS-mpich%{?_isa}

%description -n python%{python3_other_pkgversion}-%{pypi_name}-mpich
Python%{python3_other_pkgversion} bindings for MPICH PETSc.
%endif
%endif
%endif

%prep
%setup -qc

rm -rf %{pypi_name}-%{version}/%{pypi_name}.egg-info

cp -a %{pypi_name}-%{version} %{pypi_name}-mpich
mv %{pypi_name}-%{version} %{pypi_name}-openmpi

%if 0%{?with_openmpi}
pushd %{pypi_name}-openmpi
%patch0 -p0
%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
sed -e 's|@@arch@@|%{_arch}|g' -i conf/baseconf.py
sed -e 's|@@bits@@|%{?__isa_bits}|g' -i conf/baseconf.py
sed -e 's|-@@petscver@@||g' -i conf/baseconf.py
%else
sed -e 's|@@arch@@|%{_arch}|g' -i conf/baseconf.py
sed -e 's|@@bits@@||g' -i conf/baseconf.py
sed -e 's|-@@petscver@@||g' -i conf/baseconf.py
%endif
popd
%endif

%if 0%{?with_mpich}
pushd %{pypi_name}-mpich
%patch1 -p0
%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
sed -e 's|@@arch@@|%{_arch}|g' -i conf/baseconf.py
sed -e 's|@@bits@@|%{?__isa_bits}|g' -i conf/baseconf.py
sed -e 's|-@@petscver@@||g' -i conf/baseconf.py
%else
sed -e 's|@@arch@@|%{_arch}|g' -i conf/baseconf.py
sed -e 's|@@bits@@||g' -i conf/baseconf.py
sed -e 's|-@@petscver@@||g' -i conf/baseconf.py
%endif
popd
%endif

%build

# openmpi petsc4py
%if 0%{?with_openmpi}
pushd %{pypi_name}-openmpi

%if 0%{?el7}
%{?dts:source /opt/rh/devtoolset-8/enable}
%endif

%{_openmpi_load}
export PETSC_DIR=%{_prefix}
%if 0%{?with_python2}
%py2_build
%endif
%if 0%{?with_python3}
%py3_build

%if 0%{?with_python3_other}
%py3_other_build
%endif
%endif
popd
%{_openmpi_unload}
%endif

# mpich petsc4py
%if 0%{?with_mpich}
pushd %{pypi_name}-mpich

%if 0%{?el7}
%{?dts:source /opt/rh/devtoolset-8/enable}
%endif

%{_mpich_load}
export PETSC_DIR=%{_prefix}
%if 0%{?with_python2}
%py2_build
%endif
%if 0%{?with_python3}
%py3_build

%if 0%{?with_python3_other}
%py3_other_build
%endif
%endif
popd
%{_mpich_unload}
%endif

%install
# openmpi petsc4py
%if 0%{?with_openmpi}
%{_openmpi_load}
pushd %{pypi_name}-openmpi

%if 0%{?with_python2}
%py2_install

# Install petsc4py files into MPI directories
%if 0%{?rhel}
MPI_PYTHON2_SITEARCH=%{python2_sitearch}/openmpi
%endif

mkdir -p %{buildroot}$MPI_PYTHON2_SITEARCH
cp -a %{buildroot}%{python2_sitearch}/%{pypi_name} %{buildroot}$MPI_PYTHON2_SITEARCH/
rm -rf %{buildroot}%{python2_sitearch}/%{pypi_name}
cp -a %{buildroot}%{python2_sitearch}/%{pypi_name}-%{version}-py%{python2_version}.egg-info %{buildroot}$MPI_PYTHON2_SITEARCH/
rm -rf %{buildroot}%{python2_sitearch}/%{pypi_name}-%{version}-py%{python2_version}.egg-info
%endif

%if 0%{?with_python3}
%py3_install

# Install petsc4py files into MPI directories 
%if 0%{?rhel}
MPI_PYTHON3_SITEARCH=%{python3_sitearch}/openmpi
%endif

mkdir -p %{buildroot}$MPI_PYTHON3_SITEARCH
cp -a %{buildroot}%{python3_sitearch}/%{pypi_name} %{buildroot}$MPI_PYTHON3_SITEARCH/
rm -rf %{buildroot}%{python3_sitearch}/%{pypi_name}
cp -a %{buildroot}%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info %{buildroot}$MPI_PYTHON3_SITEARCH/
rm -rf %{buildroot}%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%if 0%{?with_python3_other}
%py3_other_install

# Install petsc4py files into MPI directories 
mkdir -p %{buildroot}%{python3_other_sitearch}/openmpi
cp -a %{buildroot}%{python3_other_sitearch}/%{pypi_name} %{buildroot}%{python3_other_sitearch}/openmpi/
rm -rf %{buildroot}%{python3_other_sitearch}/%{pypi_name}
cp -a %{buildroot}%{python3_other_sitearch}/%{pypi_name}-%{version}-py%{__python3_other}.egg-info %{buildroot}%{python3_other_sitearch}/openmpi/
rm -rf %{buildroot}%{python3_other_sitearch}/%{pypi_name}-%{version}-py%{__python3_other}.egg-info
%endif
%endif

# Install include files
mkdir -p %{buildroot}$MPI_INCLUDE/%{pypi_name}
cp -a src/include/* %{buildroot}$MPI_INCLUDE/%{pypi_name}/

%{_openmpi_unload}
popd
%endif

# mpich petsc4py
%if 0%{?with_mpich}
pushd %{pypi_name}-mpich
%{_mpich_load}

%if 0%{?with_python2}
%py2_install

# Install petsc4py files into MPI directories
%if 0%{?rhel}
MPI_PYTHON2_SITEARCH=%{python2_sitearch}/mpich
%endif

mkdir -p %{buildroot}$MPI_PYTHON2_SITEARCH
cp -a %{buildroot}%{python2_sitearch}/%{pypi_name} %{buildroot}$MPI_PYTHON2_SITEARCH/
rm -rf %{buildroot}%{python2_sitearch}/%{pypi_name}
cp -a %{buildroot}%{python2_sitearch}/%{pypi_name}-%{version}-py%{python2_version}.egg-info %{buildroot}$MPI_PYTHON2_SITEARCH/
rm -rf %{buildroot}%{python2_sitearch}/%{pypi_name}-%{version}-py%{python2_version}.egg-info
%endif

%if 0%{?with_python3}
%py3_install

# Install petsc4py files into MPI directories
%if 0%{?rhel}
MPI_PYTHON3_SITEARCH=%{python3_sitearch}/mpich
%endif

mkdir -p %{buildroot}$MPI_PYTHON3_SITEARCH
cp -a %{buildroot}%{python3_sitearch}/%{pypi_name} %{buildroot}$MPI_PYTHON3_SITEARCH/
rm -rf %{buildroot}%{python3_sitearch}/%{pypi_name}
cp -a %{buildroot}%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info %{buildroot}$MPI_PYTHON3_SITEARCH/
rm -rf %{buildroot}%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%if 0%{?with_python3_other}
%py3_other_install

# Install petsc4py files into MPI directories 
mkdir -p %{buildroot}%{python3_other_sitearch}/mpich
cp -a %{buildroot}%{python3_other_sitearch}/%{pypi_name} %{buildroot}%{python3_other_sitearch}/mpich/
rm -rf %{buildroot}%{python3_other_sitearch}/%{pypi_name}
cp -a %{buildroot}%{python3_other_sitearch}/%{pypi_name}-%{version}-py%{__python3_other}.egg-info %{buildroot}%{python3_other_sitearch}/mpich/
rm -rf %{buildroot}%{python3_other_sitearch}/%{pypi_name}-%{version}-py%{__python3_other}.egg-info
%endif
%endif

# Install include files
mkdir -p %{buildroot}$MPI_INCLUDE/%{pypi_name}
cp -a src/include/* %{buildroot}$MPI_INCLUDE/%{pypi_name}/

%{_mpich_unload}
popd
%endif

%check
# openmpi petsc4py
%if 0%{?with_openmpi}
pushd %{pypi_name}-openmpi
%{_openmpi_load}

%if 0%{?with_python2}
%if 0%{?rhel}
MPI_PYTHON2_SITEARCH=%{python2_sitearch}/openmpi
%endif

export PYTHONPATH=$RPM_BUILD_ROOT$MPI_PYTHON2_SITEARCH
%{__python2} setup.py test
%endif

%if 0%{?with_python3}
%if 0%{?rhel}
MPI_PYTHON3_SITEARCH=%{python3_sitearch}/openmpi
%endif
%if 0%{?python3_version_nodots} > 37
%ifnarch %{power64}
%{__python3} setup.py test
%endif
%endif
%if 0%{?python3_version_nodots} < 38
%{__python3} setup.py test
%endif

%if 0%{?with_python3_other}
export PYTHONPATH=$RPM_BUILD_ROOT%{python3_other_sitearch}/openmpi
%{__python3_other} setup.py test
%endif
%endif
%{_openmpi_unload}
popd
%endif

# mpich petsc4py
%if 0%{?with_mpich}
pushd %{pypi_name}-mpich
%{_mpich_load}

%if 0%{?with_python2}
%if 0%{?rhel}
MPI_PYTHON2_SITEARCH=%{python2_sitearch}/mpich
%endif

export PYTHONPATH=$RPM_BUILD_ROOT$MPI_PYTHON2_SITEARCH
%{__python2} setup.py test
%endif

%if 0%{?with_python3}
%if 0%{?rhel}
MPI_PYTHON3_SITEARCH=%{python3_sitearch}/mpich
%endif
export PYTHONPATH=$RPM_BUILD_ROOT$MPI_PYTHON3_SITEARCH
%if 0%{?python3_version_nodots} > 37
%ifnarch %{power64}
%{__python3} setup.py test
%endif
%endif
%if 0%{?python3_version_nodots} < 38
%{__python3} setup.py test
%endif

%if 0%{?with_python3_other}
export PYTHONPATH=$RPM_BUILD_ROOT%{python3_other_sitearch}/mpich
%{__python3_other} setup.py test
%endif
%endif
%{_mpich_unload}
popd
%endif

%if 0%{?with_openmpi}
%if 0%{?with_python2}
%files -n python2-%{pypi_name}-openmpi
%doc %{pypi_name}-openmpi/CHANGES.* %{pypi_name}-openmpi/README.*
%license %{pypi_name}-openmpi/LICENSE.rst
%{python2_sitearch}/openmpi/%{pypi_name}/
%{python2_sitearch}/openmpi/%{pypi_name}-%{version}-py%{python2_version}.egg-info
%endif

%files -n %{pypi_name}-openmpi-devel
%{_includedir}/openmpi-%{_arch}/%{pypi_name}/

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{pypi_name}-openmpi
%doc %{pypi_name}-openmpi/CHANGES.* %{pypi_name}-openmpi/README.*
%license %{pypi_name}-openmpi/LICENSE.rst
%{python3_sitearch}/openmpi/%{pypi_name}/
%{python3_sitearch}/openmpi/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{pypi_name}-openmpi
%doc %{pypi_name}-openmpi/CHANGES.* %{pypi_name}-openmpi/README.*
%license %{pypi_name}-openmpi/LICENSE.rst
%{python3_other_sitearch}/openmpi/%{pypi_name}/
%{python3_other_sitearch}/openmpi/%{pypi_name}-%{version}-py%{__python3_other}.egg-info
%endif
%endif
%endif

%if 0%{?with_mpich}
%if 0%{?with_python2}
%files -n python2-%{pypi_name}-mpich
%doc %{pypi_name}-mpich/CHANGES.* %{pypi_name}-mpich/README.*
%license %{pypi_name}-mpich/LICENSE.rst
%{python2_sitearch}/mpich/%{pypi_name}/
%{python2_sitearch}/mpich/%{pypi_name}-%{version}-py%{python2_version}.egg-info
%endif

%files -n %{pypi_name}-mpich-devel
%{_includedir}/mpich-%{_arch}/%{pypi_name}/

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{pypi_name}-mpich
%doc %{pypi_name}-mpich/CHANGES.* %{pypi_name}-mpich/README.*
%license %{pypi_name}-mpich/LICENSE.rst
%{python3_sitearch}/mpich/%{pypi_name}/
%{python3_sitearch}/mpich/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{pypi_name}-mpich
%doc %{pypi_name}-mpich/CHANGES.* %{pypi_name}-openmpi/README.*
%license %{pypi_name}-mpich/LICENSE.rst
%{python3_other_sitearch}/mpich/%{pypi_name}/
%{python3_other_sitearch}/mpich/%{pypi_name}-%{version}-py%{__python3_other}.egg-info
%endif
%endif
%endif

%changelog
* Sat May 30 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.13.0-2
- Rebuilt for Python 3.9

* Sat Apr 11 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.13.0-1
- Release 3.13.0

* Sun Mar 08 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.12.0-6
- Do not perform any tests with Python3.8 (upstream bug #136)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.12.0-4
- New rebuild

* Sat Dec 28 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.12.0-3
- New rebuild for fedora-infrastructure issue #8477

* Wed Dec 25 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.12.0-2
- Adjust with EPEL-7 branch modifications

* Sat Oct 19 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.12.0-1
- Release 3.12.0

* Thu Oct 03 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.0-12
- Rebuilt again on EPEL7

* Thu Oct 03 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.0-11
- New rebuild for petsc-3.11.3 on EPEL7

* Thu Oct 03 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.0-10
- New rebuild for petsc-3.11.3 on EPEL7
- Use devtools-8 on EPEL7

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.11.0-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Aug 21 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.0-8
- New rebuild for petsc-3.11.3

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.11.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.0-5
- Rebuild for petsc-3.11.3

* Fri May 24 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.0-4
- Use conditional macro for the patch #2

* Fri May 24 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.0-3
- Patched for Python-3.8

* Thu May 23 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.0-2
- Rebuild for OpenMPI-4

* Mon Apr 15 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.11.0-1
- Release 3.11.0

* Mon Mar 18 2019 Orion Poplawski <orion@nwra.com> - 3.10.1-2
- Rebuild for hdf5 1.10.5

* Tue Feb 05 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.10.1-1
- Update to 3.10.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 13 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.10.0-1
- Update to 3.10.0

* Tue Sep 04 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.9.1-4
- Deprecate Python2 on fedora 30+
- Prepare SPEC file for parallel python3X packaging on epel7
- Remove ExcludeArch for fedora < 29

* Fri Aug 03 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.9.1-3
- Fix RHEL BR packages

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 3.9.1-2
- Rebuild with fixed binutils

* Sun Jul 29 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.9.1-1
- Update to 3.9.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.9.0-3
- Rebuilt for Python 3.7

* Wed Jun 20 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.9.0-2
- Fix 'sed' patches

* Tue Apr 24 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.9.0-1
- Update to 3.9.0

* Tue Feb 06 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.8.1.6
- Fix 'sed' patches

* Tue Feb 06 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.8.1.5
- Rebuild again

* Sun Jan 28 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.8.1.4
- Rebuild for petsc-3.8.3

* Tue Dec 05 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.8.1-3
- Fix typo

* Sun Dec 03 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.8.1-2
- Set arch suffix of MPI include directories

* Wed Nov 22 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.8.1-1
- Update to 3.8.1

* Tue Oct 24 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.8.0-2
- Move header files under /usr/include

* Sun Oct 22 2017 Antonio Trande <sagitter@fedoraproject.org> - 3.8.0-1
- Initial package
