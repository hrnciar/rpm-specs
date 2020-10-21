%undefine __cmake_in_source_build
%global git_commit 925a709ba0c98d8c0beabd0e34477971946c10be
%global git_date 20140319

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

%if 0%{?fedora} >= 33
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

# git clone https://github.com/VMML/vmmlib.git
# cd %%{name}
# git archive --format=tar --prefix=%%{name}-%%{version}/ %%{git_commit} | \
# bzip2 > ../%%{name}-%%{version}-%%{git_suffix}.tar.bz2

Name:          vmmlib
Version:       1.6.2
Release:       14.%{git_suffix}%{?dist}
Summary:       A vector and matrix math library implemented using C++ templates
License:       BSD
#URL:           http://vmmlib.sourceforge.net/
URL:           http://github.com/VMML/vmmlib/
#Source0:       http://github.com/VMML/vmmlib/archive/release-%{version}.tar.gz#/%{name}-release-%{version}.tar.gz
Source0:       %{name}-%{version}-%{git_suffix}.tar.bz2
# BLAS/LAPACK tests are broken
Patch0:        0001-remove-lapack-tests.patch
BuildArch:     noarch
BuildRequires: %{blaslib}-devel, f2c, gcc-c++
BuildRequires: doxygen, cmake

%description
vmmlib is a vector and matrix math library implemented using C++ templates.
Its basic functionality includes a vector and a matrix class, with additional
functionality for the often-used 3d and 4d vectors and 3x3 and 4x4 matrices.
More advanced functionality include solvers, frustum computations and frustum
culling classes, and spatial data structures.

%package devel
Summary:       A vector and matrix math library implemented using C++ templates
Requires:      pkgconfig, cmake

%description devel
vmmlib is a vector and matrix math library implemented using C++ templates.
Its basic functionality includes a vector and a matrix class, with additional
functionality for the often-used 3d and 4d vectors and 3x3 and 4x4 matrices.
More advanced functionality include solvers, frustum computations and frustum
culling classes, and spatial data structures.

%prep
%autosetup -p1

%build
export CXXFLAGS="$CXXFLAGS -I%{_includedir}/%{blaslib}"
%cmake -DBLAS_FOUND=TRUE -DLAPACK_FOUND=TRUE -DBLAS_LIBRARIES=-l%{blaslib}
%cmake_build

%install
%cmake_install

# move docs to right place
mkdir _tmpdoc
mv %{buildroot}%{_datadir}/%{name}/{AUTHORS,LICENSE.txt,ACKNOWLEDGEMENTS,README.md} _tmpdoc/

# move cmake files to right place
mkdir -p %{buildroot}%{_datadir}/cmake/Modules/
mv %{buildroot}%{_datadir}/%{name}/CMake/*.cmake %{buildroot}%{_datadir}/cmake/Modules/
rmdir %{buildroot}%{_datadir}/%{name}/CMake

%check
export FLEXIBLAS=netlib
%ctest

%files devel
%doc RELNOTES.md CHANGES _tmpdoc/*
%{_includedir}/vmmlib
%{_libdir}/pkgconfig/vmmlib.pc
%{_datadir}/cmake/Modules/vmmlib*.cmake

%changelog
* Thu Aug 27 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.6.2-14.20140319git925a709b
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-13.20140319git925a709b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-12.20140319git925a709b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-11.20140319git925a709b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-10.20140319git925a709b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-9.20140319git925a709b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-8.20140319git925a709b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-7.20140319git925a709b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-6.20140319git925a709b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun  8 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 1.6.2-5.20140319git925a709b
- Fixed build requirements to require gcc-c++
  Resolves: rhbz#1230504

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-4.20140319git925a709b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-3.20140319git925a709b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-2.20140319git925a709b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 19 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.6.2-1.20140319git925a709b
- New version

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.6.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.5.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.4.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.3.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0-0.2.rc1
- Added dist tag to spec

* Tue Dec 20 2011 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0-0.1.rc1
- New version

* Tue Dec 13 2011 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.4.20111214svn558
- New svn snapshot that fixes cp3_tensor test

* Tue Dec 13 2011 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.3.20111214svn556
- New svn snapshot that fixes several problems in unit test

* Tue Dec 13 2011 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.2.20111122svn540
- Fixed unit test on 64 bit

* Tue Nov 22 2011 Jaroslav Škarvada <jskarvad@redhat.com> - 0-0.1.20111122svn540
- Initial release
