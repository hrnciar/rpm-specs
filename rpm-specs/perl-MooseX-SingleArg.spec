Name:           perl-MooseX-SingleArg
Version:        0.09
Release:        6%{?dist}
Summary:        No-fuss instantiation of Moose objects using a single argument
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/MooseX-SingleArg/
Source0:        http://www.cpan.org/modules/by-module/MooseX/MooseX-SingleArg-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Moose) >= 1.23
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test2::V0) >= 0.000094
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module allows Moose instances to be constructed with a single
argument. Your class or role must use this module and then use the
single_arg sugar to declare which attribute will be assigned the single
argument value.

%prep
%setup -q -n MooseX-SingleArg-%{version}

%build
%{__perl} Build.PL --prefix=%{_prefix} --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes cpanfile META.json README.md
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-2
- Perl 5.30 rebuild

* Thu Feb 28 2019 Xavier Bachelot <xavier@bachelot.org> 0.09-1
- Update to 0.09 (RHBZ#1683332).

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 03 2018 Xavier Bachelot <xavier@bachelot.org> 0.08-2
- Changes from package review.

* Wed Nov 28 2018 Xavier Bachelot <xavier@bachelot.org> 0.08-1
- Initial package.
