%global desc Paster is pluggable command-line frontend, including commands to setup package\
file layouts\
\
Built-in features:\
\
 * Creating file layouts for packages.\
   For instance a setuptools-ready file layout.\
 * Serving up web applications, with configuration based on paste.deploy\
%global sum A pluggable command-line frontend

Name:           python-paste-script
Version:        3.2.0
Release:        4%{?dist}
BuildArch:      noarch

# paste/script/wsgiserver/ is BSD licensed from CherryPy
# paste/script/util/subprocess24.py is MIT or Python
# string24.py may also be MIT or Python (looks to have come from the python-2.4 release)
# The rest of the code is MIT.
License:        MIT and BSD and (MIT or Python)
Summary:        %{sum}
URL:            https://github.com/cdent/pastescript
Source0:        https://pypi.python.org/packages/source/P/PasteScript/PasteScript-%{version}.tar.gz

%if (0%{?fedora} && (0%{?fedora} <= 30)) || (0%{?rhel} && (0%{?rhel} <= 7))
BuildRequires:  python2-devel
BuildRequires:  python2-paste-deploy
BuildRequires:  python2-six
%endif
BuildRequires:  python3-devel
BuildRequires:  python3-paste-deploy
BuildRequires:  python3-six


%description
%{desc}
%if (0%{?fedora} && (0%{?fedora} <= 30)) || (0%{?rhel} && (0%{?rhel} <= 7))
%package -n python2-paste-script
Summary:        %{sum}

%{?python_provide:%python_provide python2-paste-script}

Requires:       python2-paste >= 1.3
Requires:       python2-cheetah
Requires:       python2-cherrypy
Requires:       python2-flup
Requires:       python2-paste-deploy
Requires:       python2-six
%endif

%if (0%{?fedora} && (0%{?fedora} <= 30)) || (0%{?rhel} && (0%{?rhel} <= 7))
%description -n python2-paste-script
%{desc}
%endif

%package -n python3-paste-script
Summary:        %{sum}

%{?python_provide:%python_provide python3-paste-script}

Requires:       python3-paste >= 1.3
Requires:       python3-paste-deploy
Requires:       python3-cherrypy
Requires:       python3-six


%description -n python3-paste-script
%{desc}


%prep
%autosetup -n PasteScript-%{version}

find docs -type f -exec chmod 0644 \{\} \;


%build
%if (0%{?fedora} && (0%{?fedora} <= 30)) || (0%{?rhel} && (0%{?rhel} <= 7))
%py2_build
%endif

%py3_build


%install
%py3_install
mv %{buildroot}%{_bindir}/paster %{buildroot}%{_bindir}/paster-%{python3_version}
ln -s ./paster-%{python3_version} %{buildroot}%{_bindir}/paster-3

%if (0%{?fedora} && (0%{?fedora} <= 30)) || (0%{?rhel} && (0%{?rhel} <= 7))
%py2_install
mv %{buildroot}%{_bindir}/paster %{buildroot}%{_bindir}/paster-%{python2_version}
ln -s ./paster-%{python2_version} %{buildroot}%{_bindir}/paster-2
ln -s ./paster-%{python2_version} %{buildroot}%{_bindir}/paster
%endif

