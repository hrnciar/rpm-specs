%global pname   femon
%global __provides_exclude_from ^%{vdr_libdir}/.*\\.so.*$

Name:           vdr-%{pname}
Version:        2.4.0
Release:        7%{?dist}
Summary:        DVB frontend status monitor plugin for VDR

License:        GPLv2+
URL:            http://www.saunalahti.fi/~rahrenbe/vdr/femon/
Source0:        http://www.saunalahti.fi/~rahrenbe/vdr/femon/files/%{name}-%{version}.tgz
Source1:        %{name}.conf

BuildRequires:  gcc-c++
BuildRequires:  vdr-devel >= 2.4.0
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description
DVB frontend status monitor is a plugin that displays some signal
information parameters of the current tuned channel on VDR's OSD.  You
can zap through all your channels and the plugin should be monitoring
always the right frontend.  The transponder and stream information are
also available in advanced display modes.


%prep
%setup -q -n %{pname}-%{version}


%build
%make_build


%install
%make_install
install -Dpm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc HISTORY README
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%{vdr_libdir}/libvdr-%{pname}.so.%{vdr_apiversion}


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-5
- Rebuilt for new VDR API version

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 10 2018 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-3
- Rebuilt

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 25 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.4.0-1
- Update to 2.4.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Sun Apr  5 2015 Ville Skyttä <ville.skytta@iki.fi> - 2.2.1-1
- Update to 2.2.1

* Sat Feb 21 2015 Ville Skyttä <ville.skytta@iki.fi> - 2.2.0-1
- Update to 2.2.0

* Thu Feb 19 2015 Ville Skyttä <ville.skytta@iki.fi> - 2.1.1-1
- Update to 2.1.1

* Sat Jan 31 2015 Ville Skyttä <ville.skytta@iki.fi> - 2.0.4-6
- Ship COPYING as %%license

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Ville Skyttä <ville.skytta@iki.fi> - 2.0.4-3
- Rebuild

* Sat Mar 22 2014 Ville Skyttä <ville.skytta@iki.fi> - 2.0.4-2
- Rebuild

* Tue Mar 18 2014 Ville Skyttä <ville.skytta@iki.fi> - 2.0.4-1
- Update to 2.0.4.

* Tue Mar 11 2014 Ville Skyttä <ville.skytta@iki.fi> - 2.0.3-1
- Update to 2.0.3.

* Mon Jan 20 2014 Ville Skyttä <ville.skytta@iki.fi> - 2.0.2-1
- Update to 2.0.2.

* Sat Jan 11 2014 Ville Skyttä <ville.skytta@iki.fi> - 2.0.1-1
- Update to 2.0.1.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr  2 2013 Ville Skyttä <ville.skytta@iki.fi> - 2.0.0-1
- Update to 2.0.0.

* Sun Mar 31 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.7.19-3
- Rebuild.

* Sat Mar 16 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.7.19-2
- Rebuild.

* Wed Mar 13 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.7.19-1
- Update to 1.7.19.

* Sun Mar  3 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.7.18-2
- Rebuild.

* Mon Feb 18 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.7.18-1
- Update to 1.7.18.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 02 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.17-5
- Rebuild.

* Thu Sep 13 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.17-4
- Rebuild.

* Thu Jul 19 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.17-3
- Rebuild.

* Wed Jun 27 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.17-2
- Rebuild.

* Wed Apr  4 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.17-1
- Update to 1.7.17.

* Mon Mar 26 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.16-1
- Update to 1.7.16.

* Sat Mar 17 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.15-1
- Update to 1.7.15.

* Sun Mar 11 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.14-1
- Update to 1.7.14.

* Tue Mar  6 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.13-3
- Rebuild.

* Mon Feb 20 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.13-2
- Rebuild.

* Mon Feb  6 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.13-1
- Update to 1.7.13.

* Mon Jan 16 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.12-1
- Update to 1.7.12.

* Sun Jan 15 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.11-4
- Fix build with VDR 1.7.23.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec  4 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.7.11-1
- Update to 1.7.11.

* Sun Nov  6 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.7.10-1
- Update to 1.7.10.
- Clean up specfile constructs no longer needed with Fedora or EL6+.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep  3 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.6.7-4
- Filter out autoprovided libvdr-*.so.* (if %%filter_setup is available).

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.6.7-3
- Use ISA qualified dependency to vdr(abi).
- Use %%global instead of %%define.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 21 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.6.7-1
- Update to 1.6.7.
- Trim pre-1.6.0 %%changelog entries.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan  7 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.6.6-1
- 1.6.6.

* Wed Dec 17 2008 Ville Skyttä <ville.skytta@iki.fi> - 1.6.5-1
- 1.6.5.

* Sun Nov 30 2008 Ville Skyttä <ville.skytta@iki.fi> - 1.6.4-1
- 1.6.4.

* Mon Nov 10 2008 Ville Skyttä <ville.skytta@iki.fi> - 1.6.3-1
- 1.6.3.

* Tue Oct 14 2008 Ville Skyttä <ville.skytta@iki.fi> - 1.6.2-1
- 1.6.2.

* Sun Jun 22 2008 Ville Skyttä <ville.skytta@iki.fi> - 1.6.1-1
- 1.6.1.

* Mon Apr  7 2008 Ville Skyttä <ville.skytta@iki.fi> - 1.6.0-1
- 1.6.0.
- Build for VDR 1.6.0.
