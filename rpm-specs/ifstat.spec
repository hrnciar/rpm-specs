Summary: Interface statistics
Name: ifstat
Version: 1.1
Release: 31%{?dist}
License: GPLv2+
URL: http://gael.roualland.free.fr/ifstat/
Source0: http://gael.roualland.free.fr/ifstat/ifstat-%{version}.tar.gz
Patch0: ifstat-destdir.patch
Patch1: ifstat-UTF8.patch
BuildRequires: net-snmp-devel
BuildRequires: gcc

%description
ifstat(1) is a little tool to report interface activity like vmstat/iostat do.
In addition, ifstat can poll remote hosts through SNMP if you have the ucd-snmp
library. It will also be used for localhost if no other known method works (You
need to have snmpd running for this though).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	--enable-debug
# debug is needed for generating debug_info rpm

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%files
%doc COPYING HISTORY README TODO
%{_mandir}/man1/ifstat.1*
%{_bindir}/ifstat

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Adam Williamson <awilliam@redhat.com> - 1.1-28
- Rebuild for new net-snmp

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.1-26
- add gcc into buildrequires

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.1-12
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 03 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.1-9
- rebuild for new openssl

* Thu Oct 28 2008 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.1-8
- Changes from  bugzilla #463922 Comment #15 From Mamoru Tasaka ->
- Change the release number to X%%{?dist} (2%%{?dist}, for example)
- Files under %%_mandir are automatically marked as %%doc.

* Thu Oct 25 2008 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.1-1.7
- Changes from  bugzilla #463922 Comment #12 From Michael Schwendt ->
- fix license tag, Licence is "GPLv2+" not "GPLv2"
- Convert files to UTF8 running iconv and generating a patch

* Thu Sep 30 2008 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.1-1.6
- Changes from  bugzilla #463922 Comment #6 From Mamoru Tasaka ->
- remove -s from Makefile, and add --enable-debug to re-enable
- building of debuginfo-rpm package again

* Thu Sep 30 2008 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.1-1.5
- disable building of debuginfo-rpm package

* Thu Sep 29 2008 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.1-1.4
- Changes from  bugzilla #463922 Comment #2 From Manuel Wolfshant ->
- replace from %%makeinstall to make install, include DESTDIR patch

* Thu Sep 25 2008 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.1-1.3
- Rebuild for Fedora 10.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1-1.2
- Rebuild for Fedora Core 5.

* Sun Nov 14 2004 Dag Wieers <dag@wieers.com> - 1.1-1
- Updated to release 1.1.

* Mon Oct 06 2003 Dag Wieers <dag@wieers.com> - 1.0-0
- Initial package. (using DAR)
