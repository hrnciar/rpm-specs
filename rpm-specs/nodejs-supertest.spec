%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:       nodejs-supertest
Version:    0.11.0
Release:    12%{?dist}
Summary:    A superagent driven library for testing HTTP servers
License:    MIT
URL:        https://github.com/visionmedia/supertest
Source0:    http://registry.npmjs.org/supertest/-/supertest-%{version}.tgz

BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(methods)
BuildRequires:  npm(superagent)

%if 0%{?enable_tests}
BuildRequires:  npm(express)
BuildRequires:  npm(mocha)
BuildRequires:  npm(should)
%endif

%description
This module provides a high-level abstraction for testing HTTP servers,
while still allowing you to drop down to the lower-level API provided by
superagent.


%prep
%setup -q -n package

%nodejs_fixdep superagent '~0.17.0'
%nodejs_fixdep methods


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/supertest
cp -pr package.json index.js lib/ \
    %{buildroot}%{nodejs_sitelib}/supertest

%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'

%if 0%{?enable_tests}
NODE_TLS_REJECT_UNAUTHORIZED=0 /usr/bin/mocha --require should --reporter spec
%endif


%files
%doc example.js History.md Readme.md
%license LICENSE
%{nodejs_sitelib}/supertest


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 30 2017 Piotr Popieluch <piotr1212@gmail.com> - 0.11.0-6
- Fixdep methods
- Update spec

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.11.0-1
- update to upstream release 0.11.0

* Mon Mar 10 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.9.0-1
- initial package
