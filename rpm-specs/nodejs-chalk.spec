%{?nodejs_find_provides_and_requires}

# tests disabled because the ansi styling fails in mock
%global enable_tests 0

Name:       nodejs-chalk
Version:    1.1.3
Release:    9%{?dist}
Summary:    Terminal string styling done right
License:    MIT
URL:        https://github.com/sindresorhus/chalk
Source0:    http://registry.npmjs.org/chalk/-/chalk-%{version}.tgz
Source1:    https://raw.githubusercontent.com/chalk/chalk/v%{version}/test.js
Source2:    https://raw.githubusercontent.com/chalk/chalk/v%{version}/license

# Fix tests
Patch0:     chalk-fix-lack-of-dim.patch
# Disable failing tests
Patch1:     chalk-fix-tests.patch

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging
BuildRequires:  npm(ansi-styles)
BuildRequires:  npm(escape-string-regexp)
BuildRequires:  npm(has-ansi) >= 2.0.0
BuildRequires:  npm(has-color)
BuildRequires:  npm(strip-ansi)
BuildRequires:  npm(supports-color)

%if 0%{?enable_tests}
BuildRequires:  npm(mocha)
BuildRequires:  npm(require-uncached)
BuildRequires:  npm(semver)
%endif

%description
%{summary}.


%prep
%setup -q -n package
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .
%patch0 -p1
%patch1 -p1

%nodejs_fixdep has-color
%nodejs_fixdep ansi-styles '^2.0.0'
%nodejs_fixdep strip-ansi
%nodejs_fixdep supports-color


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/chalk
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/chalk

%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
ln -s %{nodejs_sitelib}/tape node_modules/tape
%{_bindir}/mocha -R spec
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license license
%{nodejs_sitelib}/chalk


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jul 23 2016 Jared Smith <jsmith@fedoraproject.org> - 1.1.3-1
- Update to upstream 1.1.3 release

* Mon Feb 22 2016 Jared Smith <jsmith@fedoraproject.org> - 1.1.1-8
- Disable tests because they fail in mock

* Mon Feb 22 2016 Jared Smith <jsmith@fedoraproject.org> - 1.1.1-7
- Update to upstream 1.1.1 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.0-2
- fix versioned dependencies

* Thu Mar 13 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.0-1
- initial package
