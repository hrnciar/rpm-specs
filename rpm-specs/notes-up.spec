%global uuid    com.github.philip-scott.%{name}

Name:           notes-up
Version:        2.0.2
Release:        2%{?dist}
Summary:        Markdown notes editor & manager

# The entire source code is GPLv2+ except:
# BSD:          highlight.LICENSE
License:        GPLv2+ and BSD
URL:            https://github.com/Philip-Scott/Notes-up
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

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
%autosetup -p1 -n Notes-up-%{version}


%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -Dnoele=1
%make_build


%install
%make_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{uuid}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{uuid}.desktop


%files -f %{name}.lang
%doc README.md
%license LICENSE data/assets/highlightjs/highlight.LICENSE
%{_bindir}/%{uuid}
%{_datadir}/%{name}
%{_datadir}/applications/%{uuid}.desktop
%{_datadir}/glib-2.0/schemas/org.notes.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/%{uuid}.appdata.xml


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.2-1
- Update to 2.0.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2.0.0-3
- Initial package
