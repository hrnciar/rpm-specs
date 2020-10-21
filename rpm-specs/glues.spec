%undefine __cmake_in_source_build
%global commit0 44cb7c6eae4488f921041572908f3af508880547

Name:           glues
Version:        1.5
Release:        3.20200105git44cb7c6%{?dist}
Summary:        GLU port for OpenGL ES

# SGI FREE SOFTWARE LICENSE B (Version 2.0, Sept. 18, 2008)
License:        MIT
URL:            https://github.com/lunixbochs/%{name}
Source0:        %{url}/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz

BuildRequires:  cmake gcc-c++
# TODO check compatibility for SDL 1.2+ currently in rawhide
BuildRequires:  SDL2-devel
BuildRequires:  mesa-libGL-devel


%description
This port is based on original GLU 1.3 and has original libutil, libtess and
nurbs libraries.


%package devel
Summary:        Development files for GLUES
Requires:       %{name}%{?_isa} = %{version}

%description devel
%summary.


%prep
%autosetup -n%{name}-%{commit0}
# rename so to avoid conflicts
sed -i 's,GLU ,GLUES ,' CMakeLists.txt
# skip nurbs
find source/libnurbs -type d -print -exec rm -rv '{}/*' \;


%build
%cmake
%cmake_build


%install
mkdir -p %{buildroot}%{_libdir}
install -p %{_vpath_builddir}/libGLUES.so* %{buildroot}%{_libdir}
ln -s libGLUES.so.* %{buildroot}%{_libdir}/libGLUES.so
mkdir -p %{buildroot}%{_includedir}/%{name}
cp -pr source/*.h %{buildroot}%{_includedir}/%{name}

%files
%license LICENSE
%doc README docs/*
%{_libdir}/lib*.so.1

%files devel
%license LICENSE
%doc sdltests/
%{_libdir}/libGLUES.so
%{_includedir}/%{name}/


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3.20200105git44cb7c6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2.20200105git44cb7c6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jan 05 2020 Raphael Groner <projects.rg@smart.ms> - 1.5-1.20200105git44cb7c6
- initial


