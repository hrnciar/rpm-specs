%if 0%{?fedora} < 28 && 0%{?rhel} < 8
%bcond_without libnm_glib
%else
%bcond_with libnm_glib
%endif

Summary:   NetworkManager VPN plugin for L2TP and L2TP/IPsec
Name:      NetworkManager-l2tp
Version:   1.8.2
Release:   2%{?dist}
License:   GPLv2+
URL:       https://github.com/nm-l2tp/NetworkManager-l2tp
Source:    https://github.com/nm-l2tp/NetworkManager-l2tp/releases/download/%{version}/%{name}-%{version}.tar.xz

%global ppp_version %(sed -n 's/^#define\\s*VERSION\\s*"\\([^\\s]*\\)"$/\\1/p' %{_includedir}/pppd/patchlevel.h 2>/dev/null | grep . || echo bad)

BuildRequires: glib2-devel
BuildRequires: gtk3-devel
BuildRequires: NetworkManager-libnm-devel >= 1:1.2.0
BuildRequires: libnma-devel >= 1.2.0
BuildRequires: ppp-devel
BuildRequires: libtool intltool gettext
BuildRequires: libsecret-devel
%if %with libnm_glib
BuildRequires: NetworkManager-glib-devel >= 1:1.2.0
BuildRequires: libnm-gtk-devel >= 1.2.0
%endif
BuildRequires: openssl-devel
BuildRequires: nss-devel

Requires: dbus
Requires: NetworkManager >= 1:1.2.0
Requires: ppp = %{ppp_version}
Requires: xl2tpd
%if 0%{?fedora} < 24 && 0%{?rhel} < 8
Requires: libreswan
%else
Recommends: (libreswan or strongswan)
%endif

%global __provides_exclude ^libnm-.*\\.so

%description
This package contains software for integrating L2TP and L2TP over
IPsec VPN support with the NetworkManager.

%package gnome
Summary: NetworkManager VPN plugin for L2TP and L2TP/IPsec - GNOME files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description gnome
This package contains software for integrating L2TP and L2TP over
IPsec VPN support with the NetworkManager (GNOME files).

%prep
%setup -q

%build
if [ ! -f configure ]; then
  autoreconf -fi
  intltoolize
fi
%configure \
    --disable-static \
%if %with libnm_glib
    --with-libnm-glib \
%endif
    --with-pppd-plugin-dir=%{_libdir}/pppd/%{ppp_version} \
    --with-dist-version=%{version}-%{release}
make %{?_smp_mflags}

%check
make check

%install
make install DESTDIR=%{buildroot} INSTALL="%{__install} -p"

