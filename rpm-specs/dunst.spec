Name:     dunst
Version:  1.4.1
Release:  4%{?dist}
Summary:  Simple and configurable notification-daemon
License:  BSD and MIT
URL:      https://dunst-project.org
Source0:  https://github.com/dunst-project/%{name}/archive/v%{version}.tar.gz

Requires: dbus

# keep this sorted please
BuildRequires: cairo-devel
BuildRequires: dbus-devel
BuildRequires: gcc
BuildRequires: gdk-pixbuf2-devel
BuildRequires: glib2-devel
BuildRequires: gtk2-devel
BuildRequires: libnotify-devel
BuildRequires: libpng-devel
BuildRequires: libxdg-basedir-devel
BuildRequires: libXft-devel
BuildRequires: libXinerama-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libX11-devel
BuildRequires: pango-devel
BuildRequires: systemd
BuildRequires: /usr/bin/pod2man

Provides: desktop-notification-daemon


%description
Dunst is a highly configurable and lightweight notification daemon with the
similar look and feel to dmenu.


%prep
%setup -q


%build
make %{?_smp_mflags} VERSION=%{version} PREFIX=%{_prefix} EXTRACFLAGS="%{optflags}" all dunstify


%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}
install -Dm755 dunstify %{buildroot}%{_bindir}/dunstify


%files
%doc AUTHORS CHANGELOG.md LICENSE README.md RELEASE_NOTES
%{_bindir}/%{name}
%{_bindir}/dunstify
%{_datadir}/dbus-1/services/org.knopwob.%{name}.service
%{_userunitdir}/%{name}.service
%{_datadir}/%{name}
%{_datadir}/man/man1/%{name}.1.gz

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 15 2020 Xaver Hellauer <xaver.hellauer@gmail.com> - 1.4.1-3
- Build including dunstify

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 29 2019 Lukas Zapletal <lzap@redhat.com> - 1.4.1-1
- new version

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Lukas Zapletal <lzap+rpm@redhat.com> - 1.4.0-1
- Upstream release 1.4.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Lukas Zapletal <lzap+rpm@redhat.com> 1.3.2-2
- Upstream tarball is now bz2 compressed

* Mon Jul 23 2018 Lukas Zapletal <lzap+rpm@redhat.com> 1.3.2-1
- New version 1.3.2
- Added gcc build dependency

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 23 2017 Lukas Zapletal <lzap+rpm@redhat.com> - 1.2.0-1
- New version 1.2.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 07 2015 Lukas Zapletal <lzap+rpm@redhat.com> 1.1.0-2
- Removed unnecessary numlock patch from 1.0.0

* Wed Jan 07 2015 Lukas Zapletal <lzap+rpm@redhat.com> 1.1.0-1
- Bumped to version 1.1.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun 03 2014 Lukas Zapletal <lzap+rpm@redhat.com> 1.0.0-3
- Backported numlock fix (RHBZ 1103216)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 11 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.0.0-1
- bump to stable version 1.0.0

* Mon Jan 28 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 0.5.0-1
- version bump
- inih library is no longer required

* Mon Sep 03 2012 Lukas Zapletal <lzap+rpm[@]redhat.com> - 0.3.1-3
- package review

* Wed Aug 29 2012 Lukas Zapletal <lzap+rpm[@]redhat.com> - 0.3.1-2
- package review

* Mon Aug 27 2012 Lukas Zapletal <lzap+rpm[@]redhat.com> - 0.3.1-1
- initial version
