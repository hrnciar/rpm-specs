%{?nodejs_find_provides_and_requires}

Name:           node-gyp
Version:        3.6.0
Release:        11%{?dist}
Summary:        Node.js native addon build tool
License:        MIT
URL:            https://github.com/nodejs/node-gyp
Source0:        https://github.com/nodejs/node-gyp/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        addon-rpm.gypi
# use RPM installed headers by default instead of downloading a source tree
# for the currently running node version
Patch1:         node-gyp-addon-gypi.patch
# use the system gyp
Patch2:         node-gyp-system-gyp.patch
# remove test that checks for existence of unsuffixed python
Patch3:         node-gyp-python.patch
# fix tests for changes in Node.js 12.x
Patch4:         node-gyp-node12.patch
# default to python3 instead of python2
Patch5:         node-gyp-python3.patch
# handle beta versions of python
Patch6:         node-gyp-beta.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

# gyp is the actual build framework node-gyp uses
Requires:       gyp >= 0.1-0.31
# this is the standard set of headers expected to build any node native module
Requires:       nodejs-devel libuv-devel http-parser-devel
# we also need a C++ compiler to actually build stuff ;-)
Requires:       gcc-c++

BuildRequires:  gyp
BuildRequires:  nodejs-devel libuv-devel http-parser-devel
BuildRequires:  gcc-c++

BuildRequires:  npm(tape)
BuildRequires:  npm(bindings)
BuildRequires:  npm(fstream)
BuildRequires:  npm(glob)
BuildRequires:  npm(graceful-fs)
BuildRequires:  npm(minimatch)
BuildRequires:  npm(mkdirp)
BuildRequires:  npm(nan)
BuildRequires:  npm(nopt)
BuildRequires:  npm(npmlog)
BuildRequires:  npm(osenv)
BuildRequires:  npm(path-array)
BuildRequires:  npm(request)
BuildRequires:  npm(require-inject)
BuildRequires:  npm(rimraf)
BuildRequires:  npm(semver)
BuildRequires:  npm(tar)
BuildRequires:  npm(which)

%description
node-gyp is a cross-platform command-line tool written in Node.js for compiling
native addon modules for Node.js, which takes away the pain of dealing with the
various differences in build platforms. It is the replacement to the node-waf
program which is removed for node v0.8.


%prep
%autosetup -p1
cp -p %{SOURCE1} addon-rpm.gypi
%nodejs_fixdep glob "^6.0.4"
%nodejs_fixdep minimatch "^3.0.0"
rm -rf gyp


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/node-gyp
cp -pr addon*.gypi bin lib package.json %{buildroot}%{nodejs_sitelib}/node-gyp
mkdir -p %{buildroot}%{_bindir}
ln -sf ../lib/node_modules/node-gyp/bin/node-gyp.js %{buildroot}%{_bindir}/node-gyp
%nodejs_symlink_deps


%check
%{nodejs_symlink_deps} --check
%{nodejs_sitelib}/tape/bin/tape test/test-*.js


%files
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitelib}/node-gyp
%{_bindir}/node-gyp


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 23 2019 Tom Hughes <tom@compton.nu> - 3.6.0-10
- Handle beta versions of python

* Thu Aug 15 2019 Tom Hughes <tom@compton.nu> - 3.6.0-9
- Default to python3 instead of python2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 16 2017 Tom Hughes <tom@compton.nu> - 3.6.0-3
- Remove npm(semver) dependency fix

* Thu Mar 16 2017 Tom Hughes <tom@compton.nu> - 3.6.0-2
- Fix npm(semver) dependency

* Thu Mar 16 2017 Tom Hughes <tom@compton.nu> - 3.6.0-1
- Update to 3.6.0 upstream release

* Thu Mar  2 2017 Tom Hughes <tom@compton.nu> - 3.5.0-1
- Update to 3.5.0 upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Peter Robinson <pbrobinson@fedoraproject.org> 3.2.1-4
- Drop v8-devel requires, bundled with nodejs

* Tue Jan 19 2016 Tom Hughes <tom@compton.nu> - 3.2.1-3
- Build with node 4 compatible include path

* Tue Jan 19 2016 Tom Hughes <tom@compton.nu> - 3.2.1-2
- Build with node 0.10 compatible include path

* Mon Jan 18 2016 Tom Hughes <tom@compton.nu> - 3.2.1-1
- Update to 3.2.1 upstream release
- Enable tests

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 0.10.6-13
- Update npm(semver) dependency for nodejs 4.2

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 0.10.6-12
- Update npm(minimatch) dependency
- Update npm(glob) dependency

* Thu Dec 31 2015 Tom Hughes <tom@compton.nu> - 0.10.6-11
- Update npm(semver) dependency for nodejs 4.2

* Thu Dec 31 2015 Tom Hughes <tom@compton.nu> - 0.10.6-10
- Update npm(tar) dependency

* Thu Dec 31 2015 Tom Hughes <tom@compton.nu> - 0.10.6-9
- Update npm(semver) dependency

* Thu Dec 31 2015 Tom Hughes <tom@compton.nu> - 0.10.6-8
- Update npm(fstream) dependency

* Thu Dec 31 2015 Tom Hughes <tom@compton.nu> - 0.10.6-7
- Update npm(graceful-fs) dependency

* Thu Dec 10 2015 Tom Hughes <tom@compton.nu> - 0.10.6-6
- Update npm(semver) dependency for nodejs 4.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.6-4
- fixup include order for compat-libuv010 (RHBZ#1213047)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.6-2
- fix semver dep

* Fri Jul 12 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.6-1
- new upstream release 0.10.6

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.10.1-1
- new upstream release 0.10.1

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.5-3
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.5-2
- add macro for EPEL6 dependency generation

* Wed Apr 03 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.5-1
- new upstream release 0.9.5

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.1-2
- update addon-rpm.gypi
- split out addon-rpm.gypi so it's easier to maintain

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.1-1
- new upstream release 0.9.1

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.8.4-1
- new upstream release 0.8.4

* Mon Jan 21 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.8.3-1
- new upstream release 0.8.3
- add missing Requires on http-parser-devel

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.8.2-3
- add missing build section

* Sat Jan 05 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.8.2-2
- use RPM-installed headers by default
- now patched to use the system gyp instead of relying on a symlink

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.8.2-1
- new upstream release 0.8.2
- clean up for submission

* Thu Apr 26 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.1-2
- fix dependencies

* Wed Apr 18 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.1-1
- New upstream release 0.4.1

* Fri Apr 06 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.11-1
- New upstream release 0.3.11

* Mon Apr 02 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.10-1
- New upstream release 0.3.10

* Thu Mar 29 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.9-1
- New upstream release 0.3.9

* Wed Mar 28 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.8-1
- new upstream release 0.3.8

* Thu Mar 22 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.7-1
- new upstream release 0.3.7

* Thu Mar 15 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.5-1
- initial package
