%global pypi_name django-markdownx

Name:           python-%{pypi_name}
Version:        3.0.1
Release:        3%{?dist}
Summary:        A comprehensive Markdown editor built for Django

License:        BSD
URL:            https://github.com/neutronX/django-markdownx
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(django)
BuildRequires:  python3dist(markdown)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

%description
Django MarkdownX is a comprehensive Markdown plugin built for Django, 
the renowned high-level Python web framework, with flexibility, extensibility, 
and ease-of-use at its core.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(django)
Requires:       python3dist(markdown)
Requires:       python3dist(pillow)
Requires:       python3dist(pip)

%description -n python3-%{pypi_name}
Django MarkdownX is a comprehensive Markdown plugin built for Django, 
the renowned high-level Python web framework, with flexibility, extensibility, 
and ease-of-use at its core.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

rm -rf markdownx/static/.DS_Store
rm -rf markdownx/static/markdownx/.DS_Store
rm -rf markdownx/static/markdownx/admin/.DS_Store
rm -rf markdownx/templates/.DS_Store
rm -rf markdownx/templates/markdownx/.DS_Store

chmod 0644 README.rst

%build
%py3_build

%install
%py3_install

%find_lang django
%files -n python3-%{pypi_name} -f django.lang
%license LICENSE
%doc README.rst
%{python3_sitelib}/markdownx
%exclude %{python3_sitelib}/markdownx/locale
%{python3_sitelib}/django_markdownx-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Luis Bazan <lbazan@fedoraproject.org> - 3.0.1-1
- New upstream version

* Fri Dec 27 2019 Luis Bazan <lbazan@fedoraproject.org> - 3.0.0-1
- New upstream version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.28-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.28-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Dec 11 2018 Luis Bazan <lbazan@fedoraproject.org> - 2.0.28-1
- Initial release
