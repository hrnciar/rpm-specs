%global pypi_name zstd
%global zstd_version 1.4.5

Name:           python-%{pypi_name}
Version:        %{zstd_version}.1
Release:        2%{?dist}
Summary:        Zstd Bindings for Python

License:        BSD
URL:            https://github.com/sergey-dryabzhinsky/python-zstd
Source0:        %{pypi_source}

# Patches to fix test execution
Patch0:         python-zstd-1.4.5.1-test-external.patch
Patch1:         python-zstd-1.4.5.1-test-once.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  pkgconfig(libzstd) >= %{zstd_version}

%description
Simple Python bindings for the Zstd compression library.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
# The library does not do symbol versioning to fully match automatically on
Requires:       libzstd%{?_isa} >= %{zstd_version}

%description -n python3-%{pypi_name}
Simple Python bindings for the Zstd compression library.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Remove bundled zstd library
rm -rf zstd/
# do not test the version matching, we don't really need exact version of
# zstd here
rm tests/test_version.py
sed -i -e '/test_version/d' tests/__init__.py

%build
%py3_build -- --legacy --pyzstd-legacy --external

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitearch}/%{pypi_name}*.so

%changelog
* Mon Sep 21 2020 Joel Capitao <jcapitao@redhat.com> - 1.4.5.1-2
- Edit macro for CentOS interoperability

* Sun Aug 23 2020 Neal Gompa <ngompa13@gmail.com> - 1.4.5.1-1
- Initial package (#1870571)
