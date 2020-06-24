%{?nodejs_find_provides_and_requires}

%global packagename is-registered
%global enable_tests 1

Name:		nodejs-is-registered
Version:	0.1.5
Release:	8%{?dist}
Summary:	Optionally prevents a plugin from being registered more than once

License:	MIT
URL:		https://github.com/node-base/is-registered
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
Source1:	https://raw.githubusercontent.com/node-base/%{packagename}/master/test.js
Source2:	https://raw.githubusercontent.com/node-base/%{packagename}/master/README.md

ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(define-property)
BuildRequires:	npm(isobject)
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(base)
%endif

%description
Util for Base that optionally prevents a plugin from being registered more than
once on an instance


%prep
%autosetup -n package
# setup the tests and readme
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .

%nodejs_fixdep isobject
%nodejs_fixdep define-property

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/mocha -R spec
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 18 2017 Jared Smith <jsmith@fedoraproject.org> - 0.1.5-3
- Relax dependency on npm(define-property)

* Wed May 10 2017 Jared Smith <jsmith@fedoraproject.org> - 0.1.5-2
- Relax dependency on npm(isobject)

* Sat Apr 15 2017 Jared Smith <jsmith@fedoraproject.org> - 0.1.5-1
- Initial packaging
