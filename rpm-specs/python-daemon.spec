Name:           python-daemon
Version:        2.2.4
Release:        3%{?dist}
Summary:        Library to implement a well-behaved Unix daemon process

# Some build scripts and test franework are licensed GPLv3+ but those aren't shipped
License:        ASL2.0
URL:            https://pagure.io/python-daemon
Source0:        %pypi_source
# Downstream-only patch, twine is unnecessary to build
# https://pagure.io/python-daemon/c/cc9e6a0321a547aacd568aa1e8c7d94a000d5d11
Patch0:         remove-twine-dependency.patch

BuildArch:      noarch
BuildRequires:  python3-devel, python3-setuptools
BuildRequires:  python3-testscenarios
BuildRequires:  python3-docutils
BuildRequires:  python3-lockfile
BuildRequires:  python3-mock
BuildRequires:  python3-testtools

%global _description\
This library implements the well-behaved daemon specification of PEP 3143,\
"Standard daemon process library".\

%description %_description

%package -n python3-daemon
Summary:        Library to implement a well-behaved Unix daemon process
Requires:       python3-lockfile
Requires:       python3-docutils
%{?python_provide:%python_provide python3-daemon}

%description -n python3-daemon %_description

This is the python3 version of the library.

%prep
%autosetup -p1

%build
%py3_build

%install
%py3_install
rm -fr %{buildroot}%{python3_sitelib}/tests

# Test suite requires minimock and lockfile
%check
PYTHONPATH=$(pwd) %{__python3} -m unittest discover

%files -n python3-daemon
%license LICENSE.ASF-2
%{python3_sitelib}/daemon/
%{python3_sitelib}/python_daemon-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.4-2
- Rebuilt for Python 3.9

* Sun Mar 22 2020 Carl George <carl@george.computer> - 2.2.4-1
- Latest upstream rhbz#1765895

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.3-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Aug 28 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.3-6
- Subpackage python2-daemon has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Aug 20 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.2.3-5
- Patch the test suite so it passes with py2

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.3-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 29 2019 Kevin Fenzi <kevin@scrye.com> - 2.2.3-2
- Add patch for socket tests in python 3.8. Fixes bug #1695802

* Tue Feb 12 2019 Alfredo Moralejo <amoralej@redhat.com> - 2.2.3-1
- Update to 2.2.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-9
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.1.2-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Kevin Fenzi <kevin@scrye.com> - 2.1.2-6
- Add dep on python2-docutils. Fixes bug #1478196

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1.2-5
- Python 2 binary package renamed to python2-daemon
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-2
- Rebuild for Python 3.6

* Wed Nov 09 2016 Kevin Fenzi <kevin@scrye.com> - 2.1.2-1
- Update to 2.1.2. Fixes bug #1389593

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Apr 10 2016 Kevin Fenzi <kevin@scrye.com> - 2.1.1-1
- Update to 2.1.1. Fixes bug #1234933

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 30 2015 Toshio Kuratomi <toshio@fedoraproject.org> - - 2.1.0-1
- Update to newer upstream.
- Create a python3 subpackage since upstream supports it
- Note that newer upstream has relicensed to Apache 2.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug  4 2014 Thomas Spura <tomspur@fedoraproject.org> - 1.6-7
- enable tests again as lockfile was fixed

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 14 2011 Kushal Das <kushal@fedoraproject.org> - 1.6-1
- New release of source

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Dec 23 2009 Thomas Spura <tomspur@fedoraproject.org> - 1.5.2-1
- add missing BR: python-nose
- also add lockfile as R (bug #513546)
- update to 1.5.2

* Wed Dec 23 2009 Thomas Spura <tomspur@fedoraproject.org> - 1.5.1-2
- add missing BR: minimock and lockfile -> testsuite works again
- remove patch, use sed instead

* Wed Oct 07 2009 Luke Macken <lmacken@redhat.com> - 1.5.1-1
- Update to 1.5.1
- Remove conflicting files (#512760)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 24 2009 Kushal Das <kushal@fedoraproject.org> 1.4.6-1
- Initial release

