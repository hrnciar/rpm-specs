%{?nodejs_find_provides_and_requires}

%global packagename is-regexp
%global enable_tests 1

Name:		nodejs-is-regexp
Version:	1.0.0
Release:	10%{?dist}
Summary:	Check whether a variable is a regular expression

License:	MIT
URL:		https://github.com/sindresorhus/is-regexp
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
Source1:	https://raw.githubusercontent.com/sindresorhus/is-regexp/master/license
# The license file was added after the 1.0.0 release
Source2:	https://raw.githubusercontent.com/sindresorhus/is-regexp/master/test.js
# The test file was added after the 1.0.0 release


ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:	mocha
%endif

Requires:	nodejs

%description
Check whether a variable is a regular expression


%prep
%setup -q -n package
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .


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
%doc *.md
%license license
%{nodejs_sitelib}/%{packagename}



%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 23 2015 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-2
- Enable tests and add upstream license file

* Thu Oct 15 2015 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-1
- Initial packaging
