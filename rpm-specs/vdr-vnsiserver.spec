%global plugin_name     vnsiserver

Name:           vdr-vnsiserver
Version:        1.8.0
Release:        1%{?dist}
Summary:        VDR plugin to handle Kodi clients via VNSI
License:        GPLv2+
URL:            https://github.com/FernetMenta/vdr-plugin-vnsiserver

Source:         https://github.com/FernetMenta/vdr-plugin-vnsiserver/archive/v%{version}.tar.gz

Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}
Conflicts:      vdr-vnsiserver3
BuildRequires:  gcc-c++
BuildRequires:  vdr-devel >= 1.5.9

%description
VDR plugin to handle Kodi (formerly known as XBMC) clients.
It is needed to use Kodi as a frontend and VDR as a backend.
With the plugin it is possible to get TV and PVR
functionality from a VDR into Kodi. It is able to handle several Kodi
clients connecting via the VNSI add-on.

In Kodi you need the PVR add-on "kodi-pvr-vdr-vnsi" to connect Kodi
with a VDR running this plugin.

See http://kodi.wiki/view/VDR for more information.

%prep
%setup -q -n vdr-plugin-vnsiserver-%{version}

%build
make %{?_smp_mflags} CFLAGS="-fPIC %optflags" CXXFLAGS="-fPIC %{optflags}"

%install
%make_install
install -dm 755 %{buildroot}%{vdr_configdir}/plugins/%{plugin_name}
install -Dpm 644 %{plugin_name}/* %{buildroot}%{vdr_configdir}/plugins/%{plugin_name}/
%find_lang %{name}

%files -f %{name}.lang
%doc COPYING 
%doc HISTORY
%doc README

%dir %{vdr_configdir}/plugins/%{plugin_name}
%config(noreplace) %{vdr_configdir}/plugins/%{plugin_name}/*
%{vdr_plugindir}/libvdr-%{plugin_name}.so.%{vdr_apiversion}

%changelog
* Mon Feb 10 2020 Dr. Tilmann Bubeck <bubeck@fedoraproject.org> - 1.8.0-1
- update to v1.8.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 02 2018 Dr. Tilmann Bubeck <tilmann@bubecks.de> - 1.6.0-1
- Update to v1.6.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild


* Sun Jan 15 2017 Dr. Tilmann Bubeck <tilmann@bubecks.de> - 1.5.2-1
- Update to v1.5.2

* Tue Oct 04 2016 Dr. Tilmann Bubeck <tilmann@bubecks.de> - 1.5.1-1
- Update to v1.5.1

* Sat Aug 06 2016 Dr. Tilmann Bubeck <tilmann@bubecks.de> - 1.5.0-1
- Update to v1.5.0

* Sun Jun 12 2016 Dr. Tilmann Bubeck <tilmann@bubecks.de> - 1.3.1-3
- Make compatible with GCC 6
- resolves bz #1308223

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 04 2015 Dr. Tilmann Bubeck <tilmann@bubecks.de> - 1.3.1-1
- Update to 1.3.1

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Ville Skyttä <ville.skytta@iki.fi> - 1.2.0-2
- Rebuild

* Sun Sep 14 2014 Dr. Tilmann Bubeck <tilmann@bubecks.de> - 1.2.0-1
- Update to 1.2.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Dr. Tilmann Bubeck <tilmann@bubecks.de> - 1.1.0-3
- Changed package to use version tags instead of git hash

* Tue May 20 2014 Dr. Tilmann Bubeck <tilmann@bubecks.de> - 1.1.0-2
- Added "Conflicts" to spec file

* Mon May 19 2014 Dr. Tilmann Bubeck <tilmann@bubecks.de> - 1.1.0-1
- Update to upstreams version 1.1.0, which uses VNSI protocol in
  version 5 which is compatible with XBMC 13.
- initial built for Fedora

