%{?nodejs_find_provides_and_requires}

# native-promise-only and rsvp not packaged yet
%global enable_mocha_tests 1
%global enable_nodeunit_tests 0

Name:           nodejs-async
Version:        1.5.2
Release:        10%{?dist}
Summary:        Higher-order functions and common patterns for asynchronous code

License:        MIT
URL:            https://github.com/caolan/async/
Source0:        https://github.com/caolan/async/archive/v%{version}/async-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_mocha_tests}
BuildRequires:  npm(mocha)
BuildRequires:  npm(chai)
%endif

%if 0%{?enable_nodeunit_tests}
BuildRequires:  npm(nodeunit)
BuildRequires:  npm(bluebird)
BuildRequires:  npm(es6-promise)
BuildRequires:  npm(native-promise-only)
BuildRequires:  npm(rsvp)
%endif

%description
Async is a utility module which provides straight-forward, powerful functions
for working with asynchronous JavaScript. Although originally designed for
use with Node.js, it can also be used directly in the browser.

Async provides around 20 functions that include the usual 'functional'
suspects (map, reduce, filter, forEach…) as well as some common patterns
for asynchronous control flow (parallel, series, waterfall…). All these
functions assume you follow the Node.js convention of providing a single
callback as the last argument of your async function.


%prep
%setup -q -n async-%{version}


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/async
cp -pr package.json lib %{buildroot}%{nodejs_sitelib}/async


%check
%nodejs_symlink_deps --check
%__nodejs -e "require('./')"
%if 0%{?enable_mocha_tests}
%{nodejs_sitelib}/mocha/bin/mocha mocha_test
%endif
%if 0%{?enable_nodeunit_tests}
%{nodejs_sitelib}/nodeunit/bin/nodeunit test/test-async.js
%endif


%files
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitelib}/async


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 29 2016 Jared Smith <jsmith@fedoraproject.org> - 1.5.2-1
- Update to upstream 1.5.2 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Tom Hughes <tom@compton.nu> - 1.5.0-2
- cleanup spec file, removing %%defattr

* Sat Nov 21 2015 Tom Hughes <tom@compton.nu> - 1.5.0-1
- update to 1.5.0 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 18 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.10-1
- update to upstream release 0.2.10 (#1057505)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.9-2
- restrict to compatible arches

* Tue May 28 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.9-1
- update to upstream release 0.2.9
- add %%check

* Sat May 25 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.8-1
- update to upstream release 0.2.8

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.6-2
- add macro for EPEL6 dependency generation

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.6-1
- new upstream release 0.2.6

* Wed Feb 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.5-1
- new upstream release 0.2.5

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.4-1
- new upstream release 0.2.4

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.22-3
- add missing build section

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.22-2
- Fix URL
- Provide a better description

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.22-1
- initial package generated by npm2rpm
