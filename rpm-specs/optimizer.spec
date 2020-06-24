%global file_name com.github.hannesschulze.optimizer

Name:           optimizer
Version:        1.2.1
Release:        3%{?dist}
Summary:        Find out what's eating up your system resources

License:        GPLv3+
URL:            https://github.com/hannesschulze/optimizer/
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-fallback-theme.patch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libwnck-3.0)

Requires:       hicolor-icon-theme

%description
Find out what's eating up your system resources and delete unnecessary files
from your disk.

%prep
%autosetup
# Quick fix for wrong location translate file
# https://github.com/hannesschulze/optimizer/pull/59/files
mv ru.po po/ru.po

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{file_name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{file_name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{file_name}.desktop

%files -f %{file_name}.lang
%doc README.md
%license COPYING
%{_bindir}/%{file_name}
%{_datadir}/applications/%{file_name}.desktop
%{_datadir}/glib-2.0/schemas/%{file_name}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{file_name}.svg
%{_metainfodir}/%{file_name}.appdata.xml

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.2.1-1
- Update to 1.2.1

* Tue Apr 23 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.2.0-1
- Update to 1.2.0
- Enabled fallback theme which is better suits Adwaita GTK theme

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 1.1.0-3
- Rebuild with Meson fix for #1699099

* Wed Mar 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.1.0-2
- Initial Package
