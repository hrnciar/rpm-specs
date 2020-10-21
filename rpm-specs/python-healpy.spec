%global srcname healpy
%global sum Python healpix maps tools

Name:           python-%{srcname}
Version:        1.14.0
Release:        2%{?dist}
Summary:        %{sum}

License:        GPLv2+ 
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz

# Upstream only supports 64 bit architectures, 32 Bit builds, but tests fail
# and we don't want to provide a non reliable software.
# Check https://github.com/healpy/healpy/issues/194
ExclusiveArch:  aarch64 ppc64 ppc64le x86_64 s390x
# Also explicitly exclude known unsupported architectures
ExcludeArch:    %{ix86} %{arm}

# Common build requirements
BuildRequires:  cfitsio-devel
BuildRequires:  gcc-c++

# Python 3 build requirements
BuildRequires:  python3-astropy
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-matplotlib
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-astropy
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
BuildRequires:  python3-six


%description
Healpy provides a python package to manipulate healpix maps. It is based on the
standard numeric and visualisation tools for Python, Numpy and matplotlib.

%package -n python3-%{srcname}
Summary:        %{sum}
Requires:       python3-astropy
Requires:       python3-matplotlib
Requires:       python3-six
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Healpy provides a python package to manipulate healpix maps. It is based on the
standard numeric and visualisation tools for Python, Numpy and matplotlib.

This package contains the Python 3 modules.

%prep
%autosetup -p1 -n %{srcname}-%{version}
# Delete pre-cythonized files, we do that by ourself to use Fedora Cython
find . -name *.pyx -print0 | sed "s/pyx/cpp/g" | xargs -0 rm

%build
%py3_build

%install
%py3_install
rm -f %{buildroot}%{_bindir}/healpy_get_wmap_maps.sh

%check
# For skipped tests: They require internet access and therefore have to be disabled
pushd %{buildroot}/%{python3_sitearch}
py.test-%{python3_version} -k "not (test_astropy_download_file or test_rotate_map_polarization or test_pixelweights_local_datapath)" healpy
# Remove relict from tests
rm -rf .pytest_cache
popd

# Note that there is no %%files section for the unversioned python module if we are building for several python runtimes
%files -n python3-%{srcname}
%license COPYING
%doc CHANGELOG.rst CITATION README.rst
%{python3_sitearch}/*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Christian Dersch <lupinix@fedoraproject.org> - 1.14.0-1
- new version

* Mon Jul 20 2020 Christian Dersch <lupinix@fedoraproject.org> - 1.13.0-1
- new version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.12.9-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.9-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.12.9-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 29 2019 Christian Dersch <lupinix@fedoraproject.org> - 1.12.9-1
- new version
- system libs now detected automatically, no more patch needed

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Christian Dersch <lupinix@fedoraproject.org> - 1.12.4-2
- Drop python2 subpackage

* Tue Oct 02 2018 Christian Dersch <lupinix@fedoraproject.org> - 1.12.4-1
- new version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Christian Dersch <lupinix@mailbox.org> - 1.12.3-1
- new version

* Sat Jun 30 2018 Christian Dersch <lupinix@mailbox.org> - 1.12.2-1
- new version

* Sat Jun 30 2018 Christian Dersch <lupinix@mailbox.org> - 1.12.0-4
- Use GitHub tar instead of PyPI one (as GitHub one is not Cythonized)

* Tue Jun 19 2018 Christian Dersch <lupinix@fedoraproject.org> - 1.12.0-3
- Use bundled copies of healpix and cfitsio for now due to upstream changes

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.12.0-2
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Christian Dersch <lupinix@fedoraproject.org> - 1.12.0-1
- new version

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 1.11.0-5
- rebuilt for cfitsio 3.450

* Sat Feb 24 2018 Christian Dersch <lupinix@mailbox.org> - 1.11.0-4
- rebuilt for cfitsio 3.420 (so version bump)

* Wed Feb 14 2018 Christian Dersch <lupinix@mailbox.org> - 1.11.0-3
- rebuilt

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 08 2017 Christian Dersch <lupinix@mailbox.org> - 1.11.0-1
- new version

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 01 2017 Christian Dersch <lupinix@mailbox.org> - 1.10.3-2
- enable s390x architecture

* Fri Apr 07 2017 Christian Dersch <lupinix@mailbox.org> - 1.10.3-1
- initial package (review: rhbz #1440216)


