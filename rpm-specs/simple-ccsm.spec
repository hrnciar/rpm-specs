%global basever 0.8.16

Name:           simple-ccsm
Version:        0.8.16
Release:        6%{?dist}
Summary:        Simple settings manager for Compiz
License:        GPLv2+
URL:            https://gitlab.com/compiz/%{name}
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(compiz) >= %{basever}
BuildRequires:  pkgconfig(libcompizconfig) >= %{basever}
Requires:       compiz-plugins-main >= %{basever}
Requires:       ccsm >= %{basever}
Requires:       python3-cairo
Requires:       compizconfig-python
Requires:       python3-gobject
Recommends:     compiz-plugins-extra >= %{basever}


%description
Compiz settings manager focused on simplicity for an end-user.


%prep
%autosetup -n %{name}-v%{version}

%build
python3 setup.py build \
    --prefix=%{_prefix} \
    --enableDesktopEffects

%install
python3 setup.py install \
    --root=%{buildroot} \
    --prefix=%{_prefix}

mv %{buildroot}%{_datadir}/{metainfo,appdata}/

fdupes -s %{buildroot}%{_datadir}/

desktop-file-install                              \
    --delete-original                             \
    --dir=%{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/*.desktop

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README.md NEWS
%{_bindir}/%{name}
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/appdata/%{name}.appdata.xml
%{python3_sitelib}/simple_ccsm-%{version}-py3.?.egg-info


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.16-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.16-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr  2 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.8.16-1
- New version
  Related: rhbz#1656467
- New URL

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.14.1-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.14.1-3
- Remove obsolete scriptlets

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 20 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1:0.8.14.1-1
- update to 0.8.14.1 release
- Fix Compiz checking on Python3.
- Silence a RSVG API version startup warning
- use old rpm python macros
- fix rhbz (#1444170)

* Thu Apr 20 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1:0.8.14-1
- update to 0.8.14 release
- switch to python3
- modernize spec file

* Thu Feb 23 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.8.12-4
- fix build for rawhide (f26)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 01 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.8.12-2
- simplify file section

* Wed Mar 30 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.8.12-1
- initial package

