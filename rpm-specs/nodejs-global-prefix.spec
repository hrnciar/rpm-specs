%{?nodejs_find_provides_and_requires}

%global packagename global-prefix
%global enable_tests 1

Name:		nodejs-global-prefix
Version:	1.0.2
Release:	6%{?dist}
Summary:	Get the npm global path prefix

License:	MIT
URL:		https://github.com/jonschlinkert/global-prefix.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
# Also, the 0.1.4 release has not yet been tagged in github
Source1:	https://raw.githubusercontent.com/jonschlinkert/global-prefix/%{version}/test.js
# Fix the path in the tests, as the test defaults to /usr/local instead of /usr
Patch0:		nodejs-global-prefix_fix-test-path.patch


BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
BuildRequires:	npm(expand-tilde)
BuildRequires:	npm(osenv)
BuildRequires:	npm(ini)
BuildRequires:	npm(is-windows)
BuildRequires:	npm(which)

%if 0%{?enable_tests}
BuildRequires:	mocha
%endif

%description
Get the npm global path prefix.


%prep
%setup -q -n package
# setup the tests
cp -p %{SOURCE1} .
# patch the test
#%patch0 -p1


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
NODE_ENV=test %{_bindir}/mocha -R spec
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%{!?_licensedir:%global license %doc}
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
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

* Tue Sep 19 2017 Jared Smith <jsmith@fedoraproject.org> - 1.0.2-1
- Update to upstream 1.0.2 release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Aug 06 2016 Jared Smith <jsmith@fedoraproject.org> - 0.1.4-2
- Remove trailing dot from Summary

* Mon Jul 25 2016 Jared Smith <jsmith@fedoraproject.org> - 0.1.4-1
- Initial packaging
