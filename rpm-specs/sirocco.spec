Name:           sirocco
Version:        2.0.2
Release:        1%{?dist}
Summary:        ROot Certified COntinuator

License:        GPLv2+
URL:            https://github.com/miguelmarco/SIROCCO2
Source0:        %{url}/releases/download/%{version}/lib%{name}-%{version}.tar.gz
# Fix some mixed signed/unsigned expressions
Patch0:         %{name}-signed.patch

BuildRequires:  gcc-c++
BuildRequires:  mpfr-devel

%description
This is a library for computing homotopy continuation of a given root of
one dimensional sections of bivariate complex polynomials.  The output
is a piecewise linear approximation of the path followed by the root,
with the property that there is a tubular neighborhood, with square
transversal section, that contains the actual path, and there is a three
times thicker tubular neighborhood guaranteed to contain no other root
of the polynomial.  This second property ensures that the piecewise
linear approximation computed from all roots of a polynomial form a
topologically correct deformation of the actual braid, since the inner
tubular neighborhoods cannot intersect.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p0 -n lib%{name}-%{version}

%build
export CFLAGS="%{optflags} -frounding-math"
export CXXFLAGS="%{optflags} -frounding-math"
%configure --disable-static --disable-silent-rules

# Work around libtool reordering -Wl,--as-needed after all the libraries.
sed -i 's|CC=.g..|& -Wl,--as-needed|' libtool

%make_build

%install
%make_install

# We do not want the libtool files
rm %{buildroot}%{_libdir}/*.la

%check
make check

%files
%license LICENSE
%doc README.md
%{_libdir}/libsirocco.so.0
%{_libdir}/libsirocco.so.0.*

%files devel
%{_includedir}/sirocco.h
%{_libdir}/libsirocco.so

%changelog
* Mon Feb 17 2020 Jerry James <loganjerry@gmail.com> - 2.0.2-1
- Version 2.0.2

* Tue Feb 11 2020 Jerry James <loganjerry@gmail.com> - 2.0.1-1
- Version 2.0.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct  9 2019 Jerry James <loganjerry@gmail.com> - 2.0-4
- Update to latest git snapshot

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 24 2018 Jerry James <loganjerry@gmail.com> - 2.0-1
- Initial RPM
