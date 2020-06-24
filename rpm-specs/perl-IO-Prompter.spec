Name:           perl-IO-Prompter
Version:        0.004015
Release:        5%{?dist}
Summary:        Prompt for input, read it, clean it, return it

License:        GPL+ or Artistic
URL:            https://search.cpan.org/dist/IO-Prompter/
Source0:        https://www.cpan.org/modules/by-module/IO/IO-Prompter-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.010
BuildRequires:  perl(Carp)
BuildRequires:  perl(Contextual::Return)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(diagnostics)
BuildRequires:  perl(lib)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
IO::Prompter exports a single subroutine, prompt, that prints a prompt
(but only if the program's selected input and output streams are connected
to a terminal), then reads some input, then chomps it, and finally returns
an object representing that text.


%prep
%autosetup -n IO-Prompter-%{version} -p 1


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%make_install
%{_fixperms} %{buildroot}/*


%check
%make_build test


%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.004015-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.004015-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.004015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.004015-2
- Perl 5.30 rebuild

* Mon Feb 25 2019 Björn Esser <besser82@fedoraproject.org> - 0.004015-1
- Bump release to stable (#1680374)

* Sun Feb 24 2019 Björn Esser <besser82@fedoraproject.org> - 0.004015-0.3
- Changes as suggested in review (#1680374)
- Add a BR for Perl required version
- Add a set of explicit BuildRequires
- Use %%make_install
- Drop cleanups using find
- Drop META.json fom %%doc

* Sun Feb 24 2019 Björn Esser <besser82@fedoraproject.org> - 0.004015-0.2
- Add explicit perl module compat requires

* Sun Feb 24 2019 Björn Esser <besser82@fedoraproject.org> - 0.004015-0.1
- Initial rpm release (#1680374)
