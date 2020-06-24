Name:		qmpdclient
Version:	1.2.2
Release:	19%{?dist}
Summary:	Qt4 based MPD client

License:	GPLv2+
URL:		http://bitcheese.net/wiki/QMPDClient
Source0:	http://dump.bitcheese.net/files/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop

BuildRequires:	qt4-devel qt4-webkit-devel
BuildRequires:	desktop-file-utils
BuildRequires:	cmake


%description
Qt4 based MPD client which supports:
* Covers
* Lyrics
* Tag guessing
* Internet radio
* Storing & using playlists
* Last.fm track submission
* Tray notification
* Skinnable interface
* OSD

%prep
%setup -q -n %{name}


%build
%{cmake}
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

# Add an icon for the menu system
install -Dpm 644 icons/svg/%{name}.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -Dpm 644 icons/64x64/%{name}.png %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

desktop-file-install					\
	--dir %{buildroot}/%{_datadir}/applications	\
	%{SOURCE1}


%files
%dir %{_datadir}/QMPDClient
%dir %{_datadir}/QMPDClient/translations
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png

%doc AUTHORS COPYING THANKSTO README Changelog

%lang(cs_CZ) %{_datadir}/QMPDClient/translations/cs_CZ.qm
%lang(de_DE) %{_datadir}/QMPDClient/translations/de_DE.qm
%lang(es_ES) %{_datadir}/QMPDClient/translations/es_ES.qm
%lang(fr_FR) %{_datadir}/QMPDClient/translations/fr_FR.qm
%lang(it_IT) %{_datadir}/QMPDClient/translations/it_IT.qm
%lang(nl_NL) %{_datadir}/QMPDClient/translations/nl_NL.qm
%lang(nn_NO) %{_datadir}/QMPDClient/translations/nn_NO.qm
%lang(no_NO) %{_datadir}/QMPDClient/translations/no_NO.qm
%lang(pt_BR) %{_datadir}/QMPDClient/translations/pt_BR.qm
%lang(ru_RU) %{_datadir}/QMPDClient/translations/ru_RU.qm
%lang(sv_SE) %{_datadir}/QMPDClient/translations/sv_SE.qm
%lang(tr_TR) %{_datadir}/QMPDClient/translations/tr_TR.qm
%lang(uk_UA) %{_datadir}/QMPDClient/translations/uk_UA.qm
%lang(zh_CN) %{_datadir}/QMPDClient/translations/zh_CN.qm
%lang(zh_TW) %{_datadir}/QMPDClient/translations/zh_TW.qm

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.2-14
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2.2-8
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Aug 20 2011 Julian Golderer <j.golderer@novij.at> 1.2.2-1
- Version Bump 1.2.2

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 09 2010 Julian Golderer <j.golderer@novij.at> 1.2-1
- Version Bump 1.2
- Removed %%clean section

* Sat Jun 05 2010 Julian Golderer <j.golderer@novij.at> 1.1.3-3
- Fixed #599797 - ImplicitDSOLinking
- Removed Category 'Music' from desktop file

* Mon May 10 2010 Julian Golderer <j.golderer@novij.at> 1.1.3-2
- Source url refers to updated upstream destination now

* Mon May 10 2010 Julian Golderer <j.golderer@novij.at> 1.1.3-1
- Version Bump 1.1.3

* Tue Feb 02 2010 Julian Golderer <j.golderer@novij.at> 1.1.2-4
- Changed to CMake
- Added language files

* Thu Jan 21 2010 Julian Golderer <j.golderer@novij.at> 1.1.2-3
- Dropped qt dependency
- Desktop file: removed category X-Fedora
- Removed desktop file validation
- New way to update icon cache
- Install hicolor 64x64 png icon
- Modified patch for project file

* Sat Jan 16 2010 Julian Golderer <j.golderer@novij.at> 1.1.2-2
- Modified patch for project file

* Tue Nov 17 2009 Julian Golderer <j.golderer@novij.at> 1.1.2-1
- Version Bump 1.1.2

* Thu Oct 15 2009 Julian Golderer <j.golderer@novij.at> 1.1.1-4
- Fixed Debuginfo

* Thu Oct 08 2009 Julian Golderer <j.golderer@novij.at> 1.1.1-3
- Filled doc tag
- Consistently use of macros

* Thu Oct 01 2009 Julian Golderer <j.golderer@novij.at> 1.1.1-2
- Fixed Changlog entry
- Replaced paths by macros
- Removed empty doc tag
- Set group to Applications/Multimedia
- Source0 is a url now
- Replaced spaces by tabs

* Sun Jul 19 2009 Julian Golderer <j.golderer@novij.at> 1.1.1-1
- Created base spec file