Name:           persepolis
Version:        3.2.0
Release:        4%{?dist}
Summary:        A powerful download manager powered by aria2

License:        GPLv3+
URL:            https://persepolisdm.github.io/
Source0:        https://github.com/persepolisdm/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# Disable checking for runtime dependencies in setup.py. Upstream has agreed to
# replace it with a more appropriate implementation
Patch0:         persepolis-nodepscheck.diff

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  python3-setuptools
BuildRequires:  libappstream-glib
# libnotify is required for notify-send
Requires:       aria2 libnotify python3-qt5 python3-requests
Requires:       python3-setproctitle sound-theme-freedesktop python3-psutil
Requires:       pulseaudio-utils youtube-dl

%description
Persepolis is a download manager and a GUI for aria2 powered by Python.
 - Graphical UI front end for aria2
 - Multi-segment downloading
 - Scheduling downloads
 - Download queue


%prep
%autosetup -p1
chmod a-x xdg/*.desktop
rm 'persepolis/Persepolis Download Manager.py'
find -type f -exec \
   sed -i '1s=^#!/usr/bin/\(python\|env python.*\)$=#!%{__python3}=' {} \;


%build
%{py3_build}


%install
%{py3_install}
chmod a+x %{buildroot}/%{python3_sitelib}/persepolis/__main__.py

%check
# No valid tests available
#%{__python3} setup.py test
desktop-file-validate %{buildroot}/%{_datadir}/applications/*persepolis.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml


%files
%license LICENSE
%doc README.md

%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/*
%{_mandir}/man1/%{name}.1*
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info
%{_datadir}/metainfo/com.github.persepolisdm.persepolis.appdata.xml


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.2.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 27 2019 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.2.0-1
- Update to 3.2.0, with some bug fixes and new features

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-3
- Rebuilt for Python 3.7

* Mon Apr 02 2018 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.1.0-2
- Add youtube-dl dependency

* Sat Mar 31 2018 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.1.0-1
- New upstream version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.0.1-3
- Fix a bug in registering for startup, fixes #1535604

* Mon Jan 01 2018 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.0.1-2
- Add a comment about the patch
- more specific %files section

* Sat Dec 30 2017 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 3.0.1-1
- Initial version
