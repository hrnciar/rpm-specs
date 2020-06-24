%{?python_disable_dependency_generator}

Summary:        Encrypted bandwidth-efficient backup using rsync algorithm
Name:           duplicity
Version:        0.8.13
Release:        2%{?dist}
License:        GPLv2+
URL:            http://www.nongnu.org/duplicity/
Source:         https://launchpad.net/duplicity/0.8-series/%{version}/+download/duplicity-%{version}.tar.gz
Requires:	python3-lockfile
Requires:	gnupg >= 1.0.6
Requires:       openssh-clients, ncftp >= 3.1.9, rsync, python3-boto3
Requires:       python3-paramiko python3-dropbox python3-pexpect
Requires:       python3-fasteners python3-PyDrive python3-future
Requires:       ca-certificates

BuildRequires:  gcc gettext
BuildRequires:  python3-devel librsync-devel >= 0.9.6 python3-setuptools python3-pytest-runner
BuildRequires:  python3-setuptools_scm

%description
Duplicity incrementally backs up files and directory by encrypting
tar-format volumes with GnuPG and uploading them to a remote (or
local) file server. In theory many protocols for connecting to a
file server could be supported; so far ssh/scp, local file access,
rsync, ftp, HSI, WebDAV and Amazon S3 have been written.

Because duplicity uses librsync, the incremental archives are space
efficient and only record the parts of files that have changed since
the last backup. Currently duplicity supports deleted files, full
unix permissions, directories, symbolic links, fifos, device files,
but not hard links.

%prep
%setup -q

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

mkdir -p %{buildroot}/%{_sysconfdir}/%{name}
ln -sf %{_sysconfdir}/pki/tls/cert.pem \
       %{buildroot}/%{_sysconfdir}/%{name}/cacert.pem

%find_lang %{name}

# drop documentation
rm -rf    %{buildroot}/usr/share/doc/duplicity-%{version}/AUTHORS
rm -rf    %{buildroot}/usr/share/doc/duplicity-%{version}/Changelog.GNU
rm -rf    %{buildroot}/usr/share/doc/duplicity-%{version}/CHANGELOG
rm -rf    %{buildroot}/usr/share/doc/duplicity-%{version}/COPYING
rm -rf    %{buildroot}/usr/share/doc/duplicity-%{version}/README
rm -rf    %{buildroot}/usr/share/doc/duplicity-%{version}/README-LOG
rm -rf    %{buildroot}/usr/share/doc/duplicity-%{version}/README-TESTING
rm -rf    %{buildroot}/usr/share/doc/duplicity-%{version}/README-REPO
rm -rf    %{buildroot}/usr/share/doc/duplicity-%{version}/tarfile-CHANGES
rm -rf    %{buildroot}/usr/share/doc/duplicity-%{version}/tarfile-LICENSE


%files -f %{name}.lang
%license COPYING
%doc CHANGELOG README
%{_bindir}/rdiffdir
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{_mandir}/man1/rdiffdir*
%{python3_sitearch}/%{name}*
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/cacert.pem

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.13-2
- Rebuilt for Python 3.9

* Tue May 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.8.13-1
- 0.8.13

* Thu Mar 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.8.12-1
- 0.8.12

* Mon Feb 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.8.11-1
- 0.8.11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.8.10-1
- 0.8.10fin1558

* Tue Jan 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.8.09-1
- 0.8.09

* Thu Dec 05 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.8.08-1
- 0.8.08, migrate to boto3

* Thu Nov 14 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.8.07-1
- 0.8.07

* Tue Nov 05 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.8.06-1
- 0.8.06.

* Mon Oct 07 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.8.05-1
- 0.8.05.

* Sat Aug 31 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.8.04-1
- 0.8.04.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.03-2
- Rebuilt for Python 3.8

* Fri Aug 09 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.8.03-1
- 0.8.03

* Thu Jul 25 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.8.02-1
- 0.8.02

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.8.01-3
- Patch to fix dropbox backend.

* Mon Jul 15 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.8.01-2
- Require python3-future

* Mon Jul 15 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.8.01-1
- 0.8.01

* Mon Apr 29 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.7.19-1
- 0.7.19

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.7.18.2-1
- 0.7.18.2.

* Tue Oct 16 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.7.18.1-2
- Patch for unicode issue.

* Mon Aug 27 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.7.18.1-1
- Patch for crash.

* Wed Aug 22 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.7.18-1
- 0.7.18.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 26 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.7.17-2
- Versioned lockfile deps.

* Mon Feb 26 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.7.17-1
- 0.7.17.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Feb 06 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.7.16-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Jan 17 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.7.16-1
- 0.7.16.

* Tue Nov 14 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.7.15-1
- 0.7.15, spec cleanup.

* Mon Sep 25 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.7.14-2
- Fix python2-gnupginterface requires.

* Fri Sep 01 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.7.14-1
- 0.7.14, BZ 1487444.

