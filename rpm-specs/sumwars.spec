%define __cmake_in_source_build 1

Name:           sumwars
Version:        0.5.8
Release:        23%{?dist}
Summary:        Hack and slash top-down view RPG game

# Also includes "nlfg" networking layer licensed as MIT,
# the effective license of GPLv3+ and MIT is GPLv3+
License:        GPLv3+
URL:            http://sumwars.org
Source0:        http://sourceforge.net/projects/sumwars/files/%{version}/%{name}-%{version}-src.tar.bz2
Source1:        sumwars.desktop
# Later versions of lua should still work
Patch0:         newer-lua.patch

BuildRequires:  gcc-c++
BuildRequires:  gettext, cmake, ogre-devel, cegui-devel, ois-devel, lua-devel,
BuildRequires:  libXrandr-devel, desktop-file-utils
BuildRequires:  freealut-devel, libogg-devel, libvorbis-devel, physfs-devel
BuildRequires:  tinyxml-devel, enet-devel

# Needed to automate finding font paths at build time
%global fonts font(dejavusans) font(dejavuserif)
BuildRequires: fontconfig %{fonts}

# runtime plugin, doesn't get picked up automatically
Requires:       cegui-libxml-xmlparser
Requires:       %{name}-data = %{version}

%description
Summoning Wars is an open source role-playing game, featuring both
a single-player and a multiplayer mode for about 2 to 8 players. 

%package data
Summary:        %{summary}
Requires:       %{name} = %{version}
BuildArch:      noarch
License:        CC-BY-SA

Requires:       %{fonts}

%description data
This package contains the data files for Summoning Wars.

%prep
%setup -q
%patch0

rm -rf src/enet
rm -rf src/tinyxml
rm -rf tools/*

%build
# we don't build developer tools into the application as users won't need that
# do not use the bundled TinyXML, use the system one
# do not use the bundled enet, use the system one

%cmake -DSUMWARS_BUILD_TOOLS:BOOL=OFF -DSUMWARS_NO_TINYXML:BOOL=ON -DSUMWARS_NO_ENET:BOOL=ON

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

# remove bundled but unused OgreCore.zip
rm $RPM_BUILD_ROOT/%{_datadir}/%{name}/resources/packs/OgreCore.zip

# use system-wide dejavu sans and serif fonts
ln -f -s $(fc-match -f "%{file}" "sans") \
        $RPM_BUILD_ROOT/%{_datadir}/%{name}/resources/gui/fonts/DejaVuSans.tt
ln -f -s $(fc-match -f "%{file}" "serif") \
        $RPM_BUILD_ROOT/%{_datadir}/%{name}/resources/gui/fonts/DejaVuSerif.ttf

# upstream doesn't want to install .desktop file and icons because distros
# keep them at different locations, lets install both manually

for i in 16 24 32 48 64 128
do
    install -D "share/icon/SumWarsIcon_${i}x${i}.png" \
        "$RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png"
done

desktop-file-install --dir $RPM_BUILD_ROOT/%{_datadir}/applications \
                     --mode="0644" \
                     %{SOURCE1}

# move docs to an unversioned directory
mv $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version} $RPM_BUILD_ROOT/%{_docdir}/%{name}

%files
%doc COPYING AUTHORS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%dir %{_datadir}/%{name}/translation/
%lang(de) %{_datadir}/%{name}/translation/de/
%lang(en) %{_datadir}/%{name}/translation/en/
%lang(es) %{_datadir}/%{name}/translation/es/
%lang(it) %{_datadir}/%{name}/translation/it/
%lang(pl) %{_datadir}/%{name}/translation/pl/
%lang(pt) %{_datadir}/%{name}/translation/pt/
%lang(ru) %{_datadir}/%{name}/translation/ru/
%lang(uk) %{_datadir}/%{name}/translation/uk/

%files data
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/data/
%{_datadir}/%{name}/resources/

%changelog
* Tue Sep 22 2020 Jeff Law <law@redhat.com> - 0.5.8-23
- Use cmake_in_source_build to fix FTBFS due to recent cmake macro changes

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-22
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 13 2020 Bruno Wolff III <bruno@wolff.to> = 0.5.8-20
- Automate finding fonts at build time
- Work with more recent versions of lua

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.8-14
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 0.5.8-11
- Rebuilt for Boost 1.64

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Jonathan Wakely <jwakely@redhat.com> - 0.5.8-9
- Rebuilt for Boost 1.63

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.5.8-7
- Rebuilt for Boost 1.59

* Wed Aug 05 2015 Jonathan Wakely <jwakely@redhat.com> 0.5.8-6
- Rebuilt for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 23 2015 Bruno Wolff III <bruno@wolff.to> - 0.5.8-4
- Rebuild for rebuilt Ogre

* Thu Feb 05 2015 Martin Preisler <mpreisle@redhat.com> - 0.5.8-3
- Rebuilt because of boost update

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 18 2014 Martin Preisler <mpreisle@redhat.com> - 0.5.8-1
- Updated to 0.5.8

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 0.5.6-18
- rebuild for boost 1.55.0

* Wed Apr 30 2014 Martin Preisler <mpreisle@redhat.com> - 0.5.6-17
- Rebuild for enet 1.3.12 soname bump

* Wed Aug 21 2013 Martin Preisler <mpreisle@redhat.com> - 0.5.6-16
- Patch from upstream regarding Lua >= 5.2
- Unversioned docs related patch

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 29 2013 Petr Machata <pmachata@redhat.com> - 0.5.6-14
- Rebuild for boost 1.54.0

* Sat Jun 15 2013 Bruno Wolff III <bruno@wolff.to> - 0.5.6-13
- Rebuild for enet 1.3.8 soname bump

* Sat Apr 27 2013 Bruno Wolff III <bruno@wolff.to> - 0.5.6-12
- Rebuild for enet 1.3.7 soname bump

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.5.6-11
- Rebuild for Boost-1.53.0

* Wed Jan 23 2013 Bruno Wolff III <bruno@wolff.to> - 0.5.6-10
- Rebuild for cegui soname bump

* Wed Dec 05 2012 Martin Preisler <mpreisle@redhat.com> - 0.5.6-9
- Rebuilt for Ogre 1.8.1

* Thu Nov 15 2012 Tom Callaway <spot@fedoraproject.org> - 0.5.6-8
- rebuild for new cegui
- apply patch to use -lpthread
- apply patch to find and use Boost (system)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 01 2012 Bruno Wolff III <bruno@wolff.to> 0.5.6-6
- Rebuild for ogre 1.7.4

* Mon Mar 19 2012 Martin Preisler <mpreisle@redhat.com> 0.5.6-5
- removed rm -rf $RPM_BUILD_ROOT from %%install
- moved icons and desktop file back to the base package

* Fri Mar 16 2012 Martin Preisler <mpreisle@redhat.com> 0.5.6-4
- ensure consistent usage of %%{name}
- use 80 characters per line where possible

* Wed Mar 14 2012 Martin Preisler <mpreisle@redhat.com> 0.5.6-3
- separate License fields for main package and the data subpackage
- moved dejavu font Requires to data

* Wed Mar 14 2012 Martin Preisler <mpreisle@redhat.com> 0.5.6-2
- use system TinyXML and enet
- remove unused OgreCore.zip
- desktop file reworked
- use system dejavu-{sans,serif}

* Wed Mar 07 2012 Martin Preisler <mpreisle@redhat.com> 0.5.6-1
- new package

