Name:           e2tools
Version:        0.1.0
Release:        1%{?dist}
Summary:        Manipulate files in unmounted ext2/ext3 filesystems

# No version specified.
License:        GPL+
URL:            https://e2tools.github.io/
Source0:        https://github.com/e2tools/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  e2fsprogs-devel >= 1.27
BuildRequires:  libcom_err-devel

BuildRequires:  e2fsprogs


%description
A simple set of utilities to read, write, and manipulate files in an
ext2/ext3 filesystem directly using the ext2fs library. This works

  - without root access
  - without the filesystem being mounted
  - without kernel ext2/ext3 support

The utilities are: e2cp e2ln e2ls e2mkdir e2mv e2rm e2tail


%prep
%autosetup -v


%build
%configure
%{__make} %{?_smp_mflags}


%check
%{__make} %{?_smp_flags} check


%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT


%files
%doc AUTHORS
%doc COPYING
%doc ChangeLog
%doc NEWS.md
%doc README.md
%doc TODO

%{_bindir}/e2tools
%doc %{_mandir}/man7/e2tools.7.gz

%{_bindir}/e2cp
%doc %{_mandir}/man1/e2cp.1.gz

%{_bindir}/e2ln
%doc %{_mandir}/man1/e2ln.1.gz

%{_bindir}/e2ls
%doc %{_mandir}/man1/e2ls.1.gz

%{_bindir}/e2mkdir
%doc %{_mandir}/man1/e2mkdir.1.gz

%{_bindir}/e2mv
%doc %{_mandir}/man1/e2mv.1.gz

%{_bindir}/e2rm
%doc %{_mandir}/man1/e2rm.1.gz

%{_bindir}/e2tail
%doc %{_mandir}/man1/e2tail.1.gz


%changelog
* Fri Feb  7 2020 Hans Ulrich Niedermann <hun@n-dimensional.de> - 0.1.0-1
- Update to new upstream's e2tools-0.1.0 release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.16.4-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.16.4-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb  1 2019 Hans Ulrich Niedermann <hun@n-dimensional.de> - 0.0.16.4-33
- Fix F30 build by working around the strncpy truncate warning

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.16.4-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan  8 2019 Hans Ulrich Niedermann <hun@n-dimensional.de> - 0.0.16.4-31
- Update to e2tools-0.0.16.4

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.16-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.16-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.16-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.16-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.16-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Hans Ulrich Niedermann <hun@n-dimensional.de> - 0.0.16-26
- remove useless %%defattr for clarity

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.16-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb  9 2011 Hans Ulrich Niedermann <hun@n-dimensional.de> - 0.0.16-17
- Remove unused code parts triggering new gcc warning in f15

* Wed Feb  9 2011 Hans Ulrich Niedermann <hun@n-dimensional.de> - 0.0.16-16
- Fix CVS keyword substitution breaking our patch file

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 18 2009 Hans Ulrich Niedermann <hun@n-dimensional.de> - 0.0.16-13
- Add libcom_err-devel buildreq on F12 and later (e2fsprogs-devel split)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 17 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.0.16-11
- fix license tag

* Mon Feb 11 2008 Andreas Thienemann <andreas@bawue.net> - 0.0.16-10
- Rebuild against gcc-4.3

* Sun Dec  9 2007 Hans Ulrich Niedermann <hun@n-dimensional.de> - 0.0.16-9
- Use format string macro from inttypes.h and uint64_t (#349851).

* Sat Dec  8 2007 Hans Ulrich Niedermann <hun@n-dimensional.de> - 0.0.16-8
- Special __u64 formatstring on 64bit platforms (#349851).
- Reintroduce -Werror for all platforms.
- Install man pages without x bit.

* Sat Dec  8 2007 Hans Ulrich Niedermann <hun@n-dimensional.de> - 0.0.16-6
- Cowardly avoid compiling with -Werror on alpha.
- Install files preserving timestamps where possible.
- Use RPM macros for shell commands where possible.

* Mon Jul 31 2006 Andreas Thienemann <andreas@bawue.net> - 0.0.16-5
- fix broken cast in rm.c:248 (exhibited on x86_64, but buggy everywhere) from Hans Ulrich Niedermann

* Mon Jul 17 2006 Andreas Thienemann <andreas@bawue.net> - 0.0.16-4
- Introduced %%check

* Mon Jul 17 2006 Hans Ulrich Niedermann <hun@n-dimensional.de> - 0.0.16-3
- initial package for fedora extras

