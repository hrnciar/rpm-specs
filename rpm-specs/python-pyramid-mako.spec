%global modname pyramid_mako
%global srcname pyramid-mako

Name:               python-%{srcname}
Version:            1.0.2
Release:            16%{?dist}
Summary:            Mako template bindings for the Pyramid web framework

License:            BSD
URL:                http://pypi.python.org/pypi/%{modname}
Source0:            https://files.pythonhosted.org/packages/source/p/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-pyramid

# For the test suite
BuildRequires:      python3-webtest
BuildRequires:      python3-nose
BuildRequires:      python3-mako

%description
These are bindings for the Mako templating system for the Pyramid web
framework.


%package -n python3-%{srcname}
Summary:    %{summary}
Requires:   python3-mako
Requires:   python3-pyramid
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
These are bindings for the Mako templating system for the Pyramid web
framework.


%prep
%setup -q -n %{modname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info
awk 'NR==3{print "import __main__; __main__.__requires__ = __requires__ = [\"WebTest>=1.3.1\", \"WebOb>=1.3.1\", \"zope.interface>=3.8.0\", \"Mako>=0.3.6\"]; import pkg_resources"}3' setup.py > tempfile
mv tempfile setup.py

# Remove lingering .gitignore file and hidden static folder
rm docs/.gitignore
rm -rf docs/.static


%build
%py3_build


%install
%py3_install


%check
%{__python3} setup.py test


%files -n python3-%{srcname}
%doc README.rst COPYRIGHT.txt CONTRIBUTORS.txt CHANGES.txt docs/
%license LICENSE.txt
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}*


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-15
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 22 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-12
- Subpackage python2-pyramid-mako has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-7
- Rebuilt for Python 3.7

* Tue Feb 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.2-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-2
- Rebuild for Python 3.6

* Thu Aug 18 2016 Dominika Krejci <dkrejci@redhat.com> - 1.0.2-1
- Update to 1.0.2
- Add Python 3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0a3-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0a3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 14 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 1.0a3-6
- Fix WebOb dependency for EPEL (#1270297)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0a3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Nov 13 2014 Ralph Bean <rbean@redhat.com> - 1.0a3-4
- Fix rhel conditional.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0a3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 27 2014 Ralph Bean <rbean@redhat.com> - 1.0a3-2
- Fix test deps for el6.

* Thu Mar 27 2014 Ralph Bean <rbean@redhat.com> - 1.0a3-1
- Latest upstream includes a fixed test suite.
- Reenabled the test suite.

* Thu Mar 20 2014 Ralph Bean <rbean@redhat.com> - 1.0a2-2
- Remove hidden folder as per review.

* Wed Mar 19 2014 Ralph Bean <rbean@redhat.com> - 1.0a2-1
- Initial packaging for Fedora
