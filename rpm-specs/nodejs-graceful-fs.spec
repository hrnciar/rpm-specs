%{?nodejs_find_provides_and_requires}

# tests diabled due to failing "ENOENT" tests
%global enable_tests 1

Name:           nodejs-graceful-fs
Version:        4.2.0
Release:        4%{?dist}
Summary:        A drop-in replacement for fs, making various improvements
License:        BSD
URL:            https://github.com/isaacs/node-graceful-fs
Source0:        https://github.com/isaacs/node-graceful-fs/archive/v%{version}/%{name}-%{version}.tar.gz
# Work around limitations in old version of tap
Patch0:         nodejs-graceful-fs-tap.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tap)
BuildRequires:  npm(rimraf)

%description
A drop-in replacement for fs, making various improvements.

The improvements are meant to normalize behavior across different
platforms and environments, and to make filesystem access more
resilient to errors.

Improvements over fs module

* Queues up open and readdir calls, and retries them once something
  closes if there is an EMFILE error from too many file descriptors.
* Fixes lchmod for Node versions prior to 0.6.2.
* Implements fs.lutimes if possible. Otherwise it becomes a noop.
* Ignores EINVAL and EPERM errors in chown, fchown or lchown if the
  user isn't root.
* Makes lchmod and lchown become noops, if not available.
* Retries reading a file if read results in EAGAIN error.

On Windows, it retries renaming a file for up to one second if EACCESS
or EPERM error occurs, likely because antivirus software has locked the
directory.


%prep
%autosetup -p 1 -n node-graceful-fs-%{version}


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/graceful-fs
cp -p package.json graceful-fs.js polyfills.js legacy-streams.js clone.js \
    %{buildroot}%{nodejs_sitelib}/graceful-fs
%nodejs_symlink_deps



%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
# Disable test that needs import-fresh
rm test/avoid-memory-leak.js
%{_bindir}/tap test/*.js
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/graceful-fs


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Tom Hughes <tom@compton.nu> - 4.2.0-2
- Include clone.js

* Wed Jun 26 2019 Tom Hughes <tom@compton.nu> - 4.2.0-1
- Update to 4.2.0 upstream release
- Enable tests with patch for old version of tap

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 18 2017 Jared Smith <jsmith@fedoraproject.org> - 4.1.11-1
- Update to upstream 4.1.11 release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb  3 2016 Tom Hughes <tom@compton.nu> - 4.1.3-1
- Update to 4.1.3 upstream release

* Thu Dec 31 2015 Tom Hughes <tom@compton.nu> - 4.1.2-1
- Update to 4.1.2 upstream release
- Enable tests

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.0.0-2
- include missing polyfills.js file

* Fri Jul 12 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.0.0-1
- new upstream release 2.0.0
- license file now updated upstream

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.2-1
- new upstream release 1.2.2

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.1-3
- restrict to compatible arches

* Mon May 27 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2.1-2
- the LICENSE file previously contained the wrong license (MIT), but now
  upstream have fixed it to contain the correct license (BSD) (#967442)

* Sat May 25 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2.1-1
- update to upstream release 1.2.1

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.0-2
- add macro for EPEL6 dependency generation

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.0-1
- new upstream release 1.2.0

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.14-2
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.14-1
- new upstream release 1.1.14
- clean up for submission

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.8-2
- guard Requires for F17 automatic depedency generation

* Thu Mar 22 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.8-1
- new upstream release 1.1.8

* Sun Jan 29 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.5-1
- new upstream release 1.1.5

* Sat Jan 21 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.4-2
- missing Group field for EL5

* Sat Jan 21 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.4-1
- new upstream release 1.1.4

* Thu Nov 10 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.2-0.1.20111109git33dee97
- new upstream release
- Node v0.6.0 compatibility fixes

* Tue Oct 25 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.1-1
- new upstream release

* Mon Aug 22 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.0-1
- initial package
