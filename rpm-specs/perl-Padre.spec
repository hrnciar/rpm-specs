%global use_x11_tests 1

Name:           perl-Padre
Version:        0.90
Release:        32%{?dist}
Summary:        Perl Application Development and Refactoring Environment
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Padre
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLAVEN/Padre-%{version}.tar.gz
Source1:        padre.desktop
# Fix compatibility with ORLite-1.98, in Padre-1.96, bug #914310
Patch0:         Padre-0.90-Migrating-to-the-delete_where-method-for-bulk-deleti.patch
# Fix compatibility with Pod::Perldoc >= 3.21_01, bug #1083396
Patch1:         Padre-0.90-No-exit-in-Pod-Perldoc.patch
# Disable Test::NoWarnings t/01-load.t tests not to confuse with Padre's
# intentional warning on perl 5.20, in Padre-1.02, bug #1141153
Patch2:         Padre-0.90-Disable-Test-NoWarnings-t-01-load.t-tests.patch
# Adjust a test for perl-5.22 diagnostic messages, bug #1231893, CPAN RT#99293
Patch3:         Padre-0.90-The-text-of-the-error-has-changed-in-perl-5.21.4.-RT.patch
# Fix a precedence issue reported by perl-5.22, bug #1231893
Patch4:         Padre-1.00-eliminate-precedence-issue.patch
# Fix setting SQLite synchronous level, bug #1234733,
# <https://github.com/PadreIDE/Padre/issues/17>
Patch5:         Padre-0.90-Change-synchronous-SQLite-level-before-opening-trans.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Alien::wxWidgets) >= 0.46
# perl(Capture::Tiny) at lib/Padre/Wx/Command.pm:160, version from META.yml
BuildRequires:  perl(Capture::Tiny) >= 0.06
BuildRequires:  perl(CGI) >= 3.47
BuildRequires:  perl(Class::Adapter) >= 1.05
BuildRequires:  perl(Class::Inspector) >= 1.22
BuildRequires:  perl(Class::Unload) >= 0.03
BuildRequires:  perl(Class::XSAccessor) >= 1.05
BuildRequires:  perl(Class::XSAccessor::Array) >= 1.05
# perl(constant) at lib/Padre/PluginManager.pm:52
BuildRequires:  perl(constant)
# Real version perl(Cwd) >= 3.2701 rounded
BuildRequires:  perl(Cwd) >= 3.28
BuildRequires:  perl(DBD::SQLite) >= 1.27
BuildRequires:  perl(DBI) >= 1.58
BuildRequires:  perl(Data::Dumper) >= 2.101
BuildRequires:  perl(Debug::Client) => 0.11
BuildRequires:  perl(Devel::Dumpvar) >= 0.04
BuildRequires:  perl(Devel::Refactor) >= 0.05
BuildRequires:  perl(Encode) >= 2.26
# perl(Exporter) at lib/Padre/Current.pm:88
BuildRequires:  perl(Exporter)
# perl(ExtUtils::Embed) because Padre build system supports win32.
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.56
BuildRequires:  perl(ExtUtils::Manifest) >= 1.56
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Copy::Recursive) >= 0.37
BuildRequires:  perl(File::Find::Rule) >= 0.30
# perl(File::Glob) is not used anywhere
BuildRequires:  perl(File::HomeDir) >= 0.91
BuildRequires:  perl(File::Path) >= 2.08
BuildRequires:  perl(File::pushd) >= 1.00
BuildRequires:  perl(File::Remove) >= 1.42
BuildRequires:  perl(File::ShareDir) >= 1.00
# Real version perl(File::Spec) >= 3.2701 rounded
BuildRequires:  perl(File::Spec) >= 3.28
# Real version perl(File::Spec::Functions) >= 3.2701 rounded
BuildRequires:  perl(File::Spec::Functions) >= 3.28
# perl(File::Spec::Unix) at lib/Padre/Project/Perl/Temp.pm:8
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(File::Temp) >= 0.20
BuildRequires:  perl(File::Which) >= 1.08
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Format::Human::Bytes) >= 0.04
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::Entities) >= 3.57
BuildRequires:  perl(HTML::Parser) >= 3.58
# perl(HTTP::Cookies) at lib/Padre/Sync.pm:28
BuildRequires:  perl(HTTP::Cookies)
# perl(HTTP::Request) at lib/Padre/Task/LWP.pm:124
BuildRequires:  perl(HTTP::Request)
# perl(HTTP::Request::Common) at lib/Padre/Sync.pm:29
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(IO::Scalar) >= 2.110
BuildRequires:  perl(IO::Socket) >= 1.30
BuildRequires:  perl(IO::String) >= 1.08
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(IPC::Run) >= 0.83
BuildRequires:  perl(JSON::XS) >= 2.29
# perl(lib) at Makefile.PL:7
BuildRequires:  perl(lib)
BuildRequires:  perl(List::MoreUtils) >= 0.22
BuildRequires:  perl(List::Util) >= 1.18
BuildRequires:  perl(Locale::Msgfmt) >= 0.15
BuildRequires:  perl(LWP) >= 5.815
BuildRequires:  perl(LWP::UserAgent) >= 5.815
BuildRequires:  perl(Module::Build) >= 0.37
BuildRequires:  perl(Module::CoreList) >= 2.22
BuildRequires:  perl(Module::Manifest) >= 0.07
# Padre-0.90 states ORLite-1.48, but we have 1.98 and a patch for Padre,
# bug #914310
BuildRequires:  perl(ORLite) >= 1.98
BuildRequires:  perl(Params::Util) >= 0.33
BuildRequires:  perl(Parse::ErrorString::Perl) >= 0.14
BuildRequires:  perl(Parse::ExuberantCTags) >= 1.00
BuildRequires:  perl(Pod::Abstract) >= 0.16
BuildRequires:  perl(Pod::Functions)
BuildRequires:  perl(Pod::POM) >= 0.17
# Pod::Perldoc 3.15 and 3.21 for Patch1
BuildRequires:  perl(Pod::Perldoc) >= 3.21
# perl(Pod::Perldoc::ToPod) at lib/Padre/Browser/PseudoPerldoc.pm
BuildRequires:  perl(Pod::Perldoc::ToPod)
BuildRequires:  perl(Pod::Simple) >= 3.07
BuildRequires:  perl(Pod::Simple::XHTML) >= 3.04
# POD2 directory is used at run time (and test). Seem META.yml.
BuildRequires:  perl(POD2::Base) >= 0.043
BuildRequires:  perl(POSIX)
BuildRequires:  perl(PPI) >= 1.213
# perl(PPI::Document) at lib/Padre/Task/PPI.pm
BuildRequires:  perl(PPI::Document)
# perl(PPI::Dumper) at lib/Padre/Plugin/Devel.pm
BuildRequires:  perl(PPI::Dumper)
# perl(PPI::Transform) at lib/Padre/PPI/Transform.pm
BuildRequires:  perl(PPI::Transform)
BuildRequires:  perl(PPIx::EditorTools) >= 0.13
BuildRequires:  perl(PPIx::Regexp) >= 0.005
BuildRequires:  perl(Probe::Perl) >= 0.01
# perl(Scalar::Util) at lib/Padre.pm
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable) >= 2.16
BuildRequires:  perl(Template::Tiny) >= 0.11
BuildRequires:  perl(Test::Exception) >= 0.27
BuildRequires:  perl(Test::MockObject) >= 1.09
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::NoWarnings) >= 0.084
BuildRequires:  perl(Test::Script) >= 1.07
BuildRequires:  perl(Template::Tiny) >= 0.11
BuildRequires:  perl(Text::Balanced) >= 2.01
BuildRequires:  perl(Text::Diff) >= 0.35
BuildRequires:  perl(Text::FindIndent) >= 0.10
BuildRequires:  perl(threads) >= 1.71
BuildRequires:  perl(threads::shared) >= 1.33
BuildRequires:  perl(Time::HiRes) >= 1.9718
BuildRequires:  perl(UNIVERSAL)
BuildRequires:  perl(URI)
BuildRequires:  perl(version) >= 0.80
BuildRequires:  perl(Wx) >= 0.91
# perl(Wx::App) at lib/Padre/Wx/App.pm:39
BuildRequires:  perl(Wx::App)
# perl(Wx::AUI) at lib/Padre/Wx.pm:21
BuildRequires:  perl(Wx::AUI)
# perl(Wx::DND) at lib/Padre/Wx.pm:19
BuildRequires:  perl(Wx::DND)
# perl(Wx::Event) at lib/Padre/Wx.pm:18
BuildRequires:  perl(Wx::Event)
# perl(Wx::Frame) at lib/Padre/Wx/CPAN.pm:13
BuildRequires:  perl(Wx::Frame)
# perl(Wx::Html) at lib/Padre/Wx/HtmlWindow.pm
BuildRequires:  perl(Wx::Html)
# perl(Wx::Locale) at lib/Padre/Wx.pm:22
BuildRequires:  perl(Wx::Locale)
BuildRequires:  perl(Wx::Perl::ProcessStream) >= 0.29
# perl(Wx::Print) at lib/Padre/Wx/Printout.pm
BuildRequires:  perl(Wx::Print)
# perl(Wx::RichText) at lib/Padre/Wx/Output.pm
BuildRequires:  perl(Wx::RichText)
# perl(Wx::STC) at lib/Padre/Wx.pm:20
BuildRequires:  perl(Wx::STC)
BuildRequires:  perl(YAML::Tiny) >= 1.32
%if %{use_x11_tests}
# X11 tests:
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xorg-x11-xinit
BuildRequires:  font(:lang=en)
%endif

