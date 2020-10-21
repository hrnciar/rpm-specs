Name:		sha2
Version:	1.0.1
Release:	18%{?dist}
Summary:	SHA Implementation Library
License:	BSD
URL:		http://www.aarongifford.com/computers/sha.html
Source0:	http://www.aarongifford.com/computers/%{name}-%{version}.tgz
# Makefile to build the binaries. Sent upstream via email
Source1:	%{name}-Makefile
BuildRequires:  gcc
BuildRequires:  perl-interpreter

%description
The library implements the SHA-256, SHA-384, and SHA-512 hash algorithms. The
interface is similar to the interface to SHA-1 found in the OpenSSL library.

sha2 is a simple program that accepts input from either STDIN or reads one or
more files specified on the command line, and then generates the specified hash
(either SHA-256, SHA-384, SHA-512, or any combination thereof, including all
three at once).


%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
cp -a %{SOURCE1} Makefile

%build
make %{?_smp_mflags} \
	OPTFLAGS="%{optflags}"

%install
make install \
	DESTDIR=%{buildroot} \
	LIBDIR=%{_libdir} \
	INCLUDEDIR=%{_includedir} \
	BINDIR=%{_bindir} \
	OPTFLAGS="%{optflags}"

%check
LD_PRELOAD=./libsha2.so ./sha2test.pl

%ldconfig_scriptlets


%files
%doc README
%{_libdir}/libsha2.so.*
%{_bindir}/sha2*


%files devel
%{_includedir}/sha2.h
%{_libdir}/libsha2.so


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 20 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.0.1-10
- Add explicit dependency to perl

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 16 2012 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 1.0.1-1
- Initial build
