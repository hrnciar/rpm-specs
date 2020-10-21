%{?nodejs_find_provides_and_requires}

%global packagename log-driver
%global enable_tests 1

Name:		nodejs-log-driver
Version:	1.2.5
Release:	11%{?dist}
Summary:	A simple logging framework for logging to stdout

License:	ISC
URL:		https://github.com/cainus/logdriver.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# releases aren't tagged in github, so pull the test from master
Source1:	https://raw.githubusercontent.com/cainus/logdriver/master/test/index.js
# license file is in upstream master branch, but not yet in a release tarball
Source2:	https://raw.githubusercontent.com/cainus/logdriver/master/LICENSE
# fix testing syntax
Patch0:		nodejs-log-driver_fix-test-syntax.patch

ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(should)
BuildRequires:	npm(sinon-restore)
%endif

Requires:	nodejs

%description
A simple logging framework for logging to stdout


%prep
%setup -q -n package
# test file
mkdir test
cp -p %{SOURCE1} test/
cp -p %{SOURCE2} .

%patch0 -p1

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
/usr/bin/mocha -R spec
%endif


%files
%{!?_licensedir:%global license %doc}
%license LICENSE
%doc *.md
%{nodejs_sitelib}/%{packagename}



%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Aug 06 2016 Jared Smith <jsmith@fedoraproject.org> - 1.2.5-2
- Add LICENSE file from upstream master

* Thu Oct 15 2015 Jared Smith <jsmith@fedoraproject.org> - 1.2.5-1
- Initial packaging
