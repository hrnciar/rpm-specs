%if ! 0%{?qt5_qtwebengine_arches:1}
# available from qt5-srpm-macros via redhat-rpm-config in Fedora >= 25
%global qt5_qtwebengine_arches %{ix86} x86_64 %{arm} aarch64 mips mipsel mips64el
%endif

Name:           otter-browser
Summary:        Web browser controlled by the user, not vice-versa
# Files in 3rdparty/libmimeapps and 3rdparty/mousegestures are BSD (2 clause)
License:        GPLv3+ and BSD
Version:        1.0.01
Release:        4%{?dist}
URL:            http://otter-browser.org/
Source0:        https://github.com/OtterBrowser/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  hunspell-devel
BuildRequires:  kf5-sonnet-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtwebkit-devel
%ifarch %{qt5_qtwebengine_arches}
BuildRequires:  qt5-qtwebengine-devel
%endif
BuildRequires:  qt5-qtsensors-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtxmlpatterns-devel
BuildRequires:  libappstream-glib

%description
Web browser aiming to recreate classic Opera (12.x) UI using Qt5.

%prep
%setup -qn %{name}-%{version}
#################################################
#rm -rf 3rdparty/sonnet
#################################################

%build
%cmake .
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_datadir}/{applications,appdata}
install -Dm 0644 packaging/otter-browser.appdata.xml %{buildroot}%{_datadir}/appdata/otter-browser.appdata.xml

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
   %{name}.desktop

%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.appdata.xml

%files -f %{name}.lang
%doc CHANGELOG README.md TODO
%license COPYING
%{_bindir}/otter-browser
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/otter-browser.appdata.xml
%{_datadir}/icons/hicolor/*/apps/otter-browser.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/locale/otter-browser_jbo.qm
%{_datadir}/%{name}/locale/otter-browser_yue.qm
%{_mandir}/man1/%{name}.1.gz


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.0.01-1
- Update to 1.0.01-1

* Tue Nov 13 2018 Caolán McNamara <caolanm@redhat.com> -0.9.99.3-0.2.rc12git63b7445
- rebuild for hunspell 1.7.0

* Mon Sep 03 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.99.3-0.1.rc12git63b7445
- Update to 0.9.99.3-0.1.rc12git63b7445

* Sun Aug 12 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.99.2-0.1.rc11git4ec4151
- Update to 0.9.99.2-0.1.rc11git4ec4151

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.99-0.2.rc10git282b5b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.99-0.1.rc10git282b5b3
- Update to 0.9.99-0.1.rc10git282b5b3

* Sun Jun 10 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.99-0.1.rc9gita29c3b0
- Update to 0.9.99-0.1.rc9gita29c3b0

* Wed May 02 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.98-0.1.rc8git282600f
- Update to 0.9.98-0.1.rc8git282600f

* Tue Apr 03 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.97-0.1.rc7git8342385
- Update to 0.9.97-0.1.rc7git8342385

* Sat Mar 03 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.96-0.1.rc6git1b61eec
- Update to 0.9.96-0.1.rc6git1b61eec

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.95-0.2.rc5git406ad76
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.95-0.1.rc5git406ad76
- Update to 0.9.95-0.1.rc5git406ad76

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.94-0.2.rc4gitc2a56a0
- Remove obsolete scriptlets

* Tue Jan 02 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.9.94-0.1.rc4gitc2a56a0
- Update to 0.9.94-0.1.rc4gitc2a56a0

* Mon Dec 04 2017 Caolán McNamara <caolanm@redhat.com> - 0.9.93-0.2.rc3gitb1328fd
- rebuild for hunspell 1.6.2

* Mon Dec 04 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.9.93-0.1.rc3gitb1328fd
- Update to 0.9.93-0.1.rc3gitb1328fd

* Sat Nov 18 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.9.92-0.2.rc1gita026c61
- Update to 0.9.92-0.2.rc1gita026c61

* Thu Nov 02 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.9.92-0.1.rc1git97d18d8
- Update to 0.9.92-0.1.rc1git97d18d8

* Mon Oct 02 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.9.91-0.1.rc1git4fbf638
- Update to 0.9.91-0.1.rc1git4fbf638

* Fri Sep 29 2017 Martin Gansser <martinkg@fedoraproject.org>  - 0.9.12-0.6.beta12gitb195b9a
- Update to 0.9.12-0.6.beta12gitb195b9a
- Add BR qt5-qtsvg-devel

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-0.5.beta12gitd82cbcc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-0.4.beta12gitd82cbcc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 11 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.9.12-0.3.beta12gitd82cbcc
- Update to 0.9.12-0.3.beta12gitd82cbcc

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-0.2.beta12git90e17b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 03 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.9.12-0.1.beta12git90e17b8
- Update to 0.9.12-0.1.beta12git90e17b8

* Tue Dec 13 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.9.11-0.3.beta11gitc051a5e
- Rebuild for hunspell 1.5.x

* Mon Oct 03 2016 Dan Horák <dan[at]danny.cz> - 0.9.11-0.2.beta11gitc051a5e
- Fix BR qt5-qtwebengine-devel

* Sun Oct 02 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.9.11-0.1.beta11gitc051a5e
- Update to 0.9.11-01.beta11
- Added BR qt5-qtwebengine-devel
- Added BR hunspell-devel

* Tue May 03 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.9.10-0.1.beta10gitb36046f
- Update to 0.9.10-01.beta10

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.09-0.2.beta9gitff0bb28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.9.09-0.1.beta9gitff0bb28
- Update to 0.9.09-01.beta9
- Added BR kf5-sonnet-devel
- Follow https://fedoraproject.org/wiki/Packaging:SourceURL

* Wed Dec 02 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.9.08-0.1.beta8git2fbb4d7
- Update to 0.9.08-01.beta8

* Tue Dec 01 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.9.07-0.2.beta7gitcc6b5b5
- Added BR qt5-qtxmlpatterns-devel
- Update for new git snapshot

* Wed Sep 02 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.9.07-0.1.beta7git9946beb
- Update to 0.9.07-01.beta7

* Tue Jun 02 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.9.06-0.1.beta6gitaf837be
- Update to 0.9.06-01.beta6

* Mon Apr 06 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.9.05-0.2.beta5git8c705ab
- Update to 0.9.05-02.beta5
- Mark license files as %%license where available

* Thu Jan 01 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.9.05-0.1.beta5gitd998eb4
- Update to 0.9.05-01.beta5
- added BR qt5-qtmultimedia-devel

* Fri Dec 12 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.9.04-0.2.beta3gitcdcf0c0
- rebuild for new git release
- cleanup spec file

* Mon Dec 08 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.9.04-0.1.beta4git0bbf467
- Update to 0.9.04-0.1.beta4
- correct project's web site url
- correct license tag
- removed %%{_datadir}/icons/hicolor was not owned or used
- added %%check section
- added BR libappstream-glib
- added appdata.xml file

* Thu Oct 30 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.9.03-0.1.beta3gitc2c558a
- use commit revision in source url
- added macro %%find_lang

* Thu Aug 28 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.9.02-2
- added own directory for otter-browser

* Thu Aug 28 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.9.02-1
- Update to 0.9.02
- used macro make_install

* Mon Jun 23 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.9.01-5.beta1
- changed %%cmake command following fedora packaging guide

* Sun Jun 08 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.9.01-4.beta1
- changed release Tag

* Sat Jun 07 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.9.01-3
- replaced qmake-qt5 by cmake
- added manual page

* Fri Jun 06 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.9.01-2
- added BR desktop-file-utils

* Fri Jun 06 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.9.01-1
- initial build for Fedora 20

