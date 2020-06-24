%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:       jasmine-node
Version:    1.14.3
Release:    14%{?dist}
Summary:    DOM-less JS behavior-driven development (BDD) testing framework for Node
License:    MIT
URL:        https://github.com/mhevery/jasmine-node
Source0:    http://registry.npmjs.org/jasmine-node/-/jasmine-node-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

# Remove the version from jasmine.js location.
Patch0:     %{name}-1.14.3-Fix-location-of-jasmine.js.patch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  coffee-script
BuildRequires:  npm(fileset)
BuildRequires:  npm(gaze)
BuildRequires:  npm(jasmine-reporters)
BuildRequires:  npm(jasmine-growl-reporter)
BuildRequires:  npm(mkdirp)
BuildRequires:  npm(requirejs)
BuildRequires:  npm(walkdir)
# These are required for the files we're unbundling.
BuildRequires:  jasmine
BuildRequires:  npm(require-cs)
%endif

# We are symlinking to these files, so explicitly depend on them just in case
# the packages that own them decide to move them somewhere else.
Requires:       /usr/lib/node_modules/require-cs/cs.js
Requires:       /usr/share/jasmine/jasmine.js

%description
%{summary}.


%prep
%setup -q -n package
%patch0 -p1
rm -f lib/jasmine-node/cs.js
rm -f lib/jasmine-node/jasmine-*.js
# Lots of files are executable but shouldn't be.
find . -type f ! -iname 'specs*' -exec chmod 0644 '{}' \;

%nodejs_fixdep gaze '~0.5'
%nodejs_fixdep jasmine-growl-reporter '~0.2'
%nodejs_fixdep mkdirp '^0.5.1'


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/jasmine-node
cp -pr package.json lib/ \
    %{buildroot}%{nodejs_sitelib}/jasmine-node
mkdir -p %{buildroot}%{nodejs_sitelib}/jasmine-node/bin
install -p -D -m0755 bin/jasmine-node \
    %{buildroot}%{nodejs_sitelib}/jasmine-node/bin/jasmine-node
mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/jasmine-node/bin/jasmine-node \
    %{buildroot}%{_bindir}/jasmine-node

# Replace bundled cs.js with symlink.
mkdir -p %{buildroot}%{nodejs_sitelib}/jasmine-node/lib/jasmine-node
ln -sf %{nodejs_sitelib}/require-cs/cs.js \
    %{buildroot}%{nodejs_sitelib}/jasmine-node/lib/jasmine-node/cs.js
# Replace bundled jasmine.js with symlink.
ln -sf %{_datadir}/jasmine/jasmine.js \
    %{buildroot}%{nodejs_sitelib}/jasmine-node/lib/jasmine-node/jasmine.js

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
ln -sf %{nodejs_sitelib}/require-cs/cs.js \
    lib/jasmine-node/cs.js
ln -sf %{_datadir}/jasmine/jasmine.js \
    lib/jasmine-node/jasmine.js
# Some of the tests fail, but apparently they *should* fail.
./specs.sh
%endif


%files
%doc LICENSE README.md
%{nodejs_sitelib}/jasmine-node
%{_bindir}/jasmine-node


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Tom Hughes <tom@compton.nu> - 1.14.3-11
- Update npm(gaze) dependency

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 1.14.3-5
- Update npm(mkdirp) dependency

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 19 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.14.3-2
- fix version of npm(jasmine-growl-reporter) dependency

* Sat Mar 29 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.14.3-1
- update to upstream release 1.14.3

* Mon Aug 26 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.11.0-1
- update to upstream release 1.11.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 27 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.10.0-1
- update to upstream release 1.10.0
- restrict to compatible arches

* Sat May 25 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.7.1-1
- update to upstream release 1.7.1

* Wed Mar 20 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.4.0-3
- add missing BuildRequires for the tests and add the necessary symlinks

* Sun Mar 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.4.0-2
- amend path to jasmine.js

* Sun Mar 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.4.0-1
- update to upstream release 1.4.0
- rename from nodejs-jasmine-node to just jasmine-node
- remove bundled cs.js and jasmine.js and replace with symlinks to system
  versions
- lots of files are executable but shouldn't be, so chmod 0644 all of them
- add a custom man page

* Sat Mar 02 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2.3-2
- amend typo in the summary

* Sun Feb 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2.3-1
- initial package
