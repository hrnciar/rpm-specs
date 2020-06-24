%{?nodejs_find_provides_and_requires}

%global packagename log-utils
%global enable_tests 1

Name:		nodejs-log-utils
Version:	0.2.1
Release:	6%{?dist}
Summary:	Basic logging utils: colors, symbols and timestamp

License:	MIT
URL:		https://github.com/jonschlinkert/log-utils
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
Source1:	https://raw.githubusercontent.com/jonschlinkert/log-utils/master/test.js
# README file too
Source2:	https://raw.githubusercontent.com/jonschlinkert/log-utils/master/README.md


ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(ansi-colors)
BuildRequires:	npm(log-ok)
%if 0%{?enable_tests}
BuildRequires:	mocha
%endif

%description
Basic logging utils: colors, symbols and timestamp.


%prep
%autosetup -n package
# setup the tests and readme file
cp -p %{SOURCE1} .
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
%{_bindir}/mocha -R spec
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Apr 14 2017 Jared Smith <jsmith@fedoraproject.org> - 0.2.1-1
- Initial packaging