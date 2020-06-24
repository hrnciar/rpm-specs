%{?nodejs_find_provides_and_requires}

%global packagename snapdragon
%global enable_tests 1

Name:		nodejs-snapdragon
Version:	0.12.0
Release:	5%{?dist}
Summary:	Easy-to-use plugin system for parsers and compilers

License:	MIT
URL:		https://github.com/jonschlinkert/snapdragon
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
# Source1 is generated by running Source10, which pulls from the upstream
# version control repository.
Source1:	tests-%{version}.tar.bz2
Source2:	docs-%{version}.tar.bz2
Source3:	examples-%{version}.tar.bz2
Source4:	support-%{version}.tar.bz2
Source10:	dl-tests.sh

# Patch to fix syntax of snapdragon-node v2 -- which moved from ast.pushNode to
# ast.push syntax
Patch0:		snapdragon_fix-snapdragon-node-syntax.patch


ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(component-emitter)
BuildRequires:	npm(debug)
BuildRequires:	npm(define-property)
BuildRequires:	npm(extend-shallow)
BuildRequires:	npm(get-value)
BuildRequires:	npm(map-cache)
BuildRequires:	npm(snapdragon-node)
BuildRequires:	npm(snapdragon-util)
BuildRequires:	npm(use)

%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(isobject)
BuildRequires:	npm(mocha)
BuildRequires:	npm(snapdragon-capture)
BuildRequires:	npm(snapdragon-capture-set)
%endif

%description
Easy-to-use plugin system for creating powerful, fast and versatile parsers and
compilers, with built-in source-map support.


%prep
%setup -q -n package
# setup the tests
%setup -q -T -D -a 1 -n package
%setup -q -T -D -a 2 -n package
%setup -q -T -D -a 3 -n package
%setup -q -T -D -a 4 -n package
# Apply patches
%patch0 -p1

%nodejs_fixdep debug
%nodejs_fixdep extend-shallow '^2.0.1'
%nodejs_fixdep isobject
%nodejs_fixdep use
%nodejs_fixdep define-property
%nodejs_fixdep snapdragon-node
%nodejs_fixdep snapdragon-util

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
%doc README.md examples/ docs/
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 18 2018 Jared K. Smith <jsmith@fedoraproject.org> - 0.12.0-1
- Update to upstream 0.12.0 release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 28 2017 Jared Smith <jsmith@fedoraproject.org> - 0.11.0-5
- Add patch to fix test syntax

* Fri Aug 18 2017 Jared Smith <jsmith@fedoraproject.org> - 0.11.0-4
- Relax dependency on npm(define-property)

* Mon Apr 17 2017 Jared Smith <jsmith@fedoraproject.org> - 0.11.0-3
- Relax dependency on npm(use)

* Fri Apr 14 2017 Jared Smith <jsmith@fedoraproject.org> - 0.11.0-2
- Relax dependencies on npm(isobject) and npm(debug)

* Fri Apr 14 2017 Jared Smith <jsmith@fedoraproject.org> - 0.11.0-1
- Initial packaging
