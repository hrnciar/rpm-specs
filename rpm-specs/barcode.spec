Summary: generates barcodes from text strings
Name: barcode
Version: 0.98
Release: 38%{?dist}
License: GPLv2+
Source0: ftp://ftp.gnu.org/gnu/barcode/barcode-0.98.tar.gz
Patch0: barcode-configure.patch
Patch1: barcode-install-info.patch
Patch2: barcode-0.98-format-security.patch
URL: http://www.gnu.org/software/barcode/
BuildRequires: gcc
BuildRequires: %{_bindir}/texindex, %{_bindir}/dvips
BuildRequires: %{_bindir}/makeinfo, ghostscript

# https://fedoraproject.org/wiki/Changes/RemoveObsoleteScriptlets
%if !((0%{?fedora} >= 28) || (0%{?rhel} >= 8))
%{error:No install-info scriptlets for Fedora prior to F28 or EL prior to EL8.}
%endif

%description
Barcode is meant to solve most needs in barcode creation with a
conventional printer. It can create printouts for the conventional
product tagging standards: UPC-A, UPC-E, EAN-13, EAN-8, ISBN, as well
as a few other formats. Ouput is generated as either Postscript or
Encapsulated Postscript.

%package devel
Summary:        Header files and libraries for %{name} development
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}

%description devel
The %{name}-devel package contains the header files and libraries needed
to develop programs that use the %{name} library.

%prep
%setup -q
%patch0 -p1 -b .directories
%patch1 -p1 -b .categories
%patch2 -p1 -b .format-security

%build
# fix definition of INFOTOHTML
export MAKEINFO=makeinfo
%configure
# rebuild all documentation
make -C doc clean
make

%install
rm -rf %{buildroot}
%makeinstall

%files
%doc COPYING ChangeLog README TODO doc/barcode.html
%{_bindir}/barcode
%{_mandir}/man1/barcode.1.gz
%{_infodir}/barcode.info.*

%files devel
%{_includedir}/*.h
%{_libdir}/*.a
%{_mandir}/man3/barcode.3.gz

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 0.98-36
- Remove hardcoded gzip suffix from GNU info pages

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 06 2017 Robert Scheck <robert@fedoraproject.org> - 0.98-32
- Added patch to fix -Werror=format-security related build failure

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Hans Ulrich Niedermann <hun@n-dimensional.de> - 0.98-28
- remove useless %%defattr for clarity

* Wed Feb 24 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 0.98-27
- Fix F24FTBFS caused by docs shipped in tarball (#1307342)
- Fix build of HTML documenation

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 31 2014 Robert Scheck <robert@fedoraproject.org> - 0.98-23
- Require texindex, dvips and makeinfo executables directly as they
  are provided by different packages on Fedora and (older) RHEL

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb  9 2011 Hans Ulrich Niedermann <hun@n-dimensional.de> - 0.98-17
- Have explicit requires use %%{?_isa} (new Guidelines)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug  1 2010 Hans Ulrich Niedermann <hun@n-dimensional.de> - 0.98-15
- Add virtual "Provides: -static" to -devel subpackage (#609598)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jul 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9.8-12
- fix license tag

* Mon Feb 11 2008 Andreas Thienemann <andreas@bawue.net> - 0.9.8-11
- Rebuild against gcc-4.3

* Fri Sep 08 2006 Andreas Thienemann <andreas@bawue.net> - 0.9.8-10
- FE6 Rebuild

* Mon Mar 27 2006 Andreas Thienemann <andreas@bawue.net> 0.9.8-9
- Changed texinfo dependency to texinfo-tex to satisfy #186825

* Sun Feb 05 2006 Andreas Thienemann <andreas@bawue.net> 0.98-8
- Enabled --excludedocs install

* Fri Jul 15 2005 Andreas Thienemann <andreas@bawue.net> 0.98-7
- Switched off threaded make, as it's causing problems when rebuilding
  the documentation

* Thu Jul 07 2005 Andreas Thienemann <andreas@bawue.net> 0.98-6
- Added configure patch to pick up correct libdir for x86_64
- Added missing BuildRequires for ghostscript and tetex-dvips

* Thu Jul 07 2005 Andreas Thienemann <andreas@bawue.net> 0.98-5
- Added install-info support to the texinfo file.
- Fixed minor spec errors

* Fri Jul 01 2005 Andreas Thienemann <andreas@bawue.net> 0.98-4
- Added info-install in post and pre stage.

* Fri Jul 01 2005 Andreas Thienemann <andreas@bawue.net> 0.98-3
- Added %%{epoch} tag to the -devel requires.

* Thu Jun 30 2005 Andreas Thienemann <andreas@bawue.net> 0.98-2
- spec cleanup.

* Wed Jun 29 2005 Andreas Thienemann <andreas@bawue.net> 0.98-1
- Initial RPM release.

