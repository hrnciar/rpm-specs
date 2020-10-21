Name:           notepadqq
Version:        1.4.8
Release:        13%{?dist}
Summary:        An advanced text editor for developers

# Notepadqq is licensed under GPLv3
# CodeMirror is licensed under MIT
# RequireJS is licensed under MIT
# jQuery is licensed under MIT
# nodejs-archiver is licensed under MIT
License:        GPLv3 and MIT

URL:            https://notepadqq.com/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

Patch1:         %{name}-add-node.patch
Patch2:         %{name}-appdata.patch

BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  qt5-linguist
BuildRequires:  qt-creator
BuildRequires:  qtchooser
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       nodejs-shelljs
#Requires:       nodejs-archiver
Requires:       mathjax
Requires:       hicolor-icon-theme

Provides:       bundled(nodejs-codemirror) = 5.33.0 
Provides:       bundled(nodejs-adm-zip)
Provides:       bundled(nodejs-archiver) = 0.14.4 
Provides:       bundled(jQuery) = 2.1.1
Provides:       bundled(requireJS) = 2.3.5

%description
A qt text editor for developers, with advanced tools, but remaining simple.
It supports syntax highlighting, themes and more

%prep
%autosetup -p1

# Remove bundled archiver
#rm -rf src/extension_tools/node_modules/archiver
# Remove bundled shelljs
rm -rf src/extension_tools/node_modules/shelljs
# Remove bundled MathJax
rm -rf src/editor/libs/MathJax
sed  -i -e '/cp -r libs\/MathJax/d' src/editor/Makefile

%build
export CXX=g++
export LDFLAGS="%{__global_ldflags}"
export CXXFLAGS="%{optflags}"
./configure --qmake=qmake-qt5 --lrelease %{_bindir}/lrelease-qt5
%make_build


%install
mkdir -p %{buildroot}%{_datadir}/%{name} \
         %{buildroot}%{_datadir}/applications \
         %{buildroot}%{_bindir} \
         %{buildroot}%{_mandir}/man1 \
         %{buildroot}%{_libexecdir}/%{name}/

# Manpage
install -pm 644 support_files/manpage/%{name}.1 %{buildroot}%{_mandir}/man1

# Desktop file
desktop-file-install --remove-key=Encoding --remove-key=OnlyShowIn --remove-category=Utility \
 --dir=%{buildroot}%{_datadir}/applications support_files/shortcuts/%{name}.desktop

# Appstream
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 support_files/%{name}.appdata.xml %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

