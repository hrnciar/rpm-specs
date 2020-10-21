%global enable_tests 1

# This package is now a fork, nodeunit-x, maintained by the grunt team.
# The original nodeunit was deprecated for good (?) last year.

Name:       nodeunit
Version:    0.13.0
Release:    5%{?dist}
Summary:    Easy asynchronous unit testing framework for Node.js

License:    MIT
URL:        https://github.com/gruntjs/nodeunit-x
Source0:    https://registry.npmjs.org/nodeunit-x/-/nodeunit-x-%{version}.tgz

BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(ejs)
BuildRequires:  npm(should)
BuildRequires:  npm(tap)
%endif

# I'm not sure about doing this, but for backwards compatibility I think
# it probably makes sense for nodeunit to claim to be both nodeunit + nodeunit-x?
Provides:       npm(nodeunit) = %{version}

# Document bundling
Provides:       bundled(nodejs-async)

%description
Nodeunit provides an easy asynchronous unit testing framework for Node.js:
 - helps you avoid common pitfalls when testing asynchronous code
 - easy to add test cases with setUp and tearDown functions if you wish
 - flexible reporters for custom output
 - built-in support for HTML and jUnit XML
 - allows the use of mocks and stubs

This package ship nodeunit-x, the maintained release for the gruntjs project,
as it is more active than the original upstream project.

%prep
%autosetup -n package

# tap is *horrendously* out of date in Fedora. The current package is 0.7...
# the latest release is 14.
# ejs is less terribly out of date but still bad.
%nodejs_fixdep tap
%nodejs_fixdep ejs

# deps/json2.js is not actually used.
rm deps/json2.js
# the other modules (async and assert) that are "bundled"
# are actually forks of bundled modules.

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/nodeunit
cp -pr package.json index.js deps/ lib/ %{buildroot}%{nodejs_sitelib}/nodeunit
install -p -D -m0755 bin/nodeunit %{buildroot}%{nodejs_sitelib}/nodeunit/bin/nodeunit
mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/nodeunit/bin/nodeunit %{buildroot}%{_bindir}/nodeunit

install -p -D -m0644 man1/nodeunit.1 %{buildroot}%{_mandir}/man1/nodeunit.1

# Put non-javascript arch independent files in _datadir to comply with Node.js
# packaging guidelines.
mkdir -p %{buildroot}%{_datadir}/nodeunit/bin
install -p -D -m0644 bin/nodeunit.json %{buildroot}%{_datadir}/nodeunit/bin/nodeunit.json
cp -pr share/ %{buildroot}%{_datadir}/nodeunit
mkdir -p %{buildroot}%{nodejs_sitelib}/nodeunit/bin
ln -sf %{_datadir}/nodeunit/bin/nodeunit.json %{buildroot}%{nodejs_sitelib}/nodeunit/bin/nodeunit.json
ln -sf %{_datadir}/nodeunit/share %{buildroot}%{nodejs_sitelib}/nodeunit/share

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
# Fails in Koji
rm -f test/test-httputil.js
%__nodejs ./bin/nodeunit test
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif


%files
%doc CONTRIBUTORS.md README.md doc/ examples/
%license LICENSE
%{nodejs_sitelib}/nodeunit
%{_bindir}/nodeunit
%{_datadir}/nodeunit
%{_mandir}/man1/nodeunit.1*


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 14 2019 Tom Hughes <tom@compton.nu> - 0.13.0-2
- Include, and document, bundled dependencies

* Mon Aug 26 2019 Ben Rosser <rosser.bjr@gmail.com> - 0.13.0-1
- Switched package to point at nodeunit-x and update to latest release.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul 13 2016 Jared Smith <jsmith@fedoraproject.org> - 0.9.1-5
- Update npm(tap) version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Tom Hughes <tom@compton.nu> - 0.9.1-3
- Replace path.exists with fs.stat in tests

* Sat Nov 21 2015 Tom Hughes <tom@compton.nu> - 0.9.1-2
- Update npm(tap) dependency

* Sat Nov 21 2015 Tom Hughes <tom@compton.nu> - 0.9.1-1
- Update to 0.9.1 upstream release
- Update npm(async) dependency
- Fix tests for newer npm(should)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 19 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.8.6-4
- fix version of npm(ejs) dependency

* Sun Mar 02 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.8.6-3
- fix broken symlink

* Mon Feb 24 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.8.6-2
- disable test/test-httputil.js as it fails in Koji

* Sun Feb 23 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.8.6-1
- update to upstream release 0.8.6
- remove lib/assert.js

* Sun Feb 23 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.8.1-3
- fix summary and description
- use patch instead of sed

* Sun Feb 23 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.8.1-2
- remove nodejs-json2 dependency as it is not needed either for runtime or
  for the unit tests

* Wed Aug 28 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.8.1-1
- update to upstream release 0.8.1
- remove patch that has been upstreamed
- put non-javascript arch independent files in _datadir to comply with Node.js
  packaging guidelines

* Wed May 29 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.8.0-1
- update to upstream release 0.8.0

* Sun Feb 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.4-1
- initial package
