%global pkg_name inject
%global pypi_name Inject

%global pkg_description %{expand:Dependency injection the python way, the good way.
Not a port of Guice or Spring.

Key features:
  - Fast.
  - Thread-safe.
  - Simple to use.
  - Does not steal class constructors.
  - Does not try to manage your application object graph.
  - Transparently integrates into tests.
  - Supports type hinting in Python 3.5+.
  - Autoparams leveraging type annotations.
}

 
Name: python-%{pkg_name}
Summary: Dependency injection, the Python way
License: ASL 2.0

Version: 4.3.1
Release: 2%{?dist}

URL: https://github.com/ivankorobkov/python-%{pkg_name}
Source0: %pypi_source

%global with_tests 1

BuildRequires: python3-devel
BuildRequires: python3dist(setuptools)

%if 0%{?with_tests}
BuildRequires: python3dist(pytest-runner)
%endif

BuildArch: noarch

%description
%{pkg_description}


%package -n python3-%{pkg_name}
Summary: %{summary}
BuildArch: noarch

%description -n python3-%{pkg_name}
%{pkg_description}


%prep
%autosetup -n %{pypi_name}-%{version}


%build
%py3_build


%install
%py3_install


%if 0%{?with_tests}
%check
# This file is missing from the PyPi tarballs, but is required for tests to work
# Taken from: https://raw.githubusercontent.com/ivankorobkov/python-inject/%{version}/test/__init__.py
# See issue: https://github.com/ivankorobkov/python-inject/issues/70
cat > test/__init__.py <<EOF
from unittest import TestCase
import asyncio
import inject


class BaseTestInject(TestCase):
    def tearDown(self):
        inject.clear()
    
    def run_async(self, awaitable):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(awaitable)
EOF

%pytest
%endif


%files -n python3-%{pkg_name}
%doc CHANGES.md README.md
%license LICENSE
%{python3_sitelib}/%{pkg_name}/
%{python3_sitelib}/%{pypi_name}-*.egg-info/


%changelog
* Mon Sep 28 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 4.3.1-2
- Use python3dist() for specifying dependencies
- Run tests using pytest instead of nosetests

* Fri Sep 25 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 4.3.1-1
- Initial packaging
