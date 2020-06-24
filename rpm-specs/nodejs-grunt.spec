%global enable_tests 0

Name:       nodejs-grunt
Version:    1.0.4
Release:    3%{?dist}
Summary:    Grunt is a JavaScript library used for automation and running tasks
License:    MIT
URL:        https://github.com/gruntjs/grunt
Source0:    https://github.com/gruntjs/grunt/archive/v%{version}/grunt-%{version}.tar.gz


BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(coffee-script)
BuildRequires:  npm(dateformat)
BuildRequires:  npm(eventemitter2)
BuildRequires:  npm(exit)
BuildRequires:  npm(findup-sync)
BuildRequires:  npm(glob)
BuildRequires:  npm(grunt-cli)
BuildRequires:  npm(grunt-known-options)
BuildRequires:  npm(grunt-legacy-log)
BuildRequires:  npm(grunt-legacy-util)
BuildRequires:  npm(iconv-lite)
BuildRequires:  npm(js-yaml)
BuildRequires:  npm(minimatch)
BuildRequires:  npm(nopt)
BuildRequires:  npm(path-is-absolute)
BuildRequires:  npm(rimraf)
BuildRequires:  npm(difflet)
BuildRequires:  npm(grunt-contrib-nodeunit)
BuildRequires:  npm(grunt-contrib-watch)
BuildRequires:  npm(semver)
BuildRequires:  npm(shelljs)
BuildRequires:  npm(temporary)
BuildRequires:  npm(through2)
%endif


%description
Grunt is the JavaScript task runner. Why use a task runner? In one word:
automation. The less work you have to do when performing repetitive tasks
like minification, compilation, unit testing, linting, etc, the easier
your job becomes. After you've configured it, a task runner can do most
of that mundane work for you with basically zero effort.

%prep
%autosetup -n grunt-%{version}

%nodejs_fixdep coffee-script '^1.3'
%nodejs_fixdep dateformat '*'
%nodejs_fixdep eventemitter2 '~0.4'
%nodejs_fixdep findup-sync '~0.3'
%nodejs_fixdep glob '~6.0.3'
%nodejs_fixdep minimatch '~3.0.0'
%nodejs_fixdep nopt '^3.0.6'
%nodejs_fixdep rimraf '^2.0'
%nodejs_fixdep js-yaml '^3.5.0'

# coffee-script was renamed to coffeescript...
# But we still ship coffee-script. So remove the
# npm(coffeescript) dep entirely
%nodejs_fixdep -r coffeescript

# As a consequence of the above, we need to s/coffeescript/coffee-script/...
sed 's/coffeescript/coffee-script/g' -i lib/grunt.js

%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/grunt
cp -pr package.json internal-tasks/ lib/ \
    %{buildroot}%{nodejs_sitelib}/grunt

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
grunt nodeunit:all
%endif


%files
%doc AUTHORS CHANGELOG CONTRIBUTING.md README.md
%license LICENSE
%{nodejs_sitelib}/grunt


%changelog
* Tue Feb 18 2020 Ben Rosser <rosser.bjr@gmail.com> - 1.0.4-3
- Load coffeescript as coffee-script in lib/grunt.js.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.0.4-1
- Update to latest upstream release.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Tom Hughes <tom@compton.nu> - 1.0.1-9
- Enable tests

* Thu Jul 19 2018 Tom Hughes <tom@compton.nu> - 1.0.1-8
- Update npm(rimraf) dependency

* Wed Jul 18 2018 Tom Hughes <tom@compton.nu> - 1.0.1-7
- Update npm(findup-sync) dependency
- Update npm(coffee-script) dependency

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 24 2016 Piotr Popieluch <piotr1212@gmail.com> - - 1.0.1-2
- Enable tests

* Tue Aug 09 2016 Piotr Popieluch <piotr1212@gmail.com> - - 1.0.1-1
- update to 1.0.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 17 2016 Tom Hughes <tom@compton.nu> - 0.4.5-8
- Update npm(nopt) dependency

* Mon Jan 11 2016 Tom Hughes <tom@compton.nu> - 0.4.5-7
- Update npm(js-yaml) dependency

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 0.4.5-6
- Update npm(js-yaml) dependency

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 0.4.5-5
- Update npm(glob) dependency

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 0.4.5-4
- Update npm(minimatch) dependency

* Mon Dec 14 2015 Tom Hughes <tom@compton.nu> - 0.4.5-3
- Update npm(lodash) dependency

* Sat Nov 21 2015 Tom Hughes <tom@compton.nu> - 0.4.5-2
- Update npm(colors) dependency

* Sat Nov 21 2015 Tom Hughes <tom@compton.nu> - 0.4.5-1
- Update to 0.4.5 upstream release
- Update npm(async) dependency

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 31 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.4-3
- apply patch to fix "_ is not defined" errors when using templates

* Sun Apr 20 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.4-2
- add missing internal-tasks/ folder

* Sat Mar 29 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.4-1
- update to upstream release 0.4.4

* Sun Nov 03 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.1-2
- improve %%summary
- add ExclusiveArch logic

* Fri Jun 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.1-1
- initial package
