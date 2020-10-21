Name:           slowhttptest
Version:        1.8.2
Release:        1%{?dist}
Summary:        An Application Layer DoS attack simulator

License:        ASL 2.0
URL:            https://github.com/shekyan/slowhttptest
Source0:        https://github.com/shekyan/slowhttptest/archive/v%{version}.zip#/%{name}-%{version}.zip

BuildRequires:  gcc-c++
BuildRequires:  openssl-devel

%description
SlowHTTPTest is a highly configurable tool that simulates some Application
Layer Denial of Service attacks. It implements most common low-bandwidth
Application Layer DoS attacks, such as slow-loris, Slow HTTP POST, Slow Read
attack (based on TCP persist timer exploit) by draining concurrent connections
pool, as well as Apache Range Header attack by causing very significant memory
and CPU usage on the server. 

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%doc README.md 
%license LICENSE COPYING
%{_mandir}/man*/*.*
%{_bindir}/%{name}

%changelog
* Tue Aug 25 2020 Denis Fateyev <denis@fateyev.com> - 1.8.2-1
- Update to release 1.8.2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Denis Fateyev <denis@fateyev.com> - 1.8.1-1
- Update to release 1.8.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.7-5
- Fix FTBFS (rhbz#1556449)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 03 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.7-1
- Update to latest upstream release 1.7

* Mon Apr 03 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.6-9
- Fix FTBFS (rhbz#1424451)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 01 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.6-7
- Update upstream link

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.6-4
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 03 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.6-1
- Update to new upstream release 1.6

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 10 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.5-1
- Initial package for Fedora
