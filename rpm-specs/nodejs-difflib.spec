%{?nodejs_find_provides_and_requires}

%global packagename difflib
%global enable_tests 1

Name:		nodejs-difflib
Version:	0.2.4
Release:	12%{?dist}
Summary:	Text diff library ported from Python's difflib module

License:	Python
# License text is at the bottom of README.md
URL:		https://github.com/qiao/difflib.js.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

Patch0:		difflib-0.2.4-fix-test-keywords.patch
# coffee-script no longer exports a "RESERVED" array of reserved keywords, so
# for now we'll manually copy that list of words into the test.  So much work
# for such a silly little test, but it holds true to the original intent.

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:	coffee-script
BuildRequires:	mocha
BuildRequires:	npm(heap)
BuildRequires:	npm(should)
%endif

%description
Text diff library ported from Python's difflib module


%prep
%setup -q -n package
%patch0 -p1

# remove pre-compiled version
rm lib/difflib.js

%nodejs_fixdep heap '^0.2.0'

%build
%{_bindir}/coffee -c -b -o lib/ src/difflib.coffee

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js lib/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%{_bindir}/coffee -c -b test/*.coffee
%{_bindir}/mocha --require should -R spec --ui qunit
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license README.md
# license is at the bottom of README.md, so include it in both docs and license
%{nodejs_sitelib}/%{packagename}



%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 16 2015 Jared Smith <jsmith@fedoraproject.org> - 0.2.4-2
- Initial packaging