Requires:       perl(App::cpanminus) >= 0.9923
# perl(Capture::Tiny) at lib/Padre/Wx/Command.pm:160, version from META.yml
Requires:       perl(Capture::Tiny) >= 0.06
Requires:       perl(Class::Adapter) >= 1.05
Requires:       perl(Class::Inspector) >= 1.22
Requires:       perl(Class::Unload) >= 0.03
Requires:       perl(Class::XSAccessor::Array) >= 1.02
# Real version perl(Cwd) >= 3.2701 rounded
Requires:       perl(Cwd) >= 3.28
Requires:       perl(CGI) >= 3.47
Requires:       perl(DBD::SQLite) >= 1.27
Requires:       perl(Data::Dumper)
Requires:       perl(Debug::Client) => 0.11
Requires:       perl(Devel::Dumpvar) >= 0.04
Requires:       perl(Devel::Refactor) >= 0.05
Requires:       perl(Encode) >= 2.26
Requires:       perl(ExtUtils::MakeMaker) >= 6.56
Requires:       perl(ExtUtils::Manifest) >= 1.56
Requires:       perl(File::Copy)
Requires:       perl(File::Copy::Recursive) >= 0.37
Requires:       perl(File::Find::Rule) >= 0.30
Requires:       perl(File::Path) >= 2.08
Requires:       perl(File::Remove) >= 1.42
Requires:       perl(File::ShareDir) >= 1.00
# Real version perl(File::Spec) >= 3.2701 rounded
Requires:       perl(File::Spec) >= 3.28
# Real version perl(File::Spec::Functions) >= 3.2701 rounded
Requires:       perl(File::Spec::Functions) >= 3.28
Requires:       perl(File::Temp) >= 0.20
Requires:       perl(File::Which) >= 1.08
Requires:       perl(File::pushd) >= 1.00
Requires:       perl(Format::Human::Bytes) >= 0.04
Requires:       perl(Getopt::Long)
Requires:       perl(HTML::Entities) >= 3.57
Requires:       perl(HTML::Parser) >= 3.58
# perl(HTTP::Request) at lib/Padre/Task/LWP.pm:124
Requires:       perl(HTTP::Request)
Requires:       perl(IO::Scalar) >= 2.110
Requires:       perl(IO::Socket) >= 1.30
Requires:       perl(IO::String) >= 1.08
Requires:       perl(IPC::Open2)
Requires:       perl(IPC::Open3)
Requires:       perl(IPC::Run) >= 0.83
Requires:       perl(JSON::XS) >= 2.29
Requires:       perl(List::MoreUtils) >= 0.22
Requires:       perl(List::Util) >= 1.18
Requires:       perl(LWP::UserAgent) >= 5.815
Requires:       perl(Module::Build) >= 0.37
Requires:       perl(Module::CoreList) >= 2.22
Requires:       perl(Module::Manifest) >= 0.07
# Padre-0.90 states ORLite-1.48, but we have 1.98 and a patch for Padre,
# bug #914310
Requires:       perl(ORLite) >= 1.98
Requires:       perl(POSIX)
Requires:       perl(PPI) >= 1.213
Requires:       perl(PPIx::EditorTools) >= 0.13
Requires:       perl(PPIx::Regexp) >= 0.005
Requires:       perl(Params::Util) >= 0.33
Requires:       perl(Parse::ErrorString::Perl) >= 0.14
Requires:       perl(Parse::ExuberantCTags) >= 1.00
Requires:       perl(Pod::Abstract) >= 0.16
# Pod::Perldoc 3.15 and 3.21 for Patch1
Requires:       perl(Pod::Perldoc) >= 3.21
Requires:       perl(Pod::POM) >= 0.17
Requires:       perl(Pod::Simple) >= 3.07
Requires:       perl(Pod::Simple::XHTML) >= 3.04
# POD2 directory is used at run time (and test). Seem META.yml.
Requires:       perl(POD2::Base) >= 0.043
Requires:       perl(Probe::Perl) >= 0.01
Requires:       perl(Readonly::XS) >= 1.05
Requires:       perl(Storable) >= 2.16
Requires:       perl(Template::Tiny) >= 0.11
Requires:       perl(Term::ReadLine)
Requires:       perl(Text::Balanced) >= 2.01
Requires:       perl(Text::Diff) >= 0.35
Requires:       perl(Text::FindIndent) >= 0.10
Requires:       perl(Time::HiRes) >= 1.9718
Requires:       perl(Wx) >= 0.91
Requires:       perl(Wx::Perl::ProcessStream) >= 0.29
Requires:       perl(YAML::Tiny) >= 1.32
Requires:       perl(threads) >= 1.71
Requires:       perl(version) >= 0.80
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Obsoletes:      perl-Wx-Perl-Dialog < 0.01
Provides:       perl-Wx-Perl-Dialog > 0.01
Provides:       padre = %{version}

