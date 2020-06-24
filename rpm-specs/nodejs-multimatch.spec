%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:           nodejs-multimatch
Version:        2.1.0
Release:        11%{?dist}
Summary:        Adds multiple patterns support to minimatch.match()
License:        MIT
URL:            https://github.com/sindresorhus/multimatch
Source0:        https://github.com/sindresorhus/multimatch/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?fedora} >= 19
ExclusiveArch:  %{nodejs_arches} noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(array-differ)
BuildRequires:  npm(array-union)
BuildRequires:  npm(arrify)
BuildRequires:  npm(chai)
BuildRequires:  npm(minimatch)
BuildRequires:  npm(mocha)
%endif

%description
%{summary}.


%prep
%autosetup -n multimatch-%{version}
%nodejs_fixdep arrify "^2.0.1"
%nodejs_fixdep array-union "^2.1.0"


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/multimatch
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/multimatch
%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{_bindir}/mocha --reporter spec
%endif


%files
%doc readme.md
%license license
%{nodejs_sitelib}/multimatch


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May  1 2019 Tom Hughes <tom@compton.nu> - 2.1.0-9
- Update npm(arrify) dependency

* Mon Apr 22 2019 Tom Hughes <tom@compton.nu> - 2.1.0-8
- Fix npm(array-union) dependency

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Tom Hughes <tom@compton.nu> - 2.1.0-1
- Update to 2.1.0 upstream release

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 0.1.0-5
- Update npm(minimatch) dependency

* Tue Dec 15 2015 Tom Hughes <tom@compton.nu> - 0.1.0-4
- Update npm(lodash) dependency

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 29 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.0-1
- initial package
