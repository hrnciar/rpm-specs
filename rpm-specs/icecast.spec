# This package builds a daemon-application,
# thus we build with full hardening.
%global _hardened_build 1

# Systemd or SysV?
%if 0%{?fedora} || 0%{?rhel} >= 7
%global with_systemd 1
%endif # 0%{?fedora} || 0%{?rhel} >= 7

# Setup _pkgdocdir if not defined already.
%{!?_pkgdocdir:%global _pkgdocdir	%{_docdir}/%{name}-%{version}}

Name:		icecast
Version:	2.4.4
Release:	4%{?dist}
Summary:	ShoutCast compatible streaming media server

# admin/xspf.xsl:	GPLv2+
# COPYING:		GPLv2 text
# src/fserve.c:		GPLv2
# src/thread/thread.c:	GPLv2+
# src/avl/avl.c:	BSD
# web/xml2json.xslt:	BSD
## In doc package only:
# examples/icecast_auth-1.0.tar.gz:
#   config.guess:	GPLv2+
#   configure:		FSFUL
#   COPYING:		GPLv2 text
#   install-sh:		MIT
#   Makefile.in:	FSFULLR
## Not in any binary package:
# config.guess:		GPLv3+
# configure:		FSFUL
# doc/assets/img/Makefile.in:	FSFULLR
# install-sh:		MIT
License:	GPLv2+ and GPLv2 and BSD
URL:		http://www.%{name}.org/
Source0:	https://downloads.xiph.org/releases/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}.init
Source2:	%{name}.logrotate
Source3:	%{name}.service
Source4:	%{name}.xml
Source5:	status3.xsl

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	automake
BuildRequires:	curl-devel >= 7.10.0
BuildRequires:	libogg-devel >= 1.0
BuildRequires:	libtheora-devel >= 1.0
BuildRequires:	libvorbis-devel >= 1.0
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	openssl-devel
BuildRequires:	speex-devel

Requires:	mailcap

Requires(pre):	shadow-utils

%if 0%{?with_systemd}
BuildRequires:	systemd

%{?systemd_requires}
%else # 0%{?with_systemd}
Requires(post):		/sbin/chkconfig
Requires(preun):	/sbin/chkconfig
Requires(preun):	/sbin/service
Requires(postun):	/sbin/service
%endif # 0%{?with_systemd}

Provides:	streaming-server

%description
Icecast is a streaming media server which currently supports
Ogg Vorbis and MP3 audio streams.  It can be used to create an
Internet radio station or a privately running jukebox and many
things in between.  It is very versatile in that new formats
can be added relatively easily and supports open standards for
communication and interaction.


%package doc
Summary:	Documentation files for %{name}
License:	GPLv2+ and MIT and FSFULLR and FSFUL
BuildArch:	noarch

%description doc
This package contains the documentation files for %{name}.


%prep
%autosetup -p 1
%{_bindir}/find doc/ -type f | xargs %{__chmod} 0644
%{__cp} -a doc/ html/
%{_bindir}/find html/ -name 'Makefile*' | xargs %{__rm} -f
autoreconf -f


%build
%configure \
	--with-curl \
	--enable-largefile \
	--enable-maintainer-mode \
	--with-ogg \
	--with-openssl \
	--enable-shared \
	--with-speex \
	--disable-static \
	--with-theora \
	--with-vorbis \
	--enable-yp
%make_build


%install
%make_install
%{__rm} -fr %{buildroot}%{_datadir}/%{name}/doc
%{__rm} -fr %{buildroot}%{_docdir}/%{name}
%if 0%{?with_systemd}
%{__install} -Dpm 0644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service
%else # 0%{?with_systemd}
%{__install} -Dpm 0755 %{SOURCE1} %{buildroot}%{_initrddir}/%{name}
%endif # 0%{?with_systemd}
%{__install} -Dpm 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
%{__install} -Dpm 0640 %{SOURCE4} %{buildroot}%{_sysconfdir}/%{name}.xml
%{__install} -Dpm 0644 %{SOURCE5} %{buildroot}%{_datadir}/%{name}/web/status3.xsl
%{__mkdir} -p %{buildroot}%{_localstatedir}/log/%{name}	\
	%{buildroot}%{_localstatedir}/run/%{name}	\
	%{buildroot}%{_pkgdocdir}/{conf,examples}
