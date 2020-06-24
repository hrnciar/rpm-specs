%global pname   osdteletext
%global __provides_exclude_from ^%{vdr_plugindir}/.*\\.so.*$

Name:           vdr-%{pname}
Version:        0.9.7
Release:        8%{?dist}
Summary:        OSD teletext plugin for VDR

License:        GPLv2+
URL:            http://projects.vdr-developer.org/projects/show/plg-osdteletext
Source0:        https://projects.vdr-developer.org/attachments/download/2161/%{name}-%{version}.tgz
Source1:        %{name}.conf
# https://www.vdr-portal.de/index.php?attachment/41771-osdteletext-0-9-7-patch/
Patch0:         %{pname}-%{version}.patch
# https://www.vdr-portal.de/index.php?attachment/41884-osdteletext-4bpp-diff/
Patch1:         %{pname}-4bpp.diff

BuildRequires:  gcc-c++
BuildRequires:  vdr-devel >= 1.7.39
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description
The OSD teletext plugin displays teletext directly on VDR's on-screen
display, with sound and video from the current channel playing in the
background.


%prep
%autosetup -n %{pname}-%{version}
sed -i -e 's|/var/cache/vdr/vtx|%{vdr_rundir}/%{pname}|g' \
    osdteletext.c README README.DE rootdir.c


%build
%make_build


%install
%make_install

install -dm 755 $RPM_BUILD_ROOT%{vdr_rundir}/%{pname}
install -dm 755 $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d
echo "d %{vdr_rundir}/%{pname} 0755 %{vdr_user} root -" > \
  $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d/%{name}.conf

install -Dpm 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf

%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc HISTORY README*
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%{vdr_plugindir}/libvdr-%{pname}.so.%{vdr_apiversion}
%{_prefix}/lib/tmpfiles.d/%{name}.conf
%attr(-,%{vdr_user},root) %{vdr_rundir}/%{pname}/


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.9.7-6
- Rebuilt for new VDR API version

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 06 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.7-3
- Add %{pname}-4bpp.diff

* Sun Apr 29 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.7-2
- Add %%{pname}-%%{version}.patch
- Rebuilt for vdr-2.4.0

* Sun Feb 25 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.9.7-1
- Update to 0.9.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.9.6-1
- Update to 0.9.6

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.5-3
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.9.5-2
- Rebuild

* Tue Feb 17 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.9.5-1
- Update to 0.9.5

* Sat Jan 31 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.9.4-9
- Ship COPYING as %%license

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.9.4-6
- Rebuild

* Sun Mar 23 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.9.4-5
- Update README path in .conf

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 31 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.9.4-3
- Rebuild.

* Sat Mar 16 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.9.4-2
- Rebuild.

* Wed Mar 13 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.9.4-1
- Update to 0.9.4.

* Sun Mar  3 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.9.3-8
- Move default cache dir to the by-default tmpfs %%{vdr_rundir}.

* Mon Feb 18 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.9.3-7
- Rebuild.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 02 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.9.3-5
- Rebuild.

* Thu Sep 13 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.9.3-4
- Rebuild.

* Thu Jul 19 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.9.3-3
- Rebuild.

* Wed Jun 27 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.9.3-2
- Rebuild.

* Wed Apr  4 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.9.3-1
- Update to 0.9.3.

* Mon Mar 26 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.9.2-1
- Update to 0.9.2.

* Sun Mar 11 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.9.1-8
- Apply upstream VDR 1.7.26+ patch.

* Tue Mar  6 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.9.1-7
- Apply Udo Richter's patch taking advantage of new VDR 1.7.25 features.

* Mon Feb 20 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.9.1-6
- Rebuild.

* Sun Jan 15 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.9.1-5
- Rebuild.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec  4 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.9.1-3
- Rebuild.

* Sun Nov  6 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.9.1-2
- Clean up specfile constructs no longer needed with Fedora or EL6+.

* Sat Aug 20 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.9.1-1
- Update to 0.9.1.
- Use rpm >= 4.9's Provides filtering instead of the old Fedora way.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov  6 2010 Ville Skyttä <ville.skytta@iki.fi> - 0.9.0-1
- Update to 0.9.0.

* Sun Aug 29 2010 Ville Skyttä <ville.skytta@iki.fi> - 0.8.3-5
- Make built in cache path match default configuration.

* Thu Sep  3 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.8.3-4
- Filter out autoprovided libvdr-*.so.* (if %%filter_setup is available).

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.8.3-3
- Use ISA qualified dependency to vdr(abi).
- Use %%global instead of %%define.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun  4 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.8.3-1
- Update to 0.8.3.

* Tue May 26 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.8.2-1
- Update to 0.8.2.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 11 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.8.1-1
- 0.8.1.
- Trim pre-Fedora %%changelog entries.

* Sun Dec 21 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.7.0-1
- 0.7.0.

* Sun Dec 14 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.6.0-1
- 0.6.0 (new community upstream), patches applied upstream.

* Mon Apr  7 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.5.1-31
- Apply VDR 1.5+ patch from e-tobi.net Debian package.
- Build for VDR 1.6.0.

* Sat Feb 16 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.5.1-30
- Rebuild.

* Wed Aug 22 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.5.1-29
- BuildRequires: gawk for extracting APIVERSION.

* Tue Aug  7 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.5.1-28
- License: GPLv2+

* Sun Jan  7 2007 Ville Skyttä <ville.skytta@iki.fi> - 0.5.1-27
- Rebuild for VDR 1.4.5.

* Sun Nov 12 2006 Ville Skyttä <ville.skytta@iki.fi> - 0.5.1-26
- First FE build.