%if (0%{?fedora} && (0%{?fedora} <= 30)) || (0%{?rhel} && (0%{?rhel} <= 7))
%files -n python2-paste-script
%license docs/license.txt
%doc docs/*
%{python2_sitelib}/paste/script
%{python2_sitelib}/PasteScript-%{version}-py%{python2_version}.egg-info
%{python2_sitelib}/PasteScript-%{version}-py%{python2_version}-nspkg.pth
%{_bindir}/paster
%{_bindir}/paster-2
%{_bindir}/paster-%{python2_version}
%endif

%files -n python3-paste-script
%license docs/license.txt
%doc docs/*
%{python3_sitelib}/paste/script
%{python3_sitelib}/PasteScript-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/PasteScript-%{version}-py%{python3_version}-nspkg.pth
%{_bindir}/paster-3
%{_bindir}/paster-%{python3_version}


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.2.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 27 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0 (#1755023).

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-6
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-5
- Rebuilt for Python 3.8

* Fri Aug 16 2019 Andrea Manzi <amanzi@cern.ch> - 3.1.0-3
- remove python2-paste-script from F31 on

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0 (#1685742).
- https://pastescript.readthedocs.io/en/latest/news.html

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.2-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 03 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2 (#1224837).
- Add a python3 package.
- Some spec file cleanup and reorganization.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.5-11
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 27 2012 Luke Macken <lmacken@redhat.com> - 1.7.5-4
- Remove the conflicting tests module (#797813)

* Thu Feb 23 2012 Luke Macken <lmacken@redhat.com> - 1.7.5-3
- Apply a patch from upstream to fix a security issue when running Paster as
  root (#796790)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 08 2011 Luke Macken <lmacken@redhat.com> - 1.7.5-1
- Update to 1.7.5

* Fri Oct 28 2011 Luke Macken <lmacken@redhat.com> - 1.7.4.2-1
- Update to 1.7.4.2
- Update the unbundle patch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 30 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 1.7.3-6
- Use system tempita instead of tempita bundled in paste

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Jul 3 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 1.7.3-4
- Few cleanups
- License tag fix
- Unbundle libraries
- Require python-cherrypy for now; might want to move the bundled library out
  of cherrypy in the future

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 06 2009 Luke Macken <lmacken@redhat.com> - 1.7.3-1
- Update to 1.7.3
- Remove copydir_re_fix.patch

* Tue Dec  9 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.6.3-5
- Add patch for copydir re error
-   (http://trac.pythonpaste.org/pythonpaste/ticket/313)

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.6.3-4
- Rebuild for Python 2.6

* Mon Oct 6 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 1.6.3-3
- Require python-setuptools
- BuildRequire python-paste-deploy

* Sat Jun 14 2008 Luke Macken <lmacken@redhat.com> - 1.6.3-1
- Update to Paste 1.6.3

* Mon Mar 10 2008 Luke Macken <lmacken@redhat.com> - 1.6.2-2
- Require python-paste >= 1.3

* Thu Feb 28 2008 Luke Macken <lmacken@redhat.com> - 1.6.2-1
- Update to 1.6.2

* Wed Oct  3 2007 Luke Macken <lmacken@redhat.com> - 1.3.6-1
- 1.3.6

* Sun Sep  2 2007 Luke Macken <lmacken@redhat.com> - 1.3.5-2
- Update for python-setuptools changes in rawhide

* Sun Jul  8 2007 Luke Macken <lmacken@redhat.com> - 1.3.5-1
- 1.3.5

* Sat Mar  3 2007 Luke Macken <lmacken@redhat.com> - 1.1-1
- 1.1

* Sat Dec  9 2006 Luke Macken <lmacken@redhat.com> - 1.0-4
- Add python-devel to BuildRequires
- Python 2.5 fixes
- 1.0

* Sun Sep 17 2006 Luke Macken <lmacken@redhat.com> - 0.9.8-1
- 0.9.8

* Sun Sep  3 2006 Luke Macken <lmacken@redhat.com> - 0.9-5
- Rebuild for FC6

* Mon Aug 21 2006 Luke Macken <lmacken@redhat.com> - 0.9-4
- Include .pyo files instead of ghosting them.

* Sat Jul 29 2006 Luke Macken <lmacken@redhat.com> - 0.9-3
- Require python-paste-deploy

* Wed Jul 26 2006 Luke Macken <lmacken@redhat.com> - 0.9-2
- Rename to python-paste-script
- Use consistent buildroot variables
- Fix docs inclusion

* Mon Jul 10 2006 Luke Macken <lmacken@redhat.com> - 0.9-1
- Initial package
