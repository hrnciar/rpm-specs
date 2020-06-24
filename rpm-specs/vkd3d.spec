Name:		vkd3d
Version:	1.1
Release:	4%{?dist}
Summary:	D3D12 to Vulkan translation library

License:	LGPLv2+
URL:		https://source.winehq.org/git/vkd3d.git
Source0:	https://dl.winehq.org/vkd3d/source/%{name}-%{version}.tar.xz
Source1:	https://dl.winehq.org/vkd3d/source/%{name}-%{version}.tar.xz.sign

BuildRequires:	gcc
BuildRequires:	libxcb-devel
BuildRequires:	spirv-headers-devel
BuildRequires:	spirv-tools-devel
BuildRequires:	vulkan-loader-devel
BuildRequires:	xcb-util-devel
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xcb-util-wm-devel

# Wine does not build on aarch64 due to clang requires
# vulkan is not available in RHEL 7+ for aarch64 either
%if 0%{?rhel} >= 7
ExclusiveArch:  %{ix86} x86_64 %{arm}
%else
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64
%endif

%description
The vkd3d project includes libraries, shaders, utilities, and demos for
translating D3D12 to Vulkan.


%package -n libvkd3d
Summary:	D3D12 to Vulkan translation library


%description -n libvkd3d
libvkd3d is the main component of the vkd3d project. It's a 3D graphics
library built on top of Vulkan with an API very similar to Direct3D 12.


%package -n libvkd3d-devel
Summary:	Development files for vkd3d
Requires:	libvkd3d%{?_isa} = %{version}-%{release}


%description -n libvkd3d-devel
Development files for vkd3d


%package -n libvkd3d-utils
Summary:	Utility library for vkd3d


%description -n libvkd3d-utils
libvkd3d-utils contains simple implementations of various functions which
might be useful for source ports of Direct3D 12 applications.


%package -n libvkd3d-utils-devel
Summary:	Development files for libvkd3d-utils
Requires:	libvkd3d-devel%{?_isa} = %{version}-%{release}
Requires:	libvkd3d-utils%{?_isa} = %{version}-%{release}


%description -n libvkd3d-utils-devel
Development files for libvkd3d-utils


%prep
%setup -q


%build
%configure --with-spirv-tools
%make_build


%install
%make_install

#Remove libtool files and static libraries
find %{buildroot} -regextype egrep -regex '.*\.a$|.*\.la$' -delete


%files -n libvkd3d
%doc AUTHORS INSTALL README
%license COPYING LICENSE
%{_libdir}/libvkd3d.so.1
%{_libdir}/libvkd3d.so.1.*


%files -n libvkd3d-devel
%dir %{_includedir}/vkd3d
%{_includedir}/vkd3d/vkd3d_d3d12.h
%{_includedir}/vkd3d/vkd3d_d3dcommon.h
%{_includedir}/vkd3d/vkd3d_dxgibase.h
%{_includedir}/vkd3d/vkd3d_dxgiformat.h
%{_includedir}/vkd3d/vkd3d.h
%{_includedir}/vkd3d/vkd3d_windows.h
%{_libdir}/libvkd3d.so
%{_libdir}/pkgconfig/libvkd3d.pc


%files -n libvkd3d-utils
%{_libdir}/libvkd3d-utils.so.1
%{_libdir}/libvkd3d-utils.so.1.*


%files -n libvkd3d-utils-devel
%{_includedir}/vkd3d/vkd3d_utils.h
%{_libdir}/libvkd3d-utils.so
%{_libdir}/pkgconfig/libvkd3d-utils.pc


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 - Michael Cronenworth <mike@cchtml.com> - 1.1-1
- version update

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 - Michael Cronenworth <mike@cchtml.com> - 1.0-1
- Initial release

