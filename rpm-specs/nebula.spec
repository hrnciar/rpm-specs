Name:           nebula
Version:        0.2.3
Release:        23%{?dist}
Summary:        Intrusion signature generator

License:        GPLv2
URL:            http://nebula.carnivore.it/
Source0:        http://downloads.sourceforge.net/nebula/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  zlib-devel

%description
Nebula is an intrusion signature generator. It can help securing a network
by automatically calculating filter rules from attack traces. In a common
setup nebula runs as a daemon and receives attacks from honeypots.

%prep
%setup -q

%build
# FIXME: Package suffers from c11/inline issues
# Workaround by appending --std=gnu89 to CFLAGS
# Proper fix would be to fix the source-code
%configure CFLAGS="${RPM_OPT_FLAGS} --std=gnu89 -fcommon"
make %{?_smp_mflags} AM_CFLAGS=-D_GNU_SOURCE

%install
%make_install

%files
%doc AUTHORS ChangeLog
%license COPYING
%{_bindir}/nebula
%{_bindir}/nebulaclient

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 31 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.3-21
- Update spec file

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.2.3-12
- Append --stdc=gnu89 to CFLAGS (Work-around to c11/inline compatibility
  issues. Fix FTBFS).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 14 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.3-10
- Update spec file
- Switch to bz2 archive

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 0.2.3-6
- Updated to 0.2.3

* Fri Nov 07 2008 Rakesh Pandit <rakesh@fedoraproject.org> - 0.2.2-5
- fixed Buildrequires

* Fri Nov 07 2008 Rakesh Pandit <rakesh@fedoraproject.org> - 0.2.2-4
- saving timestamp

* Fri Nov 07 2008 Rakesh Pandit <rakesh@fedoraproject.org> - 0.2.2-3
- Fixed flags - (Till Mass)

* Fri Oct 31 2008 Rakesh Pandit <rakesh@fedoraproject.org> - 0.2.2-2
- Consistently using macros, added -j3 to make

* Fri Oct 31 2008 Rakesh Pandit <rakesh@fedoraproject.org> - 0.2.2-1
- Initial package
