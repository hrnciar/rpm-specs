%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:       nodejs-basic-auth-connect
Version:    1.0.0
Release:    11%{?dist}
Summary:    Basic authentication middleware for Node.js and Connect
License:    MIT
URL:        https://github.com/expressjs/basic-auth-connect
Source0:    http://registry.npmjs.org/basic-auth-connect/-/basic-auth-connect-%{version}.tgz
# This test file is not included in the NPM tarball.
Source1:    https://raw.github.com/expressjs/basic-auth-connect/7a0b814741446933cf78a303fd269b4f54d74f12/test.js

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  mocha
BuildRequires:  npm(connect)
BuildRequires:  npm(should)
BuildRequires:  npm(supertest)
%endif

%description
%{summary}.


%prep
%setup -q -n package
cp -p %{SOURCE1} .


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/basic-auth-connect
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/basic-auth-connect

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
NODE_ENV=test /usr/bin/mocha --require should --reporter spec
%endif


%files
%doc README.md
%{nodejs_sitelib}/basic-auth-connect


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 08 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.0-1
- initial package
