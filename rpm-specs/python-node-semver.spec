%global appname node-semver

%global appsum Python version of node-semver
%global appdesc Python version of node-semver library

Name: python-%{appname}
Version: 0.8.0
Release: 3%{?dist}
Summary: %{appsum}

License: MIT
URL: https://github.com/podhmo/python-semver
Source0: %{url}/archive/%{version}/%{appname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3dist(pytest)

%description
%{appdesc}.

%package -n python3-%{appname}
Summary: %{appsum}
%{?python_provide:%python_provide python3-%{appname}}

%description -n python3-%{appname}
%{appdesc}.

%prep
%autosetup -n python-semver-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{appname}
%license LICENSE
%doc README.rst CHANGES.txt
%{python3_sitelib}/semver/
%{python3_sitelib}/node_semver-*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 25 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0.8.0-1
- Initial SPEC release.
