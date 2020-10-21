%global srcname catkin_tools

Name:           python-%{srcname}
Version:        0.6.1
Release:        2%{?dist}
Summary:        Command line tools for working with catkin

License:        ASL 2.0
URL:            http://catkin-tools.readthedocs.org
Source0:        https://github.com/catkin/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
Provides command line tools for working with catkin


%package doc
Summary:        HTML documentation for %{srcname}
BuildRequires:  python3-rpm-macros
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx_rtd_theme

%description doc
HTML documentation for %{srcname}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  cmake
BuildRequires:  python%{python3_pkgversion}-catkin_pkg >= 0.2.9
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-osrf-pycommon >= 0.1.1
BuildRequires:  python%{python3_pkgversion}-pyparsing
BuildRequires:  python%{python3_pkgversion}-PyYAML
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-trollius
Requires:       cmake
Requires:       make
Conflicts:      python2-%{srcname} < 0.4.4-7
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-catkin_pkg >= 0.2.9
Requires:       python%{python3_pkgversion}-osrf-pycommon >= 0.1.1
Requires:       python%{python3_pkgversion}-PyYAML
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-trollius
%endif

%if !0%{?rhel} || 0%{?rhel} >= 8
Suggests:       %{name}-doc = %{version}-%{release}
%endif

%description -n python%{python3_pkgversion}-%{srcname}
Provides command line tools for working with catkin


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build

%make_build -C docs html man SPHINXBUILD=sphinx-build-%{python3_version}
rm docs/_build/html/.buildinfo


%install
%py3_install

install -p -m0644 -D docs/_build/man/%{srcname}.1 %{buildroot}%{_mandir}/man1/%{srcname}.1

# Fix the install location of the bash completion scripts
install -d %{buildroot}%{_datadir}/bash-completion/completions/
mv %{buildroot}/etc/bash_completion.d/%{srcname}-completion.bash %{buildroot}%{_datadir}/bash-completion/completions/catkin


%check
# Many tests require catkin itself, which isn't packaged in Fedora
%global exclude_tests \\\
  -e 'test_build_*' \\\
  -e 'test_catkin_build_with_*' \\\
  -e 'test_cmake_args' \\\
  -e 'test_code_format' \\\
  -e 'test_init_local_empty_src' \\\
  -e 'test_profile_*' \\\
  %{nil}

PYTHONPATH=%{buildroot}%{python3_sitelib} \
  PATH=%{buildroot}%{_bindir}:$PATH \
  nosetests-%{python3_version} -w tests %{exclude_tests}


%files doc
%license LICENSE
%doc docs/_build/html

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{_bindir}/catkin
%{_mandir}/man1/%{srcname}.1.*
%{_datadir}/zsh/site-functions/_catkin
%{_datadir}/bash-completion/


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 08 2020 Scott K Logan <logans@cottsay.net> - 0.6.1-1
- Update to 0.6.1 (rhbz#1843716)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.5-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.5-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.5-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 02 2019 Scott K Logan <logans@cottsay.net> - 0.4.5-1
- Update to 0.4.5
- Use python3 macros
- Make dependency generation compatible with EPEL
- Make doc subpackage a weaker dependency

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.4-9
- Enable python dependency generator

* Wed Jan 09 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.4-8
- Subpackage python2-catkin_tools has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Wed Aug 01 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.4-7
- Only one /usr/bin/catkin

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.4-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 09 2017 Rich Mattes <richmattes@gmail.com> - 0.4.4-1
- Update to release 0.4.4 (rhbz#1411058)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-2
- Rebuild for Python 3.6

* Sun Sep 18 2016 Scott K Logan <logans@cottsay.net> 0.4.2-1
- Update to release 0.4.2 (rhbz#1328284)
- Update to latest packaging guidelines
- Split off doc package

* Sun Sep 18 2016 Scott K Logan <logans@cottsay.net> - 0.3.1-3
- Fix bash completion installation location (rhbz#1375604)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Feb 21 2016 Rich Mattes <richmattes@gmail.com> - 0.3.1-1
- Update to release 0.3.1 (rhbz#1293318)
- Fix rawhide FTBFS (rhbz#1307897)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 02 2015 Scott K Logan <logans@cottsay.net> - 0.3.0-3
- Add upstream patch for newer versions of flake8

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sat Jul 04 2015 Scott K Logan <logans@cottsay.net> - 0.3.0-1
- Update to 0.3.0
- Add Requires: cmake make (RHBZ#1227816)
- Update to latest packaging guidelines

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 22 2014 Scott K Logan <logans@cottsay.net> - 0.2.0-2
- Add upstream terminal width patch to enable tests

* Sat Oct 18 2014 Scott K Logan <logans@cottsay.net> - 0.2.0-1
- Update to 0.2.0
- Add python3 package
- Exclude new test_build_* tests because they require catkin
- Disable buildfarm testing (https://github.com/catkin/catkin_tools/issues/122)

* Tue Jun 10 2014 Scott K Logan <logans@cottsay.net> - 0.1.0-1
- Initial package
