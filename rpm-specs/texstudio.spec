Name:           texstudio
Version:        3.0.1
Release:        2%{?dist}

Summary:        A feature-rich editor for LaTeX documents
# texstudio binary: GPLv3 due to static linkage of bundled qcodeedit
# texstudio data and image files: GPLv2+
License:        GPLv2+ and GPLv3
URL:            https://www.texstudio.org

Source0:        https://github.com/texstudio-org/texstudio#/archive/%{name}-%{version}.tar.gz
Source1:        texstudio.desktop
Patch1:         texstudio-use-system-qtsingleapplication-instead-of-bundled-on.patch
Patch2:         texstudio-disable-update-check.patch
# don't muck with default build flags
Patch3:         texstudio-wtf_flags.patch

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qttools-static
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  hunspell-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  poppler-qt5-devel
BuildRequires:  qtsingleapplication-qt5-devel
BuildRequires:  qtsinglecoreapplication-qt5-devel
BuildRequires:  qtermwidget-devel
BuildRequires:  quazip-qt5-devel
BuildRequires:  zlib-devel

Requires:       tex(latex)
Requires:       tex(preview.sty)
Requires:       tex-dvipng
Requires:       qt5-qtsvg
Requires:       qterm
Provides:       bundled(qcodeedit) 
Provides:       texmakerx = %{version}-%{release}
Obsoletes:      texmakerx < 2.2-1
%description
TeXstudio, formerly known as TexmakerX is a fork of the 
LaTeX IDE TexMaker and gives you an environment where you can 
easily create and manage LaTeX documents.
It provides modern writing support, like interactive spell checking, 
code folding and syntax highlighting. 
Also it serves as a starting point from where you can easily run 
all necessary LaTeX tools.
Although TeXstudio has a lot of additional features, 
it tries to be like an improved version of Texmaker, 
so it keeps it look&feel.

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1 -b .qtsingle
%patch2 -p1 -b .update_check
%patch3 -p1 -b .wtf_flags

rm -rf {hunspell,qtsingleapplication,quazip}

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{qmake_qt5} \
%ifnarch %{ix86} x86_64 %{arm}
    NO_CRASH_HANDLER=1 \
%endif
    USE_SYSTEM_HUNSPELL=1 \
    USE_SYSTEM_QTSINGLEAPPLICATION=1 \
    INTERNAL_TERMINAL=1 \
    USE_SYSTEM_QUAZIP=1 QUAZIP_LIB=-lquazip5 QUAZIP_INCLUDE=%{_includedir}/quazip5/ \
    ../texstudio.pro
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install INSTALL_ROOT=$RPM_BUILD_ROOT -C %{_target_platform}

install -Dp -m 0644 utilities/texstudio16x16.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/texstudio.png
install -Dp -m 0644 utilities/texstudio22x22.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/22x22/apps/texstudio.png
install -Dp -m 0644 utilities/texstudio32x32.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/texstudio.png
install -Dp -m 0644 utilities/texstudio48x48.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/texstudio.png
install -Dp -m 0644 utilities/texstudio64x64.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/46x46/apps/texstudio.png


rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/{AUTHORS,COPYING,*.desktop,tex*.png,CHANGELOG.txt}
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/{*.dic,*.aff}
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/qt_*.qm

%find_lang %{name} --with-qt

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

