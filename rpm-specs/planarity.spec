Name:		planarity
Summary:	Implementations of several planarity-related graph algorithms
Version:	3.0.0.5
Release:	6%{?dist}
License:	BSD
URL:		https://github.com/graph-algorithms/edge-addition-planarity-suite
Source0:	%{url}/archive/Version_%{version}/%{name}-%{version}.tar.gz
# sagemath patches renamed with planarity- prefix
# https://github.com/graph-algorithms/edge-addition-planarity-suite/pull/3
Patch0:		%{name}-extern.patch

BuildRequires:	gcc
BuildRequires:	libtool

%description
This code project provides a library for implementing graph algorithms
as well as implementations of several planarity-related graph algorithms.
The origin of this project is the reference implementation for the Edge
Addition Planarity Algorithm, which is now the fastest and simplest
linear-time method for planar graph embedding and planarity obstruction
isolation (i.e. Kuratowski subgraph isolation).

The software in this code project provides a graph algorithm framework and
library, including an updated version of the edge addition combinatorial
planar graph embedder and planar obstruction isolator (i.e., a Kuratowski
subgraph isolator). This code project also includes several extensions
that implement planarity-related algorithms such as a planar graph drawing
algorithm, an outerplanar graph embedder and outerplanar obstruction
isolator, and a number of subgraph homeomorphism search algorithms.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
This package contains the header files and development documentation
for %{name}.

%prep
%autosetup -p0 -n edge-addition-%{name}-suite-Version_%{version}

# Use unix line endings in installed headers
for header in c/*.h; do
    sed -i.orig 's|\r$||g' $header
    # Preserve timestamps
    touch -r $header.orig $header
    rm $header.orig
done

# Generate the configure script
autoreconf -fi .

%build
%configure --enable-static=false

# Eliminate hardcoded rpaths, and workaround libtool moving all -Wl options
# after the libraries to be linked
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|-nostdlib|-Wl,--as-needed &|' \
    -i libtool

# Do not use hardcoded CFLAGS=-O3
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
make install DESTDIR="%{buildroot}"
rm %{buildroot}%{_libdir}/*.la

%files
%license LICENSE.TXT
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so.*

%files		devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so

%changelog
* Tue Feb 11 2020 Jerry James <loganjerry@gmail.com> - 3.0.0.5-6
- Apply the patch to fix FTBFS with gcc 10
- Update URLs

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov  8 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 3.0.0.5-1
- Update to version required by newer sagemath
- Remove no longer need source1 and source2
- Remove no longer need patch1 and patch2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov  4 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.2.0-1
- Initial planarity spec.
