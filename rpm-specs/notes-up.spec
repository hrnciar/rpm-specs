%global uuid    com.github.philip-scott.%{name}

Name:           notes-up
Version:        2.0.2
Release:        6%{?dist}
Summary:        Markdown notes editor & manager

# The entire source code is GPLv2+ except:
# BSD:          highlight.LICENSE
License:        GPLv2+ and BSD
URL:            https://github.com/Philip-Scott/Notes-up
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch1:         0001-NotebookListDialog-Make-modal.patch
Patch2:         0002-Remove-window-from-global-variable.patch
Patch3:         0003-Dual-Mode.patch
Patch4:         0004-Viewer-Auto-Update-a-second-after-typing-in-dual-vie.patch
Patch5:         0005-Update-ISSUE_TEMPLATE.md.patch
Patch6:         0006-Support-Multiple-Files-329.patch
Patch7:         0007-Update-French-translation-333.patch
Patch8:         0008-Downgrade-Node.js-to-fix-builds-on-Travis-CI-337.patch
Patch9:         0009-Use-sudo-only-to-install-not-to-build-343.patch
Patch10:        0010-Add-size-to-charArray-in-libmarkdown.vapi.patch
Patch11:        0011-Support-multiple-files-358.patch
Patch12:        0012-Add-CI-362.patch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  vala
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(granite) >= 5.2.0
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.9.10
BuildRequires:  pkgconfig(gtksourceview-3.0) >= 3.10
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(libmarkdown)
BuildRequires:  pkgconfig(sqlite3) >= 3.5.9
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Requires:       hicolor-icon-theme

%description
The intuitive writing app for everyone, from students to developers.

With powerful features like:

- Easy-to-use markdown editor.
- Notebooks and tags, quickly find and organize your notes.
- Your work is saved automatically as you write, you will never loose
  your work.
- Plugins: such as embedding YouTube videos and setting text color.
- Export as PDF and Markdown files.
- Cross-Note Links to quickly reference other notes.
- 3 Beautiful app themes to help you create the best writing environment.
- And much more!


%prep
%autosetup -n Notes-up-%{version} -p1


%build
%cmake \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -Dnoele=1
%cmake_build


%install
%cmake_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%doc README.md
%license LICENSE data/assets/highlightjs/highlight.LICENSE
%{_bindir}/%{uuid}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/org.notes.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/mime/packages/*.mime.xml
%{_metainfodir}/*.xml


%changelog
* Wed Sep  2 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.2-6
- Backport patches for new Vala compatibility | Fix FTBFS f33 | RH#1865072

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 30 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.2-4
- Rebuild with out-of-source builds new CMake macros

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.2-1
- Update to 2.0.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.0-3
- Initial package
