
%if 0%{?fedora} || 0%{?rhel} >= 8
%{!?python3_pkgversion: %global python3_pkgversion 3}
%else
%{!?python3_pkgversion: %global python3_pkgversion 34}
%endif

%global modname arrow

Name:               python-%{modname}
Version:            0.15.6
Release:            1%{?dist}
Summary:            Better dates and times for Python

License:            ASL 2.0
URL:                https://pypi.io/project/arrow
Source0:            %pypi_source arrow
# This lets us drop a hard to port dep for py3 on epel7.
Patch0:             python-arrow-remove-simplejson-test.patch

BuildArch:          noarch

%description
Arrow is a Python library that offers a sensible, human-friendly approach to
creating, manipulating, formatting and converting dates, times, and timestamps.

It implements and updates the datetime type, plugging gaps in functionality,
and provides an intelligent module API that supports many common creation
scenarios.

Simply put, it helps you work with dates and times with fewer imports and a lot
less code.

%package -n         python%{python3_pkgversion}-%{modname}
Summary:            Better dates and times for Python
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}

BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-setuptools
BuildRequires:      python%{python3_pkgversion}-chai
BuildRequires:      python%{python3_pkgversion}-dateutil
BuildRequires:      python%{python3_pkgversion}-pytz
BuildRequires:      python%{python3_pkgversion}-pytest
BuildRequires:      python%{python3_pkgversion}-pytest-mock
BuildRequires:      python%{python3_pkgversion}-pytest-cov
BuildRequires:      python%{python3_pkgversion}-six
BuildRequires:      python%{python3_pkgversion}-simplejson
BuildRequires:      python%{python3_pkgversion}-mock
BuildRequires:      python%{python3_pkgversion}-dateparser

Requires:           python%{python3_pkgversion}-dateutil
Requires:           python%{python3_pkgversion}-six

%description -n python%{python3_pkgversion}-%{modname}
Arrow is a Python library that offers a sensible, human-friendly approach to
creating, manipulating, formatting and converting dates, times, and timestamps.

It implements and updates the datetime type, plugging gaps in functionality,
and provides an intelligent module API that supports many common creation
scenarios.

Simply put, it helps you work with dates and times with fewer imports and a lot
less code.

%prep
%setup -q -n %{modname}-%{version}

#%patch0 -p1


# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%build
%{py3_build}

%install
%{py3_install}

%check
pytest-%{python3_version} tests

%files -n python%{python3_pkgversion}-%{modname}
%doc README.rst CHANGELOG.rst
%license LICENSE
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}-*

%changelog
* Mon Jun 15 2020 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.15.6-1
- Update to upstream release 0.15.6
- Add BR on pytest, pytest-mock and pytest-cov

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 0.15.5-2
- Rebuilt for Python 3.9

* Tue Mar 17 2020 Clément Verna <cverna@fedoraproject.org> - 0.15.5-1
- Update to 0.15.5. Fixes bug #1749062

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.6-2
- Subpackage python2-arrow has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Sep 02 2019 Kevin Fenzi <kevin@scrye.com> - 0.14.6-1
- Update to 0.14.6. Fixes bug #1742367

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 29 2019 Kevin Fenzi <kevin@scrye.com> - 0.14.2-1
- Update to 0.14.2. Fixes bug #1711590

* Thu Apr 11 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.13.1-1
- Update to 0.13.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.12.1-2
- Add Requires on python2-backports-functools_lru_cache

* Sun Jul 22 2018 Kevin Fenzi <kevin@scrye.com> - 0.12.1-1
- Fix FTBFS bug #1605600
- Update to 0.12.1. Fixes bug #1536424

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 20 2017 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.10.0-3
- Fix building 0.10.0 by using the patch: d714497968
  https://github.com/eventable/vobject/commit/d714497968d782afe88c3f5a7c81531bb41b33d8

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.10.0-1
- Update to 0.10.0

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-4
- Rebuild for Python 3.6

* Wed Jul 27 2016 Ralph Bean <rbean@redhat.com> - 0.8.0-3
- Get things ready to work with py34 on epel7, someday.
- Explicit python2 subpackage.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 15 2016 Ralph Bean <rbean@redhat.com> - 0.8.0-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sat Oct 24 2015 Ralph Bean <rbean@redhat.com> - 0.7.0-1
- new version

* Wed Sep 16 2015 Ralph Bean <rbean@redhat.com> - 0.6.0-1
- new version
- Include license file, now shipped by upstream
- Run tests the way upstream does in their Makefile.

* Tue Sep 15 2015 Ralph Bean <rbean@redhat.com> - 0.5.0-3
- Get ready for Python34 on EPEL7.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 22 2015 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.5.0-1
- Update to 0.5.0

* Wed Jan 21 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.4-1
- Update to version 0.4.4
- Enable tests (#1183352)

* Wed Jul 09 2014 Ralph Bean <rbean@redhat.com> - 0.4.2-5
- Modernize python3 macro definition.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Dec 17 2013 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.4.2-1
- Add python-six and python-dateutil as Requires

* Wed Nov 27 2013 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.4.2-1
- Update to 0.4.2
- Prepare for when the tests will be included in the releases
- Add BR to python-chai, python-dateutil and python-six

* Mon Oct 28 2013  Pierre-Yves Chibon <pingou@pingoured.fr> - 0.4.1-1
- initial package for Fedora
