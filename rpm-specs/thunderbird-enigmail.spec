# spec file for thunderbird-enigmail
#
# Copyright (c) 2009-2015 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global thunderbird_app_id \{3550f703-e582-4d05-9a08-453d09bdfdc6\} 
%global enimail_app_id     \{847b3a00-7ab1-11d4-8f02-006008948af5\}

%global thunmin            68.0

%global enigmail_extname   %{_datadir}/mozilla/extensions/%{thunderbird_app_id}/%{enimail_app_id}

#global gitcommit          e6dcbdde07a5a7de6e1cc3605fcb810f3c9cede0
#global gitdate            20191029
#global gitshort           %%(c=%%{gitcommit}; echo ${c:0:7})

Summary:        Authentication and encryption extension for Mozilla Thunderbird
Name:           thunderbird-enigmail
Version:        2.1.6
Release:        1%{?dist}
URL:            https://enigmail.net/
# All files licensed under MPL 1.1/GPL 2.0/LGPL 2.1
License:        MPLv1.1 or GPLv2+ or LGPLv2+

BuildArch:      noarch
# Thunderbird is not available on all supported platforms
ExcludeArch: armv7hl
ExcludeArch: s390x

%if 0%{?gitdate}
# git clone git://git.code.sf.net/p/enigmail/source enigmail-source
# cd enigmail-source; git checkout c429d03
# git archive --format=tar.gz --prefix enigmail/ --output ../enigmail-1.8-d77065b.tar.gz --verbose  master
Source0:        enigmail-%{version}-%{gitshort}.tar.gz
%else
Source0:        https://enigmail.net/download/source/enigmail-%{version}.tar.gz
%endif
Source1:        https://enigmail.net/download/source/enigmail-%{version}.tar.gz.asc
# Key for Enigmail versions 1.8 and newer:
#   Key ID: 0xDD5F693B
#   Fingerprint: 4F9F 89F5 505A C1D1 A260 631C DB11 87B9 DD5F 693B
#   "Patrick Brunschwig <patrick@enigmail.net>"
#   "Patrick Brunschwig <patrick@brunschwig.net>"
Source2:        https://www.enigmail.net/download/other/Enigmail_public_key.asc
Source3:        thunderbird-enigmail.metainfo.xml

BuildRequires:  gnupg2
BuildRequires:  zip
BuildRequires:  perl-interpreter >= 5.8
BuildRequires:  python3

%if 0%{?fedora} >= 21
BuildRequires:  libappstream-glib
%endif

Requires:  thunderbird >= %{thunmin}
Requires:  pinentry-gui
Requires:  gnupg2


%description
Enigmail is an extension to the mail client Mozilla Thunderbird
which allows users to access the authentication and encryption
features provided by GnuPG 


%prep
%if 0%{?gitdate}
%else
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%setup -q -n enigmail

grep -q "PACKAGE_VERSION='%{version}'" configure || exit 1


%build
# see https://www.enigmail.net/download/build_instructions.php
%configure

make


%install
mkdir -p $RPM_BUILD_ROOT%{enigmail_extname}
unzip -q build-tb/enigmail-*.xpi -d $RPM_BUILD_ROOT%{enigmail_extname}

# if Fedora >= 21
# install MetaInfo file for firefox
%if 0%{?fedora} >= 21
    DESTDIR=%{buildroot} appstream-util install %{SOURCE3}
%endif

%files
%license LICENSE
%{enigmail_extname}

