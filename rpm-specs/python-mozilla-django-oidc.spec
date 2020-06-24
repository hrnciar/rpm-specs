%global shortname mozilla-django-oidc
Name:          python-%{shortname}
Version:       1.2.2
Release:       4%{?dist}
Summary:       A django OpenID Connect library

License:       MPLv2.0
URL:           https://github.com/mozilla/%{shortname}/
Source0:       https://github.com/mozilla/%{shortname}/archive/%{version}.tar.gz#/%{shortname}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
A django OpenID Connect library.

%package -n python3-%{shortname}
Summary:       A django OpenID Connect library
%{?python_provide:%python_provide python3-%{shortname}}
Requires:      python3-django

%description -n python3-%{shortname}
A django OpenID Connect library.

%prep
%autosetup -n %{shortname}-%{version} -p1

%build
%py3_build

%install
%py3_install

%files -n python3-%{shortname}
%license LICENSE
%{python3_sitelib}/mozilla_django_oidc/
%{python3_sitelib}/mozilla_django_oidc-*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.2-2
- Review updates

* Thu Dec 12 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.2-1
- Initial package
