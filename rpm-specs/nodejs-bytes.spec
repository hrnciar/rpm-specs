%{?nodejs_find_provides_and_requires}

Name:           nodejs-bytes
Version:        3.1.0
Release:        1%{?dist}
Summary:        Utility to parse a string bytes to bytes and vice-versa

License:        MIT
URL:            https://www.npmjs.com/package/bytes
Source0:        https://github.com/visionmedia/bytes.js/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)


%description
%summary


%prep
%autosetup -p 1 -n bytes.js-%{version}


%build



%install
mkdir -p %{buildroot}%{nodejs_sitelib}/bytes
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/bytes
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
mocha --check-leaks --reporter spec


%files
%doc History.md Readme.md
%license LICENSE
%{nodejs_sitelib}/bytes


%changelog
* Fri Feb 07 2020 Ben Rosser <rosser.bjr@gmail.com> - 3.1.0-1
- Update to latest upstream release, 3.1.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 09 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.4.0-1
- Update, change %%summary

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.3.0-1
- update to upstream release 0.3.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 06 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.1-4
- fix compatible arches for f18/el6

* Fri Jul 05 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.1-3
- restrict to compatible arches

* Wed Jun 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.1-2
- rebuild for missing npm(bytes) provides

* Sun Apr 07 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.1-1
- update to upstream release 0.2.1

* Tue Feb 12 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.0-2
- document how to retrieve tests

* Mon Feb 11 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.0-1
- initial package
