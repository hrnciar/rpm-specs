%{?nodejs_find_provides_and_requires}

%global packagename rollup-plugin-node-resolve

# Tests disabled, as the tests require npm(rollup-plugin-commonjs), but it
# depends on this module
%global enable_tests 0

Name:		nodejs-rollup-plugin-node-resolve
Version:	3.3.0
Release:	5%{?dist}
Summary:	Bundle third-party dependencies in node_modules

License:	MIT
URL:		https://github.com/rollup/rollup-plugin-node-resolve.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
# Source{1-9} are generated by running Source10, which pulls from the upstream
# version control repository.
Source1:	tests-%{version}.tar.bz2
Source10:	dl-tests.sh
# license
Source11:	https://github.com/rollup/rollup/blob/master/LICENSE.md


BuildArch:	noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(builtin-modules)
BuildRequires:	npm(is-module)
BuildRequires:	npm(resolve)

%if 0%{?enable_tests}
BuildRequires:	mocha
%endif

%description
Bundle third-party dependencies in node_modules


%prep
%autosetup -n package
# setup the tests
%autosetup -T -D -a 1 -n package
cp -p %{SOURCE11} .

%nodejs_fixdep builtin-modules

%build
# nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json dist/ \
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
%license LICENSE.md
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Jared K. Smith <jsmith@fedoraproject.org> - 3.3.0-1
- Initial packaging
