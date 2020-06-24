%global upstream_version 3_4_0

Name:           opensubdiv
Version:        3.4.0
Release:        4%{?dist}
Summary:        An Open-Source subdivision surface library

License:        ASL 2.0
URL:            http://graphics.pixar.com/%{name}
Source0:        https://github.com/PixarAnimationStudios/OpenSubdiv/archive/v%{upstream_version}.tar.gz#/%{name}-%{version}.tar.gz/%{name}-%{version}.tar.gz
Patch0:         %{name}-rpath.patch


BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  glfw-devel
BuildRequires:  graphviz-devel
BuildRequires:  opencl-headers
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:	python3-docutils
BuildRequires:  tbb-devel


%description
OpenSubdiv is a set of open source libraries that implement high performance
subdivision surface (subdiv) evaluation on massively parallel CPU and
GPU architectures. 
This codepath is optimized for drawing deforming subdivs with static topology
at interactive framerates.

%package        libs
Summary:        Core OpenSubdiv libraries
Requires:       %{name}%{?_isa} = %{version}-%{release} 
%description    libs
%{summary}


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n OpenSubdiv-%{upstream_version}

%build
mkdir cmake-build
pushd cmake-build

%cmake \
       -DCMAKE_BUILD_TYPE=Release \
       -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DCMAKE_LIBDIR_BASE=%{_libdir} \
       -DGLEW_LOCATION=%{_libdir} \
       -DGLFW_LOCATION=%{_libdir} \
       -DNO_CUDA=1 \
       -DNO_GLFW_X11=1 // disable X11 dependencies\
       -DNO_PTEX=1 \
       -DOPENCL_INCLUDE_DIRS=%{_includedir} \
       -DOpenGL_GL_PREFERENCE=GLVND \
       -DTBB_LOCATION=%{_libdir} \
     ..
%make_build

popd

%{?_with_tests:
%check
pushd cmake-build
make test V=1
popd
}

%install
pushd cmake-build
%make_install

# Let rpmbuild pick up documentation
mv %{buildroot}%{_docdir}/%{name} docs

# Move tutorials out of subdirectory
mv %{buildroot}%{_bindir}/tutorials/* %{buildroot}%{_bindir}/
rm -fr %{buildroot}%{_bindir}/tutorials

# Remove static files
find %{buildroot} -name '*.la' -delete
find %{buildroot} -name '*.a' -delete

popd

%files
%{_bindir}/far_perf
%{_bindir}/far_regression
%{_bindir}/hbr_baseline
%{_bindir}/hbr_regression
%{_bindir}/osd_regression
%{_bindir}/stringify

%files libs
%license LICENSE.txt
%doc README.md
%{_libdir}/*.so.%{version}

%files devel
%doc NOTICE.txt cmake-build/docs/*
%{_bindir}/farViewer
%{_bindir}/glEvalLimit
%{_bindir}/glFVarViewer
%{_bindir}/glImaging
%{_bindir}/glPaintTest
%{_bindir}/glShareTopology
%{_bindir}/glStencilViewer
%{_bindir}/glViewer
%{_bindir}/far_tutorial*
%{_bindir}/hbr_tutorial*
%{_bindir}/osd_tutorial*
%{_includedir}/*
%{_libdir}/*.so

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 14 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 3.4.0-3
- Remove rpath
- Remove unneeded ldconfig_scriptlets macro
- Improve spec file upon review (rhbz #1762155)

* Mon Oct 14 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 3.4.0-2
- Adjust maximum line limit on description

* Mon Oct 14 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 3.4.0-1
- Initial package
