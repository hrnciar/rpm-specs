%global pname     skinsoppalusikka
%global __provides_exclude_from ^%{vdr_plugindir}/.*\\.so.*$

Name:           vdr-%{pname}
Version:        2.4.0
Release:        4%{?dist}
Summary:        The "Soppalusikka" skin for VDR

License:        GPLv2+
URL:            http://www.saunalahti.fi/~rahrenbe/vdr/soppalusikka/
Source0:        http://www.saunalahti.fi/~rahrenbe/vdr/soppalusikka/files/%{name}-%{version}.tgz
Source1:        %{name}.conf

BuildRequires:  gcc-c++
BuildRequires:  vdr-devel >= 1.7.21 gettext
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}


%description
The "Soppalusikka" is a standalone skin providing the good old "ElchiAIO"
looks.

%prep
%setup -q -n %{pname}-%{version}


%build
make %{?_smp_mflags} STRIP=/bin/true

%install
rm -rf $RPM_BUILD_ROOT
# make install would install the themes under /etc, let's not use that
make install-lib install-i18n DESTDIR=$RPM_BUILD_ROOT
install -Dpm 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
# install the themes to the custom location used in Fedora
install -dm 755 $RPM_BUILD_ROOT%{vdr_vardir}/themes
install -pm 644 themes/*.theme $RPM_BUILD_ROOT%{vdr_vardir}/themes/

%find_lang %{name}



%files -f %{name}.lang
%doc COPYING HISTORY README
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%{vdr_plugindir}/libvdr-%{pname}.so.%{vdr_apiversion}
%{vdr_vardir}/themes/soppalusikka-*.theme


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 4 2018 Ville-Pekka Vainio <vpvainio AT iki.fi> - 2.4.0-1
- New upstream release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 14 2016 Ville-Pekka Vainio <vpvainio AT iki.fi> - 2.2.1-1
- New upstream release

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0.3-7
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Ville Skyttä <ville.skytta@iki.fi> - 2.0.3-6
- Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Ville Skyttä <ville.skytta@iki.fi> - 2.0.3-3
- Rebuild

* Sun Mar 23 2014 Ville Skyttä <ville.skytta@iki.fi> - 2.0.3-2
- Rebuild

* Sun Jan 26 2014 Ville-Pekka Vainio <vpvainio AT iki.fi> - 2.0.3-1
- New upstream release

* Sat Oct 26 2013 Ville-Pekka Vainio <vpvainio AT iki.fi> - 2.0.2-1
- New upstream release

* Fri Oct 18 2013 Ville-Pekka Vainio <vpvainio AT iki.fi> - 2.0.1-1
- New upstream release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Apr 13 2013  Ville-Pekka Vainio <vpvainio AT iki.fi> - 2.0.0-1
- New upstream release
- Update the spec for the new VDR and Soppalusikka versions

* Sun Mar 31 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.7.8-7
- Rebuild.

* Sat Mar 16 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.7.8-6
- Rebuild.

* Wed Mar 13 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.7.8-5
- Rebuild.

* Sun Mar 03 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.7.8-4
- Rebuild.

* Mon Feb 18 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.7.8-3
- Fix bogus dates in %%changelog.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 10 2012  Ville-Pekka Vainio <vpvainio AT iki.fi> - 1.7.8-1
- New upstream release

* Tue Oct 02 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.7-4
- Rebuild.

* Thu Sep 13 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.7-3
- Rebuild.

* Thu Jul 19 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.7-2
- Rebuild.

* Sun Jul 01 2012 Ville-Pekka Vainio <vpvainio AT iki.fi> - 1.7.7-1
- Update to 1.7.7 for VDR 1.7.28.

* Tue Mar 27 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.5-7
- Rebuild.

* Sun Mar 11 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.5-6
- Rebuild.

* Tue Mar 06 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.5-5
- Rebuild.

* Mon Feb 20 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.5-4
- Rebuild.

* Sun Jan 15 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.7.5-3
- Rebuild.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec  4 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.7.5-1
- Update to 1.7.5.

* Tue Nov 15 2011 Ville-Pekka Vainio <vpvainio AT iki.fi> 1.7.4-1
- Update to 1.7.4 for VDR 1.7
- Update the spec to use the new vdr packaging macros

* Sun Nov  6 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.6.5-3
- Rebuild.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 10 2010 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.6.5-1
- 1.6.5

* Sun Sep 06 2009 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.6.4-3
- Filter out autoprovided libvdr-*.so.* (if %%filter_setup is available).
- Use ISA qualified dependency to vdr(abi).
- Use %%global instead of %%define.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 14 2009 - Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> 1.6.4-1
- 1.6.4

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 30 2008 - Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> 1.6.3-1
- 1.6.3

* Mon Nov 24 2008 - Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> 1.6.2-2
- Rebuild for VDR 1.6.0-15.fc11

* Tue Oct 14 2008 - Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> 1.6.2-1
- 1.6.2
- HISTORY converted to UTF-8 by upstream, remove conversion from the spec file

* Wed Jun 25 2008 - Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> 1.6.1-1
- 1.6.1 including translation updates and a bugfix

* Tue Apr 08 2008 - Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> 1.6.0-1
- New version for VDR 1.6

* Sat Feb 16 2008 - Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> 1.0.6-2
- Rebuild for GCC 4.3

* Mon Jan 21 2008 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.0.6-1
- Upstream released a new version
- Change Source0 to be a complete URL of the source

* Tue Oct 16 2007 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.0.5-2
- License is actually GPLv2 _or later_, I missed that, fixed now.

* Fri Oct 12 2007 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.0.5-1
- Upstream released a new version
- Upstream changed license to GPLv2, see README
- Description updated to match new README
- Upstream removed channel logos, no need for the removal script anymore

* Thu Oct 11 2007 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.0.4-1
- s/soppalusikka/skinsoppalusikka/ in vdr-skinsoppalusikka.conf
- Bump release for the first Fedora build
- Try to hide my email from the spambots a bit

* Sun Oct 07 2007 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.0.4-0.4
- Remove the /var/lib/vdr/themes dir, it's owned by the vdr package.
- Change license tag from GPLv2 to GPL+.
- Remove datadir define, as it's not used.
- s/femon/skinsoppalusikka/ in vdr-skinsoppalusikka.conf

* Sun Oct 07 2007 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.0.4-0.3
- Remove channel logos, add vdr-skinsoppalusikka-prepare-tarball.sh for doing
  it automatically.

* Sun Oct 07 2007 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.0.4-0.2
- Remove the symbols, since they are compiled into the binary plugin. Thanks
  to Mandriva packager Anssi Hannula for the information.

* Sun Oct 07 2007 Ville-Pekka Vainio <vpivaini AT cs.helsinki.fi> - 1.0.4-0.1
- Initial package.
