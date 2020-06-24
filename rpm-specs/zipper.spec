Name:           zipper
Summary:        C++ wrapper around minizip compression library
Version:        1.0.1
Release:        1%{?dist}
URL:            https://github.com/sebastiandev/zipper

## Source archive from github obtained by
## git clone --recursive https://github.com/sebastiandev/zipper.git
## git checkout e9f150516cb55d194b5e01d21a9527783e98311d (release 1.0.1)
## rm -rf zipper/.git*
## tar -czvf  zipper-1.0.1.tar.gz zipper
Source0:        https://github.com/sebastiandev/zipper/archive/zipper/%{name}-%{version}.tar.gz

# zlib and GPL+ (no version) licenses come from minizip/ source code
License:        MIT and zlib and GPL+

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: zlib-devel
Provides: bundled(minizip) = 1.2.8

%description
Zipper brings the power and simplicity of minizip to a more
object oriented/c++ user friendly library.
It was born out of the necessity of a compression library that would be
reliable, simple and flexible. 
By flexibility I mean supporting all kinds of inputs and outputs,
but specifically been able to compress into memory instead of been
restricted to file compression only, and using data from memory instead
of just files as well.

Features:
- Create zip in memory
- Allow files, vector and generic streams as input to zip
- File mappings for replacing strategies
  (overwrite if exists or use alternative name from mapping)
- Password protected zip
- Multi platform

%package devel
Summary: Development files of %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides header files, shared and static library files of %{name}.

%package static
Summary: Static library of %{name}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description static
This package provides static library file of %{name}.

%prep
%autosetup -n zipper

# Fix library destination
sed -e 's|DESTINATION lib|DESTINATION %{_lib}|g' -i CMakeLists.txt

# Fix permissions
find ./minizip/ -name '*.c' -exec chmod 0644 '{}' \;

%build
mkdir -p build && cd build
export CXXFLAGS="%{optflags}"
%cmake -Wno-cpp -Wno-dev \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DBUILD_SHARED_VERSION:BOOL=ON -DBUILD_STATIC_VERSION:BOOL=ON \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES -DCMAKE_SKIP_RPATH:BOOL=YES ..
%make_build

%install
export LIBDIR=%{_libdir}
%make_install -C build

%ldconfig_scriptlets

%check
make test -C build

%files
%doc README.md VERSION.txt
%license LICENSE.md
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_includedir}/zipper/

%files static
%{_libdir}/*-static.a

%changelog
* Sat May 09 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.0.1-1
- Release 1.0.1

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-7.20170831giteee877a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-6.20170831giteee877a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5.20170831giteee877a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4.20170831giteee877a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 03 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.9.1-3.20170831giteee877a
- Rebuild for batched updates

* Sun Apr 29 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.9.1-2.20170831giteee877a
- Specify bundled code's license and version

* Thu Apr 19 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.9.1-1.20170831giteee877a
- First package
