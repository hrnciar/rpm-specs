%global srcname django-js-asset

Name:           python-%{srcname}
Version:        1.2.2
Release:        3%{?dist}
Summary:        Script tag with additional attributes for django.forms.Media

License:        BSD
URL:            https://github.com/matthiask/django-js-asset
Source:         %{pypi_source}

BuildArch:      noarch

%global _description \
%{summary}.

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# https://github.com/matthiask/django-js-asset/pull/5
Requires:       python%{python3_version}dist(django)

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -vr *.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/django_js_asset-*.egg-info/
%{python3_sitelib}/js_asset/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 31 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.2-1
- Initial package
