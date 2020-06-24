# common macros, yet to be defined. see:
# https://fedoraproject.org/wiki/User:Kalev/MozillaExtensionsDraft
%global moz_extensions %{_datadir}/mozilla/extensions

%global ext_id jid1-F9UJ2thwoAm5gQ@jetpack

%global firefox_app_id \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%global firefox_inst_dir %{moz_extensions}/%{firefox_app_id}

%global fileid 866284

Name:           mozilla-lightbeam
Version:        2.1.0
Release:        5%{?dist}
Summary:        An add-on for visualizing HTTP requests between websites in real time

License:        MPLv2.0 and BSD and ASL 2.0
URL:            https://www.mozilla.org/lightbeam/
# Git repo at https://github.com/mozilla/lightbeam-we
Source0:        https://addons.mozilla.org/firefox/downloads/file/%{fileid}/firefox_lightbeam-%{version}-an+fx-linux.xpi
Source1:        mozilla-lightbeam.metainfo.xml

Requires:       mozilla-filesystem
BuildArch:      noarch
BuildRequires:  libappstream-glib
# ext-libs/d3.min.js http://d3js.org/ BSD
Provides:       bundled(js-d3) = 4.13.0
# ext-libs/dexie.js http://dexie.org/ ASL 2.0
Provides:       bundled(js-dexie) = 2.0.1
# fonts/OpenSans*.ttf
# -> OpenSans ASL 2.0
Provides:       bundled(open-sans-fonts) = 1.10

%description
Using interactive visualizations, Lightbeam enables you to see the first
and third party sites you interact with on the Web. As you browse,
Lightbeam reveals the full depth of the Web today, including parts
that are not transparent to the average user. Using three distinct
interactive graphic representations — Graph, Clock and
List — Lightbeam enables you to examine individual third parties
over time and space, identify where they connect to your online activity
and provides ways for you to engage with this unique view of the Web.

%prep
%setup -qc

%build
echo Nothing to build

%install
install -Dpm644 %{SOURCE0} %{buildroot}%{firefox_inst_dir}/%{ext_id}.xpi

install -Dpm644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo/%{name}.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.metainfo.xml

%files
%{firefox_inst_dir}/%{ext_id}.xpi
%{_datadir}/metainfo/%{name}.metainfo.xml

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Dominik Mierzejewski <rpm@greysector.net> - 2.1.0-1
- update to 2.1.0 (#1546516)
- update bundled dependencies versions

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2.0.4-1
- update to 2.0.4 (#1504387)
- install metainfo file in the new standard location

* Thu Oct 05 2017 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2.0.3-1
- update to 2.0.3

* Mon Oct 02 2017 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2.0.1-2
- stop pretending to support SeaMonkey, it never worked
  (see http://addonconverter.fotokraina.com/compatibility/)

* Sun Oct 01 2017 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2.0.1-1
- update to 2.0.1
- update bundled stuff Provides and License field

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 26 2017 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1.3.2-1
- update to 1.3.2
- drop RHEL5 conditional

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 22 2016 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1.3.1-2
- add appstream file

* Fri Aug 19 2016 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1.3.1-1
- update to 1.3.1
- added versions to bundled font Provides

* Fri Mar 11 2016 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1.3.0-1
- update to 1.3.0
- package signed xpi from addons.mozilla.org
- add missing license tags
- add more Provides for bundled stuff

* Mon Mar 09 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1.2.1-1
- updated to 1.2.1
- added temporary Provides for bundled stuff

* Mon Dec 15 2014 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1.1.0-1
- updated to 1.1.0
- requires firefox >= 26
- simplify and improve install commands
- fix installation path for seamonkey

* Fri Oct 03 2014 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1.0.10.2-1
- updated to 1.0.10.2

* Mon Jun 02 2014 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1.0.10.1-1
- updated to 1.0.10.1

* Thu Mar 27 2014 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1.0.9-1
- Initial package
