Name:		vmemcache
Version:	0.8
Release:	3%{?dist}
Summary:	Buffer-based LRU cache

License:	BSD
URL:		https://github.com/pmem/vmemcache
Source0:	https://github.com/pmem/vmemcache/archive/%{version}/%{name}-%{version}.tar.gz
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


%build
%cmake
make %{?_smp_mflags}


%install
%make_install


%check
ctest %{?_smp_mflags} --output-on-failure


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
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 Adam Borowski <kilobyte@angband.pl> 0.8-1
- Initial packaging
