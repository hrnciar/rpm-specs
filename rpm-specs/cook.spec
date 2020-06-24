Name:		cook
Version:	2.34
Release:	22%{?dist}

Summary: 	File construction tool

License:	GPLv2+
URL:		http://miller.emu.id.au/pmiller/software/cook
Source:		http://miller.emu.id.au/pmiller/software/cook/cook-%{version}.tar.gz
# Fix including roff files, bug #1307402
Patch0:     cook-2.34-Fix-including-roff-files.patch
BuildRequires:  gcc
BuildRequires:	groff
BuildRequires:  bison
BuildRequires:  gettext
BuildRequires:  perl-generators
BuildRequires:  sharutils
BuildRequires:  ghostscript
BuildRequires:  m4
Provides:	perl(host_lists.pl)

%description
Cook is a tool for constructing files. It is given a set of files to
create, and recipes of how to create them. In any non-trivial program
there will be prerequisites to performing the actions necessary to
creating any file, such as include files.  The cook program provides a
mechanism to define these.


%prep
%setup -q
%patch0 -p1


%build
%configure --libdir=%{_datadir}
# _smp_mflags breaks the build
make # %{?_smp_mflags}
groff -Tps -s -p -t -mm -I../../etc lib/en/tutorial/main.mm > tutorial.ps
groff -Tps -s -p -t -mm -I../../etc lib/en/user-guide/main.mm > user-guide.ps
groff -Tps -s -p -t -mm -I../../etc lib/en/refman/main.man > refman.ps
for f in *.ps; do
    ps2pdf $f
done


%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_datadir}/cook/en/man1
mkdir -p $RPM_BUILD_ROOT%{_datadir}/cook/en/LC_MESSAGES
make DESTDIR=$RPM_BUILD_ROOT install
rm -fr $RPM_BUILD_ROOT%{_datadir}/cook/en/man1
rm -fr $RPM_BUILD_ROOT%{_datadir}/cook/en/refman.*
rm -fr $RPM_BUILD_ROOT%{_datadir}/cook/en/tutorial.*
rm -fr $RPM_BUILD_ROOT%{_datadir}/cook/en/user-guide.*


%check
make sure



%files
%{_bindir}/*
%{_datadir}/cook
%{_mandir}/man1/*
%doc *.pdf
%doc README


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.34-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.34-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.34-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.34-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.34-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 02 2017 Petr Pisar <ppisar@redhat.com> - 2.34-17
- Reenable documentation in PDF (bug #1470700)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.34-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.34-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 2.34-14
- Do not use broken grog for generating documentation (bug #1307402)
- Fix including roff files (bug #1307402)
- Do not convert documentation to PDF because it fails on s390x (bug #1470700)

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 2.34-13
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.34-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.34-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.34-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.34-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.34-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.34-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.34-6
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.34-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 21 2011 Gérard Milmeister <gemi@bluewin.ch> - 2.34-2
- Documentation is built and included

* Tue Feb  8 2011 Gérard Milmeister <gemi@bluewin.ch> - 2.34-1
- new release 2.34

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Aug  4 2008 Gerard Milmeister <gemi@bluewin.ch> - 2.32-1
- new release 2.32

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.30-2
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Gerard Milmeister <gemi@bluewin.ch> - 2.30-1
- new release 2.30
- change license to GPLv2+

* Wed Jun  6 2007 Gerard Milmeister <gemi@bluewin.ch> - 2.28-1
- new version 2.28

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.26-3
- Rebuild for FE6

* Fri Feb 17 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.26-2
- Rebuild for Fedora Extras 5

* Tue Jan 17 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.26-1
- new version 2.26

* Wed May 25 2005 Jeremy Katz <katzj@redhat.com> - 2.25-4
- fix build with gcc4 (mschwendt, #156203)

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 2.25-3
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sat Feb 12 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:2.25-1
- New Version 2.25

* Tue Oct 28 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:2.24-0.fdr.3
- added check

* Mon Oct 27 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:2.24-0.fdr.2
- Improved specfile

* Sat Oct 18 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:2.24-0.fdr.1
- First Fedora release
