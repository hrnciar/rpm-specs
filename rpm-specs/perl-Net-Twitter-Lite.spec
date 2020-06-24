Name:           perl-Net-Twitter-Lite
Version:        0.12008
Release:        12%{?dist}
Summary:        Perl interface to the Twitter API
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Net-Twitter-Lite
Source0:        https://cpan.metacpan.org/authors/id/M/MM/MMIMS/Net-Twitter-Lite-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(blib)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::DoubleEncodedUTF8)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(JSON) >= 2.02
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::UserAgent) >= 5.82
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(Net::HTTP)
BuildRequires:  perl(Net::Netrc)
BuildRequires:  perl(Net::OAuth) >= 0.25
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
# Not used - perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.82
# Not used - perl(Test::Pod) >= 1.41
# Not used - perl(Test::Pod::Coverage) >= 1.08
# Not used - perl(Test::Spelling) >= 0.11
BuildRequires:  perl(URI) >= 1.40
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(warnings)
Requires:       perl(JSON) >= 2.02
Requires:       perl(LWP::Protocol::https)
Requires:       perl(LWP::UserAgent) >= 5.82
Requires:       perl(Net::Netrc)
Requires:       perl(Net::OAuth) >= 0.25
Requires:       perl(Scalar::Util)
Requires:       perl(Storable)
Requires:       perl(URI) >= 1.40
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(JSON\\)$
%global __requires_exclude %__requires_exclude|^perl\\(LWP::UserAgent\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Net::OAuth\\)$
%global __requires_exclude %__requires_exclude|^perl\\(URI\\)$
%description
This module provides a perl interface to the Twitter API v1.

%prep
%setup -q -n Net-Twitter-Lite-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes examples README
%{perl_vendorlib}/Net/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.12008-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12008-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12008-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.12008-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12008-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12008-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.12008-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12008-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12008-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.12008-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12008-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.12008-1
- 0.12008 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.12006-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12006-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12006-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.12006-4
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.12006-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 14 2014 David Dick <ddick@cpan.org> - 0.12006-1
- Initial release
