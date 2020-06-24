Name:		cvsplot
Version:	1.7.4
Release:	23%{?dist}

Summary:	Collect statistics from CVS controlled files

License:	GPLv2
URL:		http://cvsplot.sourceforge.net/
Source:		http://download.sourceforge.net/cvsplot/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	perl-generators
Requires:	cvs >= 1.11.1, gnuplot, perl-DateManip >= 5.42
Requires:	perl(String::ShellQuote)

Patch0:		cvsplot-1.7.4.gnuplot.patch

%description
Cvsplot is used for collecting statistics from CVS controlled files.
It produces simple statistics such as how the total number of files
and lines of code change against time.


%prep
%setup -q
%patch0

%build


%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 755 cvsplot.pl $RPM_BUILD_ROOT%{_bindir}/cvsplot



%files
%doc CHANGELOG LICENSE README
%{_bindir}/cvsplot


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.7.4-12
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Aug 19 2007 Marek Mahut <mmahut redhat.com> - 1.7.4-5
- Updating license tag

* Sat Jun 23 2007 Marek Mahut <mmahut redhat.com> - 1.7.4-4
- rebuild

* Thu Jun 14 2007 Marek Mahut <mmahut redhat.com> - 1.7.4-3
- Added patch for compatibility with gnuplot 4
- Fixing spec file

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.7.4-2
- rebuilt

* Fri Dec  3 2004 Ville Skyttä <ville.skytta at iki.fi> - 1.7.4-1
- Update to 1.7.4.

* Thu Jul  1 2004 Ville Skyttä <ville.skytta at iki.fi> - 1.7.3-0.fdr.1
- Update to 1.7.3.

* Sun Mar 21 2004 Ville Skyttä <ville.skytta at iki.fi> - 1.7.2-0.fdr.1
- Update to 1.7.2.

* Sun Sep 14 2003 Ville Skyttä <ville.skytta at iki.fi> - 1.7.1-0.fdr.3
- Require perl-DateManip >= 5.42 to get rid of UTF-8 warnings.

* Sun Sep 14 2003 Ville Skyttä <ville.skytta at iki.fi> - 1.7.1-0.fdr.2
- Remove .pl extension from executable.
- Remove #---- section markers, other spec cleanups.

* Tue May 27 2003 Ville Skyttä <ville.skytta at iki.fi> - 1.7.1-0.fdr.1
- Update to 1.7.1.

* Tue May 13 2003 Ville Skyttä <ville.skytta at iki.fi> - 1.7.0-0.fdr.1
- Update to 1.7.0.

* Thu May  8 2003 Ville Skyttä <ville.skytta at iki.fi> - 1.6.5-0.fdr.1
- Update to 1.6.5.

* Sun Apr 13 2003 Ville Skyttä <ville.skytta at iki.fi> - 1.6.4-0.fdr.1
- Update to 1.6.4.
- Save .spec in UTF-8.

* Sat Mar 22 2003 Ville Skyttä <ville.skytta at iki.fi> - 1.6.3-0.fdr.1
- Update to current Fedora guidelines.

* Fri Feb  7 2003 Ville Skyttä <ville.skytta at iki.fi> - 1.6.3-1.fedora.1
- First Fedora release.
