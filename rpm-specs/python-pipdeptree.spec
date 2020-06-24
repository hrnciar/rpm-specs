%global srcname pipdeptree

%global _description\
pipdeptree is a command line utility for displaying the installed python\
packages in form of a dependency tree. It works for packages installed\
globally on a machine as well as in a virtualenv.

Name:           python-%{srcname}
Version:        0.13.2
Release:        6%{?dist}
Summary:        Command line utility to show dependency tree of packages

License:        MIT
URL:            https://github.com/naiquevin/pipdeptree
Source0:        https://github.com/naiquevin/pipdeptree/archive/%{version}/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
# Dependencies for the tests
# BuildRequires:  python3dist(tox)

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

Requires:       python3dist(graphviz)
Requires:       python3dist(pip) >= 6
Requires:       python3dist(setuptools)
%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{_bindir}/pipdeptree
# Ignore the tests directory
%exclude %{python3_sitelib}/tests
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13.2-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 21 2019 Dhanesh B. Sabane <dhanesh95@fedoraproject.org> - 0.13.2-1
- Fix Bug #1697089 - Bump version to 0.13.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 13 2019 Dhanesh B. Sabane <dhanesh95@fedoraproject.org> - 0.13.1-2
- Bump version to 0.13.1 and ignore tests

* Sat Jun 30 2018 Dhanesh B. Sabane <dhanesh95@disroot.org> - 0.12.1-1
- Initial package.
