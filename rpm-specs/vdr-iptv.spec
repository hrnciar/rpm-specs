Name:           vdr-iptv
Version:        2.4.0
Release:        7%{?dist}
Summary:        IPTV plugin for VDR

License:        GPLv2+
URL:            http://www.saunalahti.fi/rahrenbe/vdr/iptv/
Source0:        http://www.saunalahti.fi/rahrenbe/vdr/iptv/files/%{name}-%{version}.tgz

BuildRequires:  gcc-c++
BuildRequires:  vdr-devel >= 2.4.0
BuildRequires:  gettext
BuildRequires:  libcurl-devel
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description
This plugin integrates multicast IPTV transport streams seamlessly into
VDR. You can use any IPTV channel like any other normal DVB channel for
live viewing, recording, etc. The plugin also features full section
filtering capabilities which allow for example EIT information to be
extracted from the incoming stream.

%prep
%setup -q -n iptv-%{version}

# Fix paths in plugin scripts as defined by Fedora
sed -i "s|^CHANNELS_CONF=.*|CHANNELS_CONF=%{vdr_configdir}/channels.conf|; \
        s|^CHANNEL_SETTINGS_DIR=.*/iptv|CHANNEL_SETTINGS_DIR=%{vdr_configdir}/plugins/%{vdr_plugin}|" \
        iptv/vlc2iptv

%build
make CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" STRIP=: %{?_smp_mflags} all

%install
make install DESTDIR=%{buildroot}

%find_lang %{name}

%files -f %{name}.lang
%doc HISTORY README
%license COPYING
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}
%dir %{vdr_configdir}/plugins/iptv
%config(noreplace) %{vdr_resdir}/plugins/iptv/*.sh
%config(noreplace) %{vdr_resdir}/plugins/iptv/vlc2iptv

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

* Wed Apr 18 2018 Martin Gansser <martinkg@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 07 2016 Martin Gansser <martinkg@fedoraproject.org> - 2.2.1-5
- Patch to fix build with -std=c++11

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Apr 06 2015 Martin Gansser <martinkg@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1
- Mark license files as %%license where available

* Thu Feb 19 2015 Ville Skyttä <ville.skytta@iki.fi> - 2.0.2-12
- Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Ville Skyttä <ville.skytta@iki.fi> - 2.0.2-9
- Rebuild

* Sun Mar 23 2014 Ville Skyttä <ville.skytta@iki.fi> - 2.0.2-8
- Rebuild

* Sat Feb 15 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.0.2-7
- added STRIP to get a usefull debuginfo package

* Wed Feb 12 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.0.2-6
- added %%dir for %%{vdr_configdir}/plugins/iptv

* Wed Feb 12 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.0.2-5
- added noreplace to prevent config files to be overwritten

* Mon Feb 03 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.0.2-4
- replaced gettext-devel by gettext in BuildRequires
- dropped iptv.conf file

* Mon Feb 03 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.0.2-3
- added compiler flags in build section
- fixed paths in plugin scripts for channels.conf

* Tue Jan 21 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.0.2-2
- corrected discription in vdr-iptv.conf file

* Mon Jan 20 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.0.2-1
- Initial build

