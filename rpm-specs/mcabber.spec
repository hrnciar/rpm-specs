Name:           mcabber
Version:        1.1.0
Release:        5%{?dist}
Summary:        Console Jabber instant messaging client

License:        GPLv2+
URL:            https://mcabber.com
Source0:        http://mcabber.com/files/%{name}-%{version}.tar.bz2
Patch0:         mcabber-fno-common-fix.patch

BuildRequires:  gcc
BuildRequires:  enchant-devel
BuildRequires:  gpgme-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  glib2-devel
BuildRequires:  gettext-devel
BuildRequires:  libotr-devel >= 4.0.0
BuildRequires:  loudmouth-devel
BuildRequires:  libtool

%package devel
Summary: Development files for mcabber
Requires: %{name} = %{version}-%{release} pkgconfig

%description
mcabber is a console Jabber instant messaging/chat client with SSL support, MUC
(Multi-User Chat) support, history logging, commands completion, and external
action triggers.

%description devel
Headers and miscellaneous files used for building projects using mcabber

%prep
%autosetup -p1

%build
bash autogen.sh
%configure --disable-dependency-tracking --enable-enchant --enable-otr
%make_build

%install
%make_install

# Let's get the executable bits off the contrib files, avoiding unwanted deps.
find contrib/ -type f | xargs chmod -x

%files
%doc contrib AUTHORS ChangeLog NEWS README doc/README_PGP.txt TODO *.example
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}
%{_libdir}/%{name}

%files devel
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 03 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.0-1
- Update to 1.1.0
- Clean spec

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5

* Sat Dec 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.4-2
- Rebuild for gpgme 1.18

* Wed Nov 30 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4

* Wed Sep 21 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3

* Sat May 28 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.0.2-1
- New upstream release

* Thu Jan 28 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.0.1-1
- New upstream release

* Sun Oct 25 2015 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.0.0-0.20151025hgea90906cb691
- New upstream release and get closer to dev since big fixes are being committed

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Aug 21 2014 Till Maas <opensource@till.name> - 0.10.3-1
- Update to new upstream release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Oct 13 2013 Till Maas <opensource@till.name> - 0.10.2-5
- Harden build

* Wed Aug 21 2013 Paul Wouters <pwouters@redhat.com> - 0.10.2-4
- Ensure to BuildRequires: libotr-devel >= 4.0.0

* Tue Aug 06 2013 Till Maas <opensource@till.name> - 0.10.2-3
- Support libotr4 with patch from debian

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jan 30 2013 Till Maas <opensource@till.name> - 0.10.2-1
- Update to new release

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 06 2010 Matěj Cepl <mcepl@redhat.com> - 0.10.1-1
- New upstream release

* Fri Aug 27 2010 Michael Fleming <mfleming+rpm@thatfleminggent.com> - 0.10.0-1
- Update to 0.10.0
- Split out devel subpackage

* Thu Oct 8 2009 Michael Fleming <mfleming+rpm@thatfleminggent.com> - 0.9.10-1
- Update to 0.9.10 (bz# 527738)
- Switch to enchant for spellchecking (bz# 523963)

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.9.9-5
- rebuilt with new openssl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 0.9.9-2
- rebuild with new openssl

* Sun Oct 12 2008 Michael Fleming <mfleming+rpm@enlartenment.com> - 0.9.9-1
- Upgrade to 0.9.9
- Revert to using OpenSSL (#bz 389481)

* Sat Jun 28 2008 Michael Fleming <mfleming+rpm@enlartenment.com> - 0.9.7-1
- Version upgrade (#bz 452437)
- Build against GNUTLS 2.4

* Sat Feb 23 2008 Michael Fleming <mfleming+rpm@enlartenment.com> - 0.9.6-1
- Version upgrade to fix longstanding EVR issue :-)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.4-2
- Autorebuild for GCC 4.3

* Sun Oct 28 2007 Michael Fleming <mfleming+rpm@enlartenment.com> - 0.9.4-1
- New upstream release
- Use GnuTLS in place of OpenSSL
- Enable OTR (Off The Record) support.

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.9.3-6
- Correct location of README_PGP.txt

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.9.3-5
- Rebuild for selinux ppc32 issue.

* Sun Aug 26 2007 Michael Fleming <mfleming+rpm@enlartenment.com> 0.9.3-4
- Update License tag
- Add README_PGP.txt (RH #250603)

* Wed Jul 25 2007 Jesse Keating <jkeating@redhat.com> - 0.9.3-3
- Rebuild for RH #249435

* Tue Jul 10 2007 Michael Fleming <mfleming+rpm@enlartenment.com> 0.9.3-2
- Remove broken .desktop file - it's not really needed for a console app.

* Thu Jun 21 2007 Michael Fleming <mfleming+rpm@enlartenment.com> 0.9.3-1.mf
- Upstream update
- Fix .desktop file categories.

* Sun Jun 17 2007 Michael Fleming <mfleming+rpm@enlartenment.com> 0.9.2-2.mf
- Actually enable aspell support this time.

* Wed Jun 13 2007 Michael Fleming <mfleming+rpm@enlartenment.com> 0.9.2-1.mf
- Upstream update
- Add aspell-devel BR for spellchecking support (in an IM client? What?!)
- Use the .desktop file as Mikael has been kind enough to include one.

* Sun Feb 11 2007 Michael Fleming <mfleming+rpm@enlartenment.com> 0.9.1-1.mf
- Upstream update

* Sun Dec 17 2006 Michael Fleming <mfleming+rpm@enlartenment.com> 0.9.0-1.mf
- Upstream update
- GPG support enabled (added gpgme-devel to BR:)

* Sun Nov 19 2006 Michael Fleming <mfleming+rpm@enlartenment.com> 0.8.3-1.mf
- Upstream update

* Wed Sep 20 2006 Michael Fleming <mfleming+rpm@enlartenment.com> 0.8.2-1.mf
- Upstream update

* Tue Aug 22 2006 Michael Fleming <mfleming+rpm@enlartenment.com> 0.8.1-1.mf
- Upstream update (small keybinding fixes)

* Mon Aug 14 2006 Michael Fleming <mfleming+rpm@enlartenment.com> 0.8.0-1.mf
- Upstream update

* Wed Jun 28 2006 Michael Fleming <mfleming+rpm@enlartenment.com> 0.7.8-1.mf
- Upstream update (skipped 0.7.7 due to makefile oddity).

* Thu May 11 2006 Michael Fleming <mfleming+rpm@enlartenment.com> 0.7.6-1.mf
- Initial package.

