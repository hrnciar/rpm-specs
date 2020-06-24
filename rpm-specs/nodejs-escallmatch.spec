%{?nodejs_find_provides_and_requires}

%global packagename escallmatch

# Tests disabled due to the missing babel suite
%global enable_tests 0

Name:		nodejs-escallmatch
Version:	1.5.0
Release:	6%{?dist}
Summary:	ECMAScript CallExpression matcher made from function/method signature

License:	MIT
URL:		https://github.com/twada/escallmatch.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
Source1:	https://raw.githubusercontent.com/twada/escallmatch/master/LICENSE


BuildArch:	noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(array-filter)
BuildRequires:	npm(array-foreach)
BuildRequires:	npm(array-map)
BuildRequires:	npm(array-reduce)
BuildRequires:	npm(call-matcher)
BuildRequires:	npm(component-indexof)
BuildRequires:	npm(deep-equal)
BuildRequires:	npm(estraverse)
BuildRequires:	npm(esprima)
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(espurify)
%endif

%description
ECMAScript CallExpression matcher made from function/method signature


%prep
%setup -q -n package
cp -p %{SOURCE1} LICENSE

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
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}



%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Apr 19 2017 Jared Smith <jsmith@fedoraproject.org> - 1.5.0-1
- Update to upstream 1.5.0 release

* Mon Nov  9 2015 Jared Smith <jsmith@fedoraproject.org> - 1.4.2-1
- Initial packaging
