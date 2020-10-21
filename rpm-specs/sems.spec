Summary:	SIP Express Media Server, an extensible SIP media server
Name:		sems
Version:	1.7.0
Release:	0.4.20200311.git.baad471%{?dist}
URL:		https://github.com/sems-server/%{name}
#Source0:	https://github.com/sems-server/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source0:	https://github.com/sems-server/%{name}/archive/baad471/%{name}-%{version}.tar.gz
License:	GPLv2+
# Will be proposed for inclusion in upstream
Patch1:		sems-0001-Allow-rewrite-of-custom-makefiles-by-CMake.patch
# Fedora-specific
Patch2:		sems-0002-Set-CFG_PREFIX-to-empty-string-by-default.patch
# Fedora-specific
Patch3:		sems-0003-Disable-py_sems-broken.patch
# Fedora-specific
Patch4:		sems-0004-Don-t-use-versioned-dir-for-installing-docs.patch
# Fedora-specific
Patch5:		sems-0005-Use-Python2-explicitly.patch
Patch6:		sems-0006-Use-variable-value-instead-of-prints-within-if.endif.patch
Patch7:		sems-0007-Remove-compat-getos-getarch.patch
# https://github.com/sems-server/sems/pull/146
Patch8:		sems-0008-cmake-fix-symbol-visibility.patch
# Workaround for bug in GCC 10 on s390x (test again in the next builds)
Patch9:		sems-0009-Don-t-copy-byte-which-will-be-replaced-with-NULL-any.patch

%ifarch s390x
%define _lto_cflags %{nil}
%endif

BuildRequires:	cmake >= 3.0
BuildRequires:	flite-devel
BuildRequires:	gcc-c++
BuildRequires:	gsm-devel
BuildRequires:	hiredis-devel
BuildRequires:	ilbc-devel
BuildRequires:	lame-devel
BuildRequires:	libevent-devel
BuildRequires:	libmpg123-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	mISDN-devel
BuildRequires:	mysql++-devel
BuildRequires:	openssl-devel
BuildRequires:	opus-devel
# FIXME disable python2 until upstream adds support for Py3
#BuildRequires:	python2-devel
BuildRequires:	spandsp-devel
BuildRequires:	speex-devel
BuildRequires:	systemd-rpm-macros
BuildRequires:	/usr/bin/git
BuildRequires:	/usr/bin/man
BuildRequires:  git-core-doc
BuildRequires:  groff
BuildRequires:  python2
Requires(pre):  /usr/sbin/useradd
# Disable gateway module
Obsoletes: %{name}-gateway =< 1.3.1
Provides: %{name}-gateway%{?_isa} = %{version}-%{release}
# Disable python module
Obsoletes: %{name}-python
Provides: %{name}-python%{?_isa} = %{version}-%{release}
# FIXME disable python2 until upstream adds support for Py3
Obsoletes: %{name}-conf_auth =< 1.6.0
# FIXME disable python2 until upstream adds support for Py3
Obsoletes: %{name}-ivr =< 1.6.0
# FIXME disable python2 until upstream adds support for Py3
Obsoletes: %{name}-mailbox =< 1.6.0
# FIXME disable python2 until upstream adds support for Py3
Obsoletes: %{name}-pin_collect =< 1.6.0

%description
SEMS (SIP Express Media Server) is very extensible and programmable
SIP media server for SER or OpenSER. The plug-in based SDK enables
you to extend SEMS and write your own applications and integrate new
codec. Voice-mail, announcement and echo plug-ins are already included.
SEMS supports g711u, g711a, GSM06.10 and wav file.

#%package	conf_auth
#Summary:	Conference with authorization
#Requires:	%{name}%{?_isa} = %{version}-%{release}
#Requires:	%{name}-ivr%{?_isa} = %{version}-%{release}

#%description	conf_auth
#Conference with authorization by PIN-numbers.

%package	conference
Summary:	Conferencing application
Requires:	%{name}%{?_isa} = %{version}-%{release}
Obsoletes:	%{name} < 1.2.0

%description	conference
Conferencing application for SEMS.

%package	diameter_client
Summary:	A simple DIAMETER client implementation
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	diameter_client
This is a very simple DIAMETER client implementation. it does
implement only parts of the base protocol, and is not a complete
DIAMETER implementation.

It is used from other modules with the DI API - i.e. other modules
can execute DI functions to add a server connection, or send a
DIAMETER request.

%package	dsm
Summary:	The state machine interpreter for SEMS
Requires:	%{name}%{?_isa} = %{version}-%{release}
Obsoletes:	%{name} < 1.2.0

%description	dsm
DonkeySM is a state machine interpreter for SEMS. Application
or service logic can comfortably and accurately be defined
as state machine, in a simple textual state machine definition
language, and executed by the dsm module as application in SEMS.

%package	early_announce
Summary:	Early announce application
Requires:	%{name}%{?_isa} = %{version}-%{release}
Obsoletes:	%{name} < 1.2.0

%description	early_announce
Early annonce application for SEMS.

%package	g722
Summary:	G.722 support for SEMS
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	g722
This is a wrapper around the g722 codec from the spandsp library.


