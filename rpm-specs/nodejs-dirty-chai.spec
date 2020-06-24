%{?nodejs_find_provides_and_requires}

%global packagename dirty-chai
%global enable_tests 1

Name:		nodejs-dirty-chai
Version:	2.0.1
Release:	5%{?dist}
Summary:	Extends Chai with lint-friendly terminating assertions

License:	MIT
URL:		https://github.com/prodatakey/dirty-chai
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# license file requested at https://github.com/prodatakey/dirty-chai/pull/35
Source1:	LICENSE-MIT.txt


BuildArch:	noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:	nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(chai)
BuildRequires:	npm(chai-as-promised)
BuildRequires:	npm(es6-promise)
BuildRequires:	npm(require-uncached)
%endif

%description
Extends Chai with lint-friendly terminating assertions.


%prep
%autosetup -n package
cp -p %{SOURCE1} .

%build
# nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json lib/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
NODE_ENV=test %{_bindir}/mocha -R spec
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc *.md
%license LICENSE-MIT.txt
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 24 2018 Jared K. Smith <jsmith@fedoraproject.org> - 2.0.1-1
- Initial packaging
