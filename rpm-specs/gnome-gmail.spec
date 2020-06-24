%if 0%{?fedora}
%bcond_without python3
%else
%bcond_with python3
%endif
%{!?python3_pkgversion: %global python3_pkgversion 3}

Name:           gnome-gmail
Version:        2.4.1
Release:        11%{?dist}
Summary:        Integrate GMail into the GNOME desktop

License:        GPLv2
URL:            https://davesteele.github.io/gnome-gmail/
Source0:        https://github.com/davesteele/%{name}/archive/master/%{version}.tar.gz
# https://github.com/davesteele/gnome-gmail/pull/65
Patch0:         0001-Load-only-needed-dialog-objects-from-builder.patch
# https://github.com/davesteele/gnome-gmail/issues/55
Patch2:         %{name}-2.4-py3-upload.patch
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  %{_bindir}/appstream-util
BuildRequires:  gtk3
BuildRequires:  libnotify
BuildRequires:  libsecret
BuildRequires:  libwnck3
%if %{with python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-gobject-base
Requires:       python%{python3_pkgversion}-six
Requires:       python%{python3_pkgversion}-gobject-base
%else
BuildRequires:  python2-devel
BuildRequires:  pytest
BuildRequires:  python2-mock
BuildRequires:  python2-nose
BuildRequires:  python2-six
BuildRequires:  pygobject2
Requires:       python2-six
Requires:       pygobject2
%endif

Requires:       gtk3
Requires:       hicolor-icon-theme
Requires:       libnotify
Requires:       libsecret
Requires:       libwnck3
Requires:       xdg-utils


%description
This package makes Gmail a choice in the Gnome control panel for the default
mail handler. It opens in the default web browser.


%prep
%setup -qn %{name}-master-%{version}
%patch0 -p1
%if %{with python3}
%patch2 -p1
%endif
rm test/test_setup.py  # unnecessary for us (setup.py --dry-run install)
# https://github.com/davesteele/gnome-gmail/issues/57
sed -i -e "s|/etc/resolv.conf|$(pwd)/README.md|" test/test_main.py


%build
%if %{with python3}
%py3_build
%else
%py2_build
%endif


%install
%if %{with python3}
%py3_install
sed -i -e 's|/usr/bin/python[^ ]*|%{__python3}|' \
    %{buildroot}%{_datadir}/%{name}/gnomegmail.py
%else
%py2_install
sed -i -e 's|/usr/bin/python[^ ]*|%{__python2}|' \
    %{buildroot}%{_datadir}/%{name}/gnomegmail.py
%endif
cat <<\EOF > %{buildroot}%{_bindir}/%{name}
#!/bin/sh
# GDK_BACKEND=x11 hack: see https://github.com/davesteele/gnome-gmail/pull/53
exec /usr/bin/env GDK_BACKEND=x11 %{_datadir}/%{name}/gnomegmail.py "$@"
EOF
%find_lang %{name}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{name}.desktop

# Manpages
mkdir -p %{buildroot}/%{_mandir}/man1/
install -m 644 %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1
rm -rf %{buildroot}/%{_docdir}/%{name}


%check
%if %{with python3}
%{__python3} -Wall setup.py test
%else
%{__python2} -Wall setup.py test
%endif
appstream-util validate-relax --nonet \
    %{buildroot}%{_datadir}/appdata/*.appdata.xml


%files -f %{name}.lang
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS ChangeLog NEWS README.md
%{_bindir}/%{name}
%if %{with python3}
%{python3_sitelib}/*egg-info
%else
%{python2_sitelib}/*egg-info
%endif
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}
%{_datadir}/gnome/autostart/%{name}-startup.desktop
%{_mandir}/man1/%{name}.1*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.1-11
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.1-9
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4.1-5
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 13 2017 Ville Skyttä <ville.skytta@iki.fi> - 2.4.1-3
- Patch to fix handler not found errors on startup (#1264237)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 21 2017 Ville Skyttä <ville.skytta@iki.fi> - 2.4.1-1
- Update to 2.4.1
- Run tests with -Wall

* Mon May 22 2017 Ville Skyttä <ville.skytta@iki.fi> - 2.4-1
- Update to 2.4, hack to work with Wayland

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Ville Skyttä <ville.skytta@iki.fi> - 2.3.1-1
- Update to 2.3.1

* Thu Jan  5 2017 Ville Skyttä <ville.skytta@iki.fi> - 2.3-1
- Update to 2.3
- Sync icon cache and desktop database scriptlets with packaging guidelines

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.2-2
- Rebuild for Python 3.6

* Fri Jul  1 2016 Ville Skyttä <ville.skytta@iki.fi> - 2.2-1
- Update to 2.2

* Sun May 29 2016 Ville Skyttä <ville.skytta@iki.fi> - 2.1-1
- Update to 2.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 10 2016 Ville Skyttä <ville.skytta@iki.fi> - 2.0.1-1
- Update to 2.0.1

* Fri Dec  4 2015 Ville Skyttä <ville.skytta@iki.fi> - 1.9.5-1
- Upstream 1.9.5, python 3 packaging preparations
- Fix build and runtime dependencies
- Mark COPYING as %%license where applicable
- Clean up desktop-file-install and files list

* Sat Nov 28 2015 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 1.9.4-1
- Upstream 1.9.4

* Fri Nov 20 2015 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 1.9.3.1-2
- Fix requires and bug #1268672 gnome-gmail version 1.9.3.1-1.fc22 noarch crashes !

* Fri Aug 28 2015 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 1.9.3.1-1
- Upstream 1.9.3.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 05 2011 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 1.8.2-1
- Upstream 1.8.2

* Wed Aug 31 2011 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 1.8.1-1
- Upstream 1.8.1

* Sun Apr 24 2011 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 1.7.2-2
- Add scheme handler line in desktop file, for GNOME 3

* Mon Feb 28 2011 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 1.7.2-1
- Upstream 1.7.2

* Fri Feb 18 2011 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 1.7.1-1
- Upstream 1.7.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Oct 31 2010 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 1.7-2
- Fix bug #629260 Missing panel icon for gnome-gmail

* Fri Oct 22 2010 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 1.7-1
- Upstream 1.7
- Add french translation in SPEC

* Wed Jul 21 2010 Guillaume Kulakowski <guillaume.kulakowski@fedoraproject.org> - 1.5.1-1
- Initial packaging
