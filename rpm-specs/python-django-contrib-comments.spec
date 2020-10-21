# Created by pyp2rpm-3.3.2
%global pypi_name django-contrib-comments

Name:           python-%{pypi_name}
Version:        1.9.2
Release:        2%{?dist}
Summary:        The code formerly known as django.contrib.comments

License:        BSD
URL:            https://github.com/django/django-contrib-comments
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(django) >= 1.11
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)

%description
Django "excontrib" Comments Django used to include a comments framework; since
Django 1.6 it's been separated to a separate project. This is that project.This
framework can be used to attach comments to any model, so you can use it for
comments on blog entries, photos, book chapters, or anything else.For details,
consult the documentation.

Documentation: https://django-contrib-comments.readthedocs.io/en/latest/

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(django) >= 1.11
Requires:       python3dist(six)
%description -n python3-%{pypi_name}
Django "excontrib" Comments Django used to include a comments framework; since
Django 1.6 it's been separated to a separate project. This is that project.This
framework can be used to attach comments to any model, so you can use it for
comments on blog entries, photos, book chapters, or anything else.For details,
consult the documentation.

Documentation: https://django-contrib-comments.readthedocs.io/en/latest/

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf django_contrib_comments.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/django_comments
%{python3_sitelib}/django_contrib_comments-%{version}-py*.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 16 2020 Chenxiong Qi <qcxhome@gmail.com> - 1.9.2-1
- Initial package.
