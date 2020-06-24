%global  basever 0.8.16

Name:           emerald-themes
License:        GPLv2
Version:        0.8.16
Release:        3%{?dist}
Epoch:          1
Summary:        Themes for Emerald, a window decorator for Compiz Fusion
URL:            https://gitlab.com/compiz/%{name}
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildArch:      noarch

Requires:       compiz >= %{basever}
Requires:       emerald >= %{basever}
BuildRequires:  libtool
BuildRequires:  automake

Obsoletes:      emerald-themes-extra


%description
Emerald is themeable window decorator and compositing
manager for Compiz Fusion.

This package contains themes for emerald.


%prep
%setup -q -n %{name}-v%{version}

%build
./autogen.sh
%configure

make %{?_smp_mflags} V=1

%install
%{make_install}


%files
%doc COPYING NEWS
%{_datadir}/emerald/themes/


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr  2 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 1:0.8.16-1
- New version
  Related: rhbz#1656467
- New URL

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 18 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1:0.8.14-1
- test 0.8.14 release
- Add a Yosemite theme.
- Add a graphite version of the Yosemite theme.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri May 27 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.12.1-1
- update to 0.8.12.1 release

* Sat Feb 13 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.12-1
- update to 0.8.12 release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.5.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 18 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.5.2-12
- rebuild for f22

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> -  1:0.5.2-8
- own directory
- use new upstream package for rpm
- generate configure
- drop unnecessary command to remove import.sh
- remove files with 'bak' instead of '~'
- drop unnecessary 'chmod' command

* Mon Oct 15 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> -  1:0.5.2-7
- build for fedora
- review package
- remove %%defattr(-,root,root,-)
- remove BuildRoot
- add basever
- add Epoch tag

