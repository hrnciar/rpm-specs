
%global modname pkgwat.api

Name:             python-pkgwat-api
Version:          0.13
Release:          6%{?dist}
Summary:          Python API for querying the fedora packages webapp

License:          LGPLv2+
URL:              https://pypi.python.org/pypi/pkgwat.api
Source0:          https://pypi.python.org/packages/source/p/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:        noarch

%description
Python API for pkgwat
http://pypi.python.org/pypi/pkgwat.cli

%package -n python3-pkgwat-api
Summary:          Python API for querying the fedora packages webapp
%{?python_provide:%python_provide python3-pkgwat-api}

BuildRequires:    python3-devel
BuildRequires:    python3-setuptools
BuildRequires:    python3-six
BuildRequires:    python3-requests
Requires:         python3-six
Requires:         python3-requests

%description -n python3-pkgwat-api
Python3 API for pkgwat
http://pypi.python.org/pypi/pkgwat.cli.

%prep
%setup -q -n %{modname}-%{version}

rm -rf pkgwat.api.egg-info

%build
%{py3_build}

%install
%{py3_install}

%files -n python3-pkgwat-api
%doc README.rst lgpl-2.1.txt
%license LICENSE
%{python3_sitelib}/pkgwat
%{python3_sitelib}/%{modname}-%{version}-*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Kamil Páral <kparal@redhat.com> - 0.13-1
- Release 0.13

* Mon Feb 11 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12-19
- Subpackage python2-pkgwat-api has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.12-16
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.12-12
- Rebuild for Python 3.6

* Fri Sep 09 2016 Ralph Bean <rbean@redhat.com> - 0.12-11
- Modernize python macros.
- Explicitly python2 subpackage.

* Fri Sep 09 2016 Ralph Bean <rbean@redhat.com> - 0.12-10
- Remove no-longer-needed Obsoletes/Provides (RHBZ#1374243).

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 13 2015 Ralph Bean <rbean@redhat.com> - 0.12-7
- Fix rhel7 conditional...

* Thu Nov 12 2015 Ralph Bean <rbean@redhat.com> - 0.12-6
- Make python-ordereddict unnecessary on EL7.

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Thu Nov 14 2013 Ralph Bean <rbean@redhat.com> - 0.12-1
- Fix unicode issues when stripping html from responses.

* Sun Nov 03 2013 Ralph Bean <rbean@redhat.com> - 0.10-2
- Add obsoletes/provides on python3-python-pkgwat-api

* Tue Oct 22 2013 Ralph Bean <rbean@redhat.com> - 0.10-1
- Latest upstream with some bugfixes.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 11 2013 Ralph Bean <rbean@redhat.com> - 0.9-1
- Latest upstream.
- New history function to search datagrepper.
- Subpackages support with patches from Ariel O. Barria.

* Tue Apr 09 2013 Ralph Bean <rbean@redhat.com> - 0.8-1
- Latest upstream with a bugfix for py2.6.
- Conditionally depend on python-ordereddict.
- Remove py3.2 patch.  Now included in upstream's release.

* Wed Mar 20 2013 Ralph Bean <rbean@redhat.com> - 0.7-3
- Correctly name the python3 subpackage.

* Thu Feb 28 2013 Ralph Bean <rbean@redhat.com> - 0.7-2
- Patch to fix syntax error on python3.2.

* Thu Feb 28 2013 Ralph Bean <rbean@redhat.com> - 0.7-1
- Latest upstream with a new "get" function.

* Wed Feb 27 2013 Ralph Bean <rbean@redhat.com> - 0.6-1
- Latest upstream with new functions for querying relationships.
- Removed spurious newlines in .spec file.
- Modernized with_python3 conditional.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 22 2013 Ralph Bean <rbean@redhat.com> - 0.5-1
- Latest upstream; Fix to the karma formatting.

* Wed Jan 16 2013 Ralph Bean <rbean@redhat.com> - 0.4-1
- Latest upstream with support for newer python-requests.

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 0.3-5
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 05 2012 Ralph Bean <rbean@redhat.com> - 0.3-3
- Remove the bundled egg-info.

* Mon Jul 02 2012 Ralph Bean <rbean@redhat.com> - 0.3-2
- Remove tests for koji.

* Mon Jul 02 2012 Ralph Bean <rbean@redhat.com> - 0.3-1
- Latest upstream, includes unit tests.

* Mon Jul 02 2012 Ralph Bean <rbean@redhat.com> - 0.1-1
- Initial package for Fedora
