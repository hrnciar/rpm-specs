#Blaze is a header only library
%global debug_package %{nil}
Name:           blaze
Version:        3.7
Release:        1%{?dist}
Summary:        An high-performance C++ math library for dense and sparse arithmetic
License:        BSD
URL:            https://bitbucket.org/blaze-lib/blaze
Source0:        https://bitbucket.org/blaze-lib/blaze/downloads/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++ >= 4.9
BuildRequires: cmake
BuildRequires: openblas-devel
BuildRequires: lapack
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

Requires: lapack
Requires: openblas-devel
Requires: boost

%description devel
%{blaze_desc}

%prep
%setup -n %{name}-%{version} -q

%build
pushd blaze
%{cmake} -DLIB=%{_lib} %{?cmake_opts:%{cmake_opts}} ..
%make_build
popd

%install
pushd blaze
%make_install
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





