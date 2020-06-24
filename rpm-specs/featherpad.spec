# For release builds set to 1, for snapshots set to 0
%global relbuild 1 

%if !0%{?relbuild}
%global commit 73252293ca720d7783372b477f34ca9fad0ad8f6
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20170401
%global git_ver -git%{gitdate}.%{shortcommit}
%global git_rel .git%{gitdate}.%{shortcommit}
%endif # !0%%{?relbuild}

%global github_name FeatherPad

Name:           featherpad
Version:        0.9.3
Release:        3%{?dist}
Summary:        Lightweight Qt5 Plain-Text Editor

License:        GPLv3+
URL:            https://github.com/tsujan/%{github_name}
%if 0%{?relbuild}
Source0:        %{url}/archive/V%{version}.tar.gz#/%{github_name}-%{version}.tar.gz
%else  # 0%%{?relbuild}
Source0:        %{url}/archive/%{commit}.tar.gz#/%{github_name}-%{version}%{?git_ver}.tar.gz
%endif # 0%%{?relbuild}

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtx11extras-devel

Requires:       hicolor-icon-theme

%description
FeatherPad is a lightweight Qt5 plain-text editor for Linux. It is independent
of any desktop environment and has:

* Drag-and-drop support, including tab detachment and attachment;
* X11 virtual desktop awareness (using tabs on current desktop but opening a 
  new window on another);
* An optionally permanent search-bar with a different search entry 
  for each tab;
* Instant highlighting of found matches when searching;
* A docked window for text replacement;
* Support for showing line numbers and jumping to a specific line;
* Automatic detection of text encoding as far as possible and optional saving
  with encoding;
* Syntax highlighting for common programming languages;
* Printing;
* Text zooming;
* Appropriate but non-interrupting prompts;


%prep
%if 0%{?relbuild}
%autosetup -n %{github_name}-%{version} -p 1
%else  # 0%%{?relbuild}
%autosetup -n %{github_name}-%{commit} -p 1
%endif # 0%%{?relbuild}

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{qmake_qt5} ..
%make_build
popd


%install
make install INSTALL_ROOT=%{buildroot} -C %{_target_platform}
%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop



%files -f %{name}.lang
%license COPYING
%doc ChangeLog INSTALL NEWS README.md
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/help
%{_datadir}/%{name}/help_ja_JP
%dir %{_datadir}/%{name}/translations


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 15 2019 Zamir SUN <sztsian@gmail.com> - 0.9.3-1
- Update to 0.9.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 10 2018 Christian Dersch <lupinix@mailbox.org> - 0.9.0-1
- new version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.1-2
- Remove obsolete scriptlets

* Fri Oct 20 2017 Christian Dersch <lupinix@mailbox.org> - 0.6.1-1
- new version

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat May  6 2017 Christian Dersch <lupinix@mailbox.org> 0.6-1
- new version (0.6 release)

* Sun Apr  9 2017 Christian Dersch <lupinix@mailbox.org> 0.6-0.1.git20170401.7325229
- initial build (review rhbz #1440542)
