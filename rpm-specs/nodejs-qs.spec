%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:           nodejs-qs
Version:        6.5.1
Release:        8%{?dist}
Summary:        Query string parser for Node.js
License:        BSD
URL:            https://github.com/ljharb/qs
Source0:        https://registry.npmjs.org/qs/-/qs-%{version}.tgz
BuildArch:      noarch

ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(iconv-lite)

%if 0%{?enable_tests}
BuildRequires:  npm(tape)
%endif

%description
This is a query string parser for node and the browser supporting nesting,
as it was removed from 0.3.x, so this library provides the previous and
commonly desired behavior (and twice as fast). Used by express, connect
and others.


%prep
%setup -q -n package


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/qs
cp -p package.json %{buildroot}%{nodejs_sitelib}/qs
mkdir -p %{buildroot}%{nodejs_sitelib}/qs/lib
install -p -m644 lib/*.js %{buildroot}%{nodejs_sitelib}/qs/lib
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'

%if 0%{?enable_tests}
%__nodejs test
%endif


%files
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitelib}/qs


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.1-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 03 2017 Jared Smith <jsmith@fedoraproject.org> - 6.5.1-1
- Update to upstream 6.5.1 release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 31 2017 Piotr Popieluch <piotr1212@gmail.com> - 6.4.0-1
- Update to 6.4

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Tom Hughes <tom@compton.nu> - 6.0.2-1
- Update to 6.0.2 upstream release
- Enable tests

* Sun Jan 17 2016 Tom Hughes <tom@compton.nu> - 6.0.1-1
- Update to 6.0.1 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Sep 24 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.6.6-3
- backport security fix for memory exhaustion denial-of-service (RHBZ#1146054)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 10 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.6.6-1
- update to upstream release 0.6.6

* Sun Jul 28 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.6.5-3
- add ExclusiveArch logic

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.6.5-2
- restrict to compatible arches

* Sat May 25 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.6.5-1
- update to upstream release 0.6.5

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.5.6-2
- add macro to enable dependency generation in EPEL

* Wed Apr 10 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.6-1
- update to upstream release 0.5.6

* Fri Mar 22 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.5-1
- update to upstream release 0.5.5

* Sat Mar 16 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.4-1
- update to upstream release 0.5.4

* Wed Feb 20 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.3-3
- fix typo in %%description

* Wed Feb 20 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.3-2
- fix typo in %%summary

* Mon Feb 11 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.3-1
- initial package
