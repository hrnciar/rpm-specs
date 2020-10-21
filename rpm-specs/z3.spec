Name:           z3
Version:        4.8.9
Release:        2%{?dist}
Summary:        Satisfiability Modulo Theories (SMT) solver

License:        MIT
URL:            https://github.com/Z3Prover/z3
Source0:        https://github.com/Z3Prover/z3/archive/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  graphviz
BuildRequires:  help2man
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  ninja-build
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-zarith-devel
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}

%description
Z3 is a satisfiability modulo theories (SMT) solver; given a set of
constraints with variables, it reports a set of values for those
variables that would meet the constraints.  The Z3 input format is an
extension of the one defined by the SMT-LIB 2.0 standard.  Z3 supports
arithmetic, fixed-size bit-vectors, extensional arrays, datatypes,
uninterpreted functions, and quantifiers.

%package libs
Summary:        Library for applications that use z3 functionality

%description libs
Library for applications that use z3 functionality.

%package devel
Summary:        Header files for build applications that use z3
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Header files for build applications that use z3.

%package doc
Summary:        API documentation for Z3
# FIXME: this should be noarch, but we end up with different numbers of inheritance
# graphs on different architectures.  Why?

%description doc
API documentation for Z3.

%package -n java-%{name}
Summary:        Java interface to z3
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       java
Requires:       javapackages-tools

%description -n java-%{name}
Java interface to z3.

%package -n ocaml-%{name}
Summary:        Ocaml interface to z3
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description -n ocaml-%{name}
Ocaml interface to z3.

%package -n ocaml-%{name}-devel
Summary:        Files for building ocaml applications that use z3
Requires:       ocaml-%{name}%{?_isa} = %{version}-%{release}

%description -n ocaml-%{name}-devel
Files for building ocaml applications that use z3.

%package -n python3-%{name}
Summary:        Python 3 interface to z3
BuildArch:      noarch
Requires:       %{name}-libs = %{version}-%{release}

%description -n python3-%{name}
Python 3 interface to z3.

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}

# Enable verbose builds, use Fedora CFLAGS, preserve timestamps when installing,
# include the entire contents of the archives in the library, link the library
# with the correct flags, and build the ocaml files with debuginfo.
sed \
  -e 's/@$(CXX)/$(CXX)/' \
  -e '/O3/d' \
  -e "s/\(['\"]\)cp\([^[:alnum:]]\)/\1cp -p\2/" \
  -e "s/\(SLIBEXTRAFLAGS = '\)'/\1-Wl,--no-whole-archive -Wl,--as-needed'/" \
  -e "/SLIBFLAGS/s|-shared|& $RPM_LD_FLAGS -Wl,--whole-archive|" \
  -e 's/\(libz3$(SO_EXT)\)\(\\n\)/\1 -Wl,--no-whole-archive\2/' \
  -e "s/OCAML_FLAGS = ''/OCAML_FLAGS = '-g'/" \
  -i scripts/mk_util.py

# Comply with the Java packaging guidelines
sed -e '/libz3java/s,\(System\.load\)Library("\(.*\)"),\1("%{_libdir}/z3/\2.so"),' \
    -i scripts/update_api.py

# Update an OCaml interface
sed -i 's/Pervasives/Stdlib/' src/api/ml/z3.ml

# FIXME: For unknown reasons, cmake replaces the version with nothing at all
sed -i 's/@VERSION@/%{version}/' z3.pc.cmake.in

# Fix character encoding
iconv -f iso8859-1 -t utf-8 RELEASE_NOTES > RELEASE_NOTES.utf8
touch -r RELEASE_NOTES RELEASE_NOTES.utf8
mv -f RELEASE_NOTES.utf8 RELEASE_NOTES

%build
export CXXFLAGS="$RPM_OPT_FLAGS"
export LANG="C.UTF-8"
export PYTHON="%{python3}"

%cmake -G Ninja \
  -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir}/%{name} \
  -DCMAKE_JAVA_COMPILE_FLAGS="-source;1.8;-target;1.8" \
  -DZ3_BUILD_DOCUMENTATION:BOOL=ON \
  -DZ3_BUILD_JAVA_BINDINGS:BOOL=ON \
  -DZ3_BUILD_PYTHON_BINDINGS:BOOL=ON \
  -DZ3_INCLUDE_GIT_HASH:BOOL=OFF \
  -DZ3_INCLUDE_GIT_DESCRIBE:BOOL=OFF \
  -DZ3_USE_LIB_GMP:BOOL=ON

%cmake_build

# The cmake build system does not build the OCaml interface.  Do that manually.
#
# First, run the configure script to generate several files.
# This is NOT an autoconf-generated configure script.
./configure -p %{_prefix} --gmp --ml

