# Created by pyp2rpm-3.3.2
%global pypi_name freecell_solver

Name:           python-%{pypi_name}
Version:        0.2.6
Release:        1%{?dist}
Summary:        Freecell Solver Python bindings

License:        MIT
URL:            https://fc-solve.shlomifish.org/
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildConflicts: python3dist(coverage) = 4.4
BuildRequires:  python3dist(coverage) >= 4.0
BuildRequires:  python3dist(hacking) >= 0.12.0
BuildRequires:  python3dist(openstackdocstheme)
BuildRequires:  python3dist(oslotest) >= 1.10.0
BuildRequires:  python3dist(pbr)
BuildRequires:  python3dist(pbr) >= 2.0
BuildRequires:  python3dist(python-subunit) >= 0.0.18
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(testtools) >= 1.4.0
BuildRequires:  python3dist(sphinx)

%description
Python bindings for Freecell Solver using cffi.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(pbr) >= 2.0
%description -n python3-%{pypi_name}
Python bindings for Freecell Solver using cffi.

%package -n python-%{pypi_name}-doc
Summary:        freecell_solver documentation
%description -n python-%{pypi_name}-doc
Documentation for freecell_solver

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst doc/source/readme.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Tue Jun 23 2020 Shlomi Fish <shlomif@shlomifish.org> 0.2.6-1
- New Upstream Version

* Fri May 29 2020 Shlomi Fish <shlomif@shlomifish.org> 0.2.3-6
- Rebuild for Python 3.9

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.3-2
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Shlomi Fish <shlomif@shlomifish.org> - 0.2.3-1
- Initial package.
