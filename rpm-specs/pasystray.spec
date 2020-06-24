Name:           pasystray
Version:        0.6.0
Release:        11%{?dist}
Summary:        PulseAudio system tray
License:        LGPLv2+
URL:            https://github.com/christophgysin/pasystray

Source0:        https://github.com/christophgysin/pasystray/archive/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  automake
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  desktop-file-utils

%description
A replacement for the deprecated padevchooser.
pasystray allows setting the default PulseAudio source/sink and moving streams
on the fly between sources/sinks without restarting the client applications.

%prep
%setup -q

%build
autoreconf -i
%configure
make %{?_smp_mflags}

%install
%make_install

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_mandir}/man1/%{name}.1*
%license LICENSE
%doc README.md

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Michael Simacek <msimacek@redhat.com> - 0.6.0-7
- Add BR on gcc and make

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.0-5
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 17 2016 Michael Simacek <msimacek@redhat.com> - 0.6.0-1
- Update to upstream version 0.6.0

* Sun Jun 19 2016 Michael Simacek <msimacek@redhat.com> - 0.5.2-1
- Initial packaging
