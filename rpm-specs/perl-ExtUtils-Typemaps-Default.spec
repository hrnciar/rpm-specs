Name:           perl-ExtUtils-Typemaps-Default
Version:        1.05
Release:        18%{?dist}
Summary:        Set of useful typemaps
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/ExtUtils-Typemaps-Default
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/ExtUtils-Typemaps-Default-%{version}.tar.gz
BuildArch:      noarch
# temporary fix until more recent version is available
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::Typemaps) >= 3.18-292
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
Requires:       perl(ExtUtils::Typemaps) >= 3.18-292
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# Filtering unversioned requires
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(ExtUtils::Typemaps\\)$

%description
ExtUtils::Typemaps::Default is an ExtUtils::Typemaps subclass that provides
a set of default mappings (in addition to what perl itself provides). These
default mappings are currently defined as the combination of the mappings
provided by the following typemap classes which are provided in this
distribution:

ExtUtils::Typemaps::ObjectMap
ExtUtils::Typemaps::STL
ExtUtils::Typemaps::Basic

%prep
%setup -q -n ExtUtils-Typemaps-Default-%{version}

# this is fixed in BuildRequired version of ExtUtils::Typemap 3.18-292
sed -i 's/3.18_03/3.18/' Build.PL

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.05-18
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.05-15
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.05-12
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.05-9
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.05-7
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.05-4
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.05-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 11 2013 Miro Hrončok <mhroncok@redhat.com> - 1.05-1
- New upstream release 1.05 (#1039710)
- Temporarily (build)require ExtUtils::Typemaps >= 3.18-292, patch Build.PL to accept it

* Wed Aug 28 2013 Miro Hrončok <mhroncok@redhat.com> - 1.04-1
- New upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.01-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 06 2013 Miro Hrončok <miro@hroncok.cz> - 1.01-3
- Removed deleting empty dirs
- Removed META.json from doc
- Filtered unversioned requires

* Fri Nov 16 2012 Miro Hrončok <miro@hroncok.cz> - 1.01-2
- Removed BRs provided by perl package
- Removed perl autofilter

* Wed Nov 14 2012 Miro Hrončok <miro@hroncok.cz> 1.01-1
- New version.
- Longer description.

* Tue Sep 25 2012 Miro Hrončok <miro@hroncok.cz> 1.00-1
- Specfile autogenerated by cpanspec 1.78 and revised.
