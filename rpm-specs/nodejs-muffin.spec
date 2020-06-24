%{?nodejs_find_provides_and_requires}

Name:       nodejs-muffin
Version:    0.9.0
Release:    15%{?dist}
Summary:    Node.js module with handy helpers for building Cakefiles
# License text is included in Readme.md
License:    MIT
URL:        http://hornairs.github.com/muffin/
Source0:    http://registry.npmjs.org/muffin/-/muffin-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging
Requires:       cloc

%description
This Node.js module has handy helpers for building Cakefiles.

It has a set of generic high level file operations you don't want to implement
yourself, like copying files, CoffeeScript compilation and compile time
requiring, minification, and SLOC counting.


%prep
%setup -q -n package
rm -f deps/cloc.pl
rm -rf docs/public/fonts/
%nodejs_fixdep coffee-script '~1.4'
%nodejs_fixdep glob '~6.0.3'
%nodejs_fixdep prompt '~0.2'
%nodejs_fixdep q '~1.0'
%nodejs_fixdep q-io '~1.6'
%nodejs_fixdep snockets '~1.3'
%nodejs_fixdep temp '~0.5'
%nodejs_fixdep uglify-js '~2.2'


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/muffin
cp -pr package.json deps/ lib/ \
    %{buildroot}%{nodejs_sitelib}/muffin

# Use system provided cloc.pl
ln -sf /usr/bin/cloc \
    %{buildroot}%{nodejs_sitelib}/muffin/deps/cloc.pl

%nodejs_symlink_deps


%files
%doc Readme.md docs/
%{nodejs_sitelib}/muffin


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 0.9.0-7
- Update npm(glob) dependency

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 04 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.9.0-5
- fix version of npm(q) dependency

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 20 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.9.0-2
- make versioned dependencies less specific

* Sun May 26 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.9.0-1
- update to upstream release 0.9.0
- now using uglify-js 2.x branch
- patches for new q API have now been upstreamed
- add symlink for cloc.pl

* Wed Feb 13 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.0-1
- initial package
