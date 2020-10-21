Name:           cddlib
Epoch:          1
Version:        0.94j
Release:        6%{?dist}
Summary:        A library for generating all vertices in convex polyhedrons
License:        GPLv2+
URL:            https://www.inf.ethz.ch/personal/fukudak/cdd_home/
Source0:        https://github.com/cddlib/cddlib/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  libtool
BuildRequires:  tex(latex)

%description
The C-library cddlib is a C implementation of the Double Description 
Method of Motzkin et al. for generating all vertices (i.e. extreme points)
and extreme rays of a general convex polyhedron in R^d given by a system 
of linear inequalities:

   P = { x=(x1, ..., xd)^T :  b - A  x  >= 0 }

where A is a given m x d real matrix, b is a given m-vector 
and 0 is the m-vector of all zeros.

The program can be used for the reverse operation (i.e. convex hull
computation). This means that one can move back and forth between 
an inequality representation and a generator (i.e. vertex and ray) 
representation of a polyhedron with cdd. Also, cdd can solve a linear
programming problem, i.e. a problem of maximizing and minimizing 
a linear function over P.


%package devel
Summary:        Headers for cddlib
Requires:       gmp-devel%{?_isa}
Requires:       %{name}%{?_isa} = 1:%{version}-%{release}

%description devel
Include files for cddlib.


%package static
Summary:        Static libraries for cddlib

%description static
Static libraries for cddlib.


%package tools
Summary:        Sample binaries that use cddlib
Requires:       %{name}%{?_isa} = 1:%{version}-%{release}

%description tools
Sample binaries that use cddlib.


%prep
%autosetup -p0

# Regenerate Makefile.in files due to patched Makefile.am files
autoreconf -ifs

# Fix the FSF's address
for f in `find . -type f -print0 | xargs -0 grep -Fl '675 Mass'`; do
  sed -i.orig \
    's/675 Mass Ave, Cambridge, MA 02139/51 Franklin Street, Suite 500, Boston, MA  02110-1335/' \
    $f
  touch -r $f.orig $f
  rm -f $f.orig
done

# Force rebuilding of the documentation
rm -f doc/cddlibman.pdf


%build
%configure

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

make %{?_smp_mflags}

# Need one more invocation of pdflatex to get cross references correct
pushd doc
pdflatex cddlibman
popd


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
mkdir $RPM_BUILD_ROOT%{_includedir}/cddlib
mv $RPM_BUILD_ROOT%{_includedir}/{cdd,cdd_f,cddmp,cddmp_f,cddtypes,cddtypes_f,setoper,splitmix64}.h \
  $RPM_BUILD_ROOT%{_includedir}/cddlib/
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# Do not prematurely install documentation
rm -fr $RPM_BUILD_ROOT%{_pkgdocdir}


%ldconfig_scriptlets


%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/*.so.*


%files devel
%doc doc/cddlibman.pdf examples*
%{_includedir}/cddlib
%{_libdir}/*.so


%files static
%{_libdir}/libcdd.a
%{_libdir}/libcddgmp.a


%files tools
%{_bindir}/*


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.94j-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.94j-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 24 2019 Jerry James <loganjerry@gmail.com> - 1:0.94j-4
- Drop cdd_both_reps.c and accompanying patch, replaced with cddexec

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.94j-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.94j-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct  1 2018 Jerry James <loganjerry@gmail.com> - 0.94j-1
- New upstream release
- Add Epoch to deal with new dot in the version number

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 094i-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Jerry James <loganjerry@gmail.com> - 094i-1
- New upstream release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 094h-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 27 2017 Jerry James <loganjerry@gmail.com> - 094h-7
- Rebuild without linker aliases, no longer needed
- Update URLs

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 094h-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 094h-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 094h-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 094h-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 094h-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Jerry James <loganjerry@gmail.com> - 094h-1
- New upstream release

* Thu Mar 12 2015 Jerry James <loganjerry@mgail.com> - 094g-13
- Rebuild with hardening flags

* Wed Feb 11 2015 Jerry James <loganjerry@gmail.com> - 094g-12
- Use license macro

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 094g-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 094g-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 094g-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 094g-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 Jerry James <loganjerry@gmail.com> - 094g-7
- Add function aliases in the GMP build for polymake
- License fixing code now handles names with spaces

* Sat Jul 28 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 094g-6
- Add libtool to build requires

* Sun Jul 22 2012 Conrad Meyer <konrad@tylerc.org> - 094g-5
- Add automake BR too

* Sun Jul 22 2012 Conrad Meyer <konrad@tylerc.org> - 094g-4
- Add autoconf BR as per mass rebuild build failure

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 094g-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 5 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 094g-2
- Add sagemath patches

* Tue Apr 24 2012 Jerry James <loganjerry@gmail.com> - 094g-1
- New upstream release
- All patches upstreamed
- Non-free sources removed from upstream tarball

* Fri Apr 20 2012 Jerry James <loganjerry@gmail.com> - 094f-15
- Package the sample binaries in -tools for the use of projects such as LattE
- Add memleak patch from upstream

* Fri Feb 24 2012 Jerry James <loganjerry@gmail.com> - 094f-14
- Actually apply the const patch

* Fri Feb 24 2012 Jerry James <loganjerry@gmail.com> - 094f-13
- Add const qualifier to public function parameters
- Fix the FSF's address

* Sat Jan  7 2012 Jerry James <loganjerry@gmail.com> - 094f-12
- Rebuild for GCC 4.7
- Minor spec file cleanups

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 094f-11.2
- rebuild with new gmp without compat lib

* Mon Oct 10 2011 Peter Schiffer <pschiffe@redhat.com> - 094f-11.1
- rebuild with new gmp

* Thu Apr  7 2011 Jerry James <loganjerry@gmail.com> - 094f-11
- Build shared libraries as well as static
- Drop BuildRoot and the clean section

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 094f-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 094f-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 094f-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 28 2008 Conrad Meyer <konrad@tylerc.org> - 094f-7
- Install headers with install -p to save timestamps.
- Install headers to namespaced directory.
- Generate pdf from latex source.

* Fri Oct 31 2008 Conrad Meyer <konrad@tylerc.org> - 094f-6
- Describe vividly the process whereby the non-free file is
  stripped from the source tarball.

* Thu Oct 30 2008 Conrad Meyer <konrad@tylerc.org> - 094f-5
- Tarball scrubbed of content we are unable to ship.

* Tue Oct 28 2008 Conrad Meyer <konrad@tylerc.org> - 094f-4
- Remove modules that do not meet licensing guidelines.
- Don't generate debuginfo.

* Tue Oct 28 2008 Conrad Meyer <konrad@tylerc.org> - 094f-3
- Fix permissions on documentation.

* Mon Oct 27 2008 Conrad Meyer <konrad@tylerc.org> - 094f-2
- Incorporate several suggestions from review.

* Thu Sep 25 2008 Conrad Meyer <konrad@tylerc.org> - 094f-1
- Initial package.
