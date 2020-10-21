Name:		radamsa
Version:	0.6
Release:	2%{?dist}
Summary:	A general-purpose fuzzer
License:	MIT 
URL:		https://gitlab.com/akihe/radamsa
Source0:	https://gitlab.com/akihe/radamsa/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:	owl-lisp

%description
Radamsa is a test case generator for robustness testing.
It can be used to test how well a program can stand malformed and potentially
malicious inputs.

%prep
%autosetup -p1 -n %{name}-v%{version}


%build
make build_radamsa CFLAGS="%{optflags}" %{?_smp_mflags}
chmod 644 radamsa.c

%install
%make_install


%files
%doc README.md LICENCE
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 12 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.6-1
- Update to 0.6
- Update URLs

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Niranjan MR <mrniranjan@fedoraproject.org> - 0.5-1
- Update radamsa to v0.5

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec 19 2014 Niranjan MR <mrniranjan@fedoraproject.org> - 0.4-2
Add new target build_radamsa to build radamsa.c from /usr/bin/ol

* Thu Nov 27 2014 Niranjan MR <mrniranjan@fedoraproject.org> - 0.4-1
- initial version 