# Second, to prevent make from rebuilding the entire library, copy the
# cmake-built library to where make expects it.
cp -dp %{_vpath_builddir}/libz3.so* build

# Third, make wants to rebuild libz3.so since its dependencies do not exist.
# Do selective Makefile surgery to prevent this.
sed -i '/^api/s/ libz3\$(SO_EXT)//g' build/Makefile

# Fourth, build the OCaml interface
%make_build -C build ml

%install
export LANG="C.UTF-8"

# Install the C++, python3, and Java interfaces
%cmake_install

# Move the Java interface to its correct location
mkdir -p %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_jnidir}
mv %{buildroot}%{_javadir}/*.jar %{buildroot}%{_jnidir}
ln -s %{_jnidir}/com.microsoft.z3.jar %{buildroot}%{_libdir}/%{name}
mv %{buildroot}%{_libdir}/lib%{name}java.so %{buildroot}%{_libdir}/%{name}

# Install the OCaml interface
pushd build/api/ml
mkdir -p %{buildroot}%{_libdir}/ocaml/Z3
cp -p META *.{a,cma,cmi,cmx,cmxa,cmxs,mli} %{buildroot}%{_libdir}/ocaml/Z3
mkdir -p %{buildroot}%{_libdir}/ocaml/stublibs
cp -p *.so %{buildroot}%{_libdir}/ocaml/stublibs
popd

# We handle the documentation files below
rm -rf %{buildroot}%{_docdir}/Z3

# Make a man page
mkdir -p %{buildroot}%{_mandir}/man1
help2man -N -o %{buildroot}%{_mandir}/man1/%{name}.1 %{_vpath_builddir}/%{name}

#%%check
# Some of the tests require more memory than the koji builders have available.
#
#export LANG="C.UTF-8"
#pushd build
#make test-z3
#./test-z3 /a
#popd

%files
%doc README.md RELEASE_NOTES
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files libs
%license LICENSE.txt
%{_libdir}/lib%{name}.so.4*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc %{_vpath_builddir}/doc/api/html examples
%license LICENSE.txt

%files -n java-%{name}
%{_libdir}/%{name}/
%{_jnidir}/com.microsoft.z3*jar

%files -n ocaml-%{name}
%dir %{_libdir}/ocaml/Z3/
%{_libdir}/ocaml/Z3/META
%{_libdir}/ocaml/Z3/*.cma
%{_libdir}/ocaml/Z3/*.cmi
%{_libdir}/ocaml/Z3/*.cmxs
%{_libdir}/ocaml/stublibs/*.so

%files -n ocaml-%{name}-devel
%{_libdir}/ocaml/Z3/*.a
%{_libdir}/ocaml/Z3/*.cmx
%{_libdir}/ocaml/Z3/*.cmxa
%{_libdir}/ocaml/Z3/*.mli

%files -n python3-%{name}
%{python3_sitelib}/%{name}/

%changelog
* Fri Sep 25 2020 Jerry James <loganjerry@gmail.com> - 4.8.9-2
- Rebuild for ocaml-zarith 1.10

* Fri Sep 11 2020 Jerry James <loganjerry@gmail.com> - 4.8.9-1
- Version 4.8.9

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 4.8.8-7
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 4.8.8-6
- OCaml 4.11.0 rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Jerry James <loganjerry@gmail.com> - 4.8.8-4
- Build with cmake
- Manually build the OCaml interface
- Limit the class file version in the Java interface
- Allow the library to hide internal symbols; this means that the binary can no
  longer be linked with the library, so the main package does not depend on
  the -libs package
- The python package no longer contains an ELF object, so make it noarch

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 4.8.8-4
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.8.8-3
- Rebuilt for Python 3.9

* Thu May 14 2020 Wolfgang Stöggl <c72578@yahoo.de> - 4.8.8-2
- Add Z3 cmake files required by find_package(Z3)

* Sat May  9 2020 Jerry James <loganjerry@gmail.com> - 4.8.8-1
- Version 4.8.8
- Drop all patches; all have been upstreamed

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 4.8.7-10
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 4.8.7-9
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 4.8.7-8
- OCaml 4.11.0 pre-release

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 4.8.7-7
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 4.8.7-6
- OCaml 4.10.0 final.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Jerry James <loganjerry@gmail.com> - 4.8.7-4
- Make -doc be archful (bz 1792740)
- Add -signed-char and -gcc-10-s390x patches

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 4.8.7-4
- OCaml 4.10.0+beta1 rebuild.

* Fri Jan 10 2020 Richard W.M. Jones <rjones@redhat.com> - 4.8.7-3
- OCaml 4.09.0 for riscv64

* Sat Dec  7 2019 Jerry James <loganjerry@gmail.com> - 4.8.7-2
- OCaml 4.09.0 (final) rebuild

* Thu Nov 21 2019 Jerry James <loganjerry@gmail.com> - 4.8.7-1
- New upstream version
- Add -ocamldoc patch to fix documentation build failure
- Add -trailing-zeros32 patch to fix build failures on some platforms

* Fri Sep 20 2019 Jerry James <loganjerry@gmail.com> - 4.8.6-1
- New upstream version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.8.5-6
- Rebuilt for Python 3.8

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 4.8.5-5
- OCaml 4.08.1 (final) rebuild.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 4.8.5-4
- OCaml 4.08.1 (rc2) rebuild.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Richard W.M. Jones <rjones@redhat.com> - 4.8.5-2
- OCaml 4.08.0 (final) rebuild.

* Sat Jun 22 2019 Jerry James <loganjerry@gmail.com> - 4.8.5-1
- New upstream version

* Mon Apr 29 2019 Richard W.M. Jones <rjones@redhat.com> - 4.8.4-3
- OCaml 4.08.0 (beta 3) rebuild.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 24 2018 Jerry James <loganjerry@gmail.com> - 4.8.4-1
- New upstream version
- Drop -no-sse patch, now handled upstream

* Wed Nov 28 2018 Jerry James <loganjerry@gmail.com> - 4.8.3-1
- New upstream version

* Tue Oct 30 2018 Jerry James <loganjerry@gmail.com> - 4.8.1-1
- New upstream version
- Drop python2 subpackage (bz 1634981)

* Fri Sep  7 2018 Jerry James <loganjerry@gmail.com> - 4.7.1-5
- Build with SSE2 support on 32-bit x86

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 4.7.1-4
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 4.7.1-3
- OCaml 4.07.0-rc1 rebuild.

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.7.1-2
- Rebuilt for Python 3.7

* Tue May 22 2018 Jerry James <loganjerry@gmail.com> - 4.7.1-1
- New upstream version (bz 1581516)
- Drop upstreamed -vector patch

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 24 2017 Jerry James <loganjerry@gmail.com> - 4.6.0-1
- New upstream version (bz 1527531)
- Add a python3 subpackage

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.5.0-8
- Python 2 binary package renamed to python2-z3
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Fri Nov 17 2017 Richard W.M. Jones <rjones@redhat.com> - 4.5.0-7
- OCaml 4.06.0 rebuild.
- Add dependency on ocaml-num.

* Tue Aug 08 2017 Richard W.M. Jones <rjones@redhat.com> - 4.5.0-6
- OCaml 4.05.0 rebuild.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 4.5.0-4
- OCaml 4.04.2 rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 4.5.0-3
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov  8 2016 Jerry James <loganjerry@gmail.com> - 4.5.0-1
- New upstream version
- All patches except -sse2 have been upstreamed; drop them
- Upstream now ships __init__.py; drop our version
- Drop all the buildroot tricks; Makefile supports DESTDIR now
- Use C.UTF-8 instead of en_US.UTF-8

* Sat Nov 05 2016 Richard W.M. Jones <rjones@redhat.com> - 4.4.1-8
- Rebuild for OCaml 4.04.0.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.1-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jul 13 2016 Jerry James <loganjerry@gmail.com> - 4.4.1-6
- Fix Java interface (bz 1353773)

* Thu Jun 30 2016 Jerry James <loganjerry@gmail.com> - 4.4.1-5
- Fix __init__.py (bz 1351580)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Jonathan Wakely <jwakely@redhat.com> - 4.4.1-3
- Patched for C++11 compatibility.

* Wed Jan 20 2016 Jerry James <loganjerry@gmail.com> - 4.4.1-2
- Add __init__.py to the python interface (bz 1298429)

* Thu Oct  8 2015 Jerry James <loganjerry@gmail.com> - 4.4.1-1
- New upstream version

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 4.4.0-4
- OCaml 4.02.3 rebuild.

* Thu Jun 25 2015 Richard W.M. Jones <rjones@redhat.com> - 4.4.0-3
- ocaml-4.02.2 final rebuild.

* Thu Jun 18 2015 Richard W.M. Jones <rjones@redhat.com> - 4.4.0-2
- ocaml-4.02.2 rebuild.

* Wed May 27 2015 Jerry James <loganjerry@gmail.com> - 4.4.0-1
- New upstream version

* Wed Apr 22 2015 Jerry James <loganjerry@gmail.com> - 4.3.2-3.20150329git.29606b5
- Fix issues found on review (bz 1206826)

* Mon Mar 30 2015 Jerry James <loganjerry@gmail.com> - 4.3.2-2.20150329git.29606b5
- Update to latest git HEAD
- Include examples in -doc

* Sat Mar 28 2015 Jerry James <loganjerry@gmail.com> - 4.3.2-1.20150327git.ac21ffe
- Initial RPM
