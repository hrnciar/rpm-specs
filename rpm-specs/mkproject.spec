Name:           mkproject
Version:        0.4.6
Release:        17%{?dist}
Summary:        Make project skeletons

License:        GPLv3+
URL:            http://code.google.com/p/makeproject
Source0:        http://makeproject.googlecode.com/files/%{name}-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  autoconf
Requires:       sed
Requires:       bash
Requires:       coreutils
Requires:       util-linux
Requires:       autoconf

%description
Make Project is a command that makes project skeletons. Make Project
automatizes the task of starting a new project with the information
provided from the command line. The package created by default is a
'hello world' project of the selected skeleton that is managed with
auto tools. There are skeletons for bash, c, c library, python, c++, c++
library and Perl.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
export AM_UPDATE_INFO_DIR=no
make install DESTDIR=$RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_docdir}/%{name}
%{_infodir}/%{name}.info.*
%{_mandir}/man1/%{name}.1.*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 07 2013 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.4.6-6
- Follow unversioned doc policy.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 07 2013 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.4.6-3
- autoconf, buildrequire.

* Wed Jan 02 2013 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.4.6-2
- Improve doc install.
- Fix changelog macros.

* Mon Dec 31 2012 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.4.6-1
- Use more generic man and info files.
- Remove obsolete "rm -rf $RPM_BUILD_ROOT".
- Fedora review request (bug 890733).

* Thu Dec 13 2012 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.4.4-1
- Use GPLv3+.
- Omit deprecated stuff like BuildRoot, Group, clean and defattr.
- Omit Requires: glibc-common, implicitly pulled by pretty much everything already.
- Conform to rpmlint.
- Reformat description from too long single line.
- BuildRequires and Requires entries listed one-by-one for a better spec legibility.
- Fix Source* tag to the full URL for the compressed archive containing the (original) pristine source code.
- Fix license to GPLv3.
- Add Changelog.
- Fedora review request (bug pending).

