%global pkgname CoverageTestRunner
%global prjname coverage-test-runner

Name:           python-%{prjname}
Version:        1.15
Release:        9%{?dist}
Summary:        Python module for enforcing code coverage completeness

License:        GPLv3+
URL:            http://liw.fi/%{prjname}/
Source0:        http://code.liw.fi/debian/pool/main/p/%{name}/%{name}_%{version}.orig.tar.xz

BuildArch:      noarch

%global _description\
CoverageTestRunner is a Python module for running unit tests and\
failing them if the unit test module does not exercise all statements\
in the module it tests.\
\
For example, unit tests in module foo_tests.py are supposed to test\
everything in the foo.py module, and if they don't, it's a bug in the\
test coverage. It does not matter if other tests happen to test the\
missing parts. The unit tests for the module should test everything in\
that module.\


%description %_description

%package -n python3-%{prjname}
Summary:        %summary
BuildRequires:  python3-devel
BuildRequires:  python3-coverage
Requires:       python3-coverage
%{?python_provide:%python_provide python3-%{prjname}}

%description -n python3-%{prjname} %_description

%prep
%autosetup

%build
%py3_build

%install
%py3_install

%check
#make check
%{__python3} CoverageTestRunner.py subdir --ignore-missing-from=test-excluded
rm -rf .coverage

%files -n python3-%{prjname}
%license COPYING
%doc NEWS README
%{python3_sitelib}/*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.15-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.15-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.15-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Miro Hrončok <mhroncok@redhat.com> - 1.15-3
- Subpackage python2-coverage-test-runner has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 20 2019 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.15-1
- Update to 1.15 based on PR by Jan Beran <jberan@redhat.com>
  https://src.fedoraproject.org/rpms/python-coverage-test-runner/pull-request/3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 25 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.11-6
- Reference python2-coverage with python2 prefix

* Tue Aug 22 2017 Iryna Shcherbina <ishcherb@redhat.com> - 1.11-5
- Add a build-time dependency on python2-devel and modernize spec file

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.11-4
- Python 2 binary package renamed to python2-coverage-test-runner
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan  9 2017 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.11-1
- Update to 1.11

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 19 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.10-5
- Adjust for removal of deprecated top-level module functions in coverage-4.0a6

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Apr 20 2013 Michel Salim <salimma@fedoraproject.org> - 1.10-1
- Update to 1.10

* Mon Feb 25 2013 Michel Salim <salimma@fedoraproject.org> - 1.9-1
- Update to 1.9

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun  4 2012 Michel Salim <salimma@fedoraproject.org> - 1.8-1
- Update to 1.8
- Drop unneeded conditional declaration of %%{python_sitelib}

* Sun Jun  3 2012 Michel Salim <salimma@fedoraproject.org> - 1.0-1
- Initial package