%package	g729
Summary:	G.729 support for SEMS
BuildRequires:	bcg729-devel
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	g729
This is a wrapper around the g729 codec from the bcg729 library.

#%package	gateway
#Summary:	ISDN gateway for SEMS
#Requires:	%{name}%{?_isa} = %{version}-%{release}

#%description	gateway
#ISDN gateway for SEMS.

%package	gsm
Summary:	GSM support for SEMS
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	gsm
GSM support for SEMS.

%package	ilbc
Summary:	iLBC support for SEMS
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	ilbc
iLBC support for SEMS.

#%package	ivr
#Summary:	IVR functionality for SEMS
#Requires:	python2 >= 2.3
#Requires:	%{name}%{?_isa} = %{version}-%{release}

#%description	ivr
#IVR functionality for SEMS.

#%package	mailbox
#Summary:	Mailbox application
#Requires:	%{name}%{?_isa} = %{version}-%{release}
#Requires:	%{name}-ivr%{?_isa} = %{version}-%{release}

#%description	mailbox
#The mailbox application is a mailbox where callers can leave messages
#for offline or unavailable users and the users can dial in to check their
#messages. It uses an IMAP server as back-end to store the voice messages.

%package	mp3
Summary:	mp3 support for SEMS
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	mp3
mp3 support for SEMS.

%package	opus
Summary:	Opus support for SEMS
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	opus
Opus support for SEMS.

#%package	pin_collect
#Summary:	Collects a PIN
#Requires:	%{name}%{?_isa} = %{version}-%{release}
#Requires:	%{name}-ivr%{?_isa} = %{version}-%{release}

#%description	pin_collect
#This application collects a PIN and then transfers using a
#(proprietary) REFER the call.

#%package	python
#Summary:	Python bindings for SEMS
#BuildRequires:	python2 >= 2.3
#BuildRequires:	python2-sip-devel
#%{?_sip_api:Requires: sip-api(%{_sip_api_major}) >= %{_sip_api}}
#Requires:	python2 >= 2.3
#Requires:	%{name}%{?_isa} = %{version}-%{release}

#%description	python
#Python bindings for SEMS.

%if 0%{?_with_rtmp}
%package	rtmp
Summary:	RTMP support for SEMS
BuildRequires:	librtmp-devel
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	rtmp
RTMP support for SEMS.
%endif

%package	speex
Summary:	Speex support for SEMS
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	speex
Speex support for SEMS.

%package	xmlrpc2di
Summary:	XMLRPC interface for SEMS
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	xmlrpc2di
This module makes the Dynamic Invocation (DI) Interfaces exported
by component modules accessible from XMLRPC. Additionally the built-in
methods calls, get_loglevel and set_loglevel are implemented (like in the
stats UDP server). Additionally, it can be used as client to access
XMLRPC servers.

%prep
%autosetup -p1 -n %{name}-baad4717fdb3c02a63eb4869f31ec33ff8ec1fed
mv ./apps/dsm/fsmc/readme.txt  ./apps/dsm/fsmc/Readme.fsmc.txt
mv doc/README.stats core/plug-in/stats/README.stats

%build
%{cmake} \
	-DSEMS_USE_SPANDSP=yes \
	-DSEMS_USE_LIBSAMPLERATE=yes \
	-DSEMS_USE_ZRTP=NO \
	-DSEMS_USE_MP3=yes \
	-DSEMS_USE_ILBC=yes \
	-DSEMS_USE_G729=yes \
	-DSEMS_USE_OPUS=yes \
	-DSEMS_USE_TTS=yes \
	-DSEMS_USE_OPENSSL=yes \
	-DSEMS_USE_MONITORING=yes \
	-DSEMS_USE_IPV6=yes \
	-DSEMS_CFG_PREFIX= \
	-DSEMS_AUDIO_PREFIX=%{_datadir} \
	-DSEMS_EXEC_PREFIX=%{_prefix} \
	-DSEMS_LIBDIR=%{_lib} \
	-DSEMS_DOC_PREFIX=%{_docdir} \
	-DSEMS_USE_PYTHON=no
%cmake_build

%install
%cmake_install

# FIXME disable python2 until upstream adds support for Py3
rm -f %{buildroot}/%{_sbindir}/%{name}-get-callproperties
rm -f %{buildroot}/%{_sbindir}/%{name}-list-active-calls
rm -f %{buildroot}/%{_sbindir}/%{name}-list-calls
rm -f %{buildroot}/%{_sbindir}/%{name}-list-finished-calls
rm -f %{buildroot}/%{_sbindir}/%{name}-sbc-get-activeprofile
rm -f %{buildroot}/%{_sbindir}/%{name}-sbc-get-regex-map-names
rm -f %{buildroot}/%{_sbindir}/%{name}-sbc-list-profiles
rm -f %{buildroot}/%{_sbindir}/%{name}-sbc-load-callcontrol-modules
rm -f %{buildroot}/%{_sbindir}/%{name}-sbc-load-profile
rm -f %{buildroot}/%{_sbindir}/%{name}-sbc-reload-profile
rm -f %{buildroot}/%{_sbindir}/%{name}-sbc-reload-profiles
rm -f %{buildroot}/%{_sbindir}/%{name}-sbc-set-activeprofile
rm -f %{buildroot}/%{_sbindir}/%{name}-sbc-set-regex-map
rm -f %{buildroot}/%{_sbindir}/%{name}-sbc-teardown-call

