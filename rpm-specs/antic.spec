Name:           antic
Version:        0.2.2
Release:        1%{?dist}
Summary:        Algebraic Number Theory In C

License:        LGPLv2+
URL:            https://github.com/wbhart/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  flint-devel
BuildRequires:  gmp-devel
BuildRequires:  gcc
BuildRequires:  pkgconfig(mpfr)

%description
Antic is an algebraic number theory library written in C.

%package        devel
Summary:        Development files for antic
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       flint-devel%{?_isa}
Requires:       gmp-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup

# Kill rpath
sed -i '/rpath/d' configure

# Fix end-of-line encodings
sed -i.orig 's/\r//' NEWS
touch -r NEWS.orig NEWS
rm NEWS.orig

%build
# This is NOT an autoconf-generated configure script.  Do NOT use %%configure.
./configure --prefix=%{_prefix} --disable-static CFLAGS="%{optflags}"
%make_build verbose LDFLAGS="$RPM_LD_FLAGS"

%install
%make_install LIBDIR=%{_lib}

%check
make check

%files
%doc AUTHORS NEWS README
%license LICENSE
%{_libdir}/libantic.so.0*

%files          devel
%{_includedir}/%{name}/
%{_libdir}/libantic.so

%changelog
* Mon Aug  3 2020 Jerry James <loganjerry@gmail.com> - 0.2.2-1
- Version 0.2.2

* Thu Jul 30 2020 Jerry James <loganjerry@gmail.com> - 0.2.1-1
- Initial RPM
