%{?nodejs_find_provides_and_requires}

%global packagename conventional-commits-parser

# tests run fine manually, but fail in mock
%global enable_tests 0

Name:		nodejs-conventional-commits-parser
Version:	2.1.7
Release:	6%{?dist}
Summary:	Parse raw conventional commits

License:	MIT
URL:		https://github.com/conventional-changelog/conventional-commits-parser
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# Test files not in NPM tarball
# Source{1-9} are generated by running Source10, which pulls from the upstream
# version control repository.
Source1:	%{packagename}-tests-%{version}.tar.bz2
Source10:	dl-cc-tests.sh

ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(lodash)
BuildRequires:	npm(trim-off-newlines)
BuildRequires:	npm(through2)
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(chai)
BuildRequires:	npm(concat-stream)
BuildRequires:	npm(is-text-path)
BuildRequires:	npm(JSONStream)
BuildRequires:	npm(meow)
BuildRequires:	npm(split2)
%endif

%description
Parse raw conventional commits


%prep
%autosetup -n package -p1
# setup the tests
%setup -q -T -D -a 1 -n package


%nodejs_fixdep chai
%nodejs_fixdep lodash
%nodejs_fixdep mocha

sed -i '1s/env //' cli.js

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js lib/ \
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
%doc README.md CHANGELOG.md
%license LICENSE.md
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 29 2018 jsmith <jsmith.fedora@gmail.com> - 2.1.7-2
- Disable tests, as they fail in mock/koji

* Tue Mar 27 2018 jsmith <jsmith.fedora@gmail.com> - 2.1.7-1
- Update to upstream 2.1.7 release

* Wed Feb 21 2018 Jared Smith <jsmith@fedoraproject.org> - 2.1.4-1
- Update to upstream 2.1.4 release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat May  6 2017 Jared Smith <jsmith@fedoraproject.org> - 1.3.0-1
- Initial packaging