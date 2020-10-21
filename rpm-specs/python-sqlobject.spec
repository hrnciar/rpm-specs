%global pypi_name SQLObject
%global lc_name sqlobject

Name:           python-%{lc_name}
Version:        3.3.0
Release:        13%{?dist}
Summary:        SQLObject Object-Relational Manager, aka database wrapper

License:        LGPLv2+
URL:            http://sqlobject.org/
Source0:        https://files.pythonhosted.org/packages/source/S/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description
Classes created using SQLObject wrap database rows, presenting a
friendly-looking Python object instead of a database/SQL interface.
Emphasizes convenience.  Works with MySQL, Postgres, SQLite, Firebird.

This package requires sqlite. Futher database connectors have to be
installed separately.

%package -n python3-%{lc_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-formencode
Requires:       python3-formencode
Requires:       python3-mysql
Requires:       python3-pydispatcher
Requires:       python3-PyGreSQL

%{?python_provide:%python_provide python3-%{lc_name}}

%description -n python3-%{lc_name}
Classes created using SQLObject wrap database rows, presenting a
friendly-looking Python object instead of a database/SQL interface.
Emphasizes convenience.  Works with MySQL, Postgres, SQLite, Firebird.

This package requires sqlite. Futher database connectors have to be
installed separately.

This package provides Python 3 build of %{lc_name}.

%prep
%autosetup -n %{pypi_name}-%{version}
# Delete shebang in all relevant files in docs
find docs -type f -exec sed -i '\@^#!/usr/bin/\(python\|env python\)[23]\?@d' {} +
# Change shebang in all relevant files
find -type f -exec sed -i '1s=^#!/usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' {} +

%build
%py3_build

chmod 0644 docs/rebuild

%install
%py3_install

# Don't install extra files
rm -r %{buildroot}%{python3_sitelib}/docs/
rm %{buildroot}%{python3_sitelib}/LICENSE

%files -n python3-%{lc_name}
%doc PKG-INFO README.rst docs
%{python3_sitelib}/%{lc_name}/
%{python3_sitelib}/%{pypi_name}-*.egg-info/
%{_bindir}/*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.3.0-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 23 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.0-10
- Subpackage python2-sqlobject has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal
- Remove stray files from %%python3_sitelib

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.0-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.0-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.3.0-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Nov 1 2016 Jan Beran <jberan@redhat.com> - 3.3.0-1
- Update to the latest upstream version
- Provide Python 3 subpackage

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 12 2014 Luke Macken <lmacken@redhat.com> - 1.5.1-1
- Update to 1.5.1 (#808859)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 01 2012 Luke Macken <lmacken@redhat.com> - 1.2.2-1
- Update to 1.2.2

* Wed Feb  8 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 1.2.1-3
- Remove the python-sqlite2 dep as sqlobject can use the sqlite3 module from
  the python stdlib

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 14 2011 Luke Macken <lmacken@redhat.com> - 1.2.1-1
- Update to 1.2.1 (#714643)

* Tue Dec  6 2011 David Malcolm <dmalcolm@redhat.com> - 1.0.1-2
- add build-time requirement on python-formencode

* Thu Jun 16 2011 Luke Macken <lmacken@redhat.com> - 1.0.1-1
- Update to 1.0.1 (#690119)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 17 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 0.15.0-1
- Update to 0.15 https://bugzilla.redhat.com/show_bug.cgi?id=659112

* Thu Oct 21 2010 Luke Macken <lmacken@redhat.com> - 0.14.1-1
- Update to 0.14.1 (#630731)

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.10.2-6
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Jan 8 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.10.2-5
- Fix deprecation warnings https://bugzilla.redhat.com/show_bug.cgi?id=552463

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.10.2-2
- Rebuild for Python 2.6

* Thu Jun 26 2008 Luke Macken <lmacken@redhat.com> 0.10.2-1
- Update to 0.10.2
- Add {MySQL,postgresql}-python to Requires

* Tue May 13 2008 Luke Macken <lmacken@redhat.com> 0.10.1-1
- Update to 0.10.1

* Tue Mar 11 2008 Luke Macken <lmacken@redhat.com> 0.10.0-1
- Update to 0.10.0

* Thu Mar  6 2008 Luke Macken <lmacken@redhat.com> 0.9.4-1
- Update to 0.9.4
- Add python-sqlobject-0.9.4-setup.patch to prevent it from trying to download
  its own version of setuptools automatically.

* Thu Feb 21 2008 Toshio Kuratomi <tkuratom@redhat.com> 0.9.3-2
- Stop deleting the ez_setup directory so we can build setuptools eggs as
  upstream intends.

* Wed Feb 13 2008 Toshio Kuratomi <tkuratom@redhat.com> 0.9.3-1
- Update to 0.9.3
- Pick up egginfo on rawhide.

* Tue Nov 27 2007 Luke Macken <lmacken@redhat.com> 0.9.2-1
- 0.9.2

* Wed Oct  3 2007 Luke Macken <lmacken@redhat.com> 0.9.1-1
- 0.9.1

* Sat Jun  2 2007 Luke Macken <lmacken@redhat.com> 0.9.0-1
- Latest upstream release

* Thu May  3 2007 Luke Macken <lmacken@redhat.com> 0.8.2-1
- 0.8.2

* Sat Mar  3 2007 Luke Macken <lmacken@redhat.com> 0.7.3-1
- 0.7.3

* Mon Dec 18 2006 Luke Macken <lmacken@redhat.com> 0.7.2-3
- Require python-sqlite2

* Tue Dec 12 2006 Luke Macken <lmacken@redhat.com> 0.7.2-2
- Add python-devel to BuildRequires

* Sat Dec  9 2006 Luke Macken <lmacken@redhat.com> 0.7.2-1
- 0.7.2
- Remove python-sqlobject-admin.patch, python-sqlobject-0.7.0-ordered-deps.patch
  and python-sqlobject-0.7.0-pkg_resources.patch

* Mon Sep 11 2006 Luke Macken <lmacken@redhat.com> 0.7.0-8
- python-sqlobject-0.7.0-ordered-deps.patch from upstream ticket
  http://trac.turbogears.org/turbogears/ticket/279 (Bug #205894)

* Fri Sep  8 2006 Luke Macken <lmacken@redhat.com> 0.7.0-7
- Include pyo files instead of ghosting them
- Rebuild for FC6

* Fri Jun  9 2006 Luke Macken <lmacken@redhat.com> 0.7.0-6
- Add python-sqlobject-0.7.0-pkg_resources.patch (Bug #195548)
- Remove unnecessary python-abi requirement

* Sun Oct 23 2005 Oliver Andrich <oliver.andrich@gmail.com> 0.7.0-5.fc4
- fixed the changelog usage of a macro

* Sun Oct 23 2005 Oliver Andrich <oliver.andrich@gmail.com> 0.7.0-4.fc4
- %%{?dist} for further distinguish the different builts.

* Thu Oct 13 2005 Oliver Andrich <oliver.andrich@gmail.com> 0.7.0-3
- fixed a spelling error reported by rpmlint
- changed the installation to use -O1
- %%ghost'ed the the resulting *.pyo files

* Thu Oct 06 2005 Oliver Andrich <oliver.andrich@gmail.com> 0.7.0-2
- fixed requirement for FormEncode >= 0.2.2
- Upgrade to upstream version 0.7.0

* Tue Sep 20 2005 Oliver Andrich <oliver.andrich@gmail.com> 0.7-0.1.b1
- Version 0.7b1