install -D -m 0644 -p pkg/rpm/sems.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/%{name}

# install systemd files
install -D -m 0644 -p pkg/rpm/sems.systemd.service %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 -p pkg/rpm/sems.systemd.tmpfiles.d.conf %{buildroot}%{_tmpfilesdir}/%{name}.conf

mkdir -p %{buildroot}%{_localstatedir}/run/%{name}
mkdir -p %{buildroot}%{_localstatedir}/spool/%{name}/voicebox

# Remove installed docs
rm -rf %{buildroot}%{_docdir}/%{name}
rm -rf %{buildroot}%{_sysconfdir}/%{name}/default.template.sample
rm -rf %{buildroot}%{_sysconfdir}/%{name}/sems.conf.default

# remove currently empty conf-file
rm -f %{buildroot}%{_sysconfdir}/%{name}/etc/conf_auth.conf

# add empty directories for audiofiles
mkdir -p %{buildroot}%{_datadir}/%{name}/audio/ann_b2b
mkdir -p %{buildroot}%{_datadir}/%{name}/audio/announcement
mkdir -p %{buildroot}%{_datadir}/%{name}/audio/announce_transfer


%pre
getent passwd %{name} >/dev/null || \
/usr/sbin/useradd -r -c "SIP Media Server"  -d %{_localstatedir}/spool/%{name} -s /sbin/nologin %{name} 2>/dev/null || :


%post
%systemd_post %{name}.service


%preun
%systemd_preun %{name}.service


%files
%dir %{_sysconfdir}/%{name}/
%dir %{_sysconfdir}/%{name}/etc/
%dir %{_libdir}/%{name}/
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/audio/
%dir %{_datadir}/%{name}/audio/ann_b2b/
%dir %{_datadir}/%{name}/audio/announcement/
%dir %{_datadir}/%{name}/audio/announce_transfer/
%dir %{_datadir}/%{name}/audio/annrecorder/
%dir %{_datadir}/%{name}/audio/precoded_announce/
%dir %{_datadir}/%{name}/audio/voicebox/
%dir %{_datadir}/%{name}/audio/voicemail/
%dir %{_datadir}/%{name}/audio/webconference/
%dir %{_libdir}/%{name}/plug-in/
%dir %attr(0755, %{name}, %{name}) %{_localstatedir}/spool/%{name}/
%dir %attr(0750, %{name}, %{name}) %{_localstatedir}/spool/%{name}/voicebox/

%config(noreplace) %{_sysconfdir}/sysconfig/%{name}

%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf

%ghost %dir %attr(0755, %{name}, %{name}) %{_localstatedir}/run/%{name}/

%config(noreplace) %{_sysconfdir}/%{name}/default.template
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/ann_b2b.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/announce_transfer.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/announcement.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/annrecorder.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/app_mapping.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/callback.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/click2dial.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/db_reg_agent.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/echo.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/monitoring.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/msg_storage.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/mwi.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/precoded_announce.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/reg_agent.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/stats.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/voicebox.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/voicemail.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/webconference.conf

%config(noreplace) %{_sysconfdir}/%{name}/etc/auth_b2b.sbcprofile.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/call_timer.sbcprofile.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/cc_call_timer.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/cc_pcalls.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/cc_syslog_cdr.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/codecfilter.sbcprofile.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/prepaid.sbcprofile.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/refuse.sbcprofile.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/replytranslate.sbcprofile.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/sbc.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/src_ipmap.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/sst_b2b.sbcprofile.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/symmetricrtp.sbcprofile.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/transparent.sbcprofile.conf

%doc README
%doc core/plug-in/adpcm/README_G711
%doc core/plug-in/stats/README.stats
%doc doc/figures
%doc doc/Howtostart_noproxy.txt
%doc doc/Howtostart_simpleproxy.txt
%doc doc/Howtostart_voicemail.txt
%doc doc/CHANGELOG
%doc doc/COPYING
%doc doc/Readme.ann_b2b.txt
%doc doc/Readme.announce_transfer.txt
%doc doc/Readme.announcement.txt
%doc doc/Readme.annrecorder.txt
%doc doc/Readme.auth_b2b.txt
%doc doc/Readme.call_timer.txt
%doc doc/Readme.callback.txt
%doc doc/Readme.click2dial.txt
%doc doc/Readme.conf_auth.txt
%doc doc/Readme.echo.txt
%doc doc/Readme.monitoring.txt
%doc doc/Readme.msg_storage.txt
%doc doc/Readme.py_sems.txt
%doc doc/Readme.reg_agent.txt
%doc doc/Readme.registrar_client.txt
%doc doc/Readme.sst_b2b.txt
%doc doc/Readme.sw_prepaid_sip.txt
#%doc doc/Readme.twit.txt
%doc doc/Readme.uac_auth.txt
%doc doc/Readme.voicebox.txt
%doc doc/Readme.voicemail.txt
%doc doc/Readme.webconference.txt
%doc doc/Tuning.txt
#%doc doc/ZRTP.txt

