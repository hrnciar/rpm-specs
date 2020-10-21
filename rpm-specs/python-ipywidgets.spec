# Created by pyp2rpm-3.3.4
%global pypi_name ipywidgets
# Documentation is disabled because it requires jupyter-sphinx
%bcond_with doc

Name:           python-%{pypi_name}
Version:        7.5.1
Release:        2%{?dist}
Summary:        IPython HTML widgets for Jupyter

License:        BSD
URL:            http://ipython.org
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(ipython)
BuildRequires:  python3dist(ipykernel)
# Docs
%if %{with doc}
BuildRequires:  python3dist(nbsphinx)
BuildRequires:  python3dist(recommonmark)
BuildRequires:  python3dist(sphinx)
%endif
# Tests
BuildRequires:  python3dist(jsonschema)
BuildRequires:  python3dist(pytest)

%description
Interactive HTML widgets for Jupyter notebooks and the IPython kernel.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Interactive HTML widgets for Jupyter notebooks and the IPython kernel.

%if %{with doc}
%package -n python-%{pypi_name}-doc
Summary:        ipywidgets documentation
%description -n python-%{pypi_name}-doc
Documentation for ipywidgets
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
sed -i "s/from distutils.core /from setuptools /" setup.py


%build
%py3_build
%if %{with doc}
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%py3_install

%check
%pytest

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%if %{with doc}
%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE
%endif

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Lumír Balhar <lbalhar@redhat.com> - 7.5.1-1
- Initial package.
