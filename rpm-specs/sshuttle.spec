Name:               sshuttle
Version:            1.0.4
Release:            1%{?dist}
Summary:            Transparent Proxy VPN
Source0:            https://files.pythonhosted.org/packages/source/s/%{name}/%{name}-%{version}.tar.gz
URL:                https://github.com/%{name}/%{name}
License:            LGPLv2+
BuildArch:          noarch
# disable flake8 tests. These should be done upstream and while they pass in rawhide, 
# it's not possible to run them in epel or older fedora branches.
Patch1:             sshuttle-no-flake8.patch

#
# backport python2 on remote site support. 
#
Patch2: https://github.com/sshuttle/sshuttle/commit/19f653df36d818531e35a03c02df4bda8a192bc0.patch

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-setuptools_scm
BuildRequires:      python3-pytest-runner
BuildRequires:      python3-mock
BuildRequires:      python3-sphinx
BuildRequires:      texinfo

# For tests
BuildRequires:      python3-pytest
BuildRequires:      python3-pytest-cov
BuildRequires:      python3-pytest-runner
BuildRequires:      python3-pytest-mock

Requires:           iptables
Requires:           openssh-clients

%description
Transparent proxy server that works as a poor man's VPN. Forwards over ssh.
Doesn't require admin. Works with Linux and MacOS. Supports DNS tunneling.

%prep
%autosetup -p1 -n %{name}-%{version}

# This file is a script, so shouldn't be installed under
# site-packages. We'll remove it for now.
rm %{name}/stresstest.py


%build
%py3_build

# Build docs
pushd docs
make man
make info
popd


%install
%py3_install

# Install docs
pushd docs
# Man
mkdir -p %{buildroot}/%{_mandir}/man1
mv _build/man/%{name}.1 %{buildroot}/%{_mandir}/man1
# Info
mkdir -p %{buildroot}/%{_infodir}
mv _build/texinfo/%{name}.info %{buildroot}/%{_infodir}
popd


%check
%{__python3} setup.py test

%files
%license LICENSE
%{_mandir}/man1/%{name}.1.*
%{_infodir}/%{name}.info.*
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}*.egg-info
%{_bindir}/sshuttle
%{_bindir}/sudoers-add


%changelog
* Sun Aug 30 2020 Kevin Fenzi <kevin@scrye.com> - 1.0.4-1
- Update to 1.0.4. Fixes bug #1856063
- Apply upstream commit to fix python2 compat on remote side. Fixes bug #1851622

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 19 2020 Kevin Fenzi <kevin@scrye.com> - 1.0.2-1
- Update to 1.0.2. Fixes bug #1848196

* Thu Jun 11 2020 Kevin Fenzi <kevin@scrye.com> - 1.0.1-1
- Update to 1.0.1. Fixed bug #1844272

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.78.5-9
- Rebuilt for Python 3.9

* Sat May 16 2020 Kevin Fenzi <kevin@scrye.com> - 0.78.5-8
- Drop flake8 check at build time to allow epel8 building. Fixes #1757034

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.78.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.78.5-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.78.5-5
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.78.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 0.78.5-3
- Remove obsolete requirements for %%post/%%preun scriptlets

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.78.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Kevin Fenzi <kevin@scrye.com> - 0.78.5-1
- Update to 0.78.5. Fixes bug #1669944

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.78.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.78.4-4
- Rebuilt for Python 3.7

* Tue Apr  3 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.78.4-3
- Simplify spec file by making it Python 3 only

* Tue Apr  3 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.78.4-2
- Add %%check section to spec file and run tests
- Add BuildRequires for python{2,3}-mock

* Tue Apr  3 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.78.4-1
- Update to 0.78.4
- Fix broken Source0 URL

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.78.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.78.3-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.78.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Kevin Fenzi <kevin@scrye.com> - 0.78.3-1
- Update to 0.78.3. Fixes bug #1468857

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.78.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.78.1-3
- Rebuild for Python 3.6

* Sun Sep 11 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.78.1-2
- Add sshuttle-0.78.1-pytest-runner.patch to move pytest-runner
  requirement from setup_requires to tests_requires in setup.py
- Only BR python[2,3]-pytest-runner on F24 and higher

* Sun Sep 11 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.78.1-1
- Update to 0.78.1
- Add BR for python[2,3]-pytest-runner

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.78.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Apr 11 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.78.0-2
- Use PyPi source tarball rather than rolling our own (only needed
  when building git snapshots)

* Sun Apr 10 2016 Kevin Fenzi <kevin@scrye.com> - 0.78.0-1
- Update to 0.78.0. Fixes bug #1325602
- Drop upstreamed patches

* Sat Apr  2 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.77.3-0.1.20160402git6e15e691
- Update to git snapshot
- Add patch to work with older python versions on server end

* Mon Mar  7 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.77.2-1
- Update to 0.77.2
- Use PyPi tarball instead of rolling our own from git
- Fixup typos in spec file changelog

* Sat Mar  5 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.77-5
- Build and package info file
- Use macros more consistently in spec file
- Move building of docs to %%build section of spec
- Remove the stresstest.py script

* Sat Mar  5 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.77-4
- Move to using hand-rolled tar balls rather than the github release
- Drop patch to set version manually
- Build and package man page
- BuildRequire the correct version of setuptools_scm

* Sat Mar  5 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.77-3
- Build with Python 3 on F24 too

* Sat Mar  5 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.77-2
- Use Python 3 for Fedora 25 and beyond, otherwise Python 2

* Sat Mar  5 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.77-1
- Update to 0.77
- Disable doc building for now
- Add patch to set version to allow build to complete
- Use python3 by default
- Use python packaging macros

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-12.20120810git9ce2fa0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-11.20120810git9ce2fa0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-10.20120810git9ce2fa0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-9.20120810git9ce2fa0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-8.20120810git9ce2fa0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 07 2013 Marcel Wysocki <maci@satgnu.net> - 0-7.20120810git9ce2fa0
- don't use doc macro for files in mandir

* Fri Nov 23 2012 Marcel Wysocki <maci@satgnu.net> - 0-6.20120810git9ce2fa0
- fixed hash ( woops, where did that g come from )
- fixed date to be commit date and not clone date
- use version 0 
- use datadir instead of /usr/local
- remove sshuttle.md in favor of the manpage
- remove make from BR
- added comment on how to create the source tarball

* Wed Oct 31 2012 Marcel Wysocki <maci@satgnu.net> - 20121019-5.gitg9ce2fa0
- remove python from deps and builddeps, rpm picks it up automatically 
- add manual page
- add missing builddep for manual generation

* Mon Oct 22 2012 Marcel Wysocki <maci@satgnu.net> - 20121019-4.gitg9ce2fa0
- add missing dependencies

* Mon Oct 22 2012 Marcel Wysocki <maci@satgnu.net> - 20121019-3.gitg9ce2fa0
- Don't use macros for rm, install, chmod and cp.
- Remove defattr, since we're not going for EPEL4.
- Remove the clean section since we're not going for EPEL5.

* Fri Oct 19 2012 Marcel Wysocki <maci@satgnu.net> - 20121019-2.gitg9ce2fa0
- use .tar.gz instead of .zip

* Fri Oct 19 2012 Marcel Wysocki <maci@satgnu.net> - 20121019-1.gitg9ce2fa0
- update to newer spapshot
- adhere more to packaging guidelines

* Thu Oct 18 2012 Marcel Wysocki <maci@satgnu.net> - 0.20121018-3
- update to newer spapshot
- fedora port
- adhere more to packaging guidelines

* Wed May  4 2011 pascal.bleser@opensuse.org
- initial version (0.20110503)
