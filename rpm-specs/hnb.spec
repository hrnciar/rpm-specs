Summary: Hierarchical Notebook
Name: hnb
Version: 1.9.19
Release: 15%{?dist}
License: GPLv2+
URL: https://github.com/liskin/lhnb
Source0: https://nomi.cz/download/releases/lhnb/lhnb-%{version}.tar.gz
Source1: hnbrc.vi
Patch0: %{name}-rpm.patch
# fix build with gcc10
Patch1: hnb-gcc10.patch
# fix -Werror=format-security errors
Patch3: hnb-format-security.patch
BuildRequires: gcc
BuildRequires: ncurses-devel

%description
Hierarchical notebook(hnb) is a curses program to structure many kinds
of data in one place, for example addresses, to-do lists, ideas, book
reviews or to store snippets of brainstorming. Writing structured
documents and speech outlines.

The default format is XML but hnb can also export to ASCII and HTML.
External programs may be used for more advanced conversions of the XML
data.

%prep
%setup -q -n lhnb-%{version}
%patch0 -p1 -b .r
%patch1 -p1 -b .gcc10
%patch3 -p1 -b .format-security
cp -p %{SOURCE1} doc/

%build
%{__make} OPTFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
install -D -p src/hnb $RPM_BUILD_ROOT%{_bindir}/hnb
install -D -pm644 doc/hnb.1 $RPM_BUILD_ROOT%{_mandir}/man1/hnb.1

%files
%license COPYING
%doc README doc/Documentation.html doc/hnbrc*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Feb 21 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.9.19-15
- fix build with gcc10

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.19-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.19-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.19-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Dominik Mierzejewski <rpm@greysector.net> - 1.9.19-11
- Add BR: gcc for https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot
- Use HTTPS for Source0 URL
- Use license macro

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 27 2014 Dominik Mierzejewski <rpm@greysector.net> 1.9.19-1
- update to a 1.9.19 fork from http://nomi.cz/download/releases/lhnb/
- drop obsolete patches
- drop obsolete specfile parts
- fix -Werror=format-security errors (bug #1037122)
- fix bogus date in changelog

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.18-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.9.18-5
- Autorebuild for GCC 4.3

* Sat Aug 25 2007 Dominik Mierzejewski <rpm@greysector.net> 1.9.18-4
- apparently .pre7 tarball contains newer code
- integrate Debian patch
- update license tag

* Tue Aug 29 2006 Dominik Mierzejewski <rpm@greysector.net> 1.9.18-3
- mass rebuild

* Fri Aug 18 2006 Dominik Mierzejewski <rpm@greysector.net> 1.9.18-2
- added dist tag

* Fri Aug 18 2006 Dominik Mierzejewski <rpm@greysector.net> 1.9.18-1
- FE compliance
- fixed compilation with gcc4

* Wed Sep 22 2004 Dominik Mierzejewski <rpm@greysector.net>
- initial build
- patch to build using RPM_OPT_FLAGS
- fix some warnings
