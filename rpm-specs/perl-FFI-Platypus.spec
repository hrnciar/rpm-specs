# Enable C++ support
%bcond_without perl_FFI_Platypus_enables_cpp
# Enable Fortran support
%bcond_without perl_FFI_Platypus_enables_fortran
# Perform optional tests
%bcond_without perl_FFI_Platypus_enables_optional_test

Name:           perl-FFI-Platypus
Version:        1.30
Release:        2%{?dist}
Summary:        Write Perl bindings to non-Perl libraries with FFI
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/FFI-Platypus
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/FFI-Platypus-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Alien::Base::Wrapper)
# Alien::FFI || Alien::FFI::pkgconfig
BuildRequires:  perl(Alien::FFI) >= 0.20
# Alien::FFI::PkgConfigPP not used on Linux
BuildRequires:  perl(base)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.12
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(lib)
# Math::Int64 0.34 used only on perls without long integers
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
%if %{with perl_FFI_Platypus_enables_cpp}
BuildRequires:  gcc-c++
%endif
# gcc-gfortran not used at tests
BuildRequires:  perl(bytes)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(constant) >= 1.32
BuildRequires:  perl(Exporter)
BuildRequires:  perl(FFI::CheckLib) >= 0.05
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util) >= 1.45
# Math::Complex not used because the distribution does not enables
# long doubles in perl
# Math::LongDouble not used because the distribution does not enables
# long doubles in perl
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(B)
BuildRequires:  perl(Encode)
BuildRequires:  perl(if)
BuildRequires:  perl(open)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(utf8)
%if %{with perl_FFI_Platypus_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Acme::Alien::DontPanic) >= 1.03
BuildRequires:  perl(Devel::Hide) >= 0.0010
# gcc used by FFI::Build::Platform
%endif
Requires:       gcc
%if %{with perl_FFI_Platypus_enables_cpp}
# gcc-c++ used by FFI::Build::Platform
Recommends:     gcc-c++
%endif
%if %{with perl_FFI_Platypus_enables_fortran}
# gcc-gfortran used by FFI::Build::Platform
Recommends:     gcc-gfortran
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(bytes)
Requires:       perl(FFI::CheckLib) >= 0.05
Requires:       perl(IPC::Cmd)

# Do not export a SONAME of a private plfill library used by
# FFI::Platypus::Memory as a fallback
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^libplfill.so\\(\\)
# Do not export private redefinitions
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(FFI::Platypus\\)$

%description
Platypus is a Perl library for creating interfaces to machine code libraries
written in languages like C, C++, Fortran, Rust, Pascal. Essentially anything
that gets compiled into machine code. This implementation uses libffi to
accomplish this task. libffi is battle tested by a number of other scripting
and virtual machine languages, such as Python and Ruby to serve a similar
role. There are a number of reasons why you might want to write an extension
with Platypus instead of XS.

%prep
%setup -q -n FFI-Platypus-%{version}
# Remove bundled modules
rm -rf inc/Alien/{Base,FFI}
perl -i -n -e 'print unless m{^inc/Alien/(?:Base|FFI)\b}' MANIFEST

%build
unset FFI_PLATYPUS_DEBUG_FAKE32 FFI_PLATYPUS_NO_ALLOCA \
    FFI_PLATYPUS_NO_EXTRA_TYPES FFI_PLATYPUS_PROBE_OVERRIDE V
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 \
    OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset FFI_PLATYPUS_DLERROR FFI_PLATYPUS_MEMORY_STRDUP_IMPL PERL5LIB V
make test

%files
%license LICENSE
%doc Changes* CONTRIBUTING examples README SUPPORT
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/FFI*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.30-2
- Perl 5.32 rebuild

* Wed Jun 17 2020 Petr Pisar <ppisar@redhat.com> - 1.30-1
- 1.30 bump

* Mon Jun 08 2020 Petr Pisar <ppisar@redhat.com> - 1.29-1
- 1.29 bump

* Wed May 20 2020 Petr Pisar <ppisar@redhat.com> - 1.28-1
- 1.28 bump

* Thu May 07 2020 Petr Pisar <ppisar@redhat.com> - 1.26-1
- 1.26 bump

* Wed May 06 2020 Petr Pisar <ppisar@redhat.com> - 1.25-1
- 1.25 bump

* Mon May 04 2020 Petr Pisar <ppisar@redhat.com> - 1.24-1
- 1.24 bump

* Thu Apr 16 2020 Petr Pisar <ppisar@redhat.com> - 1.11-1
- 1.11 bump

* Thu Feb 06 2020 Petr Pisar <ppisar@redhat.com> - 1.10-1
- 1.10 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Petr Pisar <ppisar@redhat.com> - 1.09-1
- 1.09 bump

* Thu Jan 02 2020 Petr Pisar <ppisar@redhat.com> - 1.07-1
- 1.07 bump

* Tue Dec 17 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.06-1
- 1.06 bump

* Tue Dec 10 2019 Petr Pisar <ppisar@redhat.com> - 1.02-1
- 1.02 bump

* Mon Nov 18 2019 Petr Pisar <ppisar@redhat.com> - 1.01-1
- 1.01 bump

* Tue Oct 15 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.98-1
- 0.98 bump

* Tue Aug 20 2019 Petr Pisar <ppisar@redhat.com> - 0.96-1
- 0.96 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 24 2019 Petr Pisar <ppisar@redhat.com> - 0.94-1
- 0.94 bump

* Thu Jul 18 2019 Petr Pisar <ppisar@redhat.com> - 0.92-1
- 0.92 bump

* Tue Jul 02 2019 Petr Pisar <ppisar@redhat.com> - 0.90-1
- 0.90 bump

* Wed Jun 19 2019 Petr Pisar <ppisar@redhat.com> - 0.88-1
- 0.88 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.87-2
- Perl 5.30 rebuild

* Tue Apr 23 2019 Petr Pisar <ppisar@redhat.com> - 0.87-1
- 0.87 bump

* Mon Mar 11 2019 Petr Pisar <ppisar@redhat.com> - 0.86-1
- Specfile autogenerated by cpanspec 1.78.
