%global debug_package   %{nil}

Name:           WoeUSB
Version:        3.3.1
Release:        2%{?dist}
Summary:        Windows USB installation media creator
License:        GPLv3+
URL:            https://github.com/slacka/WoeUSB
Source0:        https://github.com/slacka/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    s390x

Requires:       grub2-pc-modules
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  wxGTK3-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gettext
BuildRequires:  desktop-file-utils

%description
A utility that enables you to create your own bootable Windows installation
USB storage device from an existing Windows Installation disc or disk image.

%prep
%autosetup

%build
# Replace the version placeholders
find . -type f -print0 | xargs -0 sed -i "s/@@WOEUSB_VERSION@@/%{version}/"
autoreconf -fiv
%configure
%make_build

%install
%make_install
sed -i '1!b;s/env bash/bash/' %{buildroot}%{_bindir}/woeusb
sed -i '1!b;s/env bash/bash/' %{buildroot}%{_datadir}/woeusb/data/listDvdDrive
sed -i '1!b;s/env bash/bash/' %{buildroot}%{_datadir}/woeusb/data/listUsb
# rpmgrill fails if the desktop icon is only in /usr/share/pixmaps (bug #1539633)
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
mv %{buildroot}%{_datadir}/pixmaps/woeusbgui-icon.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
desktop-file-validate %{buildroot}%{_datadir}/applications/woeusbgui.desktop


%files
%license COPYING
# CLI
%{_bindir}/woeusb
%{_mandir}/man1/woeusb.1.gz
# GUI
%{_mandir}/man1/woeusbgui.1.gz
%{_bindir}/woeusbgui
%{_datadir}/applications/woeusbgui.desktop
%{_datadir}/icons/hicolor/48x48/apps/woeusbgui-icon.png
%dir %{_datadir}/woeusb
%dir %{_datadir}/woeusb/data
%{_datadir}/woeusb/data/c501-logo.png
%{_datadir}/woeusb/data/icon.png
%{_datadir}/woeusb/data/listDvdDrive
%{_datadir}/woeusb/data/listUsb
%{_datadir}/woeusb/data/woeusb-logo.png
%dir %{_datadir}/woeusb/locale
%dir %{_datadir}/woeusb/locale/fr
%dir %{_datadir}/woeusb/locale/fr/LC_MESSAGES
%dir %{_datadir}/woeusb/locale/zh_TW
%dir %{_datadir}/woeusb/locale/zh_TW/LC_MESSAGES
%lang(fr) %{_datadir}/woeusb/locale/fr/LC_MESSAGES/woeusb.mo
%lang(fr) %{_datadir}/woeusb/locale/fr/LC_MESSAGES/wxstd.mo
%lang(zh) %{_datadir}/woeusb/locale/zh_TW/LC_MESSAGES/woeusb.mo


%changelog
* Mon Mar 16 2020 mprahl <mprahl@redhat.com> - 3.3.1-2
- Stop building for s390x due to RHBZ#1813540

* Tue Mar 10 2020 mprahl <mprahl@redhat.com> - 3.3.1-1
- new version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 mprahl <mprahl@redhat.com> - 3.3.0-2
- Apply a workaround for RHBZ#1783669

* Wed Oct 16 2019 mprahl <mprahl@redhat.com> - 3.3.0-1
- new version

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 26 2018 mprahl <mprahl@redhat.com> - 3.2.12-1
- new version

* Sat Sep 08 2018 mprahl <mprahl@redhat.com> - 3.2.2-1
- New version
- Add grub2-pc-modules as a requirement

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 mprahl <mprahl@redhat.com> - 3.2.1-1
- new version

* Mon Apr 2 2018 Matt Prahl <mprahl@redhat.com> - 3.1.5-2
* Address rpmgrill failures

* Mon Apr 2 2018 Matt Prahl <mprahl@redhat.com> - 3.1.5-1
- Update to v3.1.5

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 9 2017 Matt Prahl <mprahl@redhat.com> - 2.2.2-1
- Update to v2.2.2

* Wed Sep 20 2017 Matt Prahl <mprahl@redhat.com> - 2.1.3-1
- Initial release
