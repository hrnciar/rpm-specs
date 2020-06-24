Name:           cvsweb
Version:        3.0.6
Release:        25%{?dist}
Summary:        Web interface for CVS repositories

License:        BSD
URL:            http://www.freebsd.org/projects/cvsweb.html
Source0:        http://people.freebsd.org/~scop/cvsweb/%{name}-%{version}.tar.gz
Patch0:         %{name}-3.0.6-fedora-config.patch

BuildArch:      noarch
BuildRequires:      perl-generators
Requires:       rcs
Requires:       cvs
Requires:       httpd

%description
CVSweb is a WWW interface for CVS repositories with which you can
browse a file hierarchy on your browser to view each file's revision
history in a very handy manner.  This package contains the FreeBSD
version of CVSweb.


%prep
%setup -q
%patch0 -p1


%build


%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 755 cvsweb.cgi \
  $RPM_BUILD_ROOT%{_datadir}/cvsweb/cvsweb.cgi
install -Dpm 644 css/cvsweb.css \
  $RPM_BUILD_ROOT%{_datadir}/cvsweb/cvsweb.css
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/cvsweb/conf.d
install -pm 644 cvsweb.conf $RPM_BUILD_ROOT%{_sysconfdir}/cvsweb
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/enscript/hl
install -pm 644 enscript/lang_cvsweb*.st $RPM_BUILD_ROOT%{_datadir}/enscript/hl
install -Dpm 644 icons/minigraph.png \
  $RPM_BUILD_ROOT%{_localstatedir}/www/icons/small/minigraph.png



%files
%doc ChangeLog NEWS README TODO INSTALL
%config(noreplace) %{_sysconfdir}/cvsweb/
%{_datadir}/cvsweb
%{_datadir}/enscript
%{_localstatedir}/www/icons/small/minigraph.png


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 3.0.6-14
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 16 2009 Dennis Gilmore <dennis@ausil.us> - 3.0.6-8
- missed a reference to missing source file

* Tue Mar 16 2009 Dennis Gilmore <dennis@ausil.us> - 3.0.6-7
- remove references to non existant cvsweb.conf file

* Tue Mar 16 2009 Dennis Gilmore <dennis@ausil.us> - 3.0.6-6
- remove references to perl patch that doesnt exist in cvs

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jun 21 2008 Lubomir Rintel <lkundrak@v3.sk> - 3.0.6-4
- Move it out of /var/www
- Correct the httpd configuration

* Fri Sep 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 3.0.6-3
- Rebuild.

* Mon Jan  9 2006 Ville Skyttä <ville.skytta at iki.fi> - 3.0.6-2
- Use enscript by default if it's installed (enscript >= 1.6.3 in FC5+).
- Fix cvsweb.css permissions.

* Sun Sep 25 2005 Ville Skyttä <ville.skytta at iki.fi> - 3.0.6-1
- 3.0.6.

* Sun May 29 2005 Ville Skyttä <ville.skytta at iki.fi> - 3.0.5-2
- 3.0.5.
- Install the sample httpd.conf as doc instead of into place; running
  cvsweb with mod_perl does not play nicely with SELinux.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 3.0.4-2
- rebuilt

* Sat Nov  6 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:3.0.4-1
- Update to 3.0.4.

* Wed Nov  3 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:3.0.3-0.fdr.1
- Update to 3.0.3.

* Fri Aug 20 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:3.0.2-0.fdr.1
- Update to 3.0.2.

* Sat May  8 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:3.0.1-0.fdr.1
- Update to 3.0.1.

* Sat Apr 24 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:3.0.0-0.fdr.2
- Make httpd reload its config on install, upgrade and erase.
- Rename httpd config file snippet to zzz-cvsweb.conf to ensure it is
  loaded after the possible perl.conf from mod_perl.

* Thu Feb 26 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:3.0.0-0.fdr.1
- Update to 3.0.0.

* Sun Feb 15 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:2.9.3-0.fdr.1
- Update to 2.9.3 (beta).

* Sat Jan 31 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:2.9.2-0.fdr.1
- Update to 2.9.2 (beta).
- Include CvsGraph icon.
- Don't use -l with cvs(1), and enable read-only annotations by default.
- Note: this is not a plug-in upgrade from earlier versions, manual
  configuration changes in %%{_sysconfdir}/cvsweb/cvsweb.conf are needed.
  See INSTALL for details.

* Sat Oct 25 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.9.1-0.fdr.3
- Allow tarballs download by default, and make root own the files inside.

* Mon Oct 13 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.9.1-0.fdr.2
- Fix source permissions.

* Mon Oct  6 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.9.1-0.fdr.1
- Update to 2.9.1.

* Mon Apr  7 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.0.6-0.fdr.2
- Don't use "Powered by..." image by default (#22 comment 5).
- Remove spurious BuildRequires: perl.
- Conditionalize httpd vs apache dependency for easier deployment on RH7x.
- Save .spec in UTF-8.

* Sat Apr  5 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.0.6-0.fdr.1
- Update to current Fedora guidelines.

* Sun Feb 23 2003 Ville Skyttä <ville.skytta at iki.fi> - 2.0.6-1.fedora.1
- First Fedora release.
