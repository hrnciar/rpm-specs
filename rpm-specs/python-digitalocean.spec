%global pypi_name python-digitalocean
%global pkgname digitalocean

%bcond_without python3
%global py3_prefix python%{python3_pkgversion}

%if 0%{?fedora} || (0%{?rhel} && 0%{?rhel} >= 8)
%bcond_with python2
%else
%bcond_without python2
%endif

Name:           python-%{pkgname}
Version:        1.15.0
Release:        2%{?dist}
Summary:        Easy access to Digital Ocean APIs to deploy droplets, images and more

License:        LGPLv3
URL:            https://pypi.python.org/pypi/python-digitalocean
Source0:        https://github.com/koalalorenzo/%{pypi_name}/archive/v%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-jsonpickle
BuildRequires:  python2-mock
BuildRequires:  python2-pytest
BuildRequires:  python2-requests
BuildRequires:  python2-responses
BuildRequires:  python2-setuptools
%endif

%if %{with python3}
BuildRequires:  %{py3_prefix}-devel
BuildRequires:  %{py3_prefix}-jsonpickle
BuildRequires:  %{py3_prefix}-mock
BuildRequires:  %{py3_prefix}-pytest
BuildRequires:  %{py3_prefix}-requests
BuildRequires:  %{py3_prefix}-responses
BuildRequires:  %{py3_prefix}-setuptools
%endif

%description
Easy access to Digital Ocean APIs to deploy droplets, images and
more.

%if %{with python2}
%package -n python2-%{pkgname}
Requires:       python2-jsonpickle
Requires:       python2-requests

Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pkgname}}

%description -n python2-%{pkgname}
Easy access to Digital Ocean APIs to deploy droplets, images and
more.

This is the Python 2 version of the package.
%endif

%if %{with python3}
%package -n %{py3_prefix}-%{pkgname}
Requires:       %{py3_prefix}-jsonpickle
Requires:       %{py3_prefix}-requests

Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkgname}}

%description -n %{py3_prefix}-%{pkgname}
Easy access to Digital Ocean APIs to deploy droplets, images and
more.

This is the Python 3 version of the package.
%endif

%prep
%autosetup -p1

%build
%if %{with python2}
%py2_build
%endif

%if %{with python3}
%py3_build
%endif

%check
%if %{with python2}
%{__python2} setup.py test
%endif

%if %{with python3}
%{__python3} setup.py test
%endif

%install
%if %{with python2}
%py2_install
%endif

%if %{with python3}
%py3_install
%endif

%if %{with python2}
%files -n python2-%{pkgname}
%license LICENSE.txt
%doc README.md
%{python2_sitelib}/digitalocean
%{python2_sitelib}/python_digitalocean-%{version}*.egg-info
%endif

%if %{with python3}
%files -n %{py3_prefix}-%{pkgname}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/digitalocean
%{python3_sitelib}/python_digitalocean-%{version}*.egg-info
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.15.0-2
- Rebuilt for Python 3.9

* Tue Apr 28 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.15.0-1
- update to 1.15.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.14.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.14.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Eli Young <elyscape@gmail.com> - 1.14.0-1
- Update to 1.14.0
- Remove Python 2 package in Fedora 30+ (#1658538)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.13.2-4
- Rebuilt for Python 3.7

* Mon Feb 26 2018 Nick Bebout <nb@usi.edu> - 1.13.2-3
- Add python2- prefix where possible

* Thu Feb 15 2018 Eli Young <elyscape@gmail.com> - 1.13.2-2
- Fix requires

* Wed Feb 14 2018 Eli Young <elyscape@gmail.com> - 1.13.2-1
- Initial package (#1544605)
