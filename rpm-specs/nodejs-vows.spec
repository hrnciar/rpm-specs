%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:           nodejs-vows
Version:        0.8.3
Release:        2%{?dist}
Summary:        Asynchronous behavior-driven development (BDD) and continuous integration

License:        MIT
URL:            https://github.com/cloudhead/vows
Source0:        http://registry.npmjs.org/vows/-/vows-%{version}.tgz
# Custom man page
Source1:        vows.1
# Patch --supress-stdout to work with Node.js 8.x
Patch0:         nodejs-vows-supress-stdout.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  coffee-script
BuildRequires:  npm(diff)
BuildRequires:  npm(eyes)
BuildRequires:  npm(glob)
%endif

%description
Vows is an asynchronous behavior-driven development (BDD) framework for
Node.js.

Vows was built from the ground up to test asynchronous code. It
executes your tests in parallel when it makes sense, and sequentially
when there are dependencies. Emphasis was put on speed of execution,
clarity and user experience.


%prep
%autosetup -p 1 -n package
%nodejs_fixdep diff "^1.0.8"
%nodejs_fixdep glob "^6.0.3"
rm -rf node_modules


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/vows
cp -pr package.json lib/ %{buildroot}%{nodejs_sitelib}/vows
mkdir -p %{buildroot}%{nodejs_sitelib}/vows/bin
install -p -D -m0755 bin/vows %{buildroot}%{nodejs_sitelib}/vows/bin/vows
mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/vows/bin/vows %{buildroot}%{_bindir}/vows
mkdir -p %{buildroot}%{_mandir}/man1
install -p -D -m0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/vows.1
%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
./bin/vows test/*.js
%endif


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/vows
%{_bindir}/vows
%{_mandir}/man1/vows.1*


%changelog
* Wed Feb  5 2020 Tom Hughes <tom@compton.nu> - 0.8.3-2
- Update npm(diff) dependency

* Wed Feb  5 2020 Tom Hughes <tom@compton.nu> - 0.8.3-1
- Update to 0.8.3 upstream release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Tom Hughes <tom@compton.nu> - 0.8.2-10
- Update to 0.8.2 upstream release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 10 2017 Tom Hughes <tom@compton.nu> - 0.8.1-9
- Rebuild for rpm 4.13 downgrade

* Thu Aug 10 2017 Tom Hughes <tom@compton.nu> - 0.8.1-8
- Patch tests to work with Node.js 8.x

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 0.8.1-4
- Update npm(glob) dependency

* Thu Oct 29 2015 Jared Smith <jsmith@fedoraproject.org> - 0.8.1-3
- Allow newer version of npm(diff) and npm(glob)

* Sun Oct 25 2015 Tom Hughes <tom@compton.nu> - 0.8.1-2
- Fix glob dependency

* Sun Oct 25 2015 Tom Hughes <tom@compton.nu> - 0.8.1-1
- Update to 0.8.1 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 20 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.0-8
- add nodejs_find_provides_and_requires macro

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 06 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.0-6
- fix nodejs-glob dependency

* Sat May 25 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.0-5
- make versioned dependency on nodejs-glob less specific

* Sun Apr 07 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.0-4
- use node-glob instead of wildcard.js, which is bundled from unknown origins
- add a more detailed %%description
- add /usr/bin/vows
- add custom man page

* Sun Mar 10 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.0-3
- fix typo in %%summary

* Sat Mar 02 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.0-2
- add ASL 2.0 to License tag
- remove /usr/bin/vows symlink

* Thu Feb 14 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.0-1
- initial package
