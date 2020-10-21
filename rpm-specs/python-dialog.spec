%global upstream_name pythondialog

Name:           python-dialog
Version:        3.5.1
Release:        3%{?dist}
Summary:        Python interface to the Unix dialog utility

License:        LGPLv2+
URL:            http://pythondialog.sourceforge.net
# Upstream releases two tarballs from the same sources
Source0:        %{pypi_source %{upstream_name}}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
A Python interface to the Unix dialog utility, designed to provide an
easy, pythonic, and as complete as possible way to use the dialog
features from Python code.}

%description %_description

%package -n python3-dialog
Requires:       dialog
Summary:        %{summary}
%{?python_provide:%python_provide python3-dialog}

%description -n python3-dialog %_description

%prep
%autosetup -n %{upstream_name}-%{version}

find examples -name '*.py' -print -exec sed -r -i 's|(.!)\s+/usr/bin/env python.*|\1%{__python3}|' {} \;

%build
%py3_build

%install
%py3_install

%files -n python3-dialog
%license COPYING
%doc README.rst examples/
%{python3_sitelib}/dialog.py*
%{python3_sitelib}/__pycache__/
%{python3_sitelib}/pythondialog-*.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.5.1-2
- Rebuilt for Python 3.9

* Tue Mar 31 2020  <zbyszek@nano-f31> - 3.5.1-1
- Update to latest version (#1778504)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.0-20
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.0-19
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 10 2018 Miro Hrončok <mhroncok@redhat.com> - 3.3.0-16
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.3.0-14
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.3.0-10
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 12 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.3.0-7
- Restore %%license
- Simplify spec file

* Sat Dec 12 2015 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 3.3.0-6
- include python_provide macro bz# 1291005
- include el6 conditionals / fixes from Nick Le Mouton

* Thu Dec 03 2015 Robert Buchholz <rbu@goodpoint.de> - 3.3.0-5
- epel7: Only build python2 package

* Thu Dec 03 2015 Robert Buchholz <rbu@goodpoint.de> - 3.3.0-4
- No need to convert README, upstream provides utf-8
- Remove obsolete comment

* Thu Nov 12 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Nov 12 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Nov 12 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@laptop> - 3.3.0-1
- Add python3 subpackage

* Wed Oct 28 2015 Felix Schwarz <fschwarz@fedoraproject.org> - 3.3.0-1
- update to new upstream version (#998103)
- drop patch for demo.py (included in upstream release)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 20 2011 Miloš Jakubíček <xjakub@fi.muni.cz> - 2.7-13
- Added python-dialog-demo.patch, fix BZ#594988
- Fix rpmlint: W: file-not-utf8 /usr/share/doc/python-dialog-2.7/TODO
- Fix rpmlint: W: file-not-utf8 /usr/share/doc/python-dialog-2.7/README

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.7-12
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.7-9
- Rebuild for Python 2.6

* Thu Jun 05 2008 Aurelien Bompard <abompard@fedoraproject.org> 2.7-8
- add egg info

* Sun Aug 26 2007 Aurelien Bompard <abompard@fedoraproject.org> 2.7-7
- fix license tag (see head of dialog.py)

* Sat Dec 09 2006 Aurelien Bompard <abompard@fedoraproject.org> 2.7-6
- rebuild

* Wed Nov 01 2006 Aurelien Bompard <abompard@fedoraproject.org> 2.7-5
- unghost .pyo file

* Wed Aug 30 2006 Aurelien Bompard <abompard@fedoraproject.org> 2.7-4
- rebuild

* Wed Feb 22 2006 Aurelien Bompard <gauret[AT]free.fr> 2.7-3
- rebuild for FC5

* Fri Dec 23 2005 Aurelien Bompard <gauret[AT]free.fr> 2.7-1
- remove hardcoded disttag

* Wed Mar 30 2005 Aurelien Bompard <gauret[AT]free.fr> 2.7-1.fc4
- change release tag for FC4
- drop Epoch

* Thu Feb 10 2005 Aurelien Bompard <gauret[AT]free.fr> 0:2.7-1
- update to version 2.7
- update URL

* Sat Feb 05 2005 Toshio Kuratomi <toshio@tiki-lounge.com> 0:2.0.6-2
- Change %%python_sitearch to %%python_sitelib as sitearch references
  /usr/lib64 on x86_64 multilib and the python files install to /usr/lib.

* Sat Jul 24 2004 Aurelien Bompard <gauret[AT]free.fr> 0:2.06-0.fdr.1
- Initial Fedora Package
