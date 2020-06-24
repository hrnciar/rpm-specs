%global upstreamver 2-5-4

Name:           cxsc
Version:        %(tr - . <<< %{upstreamver})
Release:        12%{?dist}
Summary:        C++ library for Extended Scientific Computing

%global majver  %(cut -d. -f1 <<< %{version})

License:        LGPLv2+
URL:            http://www2.math.uni-wuppertal.de/wrswt/xsc/cxsc_new.html
Source0:        http://www2.math.uni-wuppertal.de/wrswt/xsc/%{name}/%{name}-%{upstreamver}.tar.gz
# Sent upstream 22 Jun 2016.  Fix an operator error.
Patch0:         %{name}-operator.patch
# Sent upstream 22 Jun 2016.  Fix build problem on ppc64.
Patch1:         %{name}-ppc64.patch
# Fix endianness detection
Patch2:         %{name}-endian.patch
# Fix a sequence point error
Patch3:         %{name}-seq.patch
# Fix a mistaken euro symbol which leads to LaTeX errors
Patch4:         %{name}-euro.patch

BuildRequires:  doxygen-latex
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  openblas-devel

%description
C-XSC is the C language variant of the XSC (eXtensions for Scientific
Computing) project.  It provides routines that guarantee accuracy and
reliability of results.  Problem-solving routines with automatic result
verification have been developed for many standard problems of numerical
analysis, such as linear or nonlinear systems of equations, differential
and integral equations, etc. as well as for a large number of
applications in engineering and the natural sciences.  Some of the
features of C-XSC are:
- Operator concept (user-defined operators)
- Overloading concept
- Module concept
- Dynamic arrays
- Controlled rounding
- Predefined arithmetic data types real, extended real, complex,
  interval, complex interval, and corresponding vector and matrix types
- Predefined arithmetic operators and elementary functions of the highest
  accuracy for the arithmetic data types
- Data type dotprecision for the exact representation of dot products
- Library of mathematical problem-solving routines with automatic result
  verification and high accuracy

%package devel
Summary:        Header files for developing applications that use %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and library links for developing applications that use %{name}.

%package doc
Summary:        API documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       bundled(jquery)

%description doc
API documentation for %{name}.

%prep
%autosetup -p0 -n %{name}-%{upstreamver}

# Don't set rpath
sed -i 's/\(RPATH[[:blank:]]*=\).*/\1/;' Makefile.in CToolbox/Makefile
sed -i '/LINKERPATH=-Wl,-R/d' install_cxsc

# Don't build with SSE2 support on platforms the script doesn't recognize
%ifnarch %{ix86} x86_64
sed -i 's/ -mfpmath=sse -msse2//' install_cxsc.in
%endif

# Link with the openblas and OpenMP libraries
sed -i 's/\$(RARI)/& -lopenblaso -lgomp/' src/Makefile
sed -i 's/(LIBS)/& -lopenblaso/' CToolbox/Makefile

# Install in the right place on 64-bit systems
if [ %{_libdir} != "%{_prefix}/lib" ]; then
  sed -e 's|\$(PREFIX)/lib$|$(PREFIX)/%{_lib}|' \
      -e 's|\$(PREFIX)/lib;|$(PREFIX)/%{_lib};|' \
      -i src/Makefile
fi

# Use an efficient representation for a_btyp on 64-bit systems
if [ "%{__isa_bits}" = "64" ]; then
  sed -ri 's/(#define SHORTABTYP) .*/\1 1/' src/rts/o_spec.h
  sed -i 's/#if DEC_ALPHA_C+GNU_X86_64+CXSC_PPC64/#if 1/' src/rts/p88rts.h
else
  sed -ri 's/(#define SHORTABTYP) .*/\1 0/' src/rts/o_spec.h
  sed -i 's/#if DEC_ALPHA_C+GNU_X86_64+CXSC_PPC64/#if 0/' src/rts/p88rts.h
fi

# Remove spurious executable bits
chmod a-x src/fi_lib/*.{cpp,hpp}

%build
# FIXME: tests fail without -fno-inline.  Why?
if [ "%{__isa_bits}" = "64" ]; then
  use64=-DIS_64_BIT
else
  use64=
fi
printf "yes\n\
gnu\n\
no\n\
yes\n\
%ifarch x86_64
%{optflags} -DCXSC_USE_BLAS -DCXSC_USE_LAPACK -DCXSC_USE_OPENMP -DCXSC_USE_FMA -DIS_64_BIT -fopenmp -Wl,--as-needed\n\
64\n\
asm\n\
%else
%ifarch %{ix86} ppc64 ppc64le
%{optflags} -DCXSC_USE_BLAS -DCXSC_USE_LAPACK -DCXSC_USE_OPENMP -DCXSC_USE_FMA $use64 -fopenmp -Wl,--as-needed\n\
asm\n\
%else
%{optflags} -DCXSC_USE_BLAS -DCXSC_USE_LAPACK -DCXSC_USE_OPENMP -DCXSC_USE_FMA $use64 -fopenmp -frounding-math -fno-inline -Wl,--as-needed\n\
hard\n\
safe\n\
%endif
%endif
%{buildroot}%{_prefix}\n\
dynamic\n\
no\n" | ./install_cxsc

# The individual targets can be built in parallel, but specifying more than one
# to the same make invocation leads to build failures.
make %{?_smp_mflags} cxsc
make %{?_smp_mflags} libcxsc.so
mkdir usr
ln -s ../src usr/lib
ln -s lib%{name}.so.%{version} src/lib%{name}.so.%{majver}
ln -s lib%{name}.so.%{majver} src/lib%{name}.so
export LD_LIBRARY_PATH=$PWD/usr/lib
make %{?_smp_mflags} toolbox_dyn CXSCDIR=$PWD/usr

# Make the documentation
cd src
doxygen src-doxyfile

%install
make install_dyn PREFIX=%{buildroot}%{_prefix}

# Fix permissions on the library
chmod 0755 %{buildroot}%{_libdir}/lib%{name}.so.%{version}

# There are a lot of header files, so hide them in a private directory
mkdir %{buildroot}%{_includedir}/%{name}
mv %{buildroot}%{_includedir}/*.{h,hpp,inl} %{buildroot}%{_includedir}/%{name}

# Don't package the example binaries
rm -fr %{buildroot}/%{_prefix}/examples

%ldconfig_scriptlets

%check
sed -i 's/ASM$/ASM LD_LIBRARY_PATH/' Makefile
sed -i 's/export RPATH/export LD_LIBRARY_PATH/' CToolbox/Makefile
if [ %{_libdir} != "%{_prefix}/lib" ]; then
  sed -i 's|/lib|/%{_lib}|' CToolbox/Makefile
fi
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
make toolboxtest_dyn

%files
%doc changelog README
%license docu/COPYING
%{_libdir}/lib%{name}.so.2*

%files devel
%doc examples
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so

%files doc
%doc docu/apidoc docu/images

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct  6 2018 Jerry James <loganjerry@gmail.com> - 2.5.4-9
- Build with openblas instead of atlas (bz1618943)
- Do not build both SSE2/non-SSE2 for 32-bit x86 any more; default is now SSE2
- Add -euro patch to fix documentation build failure

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 24 2016 Jerry James <loganjerry@gmail.com> - 2.5.4-2
- Fix endianness detection
- Make the ppc64le build use the same asm as ppc64

* Wed Jun 22 2016 Jerry James <loganjerry@gmail.com> - 2.5.4-1
- Initial RPM
