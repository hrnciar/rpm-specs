%global pypi_name ruamel.yaml.clib
%global pname ruamel-yaml-clib

Name:           python-%{pname}
Version:        0.1.2
Release:        3%{?dist}
Summary:        C version of reader, parser and emitter for ruamel.yaml derived from libyaml

License:        MIT
URL:            https://bitbucket.org/ruamel/yaml.clib
Source0:        %{pypi_source}

BuildRequires:  gcc
BuildRequires:  libyaml-devel

%description
It is the C based reader/scanner and emitter for ruamel.yaml.

%package -n     python3-%{pname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-setuptools

%description -n python3-%{pname}
It is the C based reader/scanner and emitter for ruamel.yaml.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%{__python3} setup.py install --single-version-externally-managed --skip-build --root $RPM_BUILD_ROOT

%files -n python3-%{pname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/_ruamel_yaml.cpython-*
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 30 2019 Chandan Kumar <raukadah@gmail.com> - 0.1.2-1
- Initial package
