Name:           perl-Module-Install-Contributors
Version:        0.001
Release:        13%{?dist}
Summary:        Add an x_contributors section to your META.yml
# CONTRIBUTING: CC-SA-BY
# COPYRIGHT:    Public Domain
# other files:  GPL+ or Artistic
License:        (GPL+ or Artistic) and CC-BY-SA and Public Domain
URL:            https://metacpan.org/release/Module-Install-Contributors
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Module-Install-Contributors-%{version}.tar.gz
# To boostrap this package without bundling
Patch0:         Module-Install-Contributors-0.001-Build-without-bundled-Module-Package-modules.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Package)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  sed
# Run-time:
# Modules from ./lib are also used from the patched Makefile.PL.
BuildRequires:  perl(:VERSION) >= 5.6.0
BuildRequires:  perl(base)
BuildRequires:  perl(Module::Install::Base)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This is a plugin for Module::Install. It adds an x_contributors section to
your META.yml file. This is an array of strings, which should normally be in
"Name <email>" format, that is passed to contributors() function in
a Makefile.PL.

%prep
%setup -q -n Module-Install-Contributors-%{version}
%patch0 -p1
# Remove bundled modules.
# And remove inc/Module/Package/Dist/RDF.pm becaus it's a Module::Package::RDF
# plug-in that depends on package transitively. Fortunatelly, the
# inc/Module/Package/Dist/RDF.pm is not good for anything so the patch makes
# not to load it.
rm -r ./inc
sed -i -e '/^inc/d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING COPYRIGHT CREDITS README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jun 24 2016 Petr Pisar <ppisar@redhat.com> 0.001-1
- Specfile autogenerated by cpanspec 1.78.
