%if 0%{?fedora} || 0%{?rhel} >= 8
%global         py2readelf %{nil}
%global         py3readelf %{_bindir}/pyreadelf
%global         pyreadelf pyreadelf-3
%else
%global         py2readelf %{_bindir}/pyreadelf
%global         py3readelf %{nil}
%global         pyreadelf pyreadelf-2
%endif

%if 0%{?fedora} && 0%{?fedora} < 32
%global         with_python2 1
%endif

%if 0%{?rhel} && 0%{?rhel} < 8
%global         with_python2 1
%endif

%if 0%{?fedora} || 0%{?rhel} >= 7
%global         with_python3 1
%endif

# main package is archful to run tests everywhere but produces noarch packages
%global         debug_package %{nil}

Summary:        Pure-Python library for parsing and analyzing ELF files
Name:           pyelftools
Version:        0.26
Release:        3%{?dist}
License:        Public Domain
URL:            https://github.com/eliben/pyelftools
# https://github.com/eliben/pyelftools/issues/260
#Source0:        https://files.pythonhosted.org/packages/source/p/pyelftools/pyelftools-%{version}.tar.gz
Source0:        https://github.com/eliben/pyelftools/archive/v%{version}/%{name}-%{version}.tar.gz
%global _description \
Pure-Python library for parsing and analyzing ELF files\
and DWARF debugging information.
%description   %_description

%if 0%{?with_python2}
%package     -n python2-%{name}
Summary:        %{summary}
# https://github.com/eliben/pyelftools/issues/180
Provides:	bundled(python2-construct) = 2.6
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildArch:      noarch
%{?python_provide:%python_provide python2-%{name}}
# Remove before F30
%description -n python2-%{name} %_description
%endif # with_python2

%if 0%{?with_python3}
%package     -n python3-%{name}
Summary:	%{summary}
# https://github.com/eliben/pyelftools/issues/180
Provides:	bundled(python3-construct) = 2.6
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildArch:      noarch
%{?python_provide:%python_provide python3-%{name}}
%description -n python3-%{name} %_description
%endif

%prep
%setup -q

%build
%if 0%{?with_python2}
%{py2_build}
%endif
%if 0%{?with_python3}
%{py3_build}
%endif

%install
%if 0%{?with_python2}
%{py2_install}
pushd %{buildroot}%{_bindir}
mv readelf.py pyreadelf-%{python2_version}
ln -s pyreadelf-%{python2_version} pyreadelf-2
popd
%endif
%if 0%{?with_python3}
%{py3_install}
pushd %{buildroot}%{_bindir}
mv readelf.py pyreadelf-%{python3_version}
ln -s pyreadelf-%{python3_version} pyreadelf-3
popd
%endif
pushd %{buildroot}%{_bindir}
ln -s %{pyreadelf} pyreadelf
popd

%check
%if 0%{?with_python2}
%{__python2} test/run_all_unittests.py
%{__python2} test/run_examples_test.py
%ifarch x86_64
# tests may fail because of differences in output-formatting
# from binutils' readelf.  See:
# https://github.com/eliben/pyelftools/wiki/Hacking-guide#tests
%{__python2} test/run_readelf_tests.py || :
%endif
%endif
%if 0%{?with_python3}
%{__python3} test/run_all_unittests.py
%{__python3} test/run_examples_test.py
%ifarch x86_64
# ditto
%{__python3} test/run_readelf_tests.py || :
%endif
%endif

%if 0%{?with_python2}
%files -n python2-%{name}
%license LICENSE
%doc CHANGES
%{py2readelf}
%{_bindir}/pyreadelf-%{python2_version}
%{_bindir}/pyreadelf-2
%{python2_sitelib}/elftools
%{python2_sitelib}/pyelftools-*.egg-info
%endif

%if 0%{?with_python3}
%files -n python3-%{name}
%license LICENSE
%doc CHANGES
%{py3readelf}
%{_bindir}/pyreadelf-%{python3_version}
%{_bindir}/pyreadelf-3
%{python3_sitelib}/elftools
%{python3_sitelib}/pyelftools-*.egg-info
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.26-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 2019 Dominik Mierzejewski <rpm@greysector.net> - 0.26-1
- update to 0.26 (#1780153)
- make main package archful to run tests on all arches
  (pythonN-pyelftools subpackages are still noarch)
- run readelf tests on x86_64 only for now
- rename binaries to conform to Python packaging guidelines
- enable python3 subpackage for EPEL7
- declare bundled old construct module instead of needlessly requiring it

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.25-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.25-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Terje Rosten <terje.rosten@ntnu.no> - 0.25-2
- Still support Python 2 on Fedora 31

* Sun May 05 2019 Terje Rosten <terje.rosten@ntnu.no> - 0.25-1
- 0.25
- Use bundled construct as construct 2.9 is incompatible
- Drop Python 2 stuff on el8 and Python 31 or newer

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.24-2
- Rebuilt for Python 3.7

* Sun Jun 17 2018 Terje Rosten <terje.rosten@ntnu.no> - 0.24-1
- 0.24
- some clean up
- remove naked provide for Fedora 29 and later
- switch to Python 3 for pyreadelf for Fedora 29 and later

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.22-0.16.git20130619.a1d9681
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-0.15.git20130619.a1d9681
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.22-0.14.git20130619.a1d9681
- Python 2 binary package renamed to python2-pyelftools
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-0.13.git20130619.a1d9681
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-0.12.git20130619.a1d9681
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-0.11.git20130619.a1d9681
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.22-0.10.git20130619.a1d9681
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-0.9.git20130619.a1d9681
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-0.8.git20130619.a1d9681
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-0.7.git20130619.a1d9681
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-0.6.git20130619.a1d9681
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-0.5.git20130619.a1d9681
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-0.4.git20130619.a1d9681
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 0.22-0.3.git20130619.a1d9681
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Oct 02 2013 Björn Esser <bjoern.esser@gmail.com> - 0.22-0.2.git20130619.a1d9681
- adaptions for new Python-guidelines

* Fri Aug 16 2013 Björn Esser <bjoern.esser@gmail.com> - 0.22-0.1.git20130619.a1d9681
- update to latest pre-release git snapshot
- add python3-package
- build on all arches to get some conclusion from testsuite,
  but create noarch pkgs

* Sat Jun 08 2013 Terje Rosten <terje.rosten@ntnu.no> - 0.21-2
- Remove bundled construct lib

* Thu May 09 2013 Terje Rosten <terje.rosten@ntnu.no> - 0.21-1
- 0.21
- Run test
- Updated source url
- Drop defattr

* Wed Jun 06 2012 Kushal Das <kushal@fedoraproject.org> 0.20-1
- Intial package (#829676)
