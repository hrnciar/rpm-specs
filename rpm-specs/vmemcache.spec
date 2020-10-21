# The tests are failing for some reason if built out-of-source
%global __cmake_in_source_build 1

Name:		vmemcache
Version:	0.8
Release:	7%{?dist}
Summary:	Buffer-based LRU cache

License:	BSD
URL:		https://github.com/pmem/vmemcache
Source0:	https://github.com/pmem/vmemcache/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		0001-Don-t-let-gcc-replace-Zalloc-by-calloc.patch
ExclusiveArch:	x86_64 ppc64 ppc64le s390x aarch64

BuildRequires:	cmake
BuildRequires:	valgrind
BuildRequires:	valgrind-devel
BuildRequires:	pkg-config
BuildRequires:	gcc
BuildRequires:	pandoc

%description
Vmemcache is a volatile filesystem based key:value cache.  It works best
when backed with a DAX-capable persistent memory device, but can work on
tmpfs or on legacy disks.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1


%build
%cmake
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%{_libdir}/libvmemcache.so.0*
%license LICENSE

%files devel
%{_includedir}/*.h
%{_mandir}/*/vmemcache*
%{_libdir}/libvmemcache.so
%{_libdir}/pkgconfig/libvmemcache.pc
%doc ChangeLog


%changelog
* Tue Aug 25 2020 Adam Borowski <kilobyte@angband.pl> 0.8-7
- Re-enable LTO
- Disable optimizations for a function miscompiled by new GCC.

* Thu Aug 06 2020 Jeff Law <law@redhat.com> - 0.8-6
- Disable LTO

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 Adam Borowski <kilobyte@angband.pl> 0.8-1
- Initial packaging
