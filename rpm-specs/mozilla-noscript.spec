# internal macros ???
%global _firefox_app_id \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}

# common macros, yet to be defined. see:
# https://fedoraproject.org/wiki/User:Kalev/MozillaExtensionsDraft
%global _moz_extensions %{_datadir}/mozilla/extensions
%global _firefox_extdir %{_moz_extensions}/%{_firefox_app_id}

# needed for this package
%global extension_id \{73a6fe31-595d-460b-a920-fcc0f8843232\}

Name:           mozilla-noscript
Version:        11.0.26
Release:        1%{?dist}
Summary:        JavaScript white list extension for Mozilla Firefox

License:        GPLv2+
URL:            http://noscript.net/
# Source is a .xpi file, there is no public VCS or a tarball
Source0:        https://secure.informaction.com/download/releases/noscript-%{version}.xpi
# https://bugzilla.redhat.com/show_bug.cgi?id=1364409
Source1:        %{name}.metainfo.xml

BuildRequires:  dos2unix
# GNOME Software Center not present on EL < 7 and Fedora
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires:  libappstream-glib
%endif
Requires:       mozilla-filesystem
# https://labs.ft.com/fastclick/ MIT
# post 1.0.6 commit 7972ec0e4bce4e304a32be34608b915840d6b4b4
Provides:       bundled(js-fastclick) = 1.0.6
# https://github.com/mdmoreau/flextabs MIT
Provides:       bundled(js-flextabs) = 0.2.0
# https://mths.be/punycode MIT
Provides:       bundled(js-punycode) = 1.4.1
# https://github.com/emn178/js-sha256 MIT
Provides:       bundled(js-sha256) = 0.9.0
# https://github.com/mozilla/webextension-polyfill MPL
Provides:       bundled(webextension-polyfill) = 0.3.1
Provides:       firefox-noscript = %{version}-%{release}
Obsoletes:      firefox-noscript < %{version}
Obsoletes:      seamonkey-noscript <= 5.1.9
BuildArch:      noarch

%description
The NoScript extension provides extra protection for Firefox.
It allows JavaScript, Java, Flash and other plug-ins to be executed only by
trusted web sites of your choice (e.g. your online bank) and additionally
provides Anti-XSS protection.

%prep
%setup -q -cT
unzip -qq %{SOURCE0} GPL.txt LICENSE.txt
dos2unix -k -f GPL.txt
dos2unix -k LICENSE.txt

%build

%install
# install into _firefox_extdir
install -Dp -m 644 %{SOURCE0} %{buildroot}%{_firefox_extdir}/%{extension_id}.xpi

# install MetaInfo file for firefox, etc
%if 0%{?fedora} || 0%{?rhel} >= 7
install -Dpm644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo/%{name}.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.metainfo.xml
%endif

%files
%license GPL.txt
%doc LICENSE.txt
%{_firefox_extdir}/%{extension_id}.xpi
# GNOME Software Center metadata
%if 0%{?fedora} || 0%{?rhel} >= 7
%{_datadir}/metainfo/%{name}.metainfo.xml
%endif

