%global pypi_name django-debreach

Name:           python-%{pypi_name}
Version:        2.0.1
Release:        3%{?dist}
Summary:        Basic/extra mitigation against the BREACH attack for Django projects

License:        BSD
URL:            http://github.com/lpomfrey/django-debreach
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(django)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
Basic/extra mitigation against the BREACH attack for Django projects.

When combined with rate limiting in your web-server, or by using something
like django-ratelimit, the techniques here should provide at least some
protection against the BREACH attack.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3dist(django) >= 2.0
%description -n python3-%{pypi_name}
Basic/extra mitigation against the BREACH attack for Django projects.

When combined with rate limiting in your web-server, or by using something
like django-ratelimit, the techniques here should provide at least some
protection against the BREACH attack.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=. %{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/debreach
%{python3_sitelib}/django_debreach-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 10 2019 Javier Peña <jpena@redhat.com> - 2.0.1-1
- Updated to 2.0.1 release (#1759926, #1760238)
- Dropped Python 2 bits, version 2.x does not support it

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.2-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 31 2018 Javier Peña <jpena@redhat.com> - 1.5.2-1
- Initial package.
