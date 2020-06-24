%{?nodejs_find_provides_and_requires}

%global packagename globby
%global enable_tests 1

Name:		nodejs-globby
Version:	4.0.0
Release:	11%{?dist}
Summary:	Extends `glob` with support for multiple patterns and exposes a Promise API

License:	MIT
URL:		https://github.com/sindresorhus/globby
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
Source1:	https://raw.githubusercontent.com/sindresorhus/globby/v%{version}/test.js

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(array-union)
BuildRequires:	npm(arrify)
BuildRequires:	npm(glob)
BuildRequires:	npm(object-assign)
BuildRequires:	npm(pify)
BuildRequires:	npm(pinkie-promise)
%endif

%description
Extends `glob` with support for multiple patterns and exposes a Promise API


%prep
%setup -q -n package
# setup the tests
cp -p %{SOURCE1} .
%nodejs_fixdep array-union "^2.1.0"
%nodejs_fixdep arrify "^2.0.1"


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
%{_bindir}/echo "Tests disabled..."
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license license
%{nodejs_sitelib}/%{packagename}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May  1 2019 Tom Hughes <tom@compton.nu> - 4.0.0-9
- Update npm(arrify) dependency

* Mon Apr 22 2019 Tom Hughes <tom@compton.nu> - 4.0.0-8
- Update npm(array-union) dependency

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 08 2016 Jared Smith <jsmith@fedoraproject.org> - 4.0.0-2
- Remove test.js from package
- Don't include the license separately, as it was already in the npm tarball

* Wed Feb  3 2016 Jared Smith <jsmith@fedoraproject.org> - 4.0.0-1
- Initial packaging
