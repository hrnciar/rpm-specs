Summary:        Beep the PC speaker any number of ways
Name:           beep
Version:        1.4.7
Release:        3%{?dist}

License:        GPLv2+
URL:            https://github.com/spkr-beep/beep/

# Upstream github repo: https://github.com/spkr-beep/beep
# hun github repo:      https://github.com/ndim/beep

# Alternative source URL to download:
# curl -L -o spkr-beep-beep-1.4.0-db395a5.tar.gz https://api.github.com/repos/spkr-beep/beep/tarball/db395a53dc862eda80b3c1abf0d9136be97ad15a
# curl -L -o spkr-beep-beep-1.4.1-9ffa7a1.tar.gz https://api.github.com/repos/spkr-beep/beep/tarball/9ffa7a1feb195a60db20792890225b69720984d3
Source0:        https://github.com/spkr-beep/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz


# Fedora specific files
Source1:        README.fedora
Source2:        70-pcspkr-beep.rules
Source3:        90-pcspkr-beep.rules
Source4:        pcspkr-beep.conf


BuildRequires:  gcc
BuildRequires:  glibc-kernheaders
# for the udev macros
BuildRequires:  systemd

Requires(pre):  shadow-utils

# /etc/modprobe.d/
Requires:       kmod
# /etc/udev/rules.d/  and  /usr/lib/udev/rules.d/
Requires:       systemd-udev


%description
Beep allows the user to control the PC speaker with precision,
allowing different sounds to indicate different events. While it
can be run quite happily from the command line, its intended place
of use is within scripts, notifying the user when something
interesting occurs. Of course, it has no notion of what is
interesting, but it is really good at the notifying part.


%prep
%setup -q
install -m 0644 -p %{SOURCE1} README.fedora
sed -i 's|^\.\\" \(\.BR .*\)README.Distro\(.*\)|\1README.fedora\2|' beep.1.in && : #"


%build
make %{?_smp_mflags} COMPILERS=gcc CFLAGS_gcc="-Wall -Wextra -std=gnu99 -pedantic -Werror ${RPM_OPT_FLAGS}" LDFLAGS="${RPM_LD_FLAGS}" CPPFLAGS_gcc=""


%install
rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT" COMPILERS=gcc CFLAGS_gcc="-Wall -Wextra -std=gnu99 -pedantic -Werror ${RPM_OPT_FLAGS}" LDFLAGS="${RPM_LD_FLAGS}" CPPFLAGS_gcc=""

install -d -m 0755              "$RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d/"
install -p -m 0644 "%{SOURCE4}" "$RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d/beep.conf"

install -d -m 0755              "$RPM_BUILD_ROOT%{_udevrulesdir}/"
install -p -m 0644 "%{SOURCE2}" "$RPM_BUILD_ROOT%{_udevrulesdir}/"
install -p -m 0644 "%{SOURCE3}" "$RPM_BUILD_ROOT%{_udevrulesdir}/"


%pre
getent group beep >/dev/null || groupadd -r beep
exit 0


%files
%doc README.fedora
%license %{_pkgdocdir}/COPYING
%doc %{_pkgdocdir}/CHANGELOG
%doc %{_pkgdocdir}/CREDITS
%doc %{_pkgdocdir}/README.md
%doc %{_pkgdocdir}/PERMISSIONS.md
%doc %{_pkgdocdir}/contrib/failure-beeps
%doc %{_pkgdocdir}/contrib/success-beeps
%attr(0755,root,root) %{_bindir}/beep
%{_mandir}/man1/beep.1*
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/modprobe.d/beep.conf
%{_udevrulesdir}/70-pcspkr-beep.rules
%{_udevrulesdir}/90-pcspkr-beep.rules


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan  1 2020 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.4.7-1
- Update to beep-1.4.7
- Install contrib scripts for both successfully and failing sounding beeps.

* Fri Dec 20 2019 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.4.6-1
- Update to beep-1.4.6
- Use BEEP_LOG_LEVEL environment variable for default log level
- Avoid possible bug related to not using va_copy() with a va_list parameter

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr  2 2019 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.4.4-1
- Update to beep-1.4.4
- Install default udev rules to /usr/lib/udev/rules.d/ (not /etc/udev/)
- Give the currently locally logged in user PC speaker access out of the box
- Have beep(1) man page mention README.fedora

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 18 2019 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.4.3-1
- Update to beep-1.4.3

* Tue Jan  8 2019 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.4.1-1
- Update to beep-1.4.1

* Fri Jan  4 2019 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.4.0-1
- Update to beep-1.4.0

* Sat Dec 29 2018 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.3-26
- Stop shipping old sudo related config files
- Refuse to run when run via sudo
- Set up group 'beep' for write access to evdev device with new udev rule
- Update README.fedora to reflect new group permission setup on evdev device

* Fri Dec 28 2018 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.3-25
- guard against directory traversal in /dev/input/ check
- refuse to run if setuid or setgid root
- make the evdev device the first device to look for (does not require root)

* Fri Dec 28 2018 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.3-24
- Actually apply the patches
- Update COPYING with new FSF address
- Fix Patch9 to work as non-git patch (do the rest with shell)
- Proper naming of Patch14
- Exit beep when error accessing API

* Fri Dec 28 2018 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.3-23
- Fix CVE-2018-1000532 and mitigate against related issues (#1595592)
- Fix a number of potential integer overflows

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr  3 2018 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.3-21
- Add CVE-2018-0492 fix.
- Behaviour of multiple -f parameters matches documentation now.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 31 2016 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.3-16
- Use more appropriate sox play example in README.fedora
- Make command line examples more readable in README.fedora

* Tue May 31 2016 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.3-15
- Add shell aliases to allow non-root users to run beep from the shell
- Fix mail address in %%changelog

* Tue May 31 2016 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.3-14
- Document how non-root users can run beep via sudo (#1133231)
- Remove spec file conditional required in Fedora 12 times

* Mon May 16 2016 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.3-13
- Remove useless %%defattr for clarity

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 17 2016 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.3-11
- Do not replace config file modprobe.d/beep.conf (#1087616)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 19 2013 Hans Ulrich Niedermann  <hun@n-dimensional.de> - 1.3-7
- Use new upstream tarball beep-1.3.tar.gz (yes, it has changed!)
- Add a few fixes from upstream git repo
- Move our Makefile cleanup to upstream pull request

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 16 2010 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.3-1
- Update to upstream release beep-1.3

* Fri Jan 22 2010 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.2.2-6
- Ship modprobe config file with alias for pcspkr on F12 and later

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep  7 2008 Hans Ulrich Niedermann <hun@n-dimensional.de> - 1.2.2-3
- Initial package for submission to Fedora
