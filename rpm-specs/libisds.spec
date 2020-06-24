# Build manual pages
%bcond_without libisds_enables_man
# Support network operations
%bcond_without libisds_enables_net
# Use OpenSSL instead of libgcrypt and gpgme
%bcond_with libisds_enables_openssl
# Perform tests
%bcond_without libisds_enables_test

Name:           libisds
Version:        0.11
Release:        3%{?dist}
Summary:        Library for accessing the Czech Data Boxes
# COPYING:      LGPLv3 text
# README:       LGPLv3+
# src/gettext.h:            GPLv3+
## Not delivered in any binary package
# aclocal.m4:   GPLv2+ with exceptions and FSFULLR
# client/Makefile.in:       FSFULLR
# config.guess: GPLv3+ with exceptions
# config.rpath: FSFULLR
# config.sub:   GPLv3+ with exceptions
# configure:    GPLv2+ with exceptions and FSFUL
# depcomp:      GPLv2+ with exceptions  
# doc/Makefile.in:  FSFULLR
# install-sh:       MIT and Public Domain
# ltmain.sh:        GPLv2+ with exceptions and GPLv3+ and GPLv3+ with exceptions
# m4/gettext.m4:    FSFULLR
# m4/gpgme.m4:      FSFULLR
# m4/iconv.m4:      FSFULLR
# m4/intlmacosx.m4: FSFULLR
# m4/libgcrypt.m4:  FSFULLR
# m4/lib-ld.m4:     FSFULLR
# m4/lib-link.m4:   FSFULLR
# m4/lib-prefix.m4: FSFULLR
# m4/libtool.m4:    GPLv2+ with exceptions and FSFUL
# m4/ltoptions.m4:  FSFULLR
# m4/ltsugar.m4:    FSFULLR
# m4/lt~obsolete.m4:    FSFULLR
# m4/ltversion.m4:  FSFULLR
# m4/nls.m4:        FSFULLR
# m4/po.m4:         FSFULLR
# m4/progtest.m4:   FSFULLR
# Makefile.in:      FSFULLR
# missing:          GPLv2+ with exceptions
# po/Makefile.in.in:    (Something similar to FSFUL)
# src/Makefile.in:          FSFULLR
# test/Makefile.in:         FSFULLR
# test/offline/Makefile.in: FSFULLR
# test/online/Makefile.in:  FSFULLR
# test/simline/Makefile.in: FSFULLR
# test-driver:      GPLv2+ with exceptions
License:        LGPLv3+ and GPLv3+
URL:            http://xpisar.wz.cz/%{name}/
Source0:        %{url}dist/%{name}-%{version}.tar.xz
Source1:        %{url}dist/%{name}-%{version}.tar.xz.asc
# Key exported from Petr Pisar's keyring
Source2:        gpgkey-4B528393E6A3B0DFB2EF3A6412C9C5C767C6FAA2.gpg
# Fix building with GCC 10, in upstream after 0.11
Patch0:         libisds-0.11-tests-Fix-building-with-GCC-10.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
%if %{with libisds_enables_man}
BuildRequires:  docbook-style-xsl
BuildRequires:  libxslt
%endif
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  libxml2-devel
%if %{with libisds_enables_net}
BuildRequires:  libcurl-devel
%endif
%if %{with libisds_enables_openssl}
BuildRequires:  openssl
%else
BuildRequires:  gpgme-devel
BuildRequires:  libgcrypt-devel
%endif
BuildRequires:  make
BuildRequires:  expat-devel >= 2.0.0
# Run-time:
%if !%{with libisds_enables_openssl}
BuildRequires:  gnupg2-smime
%endif
# Tests:
%if %{with libisds_enables_test}
BuildRequires:  gnutls-devel >= 2.12.0
%endif
%if !%{with libisds_enables_openssl}
Requires:       gnupg2-smime
%endif

%description
This is a library for accessing ISDS (Informační systém datových schránek /
Data Box Information System) SOAP services as defined in Czech ISDS Act
(300/2008 Coll.) and implied documents.

%package        devel
Summary:        Development files for %{name}
License:        LGPLv3+
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libxml2-devel%{?_isa}
Requires:       pkgconfig%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%patch0 -p1
autoreconf -fi

%build
%configure \
%if %{with libisds_enables_man}
    --enable-doc \
%else
    --disable-doc \
%endif
    --disable-online-test \
%if %{with libisds_enables_openssl}
    --enable-openssl-backend \
%else
    --disable-openssl-backend \
%endif
    --disable-static \
%if %{with libisds_enables_test}
    --enable-test \
%else
    --disable-test \
%endif
%if %{with libisds_enables_net}
    --with-libcurl \
%else
    --without-libcurl \
%endif
    --enable-curlreauthorizationbug
%{make_build}

%check
make check %{?_smp_mflags}

