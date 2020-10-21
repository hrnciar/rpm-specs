%global debug_package %{nil}

%ifarch x86_64
%global platform_identificator x86_64-redhat-linux-gnu
%global target_x86_type 64
%else
%global platform_identificator i686-redhat-linux-gnu
%global target_x86_type 32
%endif

Name:           wine-dxvk
Version:        1.7.2
Release:        1%{?dist}
Summary:        Vulkan-based D3D11 and D3D10 implementation for Linux / Wine

License:        zlib
URL:            https://github.com/doitsujin/dxvk
Source0:        %{url}/archive/v%{version}/dxvk-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glslang
BuildRequires:  meson
BuildRequires:  wine-devel

%ifarch x86_64
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-headers
BuildRequires:  mingw64-cpp
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-winpthreads-static
%else
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-headers
BuildRequires:  mingw32-cpp
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-winpthreads-static
%endif

Requires(pre):  vulkan-tools

Requires:       wine-core >= 4.13
Recommends:     wine-dxvk-dxgi%{?_isa} = %{version}-%{release}
Requires:       vulkan-loader%{?_isa}

# We want x86_64 users to always have also 32 bit lib, it's the same what wine does
%ifarch x86_64
Requires:       wine-dxvk(x86-32) = %{version}-%{release}
%endif

# Recommend also the d3d9 (former D9VK)
Recommends:     wine-dxvk-d3d9%{?_isa} = %{version}-%{release}

Requires(posttrans):   %{_sbindir}/alternatives
Requires(preun):       %{_sbindir}/alternatives

ExclusiveArch:  %{ix86} x86_64

%description
%{summary}

%package dxgi
Summary:        DXVK DXGI implementation
%ifarch x86_64
Requires:       wine-dxvk-dxgi(x86-32) = %{version}-%{release}
%endif

%description dxgi
%{summary}

This package doesn't enable the use of this DXGI implementation,
it should be installed and overridden per prefix.

%package d3d9
Summary:        DXVK D3D9 implementation

Requires:       wine-dxvk%{?_isa} = %{version}-%{release}

# We want x86_64 users to always have also 32 bit lib, it's the same what wine does
%ifarch x86_64
Requires:       wine-dxvk-d3d9(x86-32) = %{version}-%{release}
%endif

%description d3d9
%{summary}

%prep
%setup -q -n dxvk-%{version}

%build
/usr/bin/meson --buildtype=plain --wrap-mode=nodownload --auto-features=enabled . %{platform_identificator} \
--cross-file build-win%{target_x86_type}.txt --buildtype release --prefix /builddir/build/BUILD/dxvk-%{version}/build
%meson_build

%install
%meson_install
#winebuild --builtin %%buildroot/builddir/build/BUILD/dxvk-%%{version}/build/bin/dxgi.dll
winebuild --builtin %buildroot/builddir/build/BUILD/dxvk-%{version}/build/bin/d3d9.dll
winebuild --builtin %buildroot/builddir/build/BUILD/dxvk-%{version}/build/bin/d3d10.dll
winebuild --builtin %buildroot/builddir/build/BUILD/dxvk-%{version}/build/bin/d3d10core.dll
winebuild --builtin %buildroot/builddir/build/BUILD/dxvk-%{version}/build/bin/d3d10_1.dll
winebuild --builtin %buildroot/builddir/build/BUILD/dxvk-%{version}/build/bin/d3d11.dll

mkdir -p %{buildroot}%{_libdir}/wine/
install -p -m 644 %buildroot/builddir/build/BUILD/dxvk-%{version}/build/bin/dxgi.dll %{buildroot}%{_libdir}/wine/
install -p -m 644 %buildroot/builddir/build/BUILD/dxvk-%{version}/build/bin/d3d9.dll %{buildroot}%{_libdir}/wine/
install -p -m 644 %buildroot/builddir/build/BUILD/dxvk-%{version}/build/bin/d3d10.dll %{buildroot}%{_libdir}/wine/
install -p -m 644 %buildroot/builddir/build/BUILD/dxvk-%{version}/build/bin/d3d10core.dll %{buildroot}%{_libdir}/wine/
install -p -m 644 %buildroot/builddir/build/BUILD/dxvk-%{version}/build/bin/d3d10_1.dll %{buildroot}%{_libdir}/wine/
install -p -m 644 %buildroot/builddir/build/BUILD/dxvk-%{version}/build/bin/d3d11.dll %{buildroot}%{_libdir}/wine/
rm -rf %buildroot/builddir/build/BUILD/dxvk-%{version}/build

