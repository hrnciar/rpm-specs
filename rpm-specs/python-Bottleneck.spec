%global upname Bottleneck

Name:		python-%{upname}
Version:	1.2.1
Release:	16%{?dist}
Summary:	Collection of fast NumPy array functions written in Cython

License:	BSD
URL:		https://pypi.org/project/Bottleneck/
Source0:	https://files.pythonhosted.org/packages/source/B/%{upname}/%{upname}-%{version}.tar.gz

BuildRequires:	gcc

%description
%{name} is a collection of fast NumPy array functions
written in Cython.


%package doc
Summary:	Documentation files for %{name}

BuildArch:	noarch

%description doc
This package contains the HTML-docs for %{name}.


%package -n python3-%{upname}
Summary:	Collection of fast NumPy array functions written in Cython

BuildRequires:	python3-devel
BuildRequires:	python3-nose
BuildRequires:	python3-numpy
BuildRequires:	python3-numpydoc
BuildRequires:	python3-scipy
BuildRequires:	python3-setuptools
BuildRequires:	python3-sphinx

Requires:	python3-numpy%{?_isa}
Requires:	python3-scipy%{?_isa}

%{?python_provide:%python_provide python3-%{upname}}

%description -n python3-%{upname}
python3-%{upname} is a collection of fast NumPy array functions
written in Cython.


%prep
%autosetup -n %{upname}-%{version} -p 1
%{__rm} -fr .egg* *.egg*

# use numpydoc from the package instead
%{__rm} -f doc/sphinxext/numpydoc.py*

# Python 2 remark
%{__sed} -i 's/fid = file(/fid = open(/' doc/source/conf.py

%build
%py3_build


%install
%py3_install

# clean unneeded stuff
%{__rm} -rf %{buildroot}%{python3_sitearch}/bottleneck/src		\
	%{buildroot}%{python3_sitearch}/bottleneck/LICENSE

%{_fixperms} %{buildroot}/*

# Move installed files to temporary location.
%{__mkdir} -p tmp_inst
%{__cp} -fpr %{buildroot}/* tmp_inst

# Build the autodocs.
export PYTHONPATH="$(/bin/pwd)/tmp_inst/%{python3_sitearch}"
%{__mkdir} -p doc/source/_static
%{_bindir}/sphinx-build -b html doc/source doc/html
unset PYTHONPATH

# Clean unneeded stuff from docs.
%{__rm} -rf doc/html/{.buildinfo,.doctrees}


%check
pushd tmp_inst/%{python3_sitearch}
%{_bindir}/nosetests-%{python3_version} -vv
popd


%files doc
%license bottleneck/LICENSE
%doc README* RELEASE* doc/html


%files -n python3-%{upname}
%license bottleneck/LICENSE
%doc README* RELEASE*
%{python3_sitearch}/bottleneck
%{python3_sitearch}/%{upname}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-15
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct  4 2019 Orion Poplawski <orion@nwra.com> - 1.2.1-13
- Fix URL

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 28 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-9
- Subpackage python2-Bottleneck has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-6
- Rebuilt for Python 3.7
- Use numpydoc from our package to fix FTBFS (#1594555)

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.1-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 16 2017 Björn Esser <besser82@fedoraproject.org> - 1.2.1-1
- Updated to new upstream release (rhbz#1451146)

* Sun Apr 09 2017 Björn Esser <besser82@fedoraproject.org> - 1.2.0-1
- Updated to new upstream release (rhbz#1105817)
- Updated spec-file to recent guidelines

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-10
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 15 2015 Thomas Spura <tomspur@fedoraproject.org> - 0.6.0-7
- Use new python macros and add python2 subpackage

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Aug 21 2013 Björn Esser <bjoern.esser@gmail.com> - 0.6.0-1
- Initial rpm release (#999563)
