
%global multilib_arches %{ix86} x86_64 ppc ppc64 s390 s390x sparcv9 sparc64

# define include static lib (else undef)
#define static 1

%if 0%{?fedora} || 0%{?rhel} >= 7
%global gf2x 1
%endif

Summary: High-performance algorithms for vectors, matrices, and polynomials 
Name:    ntl 
Version: 11.4.3
Release: 2%{?dist}

License: LGPLv2+
URL:     http://shoup.net/ntl/ 

Source0: http://shoup.net/ntl/%{name}-%{version}.tar.gz
Source1: multilib_template.h
# Detect CPU at load time, optionally use PCLMUL, AVX, FMA, and AVX2 features.
# This patch was sent upstream, but upstream prefers that the entire library
# be built for a specific CPU, which we cannot do in Fedora.
Patch0:  %{name}-loadtime-cpu.patch

BuildRequires: gcc-c++
%if 0%{?gf2x}
BuildRequires: gf2x-devel
%endif
BuildRequires: gmp-devel
BuildRequires: libtool
BuildRequires: perl-interpreter

%description
NTL is a high-performance, portable C++ library providing data structures
and algorithms for arbitrary length integers; for vectors, matrices, and
polynomials over the integers and over finite fields; and for arbitrary
precision floating point arithmetic.

NTL provides high quality implementations of state-of-the-art algorithms for:
* arbitrary length integer arithmetic and arbitrary precision floating point
  arithmetic;
* polynomial arithmetic over the integers and finite fields including basic
  arithmetic, polynomial factorization, irreducibility testing, computation
  of minimal polynomials, traces, norms, and more;
* lattice basis reduction, including very robust and fast implementations of
  Schnorr-Euchner, block Korkin-Zolotarev reduction, and the new 
  Schnorr-Horner pruning heuristic for block Korkin-Zolotarev;
* basic linear algebra over the integers, finite fields, and arbitrary
  precision floating point numbers. 

%package devel 
Summary: Development files for %{name} 
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel 
%{summary}.

%package static 
Summary: Static libraries for %{name}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
#Requires: gmp-devel
%description static 
%{summary}.


%prep
%autosetup -p0


%build
pushd src
./configure \
  CXX="${CXX-g++}" \
  CXXFLAGS="%{optflags} -fPIC" \
  LDFLAGS="$RPM_LD_FLAGS" \
  DEF_PREFIX=%{_prefix} \
  DOCDIR=%{_docdir} \
  INCLUDEDIR=%{_includedir} \
  LIBDIR=%{_libdir} \
  LDLIBS="-lpthread -lm" \
  NATIVE=off \
  %{?gf2x:NTL_GF2X_LIB=on} \
  NTL_STD_CXX14=on \
%ifarch x86_64
  NTL_LOADTIME_CPU=on \
  TUNE=x86 \
%else
  TUNE=generic \
%endif
  SHARED=on
popd

# not smp-safe
make -C src V=1


%check
make -C src check


%install
make -C src install \
  PREFIX=%{buildroot}%{_prefix} \
  DOCDIR=%{buildroot}%{_docdir} \
  INCLUDEDIR=%{buildroot}%{_includedir} \
  LIBDIR=%{buildroot}%{_libdir} 

# Fix permissions
chmod 0755 %{buildroot}%{_libdir}/libntl.so.*

# Unpackaged files
rm -rfv %{buildroot}%{_docdir}/NTL
rm -fv  %{buildroot}%{_libdir}/libntl.la
%if ! 0%{?static}
rm -fv  %{buildroot}%{_libdir}/libntl.a
%endif

%ifarch %{multilib_arches}
# hack to allow parallel installation of multilib factory-devel
for header in NTL/config NTL/gmp_aux NTL/mach_desc  ; do
mv  %{buildroot}%{_includedir}/${header}.h \
    %{buildroot}%{_includedir}/${header}-%{__isa_bits}.h
