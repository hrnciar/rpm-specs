%bcond_with mpich
%bcond_with mpi

%bcond_without bundled_sundials

%if 0%{?rhel}
%global dts devtoolset-8-
%endif

Name:           bionetgen
Version:        2.5.1
Release:        4%{?dist}
Summary:        Software for rule-based modeling of biochemical systems
License:        GPLv3
URL:            https://github.com/RuleWorld/bionetgen
Source0:        https://github.com/RuleWorld/bionetgen/archive/BioNetGen-%{version}/bionetgen-BioNetGen-%{version}.tar.gz

# patch based on example in
# http://sundials.2283335.n4.nabble.com/Usage-notes-lead-to-the-example-that-uses-the-non-existent-header-cvode-cvode-dense-h-td4654260.html
Patch0:         %{name}-network-solver.patch

BuildRequires:  muParser-devel
%if 0%{without bundled_sundials}
BuildRequires:  sundials-devel
%endif
BuildRequires:  autoconf automake
BuildRequires:  libtool
BuildRequires:  %{?dts}gcc-c++, %{?dts}gcc, %{?dts}gcc-gfortran
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Struct)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Win32)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       bionetgen-perl = %{version}-%{release}

# BioNetGen does not namespace its perl modules
%global __provides_exclude perl\\(.*BNG.*|Cache|CartesianProduct|Compartment.*|Component.*|Console|EnergyPattern|Expression|Function|HNauty|Map|ModelWrapper|Molecule*|Observable|Param*|PatternGraph|Population*|RateLaw|RefineRule|Rxn*|SBMLMultiAux|Species*|Visualization*|XML::*|XMLReader\\)
%global __requires_exclude perl\\(.*BNG.*|Cache|CartesianProduct|Compartment.*|Component.*|Console|EnergyPattern|Expression|Function|HNauty|Map|ModelWrapper|Molecule*|Observable|Param*|PatternGraph|Population*|RateLaw|RefineRule|Rxn*|SBMLMultiAux|Species*|Visualization*|XML::*|XMLReader\\)

%description
BioNetGen is software for the specification and simulation of
rule-based models of biochemical systems, including signal
transduction, metabolic, and genetic regulatory networks. The
BioNetGen language has recently been extended to include explicit
representation of compartments. A review of methods for rule-based
modeling is available in Science Signaling (Sci. STKE, 18 July 2006,
Issue 344, p. re6).

BioNetGen is presently a mixture of Perl and C++. Network generation
is currently implemented in Perl, the network simulator is C++, and a
new language parser is being developed with ANTLR.

#########
%if 0%{with mpi}
%package openmpi
Summary:    Software for rule-based modeling of biochemical systems (OpenMPI)
BuildRequires:  muParser-devel
%if 0%{without bundled_sundials}
BuildRequires:  sundials-openmpi-devel >= 3.2.1
%endif
BuildRequires:  openmpi-devel
Requires:       bionetgen-perl = %{version}-%{release}

%description openmpi
BioNetGen is software for the specification and simulation of
rule-based models of biochemical systems, including signal
transduction, metabolic, and genetic regulatory networks. The
BioNetGen language has recently been extended to include explicit
representation of compartments. A review of methods for rule-based
modeling is available in Science Signaling (Sci. STKE, 18 July 2006,
Issue 344, p. re6).

BioNetGen is presently a mixture of Perl and C++. Network generation
is currently implemented in Perl, the network simulator is C++, and a
new language parser is being developed with ANTLR.

%package openmpi-devel
Summary:    Software for rule-based modeling of biochemical systems (OpenMPI)

%description openmpi-devel
Software for rule-based modeling of biochemical systems (developer files).
%endif
######

#########
%if 0%{with mpich}
%package mpich
Summary: Software for rule-based modeling of biochemical systems (MPICH)
BuildRequires:  muParser-devel
%if 0%{without bundled_sundials}
BuildRequires:  sundials-mpich-devel >= 3.2.1
%endif
BuildRequires:  mpich-devel
Requires:       bionetgen-perl = %{version}-%{release}

%description mpich
BioNetGen is software for the specification and simulation of
rule-based models of biochemical systems, including signal
transduction, metabolic, and genetic regulatory networks. The
BioNetGen language has recently been extended to include explicit
representation of compartments. A review of methods for rule-based
modeling is available in Science Signaling (Sci. STKE, 18 July 2006,
Issue 344, p. re6).

BioNetGen is presently a mixture of Perl and C++. Network generation
is currently implemented in Perl, the network simulator is C++, and a
new language parser is being developed with ANTLR.

