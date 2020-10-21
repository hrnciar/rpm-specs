Name:           radiotray-ng
Version:        0.2.7
Release:        7%{?dist}
Summary:        Internet radio player

License:        GPLv3+
URL:            https://github.com/ebruck/radiotray-ng
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake3
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  boost-devel
BuildRequires:  wxGTK3-devel
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(libxdg-basedir)
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme

%description
%{summary}.

%prep
%autosetup
# Correct build flags
sed -i 's|-Wall -Wextra -Werror -Wpedantic|%{optflags}|' CMakeLists.txt
sed -i '/execute_process(COMMAND lsb_release/d' package/CMakeLists.txt


%build
%cmake3 \
    -DLSB_RELEASE_EXECUTABLE="lsb_release" \
    -DDISTRIBUTOR_ID="fedora"
%cmake_build


%install
%cmake_install
# Remove autostart
rm %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop
# Remove themes
rm -rf %{buildroot}%{_datadir}/icons/Yaru
rm -rf %{buildroot}%{_datadir}/icons/breeze
# Remove self-installed license file
rm %{buildroot}%{_datadir}/licences/%{name}/COPYING
#Remove unneeded script
rm %{buildroot}%{_bindir}/rt2rtng

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/rtng-bookmark-editor.desktop


%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/%{name}
%{_bindir}/rtng-bookmark-editor
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/rtng-bookmark-editor.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/%{name}


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 31 2020 Björn Esser <besser82@fedoraproject.org> - 0.2.7-6
- Rebuilt again for Boost 1.73

* Sat May 30 2020 Björn Esser <besser82@fedoraproject.org> - 0.2.7-5
- Rebuild (jsoncpp)

* Sat May 30 2020 Jonathan Wakely <jwakely@redhat.com> - 0.2.7-4
- Rebuilt for Boost 1.73

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Björn Esser <besser82@fedoraproject.org> - 0.2.7-2
- Rebuild (jsoncpp)

* Mon Oct 21 2019 Vasiliy Glazov <vascom2@gmail.com> 0.2.7-1
- Update to 0.2.7.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Vasiliy Glazov <vascom2@gmail.com> 0.2.6-2
- Use pkgconfig for BR
- Update source url

* Fri Jul 05 2019 Vasiliy Glazov <vascom2@gmail.com> 0.2.6-1
- Initial release
