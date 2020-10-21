%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:           nodejs-node-uuid
Version:        1.4.7
Release:        11%{?dist}
Summary:        Simple and fast generation of RFC4122 (v1 and v4) UUIDs for Node.js
License:        MIT
URL:            https://github.com/broofa/node-uuid
Source0:        https://registry.npmjs.org/node-uuid/-/node-uuid-%{version}.tgz
BuildArch:      noarch

%if 0%{?fedora} >= 19
ExclusiveArch:  %{nodejs_arches} noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%description
This Node.js module provides simple and fast generation of RFC4122 (v1 and v4)
UUIDs. It runs in Node.js and all browsers and can also generate
cryptographically strong random numbers.


%prep
%setup -q -n package


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/node-uuid
cp -pr package.json uuid.js \
    %{buildroot}%{nodejs_sitelib}/node-uuid
%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%__nodejs test/test.js
%endif


%files
%doc README.md
%license LICENSE.md
%{nodejs_sitelib}/node-uuid


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 17 2016 Tom Hughes <tom@compton.nu> - 1.4.7-1
- Update to 1.4.7 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 26 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.4.1-1
- update to upstream release 1.4.1

* Sun Jul 28 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.4.0-5
- add ExclusiveArch logic

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.4.0-4
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.4.0-3
- add macro to enable dependency generation in EPEL

* Fri Apr 05 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.4.0-2
- do not include benchmark/ directory

* Wed Feb 13 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.4.0-1
- initial package
