%{?nodejs_find_provides_and_requires}

%global packagename import-local

# tests disabled due to missing npm(ava) test suite
%global enable_tests 0

Name:		nodejs-import-local
Version:	1.0.0
Release:	5%{?dist}
Summary:	Let a globally installed package use a locally installed version of itself

License:	MIT
URL:		https://github.com/sindresorhus/import-local.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
Source1:	https://raw.githubusercontent.com/sindresorhus/import-local/v%{version}/test.js


BuildArch:	noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(pkg-dir)
BuildRequires:	npm(resolve-cwd)

%if 0%{?enable_tests}
BuildRequires:	npm(ava)
%endif

%description
Let a globally installed package use a locally installed version of itself if
available.


%prep
%autosetup -n package
# setup the tests
cp -p %{SOURCE1} .

%nodejs_fixdep pkg-dir '^1.0.0'

%build
# nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json index.js fixtures/ \
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
%doc *.md
%license license
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr  6 2018 Jared K. Smith <jsmith@fedoraproject.org> - 1.0.0-1
- Initial packaging
