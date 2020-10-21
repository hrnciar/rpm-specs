Name:		freetiger
Version:	5
Release:	17%{?dist}
Summary:	Free implementation of the tiger hash algorithm
%{?el5:Group:	System Environment/Libraries}

License:	BSD
URL:		http://klondike.es/%{name}
Source0:	http://klondike.es/%{name}/%{name}-v%{version}.tar.bz
Source1:	http://besser82.fedorapeople.org/%{name}/%{name}-v%{version}_cmake.tar.gz

# no need to submit, just make test-prog return 0.
Patch0:		freetiger_fix_testprog.patch

%{?el5:BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)}
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	cmake

%description
%{name} is an implementation of the tiger hash algorithm made looking
only at the tiger reference paper (thus ignoring the reference code until
a working implementation was made). It also includes a modified version
of the main program included with the tiger reference implementation which
was used for benchmarking purposes.

It has been optimized for usage in the TTH calculation algorithm and
includes optimized versions that will calculate the hashes for the
1024 byte file chunks and the 48 byte hash concatenation appending the
proper suffix automatically thus minimizing memory to memory copying.

Also %{name} features interleaved hashing where the hashes of two
different blocks are calculated at the same time interleaving the
operations of one and the other. Using this increases the
implementation performance.

%{name} also supports SSE2 for key scheduling during the tiger rounds
which also increases performance on processors supporting it and
provides an implementation of the partial hashing scheme for a more
secure password storage when authenticating clients using the GPA
command in ADC.

%package	devel
Summary:	Development files for %{name}
%{?el5:Group:	Development/Libraries}

Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -b 1 -n tiger
%patch0


%build
mkdir -p build
pushd build
%cmake \
	-DCMAKE_SKIP_RPATH:BOOL=OFF \
	..
make %{?_smp_mflags}


%check
pushd build
make check


%install
pushd build
%{?el5:rm -rf %{buildroot}}
make install DESTDIR=%{buildroot}



%ldconfig_scriptlets


%files
%doc CHANGELOG DISCLAIMER LICENSE README THANKS
%{_libdir}/*.so.*

%files devel
%doc C/README C/tigermain.c C/TODO
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/*

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5-17
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 06 2017 Björn Esser <besser82@fedoraproject.org> - 5-10
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 31 2013 Björn Esser <bjoern.esser@gmail.com> - 5-2
- devel shouldn't require cmake, owning %%{_libdir}/cmake is enough.

* Fri May 31 2013 Björn Esser <bjoern.esser@gmail.com> - 5-1
- Initial rpm release (#969387)
