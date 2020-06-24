Name:       utox
Version:    0.17.2
Release:    1%{?dist}
Summary:    The lightweight Tox client

License:    MIT or GPLv3+
URL:        https://github.com/uTox/uTox/
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:    %{name}.appdata.xml
# git clone https://github.com/uTox/uTox
# cd uTox
# git checkout v0.17.2
# git submodule init ; git submodule update
# tar -zcvf third-party.tar.gz third-party/
Source2:    third-party.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(filteraudio)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(toxcore)
Requires:       hicolor-icon-theme

%description
%summary

%prep
%autosetup -p 1 -n uTox-%{version}
%autosetup -N -T -D -a 2 -n uTox-%{version}

%build
mkdir build
cd build
%cmake ..
%make_build

%install
pushd build
%make_install
popd
install -Dp -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml
rm -rf %{buildroot}/%{_datadir}/icons/hicolor/14x14

%check
ctest -V %{?_smp_mflags}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Jun 19 12:40:14 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.17.2-1
- Update to 0.17.2 (#1823346)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 01:58:44 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.17.1-2
- Fix compatibility with GCC 10

* Wed Sep 25 16:55:23 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.17.1-1
- Release 0.17.1

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Björn Esser <besser82@fedoraproject.org> - 0.17.0-5
- rebuilt (libvpx)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.17.0-2
- Rebuilt for toxcore soname bump

* Thu Apr 19 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.17.0-1
- Upstream release 0.17.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 28 2018 Robert-André Mauchin <zebob.m@gmail.com> 0.16.1-5
- actually rebuild for new libvpx

* Fri Jan 26 2018 Tom Callaway <spot@fedoraproject.org> - 0.16.1-4
- rebuild for new libvpx

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.16.1-3
- Remove obsolete scriptlets

* Tue Oct 31 2017 Robert-André Mauchin <zebob.m@gmail.com> 0.16.1-2
- Clean-up the SPEC

* Thu Oct 12 2017 Robert-André Mauchin <zebob.m@gmail.com> 0.16.1-1
- New upstream release 0.16.1

* Fri Aug 18 2017 Robert-André Mauchin <zebob.m@gmail.com> 0.15.0-2
- Added appdata.xml
- Fixed Requires dependencies

* Sat Jul 29 2017 Robert-André Mauchin <zebob.m@gmail.com> 0.15.0-1
- First RPM release
