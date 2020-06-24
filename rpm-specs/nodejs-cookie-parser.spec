%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:       nodejs-cookie-parser
Version:    1.4.3
Release:    7%{?dist}
Summary:    A Node.js module for cookie parsing with signatures
License:    MIT
URL:        https://github.com/expressjs/cookie-parser
Source0:    https://github.com/expressjs/cookie-parser/archive/%{version}/cookie-parser-%{version}.tar.gz

BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(cookie)
BuildRequires:  npm(cookie-signature)

%if 0%{?enable_tests}
BuildRequires:  mocha
BuildRequires:  npm(supertest)
%endif

%description
Parse Cookie header and populate req.cookies with an object keyed by the
cookie names. Optionally you may enabled signed cookie support by passing a
secret string, which assigns req.secret so it may be used by other middleware.


%prep
%autosetup -n cookie-parser-%{version}
%nodejs_fixdep cookie '0.x'
%nodejs_fixdep cookie-signature '1.x'


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/cookie-parser
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/cookie-parser

%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'

%if 0%{?enable_tests}
mocha --reporter spec --bail --check-leaks test/
%endif


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/cookie-parser


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 30 2017 Piotr Popieluch <piotr1212@gmail.com> - 1.4.3-1
- Update to 1.4.3

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 12 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.1-4
- upstream have merged the pull request, so now use upstream's copy of
  the LICENSE

* Wed Mar 12 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.1-3
- fix inclusion of LICENSE

* Wed Mar 12 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.1-2
- add copy of the MIT license

* Sat Mar 08 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.1-1
- initial package
