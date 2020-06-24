%global forgeurl https://github.com/ralph-irving/squeezelite/
%global commit   1b7a17616cd2bbd9935c710dc33cda11cd0de45e
%forgemeta

# Raspberry Pi-specific GPIO support.
%ifarch          aarch64 armhfp armv7hl armv7l
%bcond_without   raspberrypi
%endif

# Allow AAC and ALAC, WMA to be played directly in the client rather than
# first being transcoded on the server.  Requires libraries not included
# in Fedora for legal reasons.
%bcond_with      faad
%bcond_with      ffmpeg


Name:            squeezelite
Version:         1.9.6.1210
Release:         1%{?dist}
Summary:         Headless music player for streaming from Logitech Media Server

# Squeezelite is released under the GPLv3 licence.
# It incorporates dsd2pcm, which is BSD licenced.
License:         GPLv3 and BSD

URL:             %{forgeurl}
Source0:         %{forgesource}
Source1:         %{name}.system.service
Source2:         %{name}.user.service
Source3:         %{name}.service.7.md
Source4:         %{name}.sysconfig
Source5:         %{name}.user.preset

BuildRequires:   alsa-lib-devel
%if %{with faad}
BuildRequires:   faad2-devel
%endif
%if %{with ffmpeg}
BuildRequires:   ffmpeg-devel
%endif
BuildRequires:   flac-devel
BuildRequires:   gcc
BuildRequires:   libmad-devel
BuildRequires:   libvorbis-devel
BuildRequires:   lirc-devel
BuildRequires:   mpg123-devel
BuildRequires:   openssl-devel
BuildRequires:   opus-devel
BuildRequires:   opusfile-devel
BuildRequires:   pandoc
BuildRequires:   soxr-devel
BuildRequires:   systemd

Requires(pre):   shadow-utils
%{?systemd_requires}


%description
Squeezelite is a headless client for Logitech Media Server, and can be
used in place of dedicated Squeezebox network music playing hardware.


%prep
%forgesetup


%build
%set_build_flags

%make_build %{?with_ffmpeg:CPPFLAGS+="-I%{_includedir}/ffmpeg"} CPPFLAGS+="-I%{_includedir}/opus" OPTS="-DDSD -DLINKALL -DRESAMPLE -DVISEXPORT -DIR -DGPIO %{?with_raspberrypi:-DRPI} %{?with_ffmpeg:-DFFMPEG} %{?!with_faad:-DNO_FAAD} -DUSE_SSL -DOPUS"

pandoc --to=man --standalone --output=%{name}.service.7 %{SOURCE3}


%install
install -p -D -t %{buildroot}/%{_bindir} %{name}
install -p -D -m 0644 %{SOURCE1} %{buildroot}/%{_unitdir}/%{name}.service
install -p -D -m 0644 %{SOURCE2} %{buildroot}/%{_userunitdir}/%{name}.service
# Change this to %%{_userpresetdir} once Fedora 27 is retired:
install -p -D -m 0644 %{SOURCE5} \
                      %{buildroot}/%{_userunitdir}/../preset/70-%{name}.preset
install -p -D -m 0644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/sysconfig/%{name}
install -p -D -t %{buildroot}/%{_mandir}/man1 -m 0644 doc/%{name}.1
install -p -D -t %{buildroot}/%{_mandir}/man7 -m 0644 %{name}.service.7
mkdir -p %{buildroot}/%{_sharedstatedir}/%{name}


%files
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%dir %attr(-,%{name},%{name}) %{_sharedstatedir}/%{name} 
%doc %{_mandir}/*/*
%doc README.md
%license LICENSE.txt
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_userunitdir}/%{name}.service
%{_userunitdir}/../preset/70-%{name}.preset


%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
    useradd -r -g %{name} -G audio -d %{_sharedstatedir}/%{name} \
        -s /sbin/nologin -c "Squeezelite headless streaming music client" \
        %{name}
exit 0


%post
%systemd_post %{name}.service
%systemd_user_post %{name}.service


%preun
%systemd_preun %{name}.service
%systemd_user_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service


%changelog
* Fri Feb  7 2020 Peter Oliver <rpm@mavit.org.uk> - 1.9.6.1210-1
- Update to 1.9.6.1210, fixing GCC 10 build failure.

* Sat Jan 25 2020 Peter Oliver <rpm@mavit.org.uk> - 1.9.6.1205-3
- Don't start user service in terminal-only sessions.
- Detect failure with systemd if exec fails.

* Fri Jan  3 2020 Peter Oliver <rpm@mavit.org.uk> - 1.9.6.1205-2
- Confusion between arm7hl and armhfp.

* Fri Jan  3 2020 Peter Oliver <rpm@mavit.org.uk> - 1.9.6.1205-1
- Update to version 1.9.6.1205.
- Native Opus support.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2.1165-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Peter Oliver <rpm@mavit.org.uk> - 1.9.2.1165-1
- Update to version 1.9.2.1165.
- Enable HTTPS.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0.1126-4.gita1dd79d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 23 2018 Peter Oliver <rpm@mavit.org.uk> - 1.9.0.1126-3
- Update to revision 1126.

* Tue Jul 31 2018 Peter Oliver <rpm@mavit.org.uk> - 1.9.0.1104-3
- Require gcc for build.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0.1104-2.gitc56dbb0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Peter Oliver <rpm@mavit.org.uk> - 1.9.0.1104-1
- Update to version 1.9.0.1104.

* Mon Apr 30 2018 Peter Oliver <rpm@mavit.org.uk> - 1.9.0.1093-7
- Update to 1.9.0.1093.

* Thu Apr 26 2018 Peter Oliver <rpm@mavit.org.uk> - 1.8.7.1083-6
- Don't replace config file on update.

* Thu Apr 26 2018 Peter Oliver <rpm@mavit.org.uk> - 1.8.7.1083-5
- Mark sysconfig file as config.
- Update man page to mention sysconfig file.

* Thu Apr 26 2018 Peter Oliver <rpm@mavit.org.uk> - 1.8.7.1083-4
- Optionally BuildRequire wiringpi on FedBerry.
- Allow passing of command line args to system service via
  /etc/sysconfig/squeezelite.
- Add missing BSD licence tag.
- Disable user service by default.
- Create config directory before starting user service.

* Thu Apr 26 2018 Peter Oliver <rpm@mavit.org.uk> - 1.8.7.1083-3
- Include systemd scriptlets to restart service on update.

* Wed Apr 25 2018 Peter Oliver <rpm@mavit.org.uk> - 1.8.7.1083-2
- Make Raspberry Pi support optional.

* Wed Apr 25 2018 Peter Oliver <rpm@mavit.org.uk> - 1.8.7.1083-1
- Update to version 1.8.7-1083.

* Tue Apr 24 2018 Peter Oliver <rpm@mavit.org.uk> - 1.8.7.1078-2
- Make optional legally problematic codecs.

* Sun Apr 22 2018 Peter Oliver <rpm@mavit.org.uk> - 1.8.7.1078-1
- Initial package.
