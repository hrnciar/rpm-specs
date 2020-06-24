# spec file for package nodejs-nodejs-realize-package-specifier

%global npm_name realize-package-specifier
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		nodejs-realize-package-specifier
Version:	3.0.1
Release:	11%{?dist}
Summary:	Producing full file paths and differentiating local tar and directory sources
Url:		https://github.com/npm/realize-package-specifier
Source0:	http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	ISC
BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:	nodejs-devel
BuildRequires:	nodejs-packaging

%if 0%{?enable_tests}
BuildRequires: npm(require-inject)
BuildRequires:	npm(tap)
%endif

BuildRequires:	npm(dezalgo)
BuildRequires:	npm(npm-package-arg)

%description
Producing full file paths and differentiating local tar and directory sources

%prep
%setup -q -n package

%{nodejs_fixdep} require-inject --dev
%{nodejs_fixdep} tap --dev

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
%{nodejs_sitelib}/realize-package-specifier
%doc README.md
%license LICENSE

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 24 2016 Jared Smith <jsmith@fedoraproject.org> - 3.0.1-4
- Bump release and rebuild so that PPC/AArch64 can build with updated value for
  nodejs_arches macro

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 14 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.1-2
- Enable nodejs-require-inject dependency
- add --dev to testing dependencies

* Thu Jun 25 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.1-1
- New upstream release

* Thu May 14 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.0-1
- Initial build
