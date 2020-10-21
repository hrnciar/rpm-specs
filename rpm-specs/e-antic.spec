Name:           e-antic
Version:        0.1.8
Release:        1%{?dist}
Summary:        Real Embedded Algebraic Number Theory In C

# See https://github.com/videlec/e-antic/issues/100
License:        LGPLv3+
URL:            https://github.com/videlec/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  antic-devel
BuildRequires:  arb-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool

%description
E-ANTIC is a C/C++ library to deal with real embedded number fields,
built on top of ANTIC.  Its aim is to have as fast as possible exact
arithmetic operations and comparisons.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       arb-devel%{?_isa}
Requires:       flint-devel%{?_isa}
Requires:       gmp-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup

# Replace an obsolete autoconf macro
sed -i 's/AC_PROG_LIBTOOL/LT_INIT/' configure.ac

# Create the configure script
autoreconf -fi .

%build
export CPPFLAGS="-I %{_includedir}/arb"
%configure --disable-silent-rules --disable-static --enable-openmp

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

%install
%make_install

# We do not want the libtool archives
rm %{buildroot}%{_libdir}/*.la

# Documentation is installed below
rm -fr %{buildroot}%{_docdir}

%check
LD_LIBRARY_PATH=$PWD/.libs make check

%files
%doc AUTHORS README poly_extra/doc/poly_extra.txt
%license COPYING COPYING.LESSER
%{_libdir}/libeantic.so.0*
%{_libdir}/libeanticxx.so.0*

%files          devel
%doc NEWS
%{_includedir}/%{name}/
%{_libdir}/libeantic.so
%{_libdir}/libeanticxx.so

%changelog
* Fri Aug  7 2020 Jerry James <loganjerry@gmail.com> - 0.1.8-1
- Initial RPM
