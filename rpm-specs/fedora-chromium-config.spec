Name:           fedora-chromium-config
Version:        1.1
Release:        6%{?dist}
Summary:        Fedora customizations for Chromium/Chrome
License:        GPLv2+
# The upstream for this is a dist-git
URL:            https://src.fedoraproject.org/rpms/fedora-chromium-config
Source0:        https://src.fedoraproject.org/rpms/fedora-chromium-config/raw/master/f/LICENSE
Source1:        https://raw.githubusercontent.com/tpopela/fedora-user-agent-chrome/master/hojggiaghnldpcknpbciehjcaoafceil.json
# Configuration to support Kerberos GSSAPI logins to the Fedora Account System
Source2:        00_gssapi.json
Source3:        %{name}-tmpfiles.conf

BuildArch:      noarch

# For the _tmpfilesdir macro
BuildRequires:  systemd-rpm-macros

Obsoletes:      fedora-user-agent-chrome < 0.0.0.5
Provides:       fedora-user-agent-chrome = %{version}-%{release}

# Starting with Chromium 83, the Kerberos support works properly
Conflicts:      chromium < 83


%description
This package is used to install customizations for Chromium/Chrome that are
recommended by Fedora.

It includes a GSSAPI configuration that enables access to many Fedora Project
services. To add support for other domains, replace the symlink
/etc/chromium/policies/managed/00_gssapi.json with your own content.


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
# that includes the same keys and a filename that sorts alphabetically higher,
# it will supersede this file. "00" is chosen to sort as low as possible.
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/%{name}-tmpfiles.conf

mkdir -p %{buildroot}%{_sysconfdir}/opt/chrome/policies/managed \
         %{buildroot}%{_sysconfdir}/chromium/policies/managed \
         %{buildroot}%{_datadir}/chromium/policies/managed

cp -a %{SOURCE2} %{buildroot}%{_datadir}/chromium/policies/managed


%files
%license licenses/LICENSE

# Fedora User Agent Extension
%dir %{_datadir}/google-chrome
%dir %{_datadir}/google-chrome/extensions
%dir %{_datadir}/chromium
%dir %{_datadir}/chromium/extensions
%{_datadir}/google-chrome/extensions/hojggiaghnldpcknpbciehjcaoafceil.json
%{_datadir}/chromium/extensions/hojggiaghnldpcknpbciehjcaoafceil.json

# GSSAPI default configuration for fedoraproject.org
%{_datadir}/chromium/policies/managed/00_gssapi.json

# Chromium GSSAPI configuration symlinks
# By default, the Chromium configuration is symlinked to the
# default configuration in /usr/share/chromium using tmpfiles.d
%dir %{_sysconfdir}/chromium/
%dir %{_sysconfdir}/chromium/policies
%dir %{_sysconfdir}/chromium/policies/managed
%ghost %{_sysconfdir}/chromium/policies/managed/00_gssapi.json

# Google Chrome GSSAPI configuration symlinks
# By default, the Chrome configuration is symlinked to the Chromium
# policy. That way there is a single place to modify both together.
%dir %{_sysconfdir}/opt/chrome/
%dir %{_sysconfdir}/opt/chrome/policies
%dir %{_sysconfdir}/opt/chrome/policies/managed
%ghost %{_sysconfdir}/opt/chrome/policies/managed/00_gssapi.json

# systemd-tmpfilesd configuration for symlinks
%{_tmpfilesdir}/%{name}-tmpfiles.conf


%changelog
* Mon Jul 27 2020 Stephen Gallagher <sgallagh@redhat.com> - 1.1-6
- Enable GSSAPI support for Chromium
- Make the default configuration a symlink to /usr/share

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

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
