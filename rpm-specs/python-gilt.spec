%global srcname gilt
%global pkgname python-gilt
%global setup_flags PBR_VERSION=%{version}

Name:    python-%{srcname}
Version: 1.2.1
Release: 3%{?dist}
Summary: Gilt is a git layering tool
License: MIT

URL:     https://github.com/retr0h/gilt
Source0: https://pypi.io/packages/source/p/%{pkgname}/%{pkgname}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: python3-pbr
BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: python3-sphinx
BuildRequires: python3-git-url-parse

%description
Gilt is a git layering tool

%package -n python-%{srcname}-doc
Summary: %summary

%description -n python-%{srcname}-doc
Documentation for python-gilt

%package -n python3-%{srcname}
Summary: %summary

Recommends: python-%{srcname}-doc

Requires: python3-sh
Requires: python3-pbr
Requires: python3-click
Requires: python3-pyyaml
Requires: python3-colorama
Requires: python3-fasteners
Requires: python3-git-url-parse

%{?python_disable_dependency_generator}
%{?python_provide:%python_provide python3-%{srcname}}
%description -n python3-%{srcname}
Gilt is a git layering tool

%prep
%autosetup -n %{pkgname}-%{version}

%build
%{setup_flags} %{py3_build}

# generate html docs
cd doc
PYTHONPATH=.. make html
# remove the sphinx-build leftovers
rm -rf build/html/.{doctrees,buildinfo}

%install
%{setup_flags} %{py3_install}

%files -n python3-%{srcname}
%license LICENSE
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/python_%{srcname}-%{version}-py%{python3_version}.egg-info
%{_bindir}/%{srcname}

%files -n python-%{srcname}-doc
%license LICENSE
%doc *.rst
%doc doc/build/html

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-3
- Rebuilt for Python 3.9

* Wed Feb 26 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 1.2.1
- Initial package
