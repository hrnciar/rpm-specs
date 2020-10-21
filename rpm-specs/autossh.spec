Summary: Utility to autorestart SSH tunnels
Name: autossh
Version: 1.4g
Release: 3%{?dist}
License: BSD
URL: https://www.harding.motd.ca/autossh/
Source0: https://www.harding.motd.ca/autossh/autossh-1.4g.tgz
Source1: autossh@.service
Source2: README.service
BuildRequires:  gcc
BuildRequires: /usr/bin/ssh
BuildRequires: systemd
%{?systemd_requires}
Requires(pre): shadow-utils
Requires: /usr/bin/ssh

%description
autossh is a utility to start and monitor an ssh tunnel. If the tunnel
dies or stops passing traffic, autossh will automatically restart it.

%prep
%setup -q
cp -p %{SOURCE2} .

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/autossh
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
mkdir -p examples

cp -p autossh.host rscreen examples
chmod 0644 examples/*

install -m 0755 -p autossh $RPM_BUILD_ROOT%{_bindir}
cp -p autossh.1 $RPM_BUILD_ROOT%{_mandir}/man1

install -m 0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}

%pre
getent group autossh >/dev/null || groupadd -r autossh
getent passwd autossh >/dev/null || \
    useradd -r -g autossh -d %{_sysconfdir}/autossh -s %{_sbindir}/nologin \
    -c "autossh service account" autossh
exit 0

%post
%systemd_post "autossh@*.service"

%preun
%systemd_preun "autossh@*.service"

%postun
%systemd_postun_with_restart "autossh@*.service"


%files
%doc CHANGES README README.service
%doc examples
%{_bindir}/*
%attr(750,autossh,autossh) %dir %{_sysconfdir}/autossh/
%{_mandir}/man1/*
%{_unitdir}/*

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4g-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4g-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Alexander Boström <abo@root.snowtree.se> - 1.4g-1
- Upgrade to 1.4g

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4e-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4e-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4e-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4e-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4e-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4e-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4e-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 23 2016 Ville SkyttÃ¤ <ville.skytta@iki.fi> - 1.4e-3
- Add systemd service

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4e-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 12 2015 Alexander Boström <abo@root.snowtree.se> - 1.4e-1
- Upgrade to 1.4e

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4c-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4c-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4c-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4c-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4c-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4c-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4c-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 14 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.4c-2
- Patch build to honor $LDFLAGS.

* Sun Oct 30 2011 Alexander Boström <abo@root.snowtree.se> - 1.4c-1
- Upgrade to 1.4c

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4a-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 15 2008 Chris Ricker <kaboom@oobleck.net> 1.4a-1
- new version

* Mon Sep 11 2006 Chris Ricker <kaboom@oobleck.net> 1.3-4
- Bump and rebuild

* Tue Feb 14 2006 Chris Ricker <kaboom@oobleck.net> 1.3-3
- Bump and rebuild

* Fri Jun 03 2005 Chris Ricker <kaboom@oobleck.net> 1.3-2%{?dist}
- Add dist tag

* Fri Jun 03 2005 Chris Ricker <kaboom@oobleck.net> 1.3-2
- Changes from Ville Skyttä (use mkdir -p, remove extraneous attr)

* Tue Apr 26 2005 Chris Ricker <kaboom@oobleck.net> 1.3-1
- Initial package