%package mpich-devel
Summary: Software for rule-based modeling of biochemical systems (MPICH)

%description mpich-devel
Software for rule-based modeling of biochemical systems (developer files).
%endif
######

%package perl
Summary:        Perl scripts and Models used by bionetgen
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Math::Trig)
Requires:       bionetgen = %{version}-%{release}
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Math::Trig)
Provides:       bundled(XML-TreePP) = 0.41
%description perl
%{summary}.

%prep
%setup -qc

pushd bionetgen-BioNetGen-%{version}

%if 0%{with bundled_sundials}
rm -f bng2/libsource/{gsl-1.9.tar.gz,Mathutils.tar.gz,muparser_v2_2_4.tar.gz,muparser_v2_2_4.zip}
tar -xvf bng2/libsource/cvode-2.6.0.tar.gz -C bng2/Network3
%else
# This patch must be used for Sundials 3.x
%if 0%{?fedora}
%autopatch -p1
%endif
rm -f bng2/libsource/*
%endif
popd

%if 0%{with mpi}
cp -a bionetgen-BioNetGen-%{version} openmpi
%endif
%if 0%{with mpich}
cp -a bionetgen-BioNetGen-%{version} mpich
%endif

%build

pushd bionetgen-BioNetGen-%{version}/bng2/Network3

sed -i 's/AC_PROG_LIBTOOL/AM_PROG_AR\nLT_INIT/' configure.ac
%if %{with bundled_sundials}
sed -i 's/AC_PROG_LIBTOOL/AM_PROG_AR\nLT_INIT/' cvode-2.6.0/configure.ac
sed -i 's/muparser_.*//' configure.ac Makefile.am
sed -i -r 's!(run_network_LDADD =).*!\1 libmathutils.la ../cvode-2.6.0/src/nvec_ser/libsundials_nvecserial.la ../cvode-2.6.0/src/cvode/libsundials_cvode.la -lmuparser!' src/Makefile.am
%else
sed -i 's/cvode-.*//; s/muparser_.*//' configure.ac Makefile.am
sed -i -r 's/(run_network_LDADD =).*/\1 libmathutils.la -lmuparser -lsundials_nvecserial -lsundials_cvode/' src/Makefile.am
%endif

autoreconf -iv --no-recursive

warnings="-Wno-unused-variable -Wno-unused-function -Wno-unused-but-set-variable -Wno-maybe-uninitialized"

%if 0%{?rhel}
%{?dts:source /opt/rh/devtoolset-8/enable}
%configure CC=/opt/rh/devtoolset-8/root/usr/bin/gcc CXX=/opt/rh/devtoolset-8/root/usr/bin/g++ F77=/opt/rh/devtoolset-8/root/usr/bin/gfortran
%else
%configure CC=gcc CXX=g++ F77=gfortran
%endif

# Build cvode
%if %{with bundled_sundials}
SETOPT_FLAGS=$(echo "%{optflags}" | sed -e 's/-Werror=format-security/-Wno-error=format-security/g')
%if 0%{?rhel}
%make_build -C cvode-2.6.0 V=1 CC=/opt/rh/devtoolset-8/root/usr/bin/gcc CXX=/opt/rh/devtoolset-8/root/usr/bin/g++ F77=/opt/rh/devtoolset-8/root/usr/bin/gfortran \
 CXXFLAGS="$SETOPT_FLAGS $warnings" CFLAGS="$SETOPT_FLAGS $warnings"
%else
%make_build -C cvode-2.6.0 V=1 CC=gcc CXX=g++ F77=gfortran CXXFLAGS="$SETOPT_FLAGS $warnings" CFLAGS="$SETOPT_FLAGS $warnings"
%endif
%endif

# Build bionetgen
%if 0%{?rhel}
%make_build -C src V=1 CC=/opt/rh/devtoolset-8/root/usr/bin/gcc CXX=/opt/rh/devtoolset-8/root/usr/bin/g++ F77=/opt/rh/devtoolset-8/root/usr/bin/gfortran CXXFLAGS="%{optflags} $warnings"
%else
%make_build -C src V=1 CC=gcc CXX=g++ F77=gfortran CXXFLAGS="%{optflags} $warnings"
%endif
popd

%if 0%{with mpi}
pushd openmpi/bng2/Network3

