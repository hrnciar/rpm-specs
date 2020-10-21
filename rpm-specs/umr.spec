%global commit cf9e2f8029c3b1871480dc04e0036a20276fbcc0
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20200709
%global fgittag %{gitdate}git%{shortcommit}

Summary: AMDGPU Userspace Register Debugger
Name: umr
Version: 1.0
Release: 8%{?fgittag:.%{fgittag}}%{?dist}
License: MIT
URL: https://gitlab.freedesktop.org/tomstdenis/umr
Source0: https://gitlab.freedesktop.org/tomstdenis/%{name}/-/archive/%{shortcommit}/%{name}-%{shortcommit}.tar.gz

#Glibc is too old prior to EL7, enable rt linking to avoid compilation failure
%if 0%{?rhel} && 0%{?rhel} < 7
%global enablert 1
%endif

#UMR requires llvm >= 7 to enable llvm features, enable for EL8+/F29+
%if 0%{?rhel} > 7 || 0%{?fedora} > 28
BuildRequires: llvm-devel
%else
%global disablellvm 1
%endif

#UMR requires a recent libdrm enable libdrm features, enable for EL8+/Fedora
%if 0%{?rhel} > 7 || 0%{?fedora}
BuildRequires: libdrm-devel
%else
%global disablelibdrm 1
%endif

BuildRequires: cmake%{?rhel:3}
BuildRequires: gcc-c++
BuildRequires: libpciaccess-devel
BuildRequires: ncurses-devel
BuildRequires: zlib-devel

%description
AMDGPU Userspace Register Debugger (UMR) is a tool to read and display, as well
as write to AMDGPU device MMIO, PCIE, SMC, and DIDT registers via userspace.

%package devel
Summary: UMR development package
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-static = %{version}-%{release}

%description devel
AMDGPU Userspace Register Debugger header files and libraries

%prep
%autosetup -p1 -n %{name}-%{shortcommit}

%build
%{!?cmake:%global cmake %%cmake3}
%cmake %{?disablellvm:-DUMR_NO_LLVM=ON} \
	%{?disablelibdrm:-DUMR_NO_DRM=ON} \
	%{?enablert:-DUMR_NEED_RT=ON} \
	-DCMAKE_BUILD_TYPE="RELEASE"
%cmake_build

%install
%cmake_install

%files
%doc README
%license LICENSE
%{_bindir}/umr
%{_mandir}/man1/*

%files devel
%{_includedir}/umr*
%{_libdir}/*.a

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8.20200709gitcf9e2f8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 09 2020 Jeremy Newton <alexjnewt AT hotmail DOT com> - 1.0-7.20200709gitcf9e2f8
- Update to newer git
- Drop static llvm dependency

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6.20191210git0affde7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 15 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5.20191210git0affde7
- Update to newer git

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4.20190514gitcb1cb54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 29 2019 Jeremy Newton <alexjnewt AT hotmail DOT com> 1.0-3.20190514gitcb1cb54
- Update to newer git, switch to gitlab

* Wed Apr 03 2019 Jeremy Newton <alexjnewt AT hotmail DOT com> 1.0-2.20190403git1139876
- Update to newer git, fixes install issues and all patches upstreamed
- Add missing static provides for devel

* Thu Mar 21 2019 Jeremy Newton <alexjnewt AT hotmail DOT com> 1.0-1.20190322.git51112c7
- Intial Package
