Name:           heimdall
Version:        1.4.2
Release:        9%{?dist}
Summary:        Flash firmware on to Samsung Galaxy S devices
License:        MIT
URL:            http://glassechidna.com.au/heimdall/
Source0:        https://github.com/Benjamin-Dobell/Heimdall/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source2:        %{name}.desktop
Patch0:         heimdall-1.4.2-support_files_bigger_than_3.5gb.patch

BuildRequires:  cmake
BuildRequires:  qt5-devel
BuildRequires:  libusb1-devel >= 1.0.8
BuildRequires:  zlib-devel
BuildRequires:  desktop-file-utils

%description
Heimdall is a cross-platform open-source utility to flash firmware
on to Samsung Galaxy S devices

%package frontend
Summary:        Qt4 based frontend for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description frontend
Heimdall is a cross-platform open-source utility to flash firmware
on to Samsung Galaxy S devices

This package provides Qt5 based frontend for %{name}

%prep
%autosetup -p1 -n Heimdall-%{version}

#remove unneeded files
rm -rf Win32
rm -rf OSX

%build
%{cmake} .
%{make_build}

%install
install -D -m 0755 bin/heimdall %{buildroot}%{_bindir}/heimdall
install -D -m 0755 bin/heimdall-frontend %{buildroot}%{_bindir}/heimdall-frontend
install -D -m 0644 heimdall/60-heimdall.rules %{buildroot}%{_udevrulesdir}/60-heimdall.rules
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE2}

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!--
EmailAddress: contact@glassechidna.com.au
SentUpstream: 2014-09-18
-->
<application>
 <id type="desktop">heimdall.desktop</id>
 <metadata_license>CC0-1.0</metadata_license>
 <project_license>MIT</project_license>
 <name>Heimdall</name>
 <summary>Flash firmware onto Samsung mobile devices</summary>
 <description>
  <p>
   Heimdall is a cross-platform open-source tool suite used to flash
   firmware (aka ROMs) onto Samsung mobile devices.
  </p>
 </description>
 <screenshots>
  <screenshot type="default" width="1275" height="718">http://jorti.fedorapeople.org/appdata/heimdall.png</screenshot>
 </screenshots>
 <url type="homepage">http://glassechidna.com.au/heimdall/</url>
 <url type="donation">http://glassechidna.com.au/donate</url>
 <updatecontact>jorti@fedoraproject.org</updatecontact>
</application>
EOF

%files
%doc Linux/README
%license LICENSE
%{_bindir}/%{name}
%{_udevrulesdir}/60-heimdall.rules

%files frontend
%{_bindir}/%{name}-frontend
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.4.2-6
- Add patch to support files bigger than 3.5 GB

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.4.2-1
- Version 1.4.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.4.1-9
- Add donation URL to AppData file

* Wed Feb 24 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.4.1-8
- Add keywords to desktop file

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.4.1-6
- use %%qmake_qt4 macro to ensure proper build flags

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 09 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.4.1-4
- Use license macro

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.4.1-3
- Add an AppData file for the software center

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 29 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.4.1-1
- Update to version 1.4.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 11 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.4.0-1
- Update to version 1.4.0
- Add zlib-devel BuildRequires and explicit version to qt-devel
- Update udev rules dir patch

* Mon Feb 25 2013 Juan Orti Alcaine <j.orti.alcaine@gmail.com> - 1.4-0.3.rc2
- Add _udevrulesdir for f17

* Mon Feb 25 2013 Juan Orti Alcaine <j.orti.alcaine@gmail.com> - 1.4-0.2.rc2
- Change BuildRequires to libusb1-devel

* Fri Feb 22 2013 Juan Orti Alcaine <j.orti.alcaine@gmail.com> - 1.4-0.1.rc2
- Bump version to 1.4rc2
- Use _udevrulesdir macro and add patch to modify udev rules dir in Makefile
- Patch to avoid udev service restart is no longer necessary
- Change dependency to libusbx
- Change group of heimdall-frontend

* Tue Oct 30 2012 Juan Orti Alcaine <j.orti.alcaine@gmail.com> - 1.3.2-3
- Don't use autogen.sh
- Improve heimdall-remove-udev-service-restart.patch
- Remove unneeded files

* Tue Oct 30 2012 Juan Orti Alcaine <j.orti.alcaine@gmail.com> - 1.3.2-2
- Remove dos2unix dependency

* Sun Oct 28 2012 Juan Orti Alcaine <j.orti.alcaine@gmail.com> - 1.3.2-1
- Bump version to 1.3.2
- Add missing dependencies
- Spec file clean up

* Tue Sep 18 2012 Eduardo Echeverria  <echevemaster@gmail.com> - 1.3.1-1
- Initial packaging
