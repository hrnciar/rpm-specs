Name:           zeal
Version:        0.6.1
Release:        5%{?dist}
Summary:        Offline documentation browser inspired by Dash

# the libqxt-sourced files are BSD licensed
License:        GPLv3+ and BSD
URL:            https://zealdocs.org/
Source0:        https://github.com/zealdocs/zeal/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake3
BuildRequires:  cmake(Qt5)
BuildRequires:  cmake(Qt5WebKit)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libarchive-devel
BuildRequires:  sqlite-devel
BuildRequires:  xcb-util-keysyms-devel
Requires:       hicolor-icon-theme

# libqxt deprecation notice, encouraging its downstreams to bundle
# the parts they need:
# https://bitbucket.org/libqxt/libqxt/wiki/Home
#
# zeal commit history for qxtglobalshortcut
# showing active maintenance
# https://github.com/zealdocs/zeal/commits/master/src/3rdparty/qxtglobalshortcut
#
# communication with upstream:
# https://github.com/zealdocs/zeal/issues/414
Provides:       bundled(libqxt) = 0.6.2

%description
Zeal is a simple offline documentation browser inspired by Dash.


%prep
%autosetup -p1

# Disable ads on the welcome page
# Ads will be removed in 0.7.x
sed -i 's/("disable_ad"), false/("disable_ad"), true/' src/libs/core/settings.cpp

%build
# turn off shared libs building:
# - it's only used from Zeal itself
# - build scripts not configured to install the lib
%cmake3 \
  -DBUILD_SHARED_LIBS:BOOL=OFF \
  .
%make_build


%install
%make_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.zealdocs.Zeal.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.zealdocs.Zeal.appdata.xml


%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/org.zealdocs.Zeal.desktop
%{_metainfodir}/org.zealdocs.Zeal.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 20 2019 Lumír Balhar <lbalhar@redhat.com> - 0.6.1-4
- Disable ads on the welcome page by default

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Lumír Balhar <lbalhar@redhat.com> - 0.6.1-2
- Specfile improved

* Wed Nov  7 2018 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.6.1-1
- Update to 0.6.1

* Fri Aug 24 2018 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 21 2018 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.5.0-3
- Fix missing dependency on libCore.so - don't build Zeal with shared libs flag

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-2
- Remove obsolete scriptlets

* Tue Jan 16 2018 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0
- Switch to cmake; upstream is deprecating qmake
- and its rule for detecting Qt >= 5.5.1 breaks on F28's Qt 5.10

* Mon Sep  4 2017 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 12 2016 Michel Alexandre Salim <michel@dellxps.localdomain> - 0.3.1-1
- Update to 0.3.1

* Sat Sep 24 2016 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Mon Feb 22 2016 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Michel Salim <salimma@fedoraproject.org> - 0.1.1-2
- Update license info, add bundled lib metadata

* Thu Sep 24 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.1.1-1
- Initial package
