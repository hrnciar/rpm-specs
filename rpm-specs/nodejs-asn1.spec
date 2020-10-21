%{?nodejs_find_provides_and_requires}

Name:           nodejs-asn1
Version:        0.2.3
Release:        3%{?dist}
Summary:        Contains parsers and serializers for ASN.1 (currently BER only)

License:        MIT
URL:            https://github.com/mcavage/node-asn1
Source0:        https://registry.npmjs.org/asn1/-/asn1-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging
BuildRequires:  npm(tap)

%description
nodejs-asn1 is a library for encoding and decoding Abstract Syntax Notation One
(ASN.1) datatypes in pure JavaScript. ASN.1 is  is a standard and notation that 
describes rules and structures for representing, encoding, transmitting, and 
decoding data in telecommunications and computer networking.

Currently Basic Encoding Rules (BER) encoding is supported; at some point 
Distinguished Encoding Rules (DER) will likely also be supported.

%prep
%setup -q -n package

%build
# Nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/asn1
cp -pr package.json lib %{buildroot}%{nodejs_sitelib}/asn1

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%tap tst/ber/*.js

%files
%{nodejs_sitelib}/asn1
%doc README.md
%license LICENSE

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.3-1
- Update to latest upstream release 0.2.3

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 07 2016 Piotr Popieluch <piotr1212@gmail.com> - 0.1.11-8
- Cleanup spec for newer guidelines

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.11-3
- restrict to compatible arches

* Fri Jun 21 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.11-2
- improve description

* Thu Jun 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.11-1
- initial package
