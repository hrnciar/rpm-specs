%global commit da2b76f9ef1fb7100a109b4c0b20e08eedf76ed6
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           freeopcua
Version:        0
Release:        0.14.20200131.%{shortcommit}%{?dist}
Summary:        Open Source C++ OPC-UA Server and Client Library

License:        LGPLv3+
URL:            http://freeopcua.github.io/
Source0:        https://github.com/FreeOpcUa/freeopcua/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# Do not override build flags, we want to use the Fedora flags
Patch0:         freeopcua.build-flags.patch
# https://github.com/FreeOpcUa/freeopcua/pull/354
Patch1:         freeopcua.catch-exception-in-destructor.patch
# Upstream has not reacted to a request to add a SOVERSION:
# https://github.com/FreeOpcUa/freeopcua/issues/337
# This patch sets the SOVERSION to 0.1.
Patch2:         freeopcua.set-soversion.patch
# https://github.com/FreeOpcUa/freeopcua/pull/356
Patch3:         freeopcua.use-system-spdlog.patch
Patch4:         freeopcua.boost-173-std-algorithm-includes.patch

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  mbedtls-devel
BuildRequires:  spdlog-devel

%description
A LGPL C++ library to develop server and client OPC-UA applications.

%package    devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
# The dependencies are not picked up automatically
Requires:   mbedtls-devel
Requires:   spdlog-devel

%description  devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n %{name}-%{commit}

# Remove bundled spdlog
rm -rf include/opc/spdlog


%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{?_lib}
%cmake_build


%install
%cmake_install


%files
%license COPYING
%doc README.md
%{_libdir}/libopc*.so.0.1


%files devel
%{_includedir}/opc
%{_libdir}/cmake/*
%{_libdir}/pkgconfig/*
%{_libdir}/libopc*.so



%changelog
* Thu Aug 06 2020 Till Hofmann <thofmann@fedoraproject.org> - 0-0.14.20200131.da2b76f
- Adapt to cmake's out-of-source builds

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20200131.da2b76f
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.20200131.da2b76f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Till Hofmann <thofmann@fedoraproject.org> - 0-0.11.20200131.da2b76f
- Add patch to fix FTBFS with boost 1.73

* Thu Apr 23 2020 Till Hofmann <thofmann@fedoraproject.org> - 0-0.10.20200131.da2b76f
- Update spdlog patch to properly export compiler flags (update to upstream PR #356)

* Tue Apr 21 2020 Till Hofmann <thofmann@fedoraproject.org> - 0-0.9.20200131.da2b76f
- Remove bundled spdlog and build against system spdlog instead

* Thu Apr 16 2020 Till Hofmann <thofmann@fedoraproject.org> - 0-0.8.20200131.da2b76f
- Add patch to set the downstream SOVERSION to 0.1

* Thu Feb 06 2020 Till Hofmann <thofmann@fedoraproject.org> - 0-0.7.20200131.da2b76f
- Add patch to catch exception in UaClient destructor

* Fri Jan 31 2020 Till Hofmann <thofmann@fedoraproject.org> - 0-0.6.20200131.da2b76f
- Update snapshot to latest upstream commit
- Remove upstreamed patches

* Sat Jul 27 2019 Till Hofmann <thofmann@fedoraproject.org> - 0-0.5.20190615.6124e55
- Add patch to fix build failure with boost 1.69

* Sat Jun 15 2019 Till Hofmann <thofmann@fedoraproject.org> - 0-0.4.20190615.6124e55
- Update snapshot to latest upstream commit

* Sun Apr 28 2019 Till Hofmann <thofmann@fedoraproject.org> - 0-0.3.20190417.2f2c886
- Add dependency of devel sub-package on mbedtls-devel

* Sun Apr 28 2019 Till Hofmann <thofmann@fedoraproject.org> - 0-0.2.20190417.2f2c886
- Move cmake and pkgconfig files into devel sub-package

* Wed Apr 17 2019 Till Hofmann <thofmann@fedoraproject.org> - 0-0.1.20190417.2f2c886
- Initial package