%changelog
* Tue May 19 2020 Dominik Mierzejewski <rpm@greysector.net> - 11.0.26-1
- update to 11.0.26 (#1836699)

* Sun May 03 2020 Dominik Mierzejewski <rpm@greysector.net> - 11.0.25-1
- update to 11.0.25 (#1825050)

* Sun Apr 12 2020 Dominik Mierzejewski <rpm@greysector.net> - 11.0.23-1
- update to 11.0.23 (#1813501)

* Mon Mar 09 2020 Dominik Mierzejewski <rpm@greysector.net> - 11.0.15-1
- update to 11.0.15 (#1782610)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 01 2019 Dominik Mierzejewski <rpm@greysector.net> - 11.0.9-1
- update to 11.0.9 (#1756745)

* Thu Sep 12 2019 Dominik Mierzejewski <rpm@greysector.net> - 11.0.3-1
- update to 11.0.3 (#1751683)
- add more bundled libraries

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 20 2019 Dominik Mierzejewski <rpm@greysector.net> - 10.2.1-2
- update to 10.2.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.1.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 26 2018 Dominik Mierzejewski <rpm@greysector.net> - 10.1.9.9-1
- update to 10.1.9.9
- sync obsoleted classic version with F28 and older

* Sun Sep 16 2018 Dominik Mierzejewski <rpm@greysector.net> - 10.1.9.6-1
- update to 10.1.9.6
- drop classic version and move WebExtension back to main package
- obsolete old vulnerable classic extension versions so that users
  can install the latest version independently

* Mon Jul 30 2018 Dominik Mierzejewski <rpm@greysector.net> - 10.1.8.16-2
- update to 10.1.8.16 (#1609266)
- make main package dependencies on subpackages versioned

* Fri Jul 20 2018 Dominik Mierzejewski <rpm@greysector.net> - 10.1.8.8-1
- update to 10.1.8.8 (#1601456)
- update classic version to 5.1.8.6
- extract only the licenses and cfg file

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.1.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Dominik Mierzejewski <rpm@greysector.net> - 10.1.8.2-3
- update to 10.1.8.2 (#1583884)

* Wed May 23 2018 Dominik Mierzejewski <rpm@greysector.net> - 10.1.8.1-2
- update to 10.1.8.1 (#1572820)

* Thu Apr 12 2018 Dominik Mierzejewski <rpm@greysector.net> - 10.1.7.5-1
- update to 10.1.7.5 (#1557592)
- update classic version to 5.1.8.5

* Fri Mar 16 2018 Dominik Mierzejewski <rpm@greysector.net> - 10.1.7.2-2
- update to 10.1.7.2 (#1557318)
- update bundled components Provides:

* Mon Feb 19 2018 Dominik Mierzejewski <rpm@greysector.net> - 10.1.6.5-1
- update to 10.1.6.5 (#1543851)
- update classic version to 5.1.8.4

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Dominik Mierzejewski <rpm@greysector.net> - 10.1.6.4-1
- update to 10.1.6.4 (#1539464)
- switch URL to upstream instead of AMO, they're identical
- split FF and SM extensions to separate subpackages

* Sat Jan 20 2018 Dominik Mierzejewski <rpm@greysector.net> - 10.1.6.3-1
- update to 10.1.6.3 (#1532905)
- install metainfo file in the new standard location

* Mon Jan 01 2018 Dominik Mierzejewski <rpm@greysector.net> - 10.1.6.2-1
- update to 10.1.6.2 (#1528835)

* Tue Dec 19 2017 Dominik Mierzejewski <rpm@greysector.net> - 10.1.6-1
- update to 10.1.6 (#1527501)

* Sat Dec 16 2017 Dominik Mierzejewski <rpm@greysector.net> - 10.1.5.8-1
- update to 10.1.5.8 (#1524389)
- bring back the classic version (still developed until June 2018)
  for SeaMonkey (#1526199)

* Sat Nov 25 2017 Dominik Mierzejewski <rpm@greysector.net> - 10.1.2-1
- update to 10.1.2

* Mon Nov 20 2017 Dominik Mierzejewski <rpm@greysector.net> - 10.1.1-1
- update to 10.1.1 (pure WebExtension version, Firefox 57+ only)

* Thu Nov 02 2017 Dominik Mierzejewski <rpm@greysector.net> - 5.1.4-1
- update to 5.1.4 (#1504408)

* Sun Oct 01 2017 Dominik Mierzejewski <rpm@greysector.net> - 5.1.1-1
- update to 5.1.1 (#1491072)

* Wed Aug 23 2017 Dominik Mierzejewski <rpm@greysector.net> - 5.0.9-1
- update to 5.0.9 (#1476252)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Dominik Mierzejewski <rpm@greysector.net> - 5.0.7.1-1
- update to 5.0.7.1 (#1474552)

* Mon Jul 03 2017 Dominik Mierzejewski <rpm@greysector.net> - 5.0.6-1
- update to 5.0.6 (#1467119)
- switch to AMO URL

* Tue May 30 2017 Dominik Mierzejewski <rpm@greysector.net> - 5.0.5-1
- update to 5.0.5 (#1450033)

* Tue Mar 21 2017 Dominik Mierzejewski <rpm@greysector.net> - 5.0.2-1
- update to 5.0.2 (#1429065)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Dominik Mierzejewski <rpm@greysector.net> - 2.9.5.3-1
- update to 2.9.5.3 (#1414179)

* Mon Dec 05 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.9.5.2-1
- update to 2.9.5.2 (#1400191)

* Wed Nov 23 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.9.5.1-1
- update to 2.9.5.1 (#1397613)

* Mon Nov 21 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.9.0.14-3
- EL7 has gnome-software, so ship appstream data there, too

* Sun Aug 21 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.9.0.14-2
- include AppStream metadata (#1364409)

* Wed Aug 10 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.9.0.14-1
- update to 2.9.0.14 (#1365329)

* Wed Aug 03 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.9.0.13-1
- update to 2.9.0.13 (#1362319)

* Fri Jul 29 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.9.0.12-1
- update to 2.9.0.12 (#1360761)

* Sun Apr 10 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.9.0.11-1
- update to 2.9.0.11 (#1325580)

* Tue Mar 29 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.9.0.10-1
- update to 2.9.0.10 (#1319364)

* Thu Mar 17 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.9.0.5-1
- update to 2.9.0.5 (#1318460)
- clean up spec and drop EL5-specific stuff

* Sun Feb 14 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.9.0.4-1
- update to 2.9.0.4 (#1306872)

* Sat Feb 06 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.9.0.3-1
- update to 2.9.0.3 (#1304561)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.9.0.2-1
- update to 2.9.0.2 (#1296924)

* Tue Jan 05 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.9-1
- update to 2.9 (#1295023)

* Sun Dec 20 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.7-2
- package unexploded so that it doesn't get disabled in FF43+
- tag license text file appropriately

* Thu Nov 26 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.7-1
- update to 2.7 (#1284465)

* Mon Oct 26 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.9.39-1
- update to 2.6.9.39 (#1275118)
- internal chrome/noscript.jar is back again

* Thu Oct 15 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.9.38-1
- update to 2.6.9.38 (#1270625)
- internal chrome.jar is now shipped unpacked by upstream
- keep timestamps after EOL conversion

* Wed Sep 30 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.9.37-1
- update to 2.6.9.37 (#1267409)

* Wed Sep 02 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.9.36-1
- update to 2.6.9.36 (#1252869)

* Sat Aug 15 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.9.35-1
- update to 2.6.9.35 (#1252869)

* Tue Aug 04 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.9.34-1
- update to 2.6.9.34

* Fri Jul 31 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.9.33-1
- update to 2.6.9.33 (#1248239)

* Tue Jul 28 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.9.32-1
- update to 2.6.9.32 (#1247133)

* Tue Jul 21 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.9.31-1
- update to 2.6.9.31 (#1243616)

* Fri Jul 10 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.9.30-1
- update to 2.6.9.30 (#1241523)

* Thu Jul 02 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.9.29-1
- update to 2.6.9.29 (#1237141)

* Thu Jun 18 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.9.27-1
- update to 2.6.9.27 (#1232980)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.9.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.9.26-1
- update to 2.6.9.26 (#1226495)

* Tue May 26 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.9.25-1
- update to 2.6.9.25 (#1197536)

* Sat Feb 21 2015 Thomas Spura <tomspur@fedoraproject.org> - 2.6.9.15-1
- update to 2.6.9.15 (#1176917)

* Wed Dec 17 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.6.9.8-1
- update to 2.6.9.8 (#1164453)

* Tue Nov 11 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.6.9.3-1
- update to 2.6.9.3 (#1124181,#1162797)

* Thu Jul 24 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.6.8.33-1
- update to 2.6.8.33 (#1104527)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.6.8.26-1
- update to 2.6.8.26 (#1094684)

* Tue Apr 15 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.6.8.20-1
- update to 2.6.8.20 (#1064214)

* Fri Jan 24 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.6.8.8-1
- update to 2.6.8.13 (#1030891, #1044655)

* Sat Oct 26 2013 Thomas Spura <tomspur@fedoraproject.org> - 2.6.8.4-1
- update to 2.6.8.4 (#1023548, #958170)

* Sun Oct 13 2013 Thomas Spura <tomspur@fedoraproject.org> - 2.6.8.2-1
- update to 2.6.8.2

* Mon Aug  5 2013 Thomas Spura <tomspur@fedoraproject.org> - 2.6.6.9-1
- update to 2.6.6.9
- fix files section to fix FTBFS (#992292)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 12 2013 Thomas Spura <tomspur@fedoraproject.org> - 2.6.5.9-1
- update to 2.6.5.9 (#890564)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 18 2012 Thomas Spura <tomspur@fedoraproject.org> - 2.6.4.1-1
- update to 2.6.4.1 (#888187)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Thomas Spura <tomspur@fedoraproject.org> - 2.4.6-1
- update to 2.4.6

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 30 2011 Thomas Spura <tomspur@fedoraproject.org> - 2.1.4-1
- update to new version (#712331)

* Fri Aug  5 2011 Thomas Spura <tomspur@fedoraproject.org> - 2.1.1-2
- change the macros to match MozillaExtensionsDraft

* Fri Jun  3 2011 Thomas Spura <tomspur@fedoraproject.org> - 2.1.1-1
- update to new version (#691356)
- renew patch

* Thu Mar 10 2011 Thomas Spura <tomspur@fedoraproject.org> - 2.0.9.9-1
- update to new version (#667389)
- renew patch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan  3 2011 Thomas Spura <tomspur@fedoraproject.org> - 2.0.9.2-1
- update to new version
- renew patch

* Mon Oct 18 2010 Thomas Spura <tomspur@fedoraproject.org> - 2.0.5.1-1
- update to new version

* Mon Oct 18 2010 Thomas Spura <tomspur@fedoraproject.org> - 2.0.3.5-1
- update to new version
- renew patch

* Thu Aug 19 2010 Thomas Spura <tomspur@fedoraproject.org> - 2.0.2.1-2
- require firefox and not mozilla-filesystem on el5

* Wed Aug 18 2010 Thomas Spura <tomspur@fedoraproject.org> - 2.0.2.1-1
- update to new version

* Fri Jul 30 2010 Thomas Spura <tomspur@fedoraproject.org> - 2.0-1
- update to new version

* Sun Jul 18 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.10-1
- new version
- renew preferences patch

* Wed Jun 30 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.97-1
- new version

* Sat Jun 12 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.87-1
- new version

* Fri May 28 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.81-1
- new version

* Mon May 24 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.79-1
- new version

* Sun May 16 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.74-1
- new version
- renew patch

* Thu Apr 22 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.69-1
- new version

* Mon Apr 19 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.66-1
- new version

* Sat Apr  3 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.60-1
- new version

* Fri Mar 19 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.57-1
- update to new version
- force dos2unix on 'binary' GPL.txt
- renew patch

* Sat Feb 27 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.50-1
- update to new version
- fix some spelling errors

* Sun Feb  7 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.45-1
- update to new version

* Sat Jan 23 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.39-1
- update to new version

* Sat Jan 16 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.35-4
- install with -p

* Fri Jan 15 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.35-3
- also install seamonkey app_id (Thomas Moschny)

* Fri Jan 15 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.35-2
- remove R: firefox, this plugin also works for seamonky and so on
  it's up to the user, what to use (Thomas Moschny)

* Fri Jan 15 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.35-1
- update to new version
- %%global vs %%define
- install in %%{_datadir} -> noarch
- delete changelog
- R: mozilla-filesystem for owning %%{_datadir}/mozilla/extensions

* Sun Jul 19 2009 Andreas Thienemann <andreas@bawue.net> - 1.9.6-1
- Initial package
