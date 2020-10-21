## This macro activates/deactivates debug option
%bcond_with debug
%global pname   osd2web
%global rname   vdr-plugin-osd2web
%global __provides_exclude_from ^%{vdr_plugindir}/.*\\.so.*$

Name:           vdr-%{pname}
Version:        0.2.54
Release:        1%{?dist}
Summary:        VDR skin interface for the browser
License:        GPLv2+
URL:            https://github.com/horchi/vdr-plugin-osd2web
Source0:        https://github.com/horchi/vdr-plugin-osd2web/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         vdr-osd2web-makefile.patch
Source1:        %{name}.conf

BuildRequires:  gcc-c++
BuildRequires:  vdr-devel >= 2.2.0
BuildRequires:  libwebsockets-devel
BuildRequires:  zlib-devel
BuildRequires:  tinyxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  jansson-devel
BuildRequires:  libexif-devel
BuildRequires:  libuuid-devel
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description
osd2web is a VDR skin interface for the browser, which displays the OSD
and allows all interactions which are possible on the OSD.

%prep
%autosetup -n %{rname}-%{version}

## Optimization flags in 'Make.config' file
sed -i \
    -e 's|PREFIX   = /usr/local|PREFIX   =  %{_prefix}|' \
    -e 's|CXXFLAGS += -O3|CXXFLAGS += %{optflags}|' \
    -e 's|@@OPTFLAGS | %{optflags}|' \
    Make.config

%if %{without debug}
sed -i -e 's|DEBUG = 1||' Make.config
%endif

%build
%make_build

%install
%make_install

install -Dpm 644 %{SOURCE1} \
  %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/%{name}.conf

# fix the perm due W: unstripped-binary-or-object
chmod 0755 %{buildroot}/%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}

# install executable to %%{vdr_plugindir} due E: executable-marked-as-config-file
rm -rf %{buildroot}/%{vdr_configdir}/plugins/osd2web/startBrowser.sh
install -Dpm 755 scripts/startBrowser.sh %{buildroot}%{vdr_plugindir}/bin/startBrowser.sh

%find_lang %{name}

%files -f %{name}.lang
%license LICENSE COPYING
%doc README
%dir %{vdr_configdir}/plugins/osd2web/
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{name}.conf
%{vdr_plugindir}/libvdr-%{pname}.so.%{vdr_apiversion}
%config(noreplace) %{vdr_configdir}/plugins/osd2web/*
%{vdr_plugindir}/bin/startBrowser.sh

%changelog
* Sun Sep 13 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.2.54-1
- Rebuilt for new libwebsockets
- Update to 0.2.54

* Sun Aug 02 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.2.52-1
- Update to 0.2.52
- Rebuilt for new VDR API version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 12 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.2.50-1
- Update to 0.2.50
- Rebuilt due an SONAME bump of libwebsockets to 4.0.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.49-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 19 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.2.49-4
- Rebuilt for new libwebsocket version 

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 22 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.2.49-2
- Rebuilt for new VDR API version

* Fri May 31 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.2.49-1
- Update to 0.2.49

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.48-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 20 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.2.48-3
- Rebuilt for new libwebsockets

* Fri Nov 09 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.2.48-2
- Use %%{version} for SOURCE tag
- Use %%bcond_with/without for debugging flag
- Mark COPYING as %%license file
- Use korrekt license GPLv2+
- take ownership of unowned directory %%{vdr_configdir}/plugins/osd2web/

* Wed Nov 07 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.2.48-1
- Initial build
