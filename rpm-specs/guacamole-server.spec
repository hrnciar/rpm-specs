%global username guacd

# Can be rebuilt with FFmpeg/H264 support enabled by passing "--with=ffmpeg" to
# mock/rpmbuild; or by globally setting these variable:
#global _with_ffmpeg 1

Name:           guacamole-server
Version:        1.1.0
Release:        6%{?dist}
Summary:        Server-side native components that form the Guacamole proxy
License:        ASL 2.0
URL:            http://guac-dev.org/

Source0:        https://github.com/apache/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.sysconfig
Source2:        %{name}.service

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  freerdp-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  libwebsockets-devel
BuildRequires:  systemd-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(freerdp2)
BuildRequires:  pkgconfig(freerdp-client2)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libtelnet)
BuildRequires:  pkgconfig(libvncserver)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(ossp-uuid)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(winpr2)

%{?_with_ffmpeg:
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
}

%description
Guacamole is an HTML5 remote desktop gateway.

Guacamole provides access to desktop environments using remote desktop protocols
like VNC and RDP. A centralized server acts as a tunnel and proxy, allowing
access to multiple desktops through a web browser.

No browser plugins are needed, and no client software needs to be installed. The
client requires nothing more than a web browser supporting HTML5 and AJAX.

The main web application is provided by the "guacamole-client" package.

%package -n libguac
Summary:        The common library used by all C components of Guacamole

%description -n libguac
libguac is the core library for guacd (the Guacamole proxy) and any protocol
support plugins for guacd. libguac provides efficient buffered I/O of text and
base64 data, as well as somewhat abstracted functions for sending Guacamole
instructions.

%package -n libguac-devel
Summary:        Development files for %{name}
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libguac-devel
The libguac-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n libguac-client-kubernetes
Summary:        Kubernetes pods terminal support for guacd
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libguac-client-kubernetes
libguac-client-kubernetes is a protocol support plugin for the Guacamole proxy
(guacd) which provides support for attaching to terminals of containers running
in Kubernetes pods.

%package -n libguac-client-rdp
Summary:        RDP support for guacd
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libguac-client-rdp
libguac-client-rdp is a protocol support plugin for the Guacamole proxy (guacd)
which provides support for RDP, the proprietary remote desktop protocol used by
Windows Remote Deskop / Terminal Services, via the libfreerdp library.

%package -n libguac-client-ssh
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Summary:        SSH support for guacd

%description -n libguac-client-ssh
libguac-client-ssh is a protocol support plugin for the Guacamole proxy (guacd)
which provides support for SSH, the secure shell.

%package -n libguac-client-vnc
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Summary:        VNC support for guacd

%description -n libguac-client-vnc
libguac-client-vnc is a protocol support plugin for the Guacamole proxy (guacd)
which provides support for VNC via the libvncclient library (part of
libvncserver).

%package -n libguac-client-telnet
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Summary:        Telnet support for guacd

%description -n libguac-client-telnet
libguac-client-telnet is a protocol support plugin for the Guacamole proxy
(guacd) which provides support for Telnet via the libtelnet library.

%package -n guacd
Summary:        Proxy daemon for Guacamole
Requires(pre):  shadow-utils
Requires:       libguac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd

%description -n guacd
guacd is the Guacamole proxy daemon used by the Guacamole web application and
framework to translate between arbitrary protocols and the Guacamole protocol.

%prep
%autosetup

%build
autoreconf -vif
%configure \
  --disable-silent-rules \
  --disable-static

%make_build
cd doc/
doxygen Doxyfile

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete
cp -fr doc/doxygen-output/html .
%if 0%{?rhel} == 6
rm -f html/installdox
%endif

mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -p -m 644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/guacd
mkdir -p %{buildroot}%{_sharedstatedir}/guacd

# Systemd unit files
mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 -D %{SOURCE2} %{buildroot}%{_unitdir}/guacd.service

%pre -n guacd
getent group %username >/dev/null || groupadd -r %username &>/dev/null || :
getent passwd %username >/dev/null || useradd -r -s /sbin/nologin \
    -d %{_sharedstatedir}/guacd -M -c 'Guacamole proxy daemon' -g %username %username &>/dev/null || :
exit 0

%post -n guacd
%systemd_post guacd.service

%preun -n guacd
%systemd_preun guacd.service

%postun -n guacd
%systemd_postun_with_restart guacd.service

