%{?nodejs_find_provides_and_requires}

%global packagename ebnf-parser
%global enable_tests 0
%global bootstrap 1

Name:		nodejs-ebnf-parser
Version:	0.1.10
Release:	9%{?dist}
Summary:	A parser for BNF and EBNF grammars used by jison

License:	MIT
URL:		https://github.com/zaach/ebnf-parser.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
Source1:	LICENSE-MIT.txt
# upstream license file requeset at https://github.com/zaach/ebnf-parser/issues/9

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging

%if !0%{?bootstrap}
BuildRequires:	npm(jison)
%endif

%if 0%{?enable_tests}
BuildRequires:	npm(jison)
BuildRequires:	npm(lex-parser)
%endif

Requires:	nodejs

%description
A parser for BNF and EBNF grammars used by jison


%prep
%setup -q -n package
cp -p %{SOURCE1} .
%nodejs_fixdep --dev -r lex-parser
%nodejs_fixdep lex-parser '0.1.x'


%build
%if !0%{?bootstrap}
%{_bindir}/jison bnf.y bnf.l
mv bnf.js parser.js
%{_bindir}/jison ebnf.y
mv ebnf.js transform-parser.js
%endif

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{__nodejs} tests/all-tests.js
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE-MIT.txt
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 24 2015 Jared Smith <jsmith@fedoraproject.org> - 0.1.10-1
- Initial packaging
- Turn on bootstrap mode for building npm(jison)
