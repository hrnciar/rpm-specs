%{?nodejs_find_provides_and_requires}

# tests have circular dependency (mocha -> jade -> monocle)
%global enable_tests 1

Name:           nodejs-monocle
Version:        1.1.51
Release:        18%{?dist}
Summary:        A tool for watching directories for file changes
License:        BSD
URL:            https://www.npmjs.com/package/monocle
Source0:        https://github.com/samccone/monocle/archive/v%{version}/%{name}-%{version}.tar.gz
# Add patch to fix test errors with recent Node.js versions
Patch0:         nodejs-monocle-afterall.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(mocha)
BuildRequires:  npm(readdirp)
%endif

%description
%{summary}.


%prep
%autosetup -p 1 -n monocle-%{version}
%nodejs_fixdep readdirp "^2.1.0"


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/monocle
cp -pr package.json monocle.js %{buildroot}%{nodejs_sitelib}/monocle
%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
/usr/bin/mocha test -R spec -t 60000
%endif


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/monocle


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.51-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 23 2019 Tom Hughes <tom@compton.nu> - 1.1.51-17
- Re-enable tests

* Fri Aug 23 2019 Tom Hughes <tom@compton.nu> - 1.1.51-16
- Add patch to fix test failures

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.51-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.51-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.51-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.51-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 12 2017 Tom Hughes <tom@compton.nu> - 1.1.51-11
- Increase test timeout

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.51-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.51-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.51-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Tom Hughes <tom@compton.nu> - 1.1.51-7
- Increase test timeout

* Thu Dec 31 2015 Tom Hughes <tom@compton.nu> - 1.1.51-6
- Enable tests

* Thu Dec 31 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.1.51-5
- Update fixdep on readdirp
- Disable tests to break circular dependency

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.51-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.51-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 26 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.1.51-2
- fix version of npm(readdirp) dependency

* Sun Mar 02 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.1.51-1
- initial package
