# what it's called on pypi
%global srcname Rx
# what it's imported as
%global libname rx
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{libname}

%global _description \
Rx is a library for composing asynchronous and event-based programs using\
observable collections and LINQ-style query operators in Python.

%bcond_without tests


Name:           python-%{pkgname}
Version:        3.1.1
Release:        2%{?dist}
Summary:        Reactive Extensions (Rx) for Python
License:        ASL 2.0
URL:            https://github.com/ReactiveX/RxPY
# PyPI tarball doesn't have tests
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch


%description %{_description}


%package -n python3-%{pkgname}
Summary:        %{summary}
BuildRequires:  python3-coverage
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pkgname}}


%description -n python3-%{pkgname} %{_description}


%prep
%autosetup -n RxPY-%{version}
rm -rf %{eggname}.egg-info


%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} setup.py test
%endif


%files -n python3-%{pkgname}
%license LICENSE
%doc README.rst authors.txt changes.md
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.1.1-1
- Update to 3.1.1

* Fri Jun 26 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.1.0-1
- Update to 3.1.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.1-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 16 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 3.0.1-2
- Add missed BR for new version: python3-coverage, python3-pytest, python3-pytest-asyncio, python3-pytest-runner
- Don't skip any tests, fixed in upstream

* Sun Sep 15 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 3.0.1-1
- Update to 3.0.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Carl George <carl@george.computer> - 1.6.1-1
- Initial package
