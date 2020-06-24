%global commit          0907ef84678cf85d51ccf623d9c8f0972d3469e5
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global snapshotdate    20181013

Name:           qtwaifu2x
Version:        0
Release:        0.4.%{snapshotdate}git%{shortcommit}%{?dist}
Summary:        Frontend for waifu2x-converter-cpp

License:        GPLv2
URL:            https://github.com/cmdrkotori/qtwaifu2x
Source0:        %url/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        qtwaifu2x.desktop

BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  qt5-qtbase-devel
Requires:       hicolor-icon-theme
Requires:       waifu2x-converter-cpp

%description
Frontend for waifu2x-converter-cpp.


%prep
%autosetup -p1 -n %{name}-%{commit}


%build
%qmake_qt5
%make_build


%install
install -Dpm 0755 qtwaifu2x %{buildroot}%{_bindir}/qtwaifu2x
install -Dpm 0644 images/icon.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/qtwaifu2x.png

desktop-file-install                                        \
    --dir=%{buildroot}%{_datadir}/applications              \
    %{SOURCE1}



%files
%license LICENSE
%doc README.md
%{_bindir}/qtwaifu2x
%{_datadir}/applications/qtwaifu2x.desktop
%{_datadir}/icons/hicolor/512x512/apps/qtwaifu2x.png


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20181013git0907ef8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20181013git0907ef8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20181013git0907ef8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 13 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20181013git0907ef8
- Initial release
