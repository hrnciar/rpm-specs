Name:           perl-AI-Categorizer
Version:        0.09
Release:        24%{?dist}
Summary:        Automatic Text Categorization

License:        GPL+ or Artistic
URL:            https://metacpan.org/release/AI-Categorizer

Source0:        https://cpan.metacpan.org/authors/id/K/KW/KWILLIAMS/AI-Categorizer-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  findutils
BuildRequires:  perl-interpreter >= 1:5.6.0
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)

# For the unit tests
BuildRequires:  perl(AI::DecisionTree) >= 0.06
BuildRequires:  perl(Algorithm::NaiveBayes)
BuildRequires:  perl(Algorithm::SVM) >= 0.06
BuildRequires:  perl(Algorithm::SVM::DataSet)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Container) >= 0.09
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Lingua::Stem) >= 0.5
BuildRequires:  perl(Params::Validate) >= 0.18
BuildRequires:  perl(Statistics::Contingency) >= 0.06
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(Time::Progress) >= 1.1

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(AI::DecisionTree) >= 0.06
Requires:       perl(Algorithm::NaiveBayes)
Requires:       perl(Algorithm::SVM) >= 0.06
Requires:       perl(Class::Container) >= 0.09
Requires:       perl(Lingua::Stem) >= 0.5
Requires:       perl(Params::Validate) >= 0.18
Requires:       perl(Statistics::Contingency) >= 0.06
Requires:       perl(Time::Progress) >= 1.1

%{?perl_default_filter}

%description
AI::Categorizer is a framework for automatic text categorization. It
consists of a collection of Perl modules that implement common
categorization tasks, and a set of defined relationships among those
modules. The various details are flexible - for example, you can choose
what categorization algorithm to use, what features (words or otherwise) of
the documents should be used (or how to automatically choose these
features), what format the documents are in, and so on.


%prep
%setup -q -n AI-Categorizer-%{version}

# Fix permissions
find . -name '*.pm' -exec chmod -x '{}' \;


%build
%{__perl} Build.PL installdirs=vendor
./Build


%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*


%check
./Build test


%files
%doc Changes README
%{perl_vendorlib}/AI/Categorizer*
%{_mandir}/man3/AI::Categorizer*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-23
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-20
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-17
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-14
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-12
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-10
- Specify all dependencies

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 07 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-8
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-7
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 26 2013 Petr Pisar <ppisar@redhat.com> - 0.09-4
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 22 2012 Mathieu Bridon <bochecha@fedoraproject.org> - 0.09-2
- A couple of fixes based on Emmanuel's review feedback:
  - Add the Perl default filter,
  - Fix the permissions on the pm files.

* Mon Aug 20 2012 Mathieu Bridon <bochecha@fedoraproject.org> 0.09-1
- Initial spec file, with help from cpanspec.
