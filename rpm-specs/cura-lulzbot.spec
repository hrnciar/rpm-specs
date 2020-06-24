%global shortname cura-lulzbot

Name:           cura-lulzbot
Version:        3.6.21
Release:        4%{?dist}
Epoch:		1
Summary:        3D printer control software
License:        AGPLv3+
URL:            https://code.alephobjects.com/project/profile/10/
# git clone https://code.alephobjects.com/source/cura-lulzbot.git
# cd cura-lulzbot
# git checkout v3.6.21
## CANNOT use git archive here, need git hash for version
# cd ..
# mv cura-lulzbot cura-lulzbot-3.6.21
# tar cvfz cura-lulzbot-3.6.21.tar.gz cura-lulzbot-3.6.21/
Source0:	cura-lulzbot-%{version}.tar.gz
BuildArch:      noarch
Patch0:		cura-lulzbot-3.2.17-system.patch
Patch1:		cura-lulzbot-2.6.21-CuraEngine-lulzbot.patch
Patch2:		cura-lulzbot-2.6.52-version-fix.patch
Patch3:		cura-lulzbot-3.6.21-disable-linux-distro-check.patch
Patch4:		cura-lulzbot-3.6.21-force-x11.patch

# There are Python plugins in /usr/lib/cura
# We need to byte-compile it with Python 3
%global __python %{__python3}

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-uranium-lulzbot == %{version}
BuildRequires:  CuraEngine-lulzbot >= 1:%{version}

Requires:       open-sans-fonts
Requires:	python3-numpy-stl
Requires:       python3-pyserial
Requires:       python3-savitar >= 2.6
Requires:       python3-uranium-lulzbot == %{version}
Requires:       python3-zeroconf
Requires:       qt5-qtquickcontrols2, qt5-qtquickcontrols
Requires:       CuraEngine-lulzbot >= 1:%{version}
Requires:	lulzbot-marlin-firmware >= 1:1.1.9.34
Requires:	lulzbot-marlin-firmware-pro >= 1:2.0.0.144
Requires:	lulzbot-marlin-firmware-bio >= 1:2.0.0.174
# lulzbot package has the materials inside it, does not conflict
# Requires:       cura-fdm-materials == %%{version}

# So that it just works
Requires:       3dprinter-udev-rules
# Needs this or it segfaults. *shrug*
Requires:	libglvnd-devel

%description
Cura is a project which aims to be an single software solution for 3D printing.
While it is developed to be used with the Ultimaker 3D printer, it can be used
with other RepRap based designs.

Cura prepares your model for 3D printing. For novices, it makes it easy to get
great results. For experts, there are over 200 settings to adjust to your
needs. As it's open source, our community helps enrich it even more.

This is the Lulzbot fork of Cura.

%prep
%setup -q -n cura-lulzbot-%{version}
%patch0 -p1 -b .system
%patch1 -p1 -b .cel
%patch2 -p1 -b .verfix
%patch3 -p1 -b .disable-linux-distro-check
%patch4 -p1 -b .force-x11
sed -i 's|3.2|%{version}|g' version.json

ENGINEVER=`cat /usr/share/CuraEngine-lulzbot/version.json |grep engine`
URANIUMVER=`cat /usr/share/uranium-lulzbot/version.json | grep uranium`
CURAVER=`cat version.json |grep cura_version`
CURAGITVER=`git rev-parse HEAD`

cat > version.json.generated << EOF
{
$CURAVER,
  "cura": "$CURAGITVER",
$URANIUMVER,
$ENGINEVER,
  "libarcus": "Fedora system package",
  "libsavitar": "Fedora system package",
  "binarydata": "Built from source",
  "build": "$CURAGITVER"
}
EOF
mv version.json version.json.old
mv version.json.generated version.json

# The setup.py is only useful for py2exe, remove it, so noone is tempted to use it
rm setup.py

# fix icon pathing in desktop file
sed -i 's|/cura/resources|/cura-lulzbot/resources|g' cura-lulzbot.desktop.in

