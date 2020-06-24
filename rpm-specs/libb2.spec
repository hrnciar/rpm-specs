%global with_check 1

Name:    libb2
Summary: C library providing BLAKE2b, BLAKE2s, BLAKE2bp, BLAKE2sp
Version: 0.98.1
Release: 2%{?dist}
License: CC0
URL:     https://blake2.net/
Source0: https://github.com/BLAKE2/libb2/archive/v%{version}/libb2-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: automake
BuildRequires: libtool

%description
C library providing BLAKE2b, BLAKE2s, BLAKE2bp, BLAKE2sp.

BLAKE2 is a cryptographic hash function faster than MD5, SHA-1, SHA-2,
and SHA-3, yet is at least as secure as the latest standard SHA-3.

%package        devel
Summary:        Development files for the Blake2 library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
%{summary}.

%prep
%autosetup -n libb2-%{version}

# Force default Fedora cflags
sed -e 's|CFLAGS=-O3|CFLAGS="%{optflags}"|g' -i configure.ac
autoreconf -ivf

%build
%configure --disable-silent-rules --enable-static=no --enable-native=no
%make_build

%if 0%{with_check}
%check
make check
%endif

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%license COPYING
%{_libdir}/libb2.so.1
%{_libdir}/libb2.so.1.*

%files devel
%{_libdir}/libb2.so
%{_libdir}/pkgconfig/libb2.pc
%{_includedir}/blake2.h

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.98.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.98.1-1
- Update to latest tagged version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-4.20171225git60ea749
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-3.20171225git60ea749
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-2.20171225git60ea749
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 18 2018 Antonio Trande <sagitter@fedoraproject.org> - 0.98-1.20171225git60ea749
- First RPM
