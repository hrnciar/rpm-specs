%{?nodejs_find_provides_and_requires}

%global enable_tests 1
%global npm_name npm-install-checks

Name:		nodejs-npm-install-checks
Version:	3.0.0
Release:	9%{?dist}
Summary:	Checks that npm runs during the installation of a module
License:	BSD
Url:		https://github.com/npm/npm-install-checks
Source:		https://registry.npmjs.org/npm-install-checks/-/npm-install-checks-%{version}.tgz
BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:	nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:	npm(tap)
BuildRequires:	npm(rimraf)
BuildRequires:	npm(mkdirp)
BuildRequires:	npm(npmlog)
Buildrequires:	npm(semver)
%endif

Requires:       npm(semver) >= 2.3.0, npm(semver) < 6

%description
A package that contains checks that npm runs during the installation. 


%prep
%setup -q -n package


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}
%{nodejs_symlink_deps}


%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%tap test/*.js
%endif


%files
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitelib}/%{npm_name}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 17 2016 Tom Hughes <tom@compton.nu> - 3.0.0-1
- Update to 3.0.0 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.5-1
- New upstream release
- fixed typo in %%check
- added BuildRequires for dependencies
- removed scl prefixes
- changed Summary to match package.json

* Fri Mar 20 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.4-5
- Changed versions of packages fixed by %%nodejs_fixdep macros
- moved macros from %%build to %%prep
- changed license to BSD

* Mon Mar 16 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.4-4
- Changed ExclusiveArch
- added %%check, %%license and %%nodejs_fixdep macro
- removed BuildRoot, Group and %%defattr

* Tue Mar 03 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.4-3
- Fixed dependency

* Tue Jan 13 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.4-2
- Remove undefined macro

* Mon Jan 12 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.4-1
- Initial build

