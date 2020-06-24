%{?nodejs_find_provides_and_requires}

%global packagename to-regex
%global enable_tests 1

Name:		nodejs-to-regex
Version:	3.0.2
Release:	5%{?dist}
Summary:	Generate a regex from a string or array of strings

License:	MIT
URL:		https://github.com/jonschlinkert/to-regex
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
Source1:	https://raw.githubusercontent.com/jonschlinkert/to-regex/3.0.1/test.js


ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(define-property)
BuildRequires:	npm(regex-not)
BuildRequires:	npm(safe-regex)
%if 0%{?enable_tests}
BuildRequires:	mocha
%endif

%description
Generate a regex from a string or array of strings.


%prep
%autosetup -n package
# setup the tests
cp -p %{SOURCE1} .

%nodejs_fixdep define-property
%nodejs_fixdep extend-shallow

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 20 2018 Jared K. Smith <jsmith@fedoraproject.org> - 3.0.2-1
- Update to upstream 3.0.2 release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 18 2017 Jared Smith <jsmith@fedoraproject.org> - 3.0.1-2
- Relax dependency on npm(define-property)

* Fri Apr 14 2017 Jared Smith <jsmith@fedoraproject.org> - 3.0.1-1
- Initial packaging
