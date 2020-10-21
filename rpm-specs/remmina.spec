%global commit0 7ebc497062de66881b71bbe7f54dabfda0129ac2

Name:          remmina
Version:       1.4.8
Release:       1%{?dist}
Summary:       Remote Desktop Client
License:       GPLv2+ and MIT
URL:           http://remmina.org

Source0:       https://gitlab.com/Remmina/Remmina/-/archive/v%{version}/Remmina-%{version}.tar.gz#/%{name}-%{version}.tar.gz

%if 0%{?rhel} >= 7
ExcludeArch:   aarch64
%endif

# Cmake helper file to easy build plugins outside remmina source tree
# See http://www.muflone.com/remmina-plugin-rdesktop/english/install.html which
# use http://www.muflone.com/remmina-plugin-builder/ with remmina bundled source.
# So we can't use it directly only as instructions.
Source1:       pluginBuild-CMakeLists.txt

%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires: cmake >= 3.0.0
%else
BuildRequires: cmake3
%endif
BuildRequires: cups-devel
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: harfbuzz-devel
BuildRequires: intltool
BuildRequires: kf5-kwallet-devel
BuildRequires: libappstream-glib
BuildRequires: libgcrypt-devel
BuildRequires: libsodium-devel
BuildRequires: pkgconfig(appindicator3-0.1)
BuildRequires: pkgconfig(avahi-ui) >= 0.6.30
BuildRequires: pkgconfig(avahi-ui-gtk3) >= 0.6.30
BuildRequires: pkgconfig(freerdp2)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(libssh) >= 0.6
BuildRequires: pkgconfig(libvncserver)
BuildRequires: pkgconfig(spice-client-gtk-3.0)
BuildRequires: pkgconfig(vte-2.91)
BuildRequires: pkgconfig(webkit2gtk-4.0)
BuildRequires: pkgconfig(xkbfile)

# We don't ship the remmina-plugins-telepathy package any longer
Obsoletes:     %{name}-plugins-telepathy < %{version}-%{release}

%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends:    %{name}-plugins-exec
Recommends:    %{name}-plugins-nx
Recommends:    %{name}-plugins-rdp
Recommends:    %{name}-plugins-secret
Recommends:    %{name}-plugins-st
Recommends:    %{name}-plugins-vnc
Recommends:    %{name}-plugins-xdmcp
%else
Requires:      %{name}-plugins-exec
Requires:      %{name}-plugins-nx
Requires:      %{name}-plugins-rdp
Requires:      %{name}-plugins-secret
Requires:      %{name}-plugins-st
Requires:      %{name}-plugins-vnc
Requires:      %{name}-plugins-xdmcp
%endif

%description
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

Remmina supports multiple network protocols in an integrated and consistent
user interface. Currently RDP, VNC, XDMCP and SSH are supported.

Please don't forget to install the plugins for the protocols you want to use.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains header files for developing plugins for
%{name}.


%package        plugins-exec
Summary:        External execution plugin for Remmina Remote Desktop Client
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    plugins-exec
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the plugin to execute external processes (commands or
applications) from the Remmina window.


%package        plugins-secret
Summary:        Keyring integration for Remmina Remote Desktop Client
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-plugins-gnome < %{version}-%{release}
Provides:       %{name}-plugins-gnome%{?_isa} = %{version}-%{release}

%description    plugins-secret
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the plugin with keyring support for the Remmina remote
desktop client.


%package        plugins-nx
Summary:        NX plugin for Remmina Remote Desktop Client
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       nxproxy

%description    plugins-nx
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the NX plugin for the Remmina remote desktop client.


%package        plugins-rdp
Summary:        RDP plugin for Remmina Remote Desktop Client
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    plugins-rdp
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the Remote Desktop Protocol (RDP) plugin for the Remmina
remote desktop client.

%package        plugins-st
Summary:        Simple Terminal plugin for Remmina Remote Desktop Client
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    plugins-st
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the Simple Terminal plugin for the Remmina remote desktop
client.

%package        plugins-vnc
Summary:        VNC plugin for Remmina Remote Desktop Client
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    plugins-vnc
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the VNC plugin for the Remmina remote desktop
client.


%package        plugins-xdmcp
Summary:        XDMCP plugin for Remmina Remote Desktop Client
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       xorg-x11-server-Xephyr

