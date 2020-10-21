Name:           xeus
Version:        0.24.2
Release:        1%{?dist}
Summary:        C++ implementation of the Jupyter kernel protocol

License:        BSD
URL:            https://github.com/jupyter-xeus/xeus
Source0:        https://github.com/jupyter-xeus/xeus/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.8
BuildRequires:  cmake(cppzmq) >= 4.3.0
BuildRequires:  cmake(nlohmann_json) >= 3.2.0
BuildRequires:  cmake(xtl) >= 0.5
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  libuuid-devel
BuildRequires:  openssl-devel >= 1.0.1
BuildRequires:  pkgconfig(libzmq) >= 4.2.5
BuildRequires:  python3dist(breathe)
BuildRequires:  python3dist(jupyter-kernel-test)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description
xeus is a library meant to facilitate the implementation of kernels for
Jupyter. It takes the burden of implementing the Jupyter Kernel protocol so
developers can focus on implementing the interpreter part of the kernel.


%package devel
Summary:        %{summary}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name} library.


%prep
%autosetup -p1


%build
%cmake -DXEUS_BUILD_STATIC_LIBS=OFF -DXEUS_DISABLE_ARCH_NATIVE=ON
%cmake_build

make -C docs SPHINXBUILD=sphinx-build-3 html
rm docs/build/html/.buildinfo


%install
%cmake_install


%check
%ctest


%files
%doc README.md docs/build/html
%license LICENSE
%{_libdir}/libxeus.so.1*

%files devel
%{_includedir}/xeus/
%{_libdir}/cmake/xeus/
%{_libdir}/libxeus.so


%changelog
* Tue Oct 06 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.24.2-1
- Update to latest version (#1884918)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.24.1-1
- Update to latest version

* Sat Jun 13 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.24.0-1
- Update to latest version

* Mon May 18 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.23.14-1
- Update to latest version

* Wed Mar 25 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.23.9-1
- Update to latest version

* Sat Mar 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.23.8-1
- Update to latest version

* Tue Mar 03 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.23.6-1
- Update to latest version

* Fri Feb 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.23.5-1
- Update to latest version
- Re-enable build on armv7hl and ppc64le

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.23.3-1
- Update to latest version

* Tue Sep 24 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.23.2-2
- rebuilt

* Mon Sep 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.23.2-1
- Update to latest version

* Sat Sep 07 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.23.1-1
- Initial package release
