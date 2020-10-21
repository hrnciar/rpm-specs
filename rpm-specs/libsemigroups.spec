Name:           libsemigroups
Version:        1.3.2
Release:        1%{?dist}
Summary:        C++ library for semigroups and monoids

License:        GPLv3+
URL:            https://github.com/libsemigroups/libsemigroups
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Fix bugs in the configure code
Patch0:         %{name}-autoconf.patch

BuildRequires:  doxygen
BuildRequires:  fontawesome-fonts-web
BuildRequires:  font(fontawesome)
BuildRequires:  font(lato)
BuildRequires:  font(robotoslab)
BuildRequires:  fontconfig
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  python3dist(beautifulsoup4)
BuildRequires:  python3dist(breathe)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-copybutton)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(sphinxcontrib-bibtex)

%description
Libsemigroups is a C++ library for semigroups and monoids; it is partly
based on "Algorithms for computing finite semigroups", "Expository
Slides", and Semigroupe 2.01 by Jean-Eric Pin.

The libsemigroups library is used in the Semigroups package for GAP.

Some of the features of Semigroupe 2.01 are not yet implemented in
libsemigroups; this is a work in progress.  Missing features include
those for:

- Green's relations, or classes
- finding a zero
- minimal ideal, principal left/right ideals, or indeed any ideals
- inverses
- local submonoids
- the kernel
- variety tests.
These will be included in a future version.

Libsemigroups performs roughly the same as Semigroupe 2.01 when there is
a known upper bound on the size of the semigroup being enumerated, and
this is used to initialize the data structures for the semigroup; see
libsemigroups::Semigroup::reserve for more details.  Note that in
Semigroupe 2.01 it is always necessary to provide such an upper bound,
but in libsemigroups it is not.

Libsemigroups also has some advantages over Semigroupe 2.01:
- there is a (hopefully) convenient C++ API, which makes it relatively
  easy to create and manipulate semigroups and monoids
- there are some multithreaded methods for semigroups and their
  congruences
- you do not have to know/guess the size of a semigroup or monoid before
  you begin
- libsemigroups supports more types of elements than Semigroupe 2.01
- it is relatively straightforward to add support for further types of
  elements and semigroups
- it is possible to enumerate a certain number of elements of a
  semigroup or monoid (say if you are looking for an element with a
  particular property), to stop, and then to start the enumeration again
  at a later point
- you can instantiate as many semigroups and monoids as you can fit in
  memory
- it is possible to add more generators after a semigroup or monoid has
  been constructed, without losing or having to recompute any
  information that was previously known
- libsemigroups contains rudimentary implementations of the Todd-Coxeter
  and Knuth-Bendix algorithms for finitely presented semigroups, which
  can also be used to compute congruences of a (not necessarily finitely
  presented) semigroup or monoid.

%package devel
Summary:        Headers files for developing with %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       eigen3-devel
Requires:       fmt-devel%{?_isa}

%description devel
Header files for developing applications that use %{name}.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       fontawesome-fonts-web
Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)

%description doc
Documentation for %{name}.

%prep
%autosetup -p1

# Regenerate configure due to patch0
autoreconf -fi .

%build
# Hpcombi is an x86-specific library that uses SSE and AVX instructions.
# It is not currently available in Fedora, and we cannot assume the
# availability of AVX in any case.
export CFLAGS="%{optflags} -fwrapv"
export CXXFLAGS="$CFLAGS"
%configure --disable-silent-rules --disable-static --disable-hpcombi \
  --enable-eigen --with-external-eigen --enable-fmt --with-external-fmt

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build
%make_build doc
rst2html --no-datestamp README.rst README.html
rm docs/build/html/.buildinfo

# Do not bundle fonts into the documentation
cd docs/build/html/_static/fonts
for suffix in eot svg ttf woff woff2; do
  rm fontawesome-webfont.$suffix
  ln -s %{_datadir}/fonts/fontawesome/fontawesome-webfont.$suffix .
