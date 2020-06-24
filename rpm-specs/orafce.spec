%global githubversion 3_9_0

Name:           orafce
Version:        3.9.0
Release:        1%{?dist}
Summary:        Implementation of some Oracle functions into PostgreSQL
License:        BSD
URL:            http://github.com/orafce/orafce
Source0:        https://github.com/orafce/orafce/archive/VERSION_%{githubversion}.tar.gz

%{?postgresql_module_requires}

BuildRequires:  gcc
BuildRequires:  clang-devel llvm-devel
BuildRequires:  postgresql-server-devel openssl-devel krb5-devel bison flex


%description
The goal of this project is implementation some functions from Oracle database.
Some date functions (next_day, last_day, trunc, round, ...) are implemented
now. Functionality was verified on Oracle 10g and module is useful
for production work.


%prep
%setup -q -n %{name}-VERSION_%{githubversion}


%build
%make_build USE_PGXS=1 PG_CONFIG=/usr/bin/pg_server_config


%install
%make_install USE_PGXS=1 PG_CONFIG=/usr/bin/pg_server_config


%files
%license COPYRIGHT.orafce
%doc INSTALL.orafce README.asciidoc
%{_libdir}/pgsql/
%{_datadir}/pgsql/
%exclude %{_docdir}/pgsql/


%changelog
* Wed Mar 11 2020 - Devrim Gündüz <devrim@gunduz.org> - 3.9.0-1
- Update to 3.9.0, to fix #1811800

* Sun Mar 08 2020 Patrik Novotný <panovotn@redhat.com> - 3.8.0-3
- Require clang and llvm on build time (JIT enabled in PostgreSQL)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 25 2019 Pavel Raiskup <praiskup@redhat.com> - 3.8.0-1
- new upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Pavel Raiskup <praiskup@redhat.com> - 3.4.0-6
- rebuild against PostgreSQL 11

* Wed Sep 05 2018 Pavel Raiskup <praiskup@redhat.com> - 3.4.0-5
- build against postgresql-server-devel (rhbz#1618698)

* Mon Jul 23 2018 Pavel Raiskup <praiskup@redhat.com> - 3.4.0-4
- ftbfs: missing gcc BR
- spec cleanup

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 11 2017 Pavel Raiskup <praiskup@redhat.com> - 3.4.0-1
- update to 3.4.0 (and build against PostgreSQL 10), per release notes:
  https://github.com/orafce/orafce/releases/tag/VERSION_3_4_0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 10 2016 Pavel Raiskup <praiskup@redhat.com> - 3.3.0-3
- bump: build in rawhide done too early

* Mon Oct 10 2016 Pavel Raiskup <praiskup@redhat.com> - 3.3.0-2
- bump: PostgreSQL 9.6.0

* Wed Oct 05 2016 Petr Kubat <pkubat@redhat.com> - 3.3.0-1
- Update to 3.3.0 per changes at
  https://github.com/orafce/orafce/releases/tag/VERSION_3_3_0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 Jozef Mlich <imlich@fit.vutbr.cz> - 3.2.0-1
- Update to 3.2.0 per changes at
  https://github.com/orafce/orafce/releases/tag/VERSION_3_2_0

* Fri Jan 08 2016 Pavel Kajaba <pkajaba@redhat.com> - 3.1.2-2
- Rebuild for PostgreSQL 9.5 (rhbz#1296584)

* Thu Dec 24 2015 Jean-Francois Saucier <jsaucier@gmail.com> - 3.1.2-1
- Update to the new upstream version
- Added support for postgresql 9.5
- Removed support for postgresql 8.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 02 2015 Jozef Mlich <jmlich@redhat.com> - 3.0.9-2
- Release bump (forgoten new-sources)

* Thu Apr 02 2015 Jozef Mlich <jmlich@redhat.com> - 3.0.9-1
- Update to new upstream version
- Requires :MODULE_COMPAT Resolves #1181151

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Jan 11 2014 Jean-Francois Saucier <jsaucier@gmail.com> - 3.0.6-1
- Update to the new upstream version
- Added support for postgresql 9.3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Jean-Francois Saucier <jsaucier@gmail.com> - 3.0.4-1
- Update to the new upstream version
- Added support for postgresql 9.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 24 2010 - Jean-Francois Saucier <jsaucier@gmail.com> - 3.0.3-1
- Update to the new upstream version

* Wed Apr 28 2010 - Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 3.0.1-3
- Rename back the package to orafce after discussion on devel list

* Mon Apr 19 2010 - Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 3.0.1-2
- Make some cleanup as described in #251805
- Clean %%files section
- Rename the package back to postgresql-orafce to be consistent with other extensions

* Fri Oct  2 2009 - Devrim Gündüz <devrim@commandprompt.com> - 3.0.1-1
- Update to 3.0.1
- Remove patch0, it is in upstream now.
- Apply some 3.0 fixes to spec.

* Wed Aug 20 2008 - Devrim Gündüz <devrim@commandprompt.com> - 2.1.4-1
- Update to 2.1.4

* Sun Jan 20 2008 - Devrim Gündüz <devrim@commandprompt.com> - 2.1.3-2
- Spec file fixes, per bz review #251805

* Mon Jan 14 2008 - Devrim Gündüz <devrim@commandprompt.com> - 2.1.3-1
- Update to 2.1.3

* Fri Aug 10 2007 - Devrim Gündüz <devrim@commandprompt.com> - 2.1.1-1
- Update to 2.1.1
- Spec file cleanup

* Wed Aug 30 2006 - Devrim Gündüz <devrim@commandprompt.com> - 2.0.1-1
- Initial packaging
