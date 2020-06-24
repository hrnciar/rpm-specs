# https://github.com/andrew-bibb/cmst/commit/7778754988c3b68b3cfa757c45ed2e44dbe35dd8
%global commit0 7778754988c3b68b3cfa757c45ed2e44dbe35dd8
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           cmst
Version:        2020.05.09
#Release:        3.git%%{shortcommit0}%%{?dist}
Release:        1%{?dist}
Summary:        A Qt based GUI front end for the connman connection manager with systemtray icon

License:        MIT
URL:            https://github.com/andrew-bibb/cmst
#Source0:        https://github.com/andrew-bibb/cmst/archive/%%{commit0}/%%{name}-%%{commit0}.tar.gz#/%%{name}-%%{shortcommit0}.tar.gz
Source0:        https://github.com/andrew-bibb/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.service

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-linguist
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:    systemd-units
Requires(pre):    shadow-utils
Requires(post):   systemd-units
Requires(preun):  systemd-units
Requires(postun): systemd-units

Requires:       connman
Requires:       hicolor-icon-theme

%description
Qt GUI for Connman with system tray icon. The program provides graphical user
interface to control the connman daemon. The connman daemon must be started as
you normally would, this program just interfaces with that daemon.
You can see what technologies and services connman has found, and for wifi
services an agent is registered to assist in obtaining the information from
you necessary to logon the wifi service.

%prep
#%%autosetup -n %%{name}-%%{commit0}
%autosetup -n %{name}-%{version}

sed -i -e 's|Categories=Settings;System;Qt;Network;|Categories=Network;|g' misc/desktop/cmst.desktop
sed -i -e 's|CMST_LIB_PATH = "/usr/lib/cmst"|CMST_LIB_PATH = "%{_libexecdir}/%{name}"|g' cmst.pri

# change permission due rpmlint W: spurious-executable-perm
find . -type f  \( -name "*.cpp" -o -name "*.h" \) -exec chmod a-x {} \;

%build
# Create translation files.
lrelease-qt5 translations/*.ts

%{qmake_qt5}
%make_build

%install
make install INSTALL_ROOT=%{buildroot}
install -d -m 0755 %{buildroot}%{_datadir}/%{name}/languages
install -m 0644 translations/*.qm \
         %{buildroot}%{_datadir}/%{name}/languages

# Systemd unit files
# copy cmst.service to unitdir /lib/systemd/system
mkdir -p %{buildroot}%{_unitdir}
install -Dpm 644 %{SOURCE1} %{buildroot}/%{_unitdir}/%{name}.service

mkdir -p %{buildroot}%{_datadir}/appdata
mv %{buildroot}%{_datadir}/metainfo/org.cmst.cmst.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml


%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.appdata.xml

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files -f %{name}.lang
%doc README.md
%license text/LICENSE
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.cmst.roothelper.conf
%{_unitdir}/%{name}.service
%{_libexecdir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/system-services/org.cmst.roothelper.service
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/autostart/%{name}-autostart.desktop
%{_mandir}/man1/*

%changelog
* Mon May 11 2020 Martin Gansser <martinkg@fedoraproject.org> - 2020.05.09-1
- Update to 2020.05.09-1

* Mon Apr 13 2020 Martin Gansser <martinkg@fedoraproject.org> - 2020.04.12-1
- Update to 2020.04.12-1

* Sun Mar 08 2020 Martin Gansser <martinkg@fedoraproject.org> - 2020.03.07-1
- Update to 2020.03.07-1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.01.13-3.git7778754
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.01.13-2.git7778754
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 27 2019 Martin Gansser <martinkg@fedoraproject.org> - 2019.01.13-1.git7778754
- Update to 2019.01.13-1.git7778754

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.01.06-3.gitd6ee8f8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.01.06-2.gitd6ee8f8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Martin Gansser <martinkg@fedoraproject.org> - 2018.01.06-1.gitd6ee8f8
- Update to 2018.01.06-1.gitd6ee8f8

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2017.09.01-4.gitdc8c83b
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.09.01-3.gitdc8c83b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2017.09.01-2.gitdc8c83b
- Remove obsolete scriptlets

* Wed Sep 20 2017 Martin Gansser <martinkg@fedoraproject.org> - 2017.09.01-1.gitdc8c83b
- Update to 2017.09.01-1.gitdc8c83b

* Tue Aug 15 2017 Martin Gansser <martinkg@fedoraproject.org> - 2017.08.04-1.git0b13591
- Update to 2017.08.04-1.git0b13591

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.03.18-3.git606da1f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.03.18-2.git606da1f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 Martin Gansser <martinkg@fedoraproject.org> - 2017.03.18-1.git606da1f
- Update to 2017.03.18-1.git606da1f
- Drop %%{name}-build.patch

* Thu Mar 02 2017 Martin Gansser <martinkg@fedoraproject.org> - 2017.02.23-1.git5be4ce6
- Update to 2017.02.23-1.git5be4ce6
- Add %%{name}-build.patch

* Tue Oct 04 2016 Martin Gansser <martinkg@fedoraproject.org> - 2016.10.03-1.gitf85b216
- Update to 2016.10.03-1.gitf85b216

* Mon Oct 03 2016 Martin Gansser <martinkg@fedoraproject.org> - 2016.10.02-1.git35ebb4b
- Update to 2016.10.02-1.git35ebb4b

* Sat Aug 27 2016 Martin Gansser <martinkg@fedoraproject.org> - 2016.08.11-1.git75a3f0b
- update to new git release

* Sat Mar 19 2016 Martin Gansser <martinkg@fedoraproject.org> - 2016.03.06-1.gitc3631b3
- rebuild for new git release

* Fri Feb 26 2016 Martin Gansser <martinkg@fedoraproject.org> - 2016.01.26-6.git660121a
- rebuild for new git release
- dropped %%{name}.appdata.xml file

* Thu Feb 25 2016 Martin Gansser <martinkg@fedoraproject.org> - 2016.01.26-5.git16ee823
- set correct file permisson
- take ownership of unowned directorys

* Thu Feb 25 2016 Martin Gansser <martinkg@fedoraproject.org> - 2016.01.26-4.git16ee823
- added BR qt5-linguist
- added BR libappstream-glib

* Wed Feb 24 2016 Martin Gansser <martinkg@fedoraproject.org> - 2016.01.26-3.git16ee823
- addedd cmst.appdata.xml file

* Wed Feb 24 2016 Martin Gansser <martinkg@fedoraproject.org> - 2016.01.26-2.git16ee823
- changed release tag
- removed owned files in files/sub-directories
- added %%find_lang macro to find .qm files

* Sat Jan 30 2016 Martin Gansser <martinkg@fedoraproject.org> - 2016.01.26-1.gitcfe10e5
- initial release