rm -f %{buildroot}%{_libdir}/NetworkManager/lib*.la
rm -f %{buildroot}%{_libdir}/pppd/%{ppp_version}/*.la

mkdir -p %{buildroot}%{_sysconfdir}/ipsec.d
mkdir -p %{buildroot}%{_sysconfdir}/strongswan/ipsec.d
touch %{buildroot}%{_sysconfdir}/ipsec.d/ipsec.nm-l2tp.secrets
touch %{buildroot}%{_sysconfdir}/strongswan/ipsec.d/ipsec.nm-l2tp.secrets

%find_lang %{name}

%pre
# remove any NetworkManager-l2tp <= 1.2.10 transient ipsec-*.secrets files.
rm -f %{_sysconfdir}/ipsec.d/nm-l2tp-ipsec-*.secrets
rm -f %{_sysconfdir}/strongswan/ipsec.d/nm-l2tp-ipsec-*.secrets
exit 0

%files -f %{name}.lang
%{_libdir}/NetworkManager/libnm-vpn-plugin-l2tp.so
%{_sysconfdir}/dbus-1/system.d/nm-l2tp-service.conf
%{_prefix}/lib/NetworkManager/VPN/nm-l2tp-service.name
%{_libexecdir}/nm-l2tp-service
%{_libdir}/pppd/%{ppp_version}/nm-l2tp-pppd-plugin.so
%ghost %attr(0600 - -) %{_sysconfdir}/ipsec.d/ipsec.nm-l2tp.secrets
%ghost %attr(0600 - -) %{_sysconfdir}/strongswan/ipsec.d/ipsec.nm-l2tp.secrets
%doc AUTHORS README.md NEWS
%license COPYING

%files gnome
%{_libexecdir}/nm-l2tp-auth-dialog
%{_libdir}/NetworkManager/libnm-vpn-plugin-l2tp-editor.so
%{_datadir}/appdata/network-manager-l2tp.metainfo.xml

%if %with libnm_glib
%{_sysconfdir}/NetworkManager/VPN/nm-l2tp-service.name
%{_libdir}/NetworkManager/libnm-*-properties.so
%endif

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 26 2020 Douglas Kosovic <doug@uq.edu.au> - 1.8.2-1
- Updated to 1.8.2 release
- Remove redundant patches
- Recommends (libreswan or strongswan) instead of just libreswan

* Thu Feb 27 2020 Douglas Kosovic <doug@uq.edu.au> - 1.8.0-5
- Patch for user certificate support fix

* Wed Feb 26 2020 Douglas Kosovic <doug@uq.edu.au> - 1.8.0-4
- Patch to support libreswan 3.30 which is no longer built with modp1024 support

* Sat Feb 22 2020 Adam Williamson <awilliam@redhat.com> - 1.8.0-3
- Rebuild for new ppp

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Douglas Kosovic <doug@uq.edu.au> - 1.8.0-1
- Updated to 1.8.0 release

* Wed Nov 06 2019 Douglas Kosovic <doug@uq.edu.au> - 1.2.16-1
- Updated to 1.2.16 release

* Tue Oct 08 2019 Douglas Kosovic <doug@uq.edu.au> - 1.2.14-1
- Updated to 1.2.14 release

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Douglas Kosovic <doug@uq.edu.au> - 1.2.12-1
- Updated to 1.2.12 release
- Use upstream provided xz tarball instead of GitHub generated gz tarball.
- Delete any transient nm-l2tp-ipsec-*.secrets files from versions <= 1.2.10
- %%ghost transient ipsec.nm-l2tp.secrets files.
- Merged EPEL 7 spec file with Fedora spec file.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 20 2018 Douglas Kosovic <doug@uq.edu.au> - 1.2.10-2
- Drop NetworkManager-devel for rawhide

* Tue Mar 20 2018 Douglas Kosovic <doug@uq.edu.au> - 1.2.10-1
- Updated to 1.2.10 release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Lubomir Rintel <lkundrak@v3.sk> - 1.2.8-4
- Drop libnm-glib for Fedora 28

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Douglas Kosovic <doug@uq.edu.au> - 1.2.8-1
- Updated to 1.2.8 release
- Replaced requires libreswan with weaker recommends libreswan,
  allows uninstalling of libreswan if IPsec support isn't required

* Fri May 19 2017 Douglas Kosovic <doug@uq.edu.au> - 1.2.6-1
- Updated to 1.2.6 release
- Added %%check section

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 20 2016 Douglas Kosovic <doug@uq.edu.au> - 1.2.4-1
- Update to 1.2.4 release
- Remove GTK dependency from base package (rh#1088677)
- Introduce new GTK-free VPN plugin base-library to nm-l2tp package
- Don't require nm-connection-editor anymore
- No need for --enable-more-warnings=yes configure switch anymore

* Mon May 16 2016 Douglas Kosovic <doug@uq.edu.au> - 1.2.2-1
- Updated to 1.2.2 release
- Added NetworkManager-l2tp-gnome RPM for GNOME files
- Updated BuildRequires, Requires, URL and Source
- Replaced filter_provides macro with newer macros

* Sat Apr 23 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.2.0-1
- Update to 1.2.0 release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.3.20151023git3239062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 27 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.2.0-0.2.20151023git3239062
- Fix el7 build

* Fri Oct 23 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.2.0-0.1.20151023git3239062
- Update to 1.2 git snapshot with libnm-based properties plugin

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Kevin Fenzi <kevin@scrye.com> 0.9.8.7-2
- Rebuild for new ppp version.

* Thu Jul 31 2014 Ivan Romanov <drizt@land.ru> - 0.9.8.7-1
- updated to 0.9.8.7

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 11 2014 Ivan Romanov <drizt@land.ru> - 0.9.8.6-2
- use ppp of any version
- dropped Groups tag

* Thu Feb 27 2014 Ivan Romanov <drizt@land.ru> - 0.9.8.6-1
- updated to 0.9.8.6

* Sun Jan 19 2014 Ivan Romanov <drizt@land.ru> - 0.9.8.5-1
- updated to 0.9.8.5
- dropped patches, went to upstream

* Mon Sep 23 2013 Ivan Romanov <drizt@land.ru> - 0.9.8-4
- added NetworkManager-l2tp-Check-var-run-pluto-ipsec-info patch (#887674)

* Mon Sep 23 2013 Ivan Romanov <drizt@land.ru> - 0.9.8-3
- added NetworkManager-l2tp-noccp-pppd-option patch (#887674)

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr  1 2013 Ivan Romanov <drizt@land.ru> - 0.9.8-1
- a new upstream version

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 25 2012 Ivan Romanov <drizt@land.ru> - 0.9.6-5
- openswan is requires

* Tue Dec 25 2012 Ivan Romanov <drizt@land.ru> - 0.9.6-4
- added openswan to BR

* Sat Dec 15 2012 Ivan Romanov <drizt@land.ru> - 0.9.6-3
- fix F17 dependency error (rh #886773)
- added licensies explanations

* Mon Nov 26 2012 Ivan Romanov <drizt@land.ru> - 0.9.6-2
- corrected License tag. Added LGPLv2+
- use only %%{buildroot}
- use %%config for configuration files
- removed unused scriptlets
- cleaned .spec file
- preserve timestamps when installing
- filtered provides for plugins
- droped zero-length changelog
- use %%global instead of %%define

* Mon Nov 19 2012 Ivan Romanov  <drizt@land.ru> - 0.9.6-1
- initial version based on NetworkManager-pptp 1:0.9.3.997-3