%{_sbindir}/%{name}
# FIXME disable python2 until upstream adds support for Py3
#%{_sbindir}/%{name}-get-callproperties
#%{_sbindir}/%{name}-list-active-calls
#%{_sbindir}/%{name}-list-calls
#%{_sbindir}/%{name}-list-finished-calls
%{_sbindir}/%{name}-logfile-callextract
%{_sbindir}/%{name}-rtp-mux-get-max-frame-age-ms
%{_sbindir}/%{name}-rtp-mux-get-mtu-threshold
%{_sbindir}/%{name}-rtp-mux-set-max-frame-age-ms
%{_sbindir}/%{name}-rtp-mux-set-mtu-threshold
#%{_sbindir}/%{name}-sbc-get-activeprofile
#%{_sbindir}/%{name}-sbc-get-regex-map-names
#%{_sbindir}/%{name}-sbc-list-profiles
#%{_sbindir}/%{name}-sbc-load-callcontrol-modules
#%{_sbindir}/%{name}-sbc-load-profile
#%{_sbindir}/%{name}-sbc-reload-profile
#%{_sbindir}/%{name}-sbc-reload-profiles
#%{_sbindir}/%{name}-sbc-set-activeprofile
#%{_sbindir}/%{name}-sbc-set-regex-map
#%{_sbindir}/%{name}-sbc-teardown-call
%{_sbindir}/%{name}-stats

%{_datadir}/%{name}/audio/beep.wav
%{_datadir}/%{name}/audio/default_en.wav
%{_datadir}/%{name}/audio/annrecorder/beep.wav
%{_datadir}/%{name}/audio/annrecorder/bye.wav
%{_datadir}/%{name}/audio/annrecorder/confirm.wav
%{_datadir}/%{name}/audio/annrecorder/greeting_set.wav
%{_datadir}/%{name}/audio/annrecorder/to_record.wav
%{_datadir}/%{name}/audio/annrecorder/welcome.wav
%{_datadir}/%{name}/audio/annrecorder/your_prompt.wav
%{_datadir}/%{name}/audio/precoded_announce/test.predef
%{_datadir}/%{name}/audio/voicebox/0.wav
%{_datadir}/%{name}/audio/voicebox/1.wav
%{_datadir}/%{name}/audio/voicebox/10.wav
%{_datadir}/%{name}/audio/voicebox/11.wav
%{_datadir}/%{name}/audio/voicebox/12.wav
%{_datadir}/%{name}/audio/voicebox/13.wav
%{_datadir}/%{name}/audio/voicebox/14.wav
%{_datadir}/%{name}/audio/voicebox/15.wav
%{_datadir}/%{name}/audio/voicebox/16.wav
%{_datadir}/%{name}/audio/voicebox/17.wav
%{_datadir}/%{name}/audio/voicebox/18.wav
%{_datadir}/%{name}/audio/voicebox/19.wav
%{_datadir}/%{name}/audio/voicebox/2.wav
%{_datadir}/%{name}/audio/voicebox/20.wav
%{_datadir}/%{name}/audio/voicebox/3.wav
%{_datadir}/%{name}/audio/voicebox/30.wav
%{_datadir}/%{name}/audio/voicebox/4.wav
%{_datadir}/%{name}/audio/voicebox/40.wav
%{_datadir}/%{name}/audio/voicebox/5.wav
%{_datadir}/%{name}/audio/voicebox/50.wav
%{_datadir}/%{name}/audio/voicebox/6.wav
%{_datadir}/%{name}/audio/voicebox/60.wav
%{_datadir}/%{name}/audio/voicebox/7.wav
%{_datadir}/%{name}/audio/voicebox/70.wav
%{_datadir}/%{name}/audio/voicebox/8.wav
%{_datadir}/%{name}/audio/voicebox/80.wav
%{_datadir}/%{name}/audio/voicebox/9.wav
%{_datadir}/%{name}/audio/voicebox/90.wav
%{_datadir}/%{name}/audio/voicebox/and.wav
%{_datadir}/%{name}/audio/voicebox/bye.wav
%{_datadir}/%{name}/audio/voicebox/first_new_msg.wav
%{_datadir}/%{name}/audio/voicebox/first_saved_msg.wav
%{_datadir}/%{name}/audio/voicebox/in_your_voicebox.wav
%{_datadir}/%{name}/audio/voicebox/msg_deleted.wav
%{_datadir}/%{name}/audio/voicebox/msg_end_menu.wav
%{_datadir}/%{name}/audio/voicebox/msg_menu.wav
%{_datadir}/%{name}/audio/voicebox/msg_saved.wav
%{_datadir}/%{name}/audio/voicebox/new_msg.wav
%{_datadir}/%{name}/audio/voicebox/new_msgs.wav
%{_datadir}/%{name}/audio/voicebox/next_new_msg.wav
%{_datadir}/%{name}/audio/voicebox/next_saved_msg.wav
%{_datadir}/%{name}/audio/voicebox/no_more_msg.wav
%{_datadir}/%{name}/audio/voicebox/no_msg.wav
%{_datadir}/%{name}/audio/voicebox/pin_prompt.wav
%{_datadir}/%{name}/audio/voicebox/saved_msg.wav
%{_datadir}/%{name}/audio/voicebox/saved_msgs.wav
%{_datadir}/%{name}/audio/voicebox/x1.wav
%{_datadir}/%{name}/audio/voicebox/x2.wav
%{_datadir}/%{name}/audio/voicebox/x3.wav
%{_datadir}/%{name}/audio/voicebox/x4.wav
%{_datadir}/%{name}/audio/voicebox/x5.wav
%{_datadir}/%{name}/audio/voicebox/x6.wav
%{_datadir}/%{name}/audio/voicebox/x7.wav
%{_datadir}/%{name}/audio/voicebox/x8.wav
%{_datadir}/%{name}/audio/voicebox/x9.wav
%{_datadir}/%{name}/audio/voicebox/you_have.wav
%{_datadir}/%{name}/audio/voicemail/default_en.wav
%{_datadir}/%{name}/audio/voicemail/beep.wav
%{_datadir}/%{name}/audio/webconference/0.wav
%{_datadir}/%{name}/audio/webconference/1.wav
%{_datadir}/%{name}/audio/webconference/2.wav
%{_datadir}/%{name}/audio/webconference/3.wav
%{_datadir}/%{name}/audio/webconference/4.wav
%{_datadir}/%{name}/audio/webconference/5.wav
%{_datadir}/%{name}/audio/webconference/6.wav
%{_datadir}/%{name}/audio/webconference/7.wav
%{_datadir}/%{name}/audio/webconference/8.wav
%{_datadir}/%{name}/audio/webconference/9.wav
%{_datadir}/%{name}/audio/webconference/beep.wav
%{_datadir}/%{name}/audio/webconference/entering_conference.wav
%{_datadir}/%{name}/audio/webconference/first_participant.wav
%{_datadir}/%{name}/audio/webconference/pin_prompt.wav
%{_datadir}/%{name}/audio/webconference/wrong_pin.wav

