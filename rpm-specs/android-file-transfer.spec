Name:           android-file-transfer
Version:        3.9
Release:        4%{?dist}
Summary:        Reliable Android MTP client with minimalist UI

License:        LGPLv2+
URL:            https://github.com/whoozle/android-file-transfer-linux
Source0:        %{url}/archive/v%{version}/%{name}-linux-%{version}.tar.gz

Requires:       hicolor-icon-theme
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(fuse)
BuildRequires:  readline-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
Android File Transfer for Linux — reliable MTP client with minimalist UI
similar to Android File Transfer for Mac.
Features:
- Simple Qt UI with progress dialogs.
- FUSE wrapper (If you'd prefer mounting your device), supporting partial
  read/writes, allowing instant access to your files.
- No file size limits.
- Automatically renames album cover to make it visible from media player.
- USB 'Zerocopy' support found in recent Linux kernel
- No extra dependencies (e.g. libptp/libmtp).
- Command line tool (aft-mtp-cli)

%prep
%autosetup -p1 -n %{name}-linux-%{version}


%build
%cmake . -GNinja
%ninja_build


%install
%ninja_install
find %{buildroot} -name '*.a' -delete
desktop-file-install                                       \
    --remove-category="System"                             \
    --remove-category="Filesystem"                         \
    --delete-original                                      \
    --dir=%{buildroot}%{_datadir}/applications             \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml


%files
%license LICENSE
%doc README.md FAQ.md
%{_bindir}/*
%{_datadir}/icons/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Marek Blaha <mblaha@redhat.com> - 3.9-2
- Rebuilt with Qt5

* Wed Jun 12 2019 Marek Blaha <mblaha@redhat.com> - 3.9-1
- New upstream release 3.9

* Mon May 20 2019 Marek Blaha <mblaha@redhat.com> - 3.8-1
- New upstream release 3.8

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.7-3
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Marek Blaha <mblaha@redhat.com> - 3.7-1
- New upstream release 3.7

* Thu Nov  8 2018 Marek Blaha <mblaha@redhat.com> - 3.6-1
- New upstream release 3.6

* Tue Jul  3 2018 Marek Blaha <mblaha@redhat.com> - 3.4-1
- Initial rpm release
