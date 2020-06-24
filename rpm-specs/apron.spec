Name:           apron
Version:        0.9.12
Release:        7%{?dist}
Summary:        Numerical abstract domain library

# The entire package is LGPLv2+ except newpolka/mf_qsort.c and ppl/*, all of
# which are GPLv2+.  This means that libpolkaMPQ.so.*, libpolkaRll.so.*, and
# libap_ppl.so.* are GPLv2+, and the other libraries are all LGPLv2+.
License:        LGPLv2+ and GPLv2+
URL:            https://antoinemine.github.io/Apron/doc/
Source0:        https://github.com/antoinemine/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# This patch has not been sent upstream as it is GCC-specific.  Certain
# symbols are defined in both libpolkaMPQ and libpolkaRll, with different
# implementations.  This patch makes references to those symbols in
# libap_pkgrid be weak references, since that library can be combined with
# either of the 2 implementations.
Patch0:         %{name}-weak.patch
# Adapt to texinfo 6.x
Patch1:         %{name}-texinfo.patch
# Adapt to mpfr 4
Patch2:         %{name}-mpfr4.patch

BuildRequires:  doxygen-latex
BuildRequires:  gcc-c++
BuildRequires:  ghostscript-tools-dvipdf
BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  mpfr-devel
BuildRequires:  ppl-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-camlidl-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-mlgmpidl-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  perl-interpreter
BuildRequires:  tex(adjustbox.sty)
BuildRequires:  tex(etoc.sty)
BuildRequires:  tex(fullpage.sty)
BuildRequires:  tex(hanging.sty)
BuildRequires:  tex(listofitems.sty)
BuildRequires:  tex(newunicodechar.sty)
BuildRequires:  tex(stackengine.sty)
BuildRequires:  tex(tabu.sty)
BuildRequires:  tex(ulem.sty)
BuildRequires:  texinfo-tex

%global sover %(cut -d. -f 1 <<< %{version})

%description
The APRON library is dedicated to the static analysis of the numerical
variables of a program by Abstract Interpretation.  The aim of such an
analysis is to infer invariants about these variables, like 1<=x+y<=z,
which holds during any execution of the program.

The APRON library is intended to be a common interface to various
underlying libraries/abstract domains and to provide additional services
that can be implemented independently from the underlying
library/abstract domain.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}
Requires:       mpfr-devel%{?_isa}
Provides:       bundled(jquery)

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package -n     ocaml-%{name}
Summary:        Ocaml interface to APRON
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n ocaml-%{name}
Ocaml interface to the APRON library.

