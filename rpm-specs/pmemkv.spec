Name:		pmemkv
Version:	1.1
Release:	1%{?dist}
Summary:	Key/Value Datastore for Persistent Memory

License:	BSD
URL:		https://github.com/pmem/pmemkv
Source0:	https://github.com/pmem/pmemkv/archive/%{version}/%{name}-%{version}.tar.gz
# There's some work to port dependencies to non-x86, but we're not there yet.
ExclusiveArch:	x86_64

BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	valgrind
BuildRequires:	valgrind-devel
BuildRequires:	pkg-config
BuildRequires:	pandoc
BuildRequires:	libpmemobj++-devel >= 1.9
BuildRequires:	libpmemobj-devel >= 1.8
BuildRequires:	tbb-devel
BuildRequires:	memkind-devel
BuildRequires:	rapidjson-devel
BuildRequires:	gtest-devel

%description
Pmemkv is a family of key:value stores, developed with persistent memory
in mind -- yet rather than being tied to a single backing implementation,
it presents a common interface to a number of engines, both provided by
pmemkv itself and external.

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
PMEM_IS_PMEM_FORCE=1 ctest --output-on-failure -j1


%files
%{_libdir}/libpmemkv*.so.1*
%license LICENSE

%files devel
%{_includedir}/*.h
%{_includedir}/*.hpp
%{_mandir}/*/*pmemkv*
%{_libdir}/libpmemkv*.so
%{_libdir}/pkgconfig/libpmemkv*.pc


%changelog
* Wed Feb 12 2020 Adam Borowski <kilobyte@angband.pl> 1.1-1
- Upstream release 1.1
- Bump BReqs for pmemobj and pmemobj-cpp.

* Tue Feb 11 2020 Adam Borowski <kilobyte@angband.pl> 1.0.2-1
- Upstream release 1.0.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 29 2019 Adam Borowski <kilobyte@angband.pl> 1.0.1-1
- Initial packaging