%{_libdir}/%{name}/plug-in/adpcm.so
%{_libdir}/%{name}/plug-in/ann_b2b.so
%{_libdir}/%{name}/plug-in/announce_transfer.so
%{_libdir}/%{name}/plug-in/announcement.so
%{_libdir}/%{name}/plug-in/annrecorder.so
%{_libdir}/%{name}/plug-in/callback.so
%{_libdir}/%{name}/plug-in/cc_bl_redis.so
%{_libdir}/%{name}/plug-in/cc_call_timer.so
%{_libdir}/%{name}/plug-in/cc_ctl.so
%{_libdir}/%{name}/plug-in/cc_dsm.so
%{_libdir}/%{name}/plug-in/cc_pcalls.so
%{_libdir}/%{name}/plug-in/cc_prepaid.so
%{_libdir}/%{name}/plug-in/cc_registrar.so
%{_libdir}/%{name}/plug-in/cc_syslog_cdr.so
%{_libdir}/%{name}/plug-in/click2dial.so
%{_libdir}/%{name}/plug-in/db_reg_agent.so
%{_libdir}/%{name}/plug-in/echo.so
%{_libdir}/%{name}/plug-in/isac.so
%{_libdir}/%{name}/plug-in/l16.so
%{_libdir}/%{name}/plug-in/monitoring.so
%{_libdir}/%{name}/plug-in/msg_storage.so
%{_libdir}/%{name}/plug-in/mwi.so
%{_libdir}/%{name}/plug-in/precoded_announce.so
%{_libdir}/%{name}/plug-in/reg_agent.so
%{_libdir}/%{name}/plug-in/registrar_client.so
%{_libdir}/%{name}/plug-in/sbc.so
%{_libdir}/%{name}/plug-in/session_timer.so
%{_libdir}/%{name}/plug-in/stats.so
%{_libdir}/%{name}/plug-in/uac_auth.so
%{_libdir}/%{name}/plug-in/voicebox.so
%{_libdir}/%{name}/plug-in/voicemail.so
%{_libdir}/%{name}/plug-in/wav.so
%{_libdir}/%{name}/plug-in/webconference.so

#%files conf_auth
# currently empty
#%config(noreplace) %{_sysconfdir}/%{name}/etc/conf_auth.conf
#%doc doc/Readme.conf_auth.txt
#%{_libdir}/%{name}/ivr/conf_auth.py*

%files conference
%config(noreplace) %{_sysconfdir}/%{name}/etc/conference.conf
%doc doc/Readme.conference.txt
%dir %{_datadir}/%{name}/audio/conference/
%{_libdir}/%{name}/plug-in/conference.so
%{_datadir}/%{name}/audio/conference/beep.wav
%{_datadir}/%{name}/audio/conference/first_participant.wav

%files diameter_client
%doc doc/Readme.diameter_client.txt
%{_libdir}/%{name}/plug-in/diameter_client.so

