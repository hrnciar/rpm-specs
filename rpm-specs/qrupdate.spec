Name:		qrupdate
Version:	1.1.2
Release:	19%{?dist}
Summary:	A Fortran library for fast updates of QR and Cholesky decompositions
License:	GPLv3+
URL:		http://qrupdate.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:	gcc-gfortran

BuildRequires:	openblas-devel

%description
qrupdate is a Fortran library for fast updates of QR and Cholesky
decompositions. 

%package devel
Summary:	Development libraries for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	openblas-devel%{?_isa}

%description devel
This package contains the development libraries for %{name}.

%prep
%setup -q
# Modify install location
sed -i 's|$(PREFIX)/lib/|$(DESTDIR)%{_libdir}/|g' src/Makefile

%build
%make_build solib FC=gfortran FFLAGS="%{optflags} -fimplicit-none -funroll-loops -fallow-argument-mismatch" BLAS="-lopenblas" LAPACK=

%install
make install-shlib LIBDIR=%{_libdir} PREFIX="%{buildroot}"
# Verify attributes
chmod 755 %{buildroot}%{_libdir}/libqrupdate.*

%check
make test FC=gfortran FFLAGS="%{optflags} -fimplicit-none -funroll-loops -fallow-argument-mismatch" BLAS="-lopenblas" LAPACK=

%ldconfig_scriptlets

%files
%license COPYING
%doc README ChangeLog
%{_libdir}/libqrupdate.so.*

%files devel
%{_libdir}/libqrupdate.so


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 10 2019 Orion Poplawski <orion@nwra.com> - 1.1.2-17
- Use openblas

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.1.2-13
- Rebuild for new gfortran

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Orion Poplawski <orion@cora.nwra.com> - 1.1.2-9
- Rebuild for gcc 7
- Cleanup spec

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 07 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.1.2-1
- Update to 1.1.2.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 12 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1.

* Mon Jan 11 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.1.0-2
- Bump spec.

* Mon Jan 11 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0.1-1
- First release.
