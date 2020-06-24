Name: piper
Version: 0.5
Release: 2%{?dist}

License: GPLv2+ and LGPLv2+
URL: https://github.com/libratbag/%{name}
Summary: GTK application to configure gaming mice
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: libratbag-ratbagd
BuildRequires: pygobject3-devel
BuildRequires: python3-devel
BuildRequires: gettext-devel
BuildRequires: python3-lxml
BuildRequires: meson
BuildRequires: git

Requires: hicolor-icon-theme
Requires: libratbag-ratbagd >= 0.10
Requires: python3-evdev
Requires: python3-lxml
Requires: gtk3

%{?python_provide:%python_provide python3-%{name}}

%description
Piper is a GTK+ application to configure gaming mice, using libratbag
via ratbagd.

%prep
%autosetup -S git
sed -i '/meson_install.sh/d' meson.build

%build
%meson
%meson_build

%check
%meson_test
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%install
%meson_install
%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{python3_sitelib}/%{name}/
%{_datadir}/applications/*.desktop
%{_metainfodir}/*.appdata.xml
%{_datadir}/icons/hicolor/*/apps/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5-2
- Rebuilt for Python 3.9

* Mon May 25 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5-1
- Updated to version 0.5.

* Tue Feb 11 2020 Peter Hutterer <peter.hutterer@redhat.com> 0.4-1
- piper 0.4

* Fri Jan 31 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3-5
- Performed SPEC cleanup to follow modern Fedora guidelines.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3-2
- Rebuilt for Python 3.8

* Fri Aug 02 2019 Peter Hutterer <peter.hutterer@redhat.com> 0.3-1
- piper 0.3

* Mon Jul 29 2019 Peter Hutterer <peter.hutterer@redhat.com> 0.2.905-1
- piper 0.2.905

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.904-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 28 2019 Peter Hutterer <peter.hutterer@redhat.com> 0.2.904-2
- Add python3-lxml to BuildRequires to pass the checks

* Thu Feb 28 2019 Peter Hutterer <peter.hutterer@redhat.com> 0.2.904-1
- Update to version 0.2.904.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.903-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Peter Hutterer <peter.hutterer@redhat.com> 0.2.903-1
- Updated to version 0.2.903.

* Wed Sep 26 2018 Peter Hutterer <peter.hutterer@redhat.com> 0.2.902-2
- Add missing Requires python3-lxml (#1632979)

* Mon Sep 10 2018 Peter Hutterer <peter.hutterer@redhat.com> 0.2.902-1
- Updated to version 0.2.902.

* Tue Aug 21 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.2.901-1
- Updated to version 0.2.901.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.900-3.20180214git5f6ed20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.900-2.20180214git5f6ed20
- Rebuilt for Python 3.7

* Thu Jun 28 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.2.900-1.20180214git5f6ed20
- Initial SPEC release.
