%global pypi_name pep517

Name:           python-%{pypi_name}
Version:        0.7.0
Release:        6%{?dist}
Summary:        Wrappers to build Python packages using PEP 517 hooks

%bcond_without tests

# colorlog.py is "copied from Tornado", Apache licensed
License:        MIT and ASL 2.0
URL:            https://github.com/takluyver/pep517
Source0:        %{pypi_source}
BuildArch:      noarch

# Don't require stdlib backport modules on Python 3.8+
# Submitted upstream: https://github.com/pypa/pep517/pull/70
Patch0:         no-backports.patch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros


%description
This package contains wrappers around the hooks of standard API
for systems which build Python packages, specified in PEP 517.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

# colorlog.py is "copied from Tornado", Apache licensed
Provides:       bundled(python3dist(tornado))

%description -n python3-%{pypi_name}
This package contains wrappers around the hooks of standard API
for systems which build Python packages, specified in PEP 517.


%prep
%autosetup -n %{pypi_name}-%{version}

# Don't run the linter as part of tests
sed -i '/^addopts=--flake8$/d' pytest.ini
sed -i '/flake8/d' tox.ini


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-t}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pypi_name}


%if %{with tests}
%check
# "test_meta" skipped as it creates a venv and tries
# to install to it from PyPI
%tox -- -- -v -k "not test_meta"
%endif


%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
* Mon Sep 21 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-6
- Use %%pyproject_buildrequires to bring in all the needed tools (like pip)
- Resolves rhbz#1880983

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Petr Viktorin <pviktori@redhat.com> - 0.7.0-2
- Don't pull in importlib_metadata & zipp backports for Python 3.8+

* Wed Oct 23 2019 Petr Viktorin <pviktori@redhat.com> - 0.7.0-1
- Update to version 0.7.0
- Change dependency from pytoml to toml

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Petr Viktorin <pviktori@redhat.com> - 0.5.0-1
- Initial package
