# spec file for package nodejs-nodejs-npm-package-arg

%global npm_name npm-package-arg
%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:           nodejs-npm-package-arg
Version:        4.1.0
Release:        11%{?dist}
Summary:        Parse the things that can be arguments to `npm install`
Url:            https://github.com/npm/npm-package-arg
Source0:        http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:        ISC
BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:  nodejs-devel
BuildRequires:	nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(tap)
BuildRequires:  npm(hosted-git-info)
BuildRequires:  npm(semver) >= 4.0.0
%endif

%description
Parse the things that can be arguments to `npm install`

%prep
%setup -q -n package
%{nodejs_fixdep} tap
%{nodejs_fixdep} semver

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json npa.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
tap test/*.js
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%doc README.md
%license LICENSE

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Tom Hughes <tom@compton.nu> - 4.1.0-1
- Update to 4.1.0 upstream release
- Enable tests

* Wed Jun 17 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 4.0.1-1
- New upstream version

* Thu May 14 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 4.0.0-1
- Initial build