%install
%{make_install}
find $RPM_BUILD_ROOT -name '*.la' -delete
%find_lang %{name}
# Remove multilib unsafe files
rm -rf client/.deps client/Makefile{,.in}

%files -f %{name}.lang
%license COPYING
%doc README AUTHORS NEWS TODO
%{_libdir}/libisds.so.5
%{_libdir}/libisds.so.5.*

%files devel
%{_includedir}/isds.h
%{_libdir}/libisds.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*
%doc client

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Petr Pisar <ppisar@redhat.com> - 0.11-2
- Fix building with GCC 10

* Fri Sep 06 2019 Petr Pisar <ppisar@redhat.com> - 0.11-1
- 0.11 bump
- License corrected to LGPLv3+ and GPLv3+

* Wed Sep 04 2019 Petr Pisar <ppisar@redhat.com> - 0.10.8-6
- Adapt tests to libgcrypt without an MD5 support

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Petr Pisar <ppisar@redhat.com> - 0.10.8-4
- Adapt tests missing en_US.UTF-8 locale
- Adapt tests to GnuTLS 3.6.4 (bug #1651213)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Petr Pisar <ppisar@redhat.com> - 0.10.8-1
- 0.10.8 bump

* Thu Mar 22 2018 Petr Pisar <ppisar@redhat.com> - 0.10.7-4
- Do no call ldconfig postscriptlets where not necessary

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Petr Pisar <ppisar@redhat.com> - 0.10.7-1
- 0.10.7 bump

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.10.6-2
- Rebuild for gpgme 1.18

* Mon Oct 17 2016 Petr Pisar <ppisar@redhat.com> - 0.10.6-1
- 0.10.6 bump

* Mon Oct 03 2016 Petr Pisar <ppisar@redhat.com> - 0.10.5-1
- 0.10.5 bump

* Thu Jun 09 2016 Petr Pisar <ppisar@redhat.com> - 0.10.4-1
- 0.10.4 bump

* Mon Mar 21 2016 Petr Pisar <ppisar@redhat.com> - 0.10.3-1
- 0.10.3 bump

* Tue Feb 09 2016 Petr Pisar <ppisar@redhat.com> - 0.10.2-3
- Fix a GCC 6 warning (bug #1305760)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Petr Pisar <ppisar@redhat.com> - 0.10.2-1
- 0.10.2 bump

* Mon Sep 07 2015 Petr Pisar <ppisar@redhat.com> - 0.10.1-1
- 0.10.1 bump

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 29 2015 Petr Pisar <ppisar@redhat.com> - 0.10-1
- 0.10 bump

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Petr Pisar <ppisar@redhat.com> - 0.9-1
- 0.9 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 02 2014 Petr Pisar <ppisar@redhat.com> - 0.8-2
- Use _DEFAULT_SOURCE where _BSD_SOURCE macro presents to satisfy glibc-2.19.90

* Mon Oct 21 2013 Petr Pisar <ppisar@redhat.com> - 0.8-1
- 0.8 bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 27 2013 Petr Pisar <ppisar@redhat.com> - 0.7-3
- Update config.sub to support aarch64 (bug #925782)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 03 2013 Petr Pisar <ppisar@redhat.com> - 0.7-1
- 0.7 bump

* Wed Oct 31 2012 Petr Pisar <ppisar@redhat.com> - 0.6.2-1
- 0.6.2 bump

* Tue Oct 30 2012 Petr Pisar <ppisar@redhat.com> - 0.6.1-1
- 0.6.1 bump

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 03 2011 Petr Pisar <ppisar@redhat.com> - 0.5-1
- 0.5 bump (breaks ABI, API preserved)
- Remove aplied patch and GPG hack

* Fri Feb 11 2011 Petr Pisar <ppisar@redhat.com> - 0.4-2
- Rebuild with GCC 4.6
- Remove BuildRoot stuff
- Make devel subpackage dependencies ISA specific

* Mon Dec 20 2010 Petr Pisar <ppisar@redhat.com> - 0.4-1
- 0.4 bump, it breaks ABI
- Use smaller xz archive instead of bzip2
- Do tests in parallel

* Fri Nov 05 2010 Petr Pisar <ppisar@redhat.com> - 0.3.1-2
- Rebuild against new libxml2

* Tue Jun 29 2010 Petr Pisar <ppisar@redhat.com> - 0.3.1-1
- 0.3.1 version bump
- Create ~/.gnupg to workaround bug in gnupg2-smime

* Tue Apr 13 2010 Petr Pisar <ppisar@redhat.com> - 0.2.1-1
- New version 0.2.1 released by upstream

* Thu Feb 11 2010 Matěj Cepl <mcepl@redhat.com> - 0.1-2
- Fixing small issue with documentation for package review

* Tue Feb 09 2010 Matěj Cepl <mcepl@redhat.com> - 0.1-1
- Initial packaging effort