%{_openmpi_load}
sed -i 's/AC_PROG_LIBTOOL/AM_PROG_AR\nLT_INIT/' configure.ac
%if %{with bundled_sundials}
sed -i 's/AC_PROG_LIBTOOL/AM_PROG_AR\nLT_INIT/' cvode-2.6.0/configure.ac
sed -i 's/muparser_.*//' configure.ac Makefile.am
sed -i -r 's!(run_network_LDADD =).*!\1 libmathutils.la ../cvode-2.6.0/src/nvec_ser/libsundials_nvecserial.la ../cvode-2.6.0/src/cvode/libsundials_cvode.la -lmuparser!' src/Makefile.am
%else
sed -i 's/cvode-.*//; s/muparser_.*//' configure.ac Makefile.am
sed -i -r 's/(run_network_LDADD =).*/\1 libmathutils.la -lmuparser -lsundials_nvecserial -lsundials_cvode/' src/Makefile.am
%endif

autoreconf -iv --no-recursive

warnings="-Wno-unused-variable -Wno-unused-function -Wno-unused-but-set-variable -Wno-maybe-uninitialized"

./configure --prefix=%{_libdir}/openmpi CC=mpicc CXX=mpic++ F77=mpifort
%if %{with bundled_sundials}
SETOPT_FLAGS=$(echo "%{optflags}" | sed -e 's/-Werror=format-security/-Wno-error=format-security/g')
%make_build -C cvode-2.6.0 V=1 CC=mpicc CXX=mpic++ F77=mpifort CXXFLAGS="$SETOPT_FLAGS $warnings" CFLAGS="$SETOPT_FLAGS $warnings"
%endif
%make_build -C src V=1 CC=mpicc CXX=mpic++ F77=mpifort CXXFLAGS="%{optflags} $warnings"
%{_openmpi_unload}

popd
%endif

%if 0%{with mpich}
pushd mpich/bng2/Network3

%{_mpich_load}
sed -i 's/AC_PROG_LIBTOOL/AM_PROG_AR\nLT_INIT/' configure.ac
%if %{with bundled_sundials}
sed -i 's/AC_PROG_LIBTOOL/AM_PROG_AR\nLT_INIT/' cvode-2.6.0/configure.ac
sed -i 's/muparser_.*//' configure.ac Makefile.am
sed -i -r 's!(run_network_LDADD =).*!\1 libmathutils.la ../cvode-2.6.0/src/nvec_ser/libsundials_nvecserial.la ../cvode-2.6.0/src/cvode/libsundials_cvode.la -lmuparser!' src/Makefile.am
%else
sed -i 's/cvode-.*//; s/muparser_.*//' configure.ac Makefile.am
sed -i -r 's/(run_network_LDADD =).*/\1 libmathutils.la -lmuparser -lsundials_nvecserial -lsundials_cvode/' src/Makefile.am
%endif

autoreconf -iv --no-recursive

warnings="-Wno-unused-variable -Wno-unused-function -Wno-unused-but-set-variable -Wno-maybe-uninitialized"

./configure --prefix=%{_libdir}/mpich CC=mpicc CXX=mpic++ F77=mpifort
%if %{with bundled_sundials}
SETOPT_FLAGS=$(echo "%{optflags}" | sed -e 's/-Werror=format-security/-Wno-error=format-security/g')
%make_build -C cvode-2.6.0 V=1 CC=mpicc CXX=mpic++ F77=mpifort CXXFLAGS="$SETOPT_FLAGS $warnings" CFLAGS="$SETOPT_FLAGS $warnings"
%endif
%make_build -C src V=1 CC=mpicc CXX=mpic++ F77=mpifort CXXFLAGS="%{optflags} $warnings"
%{_mpich_unload}

popd
%endif


%install
%make_install -C bionetgen-BioNetGen-%{version}/bng2/Network3/src
mkdir -vp %{buildroot}%{perl_vendorlib}/BioNetGen
cp -r bionetgen-BioNetGen-%{version}/bng2/Perl2 %{buildroot}%{perl_vendorlib}/BioNetGen/
cp -r bionetgen-BioNetGen-%{version}/bng2/BNG2.pl %{buildroot}%{perl_vendorlib}/BioNetGen/
cp -a bionetgen-BioNetGen-%{version}/bng2/Models2 %{buildroot}%{perl_vendorlib}/BioNetGen/
rm -f %{buildroot}%{perl_vendorlib}/BioNetGen/Models2/bin/run_network_%{_arch}-linux
rm -f %{buildroot}%{perl_vendorlib}/BioNetGen/Models2/run_network

%if 0%{with mpi}
%{_openmpi_load}
%make_install -C openmpi/bng2/Network3/src
%{_openmpi_unload}
%endif

