%global uuid    com.github.phase1geo.%{name}

Name:           minder
Version:        1.11.2
Release:        1%{?dist}
Summary:        Mind-mapping application

License:        GPLv3+
URL:            https://github.com/phase1geo/Minder
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  libmarkdown-devel
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libxml-2.0)

Requires:       hicolor-icon-theme

%description
Create, develop and visualize your ideas.

Use the power of mind-mapping to make your ideas come to life.

- Quickly create visual mind-maps using the keyboard and automatic layout
- Gorgeous themes
- Export to PDF, PNG, JPEG, BMP, SVG, OPML, CSV, Markdown and PlainText formats
- Printer support
- Add notes, tasks and images to your nodes
- Colorized node branches


%prep
%autosetup -n Minder-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{uuid}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{uuid}.lang
%license LICENSE COPYING
%doc README.md AUTHORS
%{_bindir}/%{uuid}
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/gtksourceview-3.0/styles/*.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/mime/packages/*.xml
%{_metainfodir}/*.xml


%changelog
* Sat Oct 17 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.11.2-1
- build(update): 1.11.2

* Fri Sep 25 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.11.1-1
- Update to 1.11.1

* Tue Sep 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.11.0-1
- Update to 1.11.0

* Thu Aug 27 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.10.0-1
- Update to 1.10.0

* Sat Aug 08 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.9.2-1
- Update to 1.9.2

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.9.1-1
- Update to 1.9.1

* Wed Jul 01 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.9.0-1
- Update to 1.9.0

* Sun May 17 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.8.0-1
- Update to 1.8.0

* Tue Apr 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.7.3-1
- Update to 1.7.3

* Fri Mar 27 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.7.2-1
- Update to 1.7.2

* Sun Mar 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.7.1-1
- Update to 1.7.1

* Sat Mar 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.7.0-1
- Update to 1.7.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 29 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6.0-1
- Update to 1.6.0
- Add new BR

* Sun Nov 24 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.5.1-1
- Update to 1.5.1

* Sun Sep 08 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.5.0-1
- Update to 1.5.0

* Thu Jul 25 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.4.1-1
- Update to 1.4.1

* Sat Jun 08 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.3.1-1
- Update to 1.3.1

* Wed May 29 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.3.0-1
- Update to 1.3.0

* Tue Apr 23 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.2.1-1
- Initial package
