# Created by pyp2rpm-3.3.2
%global pypi_name versioneer

%global _description %{expand:
Versioneer is a tool to automatically update version strings (in setup.py and
the conventional 'from PROJECT import _version' pattern) by asking your
version-control system about the current tree.}


Name:           python-%{pypi_name}
Version:        0.18
Release:        6%{?dist}
Summary:        Easy VCS-based management of project version strings

License:        Public Domain
URL:            https://github.com/warner/python-versioneer
Source0:        https://files.pythonhosted.org/packages/source/v/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(setuptools)

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README.md
%{_bindir}/versioneer
%{python3_sitelib}/__pycache__/%{pypi_name}*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.18-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 31 2019 Mukundan Ragavan <nonamedotc@gmail.com> - 0.18-3
- rebuild

* Mon Dec 30 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.18-2
- Address changes from package review

* Sun Dec 22 2019 Mukundan Ragavan <nonamedotc@gmail.com> - 0.18-1
- Initial package.
