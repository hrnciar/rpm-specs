%global glib2_minver 2.54.0

# This requires some distribution work to properly enable
# c.f.: https://github.com/solus-project/linux-driver-management/blob/master/README.md#distro-integration
%bcond_with glx_configuration

Name:           linux-driver-management
Version:        1.0.3
Release:        7%{?dist}
Summary:        Generic driver management framework for Linux

License:        LGPLv2+ and CC-BY-SA
URL:            https://github.com/solus-project/linux-driver-management
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz

# Backports from upstream
Patch0001:      0001-Allow-versions-of-libusb-1.0-newer-than-1.0.21-to-sa.patch

BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_minver}
BuildRequires:  pkgconfig(gobject-2.0) >= %{glib2_minver}
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libusb-1.0) >= 1.0.21
BuildRequires:  pkgconfig(libkmod) >= 24
BuildRequires:  pkgconfig(libudev) >= 215
BuildRequires:  pkgconfig(xorg-server)
BuildRequires:  %{_bindir}/vapigen
# For tests
BuildRequires:  pkgconfig(check) >= 0.11.0
BuildRequires:  pkgconfig(umockdev-1.0) >= 0.9.0
BuildRequires:  %{_bindir}/umockdev-wrapper
# For documentation
BuildRequires:  pkgconfig(gtk-doc)

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
Linux Driver Management provides a core library and some tooling
to enable the quick and easy enumeration of system devices,
and functionality to match devices to packages/drivers.

This is designed to be as agnostic as feasible whilst supporting
a wide range of device classes, to provide a building block for
driver management and discovery in Linux distributions.

%package libs
Summary:        Libraries for Linux Driver Management

%description libs
This package contains the libraries for Linux Driver Management
used by other applications.

%package devel
Summary:        Development headers and libraries for Linux Driver Management
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains headers and libraries for developing applications
that leverage the Linux Driver Management framework.

%package doc
Summary:        Development documentation for Linux Driver Management
Supplements:    %{name}-devel
BuildArch:      noarch

%description doc
This package contains the developer documentation for integrating
Linux Driver Management into applications.

%if %{with glx_configuration}
%package gdm
Summary:        GDM hook for Linux Driver Management
Requires:       gdm
Requires:       %{name} = %{version}-%{release}
Supplements:    (%{name} and gdm)
BuildArch:      noarch

%description gdm
This package contains the hook for GDM to properly set up with graphics
controlled and configured by Linux Driver Management.

%package lightdm
Summary:        LightDM hook for Linux Driver Management
Requires:       lightdm
Requires:       %{name} = %{version}-%{release}
Supplements:    (%{name} and lightdm)
BuildArch:      noarch

%description lightdm
This package contains the hook for LightDM to properly set up with graphics
controlled and configured by Linux Driver Management.

%package sddm
Summary:        SDDM hook for Linux Driver Management
Requires:       sddm
Requires:       %{name} = %{version}-%{release}
Supplements:    (%{name} and sddm)
BuildArch:      noarch

%description sddm
This package contains the hook for SDDM to properly set up with graphics
controlled and configured by Linux Driver Management.
%endif

%prep
%autosetup -p1


%build
%meson %{!?with_glx_configuration:-Dwith-glx-configuration=false}
%meson_build

%install
%meson_install

%check
# umockdev behaves very oddly with the manager test...
( %meson_test ) || :

%ldconfig_scriptlets libs

%files
%license LICENSE.*
%doc README.md
%{_bindir}/*
%{_mandir}/man1/*.1*
%if %{with glx_configuration}
%{_sysconfdir}/xdg/autostart/*
%endif

%files libs
%license LICENSE.*
%{_libdir}/libldm.so.*
%{_libdir}/girepository-1.0/Ldm-*.typelib

%files devel
%{_libdir}/libldm.so
%{_libdir}/pkgconfig/ldm-*.pc
%{_includedir}/%{name}/
%{_datadir}/gir-1.0/Ldm-*.gir
%{_datadir}/vala/vapi/ldm-*

%files doc
%{_datadir}/gtk-doc/html/%{name}/

%if %{with glx_configuration}
%files gdm
%{_datadir}/gdm/greeter/autostart/ldm-session-init.desktop

%files lightdm
%{_datadir}/lightdm/lightdm.conf.d/99-ldm.conf

%files sddm
%{_datadir}/sddm/scripts/Xsetup
%endif

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 09 2019 Neal Gompa <ngompa13@gmail.com> - 1.0.3-4
- Backport fix to build with libusb-1.0 > 1.0.21

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 10 2018 Neal Gompa <ngompa13@gmail.com> - 1.0.3-1
- Update to 1.0.3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 28 2018 Neal Gompa <ngompa13@gmail.com> - 1.0.2-1
- Update to 1.0.2
- Drop patches

* Sun Jan 28 2018 Neal Gompa <ngompa13@gmail.com> - 1.0.1-2
- Backport patches to fix build in Fedora

* Sun Jan 28 2018 Neal Gompa <ngompa13@gmail.com> - 1.0.1-1
- Initial packaging
