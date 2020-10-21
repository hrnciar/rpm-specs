%global pypi_name pydeps

%global desc %{expand: \
Python module dependency visualization. This package installs the pydeps
command, and normal usage will be to use it from the command line.}

Name:		%{pypi_name}
Version:	1.9.8
Release:	1%{?dist}
Summary:	Display module dependencies
License:	BSD
URL:		https://github.com/thebjorn/pydeps
# Use the github source to build
Source0:	%{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:	noarch

%{?python_enable_dependency_generator}

BuildRequires:	python3-devel
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(stdlib-list)
BuildRequires:	python3dist(pytest)
BuildRequires:	python3dist(pyyaml)
BuildRequires:	python3dist(tox)
BuildRequires:	/usr/bin/dot

%description
%{desc}

Requires:	python3dist(enum34)
Requires:	python3dist(setuptools)
Requires:	python3dist(stdlib-list)
Requires:	python3dist(pytest)
Requires:	python3dist(pyyaml)
Requires:	python3dist(tox)

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
# Exclude failing tests:
# https://github.com/thebjorn/pydeps/issues/71
pytest-%{python3_version} -k "not test_file and not test_file_pylib and not test_file_pyliball and not test_relative_imports_same_name_with_std and not test_relative_imports_same_name_with_std_future and not test_pydeps_colors"

%files -n %{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/pydeps
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Oct 01 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.9.9-1
- Update to new release

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.9.3-2
- Rebuilt for Python 3.9

* Wed May 13 2020 Luis Bazan <lbazan@fedoraproject.org> - 1.9.3-1
- New upstream version

* Thu Apr 23 2020 Luis Bazan <lbazan@fedoraproject.org> - 1.9.0-1
- New upstream version

* Wed Apr 22 2020 Luis Bazan <lbazan@fedoraproject.org> - 1.8.8-1
- Initial package.
