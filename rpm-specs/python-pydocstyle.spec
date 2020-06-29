%global pypi_name pydocstyle

Name: python-%{pypi_name}
Version: 5.0.1
Release: 3%{?dist}
Summary: Python docstring style checker

License: MIT
URL: https://github.com/PyCQA/pydocstyle/
# NOTE: Temporarily use GitHub archive download service until upstream includes
# tests in the release tarballs.
Source0: https://github.com/PyCQA/%{pypi_name}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: python3-devel
# Required for running tests.
BuildRequires: python3dist(snowballstemmer)
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(mypy)

%description
A static analysis tool for checking compliance with Python docstring
conventions.

It supports most of PEP 257 out of the box, but it should not be considered a
reference implementation.


%package -n python3-%{pypi_name}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires: python3dist(snowballstemmer)

%description -n python3-%{pypi_name}
A static analysis tool for checking compliance with Python docstring
conventions.

It supports most of PEP 257 out of the box, but it should not be considered a
reference implementation.


%prep
%autosetup -n %{pypi_name}-%{version}


%build
%py3_build

# Remove (incorrect) Python shebang from package's __main__.py file.
sed -i '\|/usr/bin/env|d' build/lib/pydocstyle/__main__.py


%install
%py3_install


%check
# Run main Pytest tests (skip linting with pep8 as discussed in
# https://pagure.io/packaging-committee/issue/909).

# Disable "install_package" fixure for integration tests since we want the
# tests to be run against the system-installed version of the package.
sed -i '/pytestmark = pytest.mark.usefixtures("install_package")/d' \
    src/tests/test_integration.py
# Replace 'python(2|3)?' with '%%{__python3}' in tests that run pydocstyle as
# a named Python module.
sed -E -i 's|"python(2\|3)?( -m pydocstyle)|"%{__python3}\2|' \
    src/tests/test_integration.py

# NOTE: We need to manually set PATH and PYTHONPATH environment variables so
# that newly built binaries / Python packages are found.
PATH=%{buildroot}%{_bindir}:$PATH \
PYTHONPATH=%{buildroot}%{python3_sitelib} \
py.test-3 -v src/tests

# TODO: Enable mypy tests in the future.


%files -n python3-%{pypi_name}
%license LICENSE-MIT
%doc README.rst
%{_bindir}/pydocstyle
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.0.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Tadej Janež <tadej.j@nez.si> - 5.0.1-1
- Update to 5.0.1 release
- Clean-up and modernize the SPEC file
- Drop obsolete Requires/BuildRequires

* Thu Sep 26 2019 Tadej Janež <tadej.j@nez.si> - 4.0.1-2
- Update %%check section
- Skip linting with pep8 and drop python3-pytest-pep8 build requirement

* Tue Aug 27 2019 Tadej Janež <tadej.j@nez.si> - 4.0.1-1
- Update to 4.0.1 release

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0.0-7
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.0-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Tadej Janež <tadej.j@nez.si> - 2.0.0-1
- Initial release in Fedora 25+.

* Mon May 08 2017 Tadej Janež <tadej.j@nez.si> - 2.0.0-0.1
- Update to 2.0.0 release.
- Update Requires and BuildRequires for the new version.
- Drop pep257 compatibility console script.

* Fri Apr 07 2017 Tadej Janež <tadej.j@nez.si> - 1.1.1-0.2
- Temporarily use GitHub arhive download service until upstream includes tests
  in the release tarballs.
- Run tests in %%check.
- Add appropriate BuildRequires for running the tests.
- Remove end-of-line encoding fixes which are no longer necessary.

* Mon Jan 02 2017 Tadej Janež <tadej.j@nez.si> - 1.1.1-0.1
- Initial package.
