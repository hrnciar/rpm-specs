Name:		xblas
Version:	1.0.248
Release:	21%{?dist}
Summary:	Extra Precise Basic Linear Algebra Subroutines
License:	BSD
URL:		http://www.netlib.org/xblas
Source0:	http://www.netlib.org/%{name}/%{name}-%{version}.tar.gz
Patch0:		xblas-1.0.247-shared.patch
BuildRequires:	gcc-gfortran, autoconf, m4, indent

%description
The XBLAS library of routines is part of a reference implementation for 
the Dense and Banded Basic Linear Algebra Subroutines, along with their 
Extended and Mixed Precision versions, as documented in Chapters 2 and 4 
of the new BLAS Standard.

%package devel
Summary:	Development files for xblas
Requires:	%{name} = %{version}-%{release}

%description devel
Headers and libraries for developing code that uses xblas.

%prep
%setup -q
%patch0 -p1 -b .shared
autoconf

%build
%configure
make makefiles
# smp_mflags doesn't work
make lib

%install
mkdir -p %{buildroot}%{_libdir}
install -m0755 libxblas.so.1.0.0 %{buildroot}%{_libdir}
pushd %{buildroot}%{_libdir}
ln -s libxblas.so.1.0.0 libxblas.so.1
ln -s libxblas.so.1.0.0 libxblas.so
popd
mkdir -p %{buildroot}%{_includedir}
install -m0644 src/*.h %{buildroot}%{_includedir}

%check
make tests

%ldconfig_scriptlets

%files
%doc LICENSE doc/report.ps
%{_libdir}/*.so.*

%files devel
%doc README
%{_libdir}/*.so
%{_includedir}/*.h

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.248-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.248-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.248-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.248-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.248-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb  2 2018 Tom Callaway <spot@fedoraproject.org> - 1.0.248-16
- rebuild for new gfortran

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.248-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.248-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.248-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb  4 2017 Tom Callaway <spot@fedoraproject.org> - 1.0.248-12
- rebuild for new gfortran

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.248-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.248-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.248-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.248-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.248-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.248-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.248-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.248-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.248-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 21 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.0.248-2
- drop README.devel, move README to -devel
- don't bother deleting buildroot at the beginning of install
- no need to define BuildRoot anymore

* Thu Apr 23 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.0.248-1
- update to 1.0.248

* Mon Apr 20 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.0.247-1
- initial package
