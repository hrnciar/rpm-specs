Name:           tw
Version:        0.9.16
Release:        19%{?dist}
Summary:        Translate words into different languages

License:        GPLv3+
URL:            http://code.google.com/p/translateword
Source0:        http://translateword.googlecode.com/files/%{name}-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  hunspell-devel
BuildRequires:  mythes-devel
BuildRequires:  lynx
BuildRequires:  aspell
BuildRequires:  espeak
Requires:       sed
Requires:       bash
Requires:       gawk
Requires:       coreutils
Requires:       %{_bindir}/xmllint
Requires:       curl
Requires:       util-linux
Requires:       lynx
Requires:       aspell
Requires:       espeak
Requires(post): info
Requires(preun): info

%description
translate word is a command that translates words into different
languages.  translate word uses internal dictionaries, and contacts
online to the Google Translation and the FreeTranslation engines.
It can also be integrated via the clipboard with a desktop environment.


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
%{_bindir}/mythes-raw
%{_bindir}/mythes
%{_datadir}/%{name}
%{_docdir}/%{name}
%{_infodir}/%{name}.info.*
%{_mandir}/man1/%{name}.1.*
%{_bindir}/%{name}-config-klipper
%{_bindir}/%{name}-config-gtw


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.9.16-10
- Rebuild for hunspell 1.5.x

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.16-7
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 07 2013 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.9.16-4
- Follow unversioned doc policy.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 1 2013 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.9.16-2
* Add espeak to BuildRequires.

* Sun Apr 28 2013 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.9.16-1
* Update to mainstream.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 02 2013 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.9.8-1
- Improve doc install.
- Fix changelog macros.

* Mon Dec 31 2012 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.9.6-1
- Use more generic man and info %%files.
- Remove obsolete "rm -rf $RPM_BUILD_ROOT".

* Thu Dec 13 2012 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.9.4-7
- Use GPLv3+.
- Omit deprecated stuff like BuildRoot, Group, clean and defattr.
- Omit Requires: glibc-common, implicitly pulled by pretty much everything already.
- Add tw-config-klipper to files.

* Mon Dec 10 2012 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.9.4-6
- Do not assume anything about Requires.

* Mon Dec 10 2012 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.9.4-5
- Fix BuildRequires to include lynx and aspell, remove xmllint Requires.

* Mon Dec 10 2012 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.9.4-4
- Fix release tag from 0.x to x.

* Mon Dec 10 2012 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.9.4-3
- Conform to rpmlint.

* Mon Dec 10 2012 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.9.4-2
- Reformat description from too long single line.
- In Requires tag, omit mythes, as per autodetected by RPM.
- In BuildRequires tag, omit coreutils, bash and sed. as per Guidelines#Exceptions.
- BuildRequires and Requires entries listed one-by-one for a better spec legibility.
- Fix Source* tag to the full URL for the compressed archive containing the (original) pristine source code.
- Fix license to GPLv3.
- Add Changelog.

* Mon Dec 10 2012 Juan Manuel Borges Caño <juanmabcmail@gmail.com> - 0.9.4-1
- Fedora review request (bug 885833).

