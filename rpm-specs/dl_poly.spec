# Copyright (c) 2013, 2014, 2015 Dave Love, Liverpool University
# The licence for this file is as for the package itself.

# fixme: look at shipping example/benchmark data (~ 40MB total)

# Allow -march=native if you want to rebuild
%bcond_with native

%if 0%{?el6}
%ifarch ppc64
%bcond_with mpich
%else
%bcond_without mpich
%endif
%else
%bcond_without mpich
%endif

Name:		dl_poly
Version:	1.10
Release:	9%{?dist}
Summary:	General purpose classical molecular dynamics (MD) simulation
License:	BSD
URL:		https://gitlab.com/DL_POLY_Classic
# NB, the numbers in this URL change when it's updated, but the version doesn't
Source0:	https://gitlab.com/DL_POLY_Classic/dl_poly/-/archive/RELEASE-%(echo %version|tr . -)/%{name}-%{version}.tar.gz
Source1:	dl_poly-makefile
Source2:	dl_poly.desktop
# Change executable
Patch2:		dl_poly-javaexec.patch
BuildRequires:	gcc-gfortran java-devel openmpi-devel desktop-file-utils
%if %{with mpich}
BuildRequires:	mpich-devel
%endif
Requires:	%{name}-common = %{version}-%{release}

%global base_description \
DL_POLY Classic is a general purpose molecular dynamics simulation\
package developed at Daresbury Laboratory by W. Smith, T.R. Forester\
and I.T. Todorov.  It is based on the package DL_POLY_2, which was\
originally developed by the Computational Chemistry Group, (CCG) at\
Daresbury Laboratory under the auspices of the Engineering and\
Physical Sciences Research Council (EPSRC) for (CCP5), the EPSRC's\
Collaborative Computational Project for the Computer Simulation of\
Condensed Phases.\
\
DL_POLY Classic achieves parallelisation using the Replicated Data strategy\
which is suitable for homogeneous, distributed-memory, parallel\
computers.  The code is useful for simulations of up to 30,000 atoms\
with good parallel performance on up to 100 processors, though in some\
circumstances it can exceed or fail to reach these limits.\
\
Reference: I.T. Todorov, W. Smith, K. Trachenko & M.T. Dove,\
Journal of Materials Chemistry, (2006) 16, 1911-1918

%description
%{base_description}

%package common
Summary: General purpose classical molecular dynamics (MD) simulation - common files
BuildArch: noarch

%description common
Common files for %name.
This package contains, principally the "utility" source and data files.

%package doc
Summary: Documentation for %name and %{name}-gui
BuildArch: noarch

%description doc
Documentation for %{name} and %{name}-gui.

%package openmpi
Summary: General purpose classical molecular dynamics (MD) simulation - openmpi version
Requires: openmpi%{_isa}, %{name}-common = %{version}-%{release}

%description openmpi
%{base_description}

This is a parallel version using openmpi.

%if %{with mpich}
%package mpich
Summary: General purpose classical molecular dynamics (MD) simulation - mpich version
Requires: mpich%{_isa}, %{name}-common = %{version}-%{release}

%description mpich
%{base_description}

This is a parallel version using mpich.
%endif

%package gui
Summary: GUI for %name
Requires: java, jpackage-utils
BuildArch: noarch

%description gui
This package provides the Java-based graphical user interface for %name.

%prep
# The tarball directory is like
# dl_poly-RELEASE-1-10-565a1de4234430452c8248426ca2fa15d532334d
%setup -q -n %(tar ft %SOURCE0|head -n1|sed s,/,,)
rm java/GUI.jar
cp %{SOURCE1} source/Makefile

%patch2 -p1

%build
# Serial version no longer builds.  Reported to Bill Smith, but no fix
# forthcoming.
%if %{with native}
%global native NATIVE=-march=native
%else
%global native NATIVE=
%endif
%if 0%{?fedora} >= 32 || 0%{?rhel} >= 9
%global aam -fallow-argument-mismatch
%endif
export FFLAGS="%build_fflags -O3 -ffast-math $(NATIVE) -Wno-unused-variable %{?aam}"
export LDFLAGS="%build_ldflags"
# Parallel make fails.  Extra opt flags are from the original.
%global dobuild \
mkdir $MPI_COMPILER;\
%make_build -j1 build PAR=1 %native; \
mv ../execute/DLPOLY.X $MPI_COMPILER/%{name}$MPI_SUFFIX

cd source

%{_openmpi_load}
%{dobuild}
%{_openmpi_unload}
rm  basic_comms.o merge_tools.o pass_tools.o
make clean
%if %{with mpich}
%{_mpich_load}
%{dobuild}
%{_mpich_unload}
%endif

cd ../java
sh build
cat <<+ >%{name}_gui
#!/bin/sh
exec java -jar %{_javadir}/DL_POLY_GUI.jar
+
cd ..
cat <<+ >README.running
Use the environment modules command
  module load <mpi>-%{_arch}
