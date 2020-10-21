%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

Name:           fedora-packager
Version:        0.6.0.4
Release:        2%{?dist}
Summary:        Tools for setting up a fedora maintainer environment

License:        GPLv2+
URL:            https://pagure.io/fedora-packager
Source0:        https://fedorahosted.org/releases/f/e/fedora-packager/fedora-packager-%{version}.tar.bz2

BuildRequires:  python3-devel
Requires:       koji >= 1.11.0
Requires:       bodhi-client
Requires:       rpm-build rpmdevtools rpmlint
Requires:       mock curl openssh-clients
Requires:       redhat-rpm-config
Requires:       fedpkg >= 1.0
Obsoletes:      fedora-cert < 0.6.0.3-4
# This is the version in which SNI was fixed
%if 0%{?fedora}
Requires:       krb5-workstation >= 1.14.3-4
%else
%if 0%{?rhel} >= 7
Requires:       krb5-workstation  >= 1.14.1-24
%else
# older rhels wont fully work without configuration, but lets make sure they have krb
# we should be able to assume newer RHELs's will have a new enough version
Requires:       krb5-workstation
%endif
%endif
Recommends:     fedora-packager-yubikey

BuildArch:      noarch

%description
Set of utilities useful for a fedora packager in setting up their environment.

%package yubikey
Summary:        tool for setting up a yubikey for use in Fedora
# For fedora-burn-yubikey.py
Requires:       python3-yubico
Recommends:     ykpers

BuildArch:      noarch

%description yubikey
A tool for setting up a yubikey for use in fedora

%prep
%setup -q

%build
%configure PYTHON=%{__python3}
%make_build

