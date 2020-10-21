# Perform optional test
%bcond_without perl_HTML_FormatExternal_enables_optional_test
# Enable a formatter using ELinks
%bcond_without perl_HTML_FormatExternal_enables_elinks
# Enable a formatter using html2text
%bcond_without perl_HTML_FormatExternal_enables_html2text
# Enable a formatter using Links
%bcond_without perl_HTML_FormatExternal_enables_links
# Enable a formatter using Lynx
%bcond_without perl_HTML_FormatExternal_enables_lynx
# Enable a formatter using Netrik
# netrik executable not yet packaged
%bcond_with perl_HTML_FormatExternal_enables_netrik
# Enable a formatter using Vilistextum
# vilistextum executable not yet packaged
%bcond_with perl_HTML_FormatExternal_enables_vilistextum
# Enable a formatter using w3m
%bcond_without perl_HTML_FormatExternal_enables_w3m
# Enable a formatter using Zen
# zen executable not yet packaged
%bcond_with perl_HTML_FormatExternal_enables_zen

Name:           perl-HTML-FormatExternal
Version:        26
Release:        6%{?dist}
Summary:        HTML to text formatting using external programs
# debian/rules:     GPLv3+
# debian/copyright: GPLv3+
# README:           GPLv3+
License:        GPLv3+
URL:            https://metacpan.org/release/HTML-FormatExternal
Source0:        https://cpan.metacpan.org/authors/id/K/KR/KRYDE/HTML-FormatExternal-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(constant::defer)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(File::Temp) >= 0.18
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(URI::file) >= 0.08
# Tests:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
%if %{with perl_HTML_FormatExternal_enables_optional_test}
# Optional tests:
# Devel::FindRef removed from a distribution (bug #1231234)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(Taint::Util)
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Encode)
Requires:       perl(File::Copy)
Requires:       perl(File::Temp) >= 0.18

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(URI::file\\)$

%description
This is a common base for formatter modules which turn HTML into plain text
by dumping it through the respective external programs. Available modules are:

%{?with_perl_HTML_FormatExternal_enables_elinks:HTML::FormatText::Elinks}
%{?with_perl_HTML_FormatExternal_enables_html2text:HTML::FormatText::Html2text}
%{?with_perl_HTML_FormatExternal_enables_links:HTML::FormatText::Links}
%{?with_perl_HTML_FormatExternal_enables_lynx:HTML::FormatText::Lynx}
%{?with_perl_HTML_FormatExternal_enables_netrik:HTML::FormatText::Netrik}
%{?with_perl_HTML_FormatExternal_enables_vilistextum:HTML::FormatText::Vilistextum}
%{?with_perl_HTML_FormatExternal_enables_w3m:HTML::FormatText::W3m}
%{?with_perl_HTML_FormatExternal_enables_zen:HTML::FormatText::Zen}

%if %{with perl_HTML_FormatExternal_enables_elinks}
%package Elinks
Summary:        Format HTML as plain text using ELinks
Requires:       %{name} = %{?epoch:%{epoch:}}%{version}-%{release}
Requires:       elinks
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(URI::file) >= 0.08
%description Elinks
This Perl module turns HTML into plain text using the ELinks program.
%endif

%if %{with perl_HTML_FormatExternal_enables_html2text}
%package Html2text
Summary:        Format HTML as plain text using html2text
Requires:       %{name} = %{?epoch:%{epoch:}}%{version}-%{release}
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       python3-html2text
%description Html2text
This Perl module turns HTML into plain text using the html2text program.
%endif

%if %{with perl_HTML_FormatExternal_enables_links}
%package Links
Summary:        Format HTML as plain text using Links
Requires:       %{name} = %{?epoch:%{epoch:}}%{version}-%{release}
Requires:       links
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(URI::file) >= 0.08
%description Links
This Perl module turns HTML into plain text using the Links program.
%endif

%if %{with perl_HTML_FormatExternal_enables_lynx}
%package Lynx
Summary:        Format HTML as plain text using Lynx
Requires:       %{name} = %{?epoch:%{epoch:}}%{version}-%{release}
Requires:       lynx
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(URI::file) >= 0.08
%description Lynx
This Perl module turns HTML into plain text using the Lynx program.
%endif