%if 0%{with mpich}
%{_mpich_load}
%make_install -C mpich/bng2/Network3/src
%{_mpich_unload}
%endif

%check
pushd bionetgen-BioNetGen-%{version}/bng2/Models2
%ifarch %{arm}
install -pm 755 ../Network3/src/run_network -D ./bin/run_network_armv7l-linux
install -pm 755 ../Network3/src/run_network -D ../bin/run_network_armv7l-linux
%else
install -pm 755 ../Network3/src/run_network -D ./bin/run_network_%{_target_cpu}-linux
install -pm 755 ../Network3/src/run_network -D ../bin/run_network_%{_target_cpu}-linux
%endif
echo "Running some tests ..."
../BNG2.pl CaOscillate_Func.bngl CaOscillate_Sat.bngl catalysis.bngl egfr_net.bngl egfr_net_red.bngl egfr_path.bngl energy_example1.bngl fceri_ji.bngl test_continue.bngl
echo "Tests finished."

%files
%license bionetgen-BioNetGen-%{version}/LICENSE
%doc bionetgen-BioNetGen-%{version}/README.md bionetgen-BioNetGen-%{version}/bng2/CREDITS.txt
%doc bionetgen-BioNetGen-%{version}/bng2/CHANGES.txt bionetgen-BioNetGen-%{version}/bng2/VERSION
%{_bindir}/run_network

%files perl
%{perl_vendorlib}/BioNetGen/

%if 0%{with mpi}
%files openmpi
%license bionetgen-BioNetGen-%{version}/LICENSE
%doc bionetgen-BioNetGen-%{version}/README.md bionetgen-BioNetGen-%{version}/bng2/CREDITS.txt
%doc bionetgen-BioNetGen-%{version}/bng2/CHANGES.txt bionetgen-BioNetGen-%{version}/bng2/VERSION
%{_libdir}/openmpi/bin/run_network
%endif

%if 0%{with mpich}
%files mpich
%license bionetgen-BioNetGen-%{version}/LICENSE
%doc bionetgen-BioNetGen-%{version}/README.md bionetgen-BioNetGen-%{version}/bng2/CREDITS.txt
%doc bionetgen-BioNetGen-%{version}/bng2/CHANGES.txt bionetgen-BioNetGen-%{version}/bng2/VERSION
%{_libdir}/mpich/bin/run_network
%endif

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.5.1-2
- Perl 5.32 rebuild

* Fri Jun 05 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.5.1-1
- Release 2.5.1

* Fri Mar 20 2020 Petr Pisar <ppisar@redhat.com> - 2.5.0-7
- Specify dependencies for the tests

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.5.0-4
- Use devtoolset-8 on EPEL 7

* Mon Jul 01 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.5.0-3
- Rebuild for sundials

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.5.0-2
- Perl 5.30 rebuild

* Tue May 07 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.5.0-1
- Release 2.5.0

* Sat Apr 20 2019 Antonio Trande <sagitter@fedoraproject.org> - 2.4.0-5
- Ready for MPI (disabled)
- Bundle Sundials

* Wed Feb 13 2019 Orion Poplawski <orion@cora.nwra.com> - 2.4.0-4
- Rebuild for openmpi 3.1.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 09 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4.0-2
- Filtering of SBMLMultiAux module

* Thu Nov 08 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.4.0-1
- Release 2.4.0
- Drop obsolete patch
- Rebuild on epel7 (rhbz#1647989)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.0-8
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 08 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.3.0-6
- Rebuild for sundials-3.0.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.3.0-3
- Perl 5.26 rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sun May 07 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0

* Wed Mar 08 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.2.6-7
- Rebuild for sundials-2.7.0-10

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 04 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.6-5
- Rebuild for sundials-2.7.0-7

* Tue Oct 25 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.6-4
- Rebuild for sundials-2.7.0-6

* Sun Oct 16 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.6-3
- Rebuild for libsundials (#1384636)

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.6-2
- Perl 5.24 rebuild

* Thu Feb 11 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@bupkis> - 2.2.6-1
- Update to latest version
- Fix gcc6 compilation issue (#1306648)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.5-6
- Perl 5.22 rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.5-5
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 31 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.5-4
- Rebuilt for sundials 2.6.0.

* Thu Feb 26 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/GCC5 (#1195309)

* Sun Nov 30 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.5-2
- Drop dependency on compat f77, it is not needed.

* Fri Nov 21 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.2.5-1
- Initial packaging.
