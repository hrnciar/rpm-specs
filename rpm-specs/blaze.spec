#Blaze is a header only library
%global debug_package %{nil}

Name:           blaze
Version:        3.8
Release:        2%{?dist}
Summary:        An high-performance C++ math library for dense and sparse arithmetic
License:        BSD
URL:            https://bitbucket.org/blaze-lib/blaze
Source0:        https://bitbucket.org/blaze-lib/blaze/downloads/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++ >= 4.9
BuildRequires: cmake
BuildRequires: flexiblas-devel
BuildRequires: boost-devel

%global blaze_desc \
Blaze is an open-source, high-performance C++ math library for dense and \
sparse arithmetic. With its state-of-the-art Smart Expression Template \
implementation Blaze combines the elegance and ease of use of a \
domain-specific language with HPC-grade performance, making it one of \
the most intuitive and fastest C++ math libraries available. \

%description 
%{blaze_desc}


%package devel
Summary:    Development headers for BLAZE
Provides:   blaze-static = %{version}-%{release}

Requires: flexiblas-devel
Requires: boost

%description devel
%{blaze_desc}

%prep
%setup -n %{name}-%{version} -q

%build
pushd blaze
%{cmake} -DLIB=%{_lib} -DBLAS_LIBRARIES=-lflexiblas %{?cmake_opts:%{cmake_opts}} ..
cd %{__cmake_builddir}
%make_build
cd ..
popd

%install
pushd blaze
cd %{__cmake_builddir}
%make_install
cd ..
popd
rm -rf %{_includedir}/%{name}/CMakeFiles/3.12.2
rm -rf %{_includedir}/%{name}/CMakeFiles/FindOpenMP


%files devel
%doc INSTALL
%license LICENSE
%{_includedir}/%{name}
%{_datadir}/%{name}/cmake/*.cmake
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/cmake

%changelog
* Thu Aug 27 2020 Iñaki Úcar <iucar@fedoraproject.org> - 3.8-2
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager
* Sat Aug 15  2020 Patrick Diehl  <patrickdiehl@lsu.edu> - 3.8-1
- Update to Blaze 3.8
* Mon Jul 27 2020 Patrick Diehl  <patrickdiehl@lsu.edu> - 3.7-3
- CMake fixes
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
* Mon Feb 24 2020 Patrick Diehl <patrickdiehl@lsu.edu> - 3.7.1
- Initial Release of blaze 3.7
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-1
- Initial Release of blaze 3.6
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
* Wed Feb 27 2019 Patrick Diehl <patrickdiehl@lsu.edu> - 3.5-1
- Initial Release of blaze 3.5
* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
* Thu Nov 22 2018 Patrick Diehl <patrickdiehl@lsu.edu> - 3.4-1
- Initial Release of blaze 3.4





