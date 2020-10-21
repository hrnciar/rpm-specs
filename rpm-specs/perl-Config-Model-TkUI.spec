%global use_x11_tests 1

Name:           perl-Config-Model-TkUI
Version:        1.371
Release:        4%{?dist}
Summary:        TK GUI to edit config data through Config::Model
License:        LGPLv2+
URL:            https://metacpan.org/release/Config-Model-TkUI
Source0:        https://cpan.metacpan.org/authors/id/D/DD/DDUMONT/Config-Model-TkUI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config::Model) >= 2.134
BuildRequires:  perl(Config::Model::ObjTreeScanner)
BuildRequires:  perl(Config::Model::Tester) >= 3.006
BuildRequires:  perl(Config::Model::Tester::Setup)
BuildRequires:  perl(Config::Model::Value)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Log::Log4perl) >= 1.11
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Pod::POM)
BuildRequires:  perl(Pod::POM::View::Text)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Warn) >= 0.11
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(Tk)
BuildRequires:  perl(Tk::Adjuster)
BuildRequires:  perl(Tk::Balloon)
BuildRequires:  perl(Tk::BrowseEntry)
BuildRequires:  perl(Tk::Dialog)
BuildRequires:  perl(Tk::DialogBox)
BuildRequires:  perl(Tk::DirSelect)
BuildRequires:  perl(Tk::DoubleClick)
BuildRequires:  perl(Tk::FontDialog)
BuildRequires:  perl(Tk::Frame)
BuildRequires:  perl(Tk::Menubutton)
BuildRequires:  perl(Tk::NoteBook)
BuildRequires:  perl(Tk::ObjScanner)
BuildRequires:  perl(Tk::Pane)
BuildRequires:  perl(Tk::Photo)
BuildRequires:  perl(Tk::PNG)
BuildRequires:  perl(Tk::Pod)
BuildRequires:  perl(Tk::Pod::Text)
BuildRequires:  perl(Tk::ROText)
BuildRequires:  perl(Tk::Toplevel)
BuildRequires:  perl(Tk::Tree)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(YAML)
%if %{use_x11_tests}
# X11 tests:
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xorg-x11-xinit
BuildRequires:  font(:lang=en)
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This class provides a GUI for Config::Model.

%prep
%setup -q -n Config-Model-TkUI-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%if %{use_x11_tests}
    xvfb-run -a ./Build test
%endif

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.371-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.371-3
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.371-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 15 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 1.371-1
- Update to 1.371

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.370-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.370-2
- Perl 5.30 rebuild

* Mon May 27 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.370-1
- 1.370 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.369-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.369-1
- 1.369 bump

* Fri Oct 26 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.368-1
- 1.368 bump

* Tue Sep 04 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.367-1
- 1.367 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.366-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.366-2
- Perl 5.28 rebuild

* Thu May 10 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.366-1
- 1.366 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.365-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 21 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.365-1
- 1.365 bump

* Sun Aug 27 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.364-1
- Update to 1.364

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.363-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.363-1
- 1.363 bump

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.362-2
- Perl 5.26 rebuild

* Sun May 14 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.362-1
- Update to 1.362

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.361-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.361-1
- 1.361 bump

* Tue Jan 17 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.360-1
- 1.360 bump

* Thu Jan 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.359-1
- 1.359 bump

* Thu Sep 29 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.357-1
- 1.357 bump

* Tue Jun 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.356-1
- 1.356 bump

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.354-2
- Perl 5.24 rebuild

* Mon Apr 04 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.354-1
- 1.354 bump

* Tue Mar 01 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.352-1
- 1.352 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.350-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.350-1
- 1.350 bump

* Fri Oct 23 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.349-1
- 1.349 bump

* Wed Jun 24 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.347-1
- 1.347 bump
- Specified all BRs

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.322-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.322-12
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.322-11
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.322-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 1.322-9
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.322-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.322-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.322-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 30 2012 Petr Pisar <ppisar@redhat.com> - 1.322-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.322-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.322-3
- Perl mass rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.322-2
- Perl mass rebuild

* Wed Mar 9 2011 David Hannequin david.hannequin@gmail.com 1.322-1
- Update upstream.
- Add build require File::Slurp.
- Add build require Test::Warn.
- Add build require Config::Model.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.306-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.306-5
- 661697 rebuild for fixing problems with vendorach/lib

* Wed Jun 23 2010 David Hannequin david.hannequin@gmail.com 1.306-4
- Fix wrong number of version.

* Wed Jun 23 2010 David Hannequin david.hannequin@gmail.com 1.306-3
- Fix tag.

* Wed Jun 23 2010 David Hannequin david.hannequin@gmail.com 1.306-2
- Fix tag.

* Sat Jun 19 2010 David Hannequin david.hannequin@gmail.com 1.306-1
- Fix wrong license.
- Update upstream 

* Wed Oct 28 2009 David Hannequin david.hannequin@gmail.com 1.211-2
- Add build require Test::More. 

* Sun Aug 02 2009 David Hannequin david.hannequin@gmail.com 1.211-1
- First release. 