%install
%make_install
sed -i -r 's|#!/usr/bin/python$|#!%{__python3}|' %{buildroot}/usr/*bin/*

%files
%license COPYING
%doc TODO AUTHORS ChangeLog
%{_bindir}/*
%exclude %{_bindir}/fedora-hosted
%exclude %{_bindir}/fedora-packager-setup
%exclude %{_bindir}/fedoradev-pkgowners
%exclude %{_bindir}/fedora-cert
%exclude %{python3_sitelib}/fedora_cert

%config(noreplace) %{_sysconfdir}/koji.conf.d/* 
%config(noreplace) %{_sysconfdir}/krb5.conf.d/*

%files yubikey
%license COPYING
%{_sbindir}/*

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 31 2020 Mohan Boddu <mboddu@bhujji.com> - 0.6.0.4-1
- Rebase to 0.6.0.4
  * Remove obsolete fedora-packager-setup (tmz)
  * Drop mercurial formatting from .gitignore (tmz)
  * Fix for rhbz #1412260 (sergio)
  * Option for the mode_yubikey_otp must be bytes and not string. (cverna)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Dennis Gilmore <dennis@ausil.us> - 0.6.0.2-7
- move fedora-burn-yubikey to a subpackge rhbz#756413

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.6.0.2-4
- Drop obsolete scripts, switch over to python 3 (#1024796)
  * fedora-burn-yubikey is python3 compatible
  Those old scripts have been removed:
  * fedora-hosted is for fedorahosted.org, which doesn't exist anymore
  * fedora-packager-setup and fedora-cert download certificates, which
    have been replaced by kerberos authentication
  * fedoradev-pkgowners talks to pkgdb, which is no more
  The fedora-cert python2 package is also removed.
  The other scripts are most likely obsolete too, but they are just bash
  wrappers around other tools, so they are still packaged.

* Tue Jul 31 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.0.2-3
- Do not require packagedb-cli, it's not used anymore (#1024838)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 01 2018 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.6.0.2-1
- Rebase to 0.6.0.2

* Thu Mar 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6.0.1-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Dennis Gilmore <Dennis@ausil.us> - 0.6.0.1-1
- install and include the new config file names (dennis)
- rename configs and enable fast upload (dennis)
- Configuration files in /etc/koji.conf.d need to end with .conf (puiterwijk)

* Sun Dec 11 2016 Dennis Gilmore <Dennis@ausil.us> - 0.6.0.0-2
- fix up krb5-workstation requires

* Fri Dec 09 2016 Dennis Gilmore <Dennis@ausil.us> - 0.6.0.0-1
- Make scripts executable in GIT (opensource)
- Update bugzilla owners URL everywhere (opensource)
- Properly except AuthError (opensource)

* Tue Oct 25 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.5.10.7-4
- Added kerberos configuration

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10.7-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun May 22 2016 Till Maas <opensource@till.name> - 0.5.10.7-2
- Use %%license
- Update URL
- Add fedora-cert Requires: python-fedora (#1213068) (Mike DePaulo <mikedep333@gmail.com>)
- Add Requires: python-offtrac (#1213075) (Mike DePaulo <mikedep333@gmail.com>)
- Require python-yubico

* Tue Mar 01 2016 Dennis Gilmore <dennis@ausil.us> - 0.5.10.7-1
- 0.5.10.7 release (dennis)
- add stg-koji command and fix up secondary configs (dennis)
- switch to tar-pax so I can make tarballs (dennis)
- Make fedora-packager-setup work with Python 3 (ville.skytta)
- Make fedora-cert work with Python 3 (ville.skytta)
- Python 3 fixes (ville.skytta)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.10.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 11 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.5.10.6-1
- Reworked yubikey code to use python-yubico rather than subprocess (puiterwijk)
- Use python API to write yubikey (puiterwijk)
- fedora-cert: Fix checking against the CRL (bochecha)
- fedora-cert: Fix typo (bochecha)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 24 2014 Dennis Gilmore <dennis@ausil.us> - 0.5.10.5-1
- remove fedora-cvs script as the cvs server no longer exists (dennis)
- Make fas url configurable for fedora-server-ca.cert. (rbean)
- Remove unused imports. (rbean)
- Remove another unused import. (rbean)
- Conditionalize CRL checking for el6. (rbean)
- Remove unused imports. (rbean)
- Add CRL checking to fedora-cert. (rbean)
- fedoradev-pkgowners: Update pkgdb URL (opensource)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 23 2014 Nick Bebout <nb@fedoraproject.org> - 0.5.10.4-1
- fix fedora-burn-yubikey script to add -oserial-api-visible

* Tue Mar 18 2014 Nick Bebout <nb@fedoraproject.org> - 0.5.10.3-1
- fix fedora-burn-yubikey script to work with slot 2

* Thu Dec 05 2013 Denis Gilmore <dennis@ausil.us> - 0.5.10.2-1
- update to 0.5.10.2
- drop sparc support

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 03 2013 Adam Jackson <ajax@redhat.com> 0.5.10.1-2
- Requires: packagedb-cli (which also pulls in python-bugzilla)

* Mon Dec 03 2012 Nick Bebout <nb@fedoraproject.org> - 0.5.10.1-1
- fix fedora-burn-yubikey to allow specifying what slot to use

* Fri Aug 03 2012 Dennis Gilmore <dennis@ausil.us> - 0.5.10.0-1
- fix up secondary arch configs for newer koji
- clean up message for browser import

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 08 2011 Jesse Keating <jkeating@redhat.com> - 0.5.9.6-1
- Install secondary-arch files correctly

* Mon Nov 07 2011 Jesse Keating <jkeating@redhat.com> - 0.5.9.5-1
- Move fedpkg to it's own package, no longer part of fedora-packager

* Fri Oct 28 2011 Jesse Keating <jkeating@redhat.com> - 0.5.9.4-1
- Overload curl stuff (jkeating)
- Hardcode fedpkg version requires (jkeating)
- Fix up changelog date (jkeating)

* Thu Oct 27 2011 Jesse Keating <jkeating@redhat.com> - 0.5.9.3-1
- Use the new plugin setup with rpkg
- Change fedpkg version number to 1.0

* Sat Aug 27 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.5.9.2-2
- Fix operating URL of fedoradev-pkgowners (BZ #575517).

* Sun May 22 2011 Jesse Keating <jkeating@redhat.com> - 0.5.9.2-1
- Strip the .py off of fixbranches (jkeating)
- Unconditionally check for new branch style (jkeating)
- Stop setting push.default (#705468) (jkeating)
- Make sure packages are built before lint (#702893) (jkeating)
- Except more build submission errors (#702235) (jkeating)
- Move the fixbranches.py script out of the $PATH (#698646) (jkeating)
- fedpkg: Support branch completion on non-default remotes (tmz)
- fedpkg: Update bash completion for new branch names (tmz)
- Fix retiring a package with a provided message (#701626) (jkeating)
- add arm specific and s390 specific packages so they get sent to the right
  place (dennis)
- initial go at using consistent targets across all targets dist-rawhide is
  still used for master branch (dennis)
- only pass in a target arch to local builds when specified on the command line
  some arches notably x86, arm and sparc dont build for the base arch you end
  up with .i386 .arm or .sparc rpms when you really want something else
  (dennis)

* Thu Apr 14 2011 Jesse Keating <jkeating@redhat.com> - 0.5.9.0-1
- Add a check for new-style branches (jkeating)
- Add a force option (jkeating)
- Add ability to check status of conversion (jkeating)
- Add a dry-run option (jkeating)
- Add a client side script to fix branch data (jkeating)

* Sat Apr 09 2011 Jesse Keating <jkeating@redhat.com> - 0.5.8.1-1
- Man page comment syntax fix. (ville.skytta)
- Make sure the bodhi.template file got written out (#683602) (jkeating)
- Wrap the diff in a try (#681789) (jkeating)
- Don't try to upload directories. (#689947) (jkeating)
- Fix tag-request (#684418) (jkeating)

* Fri Mar 04 2011 Jesse Keating <jkeating@redhat.com> - 0.5.7.0-1
- If chain has sets, handle them right (#679126) (jkeating)
- Fix "fedpkg help" command (make it work again) (#681242) (hun)
- Always generate a new srpm (#681359) (jkeating)
- Fix up uses of path (ticket #96) (jkeating)
- Clean up hardcoded "origin" (ticket #95) (jkeating)
- Fix obvious error in definition of curl command (pebolle)

* Wed Feb 23 2011 Jesse Keating <jkeating@redhat.com> - 0.5.6.0-1
- Fix improper use of strip() (jkeating)
- Improve the way we detect branch data (jkeating)
- Fix clone to work with old/new branch styles (jkeating)
- Add new and old support to switch_branches (jkeating)
- Update the regexes used for finding branches (jkeating)
- Don't use temporary editor files for spec (#677121) (jkeating)
- fedpkg requires rpm-build (#676973) (jkeating)
- Don't error out just from stderr from rpm (jkeating)

* Wed Feb 09 2011 Jesse Keating <jkeating@redhat.com> - 0.5.5.0-1
- Re-add 'lint' command hookup into argparse magic (hun)
- Catch errors parsing spec to get name. (#676383) (jkeating)

* Wed Feb 09 2011 Jesse Keating <jkeating@redhat.com> - 0.5.4.0-1
- Re-arrange verify-files and slight fixups (jkeating)
- Add "fedpkg verify-files" command (hun)
- Provide feedback about new-ticket. (ticket 91) (jkeating)
- Add the new pull options to bash completion (jkeating)
- Add a --rebase and --no-rebase option to pull (jkeating)
- Update the documentation for a lot of commands (jkeating)
- Handle working from a non-existent path (#675398) (jkeating)
- Fix an traceback when failing to watch a build. (jkeating)
- Handle arches argument for scratch builds (#675285) (jkeating)
- Trim the "- " out of clogs.  (#675892) (jkeating)
- Exit with an error when appropriate (jkeating)
- Add build time man page generator (hun)
- Add help text for global --user option (hun)
- Move argparse setup into parse_cmdline function (hun)
- Require python-hashlib on EL5 and 4 (jkeating)
- Catch a traceback when trying to build from local branch (jkeating)

* Mon Jan 31 2011 Jesse Keating <jkeating@redhat.com> 0.5.3.0-1
- Catch the case where there is no branch merge point (#622592) (jkeating)
- Fix whitespace (jkeating)
- Add an argument to override the "distribution" (jkeating)
- upload to lookaside cache tgz files (dennis)
- Handle traceback if koji is down or unreachable. (jkeating)
- If we don't have a remote branch, query koji (#619979) (jkeating)
- Add a method to create an anonymous koji session (jkeating)
- Make sure we have sources for mockbuild (#665555) (jwboyer) (jkeating)
- Revert "Make sure we have an srpm when doing a mockbuild (#665555)" (jkeating)
- Regenerate the srpm if spec file is newer (ticket #84) (jkeating)
- Improve cert failure message (Ticket 90) (jkeating)
- Get package name from the specfile. (Ticket 75) (jkeating)
- Handle anonymous clones in clone_with_dirs. (#660183) (ricky)
- Make sure we have an srpm when doing a mockbuild (#665555) (jkeating)
- Catch all errors from watching tasks. (#670305) (jkeating)
- Fix a traceback when koji goes offline (#668889) (jkeating)
- Fix traceback with lint (ticket 89) (jkeating)

* Wed Jan 05 2011 Dennis Gilmore <dennis@ausil.us> - 0.5.2.0-1
- new release see ChangeLog

* Tue Aug 24 2010 Jesse Keating <jkeating@redhat.com> - 0.5.1.4-1
- Fix setting push.default when cloning with dirs
- Remove build --test option in bash completion

* Mon Aug 23 2010 Jesse Keating <jkeating@redhat.com> - 0.5.1.3-1
- Error check the update call.  #625679
- Use the correct remote when listing revs
- Add the bash completion file
- make fedora-cvs only do anonymous chackouts since cvs is read only now.
- re-fix dist defines.
- Short cut the failure on repeated builds
- Allow passing srpms to the build command
- clone: set repo's push.default to tracking
- pull the username from fedora_cert to pass to bodhi
- Catch double ^c's from build.  RHBZ #620465
- Fix up chain building
- Add missing process call for non-pipe no tty.

* Thu Aug 12 2010 Dennis Gilmore <dennis@asuil.us> - 0.5.1.2-1
- fix rh bz 619733 619879 619935 620254 620465 620595 620648
- 620653 620750 621148 621808 622291 622716

* Fri Jul 30 2010 Dennis Gilmore <dennis@ausil.us> -0.5.1.0-2
- split fedpkg out on its own

* Thu Jul 29 2010 Dennis Gilmore <dennis@ausil.us> - 0.5.1.0-1
- wrap fedora-cert in try except 
- fedpkg fixes
- require python-kitchen on EL-4 and 5

* Wed Jul 28 2010 Dennis Gilmore <dennis@ausil.us> - 0.5.0.1-1
- Fix checking for unpushed changes on a branch

* Wed Jul 28 2010 Dennis Gilmore <dennis@ausil.us> - 0.5.0-1
- update to 0.5.0 with the switch to dist-git

* Thu Jul 08 2010 Dennis Gilmore <dennis@ausil.us> - 0.4.2.2-1
- new release with lost of fedpkg fixes

* Mon Jun 14 2010 Dennis Gilmore <dennis@ausil.us> - 0.4.2.1-1
- set devel for F-14
- point builds to koji.stg
- correctly create a git url for koji

* Tue Mar 23 2010 Dennis Gilmore <dennis@ausil.us> - 0.4.2-1
- update to 0.4.2
- adds missing fedora_cert. in fedora-packager-setup bz#573941
- Require python-argparse for fedpkg bz#574206
- Require make and openssh-clients bz#542209
- Patch to make cvs checkouts more robust bz#569954

* Wed Mar 03 2010 Dennis Gilmore <dennis@ausil.us> - 0.4.1-1
- update to 0.4.1 
- adds a missing "import sys" from fedora-cert bz#570370
- Require GitPython for fedpkg

* Fri Feb 26 2010 Dennis Gilmore <dennis@ausil.us> - 0.4.0-1
- update to 0.4.0 adds fedpkg 
- make a fedora_cert python library 
- add basic date check for certs 

* Tue Aug 04 2009 Jesse Keating <jkeating@redhat.com> - 0.3.8-1
- Add fedora-hosted and require offtrac

* Thu Jul 30 2009 Dennis Gilmore <dennis@ausil.us> - 0.3.7-1
- define user_cert in fedora-cvs before refrencing it 

* Tue Jul 28 2009 Dennis Gilmore <dennis@ausil.us> - 0.3.6-1
- use anon checkout when a fedora cert doesnt exist bz#514108
- quote arguments passed onto rpmbuild bz#513269

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 Dennis Gilmore <dennis@ausil.us> - 0.3.5-1
- add new rpmbuild-md5 script to build old style hash srpms
- it is a wrapper around rpmbuild

* Mon Jul  6 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.3.4-3
- add Requires: redhat-rpm-config to be sure fedora packagers are using all available macros

* Wed Jun 24 2009 Dennis Gilmore <dennis@ausil.us> - 0.3.4-2
- minor bump

* Mon Jun 22 2009 Dennis Gilmore <dennis@ausil.us> - 0.3.4-1
- update to 0.3.4 
- bugfix release with some new scripts

* Mon Mar 02 2009 Dennis Gilmore <dennis@ausil.us> - 0.3.3-1
- update to 0.3.3

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug 18 2008 Dennis Gilmore <dennis@ausil.us> - 0.3.1-1
- update to 0.3.1 fedora-cvs allows anonymous checkout
- fix some Requires  add cvs curl and wget 

* Sun Mar 30 2008 Dennis Gilmore <dennis@ausil.us> - 0.3.0-1
- update to 0.3.0 fedora-cvs uses pyOpenSSL to work out username
- remove Requires on RCS's for fedora-hosted
- rename fedora-packager-setup.sh to fedora-packager-setup

* Fri Feb 22 2008 Dennis Gilmore <dennis@ausil.us> - 0.2.0-1
- new upstream release
- update for fas2
- fedora-cvs  can now check out multiple modules at once
- only require git-core

* Mon Dec 03 2007 Dennis Gilmore <dennis@ausil.us> - 0.1.1-1
- fix typo in description 
- update to 0.1.1  fixes typo in fedora-cvs

* Sun Nov 11 2007 Dennis Gilmore <dennis@ausil.us> - 0.1-1
- initial build