%description    plugins-xdmcp
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the XDMCP plugin for the Remmina remote desktop
client.


%package        plugins-spice
Summary:        SPICE plugin for Remmina Remote Desktop Client
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    plugins-spice
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the SPICE plugin for the Remmina remote desktop
client.


%package        plugins-www
Summary:        WWW plugin for Remmina Remote Desktop Client
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    plugins-www
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the WWW plugin (web browser with authentication) for the
Remmina remote desktop client.


%package        plugins-kwallet
Summary:        KDE Wallet plugin for Remmina Remote Desktop Client
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    plugins-kwallet
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains the KDE Wallet plugin for the Remmina remote desktop
client. It will be activated automatically if KDE Wallet is installed and
running.


%package        gnome-session
Summary:        Gnome Shell session for Remmina kiosk mode
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gnome-session

%description    gnome-session
Remmina is a remote desktop client written in GTK+, aiming to be useful for
system administrators and travelers, who need to work with lots of remote
computers in front of either large monitors or tiny net-books.

This package contains Remmina kiosk mode, including a Gnome Shell session
that shows up under the display manager session menu.

%prep
%autosetup -p1 -n Remmina-v%{version}-%{commit0}

# Remove unsupported entries
sed -i -e '/x-scheme-handler/d' data/desktop/remmina-file.desktop.in

%build
mkdir -p build

%if 0%{?fedora}
# Workaround for Pango on Fedora 31+
export CFLAGS="%{optflags} -I%{_includedir}/harfbuzz"
%endif

%if 0%{?rhel} == 7
export CFLAGS="%{optflags} -std=gnu99"
%endif

%cmake \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DWITH_APPINDICATOR=ON \
    -DWITH_AVAHI=ON \
    -DWITH_FREERDP=ON \
    -DWITH_GCRYPT=ON \
    -DWITH_GETTEXT=ON \
    -DWITH_KIOSK_SESSION=ON \
    -DWITH_LIBSSH=ON \
    -DWITH_SPICE=ON \
    -DWITH_TELEPATHY=OFF \
    -DWITH_VTE=ON

%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}/%{_libdir}/cmake/%{name}/
cp -pr cmake/*.cmake %{buildroot}/%{_libdir}/cmake/%{name}/
cp -pr config.h.in %{buildroot}/%{_includedir}/%{name}/
cp -p %{SOURCE1} %{buildroot}/%{_includedir}/%{name}/

%find_lang %{name}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml

%files -f %{name}.lang
%license LICENSE
%doc AUTHORS ChangeLog README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-file-wrapper
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/actions/*.*
%{_datadir}/icons/hicolor/*/apps/*.*
%{_datadir}/icons/hicolor/*/emblems/remmina-*.svg
%{_datadir}/icons/hicolor/apps/*.svg
%{_datadir}/icons/hicolor/scalable/panel/*.svg
%{_datadir}/mime/packages/*.xml
%{_datadir}/%{name}/
%dir %{_libdir}/remmina/
%dir %{_libdir}/remmina/plugins/
%{_mandir}/man1/%{name}.*
%{_mandir}/man1/%{name}-file-wrapper.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/*.cmake

%files plugins-exec
%{_libdir}/remmina/plugins/remmina-plugin-exec.so

%files plugins-secret
%{_libdir}/remmina/plugins/remmina-plugin-secret.so

%files plugins-nx
%{_libdir}/remmina/plugins/remmina-plugin-nx.so
%{_datadir}/icons/hicolor/*/emblems/remmina-nx-symbolic.svg

%files plugins-rdp
%{_libdir}/remmina/plugins/remmina-plugin-rdp.so
%{_datadir}/icons/hicolor/*/emblems/remmina-rdp-ssh-symbolic.svg
%{_datadir}/icons/hicolor/*/emblems/remmina-rdp-symbolic.svg

