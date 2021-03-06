%{?nodejs_find_provides_and_requires}

# Tests disabled due to missing npm(acorn-6to5)
%global enable_tests 0

Name:           nodejs-escodegen
Version:        1.9.0
Release:        6%{?dist}
Summary:        ECMAScript code generator
License:        BSD
URL:            https://github.com/Constellation/escodegen
Source0:        https://registry.npmjs.org/escodegen/-/escodegen-%{version}.tgz
# Source1 is generated by running Source10, which pulls from the upstream
# revision control repository.
Source1:        tests-%{version}.tar.bz2
Source10:       dl-tests.sh

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(mocha)
BuildRequires:  npm(chai)
BuildRequires:  npm(estraverse)
BuildRequires:  npm(esutils)
BuildRequires:  npm(source-map)
%endif

%description
%{summary}.


%prep
%setup -q -n package
%setup -q -T -D -a 1 -n package

%nodejs_fixdep esprima
%nodejs_fixdep estraverse
%nodejs_fixdep source-map "^0.5.2"
rm -f *.min.js

# fix script interpreter
sed -i '1s/env //' bin/*.js

%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/escodegen
cp -pr package.json escodegen.js \
    %{buildroot}%{nodejs_sitelib}/escodegen

mkdir -p %{buildroot}%{nodejs_sitelib}/escodegen/bin
install -p -D -m0755 bin/escodegen.js \
    %{buildroot}%{nodejs_sitelib}/escodegen/bin/escodegen.js
install -p -D -m0755 bin/esgenerate.js \
    %{buildroot}%{nodejs_sitelib}/escodegen/bin/esgenerate.js

mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/escodegen/bin/escodegen.js \
    %{buildroot}%{_bindir}/escodegen.js
ln -sf %{nodejs_sitelib}/escodegen/bin/esgenerate.js \
    %{buildroot}%{_bindir}/esgenerate.js

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{_bindir}/mocha --reporter spec --timeout 30000
%endif


%files
%{!?_licensedir:%global license %doc}
%license LICENSE.BSD LICENSE.source-map
%{nodejs_sitelib}/escodegen
%{_bindir}/escodegen.js
%{_bindir}/esgenerate.js


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 25 2017 Jared Smith <jsmith@fedoraproject.org> - 1.9.0-1
- Update to upstream 1.9.0 release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 19 2016 Jared Smith <jsmith@fedoraproject.org> - 1.8.0-1
- Update to upstream 1.8.0

* Wed Feb 17 2016 Jared Smith <jsmith@fedoraproject.org> - 1.3.2-9
- Relax dependency on npm(estraverse)

* Thu Feb 11 2016 Tom Hughes <tom@compton.nu> - 1.3.2-8
- Patch tests for newer source-map

* Wed Feb 10 2016 Tom Hughes <tom@compton.nu> - 1.3.2-7
- Update npm(source-map) dependency

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Tom Hughes <tom@compton.nu> - 1.3.2-5
- Increase test timeout - koji can be slow

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 1.3.2-4
- Update npm(esprima) dependency
- Enable most tests

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 18 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.3.2-1
- update to upstream release 1.3.2

* Wed Sep 04 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.0.26-1
- update to upstream release 0.0.26

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.0.23-1
- update to upstream release 0.0.23
- restrict to compatible arches

* Fri Jun 07 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.0.22-2
- add comment about dependencies for %%check
- fix incorrect License tag

* Wed May 29 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.0.22-1
- initial package
