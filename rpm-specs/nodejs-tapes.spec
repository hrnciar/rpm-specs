%{?nodejs_find_provides_and_requires}

%global packagename tapes
%global enable_tests 1

Name:		nodejs-tapes
Version:	4.1.0
Release:	6%{?dist}
Summary:	A more robust tap-producing test harness for node and browsers

License:	MIT
URL:		https://github.com/scottcorgan/tapes
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
Source1:	https://raw.githubusercontent.com/scottcorgan/tapes/master/test/tapes.js
# License file requested upstream at https://github.com/scottcorgan/tapes/pull/17
Source2:	LICENSE

ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:	npm(async)
BuildRequires:	npm(tap)
BuildRequires:	npm(tape)
%endif

%description
A more robust tap-producing test harness for node and browsers. Adds
beforeEach, afterEach, etc.


%prep
%autosetup -n package
# setup the tests
mkdir test
cp -p %{SOURCE1} test/
# copy the license file
cp -p %{SOURCE2} .

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
ln -sf %{nodejs_sitelib}/tape node_modules/tape
%{_bindir}/tap test/tapes.js
./bin/tapes test/tapes.js
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Apr 19 2017 Jared Smith <jsmith@fedoraproject.org> - 4.1.0-1
- Initial packaging
