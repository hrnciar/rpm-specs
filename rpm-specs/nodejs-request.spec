%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:          nodejs-request
Version:       2.67.0
Release:       15%{?dist}
Summary:       Simplified HTTP request client
License:       ASL 2.0
URL:           https://github.com/request/request
Source0:       https://github.com/request/request/archive/v%{version}/request-%{version}.tar.gz
BuildArch:     noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(aws-sign2)
BuildRequires:  npm(bl)
BuildRequires:  npm(caseless)
BuildRequires:  npm(combined-stream)
BuildRequires:  npm(extend)
BuildRequires:  npm(forever-agent)
BuildRequires:  npm(form-data)
BuildRequires:  npm(har-validator)
BuildRequires:  npm(hawk)
BuildRequires:  npm(http-signature)
BuildRequires:  npm(is-typedarray)
BuildRequires:  npm(isstream)
BuildRequires:  npm(json-stringify-safe)
BuildRequires:  npm(mime-types)
BuildRequires:  npm(node-uuid)
BuildRequires:  npm(oauth-sign)
BuildRequires:  npm(qs)
BuildRequires:  npm(stringstream)
BuildRequires:  npm(tough-cookie)
BuildRequires:  npm(tunnel-agent)

%if 0%{?enable_tests}
BuildRequires:  npm(tape)
BuildRequires:  npm(bluebird)
BuildRequires:  npm(buffer-equal)
BuildRequires:  npm(rimraf)
#BuildRequires:  npm(server-destroy)
%endif

%description
Request is designed to be the simplest way possible to make HTTP calls. It
supports HTTPS and follows redirects by default.

You can stream any response to a file stream. You can also stream a file to a
PUT or POST request.  It also supports a few simple server and proxy functions.


%prep
%autosetup -p 1 -n request-%{version}
%{nodejs_fixdep} aws-sign2 "^0.7.0"
%{nodejs_fixdep} bl "^1.0.0"
%{nodejs_fixdep} form-data "^0.2.0"
%{nodejs_fixdep} hawk "^4.0.1"
%{nodejs_fixdep} http-signature "^0.10.0"
%{nodejs_fixdep} qs "^6.0.1"
%{nodejs_fixdep} tough-cookie "^2.3.1"
chmod -x index.js
rm -rf node_modules


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/request
cp -pr package.json index.js request.js lib %{buildroot}%{nodejs_sitelib}/request
%nodejs_symlink_deps


%check
%{nodejs_symlink_deps} --check
%__nodejs -e "require('./')"
%if 0%{?enable_tests}
# needs npm(server-destroy)
rm tests/test-tunnel.js
tape tests/test-*.js
%endif


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/request


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.67.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.67.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 2019 Tom Hughes <tom@compton.nu> - 2.67.0-13
- Update npm(aws-sign2) dependency

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.67.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.67.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.67.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.67.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.67.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul 27 2016 Piotr Popieluch <piotr1212@gmail.com> - - 2.67.0-7
- Update npm(tough-cookie) dependency

* Thu Mar 31 2016 Tom Hughes <tom@compton.nu> - 2.67.0-6
- Update npm(bl) dependency

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.67.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Tom Hughes <tom@compton.nu> - 2.67.0-4
- Do a basic "does it load" test even when tests are disabled

* Tue Jan 19 2016 Tom Hughes <tom@compton.nu> - 2.67.0-3
- Include the lib directory in the package

* Sun Jan 17 2016 Tom Hughes <tom@compton.nu> - 2.67.0-2
- Update dependencies

* Sun Jan 17 2016 Tom Hughes <tom@compton.nu> - 2.67.0-1
- Update to 2.67.0 upstream release

* Sun Jan 17 2016 Tom Hughes <tom@compton.nu> - 2.25.0-8
- Update npm(tunnel-agent) dependency

* Sun Jan 17 2016 Tom Hughes <tom@compton.nu> - 2.25.0-7
- Update npm(tunnel-agent) dependency

* Sun Dec 06 2015 Piotr Popieluch <piotr1212@gmail.com> - 2.25.0-6
- fixdep oauth-sign

* Tue Dec 01 2015 Piotr Popieluch <piotr1212@gmail.com> - 2.25.0-5
- Fixdep updated dependencies
- Fix permissions

* Sat Nov 21 2015 Tom Hughes <tom@compton.nu> - 2.25.0-4
- update form-data dependency

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.25.0-1
- new upstream release 2.25.0

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.21.0-1
- new upstream release 2.21.0

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.16.6-5
- restrict to compatible arches

* Tue May 28 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.16.6-4
- make versioned dependency on npm(qs) less specific
- add %%check

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.16.6-3
- add macro for EPEL6 dependency generation

* Wed Apr 10 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.16.6-2
- fix versions for newly added dependencies

* Wed Apr 03 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.16.6-1
- new upstream release 2.16.6
- cookie library now unbundled upstream

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.14.0-1
- new upstream release 2.14.0

* Tue Jan 29 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.12.0-5
- actually make patch work
- fix typo

* Mon Jan 28 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.12.0-4
- actually apply patch
- manually create dependency link to private module tobi-cookie

* Thu Jan 24 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.12.0-3
- unbundle cookie stuff

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.12.0-2
- add missing build section
- improve description

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.12.0-1
- new upstream release 2.12.0
- clean up for submission

* Wed Apr 18 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.9.202-1
- New upstream release 2.9.202

* Sun Mar 04 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.9.153-1
- new upstream release 2.9.153

* Sat Feb 25 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.9.151-1
- new upstream release 2.9.151

* Sat Jan 21 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.9.100-1
- new upstream release 2.9.100

* Thu Dec 22 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.2.9-1
- new upstream release 2.2.9

* Mon Nov 07 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.2.0-1
- new upstream release 2.2.0
- adds node v0.6 support

* Tue Oct 25 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.0-2.20110928.646c80dgit
- npm needs a newer git snapshot (apparently upstream moved to rolling release anyway)

* Tue Oct 25 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.0-1
- initial package