* Mon Aug 28 2017 Ville Skyttä <ville.skytta@iki.fi> - 0.7.13.1-5
- Own the %%{_sysconfdir}/%%{name} dir
- Install COPYING as %%license

* Mon Aug 14 2017 Nick Bebout <nb@fedoraproject.org> - 0.7.13.1-4
- Add Requires: python2-PyDrive to support Google Drive targets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.7.13.1-1
- 0.7.13.1, BZ 1462570.

* Wed Jun 14 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.7.13-1
- 0.7.13, BZ 1460834.

* Mon May 01 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.7.12-2
- Fix gpg agent, BZ 1439455.

* Wed Mar 22 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.7.12-1
- 0.7.12, BZ 1434625.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 03 2017 Jon Ciesla <limburgher@gmail.com> - 0.7.11-1
- 0.7.11, BZ 1409336.

* Mon Aug 29 2016 Jon Ciesla <limburgher@gmail.com> - 0.7.10-1
- 0.7.10, BZ 1370670.

* Mon Jul 25 2016 Jon Ciesla <limburgher@gmail.com> - 0.7.09-1
- 0.7.09, BZ 1359548.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.08-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jul 05 2016 Jon Ciesla <limburgher@gmail.com> - 0.7.08-1
- 0.7.08, BZ 1352247.

* Thu Jun 30 2016 Jon Ciesla <limburgher@gmail.com> - 0.7.07.1-2
- Require python-pexpect, BZ 1351471.

* Tue Apr 19 2016 Jon Ciesla <limburgher@gmail.com> - 0.7.07.1-1
- 0.7.07.1.

* Mon Apr 11 2016 Jon Ciesla <limburgher@gmail.com> - 0.7.07-1
- 0.7.07, BZ 1325874.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 07 2015 Jon Ciesla <limburgher@gmail.com> - 0.7.06-1
- 0.7.06, BZ 1289379.

* Wed Sep 16 2015 Jon Ciesla <limburgher@gmail.com> - 0.7.05-1
- 0.7.05, BZ 1263488.

* Mon Aug 03 2015 Jon Ciesla <limburgher@gmail.com> - 0.7.04-1
- 0.7.04, BZ 1249390.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 12 2015 Jon Ciesla <limburgher@gmail.com> - 0.7.03-1
- 0.7.03, BZ 1220586.

* Thu Mar 12 2015 Jon Ciesla <limburgher@gmail.com> - 0.7.02-1
- 0.7.02.
- librsync patch upstreamed.

