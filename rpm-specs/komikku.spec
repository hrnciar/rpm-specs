%global appname Komikku
%global uuid    info.febvre.%{appname}

Name:           komikku
Version:        0.21.1
Release:        1%{?dist}
Summary:        Online/offline manga reader for GNOME
BuildArch:      noarch

License:        GPLv3+
URL:            https://gitlab.com/valos/Komikku
Source0:        %{url}/-/archive/v%{version}/%{appname}-v%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.50.0
BuildRequires:  python3-devel >= 3.6
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.1
BuildRequires:  pkgconfig(libhandy-1) >= 1.0.0

Requires:       hicolor-icon-theme
Requires:       libhandy1 >= 1.0.0
Requires:       python3-beautifulsoup4
Requires:       python3-cloudscraper
Requires:       python3-dateparser
Requires:       python3-keyring
Requires:       python3-lxml

# # This could help to build Komikku for current Fedora releases at least in Copr
# # * https://bugzilla.redhat.com/show_bug.cgi?id=1790100#c9
# Patch0 provides compatibility with the other magic package, solving a conflict
# problem, opening komikku to f30, f31 and f32 and allowing users to use komikku,
# rpmlint and other important packages simultaneously.
#
# The conflict between python-magic and python-file-magic should be brought to
# FESCO.
Requires:       python3dist(file-magic)

Requires:       python3-pillow
Requires:       python3-pure-protobuf
Requires:       python3-unidecode

%description
An online/offline manga reader for GNOME, developed with the aim of being used
with the Librem 5 phone.


%prep
%autosetup -n %{appname}-v%{version} -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_datadir}/icons/hicolor/symbolic/*/*.svg
%{_metainfodir}/*.xml
%{python3_sitelib}/%{name}/


%changelog
* Mon Oct 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.21.1-1
- build(update): 0.21.1

* Tue Sep 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.20.0-1
- Update to 0.20.0

* Sat Aug 08 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.19.0-1
- Update to 0.19.0

* Wed Jul 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.18.0-2
- Add new dep: python3-keyring

* Wed Jul 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.18.0-1
- Update to 0.18.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.17.0-2
- Add explicitly dep: libhandy1

* Fri May 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.17.0-1
- Update to 0.17.0
- Build with system libhandy-1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.16.0-2
- Rebuilt for Python 3.9

* Sun May 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.16.0-1
- Update to 0.16.0
- Bundle libhandy-1

* Fri Apr 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.15.0-1
- Update to 0.15.0

* Tue Apr 14 2020 Lyes Saadi <fedora@lyes.eu> - 0.14.0-3
- Compatibility with python3-file-magic

* Thu Apr 02 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.14.0-2
- Specify required version of 'python3-magic' | RHBZ#1790100#c9

* Thu Apr 02 2020 Lyes Saadi <fedora@lyes.eu> - 0.14.0-1
- Update to 0.14.0

* Sun Mar 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.13.0-1
- Update to 0.13.0

* Fri Feb 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.11.1-1
- Initial package
