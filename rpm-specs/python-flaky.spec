%global pypi_name flaky
Name:           python-%{pypi_name}
Version:        3.6.1
Release:        2%{?dist}
Summary:        Plugin for nose or py.test that automatically reruns flaky tests
License:        ASL 2.0
URL:            https://github.com/box/flaky

Source0:        %{pypi_source} 
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(genty)
BuildRequires:  python3dist(nose)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

%description
Flaky is a plugin for nose or py.test that automatically reruns flaky
tests. Ideally, tests reliably pass or fail, but sometimes test fixtures must
rely on components that aren't 100% reliable. With flaky, instead of removing
those tests or marking them to @skip, they can be automatically retried.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3dist(setuptools)

%description -n python3-%{pypi_name}
Flaky is a plugin for nose or py.test that automatically reruns flaky
tests. Ideally, tests reliably pass or fail, but sometimes test fixtures must
rely on components that aren't 100% reliable. With flaky, instead of removing
those tests or marking them to @skip, they can be automatically retried.


%prep
%autosetup -n %{pypi_name}-%{version}

# Use mock from standard library:
sed -i -e 's/import mock/from unittest import mock/' \
       -e 's/from mock/from unittest.mock/' \
       test/test_*/test_*.py


%build
%py3_build


%install
%py3_install


%check
export PYTHONPATH=%{buildroot}%{python3_sitelib}
# adapted from upstream's tox.ini
%{__python3} -m nose -v --with-flaky --exclude="test_nose_options_example" test/test_nose/
%{__python3} -m pytest -v -k 'example and not options' --doctest-modules test/test_pytest/
%{__python3} -m pytest -v -k 'example and not options' test/test_pytest/
%{__python3} -m pytest -v -p no:flaky test/test_pytest/test_flaky_pytest_plugin.py
%{__python3} -m nose -v --with-flaky --force-flaky --max-runs 2 test/test_nose/test_nose_options_example.py
%{__python3} -m pytest -v --force-flaky --max-runs 2  test/test_pytest/test_pytest_options_example.py


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info


%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 3.6.1-2
- Rebuilt for Python 3.9

* Wed Mar 11 2020 Tomas Hrnciar <thrnciar@redhat.com> - 3.6.1-1
- Update to 3.6.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.5.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.5.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 30 2019 Miro Hrončok <mhroncok@redhat.com> - 3.5.3-1
- Update to 3.5.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 30 2018 Miro Hrončok <mhroncok@redhat.com> - 3.4.0-1
- Initial package
