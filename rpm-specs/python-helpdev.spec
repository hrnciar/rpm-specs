# Created by pyp2rpm-3.3.2
%global pypi_name helpdev

%global _description %{expand:
Helping users and developers to get information about the environment to report
bugs or even test your system without spending a day on it. It can get
information about hardware, OS, paths, Python distribution and packages,
including Qt-things.}

Name:           python-%{pypi_name}
Version:        0.6.10
Release:        4%{?dist}
Summary:        HelpDev - Extracts information about the Python environment easily

License:        MIT
URL:            https://gitlab.com/dpizetta/helpdev
Source0:        https://files.pythonhosted.org/packages/source/h/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# license file not in pypi tarball
Source1:        https://gitlab.com/dpizetta/%{pypi_name}/raw/master/LICENSE.rst
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(psutil) >= 5.6
Requires:       python3dist(setuptools)

%description -n python3-%{pypi_name}
%_description

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
cp %{SOURCE1} .

# importlib.metadata is in python3.8
# https://gitlab.com/dpizetta/helpdev/merge_requests/1
sed -i "s|'importlib_metadata', ||" setup.py
sed -i "s|import importlib_metadata|import importlib.metadata as importlib_metadata|" helpdev/__init__.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE.rst
%{_bindir}/helpdev
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.10-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 23 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.6.10-2
- Fix spec issues

* Sat Dec 21 2019 Mukundan Ragavan <nonamedotc@gmail.com> - 0.6.10-1
- Initial package.
