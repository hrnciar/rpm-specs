Name:		debmirror
Version:	2.33
Release:	2%{?dist}
Summary:	Debian partial mirror script, with ftp and package pool support

License:	GPLv2+
URL:		http://packages.qa.debian.org/d/%{name}.html
Source:		http://ftp.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.xz

BuildArch:	noarch
BuildRequires: perl
BuildRequires: perl-generators
BuildRequires: /usr/bin/pod2man
Requires:	patch
Requires:   ed
Requires:   gnupg
Requires:   rsync
Requires:   coreutils
Requires:   findutils
Requires:   gzip
Requires:   bzip2
Requires:   perl-Net-INET6Glue

%description
This program downloads and maintains a partial local Debian mirror.
It can mirror any combination of architectures, distributions and
sections. Files are transferred by ftp, http, hftp or rsync, and package
pools are fully supported. It also does locking and updates trace files.


%prep
%setup -q -n work

%build


%install
%{__install} -Dp -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
%{__install} -Dp -m 0644 examples/%{name}.conf %{buildroot}%{_sysconfdir}/%{name}.conf

# generate a man page
%{__install} -d %{buildroot}%{_mandir}/man1
pod2man %{name} %{buildroot}%{_mandir}/man1/%{name}.1


%files
%license GPL debian/copyright
%doc debian/changelog debian/NEWS doc/design.txt
%{_mandir}/man1/%{name}.1.gz
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Sérgio Basto <sergio@serjux.com> - 2.33-1
- Update to 2.33

* Mon Oct 07 2019 Sérgio Basto <sergio@serjux.com> - 2.32-1
- Update to 2.32

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Sérgio Basto <sergio@serjux.com> - 2.30-1
- Update to 2.30

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Sérgio Basto <sergio@serjux.com> - 2.29-1
- Update to 2.29

* Fri Apr 20 2018 Sérgio Basto <sergio@serjux.com> - 2.26-2
- Requires /usr/bin/pod2man instead perl-podlators (need it for el6)
- Add License tag
- Add Requires: perl-Net-INET6Glue

* Thu Apr 19 2018 Sérgio Basto <sergio@serjux.com> - 2.26-1
- Update to Debian stable version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 02 2013 Patrick Uiterwijk <patrick@puiterwijk.org> - 2.16-1
- Rebase to upstream 2.16

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.15-2
- Perl 5.18 rebuild

* Mon May 06 2013 Patrick Uiterwijk <puiterwijk@gmail.com> - 2.15-1
- Rebase to upstream 2.15

* Fri Feb 22 2013 Patrick Uiterwijk <puiterwijk@gmail.com> - 2.14-5
- Added BuildRequires: perl-podlators for pod2man

* Thu Feb 14 2013 Patrick Uiterwijk <puiterwijk@gmail.com> - 2.14-4
- Add BuildRequires perl

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Patrick Uiterwijk <puiterwijk@gmail.com> - 2.14-2
- Disabling IPv6 to solve dep problems (INET6Glue is not yet packaged)

* Sat Jul 21 2012 Patrick Uiterwijk <puiterwijk@gmail.com> - 2.14-1
- Updating to upstream 2.14

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr 01 2011 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.8-1
- Avoid trying to get d-i for *-updates suites. Debian bug #619146

* Wed Mar 09 2011 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.7-1
- Upstream released new version:
  http://packages.debian.org/changelogs/pool/main/d/debmirror/current/changelog#versionversion1:2.7

* Wed Feb 09 2011 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.5-1
- Upstream released new version:

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 22 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.4.4-1
- Upstream released new version
  See http://packages.debian.org/changelogs/pool/main/d/debmirror/current/changelog

* Wed Mar 24 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.4.3-1
- Upstream released new version

* Mon Dec 21 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> 2.4-1
- New upstream release
- Change license to GPLv2+ according to copyright file

* Wed Sep 02 2009 Simon Wesp <cassmodiah@fedoraproject.org> - 20090807-1
- New upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070123-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 09 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> - 20070123-8
- Use GPL+ as license
- Use main debian url for Source

* Wed Apr 08 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> - 20070123-7
- Change url to a page with more content
- Use %%{name} macro

* Tue Apr 07 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> - 20070123-6
- Generate a man page from the source
- Add explicit Requires on system commands used

* Tue Apr 07 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> - 20070123-5
- Package cleanup for review

* Sat Nov  1 2008 Javier palacios <javiplx@gmail.com>
- 20070123-2
- Added suggestions from the review process

* Sat Oct 11 2008 Javier palacios <javiplx@gmail.com>
- 20070123-1
- First release

