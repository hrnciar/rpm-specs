Summary:        Very fast network log-on cracker
Name:           hydra
Version:        9.0
Release:        4%{?dist}
License:        AGPLv3 with exceptions
# Old URL       https://www.thc.org/thc-hydra/
URL:            https://github.com/vanhauser-thc/thc-hydra
Source0:        https://github.com/vanhauser-thc/thc-hydra/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        xhydra.desktop
# Upstream provides non-transparent jpeg
Source2:        xhydra.png
# Sent upstream via email 20120518
Patch0:         hydra-use-system-libpq-fe.patch
Patch1:         hydra-fix-dpl4hydra-dir.patch
# APR used in libsvn needs inclusion of the linux limits.h first
# already implemented upstream
# https://github.com/vanhauser-thc/thc-hydra/commit/db9025bf86e79f1af1e1d70bdc6ea133e486c781.patch
Patch2:         hydra-fix-apr-svn.patch
# In Fedora the firebird includes are not in /include but /include/firebird
# Reported upstream: https://github.com/vanhauser-thc/thc-hydra/pull/500
Patch3:         hydra-fix-firebird-includes.patch

BuildRequires:  apr-devel
BuildRequires:  desktop-file-utils
BuildRequires:  firebird-devel
BuildRequires:  libfbclient2-devel
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  gtk2-devel
BuildRequires:  libidn-devel
BuildRequires:  libssh-devel
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig
BuildRequires:  libpq-devel
BuildRequires:  subversion-devel
BuildRequires:  memcached-devel
BuildRequires:  libmemcached-devel
BuildRequires:  mongodb-devel
BuildRequires:  mongo-c-driver-devel
BuildRequires:  libbson-devel
BuildRequires:  freerdp-devel
BuildRequires:  libwinpr-devel
BuildRequires:  afpfs-ng-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  ncurses-devel


%description
Hydra is a parallelized log-in cracker which supports numerous protocols to 
attack. New modules are easy to add, beside that, it is flexible and very fast.

This tool gives researchers and security consultants the possibility to show 
how easy it would be to gain unauthorized access from remote to a system.

%package frontend
Summary: The GTK+ front end for hydra
Requires: hydra = %{version}-%{release}
%description frontend
This package includes xhydra, a GTK+ front end for hydra. 

%prep
%autosetup -p 1 -n thc-hydra-%{version}


%build
%configure --nostrip
# Already in 9.1-dev
export CFLAGS="$CFLAGS -fcommon"
make %{?_smp_mflags}

%install

make install DESTDIR="%{buildroot}" PREFIX="" BINDIR="%{_bindir}" MANDIR="%{_mandir}/man1" DATADIR="%{_datadir}/%{name}"

mkdir -p %{buildroot}%{_datadir}/{applications,pixmaps}
install -m 644 -p %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1};

# Fix dpl4hydra.sh (w/o buildroot prefix)
sed -i 's|^INSTALLDIR=.*|INSTALLDIR=/usr|' %{buildroot}/%{_bindir}/dpl4hydra.sh


%files
%doc CHANGES README
%license LICENSE LICENSE.OPENSSL 
%{_bindir}/hydra
%{_bindir}/pw-inspector
%{_bindir}/hydra-wizard.sh
%{_bindir}/dpl4hydra.sh
%{_mandir}/man1/hydra*
%{_mandir}/man1/pw-inspector*
%{_datadir}/%{name}/dpl4hydra*.csv
%dir %{_datadir}/%{name}

%files frontend
%{_bindir}/xhydra
%{_mandir}/man1/xhydra*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%changelog
* Fri May 22 2020 Simone Caronni <negativo17@gmail.com> - 9.0-4
- Rebuild for updated FreeRDP.

