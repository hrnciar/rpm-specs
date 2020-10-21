%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:           nodejs-burrito
Version:        0.2.12
Release:        21%{?dist}
Summary:        Wrap up expressions with a trace function while walking the AST

#no license file included, "BSD" indicated in package.json
License:        BSD
URL:            https://github.com/substack/node-burrito
Source0:        https://registry.npmjs.org/burrito/-/burrito-%{version}.tgz
#to satisfy the BSD requirement that the text of the license be included, we
#include this copy of the 3-clause BSD as used in one of the author's projects.
Source1:        https://raw.github.com/substack/lambdascape/master/LICENSE

BuildArch:      noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(tap)
%endif

%description
Burrito makes it easy to do crazy stuff with the JavaScript AST.

This is useful if you want to roll your own stack traces or build a code
coverage tool.


%prep
%setup -q -n package

%nodejs_fixdep uglify-js '~1.3.4'
%nodejs_fixdep traverse '~0.6.3'

cp -p %{SOURCE1} LICENSE


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/burrito
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/burrito

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%tap test/*.js
%endif


%files
%{nodejs_sitelib}/burrito
%doc README.markdown example
%license  LICENSE


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 07 2016 Piotr Popieluch <piotr1212@gmail.com> - 0.2.12-13
- Cleanup spec

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 10 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.12-9
- fix uglify-js1 symlink

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 06 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.12-7
- fix compatible arches on f18/el6

* Fri Jul 05 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.12-6
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.12-5
- add macro to enable dependency generation on EPEL6

* Tue Mar 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.12-4
- include a LICENSE file
- fix typo in Description

* Sat Mar 16 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.12-3
- fix deps for real

* Wed Feb 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.12-2
- fix uglify-js and traverse deps

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.12-1
- initial package generated by npm2rpm