%files plugins-st
%{_libdir}/remmina/plugins/remmina-plugin-st.so
%{_datadir}/icons/hicolor/*/emblems/remmina-tool-symbolic.svg

%files plugins-vnc
%{_libdir}/remmina/plugins/remmina-plugin-vnc.so
%{_datadir}/icons/hicolor/*/emblems/remmina-vnc-ssh-symbolic.svg
%{_datadir}/icons/hicolor/*/emblems/remmina-vnc-symbolic.svg

%files plugins-xdmcp
%{_libdir}/remmina/plugins/remmina-plugin-xdmcp.so
%{_datadir}/icons/hicolor/*/emblems/remmina-xdmcp-ssh-symbolic.svg
%{_datadir}/icons/hicolor/*/emblems/remmina-xdmcp-symbolic.svg

%files plugins-spice
%{_libdir}/remmina/plugins/remmina-plugin-spice.so
%{_datadir}/icons/hicolor/*/emblems/remmina-spice-ssh-symbolic.svg
%{_datadir}/icons/hicolor/*/emblems/remmina-spice-symbolic.svg

%files plugins-www
%{_libdir}/remmina/plugins/remmina-plugin-www.so

%files plugins-kwallet
%{_libdir}/remmina/plugins/remmina-plugin-kwallet.so

%files gnome-session
%{_bindir}/gnome-session-remmina
%{_bindir}/remmina-gnome
%{_datadir}/gnome-session/sessions/remmina-gnome.session
%{_datadir}/xsessions/remmina-gnome.desktop
%{_mandir}/man1/gnome-session-remmina.1.*
%{_mandir}/man1/remmina-gnome.1.*

%changelog
* Fri Sep 11 2020 Simone Caronni <negativo17@gmail.com> - 1.4.8-1
- Update to 1.4.8.

* Mon Sep 07 2020 Than Ngo <than@redhat.com> - 1.4.7-4
- Fix FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Simone Caronni <negativo17@gmail.com> - 1.4.7-1
- Update to 1.4.7.

* Fri May 22 2020 Simone Caronni <negativo17@gmail.com> - 1.4.4-1
- Update to 1.4.4.

* Tue Feb 25 2020 Simone Caronni <negativo17@gmail.com> - 1.4.1-1
- Update to 1.4.1.

* Sun Feb 09 2020 Simone Caronni <negativo17@gmail.com> - 1.3.10-2
- Backport patch to fix build with default GCC 10 options.

* Fri Feb 07 2020 Simone Caronni <negativo17@gmail.com> - 1.3.10-1
- Update to 1.3.10.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 06 2019 Simone Caronni <negativo17@gmail.com> - 1.3.6-1
- Update to 1.3.6.

* Fri Sep 06 2019 Simone Caronni <negativo17@gmail.com> - 1.3.5-3
- Allow building on RHEL/CentOS 7.

* Tue Aug 20 2019 Simone Caronni <negativo17@gmail.com> - 1.3.5-2
- Enable KDE Wallet plugin.

* Tue Aug 20 2019 Simone Caronni <negativo17@gmail.com> - 1.3.5-1
- Update to 1.3.5

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 18 2019 Simone Caronni <negativo17@gmail.com> - 1.3.4-1
- Update to 1.3.4.

* Thu Feb 28 2019 Simone Caronni <negativo17@gmail.com> - 1.3.3-1
- Update to 1.3.3.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.32.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 30 2018 Simone Caronni <negativo17@gmail.com> - 1.2.32.1-1
- Update to 1.2.32.1.

* Mon Oct 15 2018 Simone Caronni <negativo17@gmail.com> - 1.2.32-1
- Update to 1.2.32, new Simple Terminal plugin.
- Project moved to Gitlab, update spec file accordingly.

* Mon Aug 20 2018 Simone Caronni <negativo17@gmail.com> - 1.2.31.3-1
- Update to 1.2.31.3.

* Tue Aug 14 2018 Mike DePaulo <mikedep333@gmail.com> - 1.2.31.2-1
- Update to latest stable release 1.2.31.2
- Add remmina-gnome-session subpackage for new Kiosk mode

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.52.20180408.git.6b62986
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.51.20180408.git.6b62986
- Update to latest snapshot (rcgit.29).

* Wed Mar 21 2018 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.50.20180321.git.f467f19
- New snapshot, removes duplicate icon.

* Mon Mar 19 2018 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.49.20180319.git.5f3cc40
- Move checks in the check section.
- New source snapshot (#1553098, #1557572).

* Thu Mar 15 2018 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.48.20180314.git.04e4a99
- Update to latest snapshot post rc27.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.47.20180107.git.d70108c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.0-0.46.20180107.git.d70108c
- Remove obsolete scriptlets

* Tue Jan 16 2018 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.45.20180107.git.d70108c
- Update to latest snapshot.

* Fri Jan 05 2018 Pavel Alexeev <Pahan@Hubbitus.info> - 1.2.0-0.44.rcgit.26
- Update to version v1.2.0-rcgit.26.
- Drop remmina-format-security.patch which seams handled upstream in different way.

* Wed Dec 20 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.43.20171220git08f5b4b
- Update to latest 1.2.0 snapshot (rcgit.25).
- Gnome plugin renamed to secret.
- Add new executor plugin.

* Mon Sep 11 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.42.20170908git205df66
- Update to latest snapshot.
- Trim changelog.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.41.20170724git0387ee0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.40.20170724git0387ee0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 27 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.39.20170724git0387ee0
- Update to latest snapshot (matching with rcgit 19).

* Wed Jul 12 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.38.20170710git89009c8
- Update to latest snapshot.

* Mon Jun 26 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.37.20170622git7e82138
- Rebuild for FreeRDP update.

* Mon Jun 26 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.36.20170622git7e82138
- Update to latest snapshot.

* Mon May 15 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.35.20170510git41c8de6
- Update to latest snapshot.

* Mon Apr 24 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.34.20170424git2c0a77e
- Update to latest snapshot.

* Wed Mar 22 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.33.20170317git4d8d257
- Update to latest snapshot.

* Thu Mar 09 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.32.20170302git1da1fb6
- Remove non-working telepathy plugin.

* Thu Mar 02 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.31.20170302git1da1fb6
- Update to latest snapshot.

* Wed Feb 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.2.0-0.30.20161226gitd1a4a73
- rebuild (libvncserver)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.29.20161226gitd1a4a73
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 09 2017 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.28.20161226gitd1a4a73
- Switch to latest snapshot of the next branch.

* Sat Dec 03 2016 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.27.20161126git35604d5
- Update to latest code drop from the libfreerdp_updates branch.

* Fri Nov 04 2016 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.26.20161104git80a77b8
- Update to latest snapshot.
- Still not building properly with FreeRDP:
  https://github.com/FreeRDP/Remmina/issues/1028

* Fri Oct 14 2016 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.25.20161010gitaeaae39
- Update to latest snapshot.

* Sat Oct 08 2016 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.24.20161004git88f490d
- Update to latest snapshot.

* Tue Sep 20 2016 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.23.20160914git42f5a87
- Update to latest snapshot, update release to follow packaging guidelines.

* Sat Aug 27 2016 Pavel Alexeev <Pahan@Hubbitus.info> - 1.2.0-0.22.git.679bb8e
- Provide GIT_REVISION to cmake for use in version.

* Tue Aug 16 2016 Pavel Alexeev <Pahan@Hubbitus.info> - 1.2.0-0.21.git.679bb8e
- Update to try solve issues with tray icons - https://github.com/FreeRDP/Remmina/issues/944#issuecomment-239913278
- Drop old issue 292 hack.
- Conditionally allow build by hash or pre-releases.

* Fri Aug 12 2016 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.20.git.cbcb19e
- Update to latest snapshot.

* Thu Jun 23 2016 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.19.rcgit.14
- Rebuild for spice-gtk upgrade.

* Tue Jun 21 2016 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.18.rcgit.14
- Update to version 1.2.0-rcgit.14.

* Tue Jun 07 2016 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.17.rcgit.13
- Use "snapshot" name only once in the SPEC file.

* Tue Jun 07 2016 Simone Caronni <negativo17@gmail.com> - 1.2.0-0.16.rcgit.12
- Update to version 12.0-rcgit.13, enable SPICE plugin, update cmake options.

* Fri May 20 2016 David Woodhouse <dwmw2@infradead.org> - 1.2.0-0.15.rcgit.12
- Disable survey, as it has build problems

* Fri May 20 2016 David Woodhouse <dwmw2@infradead.org> - 1.2.0-0.14.rcgit.12
- Update to version 12.0-rcgit.12.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.13.rcgit.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 02 2016 Pavel Alexeev <Pahan@Hubbitus.info> - 1.2.0-0.12.rcgit.7
- Update to version 1.2.0-rcgit.7.

* Fri Jan 01 2016 Pavel Alexeev <Pahan@Hubbitus.info> - 1.2.0-0.11.git.b43697d
- Recommends all plugins by suggestion bz#1241658.
