Name:           perl-WebService-Linode
Version:        0.29
Release:        3%{?dist}
Summary:        Perl Interface to the Linode.com API
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/WebService-Linode
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIKEGRB/WebService-Linode-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.8.5
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(JSON) >= 2.00
BuildRequires:  perl(List::Util)
# Default URL has https schema
# LWP::Protocol::https not used at tests
BuildRequires:  perl(LWP::UserAgent)
# Tests:
# Test::Kwalitee 1.21 not used
BuildRequires:  perl(Test::More) >= 0.88
# Test::Pod 1.41 not used
# Optional tests:
BuildRequires:  perl(Pod::Coverage) >= 0.18
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(JSON) >= 2.00
# Default URL has https schema
Requires:       perl(LWP::Protocol::https)

# Not to process documentation
%{?perl_default_filter}

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(JSON\\)$

%description
This module implements the Linode.com API methods. Linode methods have had
dots replaced with underscores to generate the perl method name. All keys 
and parameters have been lower cased but returned data remains otherwise 
the same. For additional information see <http://www.linode.com/api/>.

%prep
%setup -qn WebService-Linode-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
unset AUTHOR_TESTING
unset RELEASE_TESTING
./Build test

%files
%doc Changes README examples/
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.29-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.29-1
- 0.29 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-11
- Perl 5.30 rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-8
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 09 2015 Petr Pisar <ppisar@redhat.com> - 0.28-1
- 0.28 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.27-2
- Perl 5.22 rebuild

* Mon Mar 02 2015 Christopher Meng <rpm@cicku.me> - 0.27-1
- Update to 0.27

* Sun Feb 01 2015 Christopher Meng <rpm@cicku.me> - 0.26-1
- Update to 0.26

* Sat Oct 18 2014 Christopher Meng <rpm@cicku.me> - 0.23-1
- Update to 0.23

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-2
- Perl 5.20 rebuild

* Wed Jul 30 2014 Christopher Meng <rpm@cicku.me> - 0.22-1
- Update to 0.22

* Sun Jul 06 2014 Christopher Meng <rpm@cicku.me> - 0.21-1
- Update to 0.21

* Tue Jul 01 2014 Christopher Meng <rpm@cicku.me> - 0.20-1
- Update to 0.20

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 13 2014 Christopher Meng <rpm@cicku.me> - 0.19-1
- Update to 0.19

* Fri Feb 07 2014 Christopher Meng <rpm@cicku.me> - 0.18-1
- Update to 0.18 with 2 factor authentication support!
- Add missing BRs and examples.

* Tue Jan 28 2014 Christopher Meng <rpm@cicku.me> - 0.17-1
- Initial Package.
