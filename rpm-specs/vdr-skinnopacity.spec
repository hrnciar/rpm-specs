%global sname   skinnopacity

Name:           vdr-skinnopacity
Version:        1.1.3
Release:        23%{?dist}
Summary:        A highly customizable native true color skin for the Video Disc Recorder

License:        GPLv2+
URL:            http://projects.vdr-developer.org/projects/skin-nopacity
Source0:        http://projects.vdr-developer.org/attachments/download/1743/%{name}-%{version}.tgz
# informed upstream to put copyright and licensing details in source files
# http://projects.vdr-developer.org/issues/1679
# Configuration files for plugin parameters. These are Fedora specific and not in upstream.
Source1:        %{name}.conf
# https://www.vdr-portal.de/index.php?attachment/41902-skinnopacity-locking-diff-gz/
Patch0:         skinnopacity-locking.diff.gz
BuildRequires:  gcc-c++
BuildRequires:  freetype-devel
BuildRequires:  ImageMagick-c++-devel
BuildRequires:  vdr-devel >= 1.7.34
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}
Requires:       %{name}-data = %{version}-%{release}

%description 
The VDR plugin "nOpacity" is a highly customizable native true color skin
for the Video Disc Recorder.

%package data
Summary:       Icons files for %{name}
BuildArch:     noarch
Requires:      %{name} = %{version}-%{release}

%description data
This package contains icons files.
 
%prep
%autosetup -n skinnopacity-%{version}
iconv -f iso-8859-1 -t utf-8 README > README.utf8 ; mv README.utf8 README
sed -i -e 's|std::auto_ptr|std::unique_ptr|' services/epgsearch.h

%build
make CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" IMAGELIB=imagemagick %{?_smp_mflags} all

%install
# make install would install the themes under /etc, let's not use that
make install-lib install-i18n install-icons DESTDIR=%{buildroot}
# install the themes to the custom location used in Fedora
install -dm 755 %{buildroot}%{vdr_vardir}/themes
# install -dm 755 %{buildroot}%{vdr_vardir}/plugins/skinnopacity/themeconfigs
install -dm 755 %{buildroot}%{_sysconfdir}/vdr/plugins/%{sname}/themeconfigs/
install -pm 644 themes/*.theme %{buildroot}%{vdr_vardir}/themes/
# install -pm 644 conf/theme-* %{buildroot}%{vdr_vardir}/plugins/skinnopacity/themeconfigs/
install -pm 644 conf/theme-* %{buildroot}%{_sysconfdir}/vdr/plugins/%{sname}/themeconfigs/

# skinnopacity.conf
install -Dpm 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/skinnopacity.conf

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING HISTORY* README*
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/skinnopacity.conf
# %%config(noreplace) %%{vdr_vardir}/plugins/skinnopacity/themeconfigs/theme-*.conf
%config(noreplace) %{_sysconfdir}/vdr/plugins/%{sname}/themeconfigs/theme-*.conf
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}
%{vdr_vardir}/themes/nOpacity-*.theme


%files data
%{vdr_resdir}/plugins/skinnopacity/icons/

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 04 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.3-21
- Use Imagemagick due segfault with Graphicsmagick

* Tue Jun 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.3-20
- Rebuilt for new VDR API version

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.3-18
- Correct themeconfigs path

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 04 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.3-16
- Dropped vdr_2.4.0_compat.patch
- Add skinnopacity-locking.diff.gz

* Tue Apr 17 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.3-15
- Rebuilt for vdr-2.4.0
- Add vdr_2.4.0_compat.patch

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 04 2015 Rex Dieter <rdieter@fedoraproject.org> 1.1.3-9
- rebuild (GraphicsMagick)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.3-7
- Rebuilt for GCC 5 C++11 ABI change

* Mon Apr 06 2015 Ville Skyttä <ville.skytta@iki.fi> - 1.1.3-6
- Rebuild (vdr)

* Mon Mar 09 2015 Rex Dieter <rdieter@fedoraproject.org> 1.1.3-5
- rebuild (GraphicsMagick)

* Thu Feb 19 2015 Ville Skyttä <ville.skytta@iki.fi> - 1.1.3-4
- Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Martin Gansser <martinkg@fedoraproject.org> - 1.1.3-1
- Update to new upstream release 1.1.3

* Sun May 11 2014 Martin Gansser <martinkg@fedoraproject.org> - 1.1.2-1.20140427gitcd33c3d
- rebuild for new git release
- added CXXFLAGS and -fPIC build flag

* Wed Apr 16 2014 Martin Gansser <martinkg@fedoraproject.org> - 1.1.1-1
- Update to new upstream release 1.1.1

* Sun Feb 02 2014 Martin Gansser <martinkg@fedoraproject.org> - 1.0.4-2
- corrected source file download link
- rebuild

* Sat Feb 01 2014 Martin Gansser <martinkg@fedoraproject.org> - 1.0.4-1
- new release
- spec file cleanup
- changed to %%{buildroot} macro

* Mon Jan 20 2014 Martin Gansser <martinkg@fedoraproject.org> - 1.0.3-8.20131221git0b29805
- changed to %%{buildroot} macro

* Mon Jan 20 2014 Martin Gansser <martinkg@fedoraproject.org> - 1.0.3-7.20131221git0b29805
- removed requirement ImageMagick-c++-devel
- added requirement GraphicsMagick-c++-devel
- added IMAGELIB=graphicsmagick to build flag

* Fri Jan 17 2014 Martin Gansser <martinkg@fedoraproject.org> - 1.0.3-6.20131221git0b29805
- added vdr-skinnopacity-data as requirement
- corrected tarball download instructions

* Wed Jan 15 2014 Martin Gansser <martinkg@fedoraproject.org> - 1.0.3-5.20131221git0b29805
- removed macro in changelog
- corrected license type to GPLv2+
- installed themes and themeconfigs to the custom location used in Fedora
- added gitdate for fedora naming schema
- added tarball download instructions

* Tue Jan 14 2014 Martin Gansser <martinkg@fedoraproject.org> - 1.0.3-4.0b29805
- used %%make_install instead of make install DESTDIR...
- using buildroot for consistency

* Sun Jan 12 2014 Martin Gansser <martinkg@fedoraproject.org> - 1.0.3-3.0b29805
- removed additional icons install section

* Sat Jan 11 2014 Martin Gansser <martinkg@fedoraproject.org> - 1.0.3-2.0b29805
- added themes and themeconfigs file
- added compiler flags in build section
- removed additional localization install section
- corrected path to README in skinnopacity.conf

* Fri Jan 03 2014 Martin Gansser <martinkg@fedoraproject.org> - 1.0.3-1.0b29805
- rebuild for new release

* Sat Dec 07 2013 Martin Gansser <martinkg@fedoraproject.org> - 1.0.2pre1-1
- rebuild for new git

* Sun Dec 01 2013 Martin Gansser <martinkg@fedoraproject.org> - 1.0.1-1
- rebuild for new git

* Sun Oct 27 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.9.0-1
- rebuild for new git

* Sat Oct 05 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.1.4-1
- rebuild for new git

* Sun May 05 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.1.1-1
- rebuild for new git

* Mon Apr 08 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.1.0-2
- rebuild for new git

* Sun Mar 31 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.1.0-1
- Rebuild.

