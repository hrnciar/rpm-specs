Summary: OpenVPN plugin for LDAP authentication
Name: openvpn-auth-ldap
Version: 2.0.4
Release: 3%{?dist}
License: BSD
URL: https://github.com/threerings/openvpn-auth-ldap
Source0: https://github.com/threerings/openvpn-auth-ldap/archive/auth-ldap-%{version}.tar.gz
# tools are not compiled with given CFLAGS
Patch2: auth-ldap-tools-CFLAGS.patch
# Patch from upstream issue n°4, to fix tap bridging.
Patch4: auth-ldap-remoteAddress.patch
# This is a plugin not linked against a lib, so hardcode the requirement
# since we require the parent configuration and plugin directories
Requires: openvpn >= 2.0
Buildrequires: doxygen
BuildRequires: gcc-objc
BuildRequires: check-devel
BuildRequires: gnustep-base-devel
Buildrequires: openldap-devel
Buildrequires: openssl-devel
Buildrequires: openvpn-devel
BuildRequires: re2c
BuildRequires: autoconf

%description
The OpenVPN Auth-LDAP Plugin implements username/password authentication via
LDAP for OpenVPN 2.x.


%prep
%setup -q -n %{name}-auth-ldap-%{version}
%patch2 -p1 -b .tools-CFLAGS
%patch4 -p1 -b .remoteAddress
# Fix plugin from the instructions in the included README
sed -i 's|^plugin .*| plugin %{_libdir}/openvpn/plugins/openvpn-auth-ldap.so "/etc/openvpn/auth/ldap.conf"|g' README.md
autoconf
autoheader


%build
# Upstream's test for needing -std=gnu99 does not work in recent Fedora
# https://github.com/threerings/openvpn-auth-ldap/issues/78
# Missing -fPIC for some objects
%configure CFLAGS="%{optflags} -fPIC -std=gnu99" \
    --libdir=%{_libdir}/openvpn/plugins \
    --with-openvpn=%{_includedir}
%make_build


%install
# Main plugin
mkdir -p %{buildroot}%{_libdir}/openvpn/plugins
%make_install
# Example config file
install -D -p -m 0600 auth-ldap.conf \
    %{buildroot}%{_sysconfdir}/openvpn/auth/ldap.conf
# Compatibility
%if 0%{?rhel} == 6
mkdir -p %{buildroot}%{_libdir}/openvpn/plugin/lib
ln -s ../../plugins/openvpn-auth-ldap.so %{buildroot}%{_libdir}/openvpn/plugin/lib
%endif


%files
%license LICENSE
%doc README.md auth-ldap.conf
%dir %{_sysconfdir}/openvpn/auth/
%config(noreplace) %{_sysconfdir}/openvpn/auth/ldap.conf
%{_libdir}/openvpn/plugins/openvpn-auth-ldap.so
%if 0%{?rhel} == 6
%{_libdir}/openvpn/plugin
%endif


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 25 2019 Orion Poplawski <orion@nwra.com> - 2.0.4-1
- Update to 2.0.4
- Build against openvpn-plugin.h from openvpn-devel

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 28 2017 Orion Poplawski <orion@cora.nwra.com> - 2.0.3-24
- Add patch to fix ldap_result() return code check and resulting crash

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 19 2017 Orion Poplawski <orion@cora.nwra.com> - 2.0.3-21
- Rebuild for gnustep-base 1.25
- Cleanup spec

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 30 2015 Orion Poplawski <orion@cora.nwra.com> - 2.0.3-18
- Fix plugin location (bug #1270984)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 11 2014 Matthias Saou <matthias@saou.eu> 2.0.3-13
- Include remoteAddress patch from upstream issue n°4, to fix tap bridging.
- Only enable the modern objc on Fedora and EL7+ (not available on EL6).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 29 2013 Orion Poplawski <orion@cora.nwra.com> - 2.0.3-12
- Use gnustep runtime (bug #870988)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb  8 2012 Matthias Saou <matthias@saou.eu> 2.0.3-10
- Include patch to fix check for no longer existing objc/objc-api.h file.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Aug 13 2011 Matthias Saou <matthias@saou.eu> 2.0.3-8
- Minor spec file cleanups.
- Fix build on F-15+.
- Make sure tools/ content gets our CFLAGS.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Matthias Saou <matthias@saou.eu> 2.0.3-5
- Update URL and Source locations.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb  3 2008 Matthias Saou <matthias@saou.eu> 2.0.3-3
- No longer use the full openvpn sources for the build, as only the
  openvpn-plugin.h file is required, so just include it alone.
- Fix check to check-devel build requirement (it needs the header).

* Thu Jun 21 2007 Matthias Saou <matthias@saou.eu> 2.0.3-2
- Patch and change README to remove build instructions and have the proper
  line to be added to openvpn's configuration.
- Move config file to a sub-dir since it gets picked up by openvpn otherwise.

* Wed Jun 20 2007 Matthias Saou <matthias@saou.eu> 2.0.3-1
- Initial RPM release.

