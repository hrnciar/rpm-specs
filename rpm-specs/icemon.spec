Name:           icemon
Version:        3.3
Release:        2%{?dist}
Summary:        Icecream GUI monitor

License:        GPLv2+
URL:            http://kfunk.org/tag/icemon/
Source0:        https://github.com/icecc/icemon/archive/v%{version}.tar.gz

BuildRequires:    gcc-c++
BuildRequires:    qt5-devel
BuildRequires:    pkgconfig(icecc) >= 1.3
BuildRequires:    docbook2X
BuildRequires:    cmake
BuildRequires:    libcap-ng-devel
BuildRequires:    lzo-devel
BuildRequires:    desktop-file-utils
BuildRequires:    docbook-dtds
BuildRequires:    extra-cmake-modules

Requires:    hicolor-icon-theme

%description
A GUI monitor for Icecream, a distributed compiler system

%prep
%autosetup -p1


%build
%cmake .
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
ctest -V %{?_smp_mflags}

%files
%{_bindir}/%{name}
%{_datadir}/applications/icemon.desktop
%{_datadir}/icons/hicolor/22x22/apps/icemon.png
%{_datadir}/icons/hicolor/16x16/apps/icemon.png
%{_datadir}/icons/hicolor/48x48/apps/icemon.png
%{_datadir}/icons/hicolor/128x128/apps/icemon.png
%{_datadir}/icons/hicolor/32x32/apps/icemon.png

%license COPYING
%doc %{_mandir}/man1/icemon.1.gz


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 27 2019 Michal Schmidt <mschmidt@redhat.com> - 3.3-1
- Updated to 3.3

* Fri Aug 02 2019 Michael Cullen <michael@cullen-online.com> - 3.2.0-1
- Updated to 3.2.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 2019 David Tardon <dtardon@redhat.com> - 3.1.0-9
- rebuild for icecream 1.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jul 30 2017 Michael Cullen <michael@cullen-online.com> - 3.1.0-5
- Removed useless BuildRequires on gzip
- Changed BuildRequires hicolor-icon-theme to be Requires since it is a runtime dependency
* Fri Jul 28 2017 Michael Cullen <michael@cullen-online.com> - 3.1.0-4
- Added BuildRequires on gcc-c++
* Fri Jul 28 2017 Michael Cullen <michael@cullen-online.com> - 3.1.0-3
- Decompressed SVG file to fix rpmlint warning
- Added BuildRequires on docbook-dtds to fix build error without network
- Changed license to GPLv2+ according to file headers
- Added calls to gtk-update-icon-cache
* Thu Jul 27 2017 Michael Cullen <michael@cullen-online.com> - 3.1.0-2
- Found a better description for spec file
* Thu Jul 27 2017 Michael Cullen <michael@cullen-online.com> - 3.1.0-1
- Initial Packaging