%if %{with perl_HTML_FormatExternal_enables_netrik}
%package Netrik
Summary:        Format HTML as plain text using Netrik
Requires:       %{name} = %{?epoch:%{epoch:}}%{version}-%{release}
Requires:       netrik
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(URI::file) >= 0.08
%description Netrik
This Perl module turns HTML into plain text using the Netrik program.
%endif

%if %{with perl_HTML_FormatExternal_enables_vilistextum}
%package Vilistextum
Summary:        Format HTML as plain text using Vilistextum
Requires:       %{name} = %{?epoch:%{epoch:}}%{version}-%{release}
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       vilistextum
%description Vilistextum
This Perl module turns HTML into plain text using the Vilistextum program.
%endif

%if %{with perl_HTML_FormatExternal_enables_w3m}
%package W3m
Summary:        Format HTML as plain text using w3m
Requires:       %{name} = %{?epoch:%{epoch:}}%{version}-%{release}
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(URI::file) >= 0.08
Requires:       w3m
%description W3m
This Perl module turns HTML into plain text using the w3m program.
%endif

%if %{with perl_HTML_FormatExternal_enables_zen}
%package Zen
Summary:        Format HTML as plain text using Zen
Requires:       %{name} = %{?epoch:%{epoch:}}%{version}-%{release}
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       zen
%description Zen
This Perl module turns HTML into plain text using the Zen program.
%endif

%prep
%setup -q -n HTML-FormatExternal-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
# t/taint.t requires enabled taint mode
export HARNESS_PERL_SWITCHES=-T
make test

%files
%license COPYING
%doc Changes examples README
%{perl_vendorlib}/*
%exclude %{perl_vendorlib}/HTML/FormatText/*
%{_mandir}/man3/*
%exclude %{_mandir}/man3/HTML::FormatText::*

%if %{with perl_HTML_FormatExternal_enables_elinks}
%files Elinks
%{perl_vendorlib}/HTML/FormatText/Elinks.pm
%{_mandir}/man3/HTML::FormatText::Elinks.*
%endif

%if %{with perl_HTML_FormatExternal_enables_html2text}
%files Html2text
%{perl_vendorlib}/HTML/FormatText/Html2text.pm
%{_mandir}/man3/HTML::FormatText::Html2text.*
%endif

%if %{with perl_HTML_FormatExternal_enables_links}
%files Links
%{perl_vendorlib}/HTML/FormatText/Links.pm
%{_mandir}/man3/HTML::FormatText::Links.*
%endif

%if %{with perl_HTML_FormatExternal_enables_lynx}
%files Lynx
%{perl_vendorlib}/HTML/FormatText/Lynx.pm
%{_mandir}/man3/HTML::FormatText::Lynx.*
%endif

%if %{with perl_HTML_FormatExternal_enables_netrik}
%files Netrik
%{perl_vendorlib}/HTML/FormatText/Netrik.pm
%{_mandir}/man3/HTML::FormatText::Netrik.*
%endif

%if %{with perl_HTML_FormatExternal_enables_vilistextum}
%files Vilistextum
%{perl_vendorlib}/HTML/FormatText/Vilistextum.pm
%{_mandir}/man3/HTML::FormatText::Vilistextum.*
%endif

%if %{with perl_HTML_FormatExternal_enables_w3m}
%files W3m
%{perl_vendorlib}/HTML/FormatText/W3m.pm
%{_mandir}/man3/HTML::FormatText::W3m.*
%endif

%if %{with perl_HTML_FormatExternal_enables_zen}
%files Zen
%{perl_vendorlib}/HTML/FormatText/Zen.pm
%{_mandir}/man3/HTML::FormatText::Zen.*
%endif

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 26-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 26-2
- Perl 5.30 rebuild

* Fri Feb 01 2019 Petr Pisar <ppisar@redhat.com> 26-1
- Specfile autogenerated by cpanspec 1.78.
