%global pypi_name Flask-PyMongo
%global pkg_name flask-pymongo

Name:           python-%{pkg_name}
Version:        2.3.0
Release:        1%{?dist}
Summary:        PyMongo support for Flask applications

License:        BSD
URL:            http://flask-pymongo.readthedocs.org/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pymongo-gridfs
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(flask)
BuildRequires:  python3dist(pymongo)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(vcversioner)
BuildRequires:  python3dist(sphinx)

%description
Flask-PyMongo - MongoDB support for Flask applications.
code is hosted on GitHub < Contributions are welcome !

%package -n     python3-%{pkg_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(flask)
Requires:       python3dist(pymongo)
%description -n python3-%{pkg_name}
Flask-PyMongo -MongoDB support for Flask applications.Flask-PyMongo is pip-
installable: $ pip install Flask-PyMongoDocumentation for Flask-PyMongo is
available on ReadTheDocs < code is hosted on GitHub < Contributions are
welcome!

%package -n python-%{pkg_name}-doc
Summary:        Flask-PyMongo documentation
%description -n python-%{pkg_name}-doc
Documentation for Flask-PyMongo

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

%check
#%%{__python3} setup.py test

%files -n python3-%{pkg_name}
%license docs/_themes/LICENSE
%doc README.md
%{python3_sitelib}/flask_pymongo
%{python3_sitelib}/Flask_PyMongo-%{version}-py%{python3_version}.egg-info

%files -n python-%{pkg_name}-doc
%doc html
%license docs/_themes/LICENSE

%changelog
* Sun Jul 12 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.3.0-1
- Initial package.