* Tue Mar 03 2020 Michal Ambroz <rebus _at seznam.cz>  9.0-3
- add buildrequires for memcached, mongodb, freerdp, afpfs, gcrypt, ncurses
- fix firebird includes
- honor the %%license tag
- build with fcommon to fix issue with "multiple definition of"

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 07 2019 Othman Madjoudj <athmane@fedoraproject.org> - 9.0-1
- Update to 9.0 (rhbz #1711202)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 08 2019 Michal Ambroz <rebus _at seznam.cz>  8.9.1-1
- Update to 8.9.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 12 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 8.6-7
- rebuilt

* Sun Feb 18 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 8.6-6
- Add make and gcc as BRs

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 20 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 8.6-4
- Fix BuildReqs

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 22 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 8.6-1
- Update to 8.6 (rhbz #1473874)
- Fix source URL

* Wed May 03 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 8.5-1
- Update to 8.5

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 8.4-1
- Update to 8.4
- Fix Source0

* Fri Aug 12 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 8.3-1
- Update to 8.3
- FIx URL since upstream now uses git tags

* Fri Jun 17 2016 Michal Ambroz <rebus _at seznam.cz>  8.2-1
- Update to 8.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Dec 21 2014 Athmane Madjoudj <athmane@fedoraproject.org>  8.1-1
- Update to 8.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Athmane Madjoudj <athmane@fedoraproject.org> 8.0-1
- Update to 8.0

* Mon Dec 30 2013 Athmane Madjoudj <athmane@fedoraproject.org> 7.6-1
- Update to 7.6
- Include hydra-wizard script (new in 7.6) 
- Fix icon filename
- Add a png icon since upstream only provides non-transparent jpeg

* Mon Nov 18 2013 Athmane Madjoudj <athmane@fedoraproject.org> 7.5-2
- Use new source file from upstream (contains minor license file fixes)

* Sun Aug 04 2013 Athmane Madjoudj <athmane@fedoraproject.org> 7.5-1
- Update to 7.5
- Update license tag.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 Athmane Madjoudj <athmane@fedoraproject.org> 7.4.2-1
- Update to 7.4.2

* Sun Dec 23 2012 Athmane Madjoudj <athmane@fedoraproject.org> 7.4-1
- Update to 7.4
- Remove s390x patch (upstreamed)

* Sat Dec 22 2012 Dan Horák <dan[at]danny.cz> 7.3-13
- s390x is 64-bit arch

* Mon Sep 10 2012 Athmane Madjoudj <athmane@fedoraproject.org> 7.3-12
- Remove dep on ncpfs-devel since it's a dead upstream.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 28 2012 Athmane Madjoudj <athmane@fedoraproject.org> 7.3-10
- Fix binaries striping issue (#825860)

* Tue May 22 2012 Athmane Madjoudj <athmane@fedoraproject.org> 7.3-9
- Update to 7.3
- Drop some patches since they're included in 7.3
- Add two patches to fix makefile and dpl4hydra

* Fri May 18 2012 Athmane Madjoudj <athmane@fedoraproject.org> 7.2-8
- Add LICENSE.OPENSSL
- Add /usr/share/hydra
- Add a patch to use system provided libpq-fe headers (provided by 
  postgresql-devel)

* Tue Apr 17 2012 Athmane Madjoudj <athmane@fedoraproject.org> 7.2-7
- Add DESTDIR support
- Include dpl4hydra

* Mon Apr 16 2012 Athmane Madjoudj <athmane@fedoraproject.org> 7.2-6
- Reverse a patch because it breaks brute-forcing NTLM-enabled services 
  (upstream confirmed that it's not necessary)

* Tue Mar 13 2012 Athmane Madjoudj <athmane@fedoraproject.org> 7.2-5
- Add patch to support mysql
- Add patch to fix warnings

* Thu Mar 08 2012 Athmane Madjoudj <athmane@fedoraproject.org> 7.2-4
- Preserve timestamps on install
- Remove extra arg in desktop file install

* Sat Feb 11 2012 Athmane Madjoudj <athmane@fedoraproject.org> 7.2-3
- Add support for CFLAGS

* Sat Feb 11 2012 Athmane Madjoudj <athmane@fedoraproject.org> 7.2-2
- Clean-up the descriptions
- Add Firebird support

* Sat Feb 11 2012 Athmane Madjoudj <athmane@fedoraproject.org> 7.2-1
- Update to 7.2

* Tue Dec 27 2011 Athmane Madjoudj <athmane@fedoraproject.org> 7.1-3
- Remove rm -rf buildroot

* Thu Dec 22 2011 Athmane Madjoudj <athmane@fedoraproject.org> 7.1-2
- Update license to GPLv3 with OpenSSL exception

* Thu Dec 22 2011 Athmane Madjoudj <athmane@fedoraproject.org> 7.1-1
- Update to recent version
- Clean-up the spec file
- Add desktop file for the frontend

* Sun Jul 04 2010 Marcus Haebler <haebler@gmail.com> - 0:5.7-0
- Initial RPM build 
