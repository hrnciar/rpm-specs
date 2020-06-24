Name:		qclib
Version:	2.1.0
Release:	1%{?dist}
Summary:	Library for extraction of system information for Linux on z Systems
License:	BSD
URL:		http://www.ibm.com/developerworks/linux/linux390/qclib.html
Source0:	http://public.dhe.ibm.com/software/dw/linux390/ht_src/%{name}-%{version}.tgz
# https://bugzilla.redhat.com/show_bug.cgi?id=1306280
Patch0:		0001-introduce-DOCDIR.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1552658
Patch1:		0002-introduce-LDFLAGS.patch
ExclusiveArch:	s390 s390x
BuildRequires:	gcc
BuildRequires:	glibc-static
BuildRequires:	doxygen

%description
%{summary}.

%package devel
Summary:	Development library and headers for qclib
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
qclib provides a C API for extraction of system information for Linux on z
Systems.
For instance, it will provide the number of CPUs
 * on the machine (CEC, Central Electronic Complex) layer
 * on the PR/SM (Processor Resource/Systems Manager) layer, i.e. visible to
   LPARs, including LPAR groups in z/VM hosts, guests and CPU pools
 * in KVM hosts and guests

This allows calculating the upper limit of CPU resources a highest level guest
can use. For example: If an LPAR on a z13 provides 4 CPUs to a z/VM hyper-visor,
and the hyper-visor provides 8 virtual CPUs to a guest, qclib can be used to
retrieve all of these numbers, and it can be concluded that not more capacity
than 4 CPUs can be used by the software running in the guest.

This package provides the development libraries and headers for qclib.

%package static
Summary:	Static library for qclib
Requires:	%{name}-devel = %{version}-%{release}
Provides:	%{name}-static = %{version}-%{release}

%description static
%{summary}. This package provides static libraries for qclib.


%prep
%autosetup


%build
make V=1 CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" %{?_smp_mflags} all doc


%install
%make_install DOCDIR=%{_docdir}
make DESTDIR=%{buildroot} DOCDIR=%{_docdir} installdoc


%check
make test-sh test


%files
%dir %{_docdir}/%{name}
%license %{_docdir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/README
%{_libdir}/libqc.so.*

%files devel
%doc %{_docdir}/%{name}/html/
%{_libdir}/libqc*.so
%{_includedir}/query_capacity.h

%files static
%{_libdir}/libqc*.a


%changelog
* Wed Apr 22 2020 Dan Horák <dan[at]danny.cz> - 2.1.0-1
- updated to 2.1.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Dan Horák <dan[at]danny.cz> - 2.0.1-1
- updated to 2.0.1

* Tue Nov 19 2019 Dan Horák <dan[at]danny.cz> - 2.0.0-1
- updated to 2.0.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Dan Horák <dan[at]danny.cz> - 1.4.1-1
- updated to 1.4.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 19 2018 Dan Horák <dan[at]danny.cz> - 1.4.0-1
- updated to 1.4.0

* Mon Mar 12 2018 Dan Horák <dan[at]danny.cz> - 1.3.1-3
- fix LDFLAGS injection (#1552658)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Dan Horák <dan[at]danny.cz> - 1.3.1-1
- updated to 1.3.1

* Mon Dec 04 2017 Dan Horák <dan[at]danny.cz> - 1.3.0-1
- updated to 1.3.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 31 2016 Rafael dos Santos <rdossant@redhat.com> 1.2.0-1
- Initial packaging
