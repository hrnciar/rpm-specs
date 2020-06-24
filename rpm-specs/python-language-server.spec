%global pypi_name python-language-server

%global short_name language-server

%global _description %{expand:
A Python implementation of the Language Server Protocol.
}

Name:           %{pypi_name}
Version:        0.31.10
Release:        4%{?dist}
Summary:        Python Language Server for the Language Server Protocol

License:        MIT
URL:            https://github.com/palantir/python-language-server
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(autopep8)
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(flake8)
BuildRequires:  python3dist(jedi)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(mccabe)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(pluggy)
BuildRequires:  python3dist(pycodestyle)
BuildRequires:  python3dist(pydocstyle) >= 2.0.0
BuildRequires:  python3dist(pyflakes) >= 1.6.0
BuildRequires:  python3dist(pylint)
BuildRequires:  python3dist(pyqt5)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(python-jsonrpc-server)
BuildRequires:  python3dist(rope) >= 0.10.5
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(ujson)
BuildRequires:  python3-versioneer
BuildRequires:  python3dist(yapf)

%description %_description

%package -n     python3-%{short_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{short_name}}

Requires:       python3dist(jedi)
Requires:       python3dist(python-jsonrpc-server)
Requires:       python3dist(pluggy)
Requires:       python3dist(ujson)

%description -n python3-%{short_name}
%_description

%prep
%autosetup -n %{pypi_name}-%{version}
# drop ujson version
# https://github.com/palantir/python-language-server/issues/744
# https://github.com/palantir/python-jsonrpc-server/issues/36
sed -i 's/ujson<=1.35;/ujson;/' setup.py

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
# disable incompatible tests
# https://github.com/palantir/python-jsonrpc-server/issues/33
# https://github.com/palantir/python-jsonrpc-server/pull/37
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-3 -v -k 'not ( test_missing_message or test_syntax_error_pylint_py )'


%files -n python3-%{short_name}
%license LICENSE
%doc README.rst
%{_bindir}/pyls
%{python3_sitelib}/pyls
%{python3_sitelib}/python_language_server-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.31.10-4
- Rebuilt for Python 3.9

* Sun May 03 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.31.10-3
- Drop BR on configparser (python2 only)

* Mon Apr 27 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.31.10-2
- Enable tests
- Disable incompatible tests

* Thu Apr 23 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.31.10-1
- Fix license field
- Update to 0.31.10
- Fix requires list

* Wed Apr 22 2020 Mukundan Ragavan <nonamedotc@gmail.com> - 0.31.9-1
- Initial package.
