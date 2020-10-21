Name:           perl-Mail-Box-IMAP4
Version:        3.007
Release:        5%{?dist}
Summary:        Handle IMAP4 folders as client
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Mail-Box-IMAP4
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/Mail-Box-IMAP4-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(IO::Handle)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(Digest::HMAC_MD5)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Mail::Box::Manage::User) >= 3
BuildRequires:  perl(Mail::Box::Net) >= 3
BuildRequires:  perl(Mail::Box::Net::Message)
BuildRequires:  perl(Mail::Box::Parser::Perl)
BuildRequires:  perl(Mail::Box::Search) >= 3
BuildRequires:  perl(Mail::IMAPClient)
BuildRequires:  perl(Mail::Message::Head)
BuildRequires:  perl(Mail::Message::Head::Complete) >= 3
BuildRequires:  perl(Mail::Message::Head::Delayed) >= 3
BuildRequires:  perl(Mail::Transport::Receive) >= 3
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Mail::Box::Identity)
BuildRequires:  perl(Mail::Box::MH)
BuildRequires:  perl(Mail::Box::Test) >= 3
BuildRequires:  perl(Mail::Message) >= 3
BuildRequires:  perl(Mail::Message::Body::Lines) >= 3
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Mail::Box) >= 3.007
Requires:       perl(Mail::Box::Net) >= 3
Requires:       perl(Mail::IMAPClient) >= 3.42
Requires:       perl(Mail::Message::Body::Lines) >= 3
Requires:       perl(Mail::Message::Head::Complete) >= 3
Requires:       perl(Mail::Message::Head::Delayed) >= 3
Requires:       perl(Mail::Transport::Receive) >= 3.004

Conflicts:      perl-Mail-Box < 3

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Mail::Box::Manage::User\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Mail::IMAPClient\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Mail::Box::(Net|Search)\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Mail::Message(::Body::Lines|::Head::Complete|::Head::Delayed|)\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Mail::(Server|Transport::Receive)\\)$

%description
Maintain a folder which has its messages stored on a remote server. The
communication between the client application and the server is implemented
using the IMAP4 protocol.

%package -n perl-Mail-Server-IMAP4
Summary:        IMAP4 server implementation
License:        GPL+ or Artistic
BuildArch:      noarch
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Mail::Box::Manage::User) >= 3
Requires:       perl(Mail::Box::Search) >= 3
Requires:       perl(Mail::Server) >= 3

%description -n perl-Mail-Server-IMAP4
This module is a place-holder, which can be used to grow code which is
needed to implement a full IMAP4 server.
The server implementation is not completed.

%prep
%setup -q -n Mail-Box-IMAP4-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc ChangeLog README
%{perl_vendorlib}/Mail/Box/*
%{perl_vendorlib}/Mail/Transport/*
%{_mandir}/man3/Mail::Box*
%{_mandir}/man3/Mail::Transport*

%files -n perl-Mail-Server-IMAP4
%{perl_vendorlib}/Mail/Server/*
%{_mandir}/man3/Mail::Server*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.007-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.007-4
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.007-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.007-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.007-1
- 3.007 bump

* Thu Jun 13 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.006-1
- 3.006 bump

* Thu Jun 06 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.005-1
- 3.005 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.004-2
- Perl 5.30 rebuild

* Fri May 03 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.004-1
- 3.004 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.003-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.003-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.003-2
- Perl 5.28 rebuild

* Mon Mar 05 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.003-1
- 3.003 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.002-1
- 3.002 bump

* Wed Jun 28 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.001-1
- Initial release