%package -n     ocaml-%{name}-devel
Summary:        Development files for the Ocaml interface to APRON
Requires:       ocaml-%{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-camlidl-devel%{?_isa}
Requires:       ocaml-mlgmpidl-devel%{?_isa}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description -n ocaml-%{name}-devel
Development files for the Ocaml interface to the APRON library.

%package -n     japron
Summary:        Java interface to APRON
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n japron
Java interface to the APRON library.

%prep
%autosetup -p0

# Fix library path for 64-bit installs
if [ "%{_lib}" = "lib64" ]; then
  sed -i 's,\${apron_prefix}/lib,&64,' configure
  sed -i 's,/lib,&64,' vars.mk
fi

# Add sonames
sed "s|(-shared -o \\\$@ \\\$\^ \\\$\(LIBS.*\))|\1 -Wl,-soname=\$@.%{sover}|" \
    -ri apronxx/Makefile
sed -i "s|_APRON_DYLIB)|& -Wl,-h,\$@.%{sover}|" apron/Makefile \
    box/Makefile newpolka/Makefile octagons/Makefile ppl/Makefile \
    products/Makefile taylor1plus/Makefile

# Fix encodings
iconv -f iso8859-1 -t utf-8 Changes > Changes.utf8
touch -r Changes Changes.utf8
mv -f Changes.utf8 Changes

# Preserve timestamps when copying
sed -i 's/^\([[:blank:]]*cp[[:blank:]]\)/\1-p /' Makefile */Makefile

# Do not change -O2 to -O3
sed -i 's/-O3/-O2/' configure Makefile.config.model

# Link the OCaml objects with our LDFLAGS
sed -e "s|\$(OCAMLMKLIB) -L.*|& -g -ldopt '$RPM_LD_FLAGS'|" \
    -e "/CMXS/s|-linkall|-ccopt '$RPM_LD_FLAGS' &|" \
    -i vars.mk

%build
# This is NOT an autoconf-generated script.  Do not use %%configure
export CPPFLAGS="-D_GNU_SOURCE"
export CFLAGS="%{optflags} -fsigned-char"
export CXXFLAGS="%{optflags} -fsigned-char"
export LDFLAGS="$RPM_LD_FLAGS"
export JAVA_HOME="%{_jvmdir}/java"
export JAVA_TOOL_OPTIONS="-Dfile.encoding=UTF8"
./configure -prefix %{_prefix} -java-prefix %{_jvmdir}/java

# Put back a flag that the configure script strips out
sed -i 's/-Wp,-D_FORTIFY_SOURCE=2/-Werror=format-security &/' Makefile.config

# Parallel builds fail intermittently
make
make doc

# for some reason this is no longer built in `make doc`
make -C mlapronidl mlapronidl.pdf

%install
# Install the ocaml bits into the buildroot
sed -i 's, install ,&-destdir %{buildroot}%{_libdir}/ocaml -ldconf ignore ,' \
    Makefile

# Install
mkdir -p %{buildroot}%{_libdir}/ocaml
mkdir -p %{buildroot}%{_jnidir}
make install INSTALL="install -p" APRON_PREFIX=%{buildroot}%{_prefix} \
  JAVA_PREFIX=%{buildroot}%{_jnidir}

# Move the JNI shared objects
mv %{buildroot}%{_libdir}/libj*.so %{buildroot}%{_jnidir}

# We don't really want the test binaries
rm -fr %{buildroot}%{_bindir}

# Move the header files into a subdirectory
mkdir %{buildroot}%{_includedir}/%{name}
mv %{buildroot}%{_includedir}/*.h %{buildroot}%{_includedir}/apronxx \
   %{buildroot}%{_includedir}/oct %{buildroot}%{_includedir}/%{name}

# Remove extraneous executable bits
find %{buildroot}%{_includedir} \( -name \*.h -o -name \*.hh \) \
     -perm /0111 -execdir chmod a-x {} +

# Erase the static libraries
rm -f %{buildroot}%{_libdir}/*.a

# Fix up the shared library names
pushd %{buildroot}%{_libdir}
for f in lib*.so; do
  mv $f $f.%{version}
  ln -s $f.%{sover} $f
  ln -s $f.%{version} $f.%{sover}
done
popd

# Don't have two sets of documentation both named html
mkdir doc
mv apron/html doc/apron
mv apronxx/doc/html doc/apronxx

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}:%{buildroot}%{_libdir}/ocaml/apron
make -C test APRON_INCLUDE=%{buildroot}%{_includedir}/%{name} \
  APRON_LIB=%{buildroot}%{_libdir}/ocaml/%{name} \
  CAMLIDL_PREFIX=%{buildroot}%{_libdir}
test/ctest1

%files
%doc AUTHORS Changes README.md apron/apron.pdf
%license COPYING
%{_libdir}/lib*.so.0
%{_libdir}/lib*.so.0.*

%files devel
%doc doc/apron doc/apronxx
%{_libdir}/lib*.so
%{_includedir}/%{name}/

%files -n ocaml-%{name}
%doc mlapronidl/mlapronidl.pdf
%dir %{_libdir}/ocaml/%{name}/
%{_libdir}/ocaml/%{name}/META
%{_libdir}/ocaml/%{name}/*.cma
%{_libdir}/ocaml/%{name}/*.cmi
%{_libdir}/ocaml/%{name}/*.cmxs
%{_libdir}/ocaml/%{name}/*.so

%files -n ocaml-%{name}-devel
%doc mlapronidl/html/*
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{name}/*.a
%{_libdir}/ocaml/%{name}/*.cmxa
%{_libdir}/ocaml/%{name}/*.cmx
%endif
%{_libdir}/ocaml/%{name}/*.h
%{_libdir}/ocaml/%{name}/*.idl
%{_libdir}/ocaml/%{name}/*.mli

%files -n japron
%doc japron/README
%license japron/COPYING
%{_jnidir}/*.jar
%{_jnidir}/*.so

%changelog
* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.12-7
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.12-6
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.12-5
- OCaml 4.11.0 pre-release

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.12-4
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.12-3
- OCaml 4.10.0 final.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.9.12-1
- New upstream release 0.9.12

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-33.1104.svn20180624
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-32.1104.svn20180624
- OCaml 4.09.0 for riscv64

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-31.1104.svn20180624
- Bump release and rebuild.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-30.1104.svn20180624
- OCaml 4.09.0 (final) rebuild.

* Fri Oct 11 2019 Jerry James <loganjerry@gmail.com> - 0.9.11-29.1104.svn20180624
- Add -mpfr4 patch and rebuild for mpfr 4

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-28.1104.svn20180624
- OCaml 4.08.1 (final) rebuild.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-27.1104.svn20180624
- OCaml 4.08.1 (rc2) rebuild.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-26.1104.svn20180624
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-25.1104.svn20180624
- OCaml 4.08.0 (final) rebuild.

* Mon Apr 29 2019 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-24.1104.svn20180624
- OCaml 4.08.0 (beta 3) rebuild.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-23.1104.svn20180624
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-22.1104.svn20180624
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-21.1104.svn20180624
- OCaml 4.07.0 (final) rebuild.

* Sat Jul  7 2018 Jerry James <loganjerry@gmail.com> - 0.9.11-20.1104.svn20180624
- Update to latest subversion commit

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-19.1097.svn20160801
- Bump release and rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-18.1097.svn20160801
- Bump release and rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-17.1097.svn20160801
- Bump release and rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-16.1097.svn20160801
- Bump release and rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-15.1097.svn20160801
- OCaml 4.07.0-rc1 rebuild.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-14.1097.svn20160801
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec  4 2017 Jerry James <loganjerry@gmail.com> - 0.9.11-13.1097.svn20160801
- Rebuild for mlgmpidl 1.2.6-1

* Fri Nov 17 2017 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-12.1097.svn20160801
- OCaml 4.06.0 rebuild.

* Tue Aug 08 2017 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-11.1097.svn20160801
- OCaml 4.05.0 rebuild.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-10.1097.svn20160801
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-9.1097.svn20160801
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-8.1097.svn20160801
- OCaml 4.04.2 rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-7.1097.svn20160801
- OCaml 4.04.1 rebuild.

* Fri Mar 24 2017 Jerry James <loganjerry@gmail.com> - 0.9.11-6.1097.svn20160801
- Rebuild for mlgmpidl

* Fri Mar  3 2017 Jerry James <loganjerry@gmail.com> - 0.9.11-5.1097.svn20160801
- Update to latest subversion commit and rebuild for ppl 1.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-4.1096.svn20160531
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 09 2016 Dan Horák <dan@danny.cz> - 0.9.11-3.1096.svn20160531
- rebuild for s390x codegen bug

* Sun Nov 06 2016 Richard W.M. Jones <rjones@redhat.com> - 0.9.11-2.1096.svn20160531
- Rebuild for OCaml 4.04.0.

* Sat Jul 16 2016 Jerry James <loganjerry@gmail.com> - 0.9.11-1.1096.svn20160531
- Update to latest subversion commit

* Sun Mar 06 2016 Than Ngo <than@redhat.com> - 0.9.10-36.svn20160125
- remove wWorkaround bz 1305739; it's fixed in lates doxygen

* Fri Feb 12 2016 Jerry James <loganjerry@gmail.com> - 0.9.10-35.1091.svn20160125
- Some ocaml projects need the debug libraries; add them back in

* Fri Feb 12 2016 Jerry James <loganjerry@gmail.com> - 0.9.10-34.1091.svn20160125
- Update to latest subversion commit
- Add japron subpackage with the Java interface
- Add %%check script
- Drop upstreamed -format-security, -mlgmpidl12, -test, and -ppl1 patches
- Add -texinfo patch to fix documentation build failure

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.10-32
- Bump release and rebuild.

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.10-31
- OCaml 4.02.3 rebuild.

* Tue Jul 21 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.10-30
- Fix bytecode compilation.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.10-29
- ocaml-4.02.2 final rebuild.

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.10-28
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.10-26
- Rebuilt for GCC 5 C++11 ABI change

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.10-25
- ocaml-4.02.1 rebuild.

* Wed Feb 11 2015 Jerry James <loganjerry@gmail.com> - 0.9.10-24
- Use license macro

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.10-23
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.10-22
- ocaml-4.02.0+rc1 rebuild.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.10-20
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Mon Jul 21 2014 Jerry James <loganjerry@gmail.com> - 0.9.10-19
- OCaml 4.02.0 beta rebuild

* Fri Jun 27 2014 Jerry James <loganjerry@gmail.com> - 0.9.10-18
- Build with -fsigned-char to fix FTBFS on aarch64
- Use a better test for installing files into 64-bit libdir

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Jerry James <loganjerry@gmail.com> - 0.9.10-16
- Rebuild for ppl 1.1

* Fri Apr 18 2014 Jerry James <loganjerry@gmail.com> - 0.9.10-15
- Ensure GNU extensions are enabled to fix build failure

* Tue Apr 15 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.10-15
- Remove ocaml_arches macro (RHBZ#1087794).

* Wed Nov 20 2013 Jerry James <loganjerry@gmail.com> - 0.9.10-14
- Add -format-security patch

* Sat Sep 14 2013 Richard W.M. Jones <rjones@redhat.com> - 0.9.10-13
- Rebuild for OCaml 4.01.0.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Jerry James <loganjerry@gmail.com> - 0.9.10-11
- Add -ppl1 patch to adapt to PPL 1.0 + GMP 5.1.0
- Update -mlgmpidl12 patch to fix more problems

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 30 2012 Tom Callaway <spot@fedoraproject.org> - 0.9.10-10
- rebuild for ppl

* Wed Oct 17 2012 Jerry James <loganjerry@gmail.com> - 0.9.10-9
- Rebuild for OCaml 4.00.1

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun  9 2012 Jerry James <loganjerry@gmail.com> - 0.9.10-7
- Rebuild for OCaml 4.00.0

* Wed May  9 2012 Jerry James <loganjerry@gmail.com> - 0.9.10-6
- Rebuild for new ocaml-mlgmpidl

* Fri Jan  6 2012 Jerry James <loganjerry@gmail.com> - 0.9.10-5
- Rebuild for GCC 4.7 and Ocaml 3.12.1

* Tue Nov  8 2011 Jerry James <loganjerry@gmail.com> - 0.9.10-4
- -devel also needs ocaml-camlidl-devel
- Pass --as-needed to the linker to fix unused shared library dependencies

* Fri Nov  4 2011 Jerry James <loganjerry@gmail.com> - 0.9.10-3
- Comment on license situation
- Drop debug libraries altogether

* Wed Aug 24 2011 Jerry James <loganjerry@gmail.com> - 0.9.10-2
- Correct license
- Build C and C++ interfaces even when the ocaml interface cannot be built
- Move debug libraries to separate packages

* Fri Jul  8 2011 Jerry James <loganjerry@gmail.com> - 0.9.10-1
- Initial RPM
