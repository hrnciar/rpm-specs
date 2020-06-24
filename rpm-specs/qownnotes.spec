%global commit  b669baa1fd6b1c870b4872d31aef6e0e27660124
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date    20200618

# Git submodules
%global qmarkdowntextedit_commit        4f7ac9ede16e159499ef0178bee5b5a451e69a13
%global qmarkdowntextedit_shortcommit   %(c=%{qmarkdowntextedit_commit}; echo ${c:0:7})

%global qttoolbareditor_commit          612029c45b7b6c38be8ffe7c600ae6a10edb9006
%global qttoolbareditor_shortcommit     %(c=%{qttoolbareditor_commit}; echo ${c:0:7})

%global qtcsv_commit                    db3e9a816d91a4773b61312cafa25eff4ddec91c
%global qtcsv_shortcommit               %(c=%{qtcsv_commit}; echo ${c:0:7})

%global fakevim_commit                  46f14b0cb56dee2cba22c13b4e0652d5e2c69bbf
%global fakevim_shortcommit             %(c=%{fakevim_commit}; echo ${c:0:7})

%global piwiktracker_commit             e3ae5a4b4ee036c0c8d7cc000411995278dec6ab
%global piwiktracker_shortcommit        %(c=%{piwiktracker_commit}; echo ${c:0:7})

%global qkeysequencewidget_commit       928690d341058209a2c1a5d8df97e1aca229c4c3
%global qkeysequencewidget_shortcommit  %(c=%{qkeysequencewidget_commit}; echo ${c:0:7})

%global md4c_commit                     d9fa2f1303e9870fac83977025271991fc775d9e
%global md4c_shortcommit                %(c=%{md4c_commit}; echo ${c:0:7})

%global qhotkey_commit                  64a2ee5c6d619250cf9ab930889bc7c0b62c9c75
%global qhotkey_shortcommit             %(c=%{qhotkey_commit}; echo ${c:0:7})


%global appname QOwnNotes
%global url1    https://github.com/pbek

Name:           qownnotes
Version:        20.6.7
Release:        1.%{date}git%{shortcommit}%{?dist}
Summary:        Plain-text file markdown note taking with Nextcloud integration

# The entire source code is MIT except bundled libs:
# BSD:          qdarkstyle
#               qkeysequencewidget
#               qmarkdowntextedit
#               singleapplication
#               simplecrypt
# MIT:          piwiktracker
#               md4c
# GPLv2         versionnumber
# GPLv3+        qttoolbareditor
# LGPLv2+       fakevim
# ASL 2.0       diff_match_patch
License:        MIT and BSD and GPLv2 and GPLv3+ and LGPLv2+ and ASL 2.0
URL:            https://www.qownnotes.org
Source0:        %{url1}/QOwnNotes/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        %{url1}/qmarkdowntextedit/archive/%{qmarkdowntextedit_commit}/qmarkdowntextedit-%{qmarkdowntextedit_shortcommit}.tar.gz
Source2:        %{url1}/Qt-Toolbar-Editor/archive/%{qttoolbareditor_commit}/qttoolbareditor-%{qttoolbareditor_shortcommit}.tar.gz
Source3:        %{url1}/qtcsv/archive/%{qtcsv_commit}/qtcsv-%{qtcsv_shortcommit}.tar.gz
Source4:        %{url1}/FakeVim/archive/%{fakevim_commit}/fakevim-%{fakevim_shortcommit}.tar.gz
Source5:        %{url1}/qt-piwik-tracker/archive/%{piwiktracker_commit}/piwiktracker-%{piwiktracker_shortcommit}.tar.gz
Source6:        %{url1}/qkeysequencewidget/archive/%{qkeysequencewidget_commit}/qkeysequencewidget-%{qkeysequencewidget_shortcommit}.tar.gz
Source7:        https://github.com/%{name}/md4c/archive/%{md4c_commit}/md4c-%{md4c_shortcommit}.tar.gz
Source8:        https://github.com/%{name}/QHotkey/archive/%{qhotkey_commit}/qhotkey-%{qhotkey_shortcommit}.tar.gz

BuildRequires:  cmake3
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5WebSockets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5XmlPatterns)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib

# Switch to 'botan2'
# * https://github.com/pbek/QOwnNotes/issues/1263
%if 0%{?fedora} >= 32
BuildRequires:  pkgconfig(botan-2) >= 2.12.0
%endif

Requires:       hicolor-icon-theme
Requires:       qt5-qtbase%{?_isa}

Recommends:     %{name}-translations = %{version}-%{release}