%files -f %{name}.lang
%{_bindir}/texstudio
%dir %{_datadir}/texstudio/
%{_datadir}/texstudio/*.png
%{_datadir}/texstudio/usermanual.css
%{_datadir}/texstudio/latex2e.*
%{_datadir}/texstudio/*.stopWords
%{_datadir}/texstudio/*.stopWords.level2
%{_datadir}/texstudio/de_DE.badWords
%{_datadir}/texstudio/template_*.tex
%{_datadir}/texstudio/template_*.zip
%{_datadir}/texstudio/*.json
%{_datadir}/texstudio/*.js
%{_datadir}/texstudio/th_*.dat
%{_datadir}/texstudio/usermanual_*.html
%{_datadir}/applications/texstudio.desktop
%{_datadir}/metainfo/texstudio.appdata.xml
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg

%doc utilities/AUTHORS utilities/COPYING utilities/manual/CHANGELOG.txt

%changelog
* Sun Sep 06 2020 Johannes Lips <hannes@fedoraproject.org> 3.0.1-2
- enabled internal terminal

* Wed Sep 02 2020 Johannes Lips <hannes@fedoraproject.org> 3.0.1-1
- Update to latest upstream release 3.0.1

* Tue Aug 25 2020 Johannes Lips <hannes@fedoraproject.org> 3.0.0-1
- Update to latest upstream release 3.0.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Johannes Lips <hannes@fedoraproject.org> 2.12.22-1
- Update to latest upstream bugfix release 2.12.22

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> 2.12.20-2
- Rebuild for poppler-0.84.0

* Tue Jan 14 2020 Johannes Lips <hannes@fedoraproject.org> 2.12.20-1
- Update to latest upstream bugfix release 2.12.20

* Thu Dec 26 2019 Johannes Lips <hannes@fedoraproject.org> 2.12.18-1
- Update to latest upstream bugfix release 2.12.18

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 19 2019 Johannes Lips <hannes@fedoraproject.org> 2.12.16-1
- Update to latest upstream bugfix release 2.12.16
- added qt5-qtsvg as requires to fix bug #1716129

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 03 2018 Johannes Lips <hannes@fedoraproject.org> 2.12.14-1
- Update to latest upstream bugfix release 2.12.14

* Mon Nov 26 2018 Johannes Lips <hannes@fedoraproject.org> 2.12.12-1
- Update to latest upstream bugfix release 2.12.12

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Johannes Lips <hannes@fedoraproject.org> 2.12.10-1
- Update to latest upstream bugfix release 2.12.10

* Thu May 17 2018 Johannes Lips <hannes@fedoraproject.org> 2.12.8-7
- fixing the texlive dependencies

* Thu May 17 2018 Johannes Lips <hannes@fedoraproject.org> 2.12.8-6
- fixing the texlive dependencies

* Wed May 16 2018 Johannes Lips <hannes@fedoraproject.org> 2.12.8-5
- fixing the texlive dependencies

* Wed May 02 2018 Johannes Lips <hannes@fedoraproject.org> 2.12.8-4
- rebuild for f28 tag

* Fri Mar 23 2018 Marek Kasik <mkasik@redhat.com> 2.12.8-3
- Rebuild for poppler-0.63.0

* Tue Feb 20 2018 Johannes Lips <hannes@fedoraproject.org> 2.12.8-2
- added missing deps for bug #1540362

* Sun Feb 11 2018 Johannes Lips <hannes@fedoraproject.org> 2.12.8-1
- Update to latest upstream bugfix release 2.12.8

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.12.6-3
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Johannes Lips <hannes@fedoraproject.org> 2.12.6-1
- Update to latest upstream bugfix release 2.12.6

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue Mar 28 2017 Johannes Lips <hannes@fedoraproject.org> 2.12.4-1
- Update to latest upstream bugfix release 2.12.4

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Johannes Lips <hannes@fedoraproject.org> 2.12.2-1
- Update to latest upstream bugfix release 2.12.2

* Fri Jan 20 2017 Christian Dersch <lupinix@mailbox.org> - 2.12.0-2
- Added patch to fix command detection

* Sat Jan 07 2017 Johannes Lips <hannes@fedoraproject.org> 2.12.0-1
- Update to latest upstream bugfix release 2.12.0

* Tue Dec 13 2016 Caolán McNamara <caolanm@redhat.com> - 2.11.2-4
- rebuild for hunspell 1.5.4

* Thu Dec 08 2016 Christian Dersch <lupinix@mailbox.org> - 2.11.2-3
- rebuilt against qt5-qtbase-5.7.1-9 fixing issues with QT_VERSION macros

* Thu Dec 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.11.2-2
- support out-of-tree builds
- set USE_SYSTEM_HUNSPELL USE_SYSTEM_QUAZIP USE_SYSTEM_QTSINGLEAPPLICATION

* Wed Oct 12 2016 Johannes Lips <hannes@fedoraproject.org> 2.11.2-1
- Update to latest upstream bugfix release 2.11.2

* Mon May 30 2016 Johannes Lips <hannes@fedoraproject.org> 2.11.0-1
- Update to latest upstream bugfix release 2.11.0

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> 2.10.8-2
- use %%qmake_qt5 to ensure proper build flags

* Sun Jan 24 2016 Johannes Lips <hannes@fedoraproject.org> 2.10.8-1
- Update to latest upstream bugfix release 2.10.8

* Tue Jan 12 2016 Johannes Lips <hannes@fedoraproject.org> 2.10.6-1
- Update to latest upstream bugfix release 2.10.6

* Wed Dec 16 2015 Johannes Lips <hannes@fedoraproject.org> 2.10.4-2
- added patch to disable update check

* Tue Oct 27 2015 Johannes Lips <hannes@fedoraproject.org> 2.10.4-1
- Update to latest upstream bugfix release 2.10.4

* Thu Sep 17 2015 Johannes Lips <hannes@fedoraproject.org> 2.10.2-1
- Update to latest upstream bugfix release 2.10.2

* Fri Sep 11 2015 Johannes Lips <hannes@fedoraproject.org> 2.10.0-1
- Update to latest upstream version 2.10.0
- added patch to fix arm build #1262987

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 24 2015 Johannes Lips <hannes@fedoraproject.org> 2.9.4-3
- add qtsingleapplication patch - using fedora version

* Sat Apr 25 2015 Johannes Lips <hannes@fedoraproject.org> 2.9.4-2
- switch to building with Qt5
- removed qtsingleapplication patch - using bundled one

* Tue Mar 24 2015 Johannes Lips <hannes@fedoraproject.org> 2.9.4-1
- Update to latest upstream version 2.9.4

* Mon Mar 23 2015 Johannes Lips <hannes@fedoraproject.org> 2.9.2-1
- Update to latest upstream version 2.9.2

* Mon Mar 09 2015 Johannes Lips <hannes@fedoraproject.org> 2.9.0-1
- Update to latest upstream version 2.9.0
- changelog cleaned up

* Sun Dec 07 2014 Johannes Lips <hannes@fedoraproject.org> 2.8.8-1
- Update to latest upstream version 2.8.8

* Tue Nov 04 2014 Johannes Lips <hannes@fedoraproject.org> 2.8.6-1
- Update to latest upstream version 2.8.6

* Tue Sep 09 2014 Johannes Lips <hannes@fedoraproject.org> 2.8.4-1
- Update to latest upstream version 2.8.4

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 26 2014 Johannes Lips <hannes@fedoraproject.org> 2.8.2-1
- Update to latest upstream version 2.8.2

* Fri Jun 20 2014 Johannes Lips <hannes@fedoraproject.org> 2.8.0-1
- Update to latest upstream version 2.8.0

* Wed Mar 19 2014 Johannes Lips <hannes@fedoraproject.org> 2.7.0-1
- Update to latest upstream version 2.7.0

* Sun Nov 03 2013 Johannes Lips <hannes@fedoraproject.org> 2.6.6-1
- Update to latest upstream version 2.6.6

* Sat Nov 02 2013 Johannes Lips <hannes@fedoraproject.org> 2.6.4-1
- Update to latest upstream version 2.6.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Johannes Lips <hannes@fedoraproject.org> 2.6.2-1
- Update to latest upstream version 2.6.2

* Sun Jun 16 2013 Johannes Lips <hannes@fedoraproject.org> 2.6.0-1
- Update to latest upstream version 2.6.0

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 11 2013 Johannes Lips <hannes@fedoraproject.org> 2.5.2-1
- update to recent upstream version

* Thu Nov 22 2012 Johannes Lips <hannes@fedoraproject.org> 2.5.1-1
- update to recent upstream version

* Mon Oct 29 2012 Dan Horák <dan[at]danny.cz> 2.5-2
- disable internal crash handler on not supported arches

* Sat Oct 27 2012 Johannes Lips <hannes@fedoraproject.org> 2.5-1
- update to recent upstream version

* Sat Feb 18 2012 Johannes Lips <Johannes.Lips googlemail com> 2.3-2
- disabled the build of debug files
