%{?nodejs_find_provides_and_requires}

%global packagename conventional-changelog-writer

# Tests run fine locally, but fail in mock/koji
%global enable_tests 0

Name:		nodejs-conventional-changelog-writer
Version:	3.0.9
Release:	5%{?dist}
Summary:	Write logs based on conventional commits and templates

License:	MIT
URL:		https://github.com/conventional-changelog/conventional-changelog-writer
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# dl-cc-tests.sh is run to download the tests from GitHub
Source1:	%{packagename}-tests-%{version}.tar.bz2
Source2:	dl-cc-tests.sh


ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(compare-func)
BuildRequires:	npm(conventional-commits-filter)
BuildRequires:	npm(dateformat)
BuildRequires:	npm(handlebars)
BuildRequires:	npm(json-stringify-safe)
BuildRequires:	npm(lodash)
BuildRequires:	npm(semver)
BuildRequires:	npm(through2)
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(chai)
BuildRequires:	npm(compare-func)
BuildRequires:	npm(concat-stream)
BuildRequires:	npm(meow)
BuildRequires:	npm(should)
BuildRequires:	npm(split)
%endif

%description
Write logs based on conventional commits and templates


%prep
%autosetup -n package
# setup the tests
%setup -q -T -D -a 1 -n package

%nodejs_fixdep dateformat
%nodejs_fixdep lodash
%nodejs_fixdep semver '^5.3.0'

%if 0%{?enable_tests}
%nodejs_fixdep chai
%nodejs_fixdep mocha
%endif

sed -i '1s/env //' cli.js

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js lib/ templates/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/mocha -R spec --require should
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc README.md
%license LICENSE.md
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 30 2018 jsmith <jsmith.fedora@gmail.com> - 3.0.9-1
- Update to upstream 3.0.9 release

* Tue Mar 27 2018 jsmith <jsmith.fedora@gmail.com> - 3.0.8-1
- Update to upstream 3.0.8 release

* Tue Mar 06 2018 jsmith <jsmith.fedora@gmail.com> - 3.0.4-1
- Update to upstream 3.0.4 release

* Wed Feb 21 2018 Jared Smith <jsmith@fedoraproject.org> - 3.0.3-1
- Update to upstream 3.0.3 release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun May  7 2017 Jared Smith <jsmith@fedoraproject.org> - 1.4.1-1
- Initial packaging
