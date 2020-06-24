Name:           perl-Net-IDN-Encode
Summary:        Internationalizing Domain Names in Applications (IDNA)
Version:        2.500
Release:        7%{?dist}
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Net-IDN-Encode
Source0:        https://cpan.metacpan.org/authors/id/C/CF/CFAERBER/Net-IDN-Encode-%{version}.tar.gz
# Make Unicode property generator compatible with perl 5.30-RC1,
# CPAN RT#129588, <https://github.com/cfaerber/Net-IDN-Encode/pull/8>
Patch0:         Net-IDN-Encode-2.500-Make-generated-arrays-available-at-compile-time.patch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-common
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(integer)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(open)
# An optional dependency, via Unicode::UCD
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Unicode::Normalize)
BuildRequires:  perl(Unicode::UCD)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# This isn't picked up automatically by rpmbuild
Requires:       perl(XSLoader)

%{?perl_default_filter}

%description
This module provides an easy-to-use interface for encoding and decoding
Internationalized Domain Names (IDNs).


%prep
%setup -q -n Net-IDN-Encode-%{version}
%patch0 -p1

# Remove incorrect executable bits
chmod -x lib/Net/IDN/Encode.pm \
         lib/Net/IDN/Standards.pod

# Convert files to UTF-8
for FILE in LICENSE README; do
  iconv -f ISO_8859-1 -t UTF8 $FILE > $FILE.utf8
  mv $FILE.utf8 $FILE
done


%build
%{__perl} Build.PL installdirs=vendor optimize="%{optflags}"
./Build


%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

%{_fixperms} %{buildroot}/*


%check
./Build test


%files
%doc Changes eg README
%license LICENSE
%{perl_vendorarch}/auto/Net
%{perl_vendorarch}/Net
%{_mandir}/man3/Net::IDN::*.3pm*


%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.500-7
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.500-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.500-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.500-4
- Perl 5.30 rebuild

* Fri May 17 2019 Petr Pisar <ppisar@redhat.com> - 2.500-3
- Make Unicode property generator compatible with perl 5.30-RC1
  (CPAN RT#129588)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.500-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 14 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 2.500-1
- Update to 2.500

* Sun Sep 23 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 2.401-1
- Update to 2.401

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.400-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.400-8
- Perl 5.28 rebuild

* Fri Mar 02 2018 Petr Pisar <ppisar@redhat.com> - 2.400-7
- Adapt to removing GCC from a build root (bug #1547165)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.400-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.400-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.400-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.400-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.400-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 08 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 2.400-1
- Update to 2.400

* Sun Dec 11 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 2.303-1
- Update to 2.303

* Sun Dec 04 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 2.301-1
- Update to 2.301

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.300-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.300-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 11 2015 Petr Šabata <contyk@redhat.com> - 2.300-2
- Prevent FTBFS by correcting the build time dependency list

* Thu Jul 23 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 2.300-1
- Update to 2.300
- Use %%license tag

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.202-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.202-2
- Perl 5.22 rebuild

* Sat Apr 25 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 2.202-1
- Update to 2.202

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.201-2
- Perl 5.20 rebuild

* Sun Aug 31 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 2.201-1
- Update to 2.201

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.003-8
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.003-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.003-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.003-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 2.003-4
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.003-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 17 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 2.003-2
- Add missing build requirements.
- Add a requirement left out by rpmbuild.
- Remove the incorrect executable bits.
- Make sure all files are UTF-8 encoded.

* Wed Jan 02 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 2.003-1
- Initial package for Fedora, with help from cpanspec.
