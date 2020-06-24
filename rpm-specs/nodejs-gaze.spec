%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:       nodejs-gaze
Version:    1.1.3
Release:    3%{?dist}
Summary:    A globbing fs.watch wrapper built from parts of other watch libraries
License:    MIT
URL:        https://github.com/shama/gaze
Source0:    http://registry.npmjs.org/gaze/-/gaze-%{version}.tgz
# Source1 is generated by running Source10, which pulls from the upstream
# version control repository.
Source1:    tests-%{version}.tar.bz2
Source2:    https://raw.githubusercontent.com/shama/gaze/v%{version}/Gruntfile.js
Source10:   dl-tests.sh

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(async)
BuildRequires:  npm(globule)
BuildRequires:  npm(grunt)
BuildRequires:  npm(grunt-cli)
BuildRequires:  npm(grunt-contrib-nodeunit)
BuildRequires:  npm(nodeunit)
BuildRequires:  npm(rimraf)
%endif

%description
This Node.js module provides a globbing fs.watch wrapper built from the best
parts of other fine watch libraries: speedy data behavior from chokidar, the
API interface from watch, and file globbing using glob.


%prep
%setup -q -n package
%setup -q -T -D -a 1 -n package
cp -p %{SOURCE2} .

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/gaze
cp -pr package.json lib/ \
    %{buildroot}%{nodejs_sitelib}/gaze

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
/usr/bin/grunt nodeunit -v
%endif


%files
%doc LICENSE-MIT README.md
%{nodejs_sitelib}/gaze


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 18 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.1.3-2
- Remove hardcoded fixdep on outdated version of globule.

* Tue Sep 24 2019 Jared K. Smith <jsmith@fedoraproject.org> - 1.1.3-1
- Update to upstream 1.1.3 release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 30 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.1-2
- fix versioned dependency on npm(globule)

* Sat Mar 29 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.1-1
- update to upstream release 0.5.1
- enable tests

* Mon Aug 26 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.1-1
- update to upstream release 0.4.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.3.4-2
- restrict to compatible arches

* Sat May 25 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.3.4-1
- update to upstream release 0.3.4

* Sat Mar 09 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.3.3-2
- shorten the %%summary

* Sun Feb 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.3.3-1
- initial package
