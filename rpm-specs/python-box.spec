%global pypi_name box

Name:           python-%{pypi_name}
Version:        5.1.1
Release:        1%{?dist}
Summary:        Python dictionaries with advanced dot notation access

License:        MIT
URL:            https://github.com/cdgriffith/Box
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Box will automatically make otherwise inaccessible keys safe to
access as an attribute. You can always pass conversion_box=False
to Box to disable that behavior. Also, all new dict and lists
added to a Box or BoxList object are converted automatically.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(msgpack)
BuildRequires:  python3dist(ruamel.yaml)

Requires:       python3dist(msgpack)
Requires:       python3dist(ruamel.yaml)
Requires:       python3dist(toml)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Box will automatically make otherwise inaccessible keys safe to
access as an attribute. You can always pass conversion_box=False
to Box to disable that behavior. Also, all new dict and lists
added to a Box or BoxList object are converted automatically.

%prep
%autosetup -n Box-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest -v test -k "not test_msgpack"

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/python_box-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Sep 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 5.1.1-1
- Enable tests
- Update to new upstream release 5.1.1 (#1867812)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.4.5-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 11 2019 David Moreau Simard <dmsimard@redhat.com> - 3.4.5-1
- Update to latest upstream release

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.4.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.4.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 5 2019 David Moreau Simard <dmsimard@redhat.com> - 3.4.1-1
- First version of the package
