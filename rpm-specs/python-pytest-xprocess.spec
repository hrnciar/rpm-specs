# Created by pyp2rpm-3.3.2
%global pypi_name pytest-xprocess

Name:           python-%{pypi_name}
Version:        0.12.1
Release:        6%{?dist}
Summary:        Pytest plugin to manage external processes across test runs

License:        MIT
URL:            https://github.com/pytest-dev/pytest-xprocess/
Source0:        %{pypi_source}
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cache)
BuildRequires:  python3dist(setuptools)

%description
Experimental py.test <>_ plugin for managing processes across test runs.Usage
install via:: pip install pytest-xprocessThis will provide a xprocess fixture
which helps you to ensure that one ore more longer-running processes are
present for your tests. You can use it to start and pre-configure test-specific
databases (Postgres, Couchdb, ...).Additionally there are two new command
line...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(psutil)
Requires:       python3dist(pytest)
Requires:       python3dist(pytest-cache)
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
Experimental py.test <>_ plugin for managing processes across test runs.Usage
install via:: pip install pytest-xprocessThis will provide a xprocess fixture
which helps you to ensure that one ore more longer-running processes are
present for your tests. You can use it to start and pre-configure test-specific
databases (Postgres, Couchdb, ...).Additionally there are two new command
line...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Remove executable bit from README
chmod -x README.rst

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/pytest_xprocess.py
%{python3_sitelib}/xprocess.py
%{python3_sitelib}/pytest_xprocess-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.12.1-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 09 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.12.1-1
- Initial package.
