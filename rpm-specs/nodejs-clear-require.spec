%{?nodejs_find_provides_and_requires}

%global packagename clear-require

# tests require npm(ava), which is not yet in Fedora
%global enable_tests 0

Name:		nodejs-clear-require
Version:	2.0.0
Release:	6%{?dist}
Summary:	Clear a module from the require cache

License:	MIT
URL:		https://github.com/sindresorhus/clear-require.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
Source1:	https://raw.githubusercontent.com/sindresorhus/clear-module/v%{version}/test.js
Source2:	https://raw.githubusercontent.com/sindresorhus/clear-module/v%{version}/fixture.js
Source3:	https://raw.githubusercontent.com/sindresorhus/clear-module/v%{version}/fixture-match.js


BuildArch:	noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(caller-path)
BuildRequires:	npm(resolve-from)

%if 0%{?enable_tests}
BuildRequires:	npm(ava)
%endif

%description
Clear a module from the require cache


%prep
%autosetup -n package
# setup the tests
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} .

%nodejs_fixdep resolve-from '^4.0.0'

%build
# nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
NODE_ENV=test %{_bindir}/ava
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc readme.md
%license license
%{nodejs_sitelib}/%{packagename}

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 18 2018 Jared K. Smith <jsmith@fedoraproject.org> - 2.0.0-1
- Initial packaging
