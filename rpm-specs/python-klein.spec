%global pypi_name klein

Name:           python-%{pypi_name}
Version:        20.6.0
Release:        1%{?dist}
Summary:        Python microframework built on werkzeug + twisted.web

License:        MIT
URL:            https://github.com/twisted/klein
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(attrs)
BuildRequires:  python3dist(hyperlink)
BuildRequires:  python3dist(incremental)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(tubes)
BuildRequires:  python3dist(twisted) >= 15.5
BuildRequires:  python3dist(werkzeug)
BuildRequires:  python3dist(zope.interface)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description
Klein is a Web Micro-Framework built on Twisted and Werkzeug.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Klein is a Web Micro-Framework built on Twisted and Werkzeug.

%package -n python-%{pypi_name}-doc
Summary:        klein documentation

%description -n python-%{pypi_name}-doc
Documentation for klein

%prep
%autosetup -n %{pypi_name}-%{version}
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

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Sun Aug 23 2020 Neal Gompa <ngompa13@gmail.com> - 20.6.0-1
- Initial package (#1870883)
