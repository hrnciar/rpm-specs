%{?nodejs_find_provides_and_requires}

%global commit 74a42f06087891273274acf2e30065ee9454bd66

%global enable_tests 1

Name:       nodejs-css-stringify
Version:    1.4.1
Release:    12%{?dist}
Summary:    A CSS compiler for Node.js
License:    MIT
URL:        https://github.com/visionmedia/css-stringify
# Use GitHub as the NPM tarball is missing useful files/folders.
Source0:    https://github.com/visionmedia/css-stringify/archive/%{commit}/%{name}-%{version}.tar.gz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  mocha
BuildRequires:  npm(css-parse)
BuildRequires:  npm(should)
BuildRequires:  npm(source-map)
%endif

%description
%{summary}.


%prep
%setup -q -n css-stringify-%{commit}
%nodejs_fixdep source-map "^0.5.2"


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/css-stringify
cp -pr package.json index.js lib/ \
    %{buildroot}%{nodejs_sitelib}/css-stringify

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
/usr/bin/mocha --require should --reporter spec --bail
%endif


%files
%doc History.md Readme.md examples/
%license LICENSE
%{nodejs_sitelib}/css-stringify


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 10 2016 Tom Hughes <tom@compton.nu> - 1.4.1-5
- Update npm(source-map) dependency

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 02 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.4.1-1
- initial package
