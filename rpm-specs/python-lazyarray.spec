# https://fedoraproject.org/wiki/Packaging:DistTag?rd=Packaging/DistTag#Conditionals
# http://rpm.org/user_doc/conditional_builds.html
%if 0%{?fedora} >= 30
# disabled by default
%bcond_with py2
%else
%bcond_without py2
%endif

# Test fails. Issue filed:
# https://bitbucket.org/apdavison/lazyarray/issues/6/test-failure
%bcond_with tests

%global desc %{expand: \
lazyarray is a Python package that provides a lazily-evaluated numerical array
class, ``larray``, based on and compatible with NumPy arrays.

Lazy evaluation means that any operations on the array (potentially including
array construction) are not performed immediately, but are delayed until
evaluation is specifically requested. Evaluation of only parts of the array is
also possible.

Use of an ``larray`` can potentially save considerable computation time and
memory in cases where:

* arrays are used conditionally (i.e. there are cases in which the array is
  never used)
* only parts of an array are used (for example in distributed computation,
  in which each MPI node operates on a subset of the elements of the array)

Documentation: http://lazyarray.readthedocs.org}

%global pypi_name     lazyarray

Name:       python-%{pypi_name}
Version:    0.3.2
Release:    8%{?dist}
Summary:    A lazily-evaluated numerical array class

License:    BSD
URL:        https://github.com/NeuralEnsemble/lazyarray/
Source0:    https://pypi.python.org/packages/source/l/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# https://github.com/NeuralEnsemble/lazyarray/raw/master/doc/conf.py
# Not included in the pypi release for some reason
Source1:    lazyarray-doc-conf.py
Source2:    Makefile.lazyarray

BuildArch:      noarch

%{?python_enable_dependency_generator}

%description
%{desc}

%package docs
Summary:    Documentation for %{name}
BuildArch:  noarch

%description docs
This package contains generated HTML documentation for %{name}.


%package -n python3-%{pypi_name}
Summary:    A lazily-evaluated numerical array class
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist nose}
BuildRequires:  %{py3_dist sphinx}
Requires:   %{py3_dist numpy}

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}


%if %{with py2}
%package -n python2-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  %{py2_dist setuptools}
BuildRequires:  %{py2_dist numpy}
BuildRequires:  %{py2_dist nose}
Requires:   %{py2_dist numpy}

%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
%{desc}

%endif

%prep
%autosetup -n %{pypi_name}-%{version}
cp %{SOURCE1} doc/conf.py
cp %{SOURCE2} doc/Makefile

%build
%py3_build

%if %{with py2}
%py2_build
%endif

# only needs to be built once
pushd doc
    make html
    rm _build/html/.buildinfo

    pushd _build/html/
        iconv -f iso8859-1 -t utf-8 objects.inv > objects.inv.conv && mv -f objects.inv.conv objects.inv
    popd
popd
sed -i 's/\r$//' doc/_build/html/_static/jquery.js


%install
%if %{with py2}
%py2_install
%endif

%py3_install


%check
%if %{with tests}
%if %{with py2}
nosetests-%{python2_version}
%endif
nosetests-%{python3_version}
%endif

%files docs
%license LICENSE
%doc doc/_build/html

%files -n python3-%{pypi_name}
%license LICENSE
%doc changelog.txt README.rst
%{python3_sitelib}/%{pypi_name}-%{version}-py3.?.egg-info
%{python3_sitelib}/__pycache__/%{pypi_name}*
%{python3_sitelib}/%{pypi_name}*.py

%if %{with py2}
%files -n python2-%{pypi_name}
%license LICENSE
%doc changelog.txt README.rst
%{python2_sitelib}/%{pypi_name}-%{version}-py2.?.egg-info
%{python2_sitelib}/%{pypi_name}*.py*
%endif

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 06 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.2-1
- Update to latest version
- Use conditional to provide py2 builds when required
- Remove duplicated doc package
- minor cosmetic spec tweaks

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.8-13
- Subpackage python2-lazyarray has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.8-11
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.8-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.8-8
- Python 2 binary package renamed to python2-lazyarray
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.8-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Mar 08 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.2.8-3
- Provide python2 package

* Tue Mar 08 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.2.8-2
- Update doc config
- Disable test - issue filed upstream

* Tue Mar 08 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.2.8-1
- Update to latest upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 08 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.2.7-3
- Correct nosetest3* usage

* Wed Oct 08 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.2.7-2
- Make nosetest for py3 a wildcard

* Wed Oct 08 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.2.7-1
- Split documentation to separate sub package

* Tue Oct 07 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.2.7-1
- Added tests
- Corrected file lists
- Added docs

* Tue Oct 07 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.2.7-1
- Initial rpm build
