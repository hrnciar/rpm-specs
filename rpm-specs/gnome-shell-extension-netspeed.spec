# https://github.com/hedayaty/NetSpeed/commit/9d7459967d3e38f9330e40b047db76013ea623f8
%global uuid netspeed@hedayaty.gmail.com
%global commit  9d7459967d3e38f9330e40b047db76013ea623f8
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20200323
# Minimum GNOME Shell version supported
%global min_gs_version 3.20

Name:           gnome-shell-extension-netspeed
Version:        3.30
Release:        0.9.%{gitdate}git%{shortcommit}%{?dist}
Summary:        A gnome-shell extension to show speed of the internet
License:        GPLv3+
URL:            https://github.com/hedayaty/NetSpeed
Source0:        https://github.com/hedayaty/NetSpeed/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  gnome-common
Requires:       gnome-shell-extension-common >= %{min_gs_version}

%description
Add an Internet speed indicator to status area.

%prep
%setup -q -n NetSpeed-%{commit}
sed -i -e 's|LANGUAGES=de en_CA fa fr it pt_BR ru zh_CN zh_TW|LANGUAGES=de en_CA es_ES fa fr it nl_NL pt_BR ru tr zh_CN zh_TW|' Makefile

%build
%make_build

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas
install -Dp -m 0644 {extension.js,lib.js,net_speed*.js,metadata.json,stylesheet.css,prefs.js} \
    %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/
install -Dp -m 0644 schemas/org.gnome.shell.extensions.netspeed.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/

# install language files
mkdir -p %{buildroot}%{_datadir}/locale/{ca,de,en_CA,es_ES,fa,fr,it,nl_NL,pt_BR,ru,tr,zh_CN,zh_TW}/LC_MESSAGES
for l in ca de en_CA es_ES fa fr it nl_NL pt_BR ru tr zh_CN zh_TW; do
  install -Dp -m 0644 locale/"$l"/LC_MESSAGES/netspeed.mo \
  %{buildroot}%{_datadir}/locale/"$l"/LC_MESSAGES/
done

# remove precompiled gschemas
rm -rf %{builddir}/%{_datadir}/gnome-shell/extensions/%{uuid}/schemas/

%find_lang netspeed

%files -f netspeed.lang
%license gpl-2.0.md
%doc CHANGELOG README.md
%{_datadir}/gnome-shell/extensions/%{uuid}/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.netspeed.gschema.xml

%changelog
* Mon Apr 13 2020 Martin Gansser <martinkg@fedoraproject.org> - 3.30-0.9.20200323git9d74599
- Add missing lib.js file (RHBZ#1823337)

* Wed Apr 01 2020 Martin Gansser <martinkg@fedoraproject.org> - 3.30-0.8.20200323git9d74599
- Update to 3.30-0.8.20200323git9d74599

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.30-0.7.20191015gitafff448
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 25 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.30-0.6.20191015gitafff448
- Add missing locales

* Fri Oct 25 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.30-0.5.20191015gitafff448
- Update to 3.30-0.5.20191015gitafff448

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.30-0.4.20190430gita62e19b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.30-0.3.20190430gita62e19b
- Add ru lang files
- Pump up version to 3.30

* Tue Apr 30 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.29-0.2.20190430gita62e19b
- Update to 3.29-0.2.20190430gita62e19b

* Sun Apr 28 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.29-0.1.20190422git05accfc
- Update to 3.29-0.1.20190422git05accfc

* Fri Apr 19 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.28-0.8.20181019gitc109544
- Add support for gnome 3.32

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.28-0.7.20181019gitc109544
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 25 2018 Martin Gansser <martinkg@fedoraproject.org> - 3.28-0.6.20181019gitc109544
- Update to recent git version 3.28-0.6.20181019gitc109544

* Fri Sep 28 2018 Martin Gansser <martinkg@fedoraproject.org> - 3.28-0.5.20180208gite3cea60
- Add support for gnome 3.30

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28-0.4.20180208gite3cea60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 Martin Gansser <martinkg@fedoraproject.org> - 3.28-0.3.20180208gite3cea60
- Remove scriptlet glib-compile-schemas: This scriptlet SHOULD NOT be used in Fedora 24 or later.
- Remove Group: is not used in Fedora
- Add -q to %%setup to make it quiet

* Wed Feb 07 2018 Martin Gansser <martinkg@fedoraproject.org> - 3.28-0.2.20180208gite3cea60
- Update to recent git version 3.28-0.2.20180208gite3cea60

* Wed Feb 07 2018 Martin Gansser <martinkg@fedoraproject.org> - 3.28-0.1.20180207git02a51b2
- Update to recent git version 3.28-0.1.20180207git02a51b2

* Wed Jul 19 2017 Martin Gansser <martinkg@fedoraproject.org> - 3.17-0.8.20170719git0b769d5
- Update to recent git version 3.17-0.8.20170719git0b769d5

* Wed Mar 29 2017 Martin Gansser <martinkg@fedoraproject.org> - 3.17-0.7.20160806git16a25ec
- Add netspeed_schema.patch

* Tue Mar 21 2017 Martin Gansser <martinkg@fedoraproject.org> - 3.17-0.6.20160806git16a25ec
- Add missing colon at Source1 tag
- Remove schemas in the extension's own directory 

* Mon Mar 20 2017 Martin Gansser <martinkg@fedoraproject.org> - 3.17-0.5.20160806git16a25ec
- Add fix_gettext-domain.patch

* Sat Mar 18 2017 Martin Gansser <martinkg@fedoraproject.org> - 3.17-0.4.20160806git16a25ec
- Take license file in plain text
- Add correct link to gnome-version.patch file
- Remove precompiled gschemas
- Add RR gnome-shell-extension-common
- Add fix_I18n_error_on_Gnome_3_14.patch
- Add fix_language_po_files.patch

* Wed Sep 21 2016 Martin Gansser <martinkg@fedoraproject.org> - 3.17-0.3.20160806git16a25ec
- Add LICENSE file

* Wed Sep 21 2016 Martin Gansser <martinkg@fedoraproject.org> - 3.17-0.2.20160806git16a25ec
- Use correct git release version
- Use correct version 3.17

* Fri Sep 16 2016 Martin Gansser <martinkg@fedoraproject.org> - 3.17-0.1.20160806git16a25ec
- Update to 3.17

* Fri Feb 12 2016 Martin Gansser <martinkg@fedoraproject.org> - 3.16-0.2.20150907gita83ed37
- Initial package for Fedora
