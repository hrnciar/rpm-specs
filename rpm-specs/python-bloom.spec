%global srcname bloom

Name:           python-%{srcname}
Version:        0.9.7
Release:        2%{?dist}
Summary:        Bloom is a release automation tool

License:        BSD
URL:            http://www.ros.org/wiki/bloom
Source0:        https://github.com/ros-infrastructure/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
Bloom provides tools for releasing software on top of a git repository
and leverages tools and patterns from git-buildpackage. Additionally,
bloom leverages meta and build information from catkin
(https://github.com/ros/catkin) to automate release branching and the
generation of platform specific source packages, like debian's src-debs.


%package doc
Summary:        HTML documentation for '%{name}'
BuildRequires:  python%{python3_pkgversion}-sphinx

%description doc
HTML documentation for the '%{srcname}' python module


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  git
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-empy
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-rosdep >= 0.15.0
BuildRequires:  python%{python3_pkgversion}-rosdistro >= 0.8.0
BuildRequires:  python%{python3_pkgversion}-vcstools >= 0.1.22
Conflicts:      python2-%{srcname} < 0.7.2-3
%{?python_provide:%python_provide python%{python3_pkgversion}-bloom}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-catkin_pkg >= 0.4.3
Requires:       python%{python3_pkgversion}-dateutil
Requires:       python%{python3_pkgversion}-empy
Requires:       python%{python3_pkgversion}-PyYAML
Requires:       python%{python3_pkgversion}-rosdep >= 0.15.0
Requires:       python%{python3_pkgversion}-rosdistro >= 0.8.0
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-vcstools >= 0.1.22
%endif

%if !0%{?rhel} || 0%{?rhel} >= 8
Suggests:       %{name}-doc = %{version}-%{release}
%endif

%description -n python%{python3_pkgversion}-%{srcname}
Bloom provides tools for releasing software on top of a git repository
and leverages tools and patterns from git-buildpackage. Additionally,
bloom leverages meta and build information from catkin
(https://github.com/ros/catkin) to automate release branching and the
generation of platform specific source packages, like debian's src-debs.


%prep
%autosetup -p1 -n %{srcname}-%{version}

# These scripts need a versionless python executable.
# They're only used for the tests - we'll do something else.
rm scripts/*


%build
%py3_build

%make_build -C docs html man SPHINXBUILD=sphinx-build-%{python3_version}
rm docs/_build/html/.buildinfo


%install
%py3_install -- --install-scripts %{_bindir}/scripts

echo -n > py3_bins
mkdir py3_bindir
for f in `ls %{buildroot}%{_bindir}/scripts`; do
    mv %{buildroot}%{_bindir}/scripts/$f %{buildroot}%{_bindir}/$f-%{python3_version}
    ln -s $f-%{python3_version} %{buildroot}%{_bindir}/$f-3
    ln -s $f-%{python3_version} %{buildroot}%{_bindir}/$f
    echo -e "%{_bindir}/$f\n%{_bindir}/$f-3\n%{_bindir}/$f-%{python3_version}" >> py3_bins
    ln -s %{buildroot}%{_bindir}/$f-%{python3_version} py3_bindir/$f
done

# Scripts don't install the manpage - do it manually.
install -p -m0644 -D docs/_build/man/%{srcname}.1 %{buildroot}%{_mandir}/man1/%{srcname}.1


%check
# Exclude all code format tests and those which require internet access
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    PATH=$PWD/py3_bindir:$PATH \
    %{__python3} -m nose -w test -e "(test_code_format|test_(multi|unary)_package_repository|test_upstream_tag_special_tag)"


%files doc
%license LICENSE.txt
%doc docs/_build/html

%files -n python%{python3_pkgversion}-%{srcname} -f py3_bins
%license LICENSE.txt
%doc CHANGELOG.rst README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{_mandir}/man1/%{srcname}.1.*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.7-2
- Rebuilt for Python 3.9

* Sat May 09 2020 Scott K Logan <logans@cottsay.net> - 0.9.7-1
- Update to 0.9.7 (rhbz#1830030)

* Wed Apr 15 2020 Scott K Logan <logans@cottsay.net> - 0.9.3-1
- Update to 0.9.3 (rhbz#1797911)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 30 2019 Scott K Logan <logans@cottsay.net> - 0.9.0-1
- Update to 0.9.0 (rhbz#1763368)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 12 2019 Scott K Logan <logans@cottsay.net> - 0.8.0-1
- Update to 0.8.0 (rhbz#1699490)
- Make doc subpackage a weaker dependency

* Mon Feb 11 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-3
- Subpackage python2-bloom has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Scott K Logan <logans@cottsay.net> - 0.7.2-1
- Update to 0.7.2
- Run more relevant tests
- Remove obsolete Group tag
- Switch to Python 3 for doc generation
- Add Python version conditionals

* Fri Jan 11 2019 Scott K Logan <logans@cottsay.net> - 0.7.1-1
- Update to 0.7.1

* Fri Jan 11 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-2
- Enable python dependency generator

* Thu Jan 10 2019 Scott K Logan <logans@cottsay.net> - 0.7.0-1
- Update to 0.7.0

* Thu Nov 15 2018 Scott K Logan <logans@cottsay.net> - 0.6.9-1
- Update to 0.6.9

* Wed Nov 07 2018 Scott K Logan <logans@cottsay.net> - 0.6.8-1
- Update to 0.6.8
- Use python3_pkgversion
- Use srcname
- Create a separate 'doc' package

* Fri Aug 10 2018 Rich Mattes <richmattes@gmail.com> - 0.6.6-1
- Update to release 0.6.6 (rhbz#1504444)
- Fix rahwhide FTBFS (rhbz#1605618)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.26-5
- Rebuilt for Python 3.7

* Sun Feb 11 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.26-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 09 2017 Rich Mattes <richmattes@gmail.com> - 0.5.26-1
- Update to release 0.5.26 (rhbz#1426464)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 21 2016 Rich Mattes <richmattes@gmail.com> - 0.5.23-1
- Update to release 0.5.23 (rhbz#1315529)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.22-4
- Rebuild for Python 3.6

* Sun Nov 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.5.22-3
- Fix PyYAML dependency

* Mon Oct 24 2016 Rich Mattes <richmattes@gmail.com> - 0.5.22-2
- Fix Requires for rawhide

* Thu Oct 20 2016 Rich Mattes <richmattes@gmail.com> - 0.5.22-1
- Update to 0.5.22 (rhbz#1370774)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.21-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Apr 03 2016 Scott K Logan <logans@cottsay.net> - 0.5.21-1
- Update to 0.5.21

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 24 2015 Rich Mattes <richmattes@gmail.com> - 0.5.20-1
- Update to 0.5.20 (rhbz#1214972)

* Wed Mar 04 2015 Rich Mattes <richmattes@gmail.com> - 0.5.19-1
- Update to 0.5.19

* Mon Dec 15 2014 Scott K Logan <logans@cottsay.net> - 0.5.16-1
- Update to 0.5.16

* Sat Dec 13 2014 Scott K Logan <logans@cottsay.net> - 0.5.15-1
- Update to 0.5.15

* Fri Nov 28 2014 Scott K Logan <logans@cottsay.net> - 0.5.14-1
- Update to 0.5.14

* Thu Sep 25 2014 Scott K Logan <logans@cottsay.net> - 0.5.12-1
- Update to 0.5.12

* Thu Jul 24 2014 Scott K Logan <logans@cottsay.net> - 0.5.11-1
- Update to 0.5.11

* Mon Jun 09 2014 Scott K Logan <logans@cottsay.net> - 0.5.9-1
- Update to 0.5.9

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Scott K Logan <logans@cottsay.net> - 0.5.8-1
- Update to 0.5.8

* Fri Apr 11 2014 Scott K Logan <logans@cottsay.net> - 0.5.4-1
- Update to 0.5.4
- Removed setuptools patch

* Mon Apr 07 2014 Scott K Logan <logans@cottsay.net> - 0.5.2-1
- Update to 0.5.2
- Changed source URL to Github
- Added HTML to docs
- Added man page
- Added LICENSE.txt
- Added setuptools patch

* Tue Mar 04 2014 Scott K Logan <logans@cottsay.net> - 0.5.1-1
- Initial package
