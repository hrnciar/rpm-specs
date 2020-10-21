Name:		brial
Version:	1.2.10
Release:	1%{?dist}
Summary:	Framework for Boolean Rings
# The entire source code is GPLv2+ except the Cudd directory that is BSD
License:	GPLv2+ and BSD
URL:		https://github.com/BRiAl/BRiAl/
Source0:	https://github.com/BRiAl/BRiAl/releases/download/%{version}/%{name}-%{version}.tar.bz2
# The clock function has been removed from python 3.8.  See
# https://github.com/BRiAl/BRiAl/commit/74d861705c77c3af7e6a2e49dd57f8d26a664072
Patch0:		%{name}-clock.patch
# cudd/cudd.h:#define CUDD_VERSION "2.5.0"
Provides:	bundled(cudd) = 2.5.0
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(gdlib)
BuildRequires:	pkgconfig(m4ri)
BuildRequires:	python3-devel

%description
The core of BRiAl is a C++ library, which provides high-level data
types for Boolean polynomials and monomials, exponent vectors, as well
as for the underlying polynomial rings and subsets of the powerset of
the Boolean variables. As a unique approach, binary decision diagrams
are used as internal storage type for polynomial structures. On top of
this C++-library we provide a Python interface. This allows parsing of
complex polynomial systems, as well as sophisticated and extendable
strategies for Gröbner base computation. BRiAL features a powerful
reference implementation for Gröbner basis computation.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	boost-devel%{?_isa}

%description	devel
Development headers and libraries for %{name}.

%package	-n python3-%{name}
Summary:	Python 3 interface to %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	-n python3-%{name}
Python 3 interface to %{name}.

%prep
%autosetup -p1

%build
export CPPFLAGS="-DPBORI_NDEBUG"
%configure --enable-shared --disable-static
# Get rid of undesirable hardcoded rpaths, and workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

# Make the python interfaces
pushd sage-brial
%py3_build
popd

%install
%make_install
rm %{buildroot}%{_libdir}/*.la

# Install the python interfaces
pushd sage-brial
%py3_install
popd

%check
export LD_LIBRARY_PATH=$PWD/.libs:$PWD/groebner/src/.libs
make check

%files
%doc README
%license LICENSE
%{_libdir}/lib%{name}*.so.*

%files devel
%{_includedir}/polybori.h
%{_includedir}/polybori/
%{_libdir}/lib%{name}*.so

%files -n python3-%{name}
%doc sage-brial/README.md
%{python3_sitelib}/%{name}*

%changelog
* Mon Oct  5 2020 Jerry James <loganjerry@gmail.com> - 1.2.10-1
- Version 1.2.10

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.8-2
- Rebuilt for Python 3.9

* Thu Mar 19 2020 Jerry James <loganjerry@gmail.com> - 1.2.8-1
- Version 1.2.8

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Jerry James <loganjerry@gmail.com> - 1.2.7-1
- Version 1.2.7

* Thu Jan 16 2020 Jerry James <loganjerry@gmail.com> - 1.2.6-1
- Version 1.2.6

* Wed Sep 11 2019 Jerry James <loganjerry@gmail.com> - 1.2.5-4
- Add -clock patch to fix runtime failure with python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.5-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Jerry James <loganjerry@gmail.com> - 1.2.5-1
- New upstream version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.4-2
- Subpackage python2-brial has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Sep 13 2018 Jerry James <loganjerry@gmail.com> - 1.2.4-1
- New upstream version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.3-2
- Rebuilt for Python 3.7

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 1.2.3-1
- New upstream version (bz 1438103)
- Build for both python 2 and 3
- Add a check script

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8.5-9
- Python 2 binary package renamed to python2-brial
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 18 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> 0.8.5-4
- Add Provides/Obsoletes to remaining polybori packages (#1367526#c6)

* Wed Aug 17 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> 0.8.5-3
- Correct summary to talk about BRiAl and not PolyBori (#1367526#c4)

* Tue Aug 16 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> 0.8.5-2
- Correct setting of CXXFLAGS (#1367526#c2)
- Add proper multiple license information (#1367526#c2)
- Add Provides/Obsoletes to devel package (#1367526#c2)
- Remove unused shared library dependencies (#1367526#c2)
- Add version information to bundled Cudd (#1367526#c2)
- Change to a more informational summary (#1367526#c2)

* Wed Aug 10 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> 0.8.5-1
- Initial brial spec file
