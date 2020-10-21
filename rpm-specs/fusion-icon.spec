
Name:           fusion-icon
Version:        0.2.4
Release:        15%{?dist}
Epoch:          1
Summary:        Compiz Fusion panel applet
License:        GPLv2+
URL:            https://gitlab.com/compiz/%{name}
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildArch:      noarch

# https://github.com/compiz-reloaded/fusion-icon/commit/9c598b8
Patch1:         fusion-icon_0001-Fix-typeerror-in-python3.6.patch

BuildRequires:  python3-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  desktop-file-utils

Requires:       ccsm
Requires:       gobject-introspection
Requires:       libappindicator-gtk3
Requires:       compizconfig-python
Requires:       python3-gobject
Requires:       python3-qt5
Requires:       xvinfo

Obsoletes: %{name}-gtk < %{epoch}:%{version}-%{release}
%if 0%{?fedora} < 25
Provides:  %{name}-gtk = %{epoch}:%{version}-%{release}
%endif

%description
The Compiz Fusion Icon is a simple panel applet for starting and controlling
Compiz Fusion. Upon launch, it will attempt to start Compiz Fusion
automatically. You may need to select a window decorator, if one does not
appear.


%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%py3_build -- --with-gtk=3.0

%install
%py3_install

mv %{buildroot}%{_datadir}/{metainfo,appdata}/

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/fusion-icon.desktop



%files
%doc COPYING
%{_bindir}/fusion-icon
%{_datadir}/applications/fusion-icon.desktop
%dir %{python3_sitelib}/FusionIcon/
%{python3_sitelib}/FusionIcon/*py*
%{_datadir}/appdata/fusion-icon.appdata.xml
%{_datadir}/icons/hicolor/*/apps/fusion-icon.png
%{_datadir}/icons/hicolor/scalable/apps/fusion-icon.svg
%{python3_sitelib}/fusion_icon-%{version}-py3.?.egg-info
%{python3_sitelib}/FusionIcon/interface_gtk/
%{python3_sitelib}/FusionIcon/interface_qt/


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:0.2.4-14
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1:0.2.4-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1:0.2.4-11
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr  2 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 1:0.2.4-9
- New URL

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1:0.2.4-6
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1:0.2.4-4
- probably fix for rhbz (#1540206)
- use https://github.com/compiz-reloaded/fusion-icon/commit/9c598b8

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:0.2.4-3
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 11 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1:0.2.4-1
- update to 0.2.4 release

* Thu Apr 20 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1:0.2.3-2
- update to 0.8.14 release
- Fix fail to fallback from GTK+ if dependencies are not met.
- Add Python3 support.
- Use /usr/local as a default prefix path.
- switch to python3
- modernize spec file

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.2-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Apr  4 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1:0.2.2-2
- Drop unnessary ExcludeArch

* Wed Mar 16 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.2.2-1
- update to 0.2.2 release

* Thu Mar 03 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.2.1-1
- update to 0.2.1

* Sat Feb 13 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.2.0-1
- update to 0.2.0 release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 20 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.1.2-4
- fix runtime requires again

* Sun Dec 20 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.1.2-3
- fix runtime requires

* Sat Dec 19 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.1.2-2
- add missing requires

* Sat Dec 19 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.1.2-1
- update to 0.1.2 release
- support for mate-window-decorator
- drop subpackage
- use python rpmbuild style

* Tue Oct 20 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.1.1-1
- switch to new upstream with new 0.1.1 release
- remove old patches
- clean up spec file
- use gtk3 as gui interface
- selecting gwd with current marco theme is working now
- menu entry is now in utilities

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 18 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.1-8
- rebuild for f22

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 22 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> -  1:0.1-4
- bump version

* Mon Oct 15 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> -  1:0.1-3
- build for fedora
- review package
- remove python_sitelib stuff
- fix icon cache scriptlets
- fix python2-devel BR
- fix non-executable-script

* Sat Sep 29 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.1-2
- add %%{?dist} tag again

* Sat Sep 29 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.1-1
- add Epoch tag
- improve spec file

* Wed Sep 19 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.1.0-0.9.5e2dc9git
- improve spec file
- remove qt subpackage

* Tue May 15 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.1.0-0.8.5e2dc9git
- build for mate

