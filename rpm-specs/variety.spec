#For git snapshots, set to 0 to use release instead:
%global usesnapshot 0
%if 0%{?usesnapshot}
%global commit0 8b8bb63a10fa22760eb976b1fd57338f3dba3233
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global snapshottag .git%{shortcommit0}
%endif

Name:           variety
%if 0%{?usesnapshot}
Version:        0.8.4
Release:        0.3%{?snapshottag}%{?dist}
%else
Version:        0.8.4
Release:        3%{?dist}
%endif
Summary:        Wallpaper changer that automatically downloads wallpapers
License:        GPLv3
URL:            https://github.com/varietywalls/variety

%if 0%{?usesnapshot}
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
%else
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-configobj
BuildRequires:  python3-lxml
BuildRequires:  python3-gexiv2
BuildRequires:  python3-pycurl
BuildRequires:  python3-requests
BuildRequires:  python3-pillow-devel
BuildRequires:  intltool
BuildRequires:  yelp-devel
BuildRequires:  python3-dbus
BuildRequires:  python3-cairo-devel
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  %{py3_dist beautifulsoup4}
Requires:       python3-dbus
Requires:       hicolor-icon-theme
Requires:       ImageMagick
Requires:       libappindicator-gtk3
Requires:       python3-lxml
Requires:       python3-pillow
BuildRequires:  python3-cairo
#Requires:       python3-appindicator -- not available yet
Requires:       python3-beautifulsoup4
Requires:       python3-configobj
Requires:       python3-gexiv2
Requires:       python3-pycurl
Requires:       python3-requests
Requires:       xorg-x11-fonts-Type1

%description
Variety changes the desktop wallpaper on a regular basis, 
using user-specified or automatically downloaded images.

Variety sits conveniently as an indicator in the panel 
and can be easily paused and resumed. The mouse wheel 
can be used to scroll wallpapers back and forth until 
you find the perfect one for your current mood.

Apart from displaying images from local folders, several 
different online sources can be used to fetch wallpapers 
according to user-specified criteria.

Variety can also automatically apply various fancy 
filters to the displayed images - charcoal painting, 
oil painting, heavy blurring, etc. - so that your 
desktop is always fresh and unique. 

%prep

%if 0%{?usesnapshot}
%setup -q -n %{name}-%{commit0}
%else
%autosetup -p1
%endif


%if 0%{?fedora} >= 33
# Replace deprecated getiterator() with iter()
sed -i -e 's|getiterator|iter|' variety_lib/Builder.py
%endif

# remove debian part
rm -rf debian

%build
# Bytecompile Python modules
%py_byte_compile %{__python3} setup.py build

%install
%{__python3} setup.py install --root=%{buildroot}

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}.appdata.xml

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/%{name}/
%{python3_sitelib}/jumble/
%{python3_sitelib}/%{name}-*-py*.egg-info
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}_lib/
%{_datadir}/icons/hicolor/22x22/apps/%{name}-indicator-dark.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}-indicator.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
* Sun Oct 04 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.8.4-3
- Replace deprecated getiterator() with iter()

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.8.4-1
- Update to 0.8.4
- Bytecompile Python modules

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.4-0.2.git8b8bb63
- Rebuilt for Python 3.9

* Tue Mar 24 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.8.4-0.1.git8b8bb63
- Update to 0.8.4-0.1.git8b8bb63 fix (BZ #1794896)

* Wed Feb 12 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.8.3-1
- Update to 0.8.3

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.8.2-1
- Update to 0.8.2

* Sat Jan 04 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.8.1-2
- Bump version due #8482 Koji build fails with "GenericError: Build already in progress"

* Thu Jan 02 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1

* Thu Nov 14 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.8.0-0.7.gite81db6b
- Add RR xorg-x11-fonts-Type1 with Bitstream Character as fallback font

* Wed Oct 30 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.8.0-0.6.gite81db6b
- Update to 0.8.0-0.6.gite81db6b

* Thu Sep 05 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.8.0-0.5.git3fbf10e
- Update to 0.8.0-0.5.git3fbf10e
- Add BR %%{py3_dist beautifulsoup4} fix (BZ #1749302)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-0.4.gitf8d1e5b
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.8.0-0.3.gitf8d1e5b
- Update to 0.8.0-0.3.gitf8d1e5b

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-0.2.git2dd2ee2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 29 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.8.0-0.1.git2dd2ee2
- Update to 0.8.0-0.1.git2dd2ee2

* Mon Apr 22 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.7.2-1
- Update to 0.7.2

* Fri Apr 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-4
- Drop obsolete Python 2 dependencies

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 0.7.1-3
- Drop obsolete pyexiv2 dependency

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 09 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.7.1-1
- Update to 0.7.1

* Fri Oct 05 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-2
- Use Metainfo dir for appdata file

* Mon Oct 01 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0
- Switche to python3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 18 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.6.9-1
- Update to 0.6.9

* Tue May 01 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.6.8-2
- Dropped RR pywebkitgtk (BZ#1573401)

* Mon Apr 23 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.6.8-1
- Update to 0.6.8

* Thu Apr 05 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.6.7-2
- Add bytecompile with Python 2 %%global __python %%{__python2}

* Wed Apr 04 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.6.7-1
- Update to 0.6.7
- Changed SOURCE link to github
- Fix python requires for f28

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.6-2
- Remove obsolete scriptlets

* Tue Sep 19 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.6.6-1
- Update to 0.6.6

* Wed Aug 23 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.6.5-1
- Update to 0.6.5
- Cleanup spec file
- Dropped variety-0.6.4-fix_webkit_version.patch
- Dropped BR webkitgtk-devel
- Dropped RR webkitgtk4

* Mon Aug 21 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.6.4-4
- Add variety-0.6.4-fix_webkit_version.patch
- Correct BR webkitgtk3 becomes webkitgtk4 
- Add RR pywebkitgtk

* Sat Aug 19 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.6.4-3
- Add RR libappindicator-gtk3
- Correct RR ImageMagick it's case sensitive
- Add RR webkitgtk3

* Fri Aug 18 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.6.4-2
- Add RR python-lxml
- Add RR python-pillow
- Add RR pycairo
- Add RR dbus-python
- Add RR python-appindicator
- Add RR python-beautifulsoup4
- Add RR python-configobj
- Add RR python2-gexiv2
- Add RR python-pycurl
- Add RR python2-requests
- Add RR pyexiv2
- Add RR imagemagick
- Add RR hicolor-icon-theme
- Add BR libappstream-glib
- Add appdata.xml file

* Tue Jul 18 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.6.4-1
- initial build
