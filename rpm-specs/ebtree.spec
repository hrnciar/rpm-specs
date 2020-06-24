%global _hardened_build 1

Name:		ebtree
Version:	6.0.8
Release:	13%{?dist}
Summary:	Elastic binary tree library

License:	LGPLv2
URL:		http://1wt.eu/articles/ebtree/
Source0:	http://1wt.eu/tools/%{name}/%{name}-%{version}.tar.gz

# Build shared libraries. Upstream is asked for this in private mail.
# No mailing list nor bug tracker available
Patch1:		ebtree-6.0.8.build_shared_libs.patch

# There is no real test, just some binaries to run. So add a script to run them
Patch2:		ebtree-6.0.8.add_test_script.patch

BuildRequires:	make
BuildRequires:	coreutils
BuildRequires:	gcc
BuildRequires:	util-linux

# For epel5 support

%description
ebtree is a binary search tree specially optimized to very
frequently store, retrieve and delete discrete integer or binary
data without having to deal with memory allocation.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
License:	LGPLv2 and GPLv2+

%description devel
Development files for %{name}

%prep
%setup -q
%patch1 
%patch2

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"

# Some hardening on epel5,6
%if 0%{?rhel} == 5 || 0%{?rhel} == 6
export CFLAGS="%{optflags} -fPIC -DPIC -fPIE"
export LDFLAGS="%{?__global_ldflags} -Wl,-z,relro -z,now"
%endif
make %{?_smp_mflags} PREFIX=%{_prefix}
make test
head -245 ebtree.h > README

%check
bash tests.sh

%install
# For el5,6,7 support
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pkgconfig

%{make_install} PREFIX=%{_prefix}

%files
%doc VERSION README
%{_libdir}/*.so.*
%if 0%{?fedora} >= 17 || 0%{?rhel} >= 7
%license LICENSE
%else
%doc LICENSE
%endif

%files devel
%doc VERSION README examples
%{_includedir}/%{name}/*.h
%{_datadir}/pkgconfig/%{name}.pc
%{_libdir}/*.so
%if 0%{?fedora} >= 17 || 0%{?rhel} >= 7
%license LICENSE
%else
%doc LICENSE
%endif

%ldconfig_scriptlets

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 16 2017 Ingvar Hagelund <ingvar@redpill-linpro.com> 6.0.8-5
- Added pkgconfig and install targets to makefile patch

* Wed Jan 04 2017 Ingvar Hagelund <ingvar@redpill-linpro.com> 6.0.8-4
- post{un} -p ldconfig
- Fixed two-digit soname in Makefile patch
- added macro __global_ldflags also to epel5,6

* Wed Dec 07 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 6.0.8-3
- Patch specfile to honor CFLAGS and LDFLAGS
- Add some flags for hardening on epel5,6 too

* Tue Dec 06 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 6.0.8-2
- Set correct license combo for -devel subpackage
- Added buildreqs
- Only include LICENSE once
- Run test suite
- Set 0.1 as soversion
- devel subpackage reuquire main package NEVRA
- Call ldconfig in post and postun
- Move header files to separate directory

* Thu Aug 25 2016 Ingvar Hagelund <ingvar@redpill-linpro.com> 6.0.8-1
- First wrap for Fedora
