Name:		kpcli	
Version:	3.5
Release:	1%{?dist}
Summary:	KeePass Command Line Interface (CLI) / interactive shell
License:	GPL+ or Artistic
BuildArch:	noarch
URL:		http://kpcli.sourceforge.net/	
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}.pl
Source1:	http://downloads.sourceforge.net/project/%{name}/README
BuildRequires:	perl-generators
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:	perl(Term::ReadLine)
Requires:	perl(Term::ReadLine::Gnu)
Requires:	perl(Capture::Tiny)
Requires:	perl(Digest::MD5)
Requires:	perl(XML::Parser)
Requires:	perl(Crypt::PWSafe3)

%description
KeePass Command Line Interface (CLI) / interactive shell. 
Use this program to access and manage your KeePass 1.x or
2.x databases from a Unix-like command line.

%prep
cp -p %{SOURCE0} %{_builddir}/
cp -p %{SOURCE1} %{_builddir}/


%build
# Nothing to build.

%install
mkdir -p %{buildroot}%{_bindir}/
install -p -m0755 %{name}-%{version}.pl %{buildroot}%{_bindir}/%{name}

%files
%doc README
%{_bindir}/kpcli

%changelog
* Sat Sep 19 2020 Charles R. Anderson <cra@wpi.edu> - 3.5-1
- Updated to 3.5

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.4-3
- Perl 5.32 re-rebuild of bootstrapped packages

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.4-2
- Perl 5.32 rebuild

* Wed May 13 2020 Charles R. Anderson <cra@wpi.edu> - 3.4-1
- Updated to 3.4

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 16 2019 Charles R. Anderson <cra@wpi.edu> - 3.3-1
- Updated to 3.3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.2-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.2-2
- Perl 5.28 rebuild

* Sun Feb 18 2018 Charles R. Anderson <cra@wpi.edu> - 3.2-1
- Updated to 3.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.1-2
- Perl 5.26 rebuild

* Mon Mar 27 2017 Matias Kreder <delete@fedoraproject.org> 3.1-1
- Updated to 3.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.0-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Charles R. Anderson <cra@wpi.edu> - 3.0-1
- Updated to 3.0.  Adds support for importing PasswordSafe v3 files.
- preserve timestamp on prep/install
- Add README file

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.8-4
- Perl 5.22 rebuild

* Wed Jun 10 2015 Matias Kreder <mkreder@gmail.com> - 2.8-3
- Removing perl(Clipboard) as perl(Clipboard) will be probably retired 

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.8-2
- Perl 5.22 rebuild

* Sat May 09 2015 Charles R. Anderson <cra@wpi.edu> - 2.8-1
- Updated to 2.8

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.7-3
- Perl 5.20 rebuild

* Fri Aug 01 2014 Matias Kreder <delete@fedoraproject.org> 2.7-2
- Added perl-XML-Parser

* Mon Jul 14 2014 Matias Kreder <delete@fedoraproject.org> 2.7-1
- Updated to 2.7

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 10 2014 Matias Kreder <delete@fedoraproject.org> 2.4-2
- Added perl perl(Capture::Tiny) and perl(Clipboard)

* Sun Mar 02 2014 Matias Kreder <delete@fedoraproject.org> 2.4-1
- Updated to 2.4

* Mon Sep 02 2013 Matias Kreder <delete@fedoraproject.org> 2.3-3
- Updated license information

* Thu Aug 29 2013 Matias Kreder <delete@fedoraproject.org> 2.3-2
- Updated .spec file according to BZ# 1002324

* Wed Aug 28 2013 Matias Kreder <delete@fedoraproject.org> 2.3-1
- Initial build.
