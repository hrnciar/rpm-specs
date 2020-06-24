%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:       nodejs-commander
Version:    2.9.0
Release:    9%{?dist}
Summary:    Node.js command-line interfaces made easy
# License text is included in Readme.md
License:    MIT
URL:        https://github.com/visionmedia/commander.js
Source0:    https://registry.npmjs.org/commander/-/commander-%{version}.tgz
# Source1 is generated by running Source10, which pulls from the upstream
# version control repository.
Source1:    tests-v%{version}.tar.bz2
Source2:    examples-v%{version}.tar.bz2
Source10:   dl-tests.sh

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

# Dep generator bug which adds a trailing dot in the nodejs(engine) requires.
Patch0:     %{name}-2.9.0-Fix-engine-dep.patch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(should)
BuildRequires:  npm(sinon)
BuildRequires:  npm(graceful-readlink)
%endif

%description
The complete solution for Node.js command-line interfaces,
inspired by Ruby's commander.


%prep
%setup -q -n package
%setup -q -T -D -a 1 -n package
%setup -q -T -D -a 2 -n package
%patch0 -p1


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/commander
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/commander

%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
./test/run test/test.*.js
%endif


%files
%doc Readme.md examples/
%license LICENSE
%{nodejs_sitelib}/commander


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Piotr Popieluch <piotr1212@gmail.com> - 2.9.0-1
- update to upstream release 2.9.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.2.0-1
- update to upstream release 2.2.0

* Sun Mar 02 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.1.0-1
- update to upstream release 2.1.0

* Thu Aug 29 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2.0-6
- fix version of dependency on nodejs-keypress again

* Wed Aug 28 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2.0-5
- fix version of dependency on nodejs-keypress

* Mon Aug 26 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2.0-4
- rebuild to enable tests

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 06 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2.0-2
- fix compatible arches for f18/el6

* Fri Jul 05 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2.0-1
- restrict to compatible arches
- update to upstream release 1.2.0

* Wed Jun 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.1-2
- rebuild for missing npm(commander) provides on EL6

* Tue Feb 12 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.1.1-1
- update to upstream release 1.1.1
- remove patch that disables a known broken test

* Mon Feb 11 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.6.1-1
- initial package