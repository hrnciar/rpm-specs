Name:           normaliz
Version:        3.8.9
Release:        1%{?dist}
Summary:        A tool for mathematical computations

License:        GPLv3+
URL:            https://www.normaliz.uni-osnabrueck.de/
Source0:        https://github.com/Normaliz/Normaliz/archive/v%{version}/%{name}-%{version}.tar.gz
# Adapt to cocoalib 0.99650
Patch0:         %{name}-cocoalib.patch

BuildRequires:  boost-devel
BuildRequires:  cocoalib-devel
BuildRequires:  e-antic-devel
BuildRequires:  flint-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  pkgconfig(nauty)

Requires:       lib%{name}%{?_isa} = %{version}-%{release}

%description
Normaliz is a tool for computations in affine monoids, vector
configurations, lattice polytopes, and rational cones.

Documentation and examples can be found in %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}},
in particular you may find Normaliz%{version}Documentation.pdf useful.  

%package -n libnormaliz
Summary:        Normaliz internals as a library

%description -n libnormaliz
This package contains the normaliz internals as a library, often called
libnormaliz.

%package -n libnormaliz-devel
Summary:        Developer files for libnormaliz
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
Requires:       e-antic-devel%{?_isa}
Requires:       flint-devel%{?_isa}
Requires:       gmp-devel%{?_isa}

%description -n libnormaliz-devel
Header files and library links to develop applications that use the
Normaliz internals as a library (libnormaliz).

%prep
%autosetup -p0 -n Normaliz-%{version}

# Use our compiler flags
sed -i 's|-O3 -funroll-loops|%{optflags} -I%{_includedir}/gfanlib|' \
    source/Makefile.configuration

# Fix the date in the 3.8.9 changelog
sed -i 's/2030/2020/' CHANGELOG

# Generate configure
autoreconf -fi .

%build
export CPPFLAGS="-I%{_includedir}/arb -I%{_includedir}/gfanlib"
%configure \
  --disable-silent-rules \
  --disable-static \
  --with-cocoalib=%{_prefix}

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build
mkdir -p docs/example

# Correct the end of line encodings for use on Linux
pushd example
for file in *.in
do
    sed 's/\r//' "$file" > "../docs/example/$file"
    touch -r "$file" "../docs/example/$file"
done
popd

# Generate the man page
export LD_LIBRARY_PATH=$PWD/source/.libs
help2man -s 1 -o normaliz.1 -N source/.libs/normaliz