%ldconfig_scriptlets -n libguac

%ldconfig_scriptlets -n libguac-client-kubernetes

%ldconfig_scriptlets -n libguac-client-rdp

%ldconfig_scriptlets -n libguac-client-ssh

%ldconfig_scriptlets -n libguac-client-vnc

%ldconfig_scriptlets -n libguac-client-telnet

%files -n libguac
%license LICENSE
%doc README CONTRIBUTING
%{_libdir}/libguac.so.*

%files -n libguac-devel
%doc html
%{_includedir}/*
%{_libdir}/libguac.so

# The libguac source code dlopen's these plugins, and they are named without
# the version in the shared object; i.e. "libguac-client-$(PROTOCOL).so".

%files -n libguac-client-kubernetes
%{_libdir}/libguac-client-kubernetes.so
%{_libdir}/libguac-client-kubernetes.so.*

%files -n libguac-client-rdp
%{_libdir}/libguac-client-rdp.so
%{_libdir}/libguac-client-rdp.so.*
%{_libdir}/freerdp2/*.so

%files -n libguac-client-ssh
%{_libdir}/libguac-client-ssh.so
%{_libdir}/libguac-client-ssh.so.*

%files -n libguac-client-vnc
%{_libdir}/libguac-client-vnc.so
%{_libdir}/libguac-client-vnc.so.*

%files -n libguac-client-telnet
%{_libdir}/libguac-client-telnet.so
%{_libdir}/libguac-client-telnet.so.*

%files -n guacd
%config(noreplace) %{_sysconfdir}/sysconfig/guacd
%{_bindir}/guaclog
%{?_with_ffmpeg:
%{_bindir}/guacenc
%{_mandir}/man1/guacenc.1.*
}
%{_mandir}/man1/guaclog.1.*
%{_mandir}/man5/guacd.conf.5.*
%{_mandir}/man8/guacd.8.*
%{_sbindir}/guacd
%{_unitdir}/guacd.service
%attr(750,%{username},%{username}) %{_sharedstatedir}/guacd

%changelog
* Fri May 22 2020 Simone Caronni <negativo17@gmail.com> - 1.1.0-6
- Rebuild for updated FreeRDP.

* Sat Feb 08 2020 Simone Caronni <negativo17@gmail.com> - 1.1.0-5
- Update to final 1.1.0, switch to FreeRDP 2.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4.20190711git1a9d1e8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 02 2019 Peter Robinson <pbrobinson@fedoraproject.org> - 1.1.0-3.20190711git1a9d1e8
- Rebuild for libwebsockets 3.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2.20190711git1a9d1e8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Simone Caronni <negativo17@gmail.com> - 1.1.0-1.20190711git1a9d1e8
- Update to 1.1.0 snapshot, enable Kubernetes plugin.
- Fix license.
- Drop RHEL 6 support.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Simone Caronni <negativo17@gmail.com> - 1.0.0-1
- Update to version 1.0.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Simone Caronni <negativo17@gmail.com> - 0.9.14-1
- Update to 0.9.14.
- Update SPEC file.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 15 2017 Simone Caronni <negativo17@gmail.com> - 0.9.13-4
- Update to final 0.9.13.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-5.20170521git6d2cfda
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-4.20170521git6d2cfda
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 23 2017 Simone Caronni <negativo17@gmail.com> - 0.9.13-3.20170521git6d2cfda
- Update to latest snapshot.

* Tue Mar 21 2017 Simone Caronni <negativo17@gmail.com> - 0.9.13-2.20170317git516c4a0
- Update to 0.9.13 snapshot, fix FTBFS on Fedora 26+.

* Tue Mar 21 2017 Simone Caronni <negativo17@gmail.com> - 0.9.11-3
- Build requirement compat-freerdp12 has been renamed to freerdp1.2.

* Thu Mar 02 2017 Simone Caronni <negativo17@gmail.com> - 0.9.11-2
- Add conditional to build with optional FFmpeg support.

* Thu Mar 02 2017 Simone Caronni <negativo17@gmail.com> - 0.9.11-1
- Update to 0.9.11.
- Require compatibility FreeRDP package where FreeRDP 2.x is the default and
  always enable build of the RDP plugin.

* Wed Feb 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.9.10-4
- FTBFS: drop -Werror, --without-rpd on f25+
- %%build: --disable-silent-rules

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 0.9.10-2
- Rebuild (libwebp)

* Mon Jan 09 2017 Simone Caronni <negativo17@gmail.com> - 0.9.10-1
- Update to 0.9.10.

* Sun Oct 09 2016 Simone Caronni <negativo17@gmail.com> - 0.9.9-2
- Restore Epoch on all requirements; make it more flexible for rebases.

* Fri Apr 15 2016 Simone Caronni <negativo17@gmail.com> - 0.9.9-1
- Update to 0.9.9.
- Add libwebp as a build requirement.
- Add a temporary switch to allow compiling in GCC 6.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 11 2015 Simone Caronni <negativo17@gmail.com> - 0.9.8-3
- Use proper conditionals for freerdp build.

* Mon Nov 30 2015 Simone Caronni <negativo17@gmail.com> - 0.9.8-2
- Make FreeRDP conditional and disable it momentarily.

* Fri Sep 11 2015 Simone Caronni <negativo17@gmail.com> - 0.9.8-1
- Update to 0.9.8.

* Tue Jul 14 2015 Simone Caronni <negativo17@gmail.com> - 0.9.7-1
- Update to 0.9.7.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Simone Caronni <negativo17@gmail.com> - 0.9.6-1
- Update to 0.9.6.

* Tue Mar 17 2015 David Woodhouse <dwmw2@infradead.org> - 0.9.5-3
- API updates for new FreeRDP snapshot.

* Wed Feb 25 2015 Simone Caronni <negativo17@gmail.com> - 0.9.5-2
- Add license macro.

* Tue Feb 24 2015 Simone Caronni <negativo17@gmail.com> - 0.9.5-1
- Update to 0.9.5.
- Remove upstreamed patch.

* Thu Jan 08 2015 Simone Caronni <negativo17@gmail.com> - 0.9.4-1
- Add patch for FreeRDP 1.2.0 beta 1 refresh (1.2.0-beta1+android9).
- Update to 0.9.4.

* Mon Oct 06 2014 Simone Caronni <negativo17@gmail.com> - 0.9.3-1
- Update to 0.9.3.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 23 2014 Simone Caronni <negativo17@gmail.com> - 0.9.2-1
- Update to 0.9.2.
- Add OOSP UUID library build requirement.

* Mon Jul 21 2014 Simone Caronni <negativo17@gmail.com> - 0.9.1-6
- Update environment in service file.

* Mon Jul 21 2014 Simone Caronni <negativo17@gmail.com> - 0.9.1-5
- Add patch for FreeRDP 1.2.0 beta 1 support.
- Use automatic dependency logic for FreeRDP libraries.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun 03 2014 Simone Caronni <negativo17@gmail.com> - 0.9.1-3
- There is now VNC support (libvncserver) in all EPEL 7 arches.

* Mon May 26 2014 Simone Caronni <negativo17@gmail.com> - 0.9.1-2
- There is no VNC support (libvncserver) in EPEL 7 ppc/ppc64.

* Mon May 26 2014 Simone Caronni <negativo17@gmail.com> - 0.9.1-1
- Update to 0.9.1.
- Removed upstreamed patch.
- Enable new telnet plugin.

* Fri Apr 18 2014 Simone Caronni <negativo17@gmail.com> - 0.9.0-1
- Update to 0.9.0.
- Removed upstreamed patch.
- Backport fixes from 0.9.1 to fix build.

* Mon Nov 18 2013 Simone Caronni <negativo17@gmail.com> - 0.8.3-5
- Update patch for new autoconf.

* Mon Nov 18 2013 Simone Caronni <negativo17@gmail.com> - 0.8.3-4
- Require FreeRDP version >= 1.0.2 to avoid RDP refresh problems.

* Thu Sep 05 2013 Simone Caronni <negativo17@gmail.com> - 0.8.3-3
- Add autoconf patch for RHEL autconf compatibility.

* Mon Sep 02 2013 Simone Caronni <negativo17@gmail.com> - 0.8.3-2
- Add specific EPEL 6 workaround for really old autoconf version.

* Wed Aug 28 2013 Simone Caronni <negativo17@gmail.com> - 0.8.3-1
- Update to 0.8.3.
- Drop upstreamed patch.

* Tue Jul 30 2013 Simone Caronni <negativo17@gmail.com> - 0.8.2-2
- SysV init script was overwritten by mistake in SCM.

* Tue Jul 16 2013 Simone Caronni <negativo17@gmail.com> - 0.8.2-1
- First build.