mv %{buildroot}%{_libdir}/wine/dxgi.dll %{buildroot}%{_libdir}/wine/dxvk-dxgi.dll
mv %{buildroot}%{_libdir}/wine/d3d9.dll %{buildroot}%{_libdir}/wine/dxvk-d3d9.dll
mv %{buildroot}%{_libdir}/wine/d3d10.dll %{buildroot}%{_libdir}/wine/dxvk-d3d10.dll
mv %{buildroot}%{_libdir}/wine/d3d10core.dll %{buildroot}%{_libdir}/wine/dxvk-d3d10core.dll
mv %{buildroot}%{_libdir}/wine/d3d10_1.dll %{buildroot}%{_libdir}/wine/dxvk-d3d10_1.dll
mv %{buildroot}%{_libdir}/wine/d3d11.dll %{buildroot}%{_libdir}/wine/dxvk-d3d11.dll

%posttrans
if vulkaninfo |& grep ERROR_INITIALIZATION_FAILED > /dev/null; then
    %{_sbindir}/alternatives --install %{_libdir}/wine/d3d10.dll 'wine-d3d10%{?_isa}' %{_libdir}/wine/dxvk-d3d10.dll 5 \
    --slave %{_libdir}/wine/d3d10_1.dll 'wine-d3d10_1%{?_isa}' %{_libdir}/wine/dxvk-d3d10_1.dll \
    --slave %{_libdir}/wine/d3d10core.dll 'wine-d3d10core%{?_isa}' %{_libdir}/wine/dxvk-d3d10core.dll
    %{_sbindir}/alternatives --install %{_libdir}/wine/d3d11.dll 'wine-d3d11%{?_isa}' %{_libdir}/wine/dxvk-d3d11.dll 5
else
    %{_sbindir}/alternatives --install %{_libdir}/wine/d3d10.dll 'wine-d3d10%{?_isa}' %{_libdir}/wine/dxvk-d3d10.dll 20 \
    --slave %{_libdir}/wine/d3d10_1.dll 'wine-d3d10_1%{?_isa}' %{_libdir}/wine/dxvk-d3d10_1.dll \
    --slave %{_libdir}/wine/d3d10core.dll 'wine-d3d10core%{?_isa}' %{_libdir}/wine/dxvk-d3d10core.dll
    %{_sbindir}/alternatives --install %{_libdir}/wine/d3d11.dll 'wine-d3d11%{?_isa}' %{_libdir}/wine/dxvk-d3d11.dll 20
fi

%posttrans d3d9
if vulkaninfo |& grep ERROR_INITIALIZATION_FAILED > /dev/null; then
    %{_sbindir}/alternatives --install %{_libdir}/wine/d3d9.dll 'wine-d3d9%{?_isa}' %{_libdir}/wine/dxvk-d3d9.dll 5
else
    %{_sbindir}/alternatives --install %{_libdir}/wine/d3d9.dll 'wine-d3d9%{?_isa}' %{_libdir}/wine/dxvk-d3d9.dll 20
fi

%postun
%{_sbindir}/alternatives --remove 'wine-d3d10%{?_isa}' %{_libdir}/wine/dxvk-d3d10.dll
%{_sbindir}/alternatives --remove 'wine-d3d11%{?_isa}' %{_libdir}/wine/dxvk-d3d11.dll

%postun d3d9
%{_sbindir}/alternatives --remove 'wine-d3d9%{?_isa}' %{_libdir}/wine/dxvk-d3d9.dll

%files
%license LICENSE
%doc README.md
%{_libdir}/wine/dxvk-d3d10.dll
%{_libdir}/wine/dxvk-d3d10_1.dll
%{_libdir}/wine/dxvk-d3d10core.dll
%{_libdir}/wine/dxvk-d3d11.dll

%files d3d9
%license LICENSE
%{_libdir}/wine/dxvk-d3d9.dll

%files dxgi
%license LICENSE
%{_libdir}/wine/dxvk-dxgi.dll


%changelog
* Thu Oct 08 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.7.2-1
- Release 1.7.2

* Fri Aug 14 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.7.1-1
- Release 1.7.1

* Sun Aug 09 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.7-3
- Install dxvk as primary alternative only on systems with Vulkan support

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 17 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.7-1
- Release 1.7
- Remove winelib build and fix mingw build dll names (Matias Zuniga)

* Mon Apr 20 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.6.1-1
- Release 1.6.1

* Tue Mar 24 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.6-1
- Release 1.6

* Sat Mar 07 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.5.5-1
- Release 1.5.5

* Sun Feb 09 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.5.4-1
- Release 1.5.4

* Fri Jan 31 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.5.3-1
- Release 1.5.3

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.5.1-1
- Release 1.5.1
- Support D3D9 (wine-dxvk-d3d9 subpackage)

* Sat Dec 07 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.4.6-1
- Release 1.4.6

* Thu Nov 21 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.4.5-1
- Release 1.4.5

* Tue Oct 29 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.4.4-1
- Release 1.4.4

* Sat Oct 19 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.4.3-1
- Release 1.4.3

* Sat Sep 28 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.4.1-1
- Release 1.4.1

* Mon Sep 23 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.4-1
- Release 1.4

* Sun Aug 11 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.3.2-1
- Release 1.3.2
- Use alternatives for .dll files and dxgi.dll.so

* Thu Jul 25 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.3.1-1
- Initial packaging

