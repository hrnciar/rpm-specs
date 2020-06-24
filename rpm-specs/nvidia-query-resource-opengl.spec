# This project doesn't work with hardened as it relies on lazzy symbol resolution
# like others Xorg modules
%undefine _hardened_build

Name:           nvidia-query-resource-opengl
Version:        1.0.0
Release:        7%{?dist}
Summary:        Querying OpenGL resource usage of applications using the NVIDIA OpenGL driver

License:        BSD
URL:            https://github.com/NVIDIA/nvidia-query-resource-opengl/
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  libX11-devel
BuildRequires:  libGL-devel

Requires:       %{name}-lib%{?_isa} = %{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} > 7
%ifarch x86_64
Suggests:       (%{name}-libs(x86-32) = %{?epoch}:%{version}-%{release} if libGL(x86-32))
%endif
%endif


%description
A tool for querying OpenGL resource usage of applications using the NVIDIA
OpenGL driver. Requires NVIDIA 387 or later.

%package        lib
Summary:        Library for %{name}

%description    lib
This package contains library for %{name}.


%prep
%autosetup


%build
mkdir -p build
cd build
%cmake \
 ..

%make_build


%install
cd build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/%{name}

install -pm 0755 %{name} \
  %{buildroot}%{_bindir}

install -pm 0755 libnvidia-query-resource-opengl-preload.so \
  %{buildroot}%{_libdir}/%{name}/lib%{name}-preload.so


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%files lib
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/lib%{name}-preload.so


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 15 2017 Nicolas Chauvet <kwizart@gmail.com> - 1.0.0-2
- Add missing BR
- Improve description

* Wed Sep 13 2017 Nicolas Chauvet <kwizart@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Mon Apr 10 2017 Nicolas Chauvet <kwizart@gmail.com> - 0.0.0-1
- Initial spec file
