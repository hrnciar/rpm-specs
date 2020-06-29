%global pypi_name stdlib-list

%global desc %{expand: \
Python Standard Library List -This package includes lists of all of the
standard libraries for Python, along with the code for scraping the official
Python docs to get said lists.Listing the modules in the standard library?
Wait, why on Earth would you care about that?! Because knowing whether or
not a module is part of the standard library will come in}

Name:       python-%{pypi_name}
Version:    0.6.0
Release:    5%{?dist}
Summary:    A list of Python Standard Libraries

License:    MIT
URL:        https://github.com/jackmaney/python-stdlib-list
Source0:    %pypi_source
BuildArch:  noarch

# Enable py3.9
# https://github.com/jackmaney/python-stdlib-list/pull/34
Patch0:     0001-Add-python-3.9.patch
Patch1:     0002-Add-list-for-3.9.patch

%{?python_enable_dependency_generator}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  git-core

%description
%{desc}

%package -n python3-%{pypi_name}
Summary:    %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

# The require not picked up by the dep generator
Requires:   python3dist(sphinx)
Requires:   python3dist(sphinx-rtd-theme)

%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version} -S git
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/stdlib_list
%{python3_sitelib}/stdlib_list-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Jun 06 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.0-5
- Update patch to include lists required by other packages

* Sat Jun 06 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.0-4
- Update for python 3.9
- TODO: enable tests added in next release

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 27 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.6.0-1
- New upstream version

* Mon Nov 11 2019 Ankur Sinha <ankursinha@fedoraproject.org> - 0.5.0-5
- Fix requires
- https://bugzilla.redhat.com/show_bug.cgi?id=1770852

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-3
- Rebuilt for Python 3.8

* Fri Aug 16 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.5.0-2
- Fix comments BZ 1741623

* Thu Aug 15 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.5.0-1
- Initial package.
