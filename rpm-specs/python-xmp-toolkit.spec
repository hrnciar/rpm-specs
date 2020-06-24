%global pypi_name python-xmp-toolkit
%global srcname xmp-toolkit

Name:           python-%{srcname}
Version:        2.0.1
Release:        8%{?dist}
Summary:        Python XMP Toolkit for working with metadata

License:        BSD
URL:            https://github.com/python-xmp-toolkit/python-xmp-toolkit
Source0:        %{pypi_source %{pypi_name}}
# https://github.com/python-xmp-toolkit/python-xmp-toolkit/pull/68
Patch0001:      2f94011ab789d1d2cabc41db7a708a19a62bb573.patch
# https://github.com/python-xmp-toolkit/python-xmp-toolkit/pull/84
Source1:        https://github.com/python-xmp-toolkit/python-xmp-toolkit/raw/e0f42af4a731ac1eea2977895f2c8dd0264304c3/test/samples/BlueSquare.gif

BuildArch:      noarch

BuildRequires:  exempi
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytz)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
Python XMP Toolkit Python XMP Toolkit is a library for working with XMP
metadata, as well as reading/writing XMP metadata stored in many different file
formats.

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

Requires:       exempi
%{?python_enable_dependency_generator}

%description -n python3-%{srcname}
Python XMP Toolkit Python XMP Toolkit is a library for working with XMP
metadata, as well as reading/writing XMP metadata stored in many different file
formats.


%package -n python-%{srcname}-doc
Summary:        python-xmp-toolkit documentation

%description -n python-%{srcname}-doc
Documentation for python-xmp-toolkit


%prep
%autosetup -n %{pypi_name}-%{version} -p1
cp %SOURCE1 test/samples/

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%py3_build

# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%py3_install


%check
%{python3} setup.py test


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/libxmp
%{python3_sitelib}/python_xmp_toolkit-%{version}-py%{python3_version}.egg-info

%files -n python-%{srcname}-doc
%doc html
%license LICENSE


%changelog
* Mon Jun 22 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.1-8
- Backport fixed GIF89a test file for new exempi

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 21 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.1-1
- Initial package.
