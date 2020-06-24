%global _hardened_build 1

Summary: DNS and DNSSEC zone file validator
Name: validns
Version: 0.8
Release: 14%{?dist}
License: BSD
Url:  http://www.validns.net/
Source: http://www.validns.net/download/%{name}-%{version}.tar.gz
Patch1: validns-0.8-timing.patch
Patch2: validns-0.8-Wformat-truncation.patch
BuildRequires:  gcc
BuildRequires: Judy-devel, compat-openssl10-devel

%description
DNS and DNSSEC zone file validator. It comes with no man page and no
useful README or information, but it's a nice tool anyway :)

%prep
%autosetup -p1
#%setup -q 
#%patch1 -p1 -b .timing
#%patch2 -p1 -b .Wformat-truncation.patch

%build
%make_build
gzip validns.1

%install
mkdir -p %{buildroot}/%{_bindir} %{buildroot}/%{_mandir}/man1/
install -m 755 validns %{buildroot}/%{_bindir}/
cp -a validns.1.gz %{buildroot}/%{_mandir}/man1/

%files 
%doc LICENSE README
%{_bindir}/validns
%{_mandir}/man1/validns.1.gz

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 11 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.8-10
- Fix FTBFS on rawhide, use compat-openssl10-devel until upstream port to 1.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 11 2014 Paul Wouters <pwouters@redhat.com> - 0.8-1
- Updated to 0.8 for sha-384 support in DS records

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 16 2013 Paul Wouters <pwouters@redhat.com> - 0.7-1
- Updated to 0.7.
- Removed some el-5 only spec attributes

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 12 2012 Paul Wouters <pwouters@redhat.com> - 0.6-2
- Added -x option to skip timing info in statistics

* Thu Oct 04 2012 Paul Wouters <pwouters@redhat.com> - 0.6-1
- Updated to 0.6, which incorporates all patches

* Thu Oct 04 2012 Paul Wouters <pwouters@redhat.com> - 0.5-4
- Pullup from git for NSEC3 glue record handling fix

* Fri Aug 24 2012 Paul Wouters <pwouters@redhat.com> - 0.5-3
- Patch for handling NSEC/NSEC3 camelcasing
- Support TLSA records

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Paul Wouters <pwouters@redhat.com> - 0.5-1
- Updated to 0.5 which supports Parallelize signature verification
- Install man page

* Tue May 01 2012 Paul Wouters <pwouters@redhat.com> - 0.4-1
- Updated to 0.4 which fixes a TXT record parsing bug

* Tue Feb 28 2012 Paul Wouters <pwouters@redhat.com> - 0.3-2
- Added missing BuildRequire for openssl-devel

* Mon Feb 13 2012 Paul Wouters <pwouters@redhat.com> - 0.3-1
- Initial package

