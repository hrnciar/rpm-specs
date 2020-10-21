Name:           gloox
Epoch:          1
Version:        1.0.23
Release:        3%{?dist}
Summary:        A rock-solid, full-featured Jabber/XMPP client C++ library
License:        GPLv3
URL:            https://camaya.net/gloox
Source0:        https://camaya.net/download/%{name}-%{version}.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  gnutls-devel >= 1.2
BuildRequires:  libgcrypt-devel
BuildRequires:  libidn-devel >= 0.5
BuildRequires:  zlib-devel >= 1.2.3

%description
gloox is a rock-solid, full-featured Jabber/XMPP client library written in
C++. It makes writing spec-compliant clients easy and allows for hassle-free
integration of Jabber/XMPP functionality into existing applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       gnutls-devel%{?_isa}
Requires:       libidn-devel%{?_isa}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -qn %{name}-%{version}%{?prerel}
# recode to UTF
mv -f AUTHORS AUTHORS.old
iconv -f iso8859-1 -t UTF-8 AUTHORS.old > AUTHORS

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete -print

%check
# Tests are broken since F27, needs bugreport
#make check

%ldconfig_scriptlets

%files
%license LICENSE
%{_libdir}/libgloox.so.17*

%files devel
%doc AUTHORS ChangeLog TODO UPGRADING
%{_bindir}/%{name}-config
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/libgloox.so

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.23-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 14 2020 Jorge A Gallegos <kad@blegh.net> - 1:1.0.23-1
- Bumped to latest stable from camaya.net
- Replaced tabs with spaces in spec to placate rpmlint (mixed tabs n spaces)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:1.0.14-7
- Rebuild for libidn

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Aug 12 2015 Christopher Meng <rpm@cicku.me> - 1:1.0.14-1
- Update to 1.0.14

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1:1.0.13-3
- Rebuilt for GCC 5 C++11 ABI change

* Sun Mar 15 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1:1.0.13-2
- Rebuild for GCC5 (#1202059)

* Thu Feb 05 2015 Christopher Meng <rpm@cicku.me> - 1:1.0.13-1
- Update to 1.0.13

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 21 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1:1.0.10-3
- Add patch from Debian for ftbfs with gcc 4.9
- Update license to GPLv3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1:1.0.10-1
- Update to 1.0.10

* Tue Mar 4 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 1:1.0.9-3
- Make added before requirements arch-specific: gnutls-devel%%{?_isa}, libidn-devel%%{?_isa}bz#1034988.

* Mon Mar 3 2014 Pavel Alexeev <Pahan@Hubbitus.info> - 1:1.0.9-2
- Add Requires: gnutls-devel, libidn-devel into devel package bz#1034988.

* Sun Dec 1 2013 Pavel Alexeev <Pahan@Hubbitus.info> - 1:1.0.9-1
- Update to 1.0.9 bz#1034994

* Sun Aug 4 2013 Pavel Alexeev <Pahan@Hubbitus.info> - 1:1.0.3-1
- Update to 1.0.3 version by request bz#991399
- Add BR libgcrypt-devel

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-6.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-5.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-4.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-3.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-2.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 10 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 1.0-1.11
- Add Epoch: 1 due to correct my mistake in version enumeration: https://fedorahosted.org/rel-eng/ticket/3139
  and disclaimer rel-end delete updates.

* Sat Nov 7 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 1.0-1.10
- long-awaited release 1.0

* Mon Oct 19 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 1.0-0.9.rc3.SVNr4204
- As right mention Peter Lemenkov, my naming cheme is incorrect, renum it.
- Expand "beta" define and magick to "prerel".

* Sun Oct 18 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 1.0rc3-0.8.SVNr4204
- New build due resolve my bugreport https://mail.camaya.net/horde/whups/ticket/?id=157

* Sun Oct 18 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 1.0rc3-0.7.SVNr4203
- rc3.
- Euroelessar (one of qutIM developer, thank you) submit patches:
  http://bugs.camaya.net/horde/whups/ticket/?id=110
  http://bugs.camaya.net/horde/whups/ticket/?id=155
  http://bugs.camaya.net/horde/whups/ticket/?id=154
  http://bugs.camaya.net/horde/whups/ticket/?id=153
  http://bugs.camaya.net/horde/whups/ticket/?id=152
  http://bugs.camaya.net/horde/whups/ticket/?id=151
  http://bugs.camaya.net/horde/whups/ticket/?id=150
  http://bugs.camaya.net/horde/whups/ticket/?id=149
  all is important and rev 4200 at least required.
- Include UPGRADING to %%doc

* Wed Jul 29 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 1.0-0.6.SVNr4029
- New build due to close several bugs:
  https://mail.camaya.net/horde/whups/ticket/?id=140 - delete patch gloox-1.0-beta-SVNr4003-missed_header.patch
  https://bugs.camaya.net/horde/whups/ticket/?id=141 - delete patch gloox-1.0-GCC4.4-missing_includes.patch
  https://bugs.camaya.net/horde/whups/ticket/?id=137 - delete patch gloox-1.0-SVNr4003.glibc-private-symbol.patch
- Use "svn export" instead of "svn checkout".

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.6.SVNr4003
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 17 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 1.0-0.5.SVNr4003
- Add --exclude='.svn' to tar pack source and set time to last commit. This may allow pass hash checking soucre later.

* Tue Apr 7 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 1.0-0.4.SVNr4003
- Add Patch3: gloox-1.0-GCC4.4-missing_includes.patch to allow build on GCC4.4

* Tue Apr 7 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 1.0-0.3.SVNr4003
- REmade patch1. Instead of just comment private stuff I use temporray ugly hack - copy-past function implementation from glibc source until
  author do not reimplement it properly.

* Sun Apr 5 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 1.0-0.2.SVNr4003
- Add patch2 gloox-1.0-beta-SVNr4003-missed_header.patch - see bug http://bugs.camaya.net/horde/whups/ticket/?id=140

* Sun Apr 5 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 1.0-0.1.SVNr4003
- qutIM require gloox version 1.0 with SVN revision >= 3873. Try build current.
- Patch1 (http://bugs.camaya.net/horde/whups/ticket/?id=137) little adopted (gloox-1.0-beta7.glibc-private-symbol.patch -> gloox-1.0-SVNr4003.glibc-private-symbol.patch).
- Add SVN part into Release tag.

* Fri Mar 27 2009 Pavel Alexeev <Pahan@Hubbitus.info> - 1.0-0.0.beta3
- Import http://www.salstar.sk/pub/fedora/SRPMS/10/gloox-1.0-0.0beta3.fc10.src.rpm
- Step to 1.0-beta7 version
- Reformat with tabs spec file.
- %%beta (replace %%beta_version) now represent only number. According it change all mention of it.
- Add Requires(postun): /sbin/ldconfig and Requires(post): /sbin/ldconfig

* Fri Mar 7 2008 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.9.9.4-1
- update to upstream

* Thu Feb 28 2008 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.9.9.3-1
- update to upstream

* Sun Dec 2 2007 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.9.7-2
- removed patch
- added undef for HAVE_RES_QUERY, HAVE_RES_QUERYDOMAIN, HAVE_DN_SKIPNAME
  see: https://mail.camaya.net/horde/whups/ticket/?id=52

* Wed Nov 28 2007 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.9.7-1
- update upstream
- added patch to avoid dependecny problem on libresolv.so.2(GLIBC_PRIVATE)

* Mon Sep 17 2007 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.9.4.1-1
- first release
