Name:           cvsgraph
Version:        1.6.1
Release:        27%{?dist}
Summary:        CVS/RCS repository grapher

License:        GPLv2
URL:            http://www.akhphd.au.dk/~bertho/cvsgraph/
Source0:        http://www.akhphd.au.dk/~bertho/cvsgraph/release/%{name}-%{version}.tar.gz
Source1:        %{name}-httpd.conf
Patch0:         %{name}-1.6.0-config.patch

BuildRequires:  gcc
BuildRequires:  gd-devel
BuildRequires:  util-linux-ng
BuildRequires:  byacc
BuildRequires:  flex
BuildRequires:  freetype-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  %{__perl}

%description
CvsGraph is a utility to make a graphical representation of all
revisions and branches of a file in a CVS/RCS repository. It has been
inspired by the 'graph' option in WinCVS.


%prep
%setup -q
%patch0
rename .php3 .php contrib/*.php3
%{__perl} -pi -e \
  's|/home/bertho/public_html/cvsgraph/cvsgraph|%{_bindir}/cvsgraph|g ;
   s|/home/bertho/public_html/cvsgraph/conf/cvsgraph\.conf|%{_sysconfdir}/cvsgraph.conf|g' \
   contrib/*.php
%{__perl} -pi -e 's|/usr/local/etc|%{_sysconfdir}|g' cvsgraph.1
install -pm 644 %{SOURCE1} contrib/cvsgraph-httpd.conf


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 755 cvsgraph $RPM_BUILD_ROOT%{_bindir}/cvsgraph
install -Dpm 644 cvsgraph.conf $RPM_BUILD_ROOT%{_sysconfdir}/cvsgraph.conf
install -Dpm 644 cvsgraph.1 $RPM_BUILD_ROOT%{_mandir}/man1/cvsgraph.1
install -Dpm 644 cvsgraph.conf.5 $RPM_BUILD_ROOT%{_mandir}/man5/cvsgraph.conf.5



%files
%doc ChangeLog LICENSE README contrib/
%config(noreplace) %{_sysconfdir}/cvsgraph.conf
%{_bindir}/cvsgraph
%{_mandir}/man[15]/cvsgraph*.[15]*


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar  9 2018 Bojan Smojver <bojan@rexursive.com> - 1.6.1-23
- add gcc build requirement

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 11 2013 Remi Collet <rcollet@redhat.com> - 1.6.1-13
- rebuild for new GD 2.1.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 22 2008 Marek Mahut <mmahut fedoraproject.org> - 1.6.1-6
- Build fix for F9

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.6.1-5
- Autorebuild for GCC 4.3

* Sat Aug 18 2007 Marek Mahut <mmahut fedoraproject.org> - 1.6.1-4
- Rebuild with correct license tag

* Tue Aug 29 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.6.1-3
- Drop no longer needed Obsoletes.

* Mon Jul 31 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.6.1-2
- Ensure proper doc file permissions (#200770).

* Sun Jul  9 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.6.1-1
- 1.6.1.

* Thu Feb 16 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.6.0-2
- Rebuild.

* Sun Dec 18 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.6.0-1
- 1.6.0.

* Tue Aug 30 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.5.2-1
- 1.5.2.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.5.1-2
- rebuilt

* Wed Jan 26 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:1.5.1-1
- Update to 1.5.1; wrapper, spelling and part of config patch applied upstream.
- Drop -web subpackage, include *.php as docs.

* Fri Sep  3 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.5.0-0.fdr.1
- Update to 1.5.0.
- Improve default configuration, manual page spelling fixes.
- Rename httpd.conf snippet to zzz-cvsgraph.conf.
- Spec cleanups.

* Sun Jun  1 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.4.0-0.fdr.3
- Address -web package comments in #56.
- Spec cleanups and tweaks according to current Fedora spec template.

* Fri Apr 25 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.4.0-0.fdr.2
- Fix missing Epoch in -web "main" package dependency.
- Save .spec in UTF-8.

* Sat Mar 22 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.4.0-0.fdr.1
- Update to 1.4.0 and current Fedora guidelines.

* Fri Feb  7 2003 Ville Skyttä <ville.skytta at iki.fi> - 1.3.0-1.fedora.1
- First Fedora release.
