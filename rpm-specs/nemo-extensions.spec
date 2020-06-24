# Don't bother building debug packages as koji bitches about n-v-r from nemo package
%global         debug_package %{nil}

Name:           nemo-extensions
Version:        4.6.0
Release:        2%{?dist}
Summary:        Extensions for Nemo

License:        GPLv2+ and LGPLv2
URL:            https://github.com/linuxmint/%{name}
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gpgme-devel
BuildRequires:  pkgconfig(cryptui-0.0) 
BuildRequires:  pkgconfig(gnome-keyring-1)
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(libnemo-extension) >= 4.6.0
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(cjs-1.0) >= 4.6.0
BuildRequires:  pkgconfig(xreader-view-1.5)
BuildRequires:  pkgconfig(libmusicbrainz5)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(clutter-gst-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  perl(XML::Parser)

%description
Extensions for Nemo

%package     -n nemo-audio-tab
Summary:     Audio tag information extension for Nemo
License:     GPLv3+
BuildArch:   noarch
Requires:    python3-mutagen
Requires:    nemo-python

%description -n nemo-audio-tab
nemo-audio-tab is an extension to view audio tag information from the properties tab.

%package     -n nemo-pastebin
Summary:     Pastebin extension for Nemo
License:     GPLv2+
BuildArch:   noarch
Requires:    pastebinit
Requires:    nemo-python

%description -n nemo-pastebin
nemo-pastebin is an extension for the Nemo file manager, which allows
users to send files to pastebins just a right-click away.

%package     -n nemo-fileroller
Summary:     File Roller extension for Nemo
License:     GPLv2+
Requires:    file-roller

%description -n nemo-fileroller
This package contains the file-roller extension for the Nemo.

%package     -n nemo-python
Summary:     Python scripting extension for Nemo
License:     GPLv2+
Obsoletes:   python2-nemo < %{version}-%{release}
Obsoletes:   python3-nemo < %{version}-%{release}
Provides:    python3-nemo = %{version}-%{release}
Requires:    nemo >= 4.6.0
Requires:    python3-gobject-base

%description -n nemo-python
Python scripting extension for Nemo

%package     -n nemo-python-devel
Summary:     Python scripting extension for Nemo
License:     GPLv2+
Obsoletes:   python2-nemo-devel < %{version}-%{release}
Obsoletes:   python3-nemo-devel < %{version}-%{release}
Requires:    nemo-python%{?_isa} = %{version}-%{release}

%description -n nemo-python-devel
Python scripting extension for Nemo

%package     -n nemo-terminal
Summary:     Embedded terminal window for Nemo
License:     GPLv3+
BuildArch:   noarch
Requires:    vte291
Requires:    nemo-python = %{version}-%{release}

%description -n nemo-terminal
Embedded terminal window for Nemo

%package     -n nemo-preview
Summary:     A quick previewer for Nemo
License:     GPLv2+
Requires:    nemo

%description -n nemo-preview
Nemo Preview is a GtkClutter and Javascript-based quick previewer
for Nemo.
It is capable of previewing documents, PDFs, sound and video files,
some text files, and possibly others in the future.

To activate the preview, left-click the file and hit space.
The preview can be closed by hitting space again, or escape.

%package     -n nemo-emblems
Summary:     Emblem support for nemo
License:     GPLv3+
BuildArch:   noarch
Requires:    nemo-python = %{version}-%{release}

%description -n nemo-emblems
Restores the emblems functionality that used to be in GNOME 2.

%package     -n nemo-image-converter
Summary:     Nemo extension to mass resize images
Requires:    ImageMagick
License:     GPLv3+

%description -n nemo-image-converter
Adds a "Resize Images..." menu item to the context menu.
This opens a dialog where you set the desired image size and file name.

%package     -n nemo-compare
Summary:     Context menu comparison extension for nemo
License:     GPLv3+
BuildArch:   noarch
Requires:    nemo-python = %{version}-%{release}
Requires:    meld

%description -n nemo-compare
Context menu comparison extension for Nemo file manager.

%package     -n nemo-seahorse
Summary:     PGP encryption and signing for Nemo
License:     GPLv2+ and LGPLv2
Requires:    seahorse%{?_isa}

%description -n nemo-seahorse
Seahorse nemo is an extension for nemo which allows encryption
and decryption of OpenPGP files using GnuPG. 

%prep
%autosetup -p1

%build
pushd nemo-audio-tab
%py3_build
popd

pushd nemo-pastebin
%py3_build
popd

pushd nemo-fileroller
NOCONFIGURE=1 ./autogen.sh
%configure
%make_build V=1
popd

pushd nemo-python
%meson
%meson_build
popd

pushd nemo-terminal
%py3_build
popd

pushd nemo-preview
NOCONFIGURE=1 ./autogen.sh
intltoolize -f
%configure
%make_build V=1
popd

pushd nemo-emblems
%py3_build
popd

pushd nemo-image-converter
NOCONFIGURE=1 gnome-autogen.sh
%configure
%make_build V=1
popd

pushd nemo-compare
%py3_build
popd

pushd nemo-seahorse
NOCONFIGURE=1 ./autogen.sh
%configure
%make_build V=1
popd 

%install
pushd nemo-audio-tab
%py3_install
popd

pushd nemo-pastebin
%py3_install
popd

pushd nemo-fileroller
%make_install
popd

pushd nemo-python
%meson_install
popd

pushd nemo-terminal
%py3_install
popd

pushd nemo-preview
%make_install
popd

pushd nemo-emblems
%py3_install
popd

pushd nemo-image-converter
%make_install
popd

pushd nemo-compare
%py3_install
popd

pushd nemo-seahorse
%make_install
popd 

# remove useless libtool archive files
rm %{buildroot}/%{_libdir}/nemo/extensions-3.0/libnemo-*.la
rm %{buildroot}/%{_libdir}/nemo/extensions-3.0/libnemo-*.a
rm %{buildroot}/%{_libdir}/nemo-preview/libnemo-preview-1.0.la


rm -rf %{buildroot}/%{_datadir}/doc/nemo-python/

desktop-file-install                                    \
 --delete-original                                      \
 --dir=%{buildroot}%{_datadir}/applications             \
 %{buildroot}/%{_datadir}/applications/nemo-seahorse-pgp-*.desktop

%find_lang nemo-preview

%files -n nemo-audio-tab
%license nemo-audio-tab/COPYING.GPL3
%{_datadir}/nemo-python/extensions/nemo-audio-tab.py
%{_datadir}/nemo-audio-tab/nemo-audio-tab.glade
%{python3_sitelib}/nemo_audio_tab-%{version}-py?.?.egg-info/


%files -n nemo-pastebin
%doc nemo-pastebin/README
%doc nemo-pastebin/NEWS
%license nemo-pastebin/COPYING
%{_bindir}/nemo-pastebin-configurator
%{_datadir}/nemo-python/extensions/nemo-pastebin.py
%{python3_sitelib}/nemo_pastebin-%{version}-py?.?.egg-info/
%{_datadir}/glib-2.0/schemas/nemo-pastebin.gschema.xml
%{_datadir}/nemo-pastebin/
%{_datadir}/icons/hicolor/*/apps/nemo-pastebin.*

%files -n nemo-fileroller
%doc nemo-fileroller/README
%license nemo-fileroller/COPYING
%{_libdir}/nemo/extensions-3.0/libnemo-fileroller.so

%files -n nemo-python
%doc nemo-python/README
%doc nemo-python/examples
%license nemo-python/COPYING
%{_libdir}/nemo/extensions-3.0/libnemo-python.so
%{_datadir}/nemo-python/
%exclude %{_datadir}/nemo-python/extensions/*

%files -n nemo-python-devel
%{_libdir}/pkgconfig/nemo-python.pc

%files -n nemo-terminal
%doc nemo-terminal/README
%license nemo-terminal/COPYING
%{_bindir}/nemo-terminal-prefs
%{_datadir}/nemo-python/extensions/nemo_terminal.py
%{_datadir}/nemo-terminal/
%{_datadir}/glib-2.0/schemas/org.nemo.extensions.nemo-terminal.gschema.xml
%{python3_sitelib}/nemo_terminal-%{version}-py?.?.egg-info/

%files -n nemo-preview -f nemo-preview.lang
%doc nemo-preview/README
%license nemo-preview/COPYING
%{_bindir}/nemo-preview
%{_libdir}/nemo-preview/
%{_libexecdir}/nemo-preview-start
%{_datadir}/nemo-preview/
%{_datadir}/dbus-1/services/org.nemo.Preview.service

%files -n nemo-emblems
%license nemo-emblems/COPYING.GPL3
%{_datadir}/nemo-python/extensions/nemo-emblems.py
%{python3_sitelib}/nemo_emblems-%{version}-py?.?.egg-info/

%files -n nemo-image-converter
%doc nemo-image-converter/README
%license nemo-image-converter/COPYING
%{_libdir}/nemo/extensions-3.0/libnemo-image-converter.so
%{_datadir}/nemo-image-converter/

%files -n nemo-compare
%{_bindir}/nemo-compare-preferences
%{_datadir}/nemo-python/extensions/nemo-compare.py
%{_datadir}/nemo-compare/nemo-compare-preferences.py
%{_datadir}/nemo-compare/utils.py*
%{python3_sitelib}/nemo_compare-%{version}-py?.?.egg-info/

%files -n nemo-seahorse
%doc nemo-seahorse/{AUTHORS,COPYING,README,NEWS,ChangeLog}
%{_bindir}/nemo-seahorse-tool
%{_libdir}/nemo/extensions-3.0/libnemo-seahorse.so
%{_datadir}/applications/nemo-seahorse-pgp-*.desktop
%{_datadir}/glib-2.0/schemas/org.nemo.plugins.seahorse*gschema.xml
%{_datadir}/nemo-seahorse/
%{_mandir}/man1/nemo-seahorse-tool.1.* 

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.6.0-2
- Rebuilt for Python 3.9

* Wed May 13 2020 Leigh Scott <leigh123linux@gmail.com> - 4.6.0-1
- Update to 4.6.0 release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Leigh Scott <leigh123linux@googlemail.com> - 4.4.0-6
- Add patch to fix gcc-10 compile issue

* Thu Jan 23 2020 Leigh Scott <leigh123linux@googlemail.com> - 4.4.0-5
- Workaround gcc-10 issue till upstream addresses it

* Fri Dec 13 2019 FeRD (Frank Dana) <ferdnyc@gmail.com> - 4.4.0-4
- nemo-python: Add provides for python3-nemo, required by some
  legacy dependent packages

* Fri Dec 13 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.4.0-3
- Add nemo-audio-tab

* Thu Nov 21 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.4.0-2
- Fix python embed issue

* Sat Nov 16 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.4.0-1
- Update to 4.4.0 release

* Tue Nov 05 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.2.0-5
- Fix nemo-python requires

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-4
- Rebuilt for Python 3.8

* Thu Aug 08 2019 FeRD (Frank Dana) <ferdnyc@gmail.com> - 4.2.0-3
- Rename Python extension package back to nemo-python

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 2019 Leigh Scott <leigh123linux@googlemail.com> - 4.2.0-1
- Update to 4.2.0 release

* Thu Jun 06 2019 Leigh Scott <leigh123linux@gmail.com> - 4.0.0-4
- Readd nemo-seahorse (rhbz #1716999)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 15 2018 Leigh Scott <leigh123linux@googlemail.com> - 4.0.0-2
- Fix emblem locale

* Thu Nov 01 2018 Leigh Scott <leigh123linux@googlemail.com> - 4.0.0-1
- Update to 4.0.0 release

* Mon Jul 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.0-6
- Swap to python2 sitearch macro

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.0-4
- Fix nemo-terminal

* Mon May 07 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.0-3
- Add provides for nemo-python

* Tue May 01 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.0-2
- Don't bother building debug packages as koji bitches about n-v-r from nemo package

* Tue May 01 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.8.0-1
- Update to 3.8.0 release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.6.0-4
- use %%python_provide macro (so arch'd provides are included too)
- tighten subpkg deps

* Thu Feb 01 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.6.0-3
- Rename nemo-python to python2-nemo

* Tue Dec 12 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.6.0-2
- Fix typelib issue

* Tue Oct 24 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.6.0-1
- update to 3.6.0 release

* Sun Sep 03 2017 Björn Esser <besser82@fedoraproject.org> - 3.4.0-9
- Fix build

* Sun Sep 03 2017 Björn Esser <besser82@fedoraproject.org> - 3.4.0-8
- Use proper Python macros

* Sun Sep 03 2017 Björn Esser <besser82@fedoraproject.org> - 3.4.0-7
- Make sure we explicitly use Python 2

* Sun Sep 03 2017 Björn Esser <besser82@fedoraproject.org> - 3.4.0-6
- Adaptions for EPEL

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 09 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.0-3
- add upstream fixes

* Wed May 31 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.0-2
- add upstream fixes

* Thu May 04 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.4.0-1
- update to 3.4.0 release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-0.2.20170131gitbefdb82
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.2.1-0.1.20170131gitbefdb82
- update to latest git

* Mon Nov 28 2016 leigh scott <leigh123linux@googlemail.com> - 3.2.0-2
- fix error on nemo-compare plugin name

* Mon Nov 07 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.2.0-1
- update to 3.2.0 release

* Fri Jun 24 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.0.0-2
- add upstream patches

* Sun Apr 24 2016 Leigh Scott <leigh123linux@googlemail.com> - 3.0.0-1
- update to 3.0.0 release

* Sun Apr 10 2016 Leigh Scott <leigh123linux@googlemail.com> - 2.8.x-10
- fix nemo-compare (bz 1323041)
- obsolete nemo-rabbitvcs

* Mon Mar 07 2016 Leigh Scott <leigh123linux@googlemail.com> - 2.8.x-9
- more epel7 fixes

* Mon Mar 07 2016 Leigh Scott <leigh123linux@googlemail.com> - 2.8.x-8
- fix epel7 build

* Sat Mar 05 2016 Leigh Scott <leigh123linux@googlemail.com> - 2.8.x-7
- fix nemo-rabbitvcs

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.x-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 29 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.8.x-5
- switch to more secure webkit version

* Fri Dec 04 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.8.x-4
- another friggin build fix for epel

* Fri Dec 04 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.8.x-3
- remove pastebin and rabbitvcs extensions for epel

* Tue Nov 10 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.8.x-2
- rebuilt

* Thu Oct 22 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.8.x-1
- update to 2.8.0 release

* Sat Jul 25 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.x-5
- build fixes

* Sat Jul 25 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.x-4
- add nemo-compare

* Mon Jul 13 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.x-3
- fix cd (nemo-terminal)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.x-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 02 2015 Leigh Scott <leigh123linux@googlemail.com> - 2.6.x-1
- update to 2.6.x

* Thu Nov 27 2014 Haïkel Guémar <hguemar@fedoraproject.org> - 2.4.x-3
- Rebuilt against newer libmusicbrainz5 (required for nemo-preview)

* Thu Nov 13 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.x-2
- change requires on nemo-terminal to vte3
- add patch to fix nemo-terminal

* Sat Nov 01 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.4.x-1
- update to 2.4.x

* Tue Oct 21 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.3.x-0.2.gited31dbd
- add noarch

* Tue Oct 21 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.3.x-0.1.gited31dbd
- update to latest git
- add nemo-emblems
- add nemo-image-converter

* Sun Oct 19 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.x-6
- patch nemo-preview for gjs changes (bz 1154111)

* Wed Oct 01 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.x-5
- rebuilt

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.x-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 2.2.x-3
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.x-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.2.x-1
- update to 2.2.x

* Thu Feb 20 2014 Kalev Lember <kalevlember@gmail.com> - 2.0.0-0.6.git6c86726
- Rebuilt for cogl soname bump

* Mon Feb 10 2014 Peter Hutterer <peter.hutterer@redhat.com> - 2.0.0-0.5.git6c86726
- Rebuild for libevdev soname bump

* Fri Feb 07 2014 Leigh Scott <leigh123linux@googlemail.com> - 2.0.0-0.4.git6c86726
- rebuilt for new cogl .so version

* Sat Nov 23 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.0-0.3.git6c86726
- add requires python-simplejson to nemo-rabbitvcs

* Sat Nov 23 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.0-0.2.git6c86726
- add nemo-preview extension

* Thu Oct 31 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.0-0.1.gitfd3cc88
- update to latest git
- add nemo-terminal extension

* Sun Oct 20 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.8.0-0.6.git3e366de
- remove the seahorse extension because
  it's broken and conflicts with seahorse-nautilus
  (can't be bothered to fix it)

* Tue Oct 08 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.8.0-0.5.git3e366de
- add nemo-rabbitvcs sub-package

* Tue Sep 24 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.8.0-0.4.git3e366de
- clean up nemo-pastebin install

* Tue Sep 24 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.8.0-0.3.git3e366de
- fix files listed twice

* Tue Sep 24 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.8.0-0.2.git3e366de
- fix nemo-pastebin
- add python extensions directory

* Tue Sep 24 2013 Leigh Scott <leigh123linux@googlemail.com> - 1.8.0-0.1.git3e366de
- Initial build