done
rm {Lato,RobotoSlab}/*.ttf
ln -s $(fc-match -f "%%{file}" "lato:bold") Lato/lato-bold.ttf
ln -s $(fc-match -f "%%{file}" "lato:bold:italic") Lato/lato-bolditalic.ttf
ln -s $(fc-match -f "%%{file}" "lato:italic") Lato/lato-italic.ttf
ln -s $(fc-match -f "%%{file}" "lato") Lato/lato-regular.ttf
ln -s $(fc-match -f "%%{file}" "robotoslab:bold") RobotoSlab/roboto-slab-v7-bold.ttf
ln -s $(fc-match -f "%%{file}" "robotoslab") RobotoSlab/roboto-slab-v7-regular.ttf
cd -

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la

fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Do not bundle the eigen3 headers
rm -fr %{buildroot}%{_includedir}/libsemigroups/Eigen

# Do not bundle the fmt headers
rm -fr %{buildroot}%{_includedir}/libsemigroups/fmt
sed -i.orig 's,"\(fmt/[[:alnum:]]*\.h\)",<\1>,g' \
    %{buildroot}%{_includedir}/libsemigroups/report.hpp
fixtimestamp %{buildroot}%{_includedir}/libsemigroups/report.hpp

%check
LD_LIBRARY_PATH=$PWD/.libs make check

%files
%doc README.html
%license LICENSE
%{_libdir}/%{name}.so.1
%{_libdir}/%{name}.so.1.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc docs/build/html
%license LICENSE

%changelog
* Sat Oct  3 2020 Jerry James <loganjerry@gmail.com> - 1.3.2-1
- Version 1.3.2

* Mon Aug 31 2020 Jerry James <loganjerry@gmail.com> - 1.3.1-3
- Fix the eigen3-devel dependency from -devel

* Mon Aug 31 2020 Jerry James <loganjerry@gmail.com> - 1.3.1-2
- Do not ship the eigen3 headers in -devel

* Mon Aug 31 2020 Jerry James <loganjerry@gmail.com> - 1.3.1-1
- Version 1.3.1
- Add -autoconf patch
- Add BR on eigen3
- Do not ship the fmt headers in -devel

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Jerry James <loganjerry@gmail.com> - 1.2.1-1
- Version 1.2.1

* Fri Jun 12 2020 Jerry James <loganjerry@gmail.com> - 1.1.0-1
- Version 1.1.0

* Tue Apr 21 2020 Jerry James <loganjerry@gmail.com> - 1.0.9-1
- Version 1.0.9

* Mon Apr 20 2020 Jerry James <loganjerry@gmail.com> - 1.0.8-1
- Version 1.0.8
- Drop upstreamed -fmt patch

* Thu Apr  9 2020 Jerry James <loganjerry@gmail.com> - 1.0.7-2
- Add -fmt patch for compatibility with fmt 6.2.0

* Sat Mar 21 2020 Jerry James <loganjerry@gmail.com> - 1.0.7-1
- Version 1.0.7
- Create font symlinks with fc-match for greater robustness

* Sun Feb  9 2020 Jerry James <loganjerry@gmail.com> - 1.0.6-1
- Version 1.0.6

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Jerry James <loganjerry@gmail.com> - 1.0.5-1
- Version 1.0.5
- Drop -unbundle-fmt patch in favor of --with-external-fmt arg to configure

* Fri Dec 13 2019 Jerry James <loganjerry@gmail.com> - 1.0.3-1
- Version 1.0.3
- New URLs
- Drop -use-after-free patch
- Unbundle fmt

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Jerry James <loganjerry@gmail.com> - 0.6.7-1
- New upstream version

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 22 2018 Jerry James <loganjerry@gmail.com> - 0.6.4-1
- New upstream version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Jerry James <loganjerry@gmail.com> - 0.6.3-1
- New upstream version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 13 2018 Jerry James <loganjerry@gmail.com> - 0.6.2-1
- New upstream version

* Sat Dec 30 2017 Jerry James <loganjerry@gmail.com> - 0.6.1-1
- New upstream version
- Add -use-after-free patch to fix test failures

* Tue Dec 12 2017 Jerry James <loganjerry@gmail.com> - 0.6.0-1
- New upstream version

* Sat Oct  7 2017 Jerry James <loganjerry@gmail.com> - 0.5.2-1
- New upstream version

* Sat Sep 30 2017 Jerry James <loganjerry@gmail.com> - 0.5.0-1
- New upstream version

* Mon Sep  4 2017 Jerry James <loganjerry@gmail.com> - 0.3.2-1
- New upstream version

* Sun Jul 30 2017 Jerry James <loganjerry@gmail.com> - 0.3.1-3
- Install the license with the -doc subpackage
- Make -doc noarch

* Sat Jul 29 2017 Jerry James <loganjerry@gmail.com> - 0.3.1-2
- Move documentation to a -doc subpackage
- Link with libpthread to fix an undefined non-weak symbol
- Kill the rpath

* Thu Jul 27 2017 Jerry James <loganjerry@gmail.com> - 0.3.1-1
- Initial RPM
