Name:           mingw-spice-protocol
Version:        0.14.0
Release:        1%{?dist}
Summary:        Spice protocol header files
# Main headers are BSD, controller / foreign menu are LGPL
License:        BSD and LGPLv2+
URL:            http://www.spice-space.org/
Source0:        http://www.spice-space.org/download/releases/spice-protocol-%{version}.tar.bz2

BuildArch:      noarch
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95

# clipboard-race patches: together with patches for vdagent
# and spice-gtk these fix problems interacting with mutter's new
# clipboard manager
# https://bugzilla.redhat.com/show_bug.cgi?id=1755038
# all rebased by Jakub Janků:
# https://github.com/jjanku/spice-protocol/tree/clipboard-race
# https://patchwork.freedesktop.org/patch/293583/
Patch0:         0002-vdagent-introduce-VD_AGENT_CAP_CLIPBOARD_NO_RELEASE_.patch
# https://patchwork.freedesktop.org/patch/293584/
Patch1:         0003-vdagent-introduce-VD_AGENT_CAP_CLIPBOARD_GRAB_SERIAL.patch

%description
Header files describing the spice protocol
and the para-virtual graphics card QXL.


%package -n mingw32-spice-protocol
Summary:        Spice protocol header files
Requires:       pkgconfig

%description -n mingw32-spice-protocol
Header files describing the spice protocol
and the para-virtual graphics card QXL.

%package -n mingw64-spice-protocol
Summary:        Spice protocol header files
Requires:       pkgconfig

%description -n mingw64-spice-protocol
Header files describing the spice protocol
and the para-virtual graphics card QXL.


%prep
%autosetup -p1 -n spice-protocol-%{version}

%build
%mingw_configure
%mingw_make %{?_smp_mflags} V=1

%install
%mingw_make install DESTDIR=%{buildroot}


%files -n mingw32-spice-protocol
%doc COPYING CHANGELOG.md
%{mingw32_includedir}/spice-1
%{mingw32_datadir}/pkgconfig/spice-protocol.pc

%files -n mingw64-spice-protocol
%doc COPYING CHANGELOG.md
%{mingw64_includedir}/spice-1
%{mingw64_datadir}/pkgconfig/spice-protocol.pc


%changelog
* Wed Feb 05 2020 Eduardo Lima (Etrunko) <etrunko@redhat.com> - 0.14.0-1
- Sync with spice-protocol version 0.14.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.12.15-1
- new version

* Fri Jul 13 2018 Victor Toso <victortoso@redhat.com> - 0.12.14-1
- Update to 0.12.14

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.12.13-1
- new version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 07 2016 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.12.12-1
- new version

* Fri Mar 11 2016 Marc-André Lureau <marcandre.lureau@redhat.com> 0.12.11-1
- Update to 0.12.11 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 01 2015 Christophe Fergeau <cfergeau@redhat.com> 0.12.10-1
- Update to 0.12.10 - Add python scripts and .proto files used
  to generate spice-gtk/spice-server marshalling C code

* Tue Jun 30 2015 Christophe Fergeau <cfergeau@redhat.com> 0.12.8-1
- Update to release 0.12.8

* Tue Jun 16 2015 Fabiano Fidêncio <fidencio@redhat.com> - 0.12.7-1
- Update to release 0.12.7

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb  1 2013 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.12.4-1
- Update to release 0.12.4

* Thu Jan 03 2013 Gerd Hoffmann <kraxel@redhat.com> - 0.12.2
- Update to release 0.12.2

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 14 2012 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.10.1-1
- Update to release 0.10.1
- Update to mingw64 packaging guideline

* Wed Mar 07 2012 Kalev Lember <kalevlember@gmail.com> - 0.8.0-4
- Renamed the source package to mingw-spice-protocol (#801030)
- Modernize the spec file
- Use mingw macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.8.0-3
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Apr 26 2011 Gerd Hoffmann <kraxel@redhat.com> - 0.8.0-1
- Update to version 0.8.0.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 30 2010 Gerd Hoffmann <kraxel@redhat.com> - 0.6.1-1
- Update to version 0.6.1.

* Fri Sep 17 2010 Gerd Hoffmann <kraxel@redhat.com> - 0.6.0-1
- Update to version 0.6.0.

* Tue Aug 3 2010 Gerd Hoffmann <kraxel@redhat.com> - 0.5.3-2
- Update to version 0.5.3.
- Change %%define to %%global.
- Drop build dependencies which are not needed.

* Tue Jul 13 2010 Gerd Hoffmann <kraxel@redhat.com> - 0.5.2-1
- Initial package.
