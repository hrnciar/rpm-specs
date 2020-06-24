%global pkgname cliapp

Name:           python-%{pkgname}
Version:        1.20180121
Release:        7%{?dist}
Summary:        Python framework for Unix command line programs

License:        GPLv2+
URL:            http://liw.fi/%{pkgname}/
Source0:        http://code.liw.fi/debian/pool/main/p/%{name}/%{name}_%{version}.orig.tar.xz

BuildArch:      noarch

%global _description\
cliapp is a Python framework for Unix-like command line programs. It\
contains the typical stuff such programs need to do, such as parsing\
the command line for options, and iterating over input files.\

%description %_description


%package -n python3-%{pkgname}
Summary:        %summary
BuildRequires:  python3-devel
BuildRequires:  python3-pyyaml
BuildRequires:  python3-coverage-test-runner
Requires:       python3-pyyaml
%{?python_provide:%python_provide python3-%{pkgname}}

%description -n python3-%{pkgname} %_description


%prep
%autosetup -p1


%build
%py3_build


%install
%py3_install


%check
# CoverageTestRunner trips up on build directory;
# since we've already done the install phase, remove it first
rm -rf build
%{__python3} -m CoverageTestRunner --ignore-missing --ignore-coverage
rm -rf .coverage


%files -n python3-%{pkgname}
%license COPYING
%doc NEWS README
%{_mandir}/man5/cliapp.5*
%{python3_sitelib}/*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.20180121-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20180121-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 18 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.20180121-5
- Do not fail tests because of incomplete coverage (#1737270)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.20180121-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20180121-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Miro Hrončok <mhroncok@redhat.com> - 1.20180121-2
- Subpackage python2-cliapp has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sun Feb  3 2019 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.20180121-1
- Update to 1.20180121

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20160724-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20160724-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 11 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.20160724-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20160724-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 25 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.20160724-6
- Reference more packages with python2 prefix

* Tue Aug 22 2017 Iryna Shcherbina <ishcherb@redhat.com> - 1.20160724-5
- Add a build-time dependency on python2-devel and modernize spec file

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.20160724-4
- Python 2 binary package renamed to python2-cliapp
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20160724-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20160724-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan  9 2017 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.20160724-1
- Update to 1.20160724

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20160316-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jun  6 2016 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.20160316-1
- Update to 1.20160316

* Sun Feb 14 2016 Michel Salim <salimma@fedoraproject.org> - 1.20160109-1
- Update to 1.20160109

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.20150829-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep  3 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.20150829-1
- Update to 1.20150829

* Sun Jul 19 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.20150701-2
- Adjust for python-coverage-4.0a6 no longer generating .coverage file

* Sun Jul 19 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.20150701-1
- Update to 1.20150701

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20140719-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec  2 2014 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.20140719-1
- Update to 1.20140719

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20130808-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Sep 27 2013 Michel Salim <salimma@fedoraproject.org> - 1.20130808-1
- Update to 1.20130808

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20130613-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 14 2013 Michel Salim <salimma@fedoraproject.org> - 1.20130613-1
- Update to 1.20130613

* Tue Apr 30 2013 Michel Salim <salimma@fedoraproject.org> - 1.20130424-1
- Update to 1.20130424

* Fri Mar 15 2013 Michel Salim <salimma@fedoraproject.org> - 1.20130313-1
- Update to 1.20130313

* Mon Feb 25 2013 Michel Salim <salimma@fedoraproject.org> - 1.20121216-1
- Update to 1.20121216

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20120630-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20120630-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul  3 2012 Michel Salim <salimma@fedoraproject.org> - 1.20120630-1
- Update to 1.20120630

* Tue Jun  5 2012 Michel Salim <salimma@fedoraproject.org> - 0.29-2
- Remove unneeded %%{python_sitelib} declaration
- Make file listing more specific
- Remove build directory before running coverage test

* Sun Jun  3 2012 Michel Salim <salimma@fedoraproject.org> - 0.29-1
- Initial package
