%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:           nodejs-detective
Version:        2.3.0
Release:        12%{?dist}
Summary:        Node.js module to find all calls to require()

License:        MIT
URL:            https://github.com/substack/node-detective
Source0:        http://registry.npmjs.org/detective/-/detective-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(escodegen)
BuildRequires:  npm(esprima)
BuildRequires:  npm(tap)
%endif

%description
Node.js module to find all calls to require(), no matter how crazily nested,
using a proper walk of the AST.

%prep
%autosetup -n package
%nodejs_fixdep esprima "^2.7.1"
%nodejs_fixdep escodegen "^1.3.2"


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/detective
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/detective
%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%tap test/*.js
%endif


%files
%{!?_licensedir:%global license %doc}
%doc readme.markdown example/
%license LICENSE
%{nodejs_sitelib}/detective


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 2.3.0-4
- Update npm(esprima) dependency

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 18 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.3.0-1
- update to upstream release 2.3.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.1.2-2
- enable tests

* Wed May 29 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.1.2-1
- update to upstream release 2.1.2

* Tue Feb 05 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.1-1
- initial package