* Sun Mar 01 2015 Robert Scheck <robert@fedoraproject.org> 0.7.01-2
- Rebuild for librsync 1.0.0 (#1126712)

* Fri Feb 27 2015 Jon Ciesla <limburgher@gmail.com> - 0.7.01-1
- 0.7.01, BZ 1155100.

* Thu Feb 26 2015 Jon Ciesla <limburgher@gmail.com> - 0.6.25-1
- 0.6.25.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 Rahul Sundaram <sundaram@fedoraproject.org> - 0.6.24-2
- add build requires on python-setuptools

* Mon May 12 2014 Rahul Sundaram <sundaram@fedoraproject.org> - 0.6.24-1
- update to 0.6.24
- drop patch for documentation and remove it directly in spec

* Fri Apr 11 2014 Rahul Sundaram <sundaram@fedoraproject.org> - 0.6.23-2
- add dependency on python-lockfile

* Fri Apr 11 2014 Rahul Sundaram <sundaram@fedoraproject.org> - 0.6.23-1
- update to 0.6.33
- drop no longer needed patch for Amazon s3 backup

* Fri Jan 17 2014 Rahul Sundaram <sundaram@fedoraproject.org> - 0.6.22-5
- Added patch to fix Amazon s3 backup (#1048068)

* Mon Jan 13 2014 Rahul Sundaram <sundaram@fedoraproject.org> - 0.6.22-4
- Added runtime requirement to python-dropbox (#1048656)

* Fri Dec 27 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.6.22-3
- Fix ssl cert enforcement (rhbz#960860)
- Fix bogus date in changelog

* Thu Dec 26 2013 Robert Scheck <robert@fedoraproject.org> 0.6.22-2
- Added runtime requirement to python-paramiko (#819272, #918933)

* Wed Dec 25 2013 Robert Scheck <robert@fedoraproject.org> 0.6.22-1
- Upgrade to 0.6.22 (#903584, #992158)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 18 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.6.21-1
- Upgrade to 0.6.21
- Fixes data corruption issues (#922576)
- Fix bogus dates in spec changelog

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 20 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.6.20-1
- Upgrade to 0.6.20 (#827960)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 08 2012 Robert Scheck <robert@fedoraproject.org> 0.6.18-1
- Upgrade to 0.6.18 (#798951)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 26 2011 Robert Scheck <robert@fedoraproject.org> 0.6.17-1
- Upgrade to 0.6.17 (#736715)

* Sun Jul 17 2011 Robert Scheck <robert@fedoraproject.org> 0.6.14-1
- Upgrade to 0.6.14 (#720589, #697222)
- Backported optparse 1.5a2 from RHEL 5 for RHEL 4 (#717133)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 09 2010 Robert Scheck <robert@fedoraproject.org> 0.6.11-1
- Upgrade to 0.6.11 (#655870)

* Sun Oct 31 2010 Robert Scheck <robert@fedoraproject.org> 0.6.10-1
- Upgrade to 0.6.10
- Added a patch to avoid ternary conditional operators (#639863)

* Wed Sep 29 2010 Jesse Keating <jkeating@redhat.com> 0.6.09-2
- Rebuilt for gcc bug 634757

* Mon Sep 13 2010 Robert Scheck <robert@fedoraproject.org> 0.6.09-1
- Upgrade to 0.6.09 (#596018)

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.08b-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Mar 28 2010 Robert Scheck <robert@fedoraproject.org> 0.6.08b-1
- Upgrade to 0.6.08b

* Sat Dec 26 2009 Robert Scheck <robert@fedoraproject.org> 0.6.06-1
- Upgrade to 0.6.06 (#550663)

* Sun Sep 27 2009 Robert Scheck <robert@fedoraproject.org> 0.6.05-1
- Upgrade to 0.6.05 (#525940)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 24 2009 Robert Scheck <robert@fedoraproject.org> 0.5.18-1
- Upgrade to 0.5.18

* Sun May 03 2009 Robert Scheck <robert@fedoraproject.org> 0.5.16-1
- Upgrade to 0.5.16

* Thu Apr 16 2009 Robert Scheck <robert@fedoraproject.org> 0.5.15-1
- Upgrade to 0.5.15

* Sat Mar 21 2009 Robert Scheck <robert@fedoraproject.org> 0.5.12-1
- Upgrade to 0.5.12 (#490289)

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 0.5.06-2
- Rebuild for gcc 4.4 and rpm 4.6

* Sun Jan 25 2009 Robert Scheck <robert@fedoraproject.org> 0.5.06-1
- Upgrade to 0.5.06 (#481489)

* Sun Dec 07 2008 Robert Scheck <robert@fedoraproject.org> 0.5.03-1
- Upgrade to 0.5.03

* Fri Dec 05 2008 Jeremy Katz <katzj@redhat.com> 0.4.12-3
- Rebuild for python 2.6

* Fri Aug 08 2008 Robert Scheck <robert@fedoraproject.org> 0.4.12-2
- Added patch to get scp without username working (#457680)

* Sun Jul 27 2008 Robert Scheck <robert@fedoraproject.org> 0.4.12-1
- Upgrade to 0.4.12

* Sat Jun 28 2008 Robert Scheck <robert@fedoraproject.org> 0.4.11-2
- Added patch for incremental backups using python 2.3 (#453069)

* Mon May 05 2008 Robert Scheck <robert@fedoraproject.org> 0.4.11-1
- Upgrade to 0.4.11 (#440346)

* Sun Feb 10 2008 Robert Scheck <robert@fedoraproject.org> 0.4.9-1
- Upgrade to 0.4.9 (#293081, #431467)

* Sat Dec 08 2007 Robert Scheck <robert@fedoraproject.org> 0.4.7-1
- Upgrade to 0.4.7

* Sat Sep 15 2007 Robert Scheck <robert@fedoraproject.org> 0.4.3-1
- Upgrade to 0.4.3 (#265701)
- Updated the license tag according to the guidelines

* Mon May 07 2007 Robert Scheck <robert@fedoraproject.org> 0.4.2-7
- Rebuild

* Wed Dec 20 2006 Robert Scheck <robert@fedoraproject.org> 0.4.2-6
- fix broken sftp support by adding --sftp-command (#220316)

* Sun Dec 17 2006 Robert Scheck <robert@fedoraproject.org> 0.4.2-5
- own %%{python_sitearch}/%%{name} and not only %%{python_sitearch}

* Sat Dec 16 2006 Robert Scheck <robert@fedoraproject.org> 0.4.2-4
- added two small fixing patches (upstream items #4486, #5183)
- many spec file cleanups and try to silence rpmlint a bit more

* Fri Sep 08 2006 Michael J. Knox <michael[AT]knox.net.nz> - 0.4.2-3
- don't ghost pyo files

* Sun Aug 27 2006 Michael J. Knox <michael[AT]knox.net.nz> - 0.4.2-2
- Rebuild for FC6

* Tue May 16 2006 Michael J. Knox <michael[AT]knox.net.nz> - 0.4.2-1
- version bump

* Thu Apr 7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sun Oct 05 2003 Ben Escoto <bescoto@stanford.edu> - 0:0.4.1-0.fdr.3
- More hints from Fedora QA (ville.skytta@iki.fi)

* Sat Aug 09 2003 Ben Escoto <bescoto@stanford.edu> - 0:0.4.1-0.fdr.2
- Repackaging for Fedora

* Fri Aug 30 2002 Ben Escoto <bescoto@stanford.edu>
- Initial RPM
