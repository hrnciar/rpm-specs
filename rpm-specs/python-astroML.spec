%global srcname astroML

Name:           python-%{srcname}
Version:        0.4.1
Release:        3%{?dist}
Summary:        Python tools for machine learning and data mining in Astronomy

License:        BSD
URL:            http://www.astroml.org/
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-astropy
BuildRequires:  python3-devel
BuildRequires:  python3-matplotlib
BuildRequires:  python3-pytest-astropy
BuildRequires:  python3-numpy
BuildRequires:  python3-scikit-learn
BuildRequires:  python3-setuptools
BuildRequires:  python3-scipy

%global _description\
AstroML is a Python module for machine learning and data mining built on\
numpy, scipy, scikit-learn, and matplotlib, and distributed under the\
3-clause BSD license. It contains a growing library of statistical and\
machine learning routines for analyzing astronomical data in python,\
loaders for several open astronomical datasets, and a large suite of\
examples of analyzing and visualizing astronomical datasets.\


%description %_description

%package -n python3-%{srcname}
Summary:        Python tools for machine learning and data mining in Astronomy

Requires:       python3-numpy
Requires:       python3-astropy
Requires:       python3-matplotlib
Requires:       python3-scikit-learn
Requires:       python3-scipy
Recommends:     python3-healpy
Provides:       python3-astroML-addons = %{version}-%{release}
Obsoletes:      python3-astroML-addons < 0.4-1
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
AstroML is a Python module for machine learning and data mining built on
numpy, scipy, scikit-learn, and matplotlib, and distributed under the
3-clause BSD license. It contains a growing library of statistical and
machine learning routines for analyzing astronomical data in python,
loaders for several open astronomical datasets, and a large suite of
examples of analyzing and visualizing astronomical datasets.

%package doc
Summary:        Docs and examples for the %{srcname} package

%description doc
Documentation and examples for %{srcname}.


%prep
%setup -qn %{srcname}-%{version}
find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'


%build
%py3_build

%install
%py3_install

%check
# Disabled tests as they do not work properly right now :(
#%{__python3} setup.py test

%files doc
%license LICENSE.rst
%doc CHANGES.rst README.rst examples

%files -n python3-%{srcname}
%license LICENSE.rst
%doc CHANGES.rst README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 27 2019 Christian Dersch <lupinix@fedoraproject.org> - 0.4.1-1
- new version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3-25
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Christian Dersch <lupinix@fedoraproject.org> - 0.3-22
- drop python2 subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3-20
- Rebuilt for Python 3.7

* Wed Feb 14 2018 Christian Dersch <lupinix@mailbox.org> - 0.3-19
- rebuilt

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3-17
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Oct 17 2017 Christian Dersch <lupinix@mailbox.org> - 0.3-16
- Recommend healpy, an optional dependency of astroML

* Mon Aug 21 2017 Christian Dersch <lupinix@mailbox.org> - 0.3-15
- Fixed Python 2 renaming

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3-14
- Python 2 binary package renamed to python2-astroml
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3-11
- Rebuild for Python 3.6

* Mon Sep 26 2016 Dominik Mierzejewski <rpm@greysector.net> - 0.3-10
- rebuilt for matplotlib-2.0.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Mar 30 2016 Björn Esser <fedora@besser82.io> - 0.3-8
- Require python2-scikit-learn

* Fri Mar 25 2016 Christian Dersch <lupinix@mailbox.org> - 0.3-7
- rebuilt

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 25 2015 Christian Dersch <lupinix@mailbox.org> - 0.3-5
- Rebuilt for updates in Python 3.5

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 24 2015 Christian Dersch <chrisdersch@gmail.com> - 0.3-2
- small spec fixes

* Tue Feb 24 2015 Christian Dersch <chrisdersch@gmail.com> - 0.3-1
- new upstream release 0.3
- initial Python 3 support
- disabled tests temporarily

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 17 2014 Christian Dersch <chrisdersch@gmail.com> - 0.2-2
- fixed spec to match packaging guidelines

* Mon Feb 24 2014 Christian Dersch <chrisdersch@gmail.com> - 0.2-1
- upgrade to version 0.2, addons is now a seperate package (upstream change)

* Thu Oct 17 2013 Christian Dersch <chrisdersch@gmail.com> - 0.1.2-2
- fixed spec to match packaging guidelines

* Thu Oct 10 2013 Christian Dersch <chrisdersch@gmail.com> - 0.1.2-1
- initial spec
