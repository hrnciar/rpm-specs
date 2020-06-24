Name:    sc
Version: 7.16
Release: 13%{?dist}
Summary: Spreadsheet Calculator

License: Public Domain
URL:     http://www.ibiblio.org/pub/Linux/apps/financial/spreadsheet/!INDEX.html
Source0: http://www.ibiblio.org/pub/Linux/apps/financial/spreadsheet/sc-%{version}.tar.gz

# These patches are from Debian, see:
# http://anonscm.debian.org/cgit/collab-maint/sc.git/tree/debian/patches?id=8d75b0ec9f761b5d5245290a79a20b409c442d52
Patch0:  Upstream-changes-from-old-versions.patch
Patch1:  function_definitions.patch
Patch2:  call_function_not_take_its_address.patch

# Patch for http://fedoraproject.org/wiki/Changes/FormatSecurity
Patch3:  format_security_fixes.patch

# https://www.mail-archive.com/debian-bugs-dist@lists.debian.org/msg1400274.html
Patch4:  nonotimeout-ncurses6.patch

BuildRequires: gcc
BuildRequires: bison
BuildRequires: ncurses-devel

%description
Spreadsheet Calculator is a free curses-based spreadsheet program that uses key
bindings similar to vi and less.

%prep
%autosetup

%build
make all sc.1 psc.1 %{?_smp_mflags} CFLAGS="%{optflags} -DSYSV3"

%install
# The "install" target of upstream's makefile does not work, so install manually

# Binaries
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 sc %{buildroot}%{_bindir}
install -m 0755 psc %{buildroot}%{_bindir}

# Man pages
install -d -m 0755 %{buildroot}%{_mandir}/man1
install -m 0644 sc.1 %{buildroot}%{_mandir}/man1
install -m 0644 psc.1 %{buildroot}%{_mandir}/man1

# Data
install -d -m 0755 %{buildroot}%{_datadir}/sc
install -m 0644 tutorial.sc %{buildroot}%{_datadir}/sc

%files
%doc CHANGES README SC.MACROS TODO
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/sc

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.16-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 Mat Booth <mat.booth@redhat.com> - 7.16-9
- Add BR on gcc

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Mat Booth <mat.booth@redhat.com> - 7.16-4
- Add patch from Debian to fix tight loop caused by ncurses 6 honouring
  "notimeout" setting, rhbz#1357902

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 05 2014 Mat Booth <mat.booth@redhat.com> - 7.16-1
- Initial version of sc package

