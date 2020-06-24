%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:           mocha
Version:        2.4.5
Release:        14%{?dist}
Summary:        A simple, flexible, fun test framework for Node.js

License:        MIT
URL:            https://github.com/mochajs/mocha
Source0:        https://github.com/mochajs/mocha/archive/v%{version}/%{name}-%{version}.tar.gz
# Dep generator bug which adds a trailing dot in the node(engine) requires
Patch0:         mocha-node-dep.patch
# Patch change in test results due to Node 6.x
Patch1:         mocha-tests.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(chalk)
BuildRequires:  npm(commander)
BuildRequires:  npm(debug)
BuildRequires:  npm(diff)
BuildRequires:  npm(escape-string-regexp)
BuildRequires:  npm(glob)
BuildRequires:  npm(growl)
BuildRequires:  npm(jade)
BuildRequires:  npm(mkdirp)
BuildRequires:  npm(should)
BuildRequires:  npm(supports-color)
%endif

%description
Mocha is a feature-rich JavaScript test framework running on Node.js and the
browser, making asynchronous testing simple and fun. Mocha tests run serially,
allowing for flexible and accurate reporting, while mapping uncaught
exceptions to the correct test cases.


%prep
%autosetup -p 1
%nodejs_fixdep commander "^2.2.0"
%nodejs_fixdep debug "^2.2.0"
%nodejs_fixdep diff "^1.0.8"
%nodejs_fixdep escape-string-regexp "^1.0.2"
%nodejs_fixdep glob "^6.0.3"
%nodejs_fixdep growl "^1.7.0"
%nodejs_fixdep jade "^1.3.1"
%nodejs_fixdep mkdirp "^0.5.0"
%nodejs_fixdep supports-color


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/mocha
cp -pr package.json index.js lib/ mocha.css mocha.js \
    %{buildroot}%{nodejs_sitelib}/mocha

rm -f %{buildroot}%{nodejs_sitelib}/mocha/lib/template.html
rm -rf %{buildroot}%{nodejs_sitelib}/mocha/lib/reporters/templates

mkdir -p %{buildroot}%{nodejs_sitelib}/mocha/bin
install -p -D -m0755 bin/mocha %{buildroot}%{nodejs_sitelib}/mocha/bin/mocha
install -p -D -m0755 bin/_mocha %{buildroot}%{nodejs_sitelib}/mocha/bin/_mocha
install -p -D -m0644 bin/options.js %{buildroot}%{nodejs_sitelib}/mocha/bin/options.js
mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/mocha/bin/mocha %{buildroot}%{_bindir}/mocha

# Use system diff.js instead.
ln -sf %{nodejs_sitelib}/diff/diff.js \
    %{buildroot}%{nodejs_sitelib}/mocha/lib/browser/diff.js

# Put these files in _datadir to comply with packaging guidelines.
mkdir -p %{buildroot}%{_datadir}/mocha/images
cp -pr images/*.png \
    %{buildroot}%{_datadir}/mocha/images
ln -sf %{_datadir}/mocha/images \
    %{buildroot}%{nodejs_sitelib}/mocha/images
cp -pr lib/template.html \
    %{buildroot}%{_datadir}/mocha
ln -sf %{_datadir}/mocha/template.html \
    %{buildroot}%{nodejs_sitelib}/mocha/lib/template.html
cp -pr lib/reporters/templates \
    %{buildroot}%{_datadir}/mocha
ln -sf %{_datadir}/mocha/templates \
    %{buildroot}%{nodejs_sitelib}/mocha/lib/reporters/templates

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
sed -i -e 's/1000/30000/' test/color.js
sed -i -e 's/200/30000/' test/acceptance/context.js
./bin/mocha --timeout 30000 test/acceptance/*.js test/*.js
%endif


%files
%doc README.md CHANGELOG.md CONTRIBUTING.md
%license LICENSE
%{nodejs_sitelib}/mocha
%{_bindir}/mocha
%{_datadir}/mocha


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 30 2017 Tom Hughes <tom@compton.nu> - 2.4.5-9
- Relax npm(debug) dependency

* Wed Sep 20 2017 Jared Smith <jsmith@fedoraproject.org> - 2.4.5-8
- Relax dependency on npm(supports-color)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 21 2016 Tom Hughes <tom@compton.nu> - 2.4.5-5
- Patch change in test output in Node 6.x

* Sun Feb 14 2016 Tom Hughes <tom@compton.nu> - 2.4.5-4
- Increase test timeout

* Mon Feb  8 2016 Tom Hughes <tom@compton.nu> - 2.4.5-3
- Increase test timeout

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Tom Hughes <tom@compton.nu> - 2.4.5-1
- Update to 2.4.5 upstream release

* Thu Jan 28 2016 Tom Hughes <tom@compton.nu> - 2.4.4-1
- Update to 2.4.4 upstream release

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 2.3.4-2
- Install bin/options.js

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 2.3.4-1
- Update to 2.3.4 upstream release

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 1.18.2-4
- Update npm(glob) dependency

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.18.2-1
- update to upstream release 1.18.2

* Sat Mar 15 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.18.0-1
- update to upstream release 1.18.0

* Sun Mar 02 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.17.1-1
- update to upstream release 1.17.1

* Sun Aug 18 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.12.0-1
- update to upstream release 1.12.0
- add ExclusiveArch logic
- enable tests

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 27 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.11.0-1
- update to upstream release 1.11.0
- restrict to compatible arches

* Sat Jun 22 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.10.0-2
- rebuild for missing npm(mocha) Provides

* Sat May 25 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.10.0-1
- update to upstream release 1.10.0

* Tue Apr 16 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.9.0-1
- update to upstream release 1.9.0

* Tue Mar 19 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.8.2-3
- fix incorrect %%changelog entries

* Tue Mar 19 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.8.2-2
- fix symlinks

* Tue Mar 19 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.8.2-1
- update to upstream release 1.8.2
- move images and templates to %%{_datadir} to comply with packaging
  guidelines

* Sat Mar 02 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.8.1-3
- add a custom man page
- include /usr/lib/node_modules/mocha/images/
- remove bundled diff.js and use system diff.js instead
- remove /usr/bin/_mocha symlink

* Thu Feb 14 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.8.1-2
- rename from nodejs-mocha to just mocha

* Thu Feb 14 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.8.1-1
- initial package
