%global srcname gammu
%global gammu_ver 1.40.0

Name:       python-gammu
Version:    3.0
Release:    1%{?dist}
Summary:    Python bindings for Gammu
License:    GPLv2+
URL:        http://wammu.eu/python-gammu/
Source0:    https://github.com/gammu/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  gammu-devel >= %{gammu_ver}
#for tests: Solve DBI failed to initialize!
BuildRequires:  libdbi-dbd-sqlite

%description
Python bindings for Gammu library.
It currently does not support all Gammu features,
but range of covered functions is increasing,
if you need some specific, feel free to use bug tracking
system for feature requests.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:    %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:   gammu-libs%{?_isa} >= %{gammu_ver}

%description -n python%{python3_pkgversion}-%{srcname}
Python3 bindings for Gammu library.
It currently does not support all Gammu features,
but range of covered functions is increasing,
if you need some specific, feel free to use bug tracking
system for feature requests.

%prep
%setup -q

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test || :

%files -n python%{python3_pkgversion}-%{srcname}
%doc AUTHORS NEWS.rst README.rst examples/*
%license COPYING
%{python3_sitearch}/gammu
%{python3_sitearch}/python_gammu-*.egg-info

%changelog
* Mon Jun 15 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 3.0-1
- Update to 3.0 (#1846915)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.12-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Miro Hrončok <mhroncok@redhat.com> - 2.12-5
- Subpackage python2-gammu has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.12-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.12-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Sérgio Basto <sergio@serjux.com> - 2.12-1
- Update to 2.12 (#1680247)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.11-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Sérgio Basto <sergio@serjux.com> - 2.11-2
- Enforce the exact EVR for gammu-libs

* Sat Jan 06 2018 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 2.11-1
- Update to 2.11 (#1531828)

* Sun Dec 24 2017 Sérgio Basto <sergio@serjux.com> - 2.10-1
- Update to python-gammu-2.10 (#1510442)
. Add python 3 compatibility for epel7

* Sun Aug 20 2017 Sérgio Basto <sergio@serjux.com> - 2.9-2
- Bump for another build

* Sun Aug 20 2017 Sérgio Basto <sergio@serjux.com> - 2.9-1
- Update to 2.9 (#1460053)

* Sun Aug 20 2017 Sérgio Basto <sergio@serjux.com> - 2.6-7
- Use python3 compatibility to EPEL
  https://fedoraproject.org/wiki/PackagingDrafts:Python3EPEL

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.6-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun May 29 2016 Sérgio Basto <sergio@serjux.com> - 2.6-1
- Update python-gammu to 2.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Sérgio Basto <sergio@serjux.com> - 2.5-1
- Update python-gammu to 2.5

* Tue Nov 17 2015 Sérgio Basto <sergio@serjux.com> - 2.4-2
- Fixed 3 typos:
  - %%{?python_provide:%%python_provide python2-%{srcname}} is duplicated on line 22.
  It should only be present on line 33.
  - python2-gammu contains %{python3_sitearch}/gammu. This does not look right.
  - python2_sitearch should be used instead of python_sitearch.

* Sun Nov 08 2015 Sérgio Basto <sergio@serjux.com> - 2.4-1
- Update python-gammu to 2.4
- Added python3 support

* Tue Jun 16 2015 Sérgio Basto <sergio@serjux.com> - 2.3-1
- python-gammu is independent since gammu-1.36, again ...

* Thu Jan  8 2009 Caolán McNamara <caolanm@redhat.com> - 0.28-1
- devel n-v-r < F-10, syncing to rebuild against libGammu

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.27-3
- Fix locations for Python 2.6

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.27-2
- Rebuild for Python 2.6

* Sat Oct 11 2008 Xavier Lamien <lxtnow@gmail.com> - 0.27-1
- Update release.

* Sun Sep 14 2008 Xavier Lamien <lxtnow@gmail.com> - 0.26-3
- Rebuild.

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.26-2
- fix license tag

* Mon Aug 25 2008 Xavier Lamien <lxtnow@gmail.com> - 0.26-1
- Update release.

* Sat Apr 05 2008 Xavier Lamien <lxtnow@gmail.com> - 0.24-3
- Added missing file on Rawhide.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.24-2
- Autorebuild for GCC 4.3

* Fri Dec 28 2007 Xavier Lamien < lxtnow[at]gmail.com > - 0.24-1
- Updated Release.

* Wed Oct 17 2007 Xavier Lamien < lxtnow[at]gmail.com > - 0.22-3
- Added pcc arch build.

* Sun Oct 14 2007 Xavier Lamien < lxtnow[at]gmail.com > - 0.22-2
- Excluded pcc arch for now, build error reported to upstream.

* Fri Oct 12 2007 Xavier Lamien < lxtnow[at]gmail.com > - 0.22-1
- Updated Release.

* Tue Jul 03 2007 Xavier Lamien < lxtnow[at]gmail.com > - 0.21-1
- Updated Release.

* Wed May 23 2007 Xavier Lamien < lxtnow[at]gmail.com > - 0.20-1
- Updated release.
- fixed permission on examples files.
- added gammu as require (need it to work with wammu package).
 
* Tue May 08 2007 Xavier Lamien < lxtnow[at]gmail.com > - 0.19-1
- Initial RPM Release.
