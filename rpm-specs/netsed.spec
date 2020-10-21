Name:           netsed
Version:        1.2
Release:        15%{?dist}
Summary:        A tool to modify network packets

License:        GPLv2+
URL:            http://silicone.homelinux.org/projects/netsed/
Source0:        http://silicone.homelinux.org/release/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  doxygen
BuildRequires:  graphviz
#BuildRequires:  rubygem-minitest

%description
NetSED is small and handful utility designed to alter the contents of
packets forwarded through your network in real time. It is really useful
for network hackers in following applications:

* black-box protocol auditing - whenever there are two or more
  proprietary boxes communicating over undocumented protocol (by enforcing 
  changes in ongoing transmissions, you will be able to test if tested 
  application is secure),
* fuzz-alike experiments, integrity tests - whenever you want to test 
  stability of the application and see how it ensures data integrity,
* other common applications - fooling other people, content filtering,
  etc - choose whatever you want to.

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"
make doc

%install
install -Dp -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

#%check
#cd test
#ruby tc_*.rb

%files
%doc LICENSE NEWS README TODO html/
%{_bindir}/%{name}

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 18 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.2-3
- Fix FTBFS (rhbz#1106289)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 15 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.2-2
- Update to latest upstream release 1.2

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 19 2012 Fabian Affolter <mail@fabian-affolter.ch> - 1.1-2
- Docs added
- Test enabled

* Sat Mar 20 2010 Fabian Affolter <mail@fabian-affolter.ch> - 1.1-1
- Initial spec for Fedora
