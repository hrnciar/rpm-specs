Name:		perl-Regexp-Trie
Version:	0.02
Release:	6%{?dist}
Summary:	Build trie-ized regexp
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Regexp-Trie
Source0:	https://cpan.metacpan.org/modules/by-module/Regexp/Regexp-Trie-%{version}.tar.gz
Patch0:		Regexp-Trie-0.02-test.patch
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Time::HiRes)
%if 0%{?fedora} < 18 && 0%{?rhel} < 7
BuildRequires:	procps
%else
BuildRequires:	procps-ng
%endif
BuildRequires:	words
# Dependencies
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This module is a faster but simpler version of Regexp::Assemble or
Regexp::Optimizer. It builds a trie-ized regexp as above. This module is
faster than Regexp::Assemble but you can only add literals:
a+b is treated as a\+b, not "more than one a's followed by b".

%prep
%setup -q -n Regexp-Trie-%{version}

# Fix issues in t/01-dict.t
%patch0

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test
prove --lib %{buildroot}%{perl_vendorlib} t/01-dict.t :: /usr/share/dict/words

%files
%doc Changes README
%{perl_vendorlib}/Regexp/
%{_mandir}/man3/Regexp::Trie.3*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.02-3
- Perl 5.30 rebuild

* Tue Feb  5 2019 Paul Howarth <paul@city-fan.org> - 0.02-2
- Improve test coverage by running t/01-dict.t (long test) as well

* Sun Feb  3 2019 Paul Howarth <paul@city-fan.org> - 0.02-1
- Initial RPM version
