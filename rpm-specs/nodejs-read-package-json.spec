%{?nodejs_find_provides_and_requires}

Name:           nodejs-read-package-json
Version:        2.0.3
Release:        10%{?dist}
Summary:        npm's package.json parser

License:        ISC
URL:            https://github.com/isaacs/read-package-json
Source0:        https://registry.npmjs.org/read-package-json/-/read-package-json-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%description
The thing npm uses to read package.json files, with semantics, defaults and
validation.

%prep
%setup -q -n package
%nodejs_fixdep glob "^6.0.3"

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/read-package-json
cp -pr package.json read-json.js %{buildroot}%{nodejs_sitelib}/read-package-json

%nodejs_symlink_deps

%files
%{nodejs_sitelib}/read-package-json
%doc README.md
%license LICENSE

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 07 2016 Piotr Popieluch <piotr1212@gmail.com> - 2.0.3-3
- cleanup spec

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Stephen Gallagher <sgallagh@redhat.com> - 2.0.3-1
- Update to 2.0.3 to support Node.js 4.x

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 1.1.3-4
- Update npm(glob) dependency

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Sep 07 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.1.3-1
- update to upstream release 1.1.3
- change License from BSD to ISC
- add ExclusiveArch logic

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.1-1
- new upstream release 1.1.1

* Mon Jun 24 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.0-2
- remove unneeded dependency fix on lru-cache

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.0-1
- new upstream release 1.1.0

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.0-5
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.0-4
- add macro for EPEL6 dependency generation

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.0-3
- fix lru-cache dep

* Fri Apr 05 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.0-2
- drop outdated dependency fix

* Wed Apr 03 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.0-1
- new upstream release 0.3.0

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.2-1
- new upstream release 0.2.2

* Wed Feb 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.0-1
- new upstream release 0.2.0

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.13-1
- new upstream release 0.1.13

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.12-2
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.12-1
- initial package generated by npm2rpm