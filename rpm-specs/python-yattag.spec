%global pypi_name yattag

Name:           python-%{pypi_name}
Version:        1.14.0
Release:        1%{?dist}
Summary:        Generate HTML or XML in a pythonic way

License:        LGPLv2
URL:            https://www.yattag.org/
Source0:        https://github.com/leforestier/yattag/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Generate HTML or XML in a pythonic way.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Generate HTML or XML in a pythonic way.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v test/*.py

%files -n python3-%{pypi_name}
%doc README.rst
%license license/COPYING
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Oct 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.14.0-1
- Remove Python 2 subpackage
- Update to latest upstrema release 1.14.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.10.0-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 26 2018 Sebastian Kisela <skisela@redhat.com> - 1.10.0-4
- python2 will be deprecated soon. Build python3 packages only.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.10.0-2
- Rebuilt for Python 3.7

* Thu Mar 22 2018 Sebastian Kisela <skisela@redhat.com> - 1.10.0-1
- New upstream release 1.10.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 08 2017 Sebastian Kisela <skisela@redhat.com> - 1.9.2-1
- New upstream release 1.9.2

* Mon Oct 09 2017 skisela@redhat.com - 1.9.0-2
- Fix description macro. Reported at https://bugzilla.redhat.com/1498071.

* Wed Aug 23 2017 Sebastian Kisela <skisela@redhat.com> - 1.9.0-1
- New upstream release 1.9.0

* Wed Jul 26 2017 Sebastian Kisela <skisela@redhat.com> - 1.8.0-1
- Initial 1.8.0 package version