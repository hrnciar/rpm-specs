# spec file for package nodejs-nodejs-validate-npm-package-name

%global npm_name validate-npm-package-name
%global commit 3af92c881549f1b96f05ab6bfb5768bba94ad72d
%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:		nodejs-validate-npm-package-name
Version:	2.2.2
Release:	10%{?dist}
Summary:	Give me a string and I'll tell you if it's a valid npm package name
Url:		https://github.com/npm/validate-npm-package-name
Source0:	https://github.com/npm/%{npm_name}/archive/%{commit}/%{npm_name}-%{commit}.tar.gz
License:	ISC

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:	nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:	npm(tap)
%endif

BuildRequires:	npm(builtins)

%description
Give me a string and I'll tell you if it's a valid npm package name

%prep
%setup -q -n %{npm_name}-%{commit}

%nodejs_fixdep builtins

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
tap test/*.js
%endif

%files
%{nodejs_sitelib}/validate-npm-package-name

%doc README.md
%license LICENSE

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.2.2-2
- Add nodejs_fixdep macro

* Tue Jun 30 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.2.2-1
- Initial build
