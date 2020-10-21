
Name:           perl-VOMS-Lite
Version:        0.20
Release:        21%{?dist}
Summary:        Perl extension for VOMS Attribute certificate creation
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/VOMS-Lite
Source0:        ftp://ftp.funet.fi/pub/CPAN/authors/id/M/MI/MIKEJ/VOMS-Lite-%{version}.tar.gz
Source1:        voms.config
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
%if 0%{?el4}%{?el5}
BuildRequires:  sed
%endif
BuildRequires:  perl(Crypt::CBC)
BuildRequires:  perl(Crypt::DES_EDE3)
# Data::Dumper not used at tests
# DBI not used at tests
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy)
# HTTP::Daemon::SSL not used at tests
# HTTP::Response not used at tests
# HTTP::Status not used at tests
# IO::Socket not used at tests
# IO::Socket::SSL not used at tests
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(MIME::Base64)
# Pod::Simple::Text not used at tests
BuildRequires:  perl(strict)
BuildRequires:  perl(Sys::Hostname)
# Term::ReadKey not used at tests
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# XML::Parser not used at tests
# Optional run-time:
# Digest::MD2 not used at tests
BuildRequires:  perl(Math::BigInt::GMP)
# Tests:
%{?!tests_req:%global tests_req BuildRequires: }
%tests_req      perl(Cwd)
%tests_req      perl(Sys::Hostname)
%tests_req      perl(Test)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Crypt::DES_EDE3)
Requires:       perl(Pod::Simple::Text)
# Optional run-time:
Requires:       perl(Digest::MD2)
Requires:       perl(Math::BigInt::GMP)

# RPM 4.8 style
# Remove WIN32::API from the requires. It is only ever loaded 
# on that platform.
%{?perl_default_filter:
%filter_from_requires /^perl(WIN32::API)/d
%perl_default_filter
}
#Add a test sub package.
%{?perl_default_subpackage_tests}
# RPM 4.9 style
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}perl\\(WIN32::API\\)

%description
VOMS (virtual organization membership service) is a system for 
managing grid level authorization data within 
multi-institutional collaborations via membership and roles
within that membership.

VOMS::Lite provides a perl library and client tools 
for interacting with an existing voms service including the 
well known C implementation of voms.

A number of commands are included for generating and processing 
proxies including  voms-proxy-init.pl, voms-ac-issue.pl, ...

Configuration of client tools can be supplied via 
$ENV{'VOMS_CONFIG_FILE'} or else ~/.grid-security/voms.conf. 
The root user only uses /etc/grid-security/voms.config.

%package -n perl-voms-server
Summary:    Perl extension for VOMS Attribute certificate creation
Requires:   perl-VOMS-Lite = %{version}-%{release} 

%description -n perl-voms-server
VOMS (virtual organization membership service) is a system for 
managing grid level authorization data within 
multi-institutional collaborations via membership and roles
within that membership.

A server voms-server.pl providing a perl implementation
of a VOMS server.

%prep
%setup -q -n VOMS-Lite-%{version}
cp -p %{SOURCE1} .

#On .el4 and .el5 we filter requires the old fashined
#way still.  The magic stuff about won't work.
%if 0%{?el4}%{?el5}
cat << \EOF > %{name}-req
#!/bin/sh
%{__perl_requires} $* |\
sed -e '/perl(WIN32::API)/d'
EOF

%global __perl_requires %{_builddir}/VOMS-Lite-%{version}/%{name}-req
chmod +x %{__perl_requires}
%endif # end of if el4,5.

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install DESTDIR=%{buildroot}
# I believe the voms-server.pl was meant to be installed in 
# sbin.
mkdir %{buildroot}%{_sbindir}
mv %{buildroot}%{_bindir}/voms-server.pl %{buildroot}%{_sbindir}/voms-server.pl
mv %{buildroot}%{_bindir}/vomsserver.pl %{buildroot}%{_sbindir}/vomsserver.pl
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

