%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:       nodejs-joosex-namespace-depended
Version:    0.18.0
Release:    12%{?dist}
Summary:    Cross-platform (browser/NodeJS), non-blocking, handling of dependencies
# LICENSE file contains LGPLv3. README.md contains BSD.
License:    LGPLv3 or BSD
URL:        https://github.com/SamuraiJack/JooseX-Namespace-Depended
Source0:    http://registry.npmjs.org/joosex-namespace-depended/-/joosex-namespace-depended-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(test-run)
%endif

%description
%{summary}.


%prep
%setup -q -n package
# Remove duplicate file (already in doc/).
rm -f lib/JooseX/Namespace/Depended.mmd


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/joosex-namespace-depended
cp -pr package.json joosex-namespace-depended-all.js lib/ \
    %{buildroot}%{nodejs_sitelib}/joosex-namespace-depended

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%__nodejs t/index.js
%endif


%files
%doc Changes LICENSE README.md doc/
%{nodejs_sitelib}/joosex-namespace-depended


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb 23 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.18.0-2
- fix License tag
- remove duplicate file

* Sun Feb 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.18.0-1
- initial package
