%global pname   remote
%global __provides_exclude_from ^%{vdr_libdir}/.*\\.so.*$

Name:           vdr-%{pname}
Version:        0.7.0
Release:        12%{?dist}
Summary:        Extended remote control plugin for VDR

License:        GPL+
URL:            http://www.escape-edv.de/endriss/vdr/
Source0:        http://www.escape-edv.de/endriss/vdr/%{name}-%{version}.tgz
Source1:        %{name}.conf
Source2:        %{name}-udev.rules
# Status query mail sent to upstream and Debian patchkit maintainer 2008-10-25
Patch0:         http://zap.tartarus.org/~ds/debian/dists/stable/main/source/vdr-plugin-remote_0.3.8-3.ds.diff.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  vdr-devel >= 1.7.38
BuildRequires:  gettext
BuildRequires:  systemd
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}
# systemd >= 214-3 for the input group
Requires:       systemd >= 214-3

%description
This plugin extends VDR's remote control capabilities, adding support
for Linux input devices, keyboards (tty), TCP connections, and LIRC.


%prep
%autosetup -n %{pname}-%{version} -p1

patch -p1 -i debian/patches/02_no_abort.dpatch
sed -i \
    -e 's/0\.3\.8/%{version}/g' \
    -e 's/"Remote control"/trNOOP("Remote control")/' \
    debian/patches/04_constness.dpatch
patch -p1 -i debian/patches/04_constness.dpatch

for f in CONTRIBUTORS HISTORY ; do
    iconv -f iso-8859-1 -t utf-8 $f > $f.utf-8 ; mv $f.utf-8 $f
done


%build
%make_build


%install
%make_install
install -Dpm 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
install -Dpm 644 %{SOURCE2} \
    %{buildroot}/%{_udevrulesdir}/52-%{name}.rules
%find_lang %{name}


%pre
usermod -a -G input %{vdr_user} || :


%files -f %{name}.lang
%license COPYING
%doc CONTRIBUTORS FAQ HISTORY README
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%config(noreplace) %{_udevrulesdir}/*-%{name}.rules
%{vdr_libdir}/libvdr-%{pname}.so.%{vdr_apiversion}


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-10
- Rebuilt for new VDR API version

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-8
- Fix FTBFS due missing BR gcc gcc-c++
- Move rules file to %%{_udevrulesdir} (RHBZ 1226698)
- Add BR systemd

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 21 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.7.0-1
- Update to 0.7.0

* Mon Jul  6 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.6.0-5
- Build with proper plugin build config, fixes LDFLAGS

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun  1 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.6.0-3
- Simplify udev rules, add vdr user to the input group

* Sun Apr 12 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.6.0-2
- Update to 0.6.0

* Thu Feb 19 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.5.0-14
- Rebuild

* Sat Jan 31 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.5.0-13
- Ship COPYING as %%license
- Use %%autosetup

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.5.0-10
- Rebuild

* Sun Mar 23 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.5.0-9
- Update README path in .conf

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 31 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.5.0-7
- Rebuild.

* Sat Mar 16 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.5.0-6
- Rebuild.

* Wed Mar 13 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.5.0-5
- Rebuild.

* Sun Mar 03 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.5.0-4
- Rebuild.

* Mon Feb 18 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.5.0-3
- Adapt to VDR >= 1.7.38 build.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 26 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.5.0-1
- Update to 0.5.0.

* Tue Oct 02 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.4.0-23
- Rebuild.

* Thu Sep 13 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.4.0-22
- Rebuild.

* Thu Jul 19 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.4.0-21
- Rebuild.

* Wed Jun 27 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.4.0-20
- Rebuild.

* Tue Mar 27 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.4.0-19
- Rebuild.

* Sun Mar 11 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.4.0-18
- Rebuild.

* Tue Mar  6 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.4.0-17
- Rebuild.

* Mon Feb 20 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.4.0-16
- Rebuild.

* Sun Jan 15 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.4.0-15
- Rebuild.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec  4 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.4.0-13
- Rebuild.

* Sun Nov  6 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.4.0-12
- Clean up specfile constructs no longer needed with Fedora or EL6+.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Oct 17 2010 Ville Skyttä <ville.skytta@iki.fi> - 0.4.0-10
- Make config more likely to work out of the box in common setups.

* Thu Sep  3 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.4.0-9
- Filter out autoprovided libvdr-*.so.* (if %%filter_setup is available).

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.4.0-8
- Use ISA qualified dependency to vdr(abi).
- Use %%global instead of %%define.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 30 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.4.0-5
- First Fedora build (#466974).
- Add specfile comments about patch statuses.
- Prune pre-0.4.0 %%changelog entries.

* Sat Oct 25 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.4.0-4
- Use ATTRS, not SYSFS in example udev rules.

* Tue Oct 14 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.4.0-3
- Fix install of localizations when built with 1.6.x.
- Add example udev rules file, improve sysconfig snippet docs.

* Mon Aug 04 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.4.0-2
- rebuild

* Tue Apr  8 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.4.0-1
- 0.4.0.
- Build for VDR 1.6.0.