# Upstream installs to lib/python3/dist-packages
# We want to install to %%{python3_sitelib}
sed -i 's|lib/python${PYTHON_VERSION_MAJOR}/dist-packages|%(echo %{python3_sitelib} | sed -e s@%{_prefix}/@@)|g' CMakeLists.txt

# Wrong end of line encoding
dos2unix docs/How_to_use_the_flame_graph_profiler.md

# Wrong shebang
sed -i '1s=^#!/usr/bin/\(python\|env python\)3*=#!%{__python3}=' cura_app.py

# nuke weird invalid locales
rm -rf resources/i18n/jp resources/i18n/ptbr

%if 0
# Invalid locale name ptbr
# https://github.com/Ultimaker/Uranium/issues/246
mv resources/i18n/{ptbr,pt_BR}
sed -i 's/"Language: ptbr\n"/"Language: pt_BR\n"/' resources/i18n/pt_BR/*.po
# also jp
mv resources/i18n/{jp,ja}
sed -i 's/"Language: jp\n"/"Language: ja\n"/' resources/i18n/ja/*.po
%endif

%build
%{cmake} -DCURA_VERSION:STRING=%{version} .
make %{?_smp_mflags}

# rebuild locales
cd resources/i18n
rm *.pot
for DIR in *; do
  pushd $DIR
  for FILE in *.po; do
    msgfmt $FILE -o LC_MESSAGES/${FILE%po}mo || :
  done
  popd
done
cd -

%install
make install DESTDIR=%{buildroot}

cp -a version.json %{buildroot}%{_datadir}/%{shortname}

# Sanitize the location of locale files
pushd %{buildroot}%{_datadir}
mv %{shortname}/resources/i18n locale
ln -s ../../locale %{shortname}/resources/i18n
rm locale/*/*.po
for i in locale/*/LC_MESSAGES; do
	pushd $i
	mv cura.mo %{shortname}.mo
	if [ -f fdmextruder.def.json.mo ]; then
		mv fdmextruder.def.json.mo fdmextruder-lulzbot.def.json.mo
	fi
	if [ -f fdmprinter.def.json.mo ]; then
		mv fdmprinter.def.json.mo fdmprinter-lulzbot.def.json.mo
	fi
	popd
done

popd

# mv files to avoid conflict
mv %{buildroot}%{_datadir}/appdata/cura.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
mv %{buildroot}%{_datadir}/mime/packages/cura.xml %{buildroot}%{_datadir}/mime/packages/%{name}.xml

# remove git files
rm -rf %{buildroot}/usr/lib/%{shortname}/plugins/OctoPrintPlugin/.gitignore

# Bytecompile the plugins
%py_byte_compile %{__python3} %{buildroot}%{_prefix}/lib/%{shortname}

%find_lang %{shortname}
%find_lang fdmextruder-lulzbot.def.json
%find_lang fdmprinter-lulzbot.def.json


%check
%if 0
# The lulzbot's uranium (UM) module lives here:
export PYTHONPATH=%{python3_sitelib}/CuraLulzbot
%{__python3} -m pytest -v
desktop-file-validate %{buildroot}%{_datadir}/applications/%{shortname}.desktop
%endif


%files -f %{shortname}.lang -f fdmextruder-lulzbot.def.json.lang -f fdmprinter-lulzbot.def.json.lang
%license LICENSE
%doc README.md
# CHANGES is not updated since 15.x
# things in docs are developer orianted
%{python3_sitelib}/CuraLulzbot/cura
%{_datadir}/%{shortname}
%{_datadir}/applications/%{shortname}.desktop
%{_datadir}/appdata/%{shortname}.appdata.xml
%{_datadir}/mime/packages/%{shortname}.xml
%{_bindir}/cura-lulzbot
%{_prefix}/lib/%{shortname}

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:3.6.21-4
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.6.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Tom Callaway <spot@fedoraproject.org> - 1:3.6.21-2
- force cura-lulzbot to run in x11 mode
- disable unused call to platform.linux_distribution

* Mon Oct 21 2019 Tom Callaway <spot@fedoraproject.org> - 1:3.6.21-1
- update to 3.6.21

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1:3.6.18-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1:3.6.18-2
- Rebuilt for Python 3.8

* Fri Aug 16 2019 Tom Callaway <spot@fedoraproject.org> - 1:3.6.18-1
- update to 3.6.18

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.6.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Tom Callaway <spot@fedoraproject.org> 1:3.6.12-1
- update to 3.6.12

* Thu May  2 2019 Tom Callaway <spot@fedoraproject.org> 1:3.6.8-1
- update to 3.6.8

* Thu Apr 18 2019 Tom Callaway <spot@fedoraproject.org> 1:3.6.6-1
- update to 3.6.6

* Wed Mar 27 2019 Tom Callaway <spot@fedoraproject.org> 1:3.6.5-1
- update to 3.6.5

* Fri Mar  8 2019 Tom Callaway <spot@fedoraproject.org> 1:3.6.3-2
- add missing R:qt5-qtquickcontrols

* Wed Feb 20 2019 Tom Callaway <spot@fedoraproject.org> 1:3.6.3-1
- update to 3.6.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 16 2018 Tom Callaway <spot@fedoraproject.org> - 1:3.2.32-1
- update to 3.2.32

* Mon Jul 30 2018 Tom Callaway <spot@fedoraproject.org> - 1:3.2.23-1
- update to 3.2.23

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1:3.2.21-2
- Rebuilt for Python 3.7

* Wed May 23 2018 Tom Callaway <spot@fedoraproject.org> - 1:3.2.21-1
- update to 3.2.21

* Wed May 23 2018 Tom Callaway <spot@fedoraproject.org> - 1:3.2.20-1
- update to 3.2.20

* Wed May  9 2018 Tom Callaway <spot@fedoraproject.org> - 1:3.2.19-1
- update to 3.2.19

* Mon Apr 23 2018 Tom Callaway <spot@fedoraproject.org> - 1:3.2.18-1
- update to 3.2.18

* Mon Apr 16 2018 Tom Callaway <spot@fedoraproject.org> - 1:3.2.17-1
- update to 3.2.17

* Mon Apr 16 2018 Tom Callaway <spot@fedoraproject.org> - 1:2.6.69-2
- add PostProcessingPlugin

* Wed Mar 14 2018 Tom Callaway <spot@fedoraproject.org> - 1:2.6.69-1
- update to 2.6.69

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.6.66-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Tom Callaway <spot@fedoraproject.org> - 1:2.6.66-2
- fix japanese locale

* Wed Jan 17 2018 Tom Callaway <spot@fedoraproject.org> - 1:2.6.66-1
- update to 2.6.66

* Fri Jan 12 2018 Tom Callaway <spot@fedoraproject.org> - 1:2.6.63-2
- fix conflicting i18n files

* Wed Jan  3 2018 Tom Callaway <spot@fedoraproject.org> - 1:2.6.63-1
- update to 2.6.63

* Fri Dec  8 2017 Tom Callaway <spot@fedoraproject.org> - 1:2.6.52-1
- update to 2.6.52

* Fri Oct 27 2017 Tom Callaway <spot@fedoraproject.org> - 1:2.6.43-1
- update to 2.6.43

* Wed Oct 25 2017 Tom Callaway <spot@fedoraproject.org> - 1:2.6.29-1
- update to 2.6.29

* Wed Aug 23 2017 Tom Callaway <spot@fedoraproject.org> - 1:2.6.23-2
- fix system patch

* Wed Aug 23 2017 Tom Callaway <spot@fedoraproject.org> - 1:2.6.23-1
- update to 2.6.23

* Mon Aug 14 2017 Tom Callaway <spot@fedoraproject.org> - 1:2.6.22-1
- update to 2.6.22

* Tue Aug  8 2017 Tom Callaway <spot@fedoraproject.org> - 1:2.6.21-3
- use CuraEngine-lulzbot

* Tue Aug  8 2017 Tom Callaway <spot@fedoraproject.org> - 1:2.6.21-2
- fix namespacing to avoid conflicts (thanks to Miro Hrončok)

* Tue Aug  8 2017 Tom Callaway <spot@fedoraproject.org> - 1:2.6.21-1
- update to 2.6.21

* Thu Jul 27 2017 Tom Callaway <spot@fedoraproject.org> - 1:2.6.19-1
- lulzbot version (forked from Miro's spec)

* Thu Jul 20 2017 Miro Hrončok <mhroncok@redhat.com> - 1:2.6.1-2
- Require cura-fdm-materials

* Wed Jun 28 2017 Miro Hrončok <mhroncok@redhat.com> - 1:2.6.1-1
- Updated to 2.6.1

* Wed May 10 2017 Miro Hrončok <mhroncok@redhat.com> - 1:2.5.0-2
- Require qt5-qtquickcontrols

* Wed May 03 2017 Miro Hrončok <mhroncok@redhat.com> - 1:2.5.0-1
- Update to modern Cura 2.x (introduce Epoch) (#1393176)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 15.04.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 03 2016 Miro Hrončok <mhroncok@redhat.com> - 15.04.4-5
- Explicitly run cura on X11 GDK backend (#1388953)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.04.4-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Mar 25 2016 Miro Hrončok <mhroncok@redhat.com> - 15.04.4-3
- Require 3dprinter-udev-rules

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15.04.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 30 2016 Miro Hrončok <mhroncok@redhat.com> - 15.04.4-1
- New version

* Wed Jul 08 2015 Miro Hrončok <mhroncok@redhat.com> - 15.02.1-4
- No longer depend on pypy
- Simplify the launcher

* Mon Jul 06 2015 Miro Hrončok <mhroncok@redhat.com> - 15.02.1-3
- Patch for #1230281

* Mon Jul 06 2015 Miro Hrončok <mhroncok@redhat.com> - 15.02.1-2
- Require latest CuraEngine

* Mon Jul 06 2015 Miro Hrončok <mhroncok@redhat.com> - 15.02.1-1
- Update to 15.02.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.12.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Miro Hrončok <mhroncok@redhat.com> - 14.12.1-4
- Patch: Open directories with xdg-open (#1217961)

* Mon Apr 20 2015 Miro Hrončok <mhroncok@redhat.com> - 14.12.1-3
- Handle files from the command line (#1213220)

* Mon Mar 30 2015 Miro Hrončok <mhroncok@redhat.com> - 14.12.1-2
- Update the no firmware patch according to communication with Cura upstream

* Mon Dec 29 2014 Miro Hrončok <mhroncok@redhat.com> - 14.12.1-1
- Updated to 14.12.1
- No longer depend on firmware

* Sat Oct 25 2014 Miro Hrončok <mhroncok@redhat.com> - 14.09-1
- New version 14.09

* Tue Jun 24 2014 Miro Hrončok <mhroncok@redhat.com> - 14.06-2
- Require at least the firmware version originally bundled in git

* Mon Jun 23 2014 Miro Hrončok <mhroncok@redhat.com> - 14.06-1
- New version 14.06

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Dec 14 2013 Miro Hrončok <mhroncok@redhat.com> - 13.11.2-1
- New version 13.11.2

* Wed Oct 16 2013 Miro Hrončok <mhroncok@redhat.com> - 13.10-1
- New upstream release with CuraEngine

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 07 2013 Miro Hrončok <mhroncok@redhat.com> - 13.04-2
- Remove resources directory before trying to create a symlink there

* Sat May 04 2013 Miro Hrončok <mhroncok@redhat.com> - 13.04-1
- New upstream release
- Fixed missing slice module

* Sat Apr 20 2013 Miro Hrončok <mhroncok@redhat.com> - 13.03-1
- New upstream release

* Tue Feb 19 2013 Miro Hrončok <mhroncok@redhat.com> - 12.12-3
- chmod 755 cura-stripper.sh
- Use firmware from ultimaker-marlin-firmware package
- removed bundling note

* Sun Jan 20 2013 Miro Hrončok <mhroncok@redhat.com> - 12.12-2
- Launcher is in Python now

* Sun Jan 13 2013 Miro Hrončok <mhroncok@redhat.com> - 12.12-1
- First version

