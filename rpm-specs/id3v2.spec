Name:           id3v2
Version:        0.1.12
Release:        21%{?dist}
Summary:        Command line ID3 tag editor

# See http://sourceforge.net/tracker/index.php?func=detail&aid=1768045&group_id=4193&atid=104193
License:        GPLv2+
URL:            http://id3v2.sourceforge.net/

# Source0:        http://downloads.sourceforge.net/id3v2/%{name}-%{version}.tar.gz
# Run "id3v2-fix-release-tarball.sh id3v2-0.1.12.tar.gz" to remove binaries
# and ".git/" from the tarball and get id3v2-0.1.12-fedora.tar.gz
# Source1:      %{name}-fix-release-tarball.sh
Source0:        %{name}-%{version}-fedora.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  id3lib-devel

%description
id3v2 is a command line tool to add, modify, remove, or view ID3v2
tags, as well as convert or list ID3v1 tags.  ID3 tags are commonly
embedded in compressed music files and are the standard way to more
fully describe the work than would normally be allowed by putting the
information in the filename.


%prep
%setup -q -n %{name}-%{version}-fedora


%build
CXXFLAGS="$RPM_OPT_FLAGS" make %{?_smp_mflags} PREFIX="%{_prefix}"


%install
install -Dpm 755 id3v2 $RPM_BUILD_ROOT%{_bindir}/id3v2
install -Dpm 644 id3v2.1 $RPM_BUILD_ROOT%{_mandir}/man1/id3v2.1


%files
%license COPYING
%doc README
%{_bindir}/id3v2
%{_mandir}/man1/id3v2.1*


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.1.12-12
- Spec-file cleanups

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.12-10
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.12-4
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 16 2010 Hans Ulrich Niedermann <hun@n-dimensional.de> - 0.1.12-1
- Updated to 0.1.12 (#595361).
- Added id3v2-fix-release-tarball.sh script to remove binaries from tarball.
- Removed id3v2-0.1.11-track-bad-free.patch (obsoleted by upstream 0.1.12).

* Sun Jan 10 2010 Hans Ulrich Niedermann <hun@n-dimensional.de> - 0.1.11-10
- Update Source0 URL (the old one has stopped working)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 22 2008 Ville Skyttä <ville.skytta at iki.fi> - 0.1.11-7
- Improve summary and description.

* Thu Jan  3 2008 Ville Skyttä <ville.skytta at iki.fi> - 0.1.11-6
- Apply sf.net patch #1252035 to fix --tracks crash (seen on PPC only).

* Thu Aug 16 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.1.11-5
- License: GPLv2+

* Wed Aug 30 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.1.11-4
- Rebuild.

* Sat Feb 18 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.1.11-3
- Rebuild.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.1.11-2
- rebuilt

* Wed Aug 25 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.1.11-0.fdr.1
- Update to 0.1.11 (bug 2013), license changed from GPL to LGPL.
- Improve description (borrowed from Debian).
- Spec file cleanups.

* Wed Oct 29 2003 Ville Skytta <ville.skytta at iki.fi> - 0:0.1.9-0.fdr.2
- Rebuild.

* Sun Apr 27 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.1.9-0.fdr.1
- First release.