%{__cp} -a html/ AUTHORS ChangeLog COPYING NEWS TODO %{buildroot}%{_pkgdocdir}
%if 0%{?fedora} || 0%{?rhel} >= 7
%{__rm} -f %{buildroot}%{_pkgdocdir}/COPYING
%endif # 0%{?fedora} || 0%{?rhel} >= 7
%{__cp} -a conf/*.dist %{buildroot}%{_pkgdocdir}/conf
%{__cp} -a examples/%{name}_auth-1.0.tar.gz %{buildroot}%{_pkgdocdir}/examples


%pre
%{_bindir}/getent passwd %{name} >/dev/null ||					\
	%{_sbindir}/useradd -M -r -d /usr/share/%{name} -s /sbin/nologin	\
		-c "%{name} streaming server" %{name} > /dev/null 2>&1 || :
exit 0


%post
%if 0%{?with_systemd}
%systemd_post %{name}.service
%else # 0%{?with_systemd}
/sbin/chkconfig --add %{name}
%endif # 0%{?with_systemd}


%preun
%if 0%{?with_systemd}
%systemd_preun %{name}.service
%else # 0%{?with_systemd}
if [ $1 = 0 ]; then
	/sbin/service %{name} stop >/dev/null 2>&1
	/sbin/chkconfig --del %{name}
fi
%endif # 0%{?with_systemd}


%postun
%if 0%{?with_systemd}
%systemd_postun_with_restart %{name}.service
%else # 0%{?with_systemd}
if [ "$1" -ge "1" ]; then
	/sbin/service %{name} condrestart >/dev/null 2>&1
fi
%endif # 0%{?with_systemd}


%files
%config(noreplace) %attr(-,root,%{name}) %{_sysconfdir}/%{name}.xml
%dir %attr(-,%{name},%{name}) %{_localstatedir}/log/%{name}
%doc %dir %{_pkgdocdir}
%if 0%{?fedora} || 0%{?rhel} >= 7
%license COPYING
%else  # 0%{?fedora} || 0%{?rhel} >= 7
%doc %{_pkgdocdir}/COPYING
%endif # 0%{?fedora} || 0%{?rhel} >= 7
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_sysconfdir}/logrotate.d/%{name}
%if 0%{?with_systemd}
%{_unitdir}/%{name}.service
%else # 0%{?with_systemd}
%dir %attr(-,%{name},%{name}) %{_localstatedir}/run/%{name}
%{_initrddir}/%{name}
%endif # 0%{?with_systemd}


%files doc
%if 0%{?fedora} || 0%{?rhel} >= 7
%license %{_datadir}/licenses/%{name}*
%endif # 0%{?fedora} || 0%{?rhel} >= 7
%doc %{_pkgdocdir}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 02 2018 Petr Pisar <ppisar@redhat.com> - 2.4.4-1
- 2.4.4 bump
- License declaration corrected from "GPLv2+" to "GPLv2+ and GPLv2 and BSD and
  MIT and FSFULLR and FSFUL"
- Fix CVE-2018-18820 (buffer overflow in URL auth code) (#1646721)
- Regenerate build scripts

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 28 2018 Björn Esser <besser82@fedoraproject.org> - 2.4.3-1
- Update to v2.4.3 (#1303784)

* Sun Jan 28 2018 Björn Esser <besser82@fedoraproject.org> - 2.4.2-7
- Add Requires: mailcap (#1519830)

* Sun Jan 28 2018 Björn Esser <besser82@fedoraproject.org> - 2.4.2-6
- Remove lots of old cruft

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jun 27 2015 Björn Esser <bjoern.esser@gmail.com> - 2.4.2-1
- update to 2.4.2 (#1236296)
- fix CVE-2015-3026 (#1210198, #1210199, #1210200)
- use %%license on Fedora 22+

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Dec 04 2014 Björn Esser <bjoern.esser@gmail.com> - 2.4.1-1
- update new to release v2.4.1 (#1101950)
- fix CVE-2014-9091 (#1168146, #1168147, #1168148, #1168149)
- fix CVE-2014-9018 (#1165880, #1165882, #1165883, #1165885)
- unified spec-file for el5+ and Fedora
- some improvements to readability
- added doc-subpkg

* Thu Dec 04 2014 Björn Esser <bjoern.esser@gmail.com> - 2.3.3-6
- enabled fully hardened build (#954320)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 14 2012 Andreas Thienemann <andreas@bawue.net> - 2.3.3-1
- Upgrade to new upstream release 2.3.3, fixing #831180, #797184, #768176 and #768175.
- Add systemd reload macro, fixing #814212.
- F18 styled systemd macros, fixing #850153.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 24 2012 Petr Pisar <ppisar@redhat.com> - 2.3.2-7
- Remove obsolete buildroot and defattr declarations from spec file
- Move to systemd (bug #782149)
- Drop unneeded /var/run/icecast because of non-forking systemd unit
  (bug #656601)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 21 2009 Andreas Thienemann <andreas@bawue.net> - 2.3.2-4
- Added SSL support
- Added LSB header to the initscripts
- Reworked config example to contain newest changes
- Added alternative config files and authentication example

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 31 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.3.2-1
- update to 2.3.2
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.3.1-5
- Autorebuild for GCC 4.3

* Mon Nov 06 2006 Jindrich Novy <jnovy@redhat.com> - 2.3.1-4
- rebuild because of the new curl

* Fri Sep 08 2006 Andreas Thienemann <andreas@bawue.net> - 2.3.1-3
- FE6 Rebuild

* Thu May 04 2006 Andreas Thienemann <andreas@bawue.net> 2.3.1-2
- Enabled Theora Streaming

* Fri Feb 03 2006 Andreas Thienemann <andreas@bawue.net> 2.3.1-1
- Updated to icecast 2.3.1-1

* Wed Aug 03 2005 Andreas Thienemann <andreas@bawue.net> 2.2.0-1
- Initial specfile
