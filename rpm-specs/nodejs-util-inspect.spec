%{?nodejs_find_provides_and_requires}

%global packagename util-inspect
%global enable_tests 1

Name:		nodejs-util-inspect
Version:	0.1.8
Release:	5%{?dist}
Summary:	A cross-browser node.js util.inspect module

License:	MIT
URL:		https://github.com/Automattic/util-inspect
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# License file requested at https://github.com/Automattic/util-inspect/pull/8
Source1:	LICENSE-MIT.md

BuildArch:	noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(array-map)
BuildRequires:	npm(array-reduce)
BuildRequires:	npm(foreach)
BuildRequires:	npm(isarray)
BuildRequires:	npm(indexof)
BuildRequires:	npm(json3)
BuildRequires:	npm(object-keys)

%if 0%{?enable_tests}
#BuildRequires:	
%endif

%description
A cross-browser node.js util.inspect module


%prep
%autosetup -n package
cp -p %{SOURCE1} .

%nodejs_fixdep foreach '^2.0.5'
%nodejs_fixdep json3 '^3.3.2'
%nodejs_fixdep object-keys '^1.0.11'

%build
# nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/echo -e "\e[102m -=#=- This module has no tests -=#=- \e[0m"
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc *.md
%license LICENSE-MIT.md
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Jared K. Smith <jsmith@fedoraproject.org> - 0.1.8-1
- Initial packaging