%files dsm
%config(noreplace) %{_sysconfdir}/%{name}/etc/dsm.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/dsm_in_prompts.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/dsm_out_prompts.conf
%config(noreplace) %{_sysconfdir}/%{name}/etc/mod_regex.conf
%doc doc/dsm
%dir %{_libdir}/%{name}/dsm/
%{_libdir}/%{name}/dsm/mod_conference.so
%{_libdir}/%{name}/dsm/mod_dlg.so
%{_libdir}/%{name}/dsm/mod_groups.so
%{_libdir}/%{name}/dsm/mod_monitoring.so
#%%{_libdir}/%{name}/dsm/mod_mysql.so
#%%{_libdir}/%{name}/dsm/mod_py.so
%{_libdir}/%{name}/dsm/mod_redis.so
%{_libdir}/%{name}/dsm/mod_regex.so
%{_libdir}/%{name}/dsm/mod_sbc.so
%{_libdir}/%{name}/dsm/mod_subscription.so
%{_libdir}/%{name}/dsm/mod_sys.so
%{_libdir}/%{name}/dsm/mod_uri.so
%{_libdir}/%{name}/dsm/mod_utils.so
%{_libdir}/%{name}/plug-in/dsm.so
# DSM scripts
%{_libdir}/%{name}/dsm/early_dbprompt.dsm
%{_libdir}/%{name}/dsm/inbound_call.dsm
%{_libdir}/%{name}/dsm/mobile_push.dsm
%{_libdir}/%{name}/dsm/outbound_call.dsm


%files early_announce
%config(noreplace) %{_sysconfdir}/%{name}/etc/early_announce.conf
%doc doc/Readme.early_announce.txt
%{_libdir}/%{name}/plug-in/early_announce.so

%files g722
%doc core/plug-in/g722/Readme.g722codec
%{_libdir}/%{name}/plug-in/g722.so


%files g729
%doc core/plug-in/g729/Readme.g729.md
%{_libdir}/%{name}/plug-in/g729.so

#%files gateway
#%config(noreplace) %{_sysconfdir}/%{name}/etc/gateway.conf
#%{_libdir}/%{name}/plug-in/gateway.so

%files gsm
%{_libdir}/%{name}/plug-in/gsm.so

%files ilbc
%doc doc/Readme.iLBC.txt
%{_libdir}/%{name}/plug-in/ilbc.so

#%files ivr
#%config(noreplace) %{_sysconfdir}/%{name}/etc/ivr.conf
#%doc doc/Readme.ivr.txt
#%dir %{_libdir}/%{name}/ivr/
#%{_libdir}/%{name}/plug-in/ivr.so
#%{_libdir}/%{name}/ivr/log.py*

#%files mailbox
#%config(noreplace) %{_sysconfdir}/%{name}/etc/mailbox.conf
#%config(noreplace) %{_sysconfdir}/%{name}/etc/mailbox_query.conf
#%doc doc/Readme.mailbox.txt
#%dir %{_datadir}/%{name}/audio/mailbox/
#%dir %{_libdir}/%{name}/ivr/imap_mailbox/
#%{_datadir}/%{name}/audio/mailbox/and.wav
#%{_datadir}/%{name}/audio/mailbox/beep.wav
#%{_datadir}/%{name}/audio/mailbox/bye.wav
#%{_datadir}/%{name}/audio/mailbox/default_en.wav
#%{_datadir}/%{name}/audio/mailbox/first_msg.wav
#%{_datadir}/%{name}/audio/mailbox/msg_deleted.wav
#%{_datadir}/%{name}/audio/mailbox/msg_menu.wav
#%{_datadir}/%{name}/audio/mailbox/msg_saved.wav
#%{_datadir}/%{name}/audio/mailbox/new_msg.wav
#%{_datadir}/%{name}/audio/mailbox/next_msg.wav
#%{_datadir}/%{name}/audio/mailbox/no_msg.wav
#%{_datadir}/%{name}/audio/mailbox/saved_msg.wav
#%{_datadir}/%{name}/audio/mailbox/you_have.wav
#%{_libdir}/%{name}/ivr/mailbox.py*
#%{_libdir}/%{name}/ivr/mailbox_query.py*
#%{_libdir}/%{name}/ivr/imap_mailbox/MailboxURL.py*
#%{_libdir}/%{name}/ivr/imap_mailbox/__init__.py*
#%{_libdir}/%{name}/ivr/imap_mailbox/imap4ext.py*

%files mp3
%doc doc/Readme.mp3plugin.txt
%{_libdir}/%{name}/plug-in/mp3.so

%files opus
%{_libdir}/%{name}/plug-in/opus.so

#%files pin_collect
#%config(noreplace) %{_sysconfdir}/%{name}/etc/pin_collect.conf
#%doc doc/Readme.pin_collect.txt
#%dir %{_datadir}/%{name}/audio/pin_collect/
#%{_datadir}/%{name}/audio/pin_collect/enter_pin.wav
#%{_datadir}/%{name}/audio/pin_collect/welcome.wav
#%{_libdir}/%{name}/ivr/pin_collect.py*

#%files python
#%config(noreplace) %{_sysconfdir}/%{name}/etc/py_sems.conf
#%doc doc/Readme.py_sems.txt
#%{_libdir}/%{name}/plug-in/py_sems.so
#%{_libdir}/%{name}/plug-in/py_sems_log.py*