%install
# Install the library, binary, and headers
%make_install
rm -f %{buildroot}%{_libdir}/*.la

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
cp -p normaliz.1 %{buildroot}%{_mandir}/man1

%check
# Some tests fail on 32-bit architectures
%ifnarch %{arm} %{ix86}
LD_LIBRARY_PATH=$PWD/source/.libs make check
%endif

%files
%doc CHANGELOG docs/* doc/Normaliz.pdf
%{_bindir}/normaliz
%{_mandir}/man1/normaliz.1*

%files -n libnormaliz
%license COPYING
%{_libdir}/libnormaliz.so.3
%{_libdir}/libnormaliz.so.3.*

%files -n libnormaliz-devel
%doc source/libnormaliz/README
%{_libdir}/libnormaliz.so
%{_includedir}/libnormaliz/

%changelog
* Wed Sep 30 2020 Jerry James <loganjerry@gmail.com> - 3.8.9-1
- Version 3.8.9

* Sat Aug 29 2020 Jerry James <loganjerry@gmail.com> - 3.8.8-1
- Version 3.8.8

* Fri Aug  7 2020 Jerry James <loganjerry@gmail.com> - 3.8.7-1
- Version 3.8.7

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul  8 2020 Jerry James <loganjerry@gmail.com> - 3.8.6-1
- Version 3.8.6

* Tue Jun  2 2020 Jerry James <loganjerry@gmail.com> - 3.8.4-3
- Rebuild for nauty 2.7.1

* Fri Mar 20 2020 Jerry James <loganjerry@gmail.com> - 3.8.4-2
- Rebuild for cocoalib 0.99700

* Wed Mar  4 2020 Jerry James <loganjerry@gmail.com> - 3.8.4-1
- Version 3.8.4

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 27 2019 Jerry James <loganjerry@gmail.com> - 3.8.3-1
- Version 3.8.3
- Drop upstreamed -seqpoint patch
- Add -cocoalib patch for CoCoAlib 0.99650

* Wed Nov  6 2019 Jerry James <loganjerry@gmail.com> - 3.8.1-1
- Version 3.8.1
- Drop upstreamed -codimension patch
- Add a man page for the binary
- Add %%check script

* Fri Sep 27 2019 Jerry James <loganjerry@gmail.com> - 3.8.0-2
- Add -codimension patch from upstream

* Tue Sep 24 2019 Jerry James <loganjerry@gmail.com> - 3.8.0-1
- New upstream release
- Add -seqpoint patch

* Sat Aug 24 2019 Jerry James <loganjerry@gmail.com> - 3.7.4-3
- Add output.h to -devel package, accidentally omitted by upstream

* Wed Aug 21 2019 Jerry James <loganjerry@gmail.com> - 3.7.4-2
- Add missing Requires to the -devel subpackage

* Fri Aug  2 2019 Jerry James <loganjerry@gmail.com> - 3.7.4-1
- New upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Jerry James <loganjerry@gmail.com> - 3.7.3-1
- New upstream release
- Build with nauty support

* Thu May  9 2019 Jerry James <loganjerry@gmail.com> - 3.7.2-1
- New upstream release
- Drop upstreamed -cocoa patch
- Upstream dropped cmake support, so go back to autotools

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 13 2018 Jerry James <loganjerry@gmail.com> - 3.6.3-1
- New upstream release

* Fri Aug 10 2018 Jerry James <loganjerry@gmail.com> - 3.6.2-1
- New upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul  3 2018 Jerry James <loganjerry@gmail.com> - 3.5.4-2
- Rebuild with cocoalib support

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 3.5.4-1
- New upstream release
- Build with flint support
- Drop upstreamed -long-long and -rethrow patches

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 27 2017 Jerry James <loganjerry@gmail.com> - 3.4.0-1
- New upstream release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Wed Apr  5 2017 Jerry James <loganjerry@gmail.com> - 3.1.4-1
- New upstream release
- jnormaliz is now a separate project

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Jonathan Wakely <jwakely@redhat.com> - 2.12.2-9
- Rebuilt for Boost 1.63 and patched for GCC 7 (#1417678)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2.12.2-7
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.2-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 2.12.2-5
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.12.2-3
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 04 2015 Petr Machata <pmachata@redhat.com> - 2.12.2-2
- Bump for rebuild.

* Mon Feb  2 2015 Jerry James <loganjerry@gmail.com> - 2.12.2-1
- New upstream release

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 2.12.1-2
- Rebuild for boost 1.57.0

* Mon Nov 10 2014 Jerry James <loganjerry@gmail.com> - 2.12.1-1
- New upstream release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug  5 2014 Jerry James <loganjerry@gmail.com> - 2.11.2-1
- New upstream release
- Build now uses cmake
- Drop upstreamed patch
- Fix license handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 2.10.1-3
- Rebuild for boost 1.55.0

* Wed Jan 15 2014 Jerry James <loganjerry@gmail.com> - 2.10.1-2
- Fix thinko in -devel dependencies

* Tue Jan 14 2014 Jerry James <loganjerry@gmail.com> - 2.10.1-1
- New upstream release
- Package libnormaliz and jNormaliz separately

* Wed Aug 21 2013 Ville Skyttä <ville.skytta@iki.fi> - 2.7-8
- Adjust for unversioned %%{_docdir_fmt} (#994006).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-7.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 2.7-6.2
- Rebuild for boost 1.54.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-5.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-4.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-3.2
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.7-1.2
- rebuild with new gmp without compat lib

* Wed Oct 12 2011 Peter Schiffer <pschiffe@redhat.com> - 2.7-1.1
- rebuild with new gmp

* Fri May 27 2011 Rex Dieter <rdieter@fedoraproject.org> 2.7-1
- 2.7

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 25 2010 Mark Chappell <tremble@fedoraproject.org> - 2.2-3
- Preserve timestamps on examples
- Ensure that the first command in install is to wipe the buildroot
- Tweak to description

* Thu Feb 25 2010 Mark Chappell <tremble@fedoraproject.org> - 2.2-2
- Move examples into a subdirectory
- Correct inconsistant use of macros
- Provide a reference to the documentation in the description

* Wed Feb 24 2010 Mark Chappell <tremble@fedoraproject.org> - 2.2-1
- Initial build
