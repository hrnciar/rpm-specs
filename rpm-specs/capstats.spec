Name:           capstats
Version:        0.26
Release:        5%{?dist}
Summary:        A command-line tool collecting packet statistics

License:        BSD
URL:            https://github.com/zeek/capstats
Source0:        https://www.zeek.org/downloads/%{name}-%{version}.tar.gz
Patch0:         capstats-0.21-configure.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libpcap-devel

%description
capstats is a small tool to collect statistics on the current load of a
network interface. It reports statistics per time interval and/or for the
tool's total run-time.

%prep
%setup -q
%patch0 -p1 -b .configure

%build
%configure --disable-rpath
%make_build

%install
%make_install

%files
%doc CHANGES README
%license COPYING
%{_bindir}/%{name}

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 19 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.26-3
- Update details as project was renamed

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 08 2018 Fabian Affolter <mail@fabian-affolter.ch> - 0.26-1
- Update to new upstream release 0.26

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Fabian Affolter <mail@fabian-affolter.ch> - 0.25-1
- Update to new upstream release 0.25

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.22-1
- Update to new upstream release 0.22

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.21-3
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 25 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.21-1
- Update to new upstream release 0.21

* Mon Feb 17 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.20-1
- Initial package