%if 0%{?_with_rtmp}
%files rtmp
%{_libdir}/%{name}/plug-in/rtmp.so
%endif

%files speex
%{_libdir}/%{name}/plug-in/speex.so

%files xmlrpc2di
%config(noreplace) %{_sysconfdir}/%{name}/etc/xmlrpc2di.conf
%doc doc/Readme.xmlrpc2di.txt
%{_libdir}/%{name}/plug-in/xmlrpc2di.so


%changelog
* Tue Sep 29 20:44:24 CEST 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.7.0-0.4.20200311.git.baad471
- Rebuilt for libevent 2.1.12
- Adjust cmake and python config to fix build (#1865475)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-0.3.20200311.git.baad471
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-0.2.20200311.git.baad471
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 12 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-21
- Remove python2 scripts

* Wed Sep 11 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-20
- Disable python2 support

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-18
- Enable mp3 support

* Fri May 03 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-17
- Added Redis support
- Added call_control modules

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 26 2018 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-15
- Fix FTBFS in Fedora 29+

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 itamar <itamar@ispbrasil.com.br> - 1.6.0-13
- add gcc into buildrequires

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.6.0-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jan 25 2018 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-11
- Fixed FTBFS in Rawhide

* Thu Jan 25 2018 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-10
- Backport fix for recent bcg729 API changes

* Wed Dec 27 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-9
- Enable G.729 plugin

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 12 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.6.0-6
- Build with compat-openssl (fixes FTBFS)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr  8 2016 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-4
- Fix FTBFS with recent GCC.
- Fix linking error

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-2
- Fix building on EL7

* Wed Jun 17 2015 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-1
- Ver. 1.6.0
- Disable py_sems module (terribly broken)
- Disable pre-systemd support

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.4.3-13
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 16 2014 Rex Dieter <rdieter@fedoraproject.org> 1.4.3-10
- rebuild (sip)


* Wed Oct 16 2013 Rex Dieter <rdieter@fedoraproject.org> 1.4.3-9
- rebuild (sip)

* Fri Sep 06 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.4.3-8
- Spec-file cleanup
- Fixed FTBFS in F20+

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 17 2013 Rex Dieter <rdieter@fedoraproject.org> 1.4.3-6
- rebuild (sip)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 05 2012 Rex Dieter <rdieter@fedoraproject.org> 1.4.3-4.1
- rebuild (sip)

* Tue Nov 20 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.4.3-4
- Build against external iLBC
- Allow conditional build with bcg729

* Mon Oct 01 2012 Rex Dieter <rdieter@fedoraproject.org> 1.4.3-3
- rebuild (sip)

* Thu Jul 19 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.4.3-2
- Fixed init-script

* Sat May 05 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.4.3-1
- Ver. 1.4.3 (bugfix release in 1.4.x branch)
- Dropped upstreamed patches

* Fri Apr 27 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.4.2-6
- Fixed systemd installation
- Enabled IPv6 (see rhbz #814229)

* Thu Apr 19 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.4.2-5
- Enabled iLBC ( https://bugzilla.redhat.com/728302#c26 )

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-4
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 24 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.4.2-2
- Works with systemd
- Fix startup failure if sbc module is enabled

* Fri Aug 26 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.4.2-1
- Ver. 1.4.2 (bugfix release in 1.4.x branch)

* Thu Jul 21 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.4.1-1
- Ver. 1.4.1
- Removed obsolete b2b apps: auth_b2b, call_timer, sst_b2b, sw_prepaid_sip
- Disabled gateway module

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan  4 2011 Peter Lemenkov <lemenkov@gmail.com> 1.3.1-4
- Disallow usage of Glibc private functions

* Mon Jan  3 2011 Peter Lemenkov <lemenkov@gmail.com> 1.3.1-3
- Fixed linking issues

* Wed Dec 29 2010 Peter Lemenkov <lemenkov@gmail.com> 1.3.1-2
- Fixed segfault in gateway module
- Properly install email template for voicemail module
- Don't start py_sems by default (causes issues with python2.7)

* Mon Dec 27 2010 Peter Lemenkov <lemenkov@gmail.com> 1.3.1-1
- Ver. 1.3.1 (Bugfix release)

* Wed Sep 29 2010 Peter Lemenkov <lemenkov@gmail.com> 1.3.0-2
- Workaround for missing atomic built-ins in EPEL5 old gcc

* Mon Sep 27 2010 Peter Lemenkov <lemenkov@gmail.com> 1.3.0-1
- Ver. 1.3.0
- Dropped half of all patches
- Dropped binrpcctrl plugin
- Merged into core sipctrl plugin

* Thu Sep 09 2010 Rex Dieter <rdieter@fedoraproject.org> 1.2.1-7
- rebuild (sip)

* Fri Aug 20 2010 Peter Lemenkov <lemenkov@gmail.com> 1.2.1-6
- Fixed severe issue in early_announce module (see %%patch12)

* Sat Jul 31 2010 Toshio Kuratomi <toshio@fedoraproject.org> 1.2.1-5
- rebuild for python 2.7

* Fri Jun 25 2010 Peter Lemenkov <lemenkov@gmail.com> 1.2.1-4
- Fixed escaping variables strategy for  new CMake (and only for new CMake)
- Disable mysql++ in early_announce and conference modules

* Tue Jun  1 2010 Peter Lemenkov <lemenkov@gmail.com> 1.2.1-3
- Fixed config-file generation for EPEL (old CMake)
- Fixed MOD_NAME parameter passing
- Fixed few typos

* Fri May  7 2010 Peter Lemenkov <lemenkov@gmail.com> 1.2.1-2
- Fixed build for EPEL

* Fri Apr 30 2010 Peter Lemenkov <lemenkov@gmail.com> 1.2.1-1
- Ver. 1.2.1
- Dropped upstreamed patches

* Thu Apr  1 2010 Peter Lemenkov <lemenkov@gmail.com> 1.2.0-2
- Fix for CMake 2.4 added

* Wed Mar 31 2010 Peter Lemenkov <lemenkov@gmail.com> 1.2.0-1
- Ver. 1.2.0
- Switched to CMake (and fixed many packaging and linking issues)
- All old patches were either applied upstream or dropped (no longer required)
- Finally removed unixsockctrl interface
- New sub-packages: conference, dsm, early_announce
- Module py_sems was re-enabled

* Mon Nov 16 2009 Rex Dieter <rdieter@fedoraproject.org> 1.1.1-7
- drop BR: sip-devel

* Fri Aug 28 2009 Peter Lemenkov <lemenkov@gmail.com> 1.1.1-6
- g722 enabled back

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.1.1-5
- rebuilt with new openssl

* Mon Aug 17 2009 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.1.1-4
- g722 is a conditional build, until it will work with latest spandsp

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.1.1-2
- disabled py_sems (python) subpackage until upstream fixes sip-4.8
  compatibility

* Sat Jul 11 2009 Peter Lemenkov <lemenkov@gmail.com> 1.1.1-1
- Ver. 1.1.1

* Thu Apr 30 2009 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.1.0-7
- rebuilt

* Sun Apr 19 2009 Peter Lemenkov <lemenkov@gmail.com> 1.1.0-6
- Fix building with GCC 4.4

* Fri Apr 10 2009 Peter Lemenkov <lemenkov@gmail.com> 1.1.0-5
- Use modified tarball (with ilBC sources completely removed)

* Thu Apr  9 2009 Peter Lemenkov <lemenkov@gmail.com> 1.1.0-4
- Internally shipped xmlrpc++ now uses system optflags
- Added more docs
- Moved audiofiles from libdir to datadir
- Removed empty conf_auth.conf
- Splitted out g722 module
- Splitted out xmlrpc2di module

* Wed Apr  8 2009 Peter Lemenkov <lemenkov@gmail.com> 1.1.0-3
- Fixed installation of python files

* Tue Apr  7 2009 Peter Lemenkov <lemenkov@gmail.com> 1.1.0-2
- Module dsm is back
- Disabled OpenSER-specific features (OpenSER is able to manage SEMS
  via SIP-headers).

* Tue Feb 17 2009 Peter Lemenkov <lemenkov@gmail.com> 1.1.0-1
- Ver. 1.1.0
- Disabled module dsm

* Mon Dec  8 2008 Peter Lemenkov <lemenkov@gmail.com> 1.0.0-0.9.svn1160
- New svn snapshot

* Wed Dec  3 2008 Peter Lemenkov <lemenkov@gmail.com> 1.0.0-0.8.svn1095
- Another one fix for audio installation

* Fri Oct 17 2008 Peter Lemenkov <lemenkov@gmail.com> 1.0.0-0.7.svn1095
- Fixed installation of audio files

* Sun Sep 28 2008 Peter Lemenkov <lemenkov@gmail.com> 1.0.0-0.6.svn1095
- New svn rev. 1095
- Some rpmlint-related fixes

* Thu Aug 21 2008 Peter Lemenkov <lemenkov@gmail.com> 1.0.0-0.5.svn
- Dropped upstreamed sems--initscript_fix.diff
- Installation of some audiofiles was fixed upstream

* Tue Aug 19 2008 Peter Lemenkov <lemenkov@gmail.com> 1.0.0-0.4.svn
- Splitted ivr module
- Fixed some rpmlint errors

* Thu Aug 14 2008 Peter Lemenkov <lemenkov@gmail.com> 1.0.0-0.3.svn
- Conditional switch "with_ilbc"

* Thu Aug 14 2008 Peter Lemenkov <lemenkov@gmail.com> 1.0.0-0.2.svn
- Splitted some modules

* Wed Aug 13 2008 Peter Lemenkov <lemenkov@gmail.com> 1.0.0-0.1.svn
- Preliminary ver. 1.0.0 (from svn)

* Sun Jun 29 2008 Peter Lemenkov <lemenkov@gmail.com> 1.0.0-rc1
- GCC4.3 patches upstreamed
- Ver. 1.0.0-rc1

* Wed Mar 26 2008 Peter Lemenkov <lemenkov@gmail.com> 0.10.0
- Initial package for Fedora

* Wed Dec 13 2006 Peter Nixon <peter+rpmspam@suntel.com.tr>
- First version of the spec file for SUSE.

