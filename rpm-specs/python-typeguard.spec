%global pypi_name typeguard

Name:           python-%{pypi_name}
Version:        2.9.1
Release:        1%{?dist}
Summary:        Run-time type checker for Python
License:        MIT
URL:            https://github.com/agronholm/%{pypi_name}
Source0:        https://pypi.io/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%package -n python3-%{pypi_name}

Summary:          %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:    python3-setuptools
BuildRequires:    python3-setuptools_scm
BuildRequires:    python3-devel
BuildRequires:    python3-pbr
BuildRequires:    python3-six >= 1.9.0
BuildRequires:    python3-tornado >= 4.5
BuildRequires:    python3-pytest
BuildRequires:    python3-pytest-cov
BuildRequires:    python3-typing-extensions
%if %{undefined __pythondist_requires}
Requires:         python3-six >= 1.9.0
%endif


%description -n python3-%{pypi_name}
This library provides run-time type checking for functions defined with PEP
484 argument (and return) type annotations.

%description
This library provides run-time type checking for functions defined with PEP
484 argument (and return) type annotations.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info/*

%build
%py3_build

%install
%py3_install

%check
%if 0%{?python3_version_nodots} <= 038
%{python3} -m pytest
%endif

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*.egg-info/

%changelog
* Mon Jul 6 2020 Christopher Brown <chris.brown@redhat.com> - 2.9.1-1
- Fix description
- Remove egg-info in prep
- Add conditional for python 3.9

* Wed May 27 2020 Christopher Brown <chris.brown@redhat.com> - 2.7.1-2
- Remove dep generator
- Simplify description
- Fix file glob

* Wed May 6 2020 Christopher Brown <chris.brown@redhat.com> - 2.7.1-1
- Initial package at 2.7.1
