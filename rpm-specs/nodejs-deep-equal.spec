%{?nodejs_find_provides_and_requires}

Name:           nodejs-deep-equal
Version:        1.0.1
Release:        11%{?dist}
Summary:        Node's assert.deepEqual algorithm
License:        MIT
URL:            https://github.com/substack/node-deep-equal
Source0:        https://registry.npmjs.org/deep-equal/-/deep-equal-%{version}.tgz
BuildArch:      noarch

%if 0%{?fedora} >= 19 || 0%{?rhel} > 7
ExclusiveArch:  %{nodejs_arches} noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tape)

%description
Node's `assert.deepEqual()` algorithm implemented as a standalone module.


%prep
%setup -q -n package


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/deep-equal
cp -pr package.json index.js lib/ \
    %{buildroot}%{nodejs_sitelib}/deep-equal
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/tape/bin/tape test/*.js


%files
%doc readme.markdown example/
%license LICENSE
%{nodejs_sitelib}/deep-equal


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 06 2017 Troy Dawson <tdawson@redhat.com> - 1.0.1-6
- Cleanup spec file conditionals

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Tom Hughes <tom@compton.nu> - 1.0.1-2
- Cleanup spec file, removing %%defattr

* Sun Aug 30 2015 Tom Hughes <tom@compton.nu> - 1.0.1-1
- update to upstream release 1.0.1
- move LICENSE file to %%license

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 27 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.1-3
- add missing lib/ directory

* Sun Oct 26 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.1-2
- actually run the tests

* Sun Oct 26 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.1-1
- update to upstream release 0.2.1
- include LICENSE file
- enable tests

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jan 17 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.0-2
- comment out BuildRequires on npm(tap)

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.0-1
- initial package generated by npm2rpm
