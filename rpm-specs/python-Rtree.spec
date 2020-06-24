%global srcname Rtree

Name:           python-%{srcname}
Version:        0.9.4
Release:        2%{?dist}
Summary:        R-Tree spatial index for Python GIS
%global _description \
Rtree is a ctypes Python wrapper of the spatialindex library, that \
provides a number of advanced spatial indexing features for the \
spatially curious Python user. These features include: \
\
-Nearest neighbor search \
-Intersection search \
-Multi-dimensional indexes \
-Clustered indexes (store Python pickles directly with index entries) \
-Bulk loading \
-Deletion \
-Disk serialization \
-Custom storage implementation \
 (to implement spatial indexing in ZODB, for example)

License:        LGPLv2
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/R/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  spatialindex-devel
BuildRequires:  python3-devel

BuildRequires:  python3-pytest
BuildRequires:  python3-numpy

%description %{_description}


%package -n python3-rtree
Summary:        %{summary}
%{?python_provide:%python_provide python3-rtree}

Requires:       spatialindex

%description -n python3-rtree %{_description}


%prep
%autosetup -n Rtree-%{version}

# Delete junk from tarball.
rm -rf Rtree.egg-info
find . -name '*.pyc' -delete
rm setup.cfg
rm -rf docs/build


%build
%py3_build


%install
%py3_install


%check
export LANG=C.UTF-8
PYTHONPATH="%{buildroot}%{python3_sitelib}" \
    py.test-%{python3_version} -ra tests
PYTHONPATH="%{buildroot}%{python3_sitelib}" \
    py.test-%{python3_version} -ra --doctest-modules rtree

# Note that there is no %%files section for the unversioned python module if we
# are building for several python runtimes
%files -n python3-rtree
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/rtree
%{python3_sitelib}/Rtree-%{version}-py?.?.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-2
- Rebuilt for Python 3.9

* Tue Feb 11 2020 Volker Fröhlich <volker27@gmx.at> - 0.9.4-1
- New version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Volker Fröhlich <volker27@gmx.at> - 0.9.3-1
- New version

* Mon Dec 09 2019 Volker Fröhlich <volker27@gmx.at> - 0.9.2-1
- New version

* Mon Nov 25 2019 Volker Fröhlich <volker27@gmx.at> - 0.9.1-1
- Remove meaningless comment
- There's no point in building documentation we don't ship and it failed too
- Remove outdated version constraints on R/BR
- Remove upstreamed patch

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8.3-8
- Subpackage python2-rtree has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 22 2017 Volker Fröhlich <volker27@gmx.at> - 0.8.3-4
- Remove meaningless comment

* Thu Aug 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8.3-4
- Rename binary packages to lowercase

* Sat Aug 12 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.8.3-3
- New upstream release
- Update spec to new guidelines
- Add Python 3 subpackage (#1481100)
- Add documentation
- Simplify spec with more macros
- NumPy is needed for testing as well

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb 08 2014 Volker Fröhlich <volker27@gmx.at> - 0.7.0-5
- Remove hard-coded library extension (BZ#1001840)
- Ignore harmless test failure to fix FTBFS
- Remove obsolete version requirements

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 12 2012 Volker Fröhlich <volker27@gmx.at> - 0.7.0-2
- BR python-setuptools instead of ...-devel
- Delete pre-built egg info

* Sat Apr 14 2012 Volker Fröhlich <volker27@gmx.at> - 0.7.0-1
- Initial package for Fedora
