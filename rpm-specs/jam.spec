Name:		jam
Version:	2.5
Release:	27%{?dist}
License:	Copyright only
Summary:	Program construction tool, similar to make
URL:		http://public.perforce.com/public/jam/index.html
Source0:	ftp://ftp.perforce.com/jam/%{name}-%{version}.zip
# Submitted upstream by e-mail
Patch0:         jam-2.5-overflow.patch
BuildRequires:  gcc
BuildRequires:	byacc

%description
Jam is a program construction tool, like make. Jam recursively builds target 
files from source files, using dependency information and updating actions 
expressed in the Jambase file, which is written in jam's own interpreted 
language. The default Jambase is compiled into jam and provides a boilerplate 
for common use, relying on a user-provide file "Jamfile" to enumerate actual 
targets and sources. 

%prep
%setup -q -c
%patch0 -p1 -b .overflows

%build
make CFLAGS="$RPM_OPT_FLAGS" CCFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m0755 bin.linux*/jam $RPM_BUILD_ROOT/%{_bindir}
install -m0755 bin.linux*/mkjambase $RPM_BUILD_ROOT/%{_bindir}

%files
%doc README RELNOTES *.html
%{_bindir}/jam
%{_bindir}/mkjambase

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 11 2009 Ville Skyttä <ville.skytta@iki.fi> - 2.5-10
- Use upstream zip instead of uncompressed tarball.

* Mon Aug  3 2009 Lubomir Rintel <lkundrak@v3.sk> - 2.5-9
- Add the stack overflow fix patch

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.5-6
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Tom "spot" Callaway <tcallawa@redhat.com> 2.5-5
- fix license tag
- rebuild for BuildID in devel

* Mon Sep 11 2006 Tom "spot" Callaway <tcallawa@redhat.com> 2.5-4
- fix minimal BR from bison to byacc
- rebuild for FC-6

* Tue Feb 28 2006 Tom "spot" Callaway <tcallawa@redhat.com> 2.5-3
- bump for FC5

* Fri Sep  9 2005 Tom "spot" Callaway <tcallawa@redhat.com> 2.5-2
- use smp_mflags
- use name and version in source field

* Fri Aug 19 2005 Tom "spot" Callaway <tcallawa@redhat.com> 2.5-1
- initial package for Fedora Extras
