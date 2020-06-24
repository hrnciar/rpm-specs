# common macros, yet to be defined. see:
# https://fedoraproject.org/wiki/User:Kalev/MozillaExtensionsDraft
%global ext_id uBlock0@raymondhill.net

%global firefox_app_id \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%global firefox_inst_dir %{_datadir}/mozilla/extensions/%{firefox_app_id}

%global fileid 3551054

Name:           mozilla-ublock-origin
Version:        1.26.2
Release:        1%{?dist}
Summary:        An efficient blocker for Firefox

License:        GPLv3+ and LGPLv3 and MIT and OFL
URL:            https://github.com/gorhill/uBlock
Source0:        https://addons.mozilla.org/firefox/downloads/file/%{fileid}/ublock_origin-%{version}-an+fx.xpi
Source1:        mozilla-ublock-origin.metainfo.xml

Requires:       mozilla-filesystem
BuildArch:      noarch
BuildRequires:  libappstream-glib
# css/fonts/fontawesome-webfont.ttf http://fontawesome.io/ OFL
# img/fontawesome/fontawesome-defs.svg
Provides:       bundled(fontawesome-fonts) = 4.7.0
# lib/punycode.js https://mths.be/punycode MIT
Provides:       bundled(js-punycode) = 1.3.2
# lib/diff https://github.com/Swatinem/diff LGPLv3
Provides:       bundled(js-github-swatinem-diff)
# lib/codemirror http://codemirror.net MIT
Provides:       bundled(js-codemirror) = 5.37.0
# lib/lz4 https://github.com/gorhill/lz4-wasm BSD
Provides:       bundled(lz4-wasm)

%description
An efficient blocker: easy on memory and CPU footprint, and yet can load and
enforce thousands more filters than other popular blockers out there.

Flexible, it's more than an "ad blocker": it can also read and create filters
from hosts files.

%prep
%setup -qc

%build
echo Nothing to build

%install
install -Dpm644 %{SOURCE0} %{buildroot}%{firefox_inst_dir}/%{ext_id}.xpi

install -Dpm644 %{SOURCE1} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%files
%license LICENSE.txt css/fonts/OFL.txt lib/codemirror/LICENSE
%{firefox_inst_dir}/%{ext_id}.xpi
%{_metainfodir}/%{name}.metainfo.xml

%changelog
* Sun May 03 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.26.2-1
- update to 1.26.2 (#1825039)

* Sun Apr 12 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.26.0-1
- update to 1.26.0 (#1820622)

* Sat Mar 14 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.25.2-1
- update to 1.25.2 (#1797341)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 01 2019 Dominik Mierzejewski <rpm@greysector.net> - 1.24.2-1
- update to 1.24.2 (#1763778)

* Sat Sep 28 2019 Dominik Mierzejewski <rpm@greysector.net> - 1.22.4-1
- update to 1.22.4 (#1756060)

* Wed Sep 11 2019 Dominik Mierzejewski <rpm@greysector.net> - 1.22.2-2
- fix wrong fileid (was pointing to 1.20.0 instead of 1.22.2)

* Mon Sep 09 2019 Dominik Mierzejewski <rpm@greysector.net> - 1.22.2-1
- update to 1.22.2 (#1713383)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 13 2019 Dominik Mierzejewski <rpm@greysector.net> - 1.19.2-1
- update to 1.19.2 (#1689200)

* Thu Mar 14 2019 Dominik Mierzejewski <rpm@greysector.net> - 1.18.6-1
- update to 1.18.6 (#1680421)
- drop conditionals that are true in F26+

* Wed Feb 20 2019 Dominik Mierzejewski <rpm@greysector.net> - 1.18.4-1
- update to 1.18.4 (#1669295)
- update bundled fontawesome version

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Dominik Mierzejewski <rpm@greysector.net> - 1.17.2-1
- update to 1.17.2

* Mon Jul 30 2018 Dominik Mierzejewski <rpm@greysector.net> - 1.16.14-1
- update to 1.16.14 (#1598265)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Dominik Mierzejewski <rpm@greysector.net> - 1.16.12-1
- update to 1.16.12 (#1567576)

* Wed May 23 2018 Dominik Mierzejewski <rpm@greysector.net> - 1.16.6-1
- update to 1.16.6 (#1567576)
- update bundled codemirror version

* Fri Apr 13 2018 Dominik Mierzejewski <rpm@greysector.net> - 1.15.24-1
- update to 1.15.24
- use correct path for metainfo file
- update bundled components list and license tag
- include license texts in the standard location, too

* Tue Feb 20 2018 Dominik Mierzejewski <rpm@greysector.net> - 1.15.10-1
- update to 1.15.10

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Dominik Mierzejewski <rpm@greysector.net> - 1.14.24-1
- update to 1.14.24

* Fri Dec 29 2017 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1.14.22-1
- update to 1.14.22
- install the appdata metainfo file into correct place

* Wed Nov 29 2017 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1.14.18-1
- Initial package