# Install a default configuration file and directory for VO grid-mapfiles.
mkdir -p %{buildroot}%{_sysconfdir}/grid-security/grid-mapfile.d
install -p -m 644 voms.config %{buildroot}%{_sysconfdir}/grid-security/voms.config

%check
make test

%files
%doc Changes README TODO 
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_bindir}/cert-init.pl
%{_bindir}/cert-req.pl
%{_bindir}/examineAC.pl
%{_bindir}/extractVOMS.pl
%{_bindir}/myproxy-get.pl
%{_bindir}/myproxy-init.pl
%{_bindir}/proxy-init.pl
%{_bindir}/verifycert.pl
%{_bindir}/voms-ac-issue.pl
%{_bindir}/voms-proxy-init.pl
%{_bindir}/voms-proxy-list.pl
%{_mandir}/man1/cert-init.pl.1*
%{_mandir}/man1/cert-req.pl.1*
%{_mandir}/man1/examineAC.pl.1*
%{_mandir}/man1/extractVOMS.pl*
%{_mandir}/man1/myproxy-get.pl*
%{_mandir}/man1/myproxy-init.pl*
%{_mandir}/man1/proxy-init.pl*
%{_mandir}/man1/verifycert.pl*
%{_mandir}/man1/voms-ac-issue.pl.1*
%{_mandir}/man1/voms-proxy-init.pl.1*
%{_mandir}/man1/voms-proxy-list.pl.1*

%dir %{_sysconfdir}/grid-security
%dir %{_sysconfdir}/grid-security/grid-mapfile.d
%config(noreplace) %{_sysconfdir}/grid-security/voms.config

%files -n perl-voms-server
%{_sbindir}/voms-server.pl
%{_sbindir}/vomsserver.pl
%{_mandir}/man1/voms-server.pl.1*
%{_mandir}/man1/vomsserver.pl.1*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-20
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-17
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-14
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-11
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 22 2016 Petr Pisar <ppisar@redhat.com> - 0.20-9
- Adapt tests_req macro invocation to SRPM build root without perl

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-8
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 17 2015 Petr Pisar <ppisar@redhat.com> - 0.20-6
- Specify all dependencies (bug #1243858)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-4
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.20-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 19 2013 Steve Traylen <steve.traylen@cern.ch> 0.20-1
- New upstream 0.20

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Petr Pisar <ppisar@redhat.com> - 0.14-8
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 0.14-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 26 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.14-3
- add RPM4.9 macro filter

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.14-2
- Perl mass rebuild

* Mon Mar 21 2011 Steve Traylen <steve.traylen@cern.ch> 0.14-1
- New upstream 0.14

* Wed Mar 16 2011 Steve Traylen <steve.traylen@cern.ch> 0.12-1
- New upstream 0.12,  Add voms-proxy-list.pl as bin new 
  command and man page.

* Sun Mar 13 2011 Steve Traylen <steve.traylen@cern.ch> 0.11-1
- Update to 0.11.
- New build requires for perl(Crypt::CBC)
- Install configuration file mode 644.
- Split server application out to seperate package.

* Sat Mar 13 2010 Steve Traylen <steve.traylen@cern.ch> 0.09-5
- Rewrite summary to make it less cryptic.
- Create a -tests package when possible.
- Install configuration file at 600.

* Sun Mar 7 2010 Steve Traylen <steve.traylen@cern.ch> 0.09-4
- Move voms-server.pl to /usr/sbin
- Add a default configuration for voms-server.pl

* Sat Mar 6 2010 Steve Traylen <steve.traylen@cern.ch> 0.09-3
- Change source URL to not point at an old mirror.

* Sun Feb 21 2010 Steve Traylen <steve.traylen@cern.ch> 0.09-2
- Filter out perl(WIN32::API) with new macros where
  possible.
- Install in DESTDIR

* Tue Feb 16 2010 Steve Traylen <steve.traylen@cern.ch> 0.09-1
- Filter out perl(WIN32::API) from requires.
- Addition of perl(Math::BigInt::GMP) for speed.
- Add bins and associated man pages to file list.
- Specfile autogenerated by cpanspec 1.78.
