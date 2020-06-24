Name:           bannergrab
Version:        3.5
Release:        15%{?dist}
Summary:        A banner grabbing tool

License:        GPLv3+
URL:            http://sourceforge.net/projects/bannergrab
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz

BuildRequires:  gcc
BuildRequires:  openssl-devel

%description
Bannergrab is a simple tool, designed to collect information from network
services. It can do this using two different methods; grab the connection
banners and send triggers and collect the responses. Bannergrab defaults to
sending triggers.

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="%{optflags} -lcrypto"

%install
install -Dp -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dp -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc Changelog README TODO
%license LICENSE
%{_mandir}/man?/*.*
%{_bindir}/%{name}

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 25 2017 Fabian Affolter <mail@fabian-affolter.ch> - 3.5-8
- Update spec file

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 24 2012 Fabian Affolter <mail@fabian-affolter.ch> - 3.5-1
- Initial package for Fedora
