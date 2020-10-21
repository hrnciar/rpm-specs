Name:       ctstream    
Version:    29
Release:    5%{?dist}
Summary:    Get URLs of Czech Television video streams
License:    GPL+
URL:        http://xpisar.wz.cz/%{name}/
Source0:    %{url}%{name}-%{version}
BuildArch:  noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators

%description
Get locators of Czech Television video streams for given web page.

%build
# Empty %%build section for possible RPM hooks

%install
install -d %{buildroot}%{_bindir}
install %{SOURCE0} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/*

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 29-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Petr Pisar <ppisar@redhat.com> - 29-1
- Version 29 bump

* Fri Jul 20 2018 Petr Pisar <ppisar@redhat.com> - 28-1
- Version 28 bump

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Petr Pisar <ppisar@redhat.com> - 27-1
- Version 27 bump

* Tue Feb 14 2017 Petr Pisar <ppisar@redhat.com> - 26-1
- Version 26 bump

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 23 2016 Petr Pisar <ppisar@redhat.com> - 25-1
- Version 25 bump

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 19 2015 Petr Pisar <ppisar@redhat.com> - 24-1
- Version 24 bump

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 02 2015 Petr Pisar <ppisar@redhat.com> - 23-1
- Version 23 bump

* Wed Dec 17 2014 Petr Šabata <contyk@redhat.com> - 22-1
- Version 22 bump

* Mon Jul 14 2014 Petr Pisar <ppisar@redhat.com> - 21-1
- Version 21 bump

* Mon Jun 30 2014 Petr Pisar <ppisar@redhat.com> - 20-1
- Version 20 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 06 2014 Petr Pisar <ppisar@redhat.com> - 19-1
- Version 19 bump

* Thu Apr 17 2014 Petr Pisar <ppisar@redhat.com> - 18-1
- Version 18 bump

* Fri Mar 28 2014 Petr Pisar <ppisar@redhat.com> - 17-1
- Version 17 bump

* Mon Feb 17 2014 Petr Pisar <ppisar@redhat.com> - 15-1
- Version 15 bump

* Mon Feb 03 2014 Petr Pisar <ppisar@redhat.com> - 13-1
- Version 13 bump

* Wed Jan 15 2014 Petr Pisar <ppisar@redhat.com> - 12-1
- Version 12 bump

* Mon Jan 13 2014 Petr Pisar <ppisar@redhat.com> - 11-1
- Version 11 bump

* Wed Jan 08 2014 Petr Pisar <ppisar@redhat.com> - 10-1
- Version 10 bump

* Thu Oct 31 2013 Petr Pisar <ppisar@redhat.com> - 9-1
- Version 9 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 8-2
- Perl 5.18 rebuild

* Mon May 27 2013 Petr Pisar <ppisar@redhat.com> - 8-1
- Version 8 bump

* Thu May 16 2013 Petr Pisar <ppisar@redhat.com> - 7-1
- Version 7 bump

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 16 2012 Petr Pisar <ppisar@redhat.com> - 6-2
- Add empty %%build section for hooks

* Fri Oct 12 2012 Petr Pisar <ppisar@redhat.com> - 6-1
- Initial spec file
