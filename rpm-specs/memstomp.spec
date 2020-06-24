%global	githash 38573e7d

Name:		memstomp
Version:	0.1.4
Release:	29%{?dist}
Summary:	Warns of memory argument overlaps to various functions
# The entire source code is LGPLV3+ with the exception of backtrace-symbols.c which
# is GPLv2+ by way of being a hacked up old version of binutils's addr2line.
# backtrace-symbols.c is built into an independent .so to avoid license contamination
License:	LGPLv3+ and GPLv2+
URL:		git://fedorapeople.org/home/fedora/wcohen/public_git/memstomp
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
# git glone git://fedorapeople.org/home/fedora/wcohen/public_git/memstomp
# cd memstomp
# git archive --prefix memstomp-0.1.4-38573e7d/ master | gzip > memstomp-0.1.4-3867e37d.tar.gz
Source0:	%{name}-%{version}-%{githash}.tar.gz
Requires:	util-linux
BuildRequires:  gcc
BuildRequires:	binutils-devel autoconf automake dejagnu

Patch0: memstomp-testsuite.patch
Patch1: memstomp-man.patch
Patch2: memstomp-rh961495.patch
Patch3: memstomp-rh962763.patch
Patch4: memstomp-quietmode.patch
Patch5: memstomp-rh1093173.patch
Patch6: memstomp-rh1133815.patch
Patch7: memstomp-implicit-int.patch
Patch8: bfd-api-change.patch


%description 
memstomp is a simple program that can be used to identify
places in code which trigger undefined behavior due to
overlapping memory arguments to certain library calls.

%ldconfig_scriptlets

%prep
%setup -q -n %{name}-%{version}-%{githash}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1


%build
autoreconf
%configure
# We force -O0 here because memstomp essentially relies on GCC
# not removing any of its checks.  GCC continues to get better
# and twarting its optimizer isn't something I have any interest
# in maintaining over time.  So just force -O0 for stupid code
# generation.
make %{?_smp_mflags} CFLAGS+="-O0 -fno-strict-aliasing"
make -k check

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc README LGPL3 GPL2 GPL3
%{_bindir}/memstomp
%{_libdir}/libmemstomp.so
%{_libdir}/libmemstomp-backtrace-symbols.so
%{_mandir}/man1/memstomp.1.gz

%changelog
* Mon May 18 2020 Jeff Law <law@redhat.com> - 0.1.4-29
- Various fixes for API changes in bfd

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 9 2016 Jeff Law <law@redhat.com> - 0.1.4-20
- Remove xfail for aarch64 in testsuite (#1334124)

* Wed Feb 17 2016 Jeff Law <law@redhat.com> - 0.1.4-19
- Build with -O0 to avoid GCC optimizing away checks we want to keep.
  (#1307767)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 26 2015 Jeff Law <law@redhat.com> 0.1.4-16
- Fixup implicit return types in testsuite.

* Tue Aug 26 2014 Jeff Law <law@redhat.com> 0.1.4-15
- Adjust PC values in saved frame addresses to get line number
  associations correct (#1133815).

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jun 4 2014 Jeff Law <law@redhat.com> 0.1.4-12
- Fix cut-n-paste bug in memmem

* Thu May 29 2014 Jeff Law <law@redhat.com> 0.1.4-11
- Add checking of various str* and mem* for NULL arguments (#1093173)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 30 2013 Jeff Law <law@redhat.com> 0.1.4-9
- Add -q/--quiet options for quiet mode.

* Tue May 14 2013 Jeff Law <law@redhat.com> 0.1.4-8
- Link in libiberty too (#962763)

* Fri May 10 2013 Jeff Law <law@redhat.com> 0.1.4-7
- Improve man page (#961518)

* Thu May 09 2013 Jeff Law <law@redhat.com> 0.1.4-5
- Fix typo in initialization message (#961495)

* Fri Mar 15 2013 Jeff Law <law@redhat.com> 0.1.4-4
- Build tests with -fno-builtin

* Mon Mar 11 2013 Jeff Law <law@redhat.com> 0.1.4-4
- Add manpage
- Add initial testsuite

* Fri Feb 22 2013 Jeff Law <law@redhat.com> 0.1.4-3
- Change %%define to %%global for git hash
- Remove git hash from version # in changelog
- Build with -fno-strict-aliasing
- Fix minor spelling error in description

* Tue Feb 5 2013 Jeff Law <law@redhat.com> 0.1.4-2
- Remove commands/directives automatically handled by rpm
- Add comment on how to build the tarball
- Change Requires to reference package rather than file
- Add comments on licensing issues
- Add autoconf and automake to BuildRequires

* Tue Feb 5 2013 Jeff Law <law@redhat.com> 0.1.4-1
- Initial release