# Do not scan documentation from dependencies
%{?perl_default_filter}

# Remove too specific requires because of version rounding
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(File::Spec\\) >= 3.2701

# Remove underspecified dependencies
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Padre::Config\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Capture::Tiny\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Class::Inspector\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Class::Unload\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Class::XSAccessor\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Class::XSAccessor::Array\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Cwd\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(DBD::SQLite\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(DBI\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Encode\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(File::HomeDir\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(File::Path\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(File::ShareDir\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(File::Spec\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(File::Spec::Functions\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(File::Temp\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(IO::Scalar\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(JSON::XS\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(List::Util\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(LWP::UserAgent\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Module::Build\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Params::Util\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Parse::ErrorString::Perl\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Pod::Abstract\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Pod::Perldoc\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Pod::Simple::XHTML\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(PPI\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Storable\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Text::Balanced\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(threads\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(threads::shared\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Time::HiRes\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(version\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Wx\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Wx::Perl::ProcessStream\\)\\s*$
%global __requires_exclude %__requires_exclude|^perl\\(YAML::Tiny\\)\\s*$

# Remove private moduiles
%global __provides_exclude %__provides_exclude|^perl\\(ExtUtils::MakeMaker::_version\\)$

%description
Padre is a text editor aimed to be an IDE for Perl.
The application maintains its configuration information
in a directory called .padre.


%prep
%setup -q -n Padre-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

find share/{examples,templates} -type f \( -name '*.pl' -o -name '*.t' \) \
    -exec chmod 755 {} +


%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

# languages are in different format than %%find_lang expects
find ${RPM_BUILD_ROOT}%{perl_vendorlib}/auto/share/dist/Padre/locale/ \
    -type f -name '*.mo' | \
    sed 's|^'"$RPM_BUILD_ROOT"'||
        s|\(.*/\)\([^.]*\)\(\.mo\)$|%lang(\2) \1\2\3|' > %{name}.lang

# Current upstream desktop file is silly, use our own
rm -f $RPM_BUILD_ROOT/%{perl_vendorlib}/auto/share/dist/Padre/padre.desktop*
# install logo of Padre into correct paths
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/{64x64,16x16}/apps/
install -m644 ./share/icons/padre/64x64/logo.png \
    $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/64x64/apps/padre.png
install -m644 ./share/icons/padre/16x16/logo.png \
    $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/16x16/apps/padre.png
# install icon
desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
--vendor="fedora" \
%endif
--dir=$RPM_BUILD_ROOT/%{_datadir}/applications %{SOURCE1}

%{_fixperms} $RPM_BUILD_ROOT/*


%check
# Fake home directory because tests expect it and touch it
export HOME="$PWD/testhome"
mkdir "$HOME"
%if %{use_x11_tests}
    xvfb-run -a make test
%else
    make test
%endif


%files -f %{name}.lang
%license Artistic COPYING LICENSE
%doc Changes padre.yml README
# To omit %%{perl_vendorlib}/auto/share/dist/Padre/locale/* pulled by -f option
%dir %{perl_vendorlib}/auto
%dir %{perl_vendorlib}/auto/share
%dir %{perl_vendorlib}/auto/share/dist
%dir %{perl_vendorlib}/auto/share/dist/Padre
     %{perl_vendorlib}/auto/share/dist/Padre/doc
     %{perl_vendorlib}/auto/share/dist/Padre/examples
     %{perl_vendorlib}/auto/share/dist/Padre/icons
     %{perl_vendorlib}/auto/share/dist/Padre/languages
%dir %{perl_vendorlib}/auto/share/dist/Padre/locale
     %{perl_vendorlib}/auto/share/dist/Padre/padre-splash*
     %{perl_vendorlib}/auto/share/dist/Padre/ppm
     %{perl_vendorlib}/auto/share/dist/Padre/README.txt
     %{perl_vendorlib}/auto/share/dist/Padre/styles
     %{perl_vendorlib}/auto/share/dist/Padre/templates
%{perl_vendorlib}/Padre*
%{_datadir}/icons/hicolor/64x64/apps/padre.png
%{_datadir}/icons/hicolor/16x16/apps/padre.png
%if 0%{?fedora} && 0%{?fedora} < 19
%{_datadir}/applications/fedora-padre.desktop
%else
%{_datadir}/applications/padre.desktop
%endif
%{_mandir}/man3/*
%{_bindir}/padre


%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.90-32
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.90-29
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.90-26
- Perl 5.28 rebuild

* Mon Feb 19 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.90-25
- Add build-require gcc

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 08 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.90-22
- Perl 5.26 re-rebuild of bootstrapped packages

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.90-20
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.90-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 09 2015 Petr Pisar <ppisar@redhat.com> - 0.90-18
- Do scan documentation for dependencies

* Fri Jun 26 2015 Petr Pisar <ppisar@redhat.com> - 0.90-17
- Fix setting SQLite synchronous level (bug #1234733)

* Thu Jun 18 2015 Petr Pisar <ppisar@redhat.com> - 0.90-16
- Perl 5.22 rebuild
- Modernize spec file
- Use xvfb-run for X11 tests
- Adjust a test for perl-5.22 diagnostic messages (bug #1231893)
- Fix a precedence issue reported by perl-5.22 (bug #1231893)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Sep 15 2014 Petr Pisar <ppisar@redhat.com> - 0.90-14
- Disable Test::NoWarnings tests in t/01-load.t (bug #1141153)

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.90-13
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Petr Pisar <ppisar@redhat.com> - 0.90-11
- Fix compatibility with Pod::Perldoc >= 3.21_01 (bug #1083396)

* Tue Oct 15 2013 Petr Pisar <ppisar@redhat.com> - 0.90-10
- Fix compatibility with ORLite-1.98 (bug #914310)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar  6 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.90-8
- Remove vendor prefix from desktop files in F19+ https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.90-5
- Perl 5.16 rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 0.90-4
- Trim Module::Build dependency version to 2 digits because upstream has
  regressed version

* Thu May 31 2012 Petr Pisar <ppisar@redhat.com> - 0.90-3
- Round Module::Build version to 2 digits

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 29 2011 Petr Pisar <ppisar@redhat.com> - 0.90-1
- 0.90 bump
- Remove RPM-4.8-style dependency filters

* Tue Jul 26 2011 Petr Pisar <ppisar@redhat.com> - 0.86-5
- RPM 4.9 dependency filtering added

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.86-4
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.86-3
- Perl mass rebuild

* Thu Jun 23 2011 Petr Pisar <ppisar@redhat.com> - 0.86-2
- Enable X11 tests
- Fix typo in requires filter
- Remove explicit requires that are found by new dependency generator
- Add new BuildRequires needed to run Padre in tests

* Wed Jun 22 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.86-1
- update to 0.86, clean spec

* Tue Mar 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.84-3
- padre.desktop as file instead of source

* Tue Mar 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.84-2
- 699569 add missing .desktop file

* Tue Mar 15 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.84-1
- update to 0.84
- remove clear section

* Wed Mar  2 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.82-1
- update to 0.82

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 31 2011 Petr Pisar <ppisar@redhat.com> - 0.80-1
- 0.80 spec
- Update dependencies and add Requires omitted by rpmbuild

* Mon Jan 17 2011 Petr Pisar <ppisar@redhat.com> - 0.78-1
- 0.78 bump
- (Build)Require POD2::Base (POD2 directory is used at run and test time.

* Thu Dec 09 2010 Petr Pisar <ppisar@redhat.com> - 0.76-1
- 0.76 bump

* Fri Nov 19 2010 Petr Pisar <ppisar@redhat.com> - 0.74-1
- 0.74 bump
- Fix templates file permission
- Mark translation files with %%lang macro
- Provide X11 server to run X11 tests (disable the tests for now as there is a
  bug preventing automation).

* Mon Oct 11 2010 Marcela Mašláňpvá <mmaslano@redhat.com> 0.72-2
- apply fix of spec from 633737

* Mon Oct 11 2010 Marcela Mašláňpvá <mmaslano@redhat.com> 0.72-1
- update and remove uncessary BR and R

* Tue Jun 22 2010 Petr Pisar <ppisar@redhat.com> - 0.64-1
- 0.64 bump
- Remove perl(File::Spec) >= 3.2701 requires because of version rounding

* Wed Jun  9 2010 Petr Pisar <ppisar@redhat.com> - 0.62-1
- 0.62 bump (bug #598539)
- Remove unversioned perl(Padre::Config) from provides
- Remove Win32::API patch

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.50-5
- Mass rebuild with perl-5.12.0

* Tue Feb  9 2010 Marcela Mašláňpvá <mmaslano@redhat.com> 0.50-4
- the patch will be needed because requires are automagically
  created and we really don't need win32::api

* Fri Feb  5 2010 Marcela Mašláňová <mmaslano@redhat.com> 0.50-3
- use DESTDIR instead of PERL_INSTALL_ROOT
- remove patch, DESTDIR fixed it all

* Thu Jan 14 2010 Marcela Mašláňová <mmaslano@redhat.com> 0.50-1
- update

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 31 2009 Marcela Mašláňová <mmaslano@redhat.com> 0.32-1
- 492937 perl-Wx-Perl-Dialog became part of Padre
- update to the latest version

* Wed Mar 04 2009 Marcela Mašláňová <mmaslano@redhat.com> 0.28-1
- Specfile autogenerated by cpanspec 1.78 again because Padre was
 rewritten and many requirement were changed.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 17 2008 Marcela Mašláňová <mmaslano@redhat.com> 0.20-1
- update to 0.20, switch off check of Wx, because unset DISPLAY
     in rpmbuild. V0.21 wasn't package because same problem
     somewhere else in code.

* Tue Nov 18 2008 Marcela Mašláňová <mmaslano@redhat.com> 0.16-1
- update to 0.16

* Mon Nov  3 2008 Marcela Mašláňová <mmaslano@redhat.com> 0.14-1
- update to 0.14
- add new requires
- remove patch for handling ORLite, with updated ORLite it's ok

* Fri Oct 10 2008 Marcela Mašláňová <mmaslano@redhat.com> 0.10-4
- move templates into _datadir

* Fri Oct 10 2008 Marcela Mašláňová <mmaslano@redhat.com> 0.10-3
- add desktop file

* Fri Oct 10 2008 Marcela Mašláňová <mmaslano@redhat.com> 0.10-2
- fix review
- example and test files should have permission 644
- desktop file is missing in upstream version

* Fri Oct 03 2008 Marcela Mašláňová <mmaslano@redhat.com> 0.10-1
- Specfile autogenerated by cpanspec 1.77.

