Name:       nss-pem
Version:    1.0.6
Release:    1%{?dist}
Summary:    PEM file reader for Network Security Services (NSS)

License:    MPLv1.1
URL:        https://github.com/kdudka/nss-pem
Source0:    https://github.com/kdudka/nss-pem/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: nss-pkcs11-devel

# require at least the version of nss that nss-pem was built against (#1428965)
Requires: nss%{?_isa} >= %(nss-config --version 2>/dev/null || echo 0)

# nss-pem is no longer a multilib package, ease the f27->f28 upgrade (#1553646)
Obsoletes: %{name} < %{version}-%{release}
%if 0%{?__isa_bits} == 64
Conflicts: %{name}%(tmp="%{_isa}" && echo "${tmp/-64/-32}") < %{version}-%{release}
%endif

%description
PEM file reader for Network Security Services (NSS), implemented as a PKCS#11
module.

%prep
%setup -q

%build
mkdir build
cd build
%cmake ../src
make %{?_smp_mflags} VERBOSE=yes

%install
cd build
make install DESTDIR=%{buildroot}

%check
cd build
ctest %{?_smp_mflags} --output-on-failure

%files
%{_libdir}/libnsspem.so
%license COPYING

%changelog
* Thu Feb 13 2020 Kamil Dudka <kdudka@redhat.com> 1.0.6-1
- update to latest upstream bugfix release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 07 2019 Kamil Dudka <kdudka@redhat.com> 1.0.5-1
- update to latest upstream bugfix release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 09 2018 Kamil Dudka <kdudka@redhat.com> 1.0.4-1
- update to latest upstream bugfix release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 09 2018 Kamil Dudka <kdudka@redhat.com>> - 1.0.3-9
- nss-pem is no longer a multilib package, ease the f27->f28 upgrade (#1553646)

* Mon Feb 19 2018 Kamil Dudka <kdudka@redhat.com>> - 1.0.3-8
- add explicit BR for the gcc compiler

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Kamil Dudka <kdudka@redhat.com> 1.0.3-6
- release bump needed to fix #1500655

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 13 2017 Kamil Dudka <kdudka@redhat.com> 1.0.3-3
- release bump

* Mon Mar 06 2017 Kamil Dudka <kdudka@redhat.com> 1.0.3-2
- require at least the version of nss that nss-pem was built against (#1428965)

* Wed Mar 01 2017 Kamil Dudka <kdudka@redhat.com> 1.0.3-1
- update to latest upstream bugfix release

* Wed Feb 22 2017 Kamil Dudka <kdudka@redhat.com> 1.0.2-4
- rebuild against nss-3.29.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 22 2016 Kamil Dudka <kdudka@redhat.com> 1.0.2-2
- explicitly conflict with all nss builds with bundled nss-pem (#1347336)

* Thu Jun 16 2016 Kamil Dudka <kdudka@redhat.com> 1.0.2-1
- packaged for Fedora
