%global forgeurl	https://github.com/bluesabre/menulibre
%global tag			menulibre-2.2.1

Name:			menulibre
Version:		2.2.1
Release:		5%{?dist}
Summary:		FreeDesktop.org compliant menu editor

%forgemeta

License:		GPLv3
URL:			https://bluesabre.org/projects/menulibre/
Source0:		%{forgesource}
Source1:		menulibre.appdata.xml
BuildArch:		noarch

Requires:		gnome-menus
Requires:		gtk3
Requires:		hicolor-icon-theme
Requires:		python3-gobject
Requires:		python3-psutil
Requires:		xdg-utils

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	libappstream-glib

BuildRequires:	gnome-menus
BuildRequires:	gtk3
BuildRequires:	python3-devel
BuildRequires:	python3-distutils-extra
BuildRequires:	python3-gobject
BuildRequires:	python3-psutil

Provides:		python3-%{name} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}
%{?python_provide:%python_provide python3-%{name}_lib}

%description
MenuLibre is an advanced FreeDesktop.org compliant menu editor.

All fields specified in the FreeDesktop.org Desktop Entry and Menu
specifications are available to quickly update. Additionally, MenuLibre
provides an editor for the launcher actions used by applications such as Unity
and Plank.

Features:

- A beautiful interface powered by the latest version of GTK+.
- Create new launchers, or modify existing ones with complete control over
  common settings and access to advanced settings.
- Add, remove, and adjust desktop actions: powerful shortcuts available used by
  Unity, Xfce, and Pantheon.
- Easily rearrange menu items to suit your needs.

%prep
%forgeautosetup

%build

%install
CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}}" LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS}}" \
%{__python3} setup.py install --root=%{buildroot}
rm -rfv %{buildroot}/usr/bin/__pycache__

# Remove hashbang line from non-executable library files
for lib in %{buildroot}%{python3_sitelib}/%{name}{,_lib}/*.py; do
	sed '1{\@^#!/usr/bin/python3@d}' $lib > $lib.new &&
	touch -r $lib $lib.new &&
	mv $lib.new $lib
done

desktop-file-install									\
--remove-key="OnlyShowIn"								\
--delete-original										\
--dir=%{buildroot}%{_datadir}/applications				\
%{buildroot}/%{_datadir}/applications/%{name}.desktop

install -Dpm 0644 -t %{buildroot}%{_metainfodir}/ %{SOURCE1}

%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files -f %{name}.lang
%doc AUTHORS NEWS README
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-menu-validate
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_metainfodir}/%{name}.appdata.xml
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}-menu-validate.1.*
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}_lib/
%{python3_sitelib}/%%{name}-*.egg-info

%changelog
* Sat Aug 08 2020 Lyes Saadi <fedora@lyes.eu> - 2.2.1-5
- Unretiring menulibre

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 2019 My Karlsson <mk@acc.umu.se> - 2.2.1-1
- Update to version 2.2.1

* Tue Apr 02 2019 Troy Dawson <tdawson@redhat.com> - 2.2.0-7
- Rebuilt to change main python from 3.4 to 3.6

* Sat Feb 09 2019 My Karlsson <mk@acc.umu.se> - 2.2.0-6
- Fix for reading menulibre-menu-validate output on el7

* Sun Feb 03 2019 My Karlsson <mk@acc.umu.se> - 2.2.0-5
- Build for epel7

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-2
- Rebuilt for Python 3.7

* Mon Mar 19 2018 My Karlsson <mk@acc.umu.se> - 2.2.0-1
- Update to upstream release 2.2.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 My Karlsson <mk@acc.umu.se> - 2.1.5-1
- Update to upstream release 2.1.5

* Sun Feb 04 2018 My Karlsson <mk@acc.umu.se> - 2.1.4-2
- Backport desktop detection fix

* Sun Jan 21 2018 My Karlsson <mk@acc.umu.se> - 2.1.4-1
- Update to upstream release 2.1.4

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.3-6
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1.3-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Apr 10 2016 My Karlsson <mk@acc.umu.se> - 2.1.3-1
- Update to upstream release 2.1.3.

* Sun Mar 13 2016 My Karlsson <mk@acc.umu.se> - 2.1.2-4
- Fix a problem where adding a launcher and no directory was selected would
  emit a type error

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sat Oct 10 2015 My Karlsson <mk@acc.umu.se> - 2.1.2-1
- Update to 2.1.2

* Sun May 31 2015 My Karlsson <mk@acc.umu.se> - 2.0.6-1
- Initial build
