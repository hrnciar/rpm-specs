%{?nodejs_find_provides_and_requires}

Name:       nodejs-debug
Version:    2.6.9
Release:    7%{?dist}
Summary:    A small debugging utility for Node.js
# License text is included in Readme.md
License:    MIT
URL:        https://github.com/visionmedia/debug
Source0:    https://registry.npmjs.org/debug/-/debug-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%description
This module is a tiny Node.js debugging utility modeled after node core's
debugging technique.


%prep
%setup -q -n package
%nodejs_fixdep ms "^2.0.0"


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/debug
cp -pr package.json node.js src %{buildroot}%{nodejs_sitelib}/debug
%nodejs_symlink_deps


%files
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitelib}/debug


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 30 2017 Tom Hughes <tom@compton.nu> - 2.6.9-1
- Update to 2.6.9 upstream release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 10 2017 Tom Hughes <tom@compton.nu> - 2.2.0-4
- Fix npm(ms) dependency

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 24 2015 Tom Hughes <tom@compton.nu> - 2.2.0-1
- update to 2.2.0 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.8.1-1
- update to upstream release 0.8.1

* Sun Apr 20 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.8.0-1
- update to upstream release 0.8.0

* Sun Feb 23 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.4-2
- History.md and example/ no longer included in the NPM tarball

* Sun Feb 23 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.4-1
- update to upstream release 0.7.4

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 06 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.2-4
- restrict to compatible arches

* Tue Jun 18 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.2-3
- rebuild for EL-6 to fix Provides generation

* Thu Feb 14 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.2-2
- correct a typo in the description

* Mon Feb 11 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.2-1
- initial package
