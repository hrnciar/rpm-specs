%global srcname patsy
%global summary Describing statistical models in Python using symbolic formulas

%global common_description                                             \
A Python package for describing statistical models and for building    \
design matrices. It is closely inspired by and compatible with         \
the 'formula' mini-language used in R and S.

Name: python-%{srcname}
Version: 0.5.1
Release: 10%{?dist}
Summary: %{summary}
# All code is under BSD except patsy.compat that is under Python
# See LICENSE.txt for details
License: BSD and Python

URL: https://github.com/pydata/patsy
Source0: https://pypi.io/packages/source/p/patsy/patsy-%{version}.tar.gz
Patch0: patsy-intersphinx.patch
Patch1: patsy-error-doc.patch
# https://github.com/pydata/patsy/issues/143
Patch2: patsy-print-doc.patch
Patch3: patsy-python39.patch

BuildArch: noarch
BuildRequires: python3-devel

%description
%{common_description}

%package -n python3-%{srcname}
Summary: %{summary}
BuildRequires: python3-nose
BuildRequires: python3-six
BuildRequires: python3-numpy
# For the docs
BuildRequires: python3-sphinx
BuildRequires: python3-ipython-sphinx
BuildRequires: python3-pandas
BuildRequires: python3-docs
BuildRequires: python3-numpy-doc
BuildRequires: texlive-latex
BuildRequires: texlive-ucs texlive-amscls
# This should be required by python3-ipython-sphinx
BuildRequires: python3-matplotlib 
# For splines
BuildRequires: python3-scipy  

Requires: python3-six
Requires: python3-numpy
# For splines
Recommends: python3-scipy

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{common_description}

%package -n python3-%{srcname}-doc
Summary: Documentation for python3-%{srcname}, includes full API docs
BuildArch: noarch

%description -n python3-%{srcname}-doc
This package contains the full API documentation for python3-%{srcname}.


%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py3_build

pushd doc
  export PYTHONPATH=`readlink -f ../build/lib`
  make html SPHINXBUILD=sphinx-build-%{python3_version}
popd

%install
%py3_install

%check
pushd %{buildroot}/%{python3_sitelib}
nosetests-%{python3_version} patsy
popd

%files -n python3-%{srcname}
%doc README.rst TODO
%license LICENSE.txt
%{python3_sitelib}/patsy*

%files -n python3-%{srcname}-doc
%doc README.rst TODO doc/_build/html
%license LICENSE.txt

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.5.1-8
- Patch a python39 problem (bz #1794275)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 0.5.1-4
- Patch a "print" command in docs

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 20 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 0.5.1-2
- Add latex for equations in docs

* Mon Nov 12 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 0.5.1-1
- New upstream source (0.5.1)
- Load intersphinx object for python and numpy

* Sat Oct 06 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 0.5.0-5
- Build docs with python3

* Fri Oct 05 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 0.5.0-4
- Drop python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-2
- Rebuilt for Python 3.7

* Mon Jun 04 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 0.5.0-1
- New upstream source (0.5.0)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.1-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-5
- Rebuild for Python 3.6

* Mon Oct 17 2016 Sergio Pascual <sergio.pasra@gmail.com> - 0.4.1-4
- Refactored spec
- Remove pandas dep, it's circular
- Recommend scipy, not require it

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 17 2015 Sergio Pascual <sergio.pasra@gmail.com> - 0.4.1-1
- New upstream source (0.4.1)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Sep 02 2015 Sergio Pascual <sergio.pasra@gmail.com> - 0.4.0-1
- New upstream source (0.4.0)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jul 21 2014 Sergio Pascual <sergio.pasra@gmail.com> - 0.3.0-1
- New upstream source (0.3.0)
- Removed patches

* Tue Jun 17 2014 Sergio Pascual <sergio.pasra@gmail.com> - 0.2.1-6
- Doc generation enabled, patch from upstream

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun 02 2014 Sergio Pascual <sergio.pasra@gmail.com> - 0.2.1-4
- Doc generation broken due to new ipython, disabled for the moment

* Fri Apr 04 2014 Sergio Pascual <sergio.pasra@gmail.com> - 0.2.1-3
- Enable pandas support in python3-patsy

* Sat Jan 11 2014 Sergio Pascual <sergio.pasra@gmail.com> - 0.2.1-2
- Split docs in a subpackage
- License is BSD and Python

* Fri Dec 13 2013 Sergio Pascual <sergio.pasra@gmail.com> - 0.2.1-1
- Initial specfile

