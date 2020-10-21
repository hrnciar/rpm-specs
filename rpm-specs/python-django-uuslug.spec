# Created by pyp2rpm-3.3.2
%global pypi_name django-uuslug

Name:           python-%{pypi_name}
Version:        1.2.0
Release:        2%{?dist}
Summary:        A Django slugify application that guarantees uniqueness and handles Unicode

License:        MIT
URL:            https://github.com/un33k/django-uuslug
Source0:        %{pypi_source}
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(django)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(python-slugify)

%description
A Django slugify application that guarantees Uniqueness and handles Unicode


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(python-slugify) >= 1.2.0
Requires:       python3dist(six)
Requires:       python3dist(django)

%description -n python3-%{pypi_name}
A Django slugify application that guarantees Uniqueness and handles Unicode


%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf django_uuslug.egg-info

# These directories are shipped in the tarball. Let's remove them.
rm -r uuslug/__pycache__/
rm -r uuslug/tests/__pycache__/

%check
%{__python3} manage.py test

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/uuslug/
%{python3_sitelib}/django_uuslug-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Chenxiong Qi <qcxhome@gmail.com> - 1.2.0-1
- Initial package.
