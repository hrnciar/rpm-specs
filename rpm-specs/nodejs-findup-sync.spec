%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:           nodejs-findup-sync
Version:        0.3.0
Release:        9%{?dist}
Summary:        Find the first file matching a given pattern

License:        MIT
URL:            https://github.com/js-cli/node-findup-sync
Source0:        https://github.com/js-cli/node-findup-sync/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(nodeunit)
BuildRequires:  npm(glob)
BuildRequires:  npm(lodash)
%endif

%description
Find the first file matching a given pattern in the current directory or
the nearest ancestor directory.


%prep
%autosetup -n node-findup-sync-%{version}
%nodejs_fixdep glob '^6.0.3'


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/findup-sync
cp -pr package.json lib/ \
    %{buildroot}%{nodejs_sitelib}/findup-sync
%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/nodeunit/bin/nodeunit test/
%endif


%files
%{!?_licensedir:%global license %doc}
%doc README.md
%license LICENSE-MIT
%{nodejs_sitelib}/findup-sync


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 0.3.0-1
- Update to 0.3.0 upstream release

* Mon Dec 14 2015 Tom Hughes <tom@compton.nu> - 0.1.3-4
- Update npm(lodash) dependency
- Enable tests

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 30 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.3.1
- update to upstream release 0.1.3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.2-1
- initial package
