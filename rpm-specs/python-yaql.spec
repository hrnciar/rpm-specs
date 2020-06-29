%global pypi_name yaql

%if 0%{?fedora} || 0%{?rhel} > 7
%global with_python3 1
%{!?python3_shortver: %global python3_shortver %(%{__python3} -c 'import sys; print(str(sys.version_info.major) + "." + str(sys.version_info.minor))')}
%else
%global with_python2 1
%{!?python2_shortver: %global python2_shortver %(%{__python2} -c 'import sys; print(str(sys.version_info.major) + "." + str(sys.version_info.minor))')}
%endif

# Disable docs building as it doesn't support recent sphinx
%global with_docs 0

Name:           python-%{pypi_name}
Version:        1.1.3
Release:        12%{?dist}
Summary:        Yet Another Query Language

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description
YAQL library has a out of the box large set of commonly used functions.

%if 0%{?with_python2}
%package -n     python2-%{pypi_name}
Summary:        YAQL library has a out of the box large set of commonly used functions.
%{?python_provide:%python_provide python2-%{pypi_name}}

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-pbr
BuildRequires:  python2-sphinx
BuildRequires:  python2-oslo-sphinx

Requires:       python2-six
Requires:       python2-pbr
Requires:       python2-babel
Requires:       python2-dateutil
%if 0%{?fedora} || 0%{?rhel} > 7
Requires:       python2-ply
%else
Requires:       python-ply
%endif

%description -n python2-%{pypi_name}
YAQL library has a out of the box large set of commonly used functions

%endif

# Python3 package
%if 0%{?with_python3}
%package -n     python3-%{pypi_name}
Summary:        YAQL library has a out of the box large set of commonly used functions.
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-tools
BuildRequires:  python3-pbr
BuildRequires:  python3-sphinx
BuildRequires:  python3-oslo-sphinx

Requires:       python3-six
Requires:       python3-pbr
Requires:       python3-babel
Requires:       python3-ply
Requires:       python3-dateutil

%description -n python3-%{pypi_name}
YAQL library has a out of the box large set of commonly used functions.
%endif

%if 0%{?with_docs}
# Documentation package
%package -n python-%{pypi_name}-doc
Summary:        Documentation for YAQL library

%description -n python-%{pypi_name}-doc
Documentation for YAQL library
%endif


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
2to3 --write --nobackups %{py3dir}
%endif

%build
%if 0%{?with_python2}
%py2_build
%endif
%if 0%{?with_python3}
pushd %{py3dir}
%py3_build
popd
%endif

%if 0%{?with_docs}
# generate html docs 
%if 0%{?with_python3}
sphinx-build-3 doc/source html
%else
sphinx-build doc/source html
%endif
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%if 0%{?with_python3}
pushd %{py3dir}
%py3_install
mv %{buildroot}/%{_bindir}/%{pypi_name} %{buildroot}/%{_bindir}/python3-%{pypi_name}
popd
%endif

%if 0%{?with_python2}
%py2_install
%endif

# rename binaries, make compat symlinks
%if 0%{?with_python2}
pushd %{buildroot}%{_bindir}
for i in %{pypi_name}-{2,%{?python2_shortver}}; do
    ln -sf %{pypi_name} $i
done
popd
%endif

%if 0%{?with_python3}
pushd %{buildroot}%{_bindir}
for i in %{pypi_name}-{3,%{?python3_shortver}}; do
    ln -sf  python3-%{pypi_name} $i
    ln -sf  python3-%{pypi_name} %{pypi_name}
done
popd
%endif

# Delete tests
rm -fr %{buildroot}%{python_sitelib}/tests

 
%if 0%{?with_python2}
%files -n python2-%{pypi_name}
%license LICENSE
%doc doc/source/readme.rst README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%{_bindir}/%{pypi_name}-2*
%{_bindir}/%{pypi_name}
%endif

# Files for python3
%if 0%{?with_python3}
%files -n python3-%{pypi_name} 
%license LICENSE
%doc doc/source/readme.rst README.rst
%{_bindir}/python3-%{pypi_name}
%{_bindir}/%{pypi_name}-3*
%{_bindir}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%endif

%if 0%{?with_docs}
%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-9
- Rebuilt for Python 3.8

* Mon Jul 29 2019 Alfredo Moralejo <amoralej@redhat.com> - 1.1.3-8
- Remove python2 subpackage from fedora and rhel < 8
- Remove docs subpackage as it doesn't support recent versions of sphinx

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.3-5
- Drop explicit locale setting
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-3
- Rebuilt for Python 3.7

* Wed Feb 14 2018 Yatin Karel <ykarel@redhat.com> - 1.1.3-2
- Fix python-ply Requires for rhel

* Fri Feb 09 2018 Alfredo Moralejo <amoralej@redhat.com> - 1.1.3-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-4
- Rebuild for Python 3.6

* Mon Aug 22 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 1.1.0-3
- Fix Requires in python2-yaql

* Fri Apr  8 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 1.1.0-2
- Fix RHBZ#1282081

* Fri Apr  8 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 1.1.0-1
- Upstream 1.1.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 18 2015 Marcos Fermin Lobo <marcos.fermin.lobo@cern.ch> 1.0.2-1.el7
- Update to 1.0.2

* Thu Nov 12 2015 Kalev Lember <klember@redhat.com> - 0.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Aug 26 2015 Marcos Fermin Lobo <marcos.fermin.lobo@cern.ch> 0.2.7-1
- First RPM for FC23
