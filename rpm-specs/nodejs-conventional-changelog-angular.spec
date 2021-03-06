%{?nodejs_find_provides_and_requires}

%global packagename conventional-changelog-angular

# tests disabled due to circular dependency on npm(conventional-changelog-core)
%global enable_tests 0

Name:		nodejs-conventional-changelog-angular
Version:	1.6.6
Release:	5%{?dist}
Summary:	A conventional-changelog angular preset

License:	ISC
URL:		https://github.com/conventional-changelog/conventional-changelog-angular
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# Test files not in NPM tarball
# Source{1-9} are generated by running Source10, which pulls from the upstream
# version control repository.
Source1:	%{packagename}-tests-%{version}.tar.bz2
Source10:	dl-cc-tests.sh

# License file
Source11:	https://raw.githubusercontent.com/conventional-changelog/conventional-changelog/master/packages/conventional-changelog-angular/LICENSE.md



ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(compare-func)
BuildRequires:	npm(github-url-from-git)
BuildRequires:	npm(q)
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(conventional-changelog-core)
%endif

%description
A conventional-changelog angular preset


%prep
%autosetup -n package
# setup the tests
%setup -q -T -D -a 1 -n package
# license
cp -p %{SOURCE11} .


%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js templates/ \
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
%doc *.md
%license LICENSE.md
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 29 2018 Jared Smith <jsmith@fedoraproject.org> - 1.6.6-1
- Update to upstream 1.6.6 release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 28 2017 Jared Smith <jsmith@fedoraproject.org> - 1.5.0-1
- Update to upstream 1.5.0 release

* Sun May  7 2017 Jared Smith <jsmith@fedoraproject.org> - 1.3.3-1
- Initial packaging
