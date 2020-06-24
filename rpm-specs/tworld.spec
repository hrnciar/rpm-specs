Name:	 tworld
%global fullname Tile World

Version: 1.3.2
Release: 13%{?dist}
Summary: Intellectually engaging puzzle game

License: GPLv2+
URL:     http://www.muppetlabs.com/~breadbox/software/tworld/
Source0: http://www.muppetlabs.com/~breadbox/pub/software/tworld/tworld-%{version}-CCLPs.tar.gz	

Source1: tworld-icon-16px.png
Source2: tworld-icon-32px.png
Source3: tworld-icon-48px.png
Source4: tworld.desktop
Source5: tworld.appdata.xml

BuildRequires: gcc SDL SDL-devel
BuildRequires: desktop-file-utils libappstream-glib
Requires: filesystem hicolor-icon-theme
Requires: %{name}-cclp = %{version}-%{release}
Requires: %{name}-data = %{version}-%{release}

%description
%{fullname} is a game made up of both intellectually engaging puzzles
and situations demanding fast reflexes. The object of each level
is simply to get out — i.e., to find and achieve the exit tile.
This simple task, however, can sometimes be extremely challenging.


%package data
Summary: Data files for %{name}
BuildArch: noarch


%description data
Data files (graphics, sounds) required to play %{fullname}.


%package cclp
Summary: Level packs for %{name}
License: Redistributable, no modification permitted
BuildArch: noarch
Requires: %{name}-data = %{version}-%{release}


%description cclp
Community-created level packs for %{fullname}.


%prep
%setup -q
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .
cp -p %{SOURCE3} .
cp -p %{SOURCE4} .
cp -p %{SOURCE5} .


%build
%configure
make %{?_smp_mflags} prefix=%{_prefix}


%install
make install prefix=%{buildroot}%{_prefix} bindir=%{buildroot}%{_bindir} mandir=%{buildroot}%{_mandir}

install -m 755 -d %{buildroot}%{_datadir}/applications/
desktop-file-install  --dir=%{buildroot}%{_datadir}/applications/  %{name}.desktop

appstream-util validate-relax --nonet tworld.appdata.xml
install -m 755 -d %{buildroot}%{_datadir}/appdata/
install -m 644 -p tworld.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

for SIZE in 16 32 48; do
  install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/apps/
  install -m 644 -p \
    tworld-icon-${SIZE}px.png \
    %{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/apps/%{name}.png
done


cp -a CCLPs %{buildroot}%{_datadir}/%{name}/
cat > %{buildroot}%{_datadir}/%{name}/sets/CCLP2-MS.dac <<EOF
file=CCLP2.dat
lastlevel=149
ruleset=ms
EOF


%files
%doc README BUGS docs/tworld.html
%license COPYING
%{_bindir}/%{name}
%{_mandir}/*/%{name}.*
%{_datadir}/appdata/%{name}.*
%{_datadir}/applications/%{name}.*
%{_datadir}/icons/hicolor/*/apps/%{name}.*


%files data
%license COPYING
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/data
     %{_datadir}/%{name}/data/intro.dat
%dir %{_datadir}/%{name}/sets
     %{_datadir}/%{name}/sets/cc*.dac
     %{_datadir}/%{name}/sets/intro*.dac
%{_datadir}/%{name}/res


%files cclp
%docdir %{_datadir}/%{name}/CCLPs
        %{_datadir}/%{name}/CCLPs
%{_datadir}/%{name}/data/CCLP*.dat
%{_datadir}/%{name}/sets/CCLP*.dac


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 28 2018 Artur Iwicki <fedora@svgames.pl> - 1.3.2-9
- Add missing BuildRequires: for gcc
- Use a loop for installing icons instead of repeating the lines several times

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 20 2018 Artur Iwicki <fedora@svgames.pl> 1.3.2-7
- Actually remove the scriplets instead of just writing a changelog entry

* Sun Jan 20 2018 Artur Iwicki <fedora@svgames.pl> 1.3.2-6
- Remove obsolete scriptlets (updating icon cache for hicolor-icon-theme)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Artur Iwicki <fedora@svgames.pl> 1.3.2-3
- Fix license tags in appdata file
- Add dependency on hicolor-icon-theme
- Remove unnecessary slashes after buildroot macro in install section

* Sat Jun 17 2017 Artur Iwicki <fedora@svgames.pl> 1.3.2-2
- Move the level packs out of -data into a -cclp subpackage
- Add a .dac file that enables the CCLP2 level pack
- Add icons and a .desktop file
- Add an .appdata.xml file

* Fri Jun 16 2017 Artur Iwicki <fedora@svgames.pl> 1.3.2-1
- Initial packaging
