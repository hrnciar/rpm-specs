%global pkgname cookiecutter

Name:           python-cookiecutter
Version:        1.6.0
Release:        13%{?dist}
Summary:        CLI utility to create projects from templates
License:        BSD
URL:            https://github.com/audreyr/cookiecutter
Source0:        https://github.com/audreyr/%{pkgname}/archive/%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-click
BuildRequires:  python3-whichcraft
BuildRequires:  python3-binaryornot
BuildRequires:  python3-poyo
BuildRequires:  python3-jinja2-time
BuildRequires:  python3-future
BuildRequires:  python3-arrow

BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest-catchlog
BuildRequires:  python3-freezegun
BuildRequires:  python3-jinja2

%description
A command-line utility that creates projects from cookiecutters (project
templates), e.g. creating a Python package project from a Python package
project template.

%package     -n python-%{pkgname}-doc
Summary: Documentation for %{pkgname}
%description -n python-%{pkgname}-doc
Documentation for %{pkgname}

%package     -n python3-%{pkgname}
Summary: %{summary}
Recommends: python-%{pkgname}-doc
Requires:  python3-binaryornot
Requires:  python3-click
Requires:  python3-future
Requires:  python3-jinja2
Requires:  python3-jinja2-time
Requires:  python3-poyo
Requires:  python3-requests
Requires:  python3-whichcraft
%{?python_provide:%python_provide python3-%{pkgname}}
%description -n python3-%{pkgname}
A command-line utility that creates projects from cookiecutters (project
templates), e.g. creating a Python package project from a Python package
project template.


%prep
%autosetup -n %{pkgname}-%{version}

# fix invocation of /usr/bin/python
sed -i 's#python -c#%{__python3} -c#' Makefile

%build
%{py3_build}

# make sphinx docs
make docs

%install
%{py3_install}

%check
%{__python3} setup.py test

%files -n python3-%{pkgname}
%license LICENSE
# For noarch packages: sitelib
%{python3_sitelib}/*
%{_bindir}/%{pkgname}

%files -n python-%{pkgname}-doc
%license LICENSE
%doc docs
%doc *.rst

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.6.0-10
- Fix failing build by adding the missing BR

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Petr Viktorin <pviktori@redhat.com> - 1.6.0-6
- Remove the Python 2 subpackage
  https://bugzilla.redhat.com/show_bug.cgi?id=1639308

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-4
- Rebuilt for Python 3.7

* Tue May 29 2018 Brett Lentz <brett.lentz@gmail.com> - 1.6.0-3
- fix deps

* Tue Apr  3 2018 Brett Lentz <brett.lentz@gmail.com> - 1.6.0-2
- fix deps

* Thu Mar  1 2018 Brett Lentz <brett.lentz@gmail.com> - 1.6.0-1
- initial packaging