# App data
pushd out/release
# Move files to comply better with FHS
install -pm 755 bin/* %{buildroot}%{_bindir}/
install -pm 755 lib/* %{buildroot}%{_libexecdir}/%{name}/
cp -a appdata/editor %{buildroot}%{_datadir}/%{name}/
cp -a appdata/extension_tools %{buildroot}%{_datadir}/%{name}/
ln -sf %{_bindir}/shjs %{buildroot}%{_datadir}/%{name}/extension_tools/node_modules/.bin/shjs
popd

# Fix executable permissions
find %{buildroot}%{_datadir} -name '*.sh' -exec chmod a+x {} ';'
find %{buildroot}%{_datadir} -name 'sauce.js' -exec chmod a+x {} ';'

find %{buildroot}%{_datadir} -name '.npmignore' -exec rm -rf {} ';'

# Install icons
for size in `ls support_files/icons/hicolor`; do
 mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${size}/apps
 install -pm 644 support_files/icons/hicolor/${size}/apps/%{name}.* %{buildroot}%{_datadir}/icons/hicolor/${size}/apps/
done

%files
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
%{_libexecdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_metainfodir}/%{name}.appdata.xml
%license COPYING src/extension_tools/node_modules/archiver/LICENSE
%doc *.md

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-13
- Second attempt - Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
- Add qt5-linguist BR

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 19 2020 Jeff Law <law@redhat.com> - 1.4.8-11
- Drop qt5-devel buildrequires

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 30 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.4.8-9
- Fix desktop file's entries

* Sat Nov 30 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.4.8-8
- Remove unnecessary dependencies

* Fri Nov 29 2019 Antonio Trande <sagitter@fedoraproject.org> - 1.4.8-7
- Some packaging fixes
- Bundle nodejs-archiver until it will be newly available on Fedora

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jan De Luyck <jan@kcore.org> - 1.4.8-3
- Removed bundled MathJax
- Updated bundled provides for jQuery and requestJS

* Tue Jun 26 2018 Jan De Luyck <jan@kcore.org> - 1.4.8-2
- Updated to latest comments on Bugzilla

* Wed Jun 13 2018 Jan De Luyck <jan@kcore.org> 1.4.8-1
- Updated to 1.4.8

* Tue Jun 12 2018 Jan De Luyck <jan@kcore.org> 1.4.0-1
- Updated to 1.4.0
- Updated SPEC file based on further comments on Bugzilla

* Fri Apr 20 2018 Jan De Luyck <jan@kcore.org> 1.3.6-1
- Removed bundled nodejs-archiver and nodejs-shelljs
- Updated to 1.3.6

* Wed Apr 11 2018 Jan De Luyck <jan@kcore.org> 1.3.4-2
- Added Provides (comment on Fedora bugzilla)

* Wed Apr 11 2018 Jan De Luyck <jan@kcore.org> 1.3.4-1
- updated to 1.3.4

* Sun Feb 04 2018 Jan De Luyck <jan@kcore.org> 1.2.0-3
- updated to codemirror 5.33.0

* Sun Dec 10 2017 Jan De Luyck <jan@kcore.org> 1.2.0-2
- Fixed some issues from Fedora bugzilla 1519785, as remarked by Ben Rosser.

* Thu Nov 30 2017 Jan De Luyck <jan@kcore.org> 1.2.0-1
- Updated to 1.2.0
- Updated to CodeMirror 5.32.0
- Moved patching to .patch files

* Sun Feb 26 2017 Kevin Puertas Ruiz <kevin01010@gmail.com> 1.0.1-5
- Fix some issues from fedora bugzilla 1426844 (Nemanja Milosevic)

* Sat Feb 25 2017 Kevin Puertas Ruiz <kevin01010@gmail.com> 1.0.1-4
- Some files change path
- Delete some tests
- Fixes to rpmlint changing shebangs of codemirror
- Patch for notepadqq start (Till notepadqq accepts patch in release)

* Wed Feb 22 2017 Kevin Puertas Ruiz <kevin01010@gmail.com> 1.0.1-3
- Fixed fedora (25) compilation
- Move files to better places
- No patch required

* Sun Feb 15 2015 Simon Arjuna Erat <erat.simon@gmail.com> 0.41.1-21
- Fixed blank opterations 2

* Sat Feb 14 2015 Simon Arjuna Erat <erat.simon@gmail.com> 0.41.1-16
- Fixed blank opterations

* Thu Feb 05 2015 Simon Arjuna Erat <erat.simon@gmail.com> 0.41.1-13
- Search in files
- Print and Print Now

* Sun Jan 11 2015 Simon Arjuna Erat <erat.simon@gmail.com> 0.41.1-10
- Close tabs with middle click

* Mon Dec 29 2014 Simon Arjuna Erat <erat.simon@gmail.com> 0.41.1-2
- Added: Qt 5.4 to LD_LIBRARY_PATH
- Added: recognize more shells: ksh, csh, tcsh, zsh and fish 

* Tue Nov 18 2014 Simon Arjuna Erat <erat.simon@gmail.com> 0.40.1-20
- Binary knows more shebangs (sh/bash)
- Figured it has a manpage & desktop files, trying to package them

* Mon Nov 17 2014 Simon Arjuna Erat <erat.simon@gmail.com> 0.40.1-9
- Figured BuildRequires and Requires

* Mon Nov 17 2014 Simon Arjuna Erat <erat.simon@gmail.com> 0.40.1-8
- Added patch
- Clean up spec

* Sat Nov 15 2014 Simon Arjuna Erat <erat.simon@gmail.com> 0.40.1-1
- Initial build attempt