to put the %{name}_<mpi> parallel executable on your path,
where <mpi> may be openmpi or mpich.  In a batch job You may
need to source /etc/profile.d/modules.sh or /etc/profile.d/modules.csh
first.
+

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir} $RPM_BUILD_ROOT%_datadir/%name
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/openmpi/bin
install source/openmpi*/%{name}_* $RPM_BUILD_ROOT%{_libdir}/openmpi/bin
%if %{with mpich}
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/mpich/bin
install source/mpich*/%{name}_* $RPM_BUILD_ROOT%{_libdir}/mpich/bin
%endif
cp data/README README.data
chmod 644 utility/dl2xyz
cp -a utility $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 java/GUI.jar $RPM_BUILD_ROOT%{_javadir}/DL_POLY_GUI.jar
install -m 755 java/%{name}_gui $RPM_BUILD_ROOT%{_bindir}
chmod 644 LICENCE.pdf manual/JavaGUI.pdf
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE2}


%check
# Would depend on shipping at least some data files, per fixme above


%files common
%license LICENCE.pdf
%doc README.data README
%{_datadir}/%{name}

%files doc
%license LICENCE.pdf
%doc manual/USRMAN.pdf manual/JavaGUI.pdf

%files gui
%license LICENCE.pdf
%{_javadir}/DL_POLY_GUI.jar
%{_bindir}/%{name}_gui
%doc README
%{_datadir}/applications/*

%files openmpi
%{_libdir}/openmpi/bin/*

%if %{with mpich}
%files mpich
%{_libdir}/mpich/bin/*
%endif


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.10-8
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Dave Love <loveshack@fedoraproject.org> - 1.10-6
- Fix FTBFS with gfortran 10

* Mon Aug 19 2019 Dave love <loveshack@fedoraproject.org> - 1.10-5
- Update URLs

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 1.10-3
- Rebuild for openmpi 3.1.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 29 2018 Dave Love <loveshack@fedoraproject.org> - 1.10-1
- New version
- Drop serial version, which no longer builds
- Fix homepaage
- Drop java patch
- Improve optimization flags

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.20140324-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.20140324-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.20140324-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.20140324-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 05 2017 Kalev Lember <klember@redhat.com> - 1.9.20140324-18
- Rebuilt for libgfortran soname bump

* Fri Oct 21 2016 Orion Poplawski <orion@cora.nwra.com> - 1.9.20140324-17
- Rebuild for openmpi 2.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.20140324-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 15 2015 Orion Poplawski <orion@cora.nwra.com> - 1.9.20140324-15
- Rebuild for openmpi 1.10.0

* Sat Aug 15 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.9.20140324-14
- Rebuild for MPI provides

* Mon Jul 27 2015 Sandro Mani <manisandro@gmail.com> - 1.9.20140324-13
- Rebuild for RPM MPI Requires Provides Change

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.20140324-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 18 2015 Dave Love <d.love@liverpool.ac.uk> - 1.9.20140324-11
- Rebuild for mpich change

* Sun Feb 22 2015 Dave Love <d.love@liverpool.ac.uk> - 1.9.20140324-10
- Drop java minimum version (for ppc64 el6)

* Fri Feb 20 2015 Dave Love <d.love@liverpool.ac.uk> - 1.9.20140324-9
- Specify permissions for installed .jar

* Thu Feb 19 2015 Dave Love <d.love@liverpool.ac.uk> - 1.9.20140324-8
- Conditionalize out mpich on ppc64 el6

* Wed Feb 11 2015 Dave Love <d.love@liverpool.ac.uk> - 1.9.20140324-7
- Remove _isa on -common and java requires

* Tue Feb 10 2015 Dave Love <d.love@liverpool.ac.uk> - 1.9.20140324-6
- Add _isa suffix to requires
- Use %%global, not %%define

* Fri Feb  6 2015 Dave Love <d.love@liverpool.ac.uk> - 1.9.20140324-5
  From review:
- Remove bundled .jar
- Change buildroot to the preferred form
- Add desktop file
- Zap %%defattr
- Use %%optflags (sigh)

* Thu Dec 11 2014 Dave Love <d.love@liverpool.ac.uk> - 1.9.20140324-4
- Drop EPEL5 for now

* Fri Nov 21 2014 Dave Love <d.love@liverpool.ac.uk> - 1.9.20140324-3
- Adjust for mpich3 on EPEL6

* Sun Jul 27 2014 Dave Love <d.love@liverpool.ac.uk> - 1.9.20140324-2
- Add doc package
- Add jpackage-utils dependency for gui
- Remove Group tags

* Thu Jun  5 2014 Dave Love <d.love@liverpool.ac.uk> - 1.9.20140324-1
- Build serial and mpich packages as well as openmpi, for Fedora
- Make common and gui packages
- Use updated tarball (which has the same version number)

* Fri Oct 11 2013 Dave Love <d.love@liverpool.ac.uk> - 1.9-1
- Initial packaging
