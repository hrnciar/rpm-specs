%{?nodejs_find_provides_and_requires}

%global packagename tippex
%global enable_tests 1

Name:		nodejs-tippex
Version:	3.0.0
Release:	8%{?dist}
Summary:	Find and erase strings and comments in JavaScript code

License:	MIT
URL:		https://github.com/Rich-Harris/tippex.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
# Source{1-9} are generated by running Source10, which pulls from the upstream
# version control repository.
Source1:	tests-%{version}.tar.bz2
Source10:	dl-tests.sh
# Rollup config
Source11:	https://raw.githubusercontent.com/Rich-Harris/tippex/v%{version}/rollup.config.js


BuildArch:	noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:	dos2unix
BuildRequires:	nodejs-packaging
BuildRequires:	npm(rollup)
BuildRequires:	npm(rollup-plugin-buble)
BuildRequires:	npm(rollup-plugin-node-resolve)

%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(locate-character)
BuildRequires:	npm(console-group)
BuildRequires:	npm(source-map-support)
%endif

%description
Find and erase strings and comments in JavaScript code


%prep
%autosetup -n package
# setup the tests
%autosetup -T -D -a 1 -n package
cp -p %{SOURCE11} .

dos2unix *.md

%build
%nodejs_symlink_deps --build
rollup -i src/index.js -f es -o dist/tippex.es.js -e locate-character
rollup -i src/index.js -f umd -n tippex -o dist/tippex.es.js -e locate-character
rm -rf node_modules


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
%{nodejs_sitelib}/%{packagename}

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 01 2018 Jared K. Smith <jsmith@fedoraproject.org> - 3.0.0-2
- Change build to avoid problem in buble plugin

* Thu May 31 2018 Jared K. Smith <jsmith@fedoraproject.org> - 3.0.0-1
- Initial packaging
