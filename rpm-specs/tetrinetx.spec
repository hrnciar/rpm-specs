Name:           tetrinetx
Version:        1.13.16
Release:        24%{?dist}
Summary:        The GNU TetriNET server

License:        GPLv2
URL:            http://tetrinetx.sourceforge.net/
Source0:        http://switch.dl.sourceforge.net/sourceforge/tetrinetx/%{name}-%{version}+qirc-1.40c.tar.gz
Source1:        tetrinetx.init
Source2:        tetrinetx.logrotate

Requires(pre):  shadow-utils
%{?systemd_requires}
BuildRequires:  gcc
BuildRequires: systemd
BuildRequires:  adns-devel
Requires:       logrotate


%description
Tetrinetx is the GNU TetriNET server written in C. It includes IRC and
Spectator supports. As many other tetrinet servers, it uses IP independent
decryption which allows the server to run behind a router.

TetriNET is a network-based, multiplayer falling bricks game. This package
contains a server for hosting TetriNET games over a public or private network.


%prep
%setup -q -n %{name}-%{version}+qirc-1.40c
# Modify the compile script to use correct directories and use "tetrinetx" as
# the program name
sed -i "s:/usr/local:%{_prefix}:g; s/tetrix\\.linux/tetrinetx/g" -i src/compile.linux

# Modify the default config file to use the correct pid file location
sed -i "s:game\\.pid:%{_localstatedir}/run/tetrinetx/game.pid:" bin/game.conf

# Modify config.h to use correct directories for config files, etc
sed -i "s:game\\.log:%{_localstatedir}/log/tetrinetx/game\\.log:;
        s:game\\.pid:%{_localstatedir}/run/tetrinetx/game\\.pid:;
        s:game\\.winlist:%{_localstatedir}/games/tetrinetx/game\\.winlist:g;
        s:\"game:\"%{_sysconfdir}/tetrinetx/game:g" src/config.h


%build
cd src
./compile.linux %{optflags} %{?_smp_mflags}
cd ..


%install
# Install executable
mkdir -p %{buildroot}%{_bindir}
install -m 755 bin/tetrinetx %{buildroot}%{_bindir}/
# Install configuration files
mkdir -p %{buildroot}%{_sysconfdir}/tetrinetx
install -p -m 644 bin/game.conf %{buildroot}%{_sysconfdir}/tetrinetx
install -p -m 644 bin/game.motd %{buildroot}%{_sysconfdir}/tetrinetx
install -p -m 644 bin/game.pmotd %{buildroot}%{_sysconfdir}/tetrinetx
install -p -m 600 bin/game.secure %{buildroot}%{_sysconfdir}/tetrinetx
# Install system init script
mkdir -p %{buildroot}%{_initrddir}
install -p -m 755 %{SOURCE1} %{buildroot}%{_initrddir}/tetrinetx
# Install logrotate.d entry
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/tetrinetx
# Log files are placed under /var/log/tetrinetx
mkdir -p %{buildroot}%{_localstatedir}/log/tetrinetx
# State data (winlists, etc) for the game will be placed in /var/games/tetrinetx
mkdir -p %{buildroot}%{_localstatedir}/games/tetrinetx
# Tetrinetx pid file goes here
mkdir -p %{buildroot}%{_localstatedir}/run/tetrinetx


%pre
getent group tetrinetx >/dev/null || groupadd -r tetrinetx
getent passwd tetrinetx >/dev/null || \
    useradd -r -g tetrinetx -d %{_localstatedir}/games/tetrinetx -M -s /sbin/nologin \
    -c "No-ip daemon user" tetrinetx

%post
%systemd_post noip.service

%preun
%systemd_preun noip.service

%postun
%systemd_postun_with_restart noip.service

%files
%doc AUTHORS ChangeLog README README.qirc.spectators bin/game.allow.example bin/game.ban.compromise.example bin/game.ban.example
%license COPYING
%{_bindir}/tetrinetx
%{_initrddir}/tetrinetx
%dir %{_sysconfdir}/tetrinetx
%config(noreplace) %{_sysconfdir}/logrotate.d/tetrinetx
%defattr(-,tetrinetx,tetrinetx)
%{_localstatedir}/log/tetrinetx
%{_localstatedir}/games/tetrinetx
%{_localstatedir}/run/tetrinetx
%config(noreplace) %{_sysconfdir}/tetrinetx/*


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 23 2016 Sérgio Basto <sergio@serjux.com> - 1.13.16-16
- Add Packaging:Systemd
- Spec clean up, add License tag.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.16-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.16-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.13.16-4
- Autorebuild for GCC 4.3

* Tue Jan 15 2008 Francois Aucamp <faucamp@fedoraproject.org> - 1.13.16-3
- Changed initscript to comply with LSB standard
- Fixed package License field

* Tue Mar 13 2007 Francois Aucamp <faucamp@csir.co.za> - 1.13.16-2
- Cleaned up sed scripts in %%prep
- Replaced config.h patch with sed script in order to support RPM macros
- Removed trademarked names from %%description

* Tue Jan 30 2007 Francois Aucamp <faucamp@csir.co.za> - 1.13.16-1
- Initial RPM build
- Created patch to make config.h refer to correct directories
- Created tetrinetx init script
- Created tetrinetx logrotate.d entry
