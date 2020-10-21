Name:		wifi-radar
Summary:	A utility for managing WiFi profiles
Version:	2.0.s10
Release:	13%{?dist}
License:	GPLv2
URL:		http://wifi-radar.tuxfamily.org/
Source0:	http://wifi-radar.tuxfamily.org/pub/%{name}-%{version}.tar.bz2
Source2:	wifi-radar-pam.d
Patch0:		fedora-compliant.patch
BuildArch:	noarch

Requires:	net-tools
Requires:	wireless-tools
Requires:	dhclient
Requires:	usermode
BuildRequires:	desktop-file-utils
BuildRequires:	perl-interpreter
BuildRequires:  %{_bindir}/pathfix.py

%description
WiFi Radar is a straightforward utility, which scans for available wireless
networks, and manages their associated profiles.

%prep
%setup -q

# wifi-radar use by default dhcpcd instead of dhcpclient and look for
# the wpa_supplicant at the wrong location, so we need to fix that
%patch0 -p1 -b .fedora

#fix the upstream desktop file (this Ubuntu's fanboys tsss)
sed -i 's/gksudo -S wifi-radar/wifi-radar/' %{name}.desktop
sed -i 's/wifi-radar.svg/wifi-radar/' %{name}.desktop
sed -i '/FilePattern=wifi-radar/d' %{name}.desktop

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT%{_prefix} 

# fix python shebangs
pathfix.py -i %{__python3} -p -n $RPM_BUILD_ROOT/usr/sbin/wifi-radar

# An empty config file
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}
touch $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}.conf

# The actual executable
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
ln -s consolehelper $RPM_BUILD_ROOT/%{_bindir}/%{name}

# consolehelper file
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/security/console.apps
cat > $RPM_BUILD_ROOT/%{_sysconfdir}/security/console.apps/%{name} <<EOF
USER=root
PROGRAM=%{_sbindir}/%{name}
SESSION=true
EOF

# PAM file
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/pam.d
cp -p %{SOURCE2} $RPM_BUILD_ROOT/%{_sysconfdir}/pam.d/%{name}

desktop-file-install --delete-original --dir $RPM_BUILD_ROOT/%{_datadir}/applications	\
	 $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%files
%doc LICENSE.GPL docs/*
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%config(noreplace) %{_sysconfdir}/security/console.apps/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_sbindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man?/%{name}.*
%{_datadir}/pixmaps/%{name}.*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.s10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.s10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.s10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Luis Bazan <lbazan@fedoraproject.org> - 2.0.s10-10
- Remove py2 dependencie

* Thu Jun 06 2019 Luis Bazan <lbazan@fedoraproject.org> - 2.0.s10-9
- Fix python shebangs BZ #1676208

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.s10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.s10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.s10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.s10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 15 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.s10-4
- Add BR: perl (Fix F26FTBFS).

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.s10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.s10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Robert Mayr <robyduck@fedoraoproject.org> - 2.0.s10-1
- bump to newest release and fix some bugs
- new upstream

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.s08-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.s08-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.s08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.s08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.s08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.s08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 01 2010 Pablo Martin-Gomez <bouska@fedoraproject.org> -2.0.s08-1
- Update to 2.0.s08

* Wed Oct 28 2009 Pablo Martin-Gomez <pablo.martin-gomez@laposte.net> - 2.0.s06-1
- Update to 2.0.s06
- Patch the source in order to be used on Fedora
- The software can't be deamonize, so initscript is useless
- Clean and recycle the spec file

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Sep  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.9.9-1
- fix license tag
- update to 1.9.9

* Sun Sep 17 2006 Ian Pilcher <i.pilcher@comcast.net> 1.9.6-3
- Bump release for FC6 rebuild
- Fix dates in previous changelog entries (It's 2006, duh!)

* Thu Jun  1 2006 Ian Pilcher <i.pilcher@comcast.net> 1.9.6-2
- Use desktop-file-install (and BuildRequire desktop-file-utils)
- Add noreplace flag to config file
- Fix doc directory permissions

* Fri May 12 2006 Ian Pilcher <i.pilcher@comcast.net> 1.9.6-1
- Initial SPEC file for Fedora Extras