# GNOME Software Center metadata
%if 0%{?fedora} >= 21
    %{_datadir}/appdata/*.metainfo.xml
%endif

#===============================================================================

%changelog
* Fri Apr 03 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 2.1.6-1
- update to 2.1.6

* Fri Jan 31 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 2.1.5-1
- update to 2.1.5
- do not build package on armv7hl/s390x (thunderbird not available there)
- enable GPG-based source file verification
- package license file
- update version to support TB 68

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.8-2
- Drop aarch64 exclude as it's available now

* Sun Aug 05 2018 Christian Dersch <lupinix@mailbox.org> - 2.0.8-1
- new version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Christian Dersch <lupinix.fedora@gmail.com> - 2.0.7-1
- new version

* Mon May 28 2018 Christian Dersch <lupinix@fedoraproject.org> - 2.0.6-1
- new version

* Sat May 19 2018 Christian Dersch <lupinix@fedoraproject.org> - 2.0.4-1
- new version fixing efail vulnerability

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 22 2017 Christian Dersch - 1.9.9-1
- new version

* Wed Oct 04 2017 Christian Dersch <lupinix@mailbox.org> - 1.9.8.3-1
- new version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Christian Dersch <lupinix@mailbox.org> - 1.9.7-1
- new version

* Tue Jun 13 2017 Christian Dersch <lupinix@mailbox.org> - 1.9.6.1-4
- Updated architectures supported by Thunderbird

* Sun Apr 23 2017 Christian Dersch <lupinix@mailbox.org> - 1.9.6.1-3
- not available on aarch64 (Thunderbird not available there)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 22 2016 Christian Dersch <lupinix@mailbox.org> - 1.9.6.1-1
- new version

* Sun Nov 13 2016 Christian Dersch <lupinix@mailbox.org> - 1.9.6-1
- new version

* Sun Sep 04 2016 Christian Dersch <lupinix@mailbox.org> - 1.9.5-1
- new version

* Sun Jul 17 2016 Christian Dersch <lupinix@mailbox.org> - 1.9.4-1
- new version

* Thu Jun 09 2016 Christian Dersch <lupinix@mailbox.org> - 1.9.3-2
- Fixed installation path for noarch

* Thu Jun 09 2016 Christian Dersch <lupinix@mailbox.org> - 1.9.3-1
- new version (1.9.3)
- minimum Thunderbird release now 38.0
- package is noarch now

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 04 2016 Christian Dersch <lupinix@mailbox.org> - 1.8.2-4
- Add Appstream metadata (#1267628)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 Remi Collet <remi@fedoraproject.org> 1.8.2-2
- add dependency on pinentry-gui #1215779
- add explicit dependency on gnupg2

* Fri Apr 17 2015 Remi Collet <remi@fedoraproject.org> 1.8.2-1
- Enigmail 1.8.2

* Mon Mar 23 2015 Remi Collet <remi@fedoraproject.org> 1.8.1-1
- Enigmail 1.8.1

* Tue Mar 17 2015 Remi Collet <remi@fedoraproject.org> 1.8-1
- Enigmail 1.8

* Fri Feb 27 2015 Remi Collet <remi@fedoraproject.org> 1.8-0.1.20150227gitd77065b
- update to git snapshot (post 1.8 Beta 1)

* Fri Aug 29 2014 Remi Collet <remi@fedoraproject.org> 1.7.2-1
- Enigmail 1.7.2, fix CVE-2014-5369

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 15 2014 Remi Collet <remi@fedoraproject.org> 1.7-1
- Enigmail 1.7

* Fri Jul 11 2014 Remi Collet <remi@fedoraproject.org> 1.7-0.3.20140709gitc429d03
- test build, new snapshot
- disable parallel build (broken)

* Mon Jun  9 2014 Remi Collet <remi@fedoraproject.org> 1.7-0.2.20140608git611bc95
- fix empty debuginfo (#1011048)

* Mon Jun  9 2014 Remi Collet <remi@fedoraproject.org> 1.7-0.1.20140608git611bc95
- Enigmail 1.7pre (git snapshot)
- new build system, without need for Thunderbird sources

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Nov 03 2013 Dennis Gilmore <dennis@ausil.us> 1.6-2
- remove ExcludeArch armv7hl

* Tue Oct  8 2013 Remi Collet <remi@fedoraproject.org> 1.6-1
- Enigmail 1.6

* Sat Sep 21 2013 Remi Collet <remi@fedoraproject.org> 1.5.2-3
- Enigmail 1.5.2 for Thunderbird > 24

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul  4 2013 Remi Collet <remi@fedoraproject.org> 1.5.2-1
- Enigmail 1.5.2 for Thunderbird 17.0.7

* Sun Feb 10 2013 Remi Collet <remi@fedoraproject.org> 1.5.1-1
- Enigmail 1.5.1 for Thunderbird 17.0.2
- sync with latest thunderbird.spec changes

* Sun Dec 30 2012 Remi Collet <remi@fedoraproject.org> 1.5.0-1
- Enigmail 1.5.0 for Thunderbird 17

* Tue Nov 20 2012 Jan Horak <jhorak@redhat.com> - 1.4.6-2
- Rebuild against newer Thunderbird

* Fri Nov  9 2012 Remi Collet <remi@fedoraproject.org> 1.4.6-1
- Enigmail 1.4.6 for Thunderbird 16

* Tue Oct 16 2012 Remi Collet <remi@fedoraproject.org> 1.4.5-2
- Enigmail 1.4.5 for Thunderbird 16.0.1
- merge changes from thunderbird in rawhide

* Tue Oct  9 2012 Remi Collet <remi@fedoraproject.org> 1.4.5-1
- Enigmail 1.4.5 for Thunderbird 16

* Mon Aug 27 2012 Remi Collet <remi@fedoraproject.org> 1.4.4-2
- Enigmail 1.4.4 for Thunderbird 15.0

* Tue Aug 21 2012 Remi Collet <remi@fedoraproject.org> 1.4.4-1
- Enigmail 1.4.4 for Thunderbird 14.0

* Sat Jul 21 2012 Remi Collet <remi@fedoraproject.org> 1.4.3-1
- Enigmail 1.4.3 for Thunderbird 14.0

* Tue Jun 05 2012 Remi Collet <remi@fedoraproject.org> 1.4.2-1
- Enigmail 1.4.2 for Thunderbird 13.0

* Sat Apr 28 2012 Remi Collet <remi@fedoraproject.org> 1.4.1-1
- Enigmail 1.4.1 for Thunderbird 12.0

* Fri Mar 16 2012 Remi Collet <remi@fedoraproject.org> 1.4-2.1
- latest patch from rawhide

* Thu Mar 15 2012 Remi Collet <remi@fedoraproject.org> 1.4-2
- Enigmail 1.4 for Thunderbird 11.0

* Sat Mar 03 2012 Remi Collet <remi@fedoraproject.org> 1.4-1
- Enigmail 1.4 for Thunderbird 10.0.2
- using upstream fixlang.pl instead of our fixlang.php

* Tue Jan 31 2012 Remi Collet <remi@fedoraproject.org> 1.3.5-1
- Enigmail 1.3.5 for Thunderbird 10.0

* Wed Dec 21 2011 Remi Collet <remi@fedoraproject.org> 1.3.4-1
- Enigmail 1.3.4 for Thunderbird 9.0

* Sat Nov 12 2011 Remi Collet <remi@fedoraproject.org> 1.3.3-1
- Enigmail 1.3.3 for Thunderbird 8.0

* Wed Oct 12 2011 Georgi Georgiev <chutzimir@gmail.com> - 1.3.2-2
- Make it work on RHEL

* Sat Oct 01 2011 Remi Collet <remi@fedoraproject.org> 1.3.2-2
- Enigmail 1.3.2 for Thunderbird 7.0.1
- fix extension version

* Thu Sep 29 2011 Remi Collet <remi@fedoraproject.org> 1.3.2-1
- Enigmail 1.3.2 for Thunderbird 7.0

* Wed Aug 17 2011 Remi Collet <remi@fedoraproject.org> 1.3-1
- Enigmail 1.3 for Thunderbird 6.0

* Sat Jul 30 2011 Remi Collet <remi@fedoraproject.org> 1.2.1-1
- Enigmail 1.2.1 for Thunderbird 5.0

* Tue Jul 19 2011 Remi Collet <remi@fedoraproject.org> 1.2-1.2
- add --enable-chrome-format=jar to generate enigmail.jar

* Sun Jul 17 2011 Remi Collet <remi@fedoraproject.org> 1.2-1.1
- fix BR (dos2unix + php-cli)

* Sun Jul 17 2011 Remi Collet <rpms@famillecollet.com> 1.2-1
- Enigmail 1.2 for Thunderbird 5.0

* Thu Jul 22 2010 Remi Collet <rpms@famillecollet.com> 1.1.2-3
- move to /usr/lib/mozilla/extensions (as lightning)
- build against thunderbird 3.1.1 sources
- sync patches with F-13

* Sat Jul 10 2010 Remi Collet <rpms@famillecollet.com> 1.1.2-2
- remove link mecanism as thundebird dir is now stable (see #608511)

* Wed Jun 30 2010 Remi Collet <rpms@famillecollet.com> 1.1.2-1
- Enigmail 1.1.1 (against thunderbird 3.1)

* Sat Jun 26 2010 Remi Collet <rpms@famillecollet.com> 1.1.1-2
- new sources (only fix displayed version)

* Sat Jun 26 2010 Remi Collet <rpms@famillecollet.com> 1.1.1-1
- Enigmail 1.1.1 (against thunderbird 3.1)

* Mon May 31 2010 Remi Collet <rpms@famillecollet.com> 1.1-1
- Enigmail 1.1 (against thunderbird 3.1rc1)

* Mon Feb 01 2010 Remi Collet <rpms@famillecollet.com> 1.0.1-1
- Enigmail 1.0.1 (against thunderbird 3.0.1)

* Fri Jan 29 2010 Remi Collet <rpms@famillecollet.com> 1.0.1-0.1.rc1
- Enigmail 1.0.1rc1 (against thunderbird 3.0.1)

* Mon Nov 30 2009 Remi Collet <rpms@famillecollet.com> 1.0.0-1
- Enigmail 1.0 (against thunderbird 3.0rc1)

* Sat Nov 21 2009 Remi Collet <rpms@famillecollet.com> 1.0-0.1.cvs20091121
- new CVS snapshot (against thunderbird 3.0rc1)

* Tue Jul 21 2009 Remi Collet <rpms@famillecollet.com> 0.97a-0.1.cvs20090721
- new CVS snapshot (against thunderbird 3.0b3)

* Thu May 21 2009 Remi Collet <rpms@famillecollet.com> 0.96a-0.3.cvs20090521
- new CVS snapshot
- fix License and Sumnary

* Mon May 18 2009 Remi Collet <rpms@famillecollet.com> 0.96a-0.2.cvs20090516
- use mozilla-extension-update.sh from thunderbird-lightning

* Sat May 16 2009 Remi Collet <rpms@famillecollet.com> 0.96a-0.1.cvs20090516
- new CVS snapshot
- rpmfusion review proposal

* Thu Apr 30 2009 Remi Collet <rpms@famillecollet.com> 0.96a-0.1.cvs20090430.fc11.remi
- new CVS snapshot
- F11 build

* Mon Mar 16 2009 Remi Collet <rpms@famillecollet.com> 0.96a-0.1.cvs20090316.fc#.remi
- new CVS snapshot
- add enigmail-fixlang.php

* Sun Mar 15 2009 Remi Collet <rpms@famillecollet.com> 0.96a-0.1.cvs20090315.fc#.remi
- enigmail 0.96a (CVS), Thunderbird 3.0b2

