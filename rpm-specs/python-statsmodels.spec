%global srcname statsmodels
%global sum Statistics in Python

Name:           python-%{srcname}
Version:        0.11.1
Release:        2%{?dist}
Summary:        %{sum}

# Package is licensed under BSD (3 clauses)
# except the following files in Public Domain
# statsmodels/datasets/anes96/data.py
# statsmodels/datasets/co2/data.py
# statsmodels/datasets/elec_equip/data.py
# statsmodels/datasets/elnino/data.py
# statsmodels/datasets/engel/data.py
# statsmodels/datasets/grunfeld/data.py
# statsmodels/datasets/longley/data.py
# statsmodels/datasets/macrodata/data.py
# statsmodels/datasets/modechoice/data.py
# statsmodels/datasets/nile/data.py
# statsmodels/datasets/randhie/data.py
# statsmodels/datasets/stackloss/data.py
# statsmodels/datasets/strikes/data.py
# statsmodels/datasets/sunspots/data.py

License:        BSD and Public Domain
URL:            https://www.statsmodels.org/
Source0:        %{pypi_source}

BuildRequires:  gcc
BuildRequires:  python3-devel
# For testing
BuildRequires:  xorg-x11-server-Xvfb
# For documentation
BuildRequires:  graphviz

%description
statsmodels is a Python module that provides classes and functions for the
estimation of many different statistical models, as well as for conducting
statistical tests, and statistical data exploration. An extensive list of
result statistics are available for each estimator. The results are tested
against existing statistical packages to ensure that they are correct.

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires: python3-Cython
BuildRequires: python3-numpy
BuildRequires: python3-scipy 
BuildRequires: python3-patsy
BuildRequires: python3-pandas
# For testing
BuildRequires: python3-matplotlib
BuildRequires: python3-matplotlib-tk
BuildRequires: python3-pytest

Requires: python3-numpy
Requires: python3-scipy 
Requires: python3-patsy
Requires: python3-pandas

%description -n python3-%{srcname}
statsmodels is a Python module that provides classes and functions for the
estimation of many different statistical models, as well as for conducting
statistical tests, and statistical data exploration. An extensive list of
result statistics are available for each estimator. The results are tested
against existing statistical packages to ensure that they are correct.

%package -n python3-%{srcname}-doc
Summary: Documentation for %{srcname}, includes full API docs
BuildArch: noarch

BuildRequires: python3-sphinx
BuildRequires: python3-numpydoc
BuildRequires: python3-ipython-sphinx
BuildRequires: python3-matplotlib

%description -n python3-%{srcname}-doc
This package contains the full API documentation for python3-%{srcname}.

%prep
%autosetup -n %{srcname}-%{version} -p1
find . -type f -exec chmod -x {} \;

pushd statsmodels
# Copy license files
cp -a stats/libqsturng/LICENSE.txt ../LICENSE.libqsturng.txt

# remove shebangs
#sed -i -e "1d" regression/quantile_regression.py

popd

%build
%py3_build

##%{__python3} setup.py build_sphinx
##rm -f build/sphinx/html/.buildinfo

%install
%py3_install

%check
# False matplotlibrc
mkdir -p matplotlib
touch matplotlib/matplotlibrc
export XDG_CONFIG_HOME=`pwd`
pushd %{buildroot}/%{python3_sitearch}
 xvfb-run pytest-%{python3_version} %{srcname} || :
popd

%files -n python3-%{srcname}
%license LICENSE.txt LICENSE.libqsturng.txt
%doc COPYRIGHTS.txt README_l1.txt README.rst
%{python3_sitearch}/statsmodels
%{python3_sitearch}/statsmodels-*-py*.egg-info
%exclude %{python3_sitearch}/statsmodels/LICENSE.txt

%files -n python3-%{srcname}-doc
%license LICENSE.txt LICENSE.libqsturng.txt
## %doc build/sphinx/html

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.11.1-2
- Rebuilt for Python 3.9

* Sun Mar 01 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.11.1
- New upstream source (0.11.1)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.11.0
- New upstream source (0.11.0)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.1-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 31 2019 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 0.10.1-1
- Update to 0.10.1 (#1742125)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 0.10.0
- New upstream source (0.10.0)

* Fri Feb 08 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 0.9.0-5
- Disable docs generation (bz #1637994)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Christian Dersch <lupinix@fedoraproject.org> - 0.9.0-3
- BuildRequires: gcc

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Christian Dersch <lupinix@mailbox.org> - 0.9.0-1
- new version

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-6
- Rebuilt for Python 3.7

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8.0-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Sergio Pascual <sergiopr@fedoraproject.org> - 0.8.0-1
- New upstream source (0.8.0)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-8
- Rebuild for Python 3.6

* Thu Sep 01 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 0.6.1-7
- Add requirements, were missing

* Thu Apr 21 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 0.6.1-6
- Use new style macros
- Redone patches

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 25 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.6.1-4
- Fix build with new pandas and numpy

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec 05 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.6.1-1
- New upstream source, bugfix (0.6.1)

* Mon Nov 17 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.6.0-1
- New upstream source (0.6.0)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 17 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.5.0-11
- Enabled documentation

* Thu Jun 12 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.5.0-10
- Documentation broken due to IPython incompatibility, disable for the moment
- Examples moved out installed package
- Disabled tests for the moment

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 24 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.5.0-8
- Enable tests in arm
- Disable failling test in i686
- Disable failling test in arm

* Tue Jan 21 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.5.0-7
- Disable tests in arm

* Mon Jan 20 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.5.0-6
- Add README.txt and COPYING from datasets to doc

* Sun Jan 19 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.5.0-5
- Added url for bug report of removed tests
- Minor fixes in the spec
- Included other LICENSE.txt in the documentation

* Wed Jan 15 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.5.0-4
- Use an empty matplotlibrc for tests

* Wed Jan 15 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.5.0-3
- Patch those tests that fail

* Fri Jan 10 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.5.0-2
- Add ipython to build documentation

* Fri Jan 10 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 0.5.0-1
- Initial spec

