# https://fedoraproject.org/wiki/Packaging:SourceURL#Github
%global commit f18a3ef33f9a7891dc7688a9b69ea4d392feac2a
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           mysqltuner
Version:        1.7.17
Release:        2%{?shortcommit:.git.%{shortcommit}}%{?dist}
Summary:        MySQL configuration assistant

License:        GPLv3+
URL:            http://mysqltuner.com/
Source0:        https://github.com/major/MySQLTuner-perl/archive/%{commit}.tar.gz#/MySQLTuner-perl-%{shortcommit}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
Requires:       which

# RHBZ 1838780 - mariadb lacks mysql provides on el8
%if 0%{?fedora} || 0%{?rhel} >= 8
Requires:       (mysql or mariadb)
%else
Requires:       mysql
%endif

%description
MySQLTuner is a script written in Perl that will assist you with your
MySQL configuration and make recommendations for increased performance
and stability.  Within seconds, it will display statistics about your
MySQL installation and the areas where it can be improved.


%prep
%setup -q -n MySQLTuner-perl-%{commit}


%build


%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 755 mysqltuner.pl $RPM_BUILD_ROOT%{_bindir}/mysqltuner



%files
%doc LICENSE README.md
%{_bindir}/mysqltuner


%changelog
* Thu May 21 2020 Andrew Bauer <zonexpertconsulting@outlook.com> - 1.7.17-2.git.f18a3ef
- RHBZ 1838780 mariadb lacks mysql provides on el8

* Thu May 21 2020 Major Hayden <major@mhtx.net> - 1.7.17-1.git.f18a3ef
- New release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-4.git.59e5f40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-3.git.59e5f40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-2.git.59e5f40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 23 2018 josef radinger <cheese@nosuchhost.net> - 1.7.13-1.git.59e5f40
- fix build
- fix version

* Mon Aug 20 2018 josef radinger <cheese@nosuchhost.net> - 1.7.2-1.git.21860fe
- bump version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.18-5.git.401cb54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.18-4.git.401cb54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.18-3.git.401cb54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.18-2.git.401cb54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 josef radinger <cheese@nosuchhost.net> - 1.6.18-1.git.401cb54
- bump version + fix download-url

* Fri Mar 04 2016 Major Hayden <major@mhtx.net> - 1.6.0-3.git.a154701
- New upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 24 2015 Major Hayden <major@mhtx.net> - 1.6.0-1
- New upstream version
- Removed 'v' from source URL

* Thu Aug 20 2015 Major Hayden <major@mhtx.net> - 1.5.1-1
- New upstream version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec 05 2014 Manuel "lonely wolf" Wolfshant <wolfy@fedoraproject.org> - 1.4.0-1
- New upstream version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.2.0-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Mar  8 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.2.0-1
- Update to 1.2.0, patches applied upstream.

* Sun Mar  6 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.1.1-4.20100125git
- Patch to fix various engine availability related issues (#682477).

* Mon Feb 28 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.1.1-3.20100125git
- Update to git revision e8495ce for users w/o passwords listing improvements.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 25 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.1.1-1
- Update to 1.1.1.
- Improve summary.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul  1 2009 Ville Skyttä <ville.skytta@iki.fi> - 1.0.0-1
- Update to 1.0.0.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Nov  4 2008 Ville Skyttä <ville.skytta@iki.fi> - 1.0.0-0.1.rc1
- 1.0.0-rc1.

* Thu Sep 11 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.9.9-1
- 0.9.9.
- Update description.

* Mon Jul 21 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.9.8-1
- 0.9.8, --checkversion patch applied upstream.

* Sat Jun 21 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.9.1-4
- Don't warn if --skipversion is used (#452172).

* Thu Jun 19 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.9.1-1
- 0.9.1.
- Patch to not "phone home" by default (--skipversion -> --checkversion).

* Sat Apr 12 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.9.0-1
- 0.9.0.

* Sun Mar  2 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.8.6-1
- 0.8.6.

* Mon Feb 18 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.8.5-1
- 0.8.5.
