Name: kiwix-desktop
Version: 2.0.1
Release: 1%{?dist}

License: GPLv3+
Summary: Kiwix desktop application

URL: https://github.com/kiwix/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

Requires: hicolor-icon-theme
Requires: shared-mime-info
Requires: aria2%{?_isa}

BuildRequires: qt5-qtwebengine-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: qt5-qtbase-devel
BuildRequires: kiwix-lib-devel
BuildRequires: mustache-devel
BuildRequires: pugixml-devel
BuildRequires: zimlib-devel
BuildRequires: qt5-linguist
BuildRequires: gcc-c++
BuildRequires: aria2
BuildRequires: gcc

# Required qt5-qtwebengine is not available on some arches.
ExclusiveArch: %{qt5_qtwebengine_arches}

%description
The Kiwix-desktop is a view/manager of zim files for GNU/Linux
and Windows. You can download and view your zim files as you
which.

%prep
%autosetup -p1
sed -e "/static {/,+2d" -e "/git describe/c\DEFINES += GIT_VERSION='%{version}'" -e "s/shell date/shell date +\%G-\%m-\%d/g" -e "s@lupdate@%{_libdir}/qt5/bin/lupdate-qt5@g" -e "s@lrelease@%{_libdir}/qt5/bin/lrelease-qt5@g" -i %{name}.pro
mkdir -p %{_target_platform}

%build
pushd %{_target_platform}
    %qmake_qt5 PREFIX=%{_prefix} ..
popd

%make_build -C %{_target_platform}

%install
%make_install INSTALL_ROOT=%{buildroot} -C %{_target_platform}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc ChangeLog README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/*.xml
%{_metainfodir}/*.appdata.xml

%changelog
* Sun May 10 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0.1-1
- Updated to version 2.0.1.

* Thu Apr 09 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0-1
- Updated to version 2.0.

* Mon Feb 10 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0-0.7.rc4
- Updated to version 2.0 RC4.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.6.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 13 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0-0.5.rc3
- Updated to version 2.0 RC3.

* Sat Aug 17 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0-0.4.rc1
- Updated to version 2.0 RC1.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.3.beta5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0-0.2.beta5
- Added aria2 to dependencies.

* Tue Jun 04 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0-0.1.beta5
- Initial SPEC release.
