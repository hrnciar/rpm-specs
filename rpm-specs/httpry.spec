Summary: A specialized packet sniffer designed for displaying and logging HTTP traffic
Name: httpry
Version: 0.1.8
Release: 13%{?dist}
License: GPLv2 and BSD
URL: http://dumpsterventures.com/jason/httpry/
Source: http://dumpsterventures.com/jason/httpry/httpry-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires: libpcap-devel

%description
httpry is a specialized packet sniffer designed for displaying and logging 
HTTP traffic. It is not intended to perform analysis itself, but to capture, 
parse, and log the traffic for later analysis. It can be run in real-time 
displaying the traffic as it is parsed, or as a daemon process that logs to 
an output file. It is written to be as lightweight and flexible as possible, 
so that it can be easily adaptable to different applications.

%prep
%setup -q

%build
sed -i 's/^CCFLAGS.*$/CCFLAGS = \$(RPM_OPT_FLAGS) \$(RPM_LD_FLAGS) -I\/usr\/include\/pcap -I\/usr\/local\/include\/pcap/' Makefile
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
install -Dp -m 0755 httpry ${RPM_BUILD_ROOT}%{_sbindir}/httpry
install -Dp -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc doc/ChangeLog doc/COPYING doc/format-string doc/method-string doc/perl-tools doc/README 
%{_sbindir}/httpry
%{_mandir}/man1/httpry.1*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.8-9
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 25 2014 Major Hayden <major@mhtx.net> - 0.1.8-1
- Upstream version 0.1.8 released.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 20 2012 Major Hayden <major@mhtx.net> - 0.1.7-1
- Upstream version 0.1.7 released.

* Mon Feb 27 2012 Major Hayden <major@mhtx.net> - 0.1.5-4
- Adjusted Makefile compiler flags to match packaging guidelines.

* Wed Aug 03 2011 Major Hayden <major@mhtx.net> - 0.1.5-3
- Additional cleanup
- Added man page
- Cleaning buildroot to meet EPEL requirements

* Fri Jun 24 2011 Major Hayden <major@mhtx.net> - 0.1.5-2
- Added %%{?_smp_mflags} to make

* Fri Jun 24 2011 Major Hayden <major@mhtx.net> - 0.1.5-1
- Initial build
