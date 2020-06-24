%global enable_tests 0

Name:       nodejs-grunt-legacy-util
Version:    1.1.1
Release:    3%{?dist}
Summary:    Deprecated Grunt utils provided for backwards compatibility
License:    MIT
URL:        https://github.com/gruntjs/grunt-legacy-util
Source0:    https://registry.npmjs.org/grunt-legacy-util/-/grunt-legacy-util-%{version}.tgz

BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

# We actually need these even if not running tests, for the standard nodejs
# 'can this module be imported' test.
BuildRequires:  npm(getobject)
BuildRequires:  npm(hooker)
BuildRequires:  npm(temporary)
BuildRequires:  npm(underscore.string)
BuildRequires:  npm(lodash)
BuildRequires:  npm(exit)
BuildRequires:  npm(which)
BuildRequires:  npm(async)

# These, however, potentially produce bootstrapping. :(
%if 0%{?enable_tests}
BuildRequires:  npm(grunt-contrib-nodeunit)
BuildRequires:  npm(grunt-cli)
%endif

%description
%{summary}.


%prep
%setup -q -n package

%nodejs_fixdep async '^1.5.0'
%nodejs_fixdep underscore.string '~2.3.1'
%nodejs_fixdep which


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/grunt-legacy-util
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/grunt-legacy-util

%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
/usr/bin/grunt nodeunit -v
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif


%files
%doc README.md CHANGELOG
%license LICENSE-MIT
%{nodejs_sitelib}/grunt-legacy-util


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.1.1-2
- Remove explicit dep on lodash 3; package now supports lodash 4.

* Mon Aug 26 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.1.1-1
- Update to latest upstream release.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 19 2017 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-5
- Relax dependency on npm(which), improve tests

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 24 2016 Piotr Popieluch <piotr1212@gmail.com> - - 1.0.0-2
- Enable tests

* Sun Aug 14 2016 Piotr Popieluch <piotr1212@gmail.com> - - 1.0.0-1
- Update to 1.0.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Tom Hughes <tom@compton.nu> - 0.2.0-6
- Enable tests

* Mon Jan 18 2016 Tom Hughes <tom@compton.nu> - 0.2.0-5
- Update npm(which) dependency

* Tue Dec 15 2015 Tom Hughes <tom@compton.nu> - 0.2.0-4
- Enable tests

* Mon Dec 14 2015 Tom Hughes <tom@compton.nu> - 0.2.0-3
- Update npm(lodash) dependency

* Sun Nov 22 2015 Tom Hughes <tom@compton.nu> - 0.2.0-2
- Enable tests

* Sat Nov 21 2015 Tom Hughes <tom@compton.nu> - 0.2.0-1
- Update to 0.2.0 upstream release
- Update npm(async) dependency

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 29 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.2-1
- initial package
