%global pname     screenshot

Name:             vdr-%{pname}
Version:          0.0.16
Release:          18%{?dist}
Summary:          VDR plugin: Takes screenshots
License:          GPL+
URL:              https://github.com/jowi24/vdr-screenshot
Source:           %{name}-%{version}.tar.gz
# https://www.linuxtv.org/pipermail/vdr/2017-June/029280.html
Patch0:           %{pname}.fullhd.patch

BuildRequires:    gcc-c++
BuildRequires:    vdr-devel >= 1.6.0-41
Requires:         vdr(abi)%{?_isa} = %{vdr_apiversion}


%description
With this plugin you can take still images of your screen. After installing
the plugin, a new mainmenu entry "Screenshot" will show up. Each time you
select this item, a file /var/cache/vdr/screenshot/title-yyyymmdd-hhmmss.jpg
will be created, where title is the current transmission or the recording
currently replayed.

%prep
%autosetup -n %{name}-%{version}
chmod -c -x screenshot.c
# For older VDR versions <=1.7.34
cp Makefile.pre.1.7.34 Makefile

iconv -f iso-8859-1 -t utf-8 HISTORY > HISTORY.utf8 ; mv HISTORY.utf8 HISTORY

%build
make %{?_smp_mflags} AUTOCONFIG= LIBDIR=. LOCALEDIR=./locale \
    VDRDIR=%{_libdir}/vdr all

%install
install -dm 755 $RPM_BUILD_ROOT%{vdr_plugindir}
install -dm 755 $RPM_BUILD_ROOT%{vdr_cachedir}/screenshot
install -pm 755 libvdr-*.so.%{vdr_apiversion} $RPM_BUILD_ROOT%{vdr_plugindir}

# Locale
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/locale
cp -pR locale/* $RPM_BUILD_ROOT%{_datadir}/locale
%find_lang %{name}

%files -f %{name}.lang
%doc HISTORY README
%license COPYING
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}
%attr(-,%{vdr_user},root) %dir %{vdr_cachedir}/screenshot/

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.16-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.16-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.0.16-16
- Rebuilt for new VDR API version

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.16-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.0.16-14
- Add BR gcc-c++

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.16-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 18 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.0.16-12
- Rebuilt for vdr-2.4.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.0.16-8
- Add screenshot.fullhd.patch
- Dropped %%{pname}.patch

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Mar 27 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.0.16-6
- Rebuilt for rawhide

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.0.16-3
- Rebuilt for GCC 5 C++11 ABI change

* Mon Apr 06 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.0.16-2
- Rebuild (vdr)

* Fri Feb 27 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.0.16-1
- rebuild for new release 0.0.16
- cleanup spec file
- mark license files as %%license where available

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.15-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.0.15-9
- Rebuild

* Sun Mar 23 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.0.15-8
- Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 31 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.0.15-6
- Rebuild.

* Sat Mar 16 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.0.15-5
- Rebuild.

* Wed Mar 13 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.0.15-4
- Rebuild.

* Sun Mar 03 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.0.15-3
- Rebuild.

* Mon Feb 18 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.0.15-2
- Rebuild.

* Sat Feb 16 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.0.15-1
- rebuild for new release

* Tue Oct 02 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.0.14-8
- Rebuild.

* Thu Sep 13 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.0.14-7
- Rebuild.

* Thu Jul 19 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.0.14-6
- Rebuild.

* Wed Jun 27 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.0.14-5
- Rebuild.

* Mon May 21 2012 Martin Gansser <linux4martin@gmx.de> 0.0.14-4.fc17
- fixed spurious-executable-perm of screenshot.c 

* Tue May 15 2012 Martin Gansser <linux4martin@gmx.de> 0.0.14-3.fc17
- picture-path and readme patch are merged
- more permission cleanups

* Tue May 15 2012 Martin Gansser <linux4martin@gmx.de> 0.0.14-2.fc17
- added Translation Content-Type charset fixes
- added readme patch
- fixed correct permissons for vdr_cachedir

* Sun May 13 2012 Martin Gansser <linux4martin@gmx.de> 0.0.14-1.fc17
- new release

* Sat May 12 2012 Martin Gansser <linux4martin@gmx.de> 0.0.13-3.fc17
- fixed dependencies
- removed strip command and comments out debug_package in rpmmacros
- added patch to store images in /var/cache/vdr/screenshot

* Tue May 08 2012 Martin Gansser <linux4martin@gmx.de> 0.0.13-2.fc17
- solved unstripped-binary-or-object warning and mixed-use-of-spaces-and-tabs
- removed unneeded global definitions

* Mon Apr 30 2012 Martin Gansser <linux4martin@gmx.de> 0.0.13-1.fc17
- initial release for fc17

