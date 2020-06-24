Name:           ktikz
Version:        0.12
Release:        10%{?dist}
Summary:        KDE Editor for the TikZ language

# ktikz/qtikz are GPLv2+, documentation is GFDL
License:        GPLv2+ and GFDL
URL:            http://www.hackenberger.at/blog/ktikz-editor-for-the-tikz-language
Source0:        https://github.com/fhackenberger/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# Use xdg-open instead of kwrite as defaut editor in qtikz
Patch0:         %{name}-0.12-default_editor.patch
# Fix PGF manual path
Patch1:         %{name}-0.12-pgfmanual.patch
# Fix RHBZ #1565806 (see also https://github.com/fhackenberger/ktikz/pull/20)
Patch2:         %{name}-0.12-RHBZ1565806.patch

BuildRequires:  cmake
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  kf5-kdelibs4support
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(poppler)
BuildRequires:  pkgconfig(poppler-qt5)
BuildRequires:  qt5-qttools-devel
# Required to display help
Requires:       khelpcenter
# pdftops required by ktikz
Requires:       poppler-utils
# Minimum TeX dependencies
Requires:       tex-latex-bin
Requires:       tex(preview.sty)
Requires:       tex(pgf.sty)
Requires:       tex(tikz.sty)
# Required to display PGF documentation
Requires:       tex-pgf-doc
Requires:       xdg-utils
# Required for the KTikZ SVG icon
Requires:       oflb-prociono-fonts
%{?kde_runtime_requires}

%description
KTikZ is a small application to assist in the creation of diagrams and drawings
using the TikZ macros from the LaTeX package "pgf". It consists of a text editor
pane in which the TikZ code for the drawing is edited and a preview pane showing
the drawing as rendered by LaTeX. The preview pane can be updated in
real-time. Common drawing tools, options and styles are available from the menus
to assist the coding process.

This package contains the KDE version of the program.


%package -n qtikz
Summary:        Editor for the TikZ language
# pdftops required by qtikz
Requires:       poppler-utils
# Required to display help
Requires:       qt5-assistant
# Minimum TeX dependencies
Requires:       tex-latex-bin
Requires:       tex(preview.sty)
Requires:       tex(pgf.sty)
Requires:       tex(tikz.sty)
# Required to display PGF documentation
Requires:       tex-pgf-doc
Requires:       xdg-utils
# Required for the QTikZ SVG icon
Requires:       oflb-prociono-fonts

%description -n qtikz
QTikZ is a small application to assist in the creation of diagrams and drawings
using the TikZ macros from the LaTeX package "pgf". It consists of a text editor
pane in which the TikZ code for the drawing is edited and a preview pane showing
the drawing as rendered by LaTeX. The preview pane can be updated in
real-time. Common drawing tools, options and styles are available from the menus
to assist the coding process.

This package contains the Qt version of the program.


%prep
%autosetup -p0


%build
# Build ktikz
mkdir -p %{_target_platform}
pushd %{_target_platform}
%cmake_kf5 ..
popd
%make_build -C %{_target_platform}

# Build qtikz
%qmake_qt5
%make_build


%install
# Install ktikz
make install/fast DESTDIR=$RPM_BUILD_ROOT -C %{_target_platform}
# Install qtikz
%make_install INSTALL_ROOT=$RPM_BUILD_ROOT

# Delete qtikz locale files wrongly installed in ktikz directories
rm -r $RPM_BUILD_ROOT%{_datadir}/%{name}/locale/

%find_lang %{name} --with-kde --with-html
%find_lang qtikz --with-qt

# Install AppData files
install -Dpm 0644 data/%{name}.appdata.xml $RPM_BUILD_ROOT%{_datadir}/metainfo/%{name}.appdata.xml
# Since no AppData file is provided for qtikz, create one from the ktikz one
sed \
    "s|ktikz\.desktop|qtikz.desktop|g; s|KtikZ|QtikZ|g" \
    data/%{name}.appdata.xml >$RPM_BUILD_ROOT%{_datadir}/metainfo/qtikz.appdata.xml

