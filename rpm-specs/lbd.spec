Name:           lbd
Version:        0.4
Release:        9%{?dist}
Summary:        A DNS/HTTP load balancing detector

License:        GPLv2+
URL:            https://github.com/craig/ge.mine.nu/tree/master/lbd
Source0:        https://raw.githubusercontent.com/craig/ge.mine.nu/master/lbd/%{name}.sh#/%{name}
BuildArch:      noarch

Requires:       bind-utils
Requires:       nc

%description
lbd (load balancing detector) detects if a given domain uses DNS and/or HTTP 
Load-Balancing (via Server: and Date: header and diffs between server answers).

%prep
# Nothing to prep

%build
# Nothing to build

%install
install -d %{buildroot}%{_bindir}
install -p -m 755 %{SOURCE0} %{buildroot}%{_bindir}/

%files
%{_bindir}/lbd

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 11 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.4-1
- Update to latest upstream release 0.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Nikolay Ulyanitsky <lystor AT gmail.com> - 0.2-7
- fix url

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Apr 18 2010 Nikolay Ulyanitsky <lystor AT lystor.org.ua> - 0.2-2
- Fix the license

* Sat Apr 17 2010 Nikolay Ulyanitsky <lystor AT lystor.org.ua> - 0.2-1
- Update to 0.2

* Sat Mar 13 2010 Nikolay Ulyanitsky <lystor AT lystor.org.ua> - 0.1-2
- Replace generally useful macros by regular commands

* Tue Feb 02 2010 Nikolay Ulyanitsky <lystor AT lystor.org.ua> - 0.1-1
- Initial package build

