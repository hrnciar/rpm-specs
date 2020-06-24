Name:           fedora-chromium-config
Version:        1.1
Release:        4%{?dist}
Summary:        Fedora customizations for Chromium/Chrome
License:        GPLv2+
# The upstream for this is a dist-git
URL:            https://src.fedoraproject.org/rpms/fedora-chromium-config
Source0:        https://src.fedoraproject.org/rpms/fedora-chromium-config/raw/master/f/LICENSE
Source1:        https://raw.githubusercontent.com/tpopela/fedora-user-agent-chrome/master/hojggiaghnldpcknpbciehjcaoafceil.json
# Configuration to support Kerberos GSSAPI logins to the Fedora Account System
Source2:    00_gssapi.json

BuildArch:      noarch

Obsoletes:      fedora-user-agent-chrome < 0.0.0.5
Provides:       fedora-user-agent-chrome = %{version}-%{release}


%description
This package is used to install customizations for Chromium/Chrome that are
recommended by Fedora.


%prep
mkdir -p %{_builddir}/licenses
cp -a %{SOURCE0} %{_builddir}/licenses/


%build


%install

mkdir -p %{buildroot}%{_datadir}/google-chrome/extensions
mkdir -p %{buildroot}%{_datadir}/chromium/extensions

cp -a %{SOURCE1} %{buildroot}%{_datadir}/google-chrome/extensions
cp -a %{SOURCE1} %{buildroot}%{_datadir}/chromium/extensions

# Install the FAS kerberos configuration for Chrome
# The managed policy directory does not merge identical keys and we don't want
# to accidentally override any configuration that a site has installed here, so
# we install it as 00_gssapi.json. If another file is present in this directory
# that includes the same keys, it will supersede this file.
#
# At the moment, we cannot do the same for Chromium because of
# https://bugzilla.redhat.com/show_bug.cgi?id=1640158
# which results in a segfault if more than one TGT is present, which is common
# for Red Hat employees working on Fedora.

mkdir -p %{buildroot}%{_sysconfdir}/opt/chrome/policies/managed
cp -a %{SOURCE2} %{buildroot}%{_sysconfdir}/opt/chrome/policies/managed/


%files
%dir %{_datadir}/google-chrome
%dir %{_datadir}/google-chrome/extensions
%dir %{_datadir}/chromium
%dir %{_datadir}/chromium/extensions
%{_datadir}/google-chrome/extensions/hojggiaghnldpcknpbciehjcaoafceil.json
%{_datadir}/chromium/extensions/hojggiaghnldpcknpbciehjcaoafceil.json

%dir %{_sysconfdir}/opt/chrome/policies/managed/
%config(noreplace)%{_sysconfdir}/opt/chrome/policies/managed/00_gssapi.json

%license licenses/LICENSE


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Stephen Gallagher <sgallagh@redhat.com> - 1.1-1
- Add Kerberos GSSAPI configuration for the Fedora Account System

* Tue Oct 16 2018 Tomas Popela <tpopela@redhat.com> - 1.0-0
- Initial packaging (by renaming the fedora-user-agent-chrome package)
