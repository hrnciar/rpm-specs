# RPM 4.8
%filter_from_requires /perl(-F)/d; /perl(-f)/d
%filter_setup
# RPM 4.9
%global __requires_exclude ^perl\\((-F|-f)\\)$

Summary:	Squid native log format (NLF) analyzer and report generator
Name:		calamaris
Version:	2.59
Release:	21%{?dist}
License:	GPLv2+
URL:		https://cord.de/calamaris-english
Source0:	https://cord.de/files/calamaris/%{name}-%{version}.tar.gz
Patch0:		calamaris-2.59-perl_512.patch
BuildArch:	noarch
BuildRequires:	perl-generators

%description
Calamaris parses the Squid Native Log and generates reports
about Peak-usage, Request-Methods, Status-reports of incoming
and outgoing requests, second and Top-level destinations,
content-types and performance.
 
%prep
%setup -q
%patch0 -p1 -b .perl_512

%build

%install
install -D -p -m 0755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D -p -m 0644 %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

# Convert everything to UTF-8
iconv -f iso-8859-1 -t utf-8 -o CHANGES.utf8 CHANGES
touch -r CHANGES CHANGES.utf8; mv -f CHANGES.utf8 CHANGES
iconv -f iso-8859-1 -t utf-8 -o EXAMPLES.utf8 EXAMPLES
touch -r EXAMPLES EXAMPLES.utf8; mv -f EXAMPLES.utf8 EXAMPLES

%files
%license COPYRIGHT
%doc CHANGES EXAMPLES README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.59-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.59-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.59-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.59-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.59-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.59-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.59-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.59-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.59-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.59-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Robert Scheck <robert@fedoraproject.org> 2.59-10
- Added patch to avoid warnings with perl >= 5.12 (#970990)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.59-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.59-8
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.59-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.59-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.59-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.59-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.59-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 2.59-2
- Rebuild against gcc 4.4 and rpm 4.6

* Thu Jul 24 2008 Robert Scheck <robert@fedoraproject.org> 2.59-1
- Upgrade to 2.59
- Initial spec file for Fedora and Red Hat Enterprise Linux