# Remove useless license file in qtikz directories
rm $RPM_BUILD_ROOT%{_datadir}/qtikz/LICENSE.GPL2

# Install QTikZ icon in /usr/share/icons/ and update desktop file for
# integration with appstream-data
install -Dpm 0644 app/icons/qtikz.svg $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/qtikz.svg
for i in 22 128; do
    install -Dpm 0644 app/icons/qtikz-$i.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}x$i/apps/qtikz.png
done
desktop-file-edit --set-icon=qtikz $RPM_BUILD_ROOT%{_datadir}/applications/qtikz.desktop


%check
desktop-file-validate $RPM_BUILD_ROOT%{_kf5_datadir}/applications/%{name}.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/qtikz.desktop

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/%{name}.appdata.xml
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/qtikz.appdata.xml


%files -f %{name}.lang
%doc Changelog README.md TODO
%license LICENSE.FDL1.2 LICENSE.GPL2
%{_kf5_bindir}/%{name}
%{_kf5_qtplugindir}/*.so
%{_kf5_datadir}/applications/%{name}.desktop
%{_kf5_datadir}/config.kcfg/%{name}.kcfg
%{_kf5_datadir}/%{name}part/
%{_kf5_datadir}/kxmlgui5/%{name}/
%{_kf5_datadir}/kservices5/%{name}part.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/%{name}/
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man1/%{name}.1.*


%files -n qtikz -f qtikz.lang
%doc Changelog README.md TODO
%license LICENSE.FDL1.2 LICENSE.GPL2
%{_bindir}/qtikz
%{_datadir}/applications/qtikz.desktop
%{_datadir}/icons/hicolor/*/apps/qtikz.*
%{_datadir}/mime/packages/qtikz.xml
%{_datadir}/qtikz/
%{_datadir}/metainfo/qtikz.appdata.xml
%{_mandir}/man1/qtikz.1.*


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 0.12-9
- Rebuild for poppler-0.84.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 18 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.12-6
- Fix RHBZ #1565806

* Tue Aug 14 2018 Marek Kasik <mkasik@redhat.com> - 0.12-5
- Rebuild for poppler-0.67.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Marek Kasik <mkasik@redhat.com> - 0.12-3
- Rebuild for poppler-0.63.0

* Tue Mar 20 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.12-2
- Add HTML documentation to %%find_lang

* Tue Mar 20 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.12-1
- Update to 0.12

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11-2
- Remove obsolete scriptlets

* Thu Nov 16 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.11-1
- Update to 0.11
- Spec cleanup
- Build qtikz with Qt 5

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-0.5.20150904gitab7bd73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-0.4.20150904gitab7bd73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-0.3.20150904gitab7bd73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 11 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.11-0.2.20150904gitab7bd73
- Fix build on ARM

* Wed Feb 10 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.11-0.1.20150904gitab7bd73
- Update to latest snapshot
- Spec cleanup

* Wed Feb 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.10-17
- use %%qmake_qt4 macro to ensure proper build flags

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.10-15
- Rebuilt for GCC 5 C++11 ABI change

* Sat Jan 31 2015 Rex Dieter <rdieter@fedoraproject.org> 0.10-14
- Requires: kate4-part, kde-apps cleanup

* Mon Aug 18 2014 Rex Dieter <rdieter@fedoraproject.org> 0.10-13
- update mime scriptlets

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 16 2012 Marek Kasik <mkasik@redhat.com> - 0.10-7
- Rebuild (poppler-0.20.0)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 15 2011 Rex Dieter <rdieter@fedoraproject.org> 0.10-5
- ktikz: Requires: kate-part (#744443)

* Mon Sep 19 2011 Marek Kasik <mkasik@redhat.com> - 0.10-4
- Rebuild (poppler-0.17.3)

* Fri Jul 15 2011 Marek Kasik <mkasik@redhat.com> - 0.10-3
- Rebuild (poppler-0.17.0)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 12 2010 Mohamed El Morabity <melmorabity@fedoraproject.org> 0.10-1
- Initial RPM release