install -p -m644 %{SOURCE1} %{buildroot}%{_includedir}/${header}.h
sed -i \
  -e "s|@@INCLUDE@@|${header}|" \
  -e "s|@@INCLUDE_MACRO@@|$(echo ${header} | tr '/.' '_')|" \
  %{buildroot}%{_includedir}/${header}.h
done
%endif


%files
%doc README
%license doc/copying.txt
%{_libdir}/libntl.so.43*

%files devel 
%doc doc/*
%{_includedir}/NTL/
%{_libdir}/libntl.so

%if 0%{?static}
%files static
%{_libdir}/libntl.a
%endif


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan  8 2020 Jerry James <loganjerry@gmail.com> - 11.4.3-1
- ntl-11.4.3
- Drop upstreamed -gf2x13 patch

* Tue Dec 10 2019 Jerry James <loganjerry@gmail.com> - 11.4.1-2
- Rebuild for gf2x 1.3.0

* Mon Oct 14 2019 Jerry James <loganjerry@gmail.com> - 11.4.1-1
- ntl-11.4.1

* Wed Sep 25 2019 Jerry James <loganjerry@gmail.com> - 11.4.0-1
- ntl-11.4.0

* Tue Sep 24 2019 Jerry James <loganjerry@gmail.com> - 11.3.4-1
- ntl-11.3.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Jerry James <loganjerry@gmail.com> - 11.3.2-1
- ntl-11.3.2

* Tue Oct 30 2018 Jerry James <loganjerry@gmail.com> - 11.3.1-1
- ntl-11.3.1

* Fri Oct  5 2018 Jerry James <loganjerry@gmail.com> - 11.3.0-1
- ntl-11.3.0

* Fri Aug 10 2018 Jerry James <loganjerry@gmail.com> - 11.2.1-1
- ntl-11.2.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul  3 2018 Jerry James <loganjerry@gmail.com> - 11.1.0-1
- ntl-11.1.0

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 11.0.0-1
- ntl-11.0.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 28 2017 Jerry James <loganjerry@gmail.com> - 10.5.0-1
- ntl-10.5.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr  5 2017 Jerry James <loganjerry@gmail.com> - 10.3.0-1
- ntl-10.3.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 20 2016 Jerry James <loganjerry@gmail.com> - 10.1.0-1
- ntl-10.1.0

* Mon Sep  5 2016 Jerry James <loganjerry@gmail.com> - 9.11.0-1
- ntl-9.11.0

* Mon Jul 25 2016 Jerry James <loganjerry@gmail.com> - 9.10.0-1
- ntl-9.10.0

* Thu Jun  2 2016 Jerry James <loganjerry@gmail.com> - 9.9.1-1
- ntl-9.9.1

* Fri Apr 29 2016 Jerry James <loganjerry@gmail.com> - 9.8.0-1
- ntl-9.8.0
- Add -loadtime-cpu patch
- Enable the check script on x86_64

* Sat Mar 19 2016 Jerry James <loganjerry@gmail.com> - 9.7.0-1
- ntl-9.7.0

* Sat Feb 20 2016 Jerry James <loganjerry@gmail.com> - 9.6.4-1
- ntl-9.6.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 9.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec  4 2015 Jerry James <loganjerry@gmail.com> - 9.6.2-1
- ntl-9.6.2

* Fri Oct 16 2015 Jerry James <loganjerry@gmail.com> - 9.4.0-1
- ntl-9.4.0

* Sat Sep 19 2015 Jerry James <loganjerry@gmail.com> - 9.3.0-1
- ntl-9.3.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 16 2015 Jerry James <loganjerry@gmail.com> - 9.1.1-1
- ntl-9.1.1

* Sat May  9 2015 Jerry James <loganjerry@gmail.com> - 9.1.0-1
- ntl-9.1.0

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 8.1.2-3
- Rebuilt for GCC 5 C++11 ABI change

* Wed Apr 01 2015 Rex Dieter <rdieter@fedoraproject.org> 8.1.2-2
- rebuild (#1206849)

* Mon Feb  2 2015 Jerry James <loganjerry@gmail.com> - 8.1.2-1
- ntl-8.1.2
- Remove add of tag to libtool mode operations; changes commented lines only

* Thu Jan 15 2015 Jerry James <loganjerry@gmail.com> - 8.1.0-1
- ntl-8.1.0

* Tue Oct 28 2014 Jerry James <loganjerry@gmail.com> - 6.2.1-1
- ntl-6.2.1
- Fix license handling
- Link with Fedora LDFLAGS

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr  2 2014 Jerry James <loganjerry@gmail.com> - 6.1.0-1
- ntl-6.1.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May  6 2013 Jerry James <loganjerry@gmail.com> - 6.0.0-1
- ntl-6.0.0
- Add -sagemath patch to let sagemath handle NTL errors

* Sat Jan 26 2013 Rex Dieter <rdieter@fedoraproject.org> 5.5.2-9
- ntl should explicitly link to libstdc++ (#904348)

* Thu Aug 16 2012 Jerry James <loganjerry@gmail.com> - 5.5.2-8
- Build with gf2x support (#848870)
- Run ldconfig in post and postun

* Wed Aug 08 2012 Rex Dieter <rdieter@fedoraproject.org> 5.5.2-7
- Broken ntl-devel due to problems in multilib support (#846497)

* Wed Aug  1 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 5.5.2-6
- Add tag to mode options for libtool (fixes FTBFS on ARM)

* Tue Jul 31 2012 Rex Dieter <rdieter@fedoraproject.org> - 5.5.2-5
- better multilib conflict handling (%%{__isa_bits})
- tighten subpkg deps (%%{?_isa})

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.2-4.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.2-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Marcela Mašláňová <mmaslano@redhat.com> - 5.5.2-2.2
- rebuild with new gmp without compat lib

* Wed Oct 12 2011 Peter Schiffer <pschiffe@redhat.com> - 5.5.2-2.1
- rebuild with new gmp

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 18 2009 Rex Dieter <rdieter@fedoraproject.org> - 5.5.2-1
- ntl-5.5.2

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 17 2009 Rex Dieter <rdieter@fedoraproject.org> - 5.5-1
- ntl-5.5
- enable shared libs (and omit static lib)

* Fri Mar 20 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 5.4.2-7
- add -static virtual Provides to -devel package

* Mon Mar 02 2009 Rex Dieter <rdieter@fedoraproject.org> 5.4.2-6
- s/i386/%%ix86/
- gcc44 patch

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 11 2008 Rex Dieter <rdieter@fedoraproject.org> 5.4.2-4
- build -fPIC (#475254)

* Mon Sep 29 2008 Rex Dieter <rdieter@fedoraproject.org> 5.4.2-3
- multilib fixes

* Thu Apr 03 2008 Rex Dieter <rdieter@fedoraproject.org> 5.4.2-2
- multiarch conflicts (#342711)

* Tue Mar 11 2008 Rex Dieter <rdieter@fedoraproject.org> 5.4.2-1
- ntl-5.4.2

* Fri Feb 08 2008 Rex Dieter <rdieter@fedoraproject.org> 5.4.1-2 
- respin (gcc43)

* Tue Dec 18 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 5.4.1-1
- ntl-5.4.1

* Sat Aug 11 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 5.4-6
- License: GPLv2+
- -static -> -devel (revert previous change)

* Mon Dec 18 2006 Rex Dieter <rdieter[AT]fedoraproject.org> 5.4-5
- -devel -> -static

* Mon Aug 28 2006 Rex Dieter <rexdieter[AT]users.sf.net> 5.4-4
- fc6 respin

* Tue Jul 25 2006 Rex Dieter <rexdieter[AT]users.sf.net> 5.4-3
- fc6 respin

* Tue Apr 11 2006 Rex Dieter <rexdieter[AT]users.sf.net> 5.4-2
- Capitalize %%summary
- disable -debuginfo, includes no debuginfo'able bits 

* Fri Jan 20 2006 Rex Dieter <rexdieter[AT]users.sf.net> 5.4-1
- 5.4 (first try)


