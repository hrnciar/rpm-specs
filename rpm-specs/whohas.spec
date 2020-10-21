Name:           whohas
Version:        0.29.1
Release:        13%{?dist}
Summary:        Command line tool for query package lists

License:        GPLv2+
URL:            http://www.philippwesche.org/200811/whohas/intro.html
Source0:        https://github.com/whohas/whohas/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl(strict)
BuildRequires:  perl(sigtrap)
BuildRequires:  perl(Config)
BuildRequires:  perl(Env)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Sys::CPU)
BuildRequires:  perl(Thread::Queue)
Requires:       perl(forks)
Requires:       perl(threads)

# Optional
Requires:       perl(Sys::CPU)

%description
whohas is a command line tool that allows querying several package
lists at once - currently supported are Arch, Debian, Gentoo and
Slackware. whohas is written in Perl and was designed to help
package maintainers find ebuilds, pkgbuilds and similar package
definitions from other distributions to learn from.

%prep
%setup -q
# Convert to utf-8
for file in usr/share/man/de/man1/whohas.1; do
    mv $file timestamp
    iconv -f ISO-8859-1 -t UTF-8 -o $file timestamp
    touch -r timestamp $file
done

%build
#nothing to build

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} INSTALL="install -p"
rm -rf %{buildroot}%{_defaultdocdir}/whohas/examples/whohas.cf

%files
%{_pkgdocdir}
%license LICENSE
%{_mandir}/man*/%{name}.*
%{_mandir}/de/man*/%{name}.*
%{_bindir}/%{name}

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Fabian Affolter <mail@fabian-affolter.ch> - 0.29.1-5
- Fix requirements (rhbz#1412449)

* Sun Feb 14 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.29.1-4
- Let package install docs (Fix FTBFS, RHBZ#1308239).
- Rework perl deps to match with perl packaging conventions.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 19 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.29.1-1
- Update to new upstream version 0.29.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.29-6
- Perl 5.18 rebuild

* Fri Mar 29 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.24-5
- Spec file updated

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 28 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.29-1
- Updated to new upstream version 0.29

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.24-2
- Rebuild

* Thu Apr 08 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.24-1
- Updated to new upstream version 0.24

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 05 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.23-1
- Updated to new upstream version 0.23

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 30 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.22-2
- License is GPLv2+ not GPLv2
- Fixed requirements

* Fri Jan 30 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.22-1
- Initial package for Fedora
