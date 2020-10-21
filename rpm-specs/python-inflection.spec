%global srcname inflection

Name:           python-%{srcname}
Version:        0.3.1
Release:        3%{?dist}
Summary:        Port of Ruby on Rails inflector to Python

License:        MIT
URL:            https://github.com/jpvanhal/inflection
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
Inflection is a string transformation library. It singularizes and pluralizes
English words, and transforms strings from CamelCase to underscored string.
Inflection is a port of Ruby on Rails’ inflector to Python.}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -vr *.egg-info

%build
%py3_build

%install
%py3_install

%check
%python3 -m pytest -v

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst CHANGES.rst
%{python3_sitelib}/inflection-*.egg-info/
%{python3_sitelib}/inflection.py
%{python3_sitelib}/__pycache__/inflection.*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-2
- Rebuilt for Python 3.9

* Sat Sep 07 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.1-1
- Initial package
