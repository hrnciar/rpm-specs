%{?nodejs_find_provides_and_requires}

%global packagename bash-match
%global enable_tests 1

Name:		nodejs-bash-match
Version:	1.0.2
Release:	8%{?dist}
Summary:	Match strings using bash, does not work on windows

License:	MIT
URL:		https://github.com/jonschlinkert/bash-match
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
Source1:	https://raw.githubusercontent.com/jonschlinkert/%{packagename}/%{version}/test.js

ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(cross-spawn)
BuildRequires:	npm(extend-shallow)
BuildRequires:	npm(is-extglob)
BuildRequires:	npm(is-windows)
%if 0%{?enable_tests}
BuildRequires:	mocha
%endif

%description
Match strings using bash. Does not work on windows, and does not read from the
file system. This library requires that Bash 4.3 or higher is installed and is
mostly used for checking parity in unit tests.


%prep
%autosetup -n package
# setup the tests
cp -p %{SOURCE1} .

%nodejs_fixdep cross-spawn

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
%{_bindir}/mocha
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 26 2017 Jared Smith <jsmith@fedoraproject.org> - 1.0.2-1
- Update to upstream 1.0.2 release

* Wed Apr 19 2017 Jared Smith <jsmith@fedoraproject.org> - 0.2.0-1
- Initial packaging
