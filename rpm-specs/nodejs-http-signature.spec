%global commit 8881c4a806604deabe958f37e51672a65ef150fe
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           nodejs-http-signature
Version:        0.10.0
Release:        16%{?dist}
Summary:        Reference implementation of Joyent's HTTP Signature Scheme
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

License:        MIT
URL:            https://github.com/joyent/node-http-signature
Source0:        https://registry.npmjs.org/http-signature/-/http-signature-%{version}.tgz
#grab the tests from github
Source1:        https://github.com/joyent/node-http-signature/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires:  nodejs-packaging

#for tests
BuildRequires:  npm(tap)
BuildRequires:  npm(node-uuid)
BuildRequires:  npm(assert-plus)
BuildRequires:  npm(asn1)
BuildRequires:  npm(ctype)

%description
nodejs-http-signature is a node.js library that has client and server components 
for Joyent's HTTP Signature Scheme.

%prep
%setup -q -n package -a1

%nodejs_fixdep assert-plus
%nodejs_fixdep ctype '~0.5.3'
%nodejs_fixdep asn1 '~0.1.11'

#move tests into regular directory
mv node-http-signature-%{commit}/test .
rm -rf node-http-signature-%{commit}

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/http-signature
cp -pr package.json lib %{buildroot}%{nodejs_sitelib}/http-signature

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%tap test/*.js

%files
%{nodejs_sitelib}/http-signature
%doc README.md http_signing.md
%license LICENSE

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 28 2016 Piotr Popieluch <piotr1212@gmail.com> - - 0.10.0-9
- fixdep assert-plus

* Sun Feb 07 2016 Piotr Popieluch <piotr1212@gmail.com> - 0.10.0-8
- cleanup spec

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.0-3
- restrict to compatible arches

* Fri Jun 21 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.0-2
- grab tests from GitHub
- relax dependency on npm(asn1)

* Thu Jun 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.0-1
- initial package
