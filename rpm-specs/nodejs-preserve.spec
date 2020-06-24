%{?nodejs_find_provides_and_requires}

%global packagename preserve

# Disable tests because of dependency on js-beautify, which depends
# on jshint, which has a disallowed license
%global enable_tests 0

Name:		nodejs-preserve
Version:	0.2.0
Release:	8%{?dist}
Summary:	Substitute tokens in the given `string` , then put them back

License:	MIT
URL:		https://github.com/jonschlinkert/preserve.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

# Disable one of the tests, as it's depending on old funcionality in js-beautify
# that has since been fixed.  Running the test fails because js-beautify is now
# smarter about the way it does things.
Patch0:		nodejs-preserve_disable-test.patch

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(should)
BuildRequires:	npm(js-beautify)
%endif

%description
Temporarily substitute tokens in the given `string` with placeholders, then
put them back after transforming the string.


%prep
%setup -q -n package

%patch0 -p1

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
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Aug 15 2016 Jared Smith <jsmith@fedoraproject.org> - 0.2.0-2
- Disable tests to remove dependency on npm(js-beautify) and jshint

* Mon Feb  8 2016 Jared Smith <jsmith@fedoraproject.org> - 0.2.0-1
- Initial packaging
