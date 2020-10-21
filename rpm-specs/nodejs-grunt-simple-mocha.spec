%{?nodejs_find_provides_and_requires}

%global packagename grunt-simple-mocha

# Tests disabled because they fail in mock, even if they pass locally
%global enable_tests 0

Name:		nodejs-grunt-simple-mocha
Version:	0.4.1
Release:	12%{?dist}
Summary:	A simple wrapper for running tests with Mocha

License:	MIT
URL:		https://github.com/yaymukund/grunt-simple-mocha.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# Fix a path in the test file
Patch0:		nodejs-grunt-simple-mocha_fix-tests.patch

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
BuildRequires:	mocha

%if 0%{?enable_tests}
BuildRequires:	npm(grunt)
BuildRequires:	npm(grunt-cli)
BuildRequires:	npm(grunt-contrib-jshint)
%endif

%description
A simple wrapper for running tests with Mocha.


%prep
%autosetup -n package -p1

# fix she-bang line in grunt-simple-mocha
sed -i '1!b;s/env node/node/' bin/grunt-simple-mocha

%build
# nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js bin/ tasks/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
ln -s %{nodejs_sitelib}/grunt-cli node_modules/grunt-cli
%if 0%{?enable_tests}
%{_bindir}/grunt
NODE_ENV=test %{_bindir}/mocha -R spec tests/acceptance-tests.js
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE-MIT
%{nodejs_sitelib}/%{packagename}

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 08 2016 Jared Smith <jsmith@fedoraproject.org> - 0.4.1-3
- Fix interpreter in bin/grunt-simple-mocha

* Mon Jul 25 2016 Jared Smith <jsmith@fedoraproject.org> - 0.4.1-2
- Do not forget the tasks/ directory

* Sat Jul 23 2016 Jared Smith <jsmith@fedoraproject.org> - 0.4.1-1
- Initial packaging