Provides:       bundled(fakevim) = 0.0.1
Provides:       bundled(md4c) = 0.4.2~git%{md4c_shortcommit}
Provides:       bundled(qhotkey) = 1.3.0~git%{qhotkey_commit}
Provides:       bundled(qkeysequencewidget) = 1.0.1
Provides:       bundled(qmarkdowntextedit) = 2019.4.0~git%{qmarkdowntextedit_shortcommit}
Provides:       bundled(qt-piwik-tracker) = 0~git%{piwiktracker_shortcommit}
Provides:       bundled(qt-toolbar-editor) = 0~git%{qttoolbareditor_shortcommit}
Provides:       bundled(qtcsv) = 1.2.2

%if 0%{?fedora} < 32
Provides:       bundled(botan) = 2.12.0
%endif

%description
QOwnNotes is the open source notepad with markdown support and todo list manager
for GNU/Linux, Mac OS X and Windows, that works together with the default notes
application of ownCloud and Nextcloud.

You are able to write down your thoughts with QOwnNotes and edit or search for
them later from your mobile device, like with CloudNotes or the
ownCloud/Nextcloud web-service.

The notes are stored as plain text files and are synced with
ownCloud's/Nextcloud's file sync functionality. Of course other software, like
Syncthing or Dropbox can be used too.

I like the concept of having notes accessible in plain text files, like it is
done in the ownCloud/Nextcloud notes apps, to gain a maximum of freedom, but I
was not able to find a decent desktop note taking tool or a text editor, that
handles them well. Out of this need QOwnNotes was born.


%package        translations
Summary:        Translations files for %{name}
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}

%description    translations
Translations files for %{name}.


%prep
%autosetup -n %{appname}-%{commit} -p1
%autosetup -n %{appname}-%{commit} -D -T -a1
%autosetup -n %{appname}-%{commit} -D -T -a2
%autosetup -n %{appname}-%{commit} -D -T -a3
%autosetup -n %{appname}-%{commit} -D -T -a4
%autosetup -n %{appname}-%{commit} -D -T -a5
%autosetup -n %{appname}-%{commit} -D -T -a6
%autosetup -n %{appname}-%{commit} -D -T -a7
%autosetup -n %{appname}-%{commit} -D -T -a8

mv qmarkdowntextedit-%{qmarkdowntextedit_commit}/*      src/libraries/qmarkdowntextedit/
mv Qt-Toolbar-Editor-%{qttoolbareditor_commit}/*        src/libraries/qttoolbareditor/
mv qtcsv-%{qtcsv_commit}/*                              src/libraries/qtcsv/
mv FakeVim-%{fakevim_commit}/*                          src/libraries/fakevim/
mv qt-piwik-tracker-%{piwiktracker_commit}/*            src/libraries/piwiktracker/
mv qkeysequencewidget-%{qkeysequencewidget_commit}/*    src/libraries/qkeysequencewidget/
mv md4c-%{md4c_commit}/*                                src/libraries/md4c/
mv QHotkey-%{qhotkey_commit}/*                          src/libraries/qhotkey/
mkdir -p src/%{_target_platform}


%build
# Build translations
# * https://github.com/pbek/QOwnNotes/issues/1744
lrelease-qt5 src/%{appname}.pro

pushd src/%{_target_platform}
%qmake_qt5 \
    PREFIX=%{buildroot}%{_prefix} \
    %if 0%{?fedora} >= 32
    USE_SYSTEM_BOTAN=1 \
    %endif
    ..
popd
%make_build -C src/%{_target_platform}


%install
%make_install -C src/%{_target_platform}
install -m 0644 -Dp obs/%{name}.appdata.xml %{buildroot}/%{_metainfodir}/%{name}.appdata.xml
%find_lang %{appname} --with-qt


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{appname}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_metainfodir}/*.xml

%files -f %{appname}.lang translations
%{_datadir}/qt5/translations/%{appname}_ceb.qm
%{_datadir}/qt5/translations/%{appname}_fil.qm
%{_datadir}/qt5/translations/%{appname}_hil.qm


%changelog
* Fri Jun 19 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 20.6.7-1.20200618gitb669baa
- Update to 20.6.7

* Thu May 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 20.5.10-1.20200518gitcaa6d48
- Update to 20.5.10
- Add new submodule 'qhotkey'
- Add new BR: Qt5X11Extras
- Translations now compiles from sources | GH-1744
- Disable LTO

* Sat Mar 28 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 20.3.7-1.20200328git7fe3aa6
- Update to 20.3.7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.1.11-2.20200119gitadec18b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 20.1.11-1.20200119gitadec18b
- Update to 20.1.11
- Add new submodule 'md4c'
- Enable LTO

* Tue Sep 17 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 19.9.12-2.20190912gitc33c89f
- Update to 19.9.12
- Remove ExcludeArches: s390x ppc64le
- Switch to botan2: https://github.com/pbek/QOwnNotes/issues/1263

* Sun Sep 08 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 19.9.5-1.20190905gitf62ac68
- Update to 19.9.5

* Sat Aug 10 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.8.4-7.20190810git0302b2c
- Initial package
- Thanks to Dead_Mozay <dead_mozay@opensuse.org> for initial spec file
