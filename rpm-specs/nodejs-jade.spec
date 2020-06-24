%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:       nodejs-jade
Version:    1.3.1
Release:    14%{?dist}
Summary:    Jade template engine for Node.js
License:    MIT
URL:        https://github.com/visionmedia/jade
Source0:    http://registry.npmjs.org/jade/-/jade-%{version}.tgz
# The test files are not included in the npm tarball.
# Source1 is generated using Source10, which pulls from the upstream
# version control repository.
Source1:    tests-%{version}.tar.bz2
Source10:   dl-tests.sh

# One of the tests passes with transformers@2.1.0 but is failing with
# transformers@3.0.0.
# https://github.com/visionmedia/jade/issues/1444
Patch0:     %{name}-1.2.0-Fix-test-import-path.patch

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  coffee-script
BuildRequires:  npm(character-parser)
BuildRequires:  npm(constantinople)
BuildRequires:  npm(less)
# The tests require a markdown library, so it could be any one of
# npm(discount), npm(marked) or npm(markdown).
BuildRequires:  npm(markdown)
BuildRequires:  npm(mocha)
BuildRequires:  npm(monocle)
BuildRequires:  npm(should)
BuildRequires:  npm(stylus)
BuildRequires:  npm(transformers)
BuildRequires:  npm(with)
BuildRequires:  uglify-js
%endif

%description
Jade is a high performance template engine heavily influenced by Haml and
implemented with JavaScript for Node.js.


%prep
%setup -q -n package
%setup -T -D -a 1 -q -n package
%patch0 -p1
%nodejs_fixdep character-parser '~1.2'
%nodejs_fixdep commander '>=2.1.0'
%nodejs_fixdep constantinople '~2.0'
%nodejs_fixdep mkdirp '^0.5.1'
%nodejs_fixdep monocle '~1.1.51'
%nodejs_fixdep transformers '>=2.1.0'
%nodejs_fixdep with '~3.0'


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/jade
cp -pr package.json index.js jade.js lib/ runtime.js \
    %{buildroot}%{nodejs_sitelib}/jade
mkdir -p %{buildroot}%{nodejs_sitelib}/jade/bin
install -p -D -m0755 bin/jade.js %{buildroot}%{nodejs_sitelib}/jade/bin/jade.js

mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/jade/bin/jade.js \
    %{buildroot}%{_bindir}/jade-nodejs

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha -R spec
%endif


%files
%doc jade-language.md jade.md LICENSE README.md Readme_zh-cn.md jade.md
%{nodejs_sitelib}/jade
%{_bindir}/jade-nodejs


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Jared K. Smith <jsmith@fedoraproject.org> - 1.3.1-11
- Fix versions of npm(commander) and npm(transformers)

* Wed Jul 18 2018 Jared K. Smith <jsmith@fedoraproject.org> - 1.3.1-10
- Relax dependencies on two libraries

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 1.3.1-4
- Update npm(mkdirp) dependency

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.3.1-1
- update to upstream release 1.3.1

* Tue Apr 01 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.3.0-3
- include _bindir/jade-nodejs

* Sat Mar 15 2014 <jamielinux@fedoraproject.org> - 1.3.0-2
- temporarily disable tests due to circular dependency

* Mon Mar 03 2014 <jamielinux@fedoraproject.org> - 1.3.0-1
- update to upstream release 1.3.0

* Sun Mar 02 2014 <jamielinux@fedoraproject.org> - 1.2.0-1
- update to upstream release 1.2.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 15 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.28.2-1
- update to upstream release 0.28.2

* Sun Feb 24 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.28.1-2
- remove /usr/bin/jade symlink

* Thu Feb 14 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.28.1-1
- initial package
