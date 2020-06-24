%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
%global enable_tests 1

Name:           nodejs-tap
Version:        0.7.1
Release:        9%{?dist}
Summary:        A Test Anything Protocol library

License:        MIT
URL:            https://github.com/isaacs/node-tap
Source0:        https://registry.npmjs.org/tap/-/tap-%{version}.tgz
Source1:        macros.nodejs-tap

BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
# we need to replicate the dependencies of this package for it to be able to
# test itself
BuildRequires:  gcc
BuildRequires:  npm(buffer-equal)
BuildRequires:  npm(deep-equal)
BuildRequires:  npm(difflet)
BuildRequires:  npm(glob)
BuildRequires:  npm(inherits) = 1.0.0
BuildRequires:  npm(mkdirp)
BuildRequires:  npm(nopt)
BuildRequires:  npm(runforcover)
BuildRequires:  npm(slide)
BuildRequires:  npm(yamlish)
%endif

%description
This is a mix-and-match set of utilities that you can use to write test
harnesses and frameworks that communicate with one another using the
Test Anything Protocol.

%prep
%setup -q -n package
#%%patch1 -p1

%nodejs_fixdep deep-equal '^1.0.1'
%nodejs_fixdep glob '^6.0.3'
%nodejs_fixdep inherits 1
%nodejs_fixdep nopt '^3.0.6'

#remove bundled modules
rm -rf node_modules

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/tap
cp -pr bin lib package.json %{buildroot}%{nodejs_sitelib}/tap

mkdir -p %{buildroot}%{_bindir}
ln -sf ../lib/node_modules/tap/bin/tap.js %{buildroot}%{_bindir}/tap

#install some macros for use in RPM %%check sections
install -Dpm0644 %{SOURCE1} %{buildroot}%{macrosdir}/macros.tap

#make secondary scripts executable
chmod 0755 %{buildroot}%{nodejs_sitelib}/tap/bin/*

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%if 0%{?enable_tests}
%{__nodejs} -e 'require("./")'

# Temporarily disable test/segv.js
rm -f test/debug-test.js

%__nodejs %{buildroot}%{nodejs_sitelib}/tap/bin/tap.js test/*.js
%endif

%files
%{nodejs_sitelib}/tap
%{_bindir}/tap
%{macrosdir}/macros.tap
%doc coverage-example example README.md AUTHORS LICENSE

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 09 2019 Jared K. Smith <jsmith@fedoraproject.org> - 0.7.1-7
- Rebuild to fix some testing

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul 13 2016 Jared Smith <jsmith@fedoraproject.org> - 0.7.1-1
- -Update to upstream 0.7.1 release

* Sun Feb 07 2016 Piotr Popieluch <piotr1212@gmail.com> - 0.4.4-10
- cleanup spec

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 17 2016 Tom Hughes <tom@compton.nu> - 0.4.4-8
- Update npm(nopt) dependency

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 0.4.4-7
- Update npm(glob) dependency

* Fri Sep  4 2015 Tom Hughes <tom@compton.nu> - 0.4.4-6
- Fix deep-equal dependency

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar  4 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.4.4-4
- Install macros in %%{_rpmconfigdir}/macros.d where available (#1074280)

* Wed Oct 29 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.4-3
- fix version of npm(deep-equal) dependency

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 03 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.4-1
- update to upstream release 0.4.4

* Sat Aug 03 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.1-7
- BuildRequire the correct version of inherits

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 11 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.1-6
- temporarily disable test/segv.js, as in local mock the test receives SIGSEGV
  but in koji it receives SIGTERM instead

* Wed Jul 10 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.1-5
- enable tests
- force the use inherits@1 since this module is incompatible with inherits@2

* Mon Jun 24 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.1-4
- fix glob dep

* Sat Jun 22 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.1-3
- add macro for EPEL6 dependency generation

* Fri Jun 14 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.1-2.1
- rebuild for missing npm(tap) provides
- temporarily disable tests to more easily fix above breakage

* Tue Apr 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.1-2
- fix rpmlint warnings

* Tue Apr 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.1-1
- new upstream release 0.4.1
- fix tests

* Tue Jan 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.3-2
- rename from tap to nodejs-tap
- remove bootstrap logic that didn't work
- instead we use ourself and BuildRequire everything we need

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.3-1
- initial package generated by npm2rpm
