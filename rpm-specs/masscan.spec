Name:		masscan
Version:	1.0.5
Release:	3%{?dist}
Summary:	This is an Internet-scale port scanner

License:	BSD
URL:		https://github.com/robertdavidgraham/masscan	
#		https://github.com/robertdavidgraham/masscan/releases

%global commit 83fbdf6fde8f40573381a546d6b27cc78d77cc85
%global shortcommit %(c=%{commit}; echo ${c:0:7})

#Source0:	https://github.com/robertdavidgraham/%{name}/archive/%{commit}/%{commit}.tar.gz
Source0:	https://github.com/robertdavidgraham/masscan/archive/%{version}/%{name}-%{version}.tar.gz
Patch2:		%{name}-1.0.5-gcc.patch

BuildRequires:	gcc
BuildRequires:	libpcap-devel

%description
This is an Internet-scale port scanner. It can scan the entire 
Internet in under 6 minutes, transmitting 10 million packets 
per second, from a single machine.
It is a faster port scan that produces results similar to nmap,
the most famous port scanner. Internally, it operates more like
scanrand, unicornscan, and ZMap, using asynchronous transmission.

%prep
%autosetup -n %{name}-%{version}
sed -i 's/\r$//' VULNINFO.md

%build
# Compile with GCC by default
# gcc is preffered compiler by Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#compiler
export CC=gcc
make %{?_smp_mflags} CFLAGS="%{optflags}" CXXFLAGS="%{optflags}"


%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_bindir}/
install -pm 0755 bin/masscan %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc VULNINFO.md README.md
%{_bindir}/%{name}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.5-2
- Update summary and source URL

* Thu Oct 17 2019 Michal Ambroz <rebus at_ seznam.cz> - 1.0.5-1
- update to version 1.0.5

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 16 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0.3-7
- Extend masscan-1.0.3-gcc5.patch to treat gcc <= 7 as GCC4
  (Fix F25FTBFS, F26FTBFS).

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 15 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.0.3-4
- Add support for gcc-5/Add masscan-1.0.3-gcc5.patch
  (Fix F23FTBFS, RHBZ#1239667).
- Add %%license.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 23 2014 Rino Rondan <villadalmine@fedoraproject.org> - 1.0.3-1
- Rebuilt for version 1.0.3 and fix Source0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 21 2014 Dan Horák <dan[at]danny.cz> - 1.0-8
- fix build on secondary arches

* Wed Jan 01 2014 Rino Rondan <villadalmine@fedoraproject.org> - 1.0-7
- Change the description

* Mon Nov 04 2013 Rino Rondan <villadalmine@fedoraproject.org> - 1.0-6
- Change the version macro, and all relationship with it

* Thu Oct 31 2013 Rino Rondan <villadalmine@fedoraproject.org> - 1.0-5
- Change summary and description

* Thu Oct 31 2013 Rino Rondan <villadalmine@fedoraproject.org> - 1.0-4
- Add some variables to build

* Thu Oct 31 2013 Rino Rondan <villadalmine@fedoraproject.org> - 1.0-3
- Add the correct info on changelog
- Fix the problem with doc

* Thu Oct 31 2013 Rino Rondan <villadalmine@fedoraproject.org> - 1.0-2
- Add the correct tag for pre-release on Version and Release
- Add global variable for checkout

* Wed Sep 11 2013 Rino Rondan <villadalmine@fedoraproject.org> - 1.0-1
- Initial Package
