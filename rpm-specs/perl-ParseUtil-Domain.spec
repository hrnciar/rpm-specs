Name:           perl-ParseUtil-Domain
Summary:        Utility for parsing a domain name into its components
Version:        2.427
Release:        10%{?dist}

# - ParseUtil::Domain is GPL+ or Artistic (the "Perl" license)
# - data/effective_tld_names.txt is MPLv2.0
# - ParseUtil::Domain::ConfigData is automatically generated during the build,
#   based on the contents of data/effective_tld_names.txt
License:        (GPL+ or Artistic) and MPLv2.0

URL:            https://metacpan.org/release/ParseUtil-Domain
Source0:        https://cpan.metacpan.org/authors/id/H/HE/HEYTRAV/ParseUtil-Domain-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(autobox)
BuildRequires:  perl(autobox::Core)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp) >= 1.17
BuildRequires:  perl(lib)
BuildRequires:  perl(Mock::Quick)
BuildRequires:  perl(Modern::Perl)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Moose)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Net::IDN::Encode) >= 2.003
BuildRequires:  perl(Net::IDN::Nameprep) >= 1.101
BuildRequires:  perl(Net::IDN::Punycode) >= 1.100
BuildRequires:  perl(Perl6::Export::Attrs)
BuildRequires:  perl(Perl::Critic)
BuildRequires:  perl(Regexp::Assemble::Compressed)
BuildRequires:  perl(Smart::Comments)
BuildRequires:  perl(Test::Class)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Test::Routine)
BuildRequires:  perl(Test::Routine::Util)
BuildRequires:  perl(Unicode::CharName) >= 1.07
BuildRequires:  sed
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%{?perl_default_filter}

%description
A tool for parsing domain names. This module makes use of the data provided
by the Public Suffix List (http://publicsuffix.org/list/) to parse TLDs.


%prep
%setup -q -n ParseUtil-Domain-%{version}

# Remove incorrect executable bits
chmod -x lib/ParseUtil/Domain.pm \
         data/effective_tld_names.txt

# Add perl shebang to script
sed -i -e '1i#!%{__perl}' bin/suffix-regex.pl bin/punyconvert

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}


%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

%{_fixperms} %{buildroot}/*


%check
TEST_AUTHOR=1 make test


%files
%doc data/effective_tld_names.txt
%{_bindir}/punyconvert
%{_bindir}/suffix-regex.pl
%{_mandir}/man1/punyconvert.1*
%{_mandir}/man3/ParseUtil::Domain*3pm*
%{perl_vendorlib}/ParseUtil*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.427-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.427-9
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.427-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.427-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.427-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.427-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.427-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.427-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.427-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 22 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 2.427-1
- Update to 2.427

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.426-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.426-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.426-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.426-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.426-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 2.426-1
- Update to 2.426

* Mon Dec 14 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 2.425-2
- Add perl(Mock::Quick) to the BuildRequires
- Enable more tests

* Fri Dec 11 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 2.425-1
- Update to 2.425

* Sat Dec 05 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 2.424-1
- Update to 2.424

* Sun Nov 15 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 2.422-1
- Update to 2.422

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.42-2
- Perl 5.22 rebuild

* Sun Oct 19 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 2.42-1
- Update to 2.42
- Update dependencies

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.36-2
- Perl 5.20 rebuild

* Sun Aug 31 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 2.36-1
- Update to 2.36

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Sep 13 2013 Paul Howarth <paul@city-fan.org> - 2.30-1
- Update to 2.30 for Perl 5.18 support (#992709)

* Fri Aug 09 2013 Petr Pisar <ppisar@redhat.com> - 2.22-5
- Perl 5.18 rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 06 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 2.22-3
- Change "tlds" to "TLDs" in the description.
- Add missing build requirements.

* Fri Jan 25 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 2.22-2
- Replace usage of the %%{__perl} macro by the plain perl command.
- Add missing build requirements.
- Remove incorrect executable bits.

* Wed Jan 02 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 2.22-1
- Initial package for Fedora, with help from cpanspec.
