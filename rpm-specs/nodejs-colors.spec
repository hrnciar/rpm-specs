%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:           nodejs-colors
Version:        1.2.1
Release:        6%{?dist}
Summary:        Get colors in your Node.js console

License:        MIT
URL:            https://github.com/Marak/colors.js
Source0:        https://github.com/Marak/colors.js/archive/v%{version}/colors-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging
BuildRequires:  nodejs(engine)

%description
%{summary}.


%prep
%autosetup  -n colors.js-%{version}


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/colors
cp -pr package.json safe.js lib themes/ \
    %{buildroot}%{nodejs_sitelib}/colors
%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%__nodejs tests/basic-test.js && %__nodejs tests/safe-test.js
%endif


%files
%doc README.md ROADMAP.md examples
%license LICENSE
%{nodejs_sitelib}/colors


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 12 2018 Tom Hughes <tom@compton.nu> - 1.2.1-1
- Update to 1.2.1 upstream release

* Sat Mar 10 2018 Tom Hughes <tom@compton.nu> - 1.2.0-1
- Update to 1.2.0 upstream release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 21 2015 Tom Hughes <tom@compton.nu> - 1.1.2-1
- Update to 1.1.2 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 03 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.6.2-1
- update to upstream release 0.6.2

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 06 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.6.0-3
- fix compatible arches for f18/el6

* Wed Jun 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.6.0-2
- rebuild for missing npm(colors) provides on EL6
- restrict to compatible arches

* Wed Feb 13 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.6.0-1
- initial package
