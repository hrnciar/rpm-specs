%global pypi_name sphinx-last-updated-by-git

Name:           python-%{pypi_name}
Version:        0.2.2
Release:        1%{?dist}
Summary:        Get the "last updated" time for each Sphinx page from Git

License:        BSD
URL:            https://github.com/mgeier/sphinx-last-updated-by-git/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
Get the "last updated" time for each Sphinx page from Git. This is a little
Sphinx_ extension that does exactly that.It also checks for included files and
other dependencies.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Get the "last updated" time for each Sphinx page from Git. This is a little
Sphinx_ extension that does exactly that.It also checks for included files and
other dependencies.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sphinx_last_updated_by_git

%files -n python3-%{pypi_name} -f %pyproject_files
%license LICENSE
%doc README.rst

%changelog
* Tue Sep 15 2020 Charalampos Stratakis <cstratak@redhat.com> - 0.2.2-1
- Update to 0.2.2
- Convert the package to pyproject macros

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-2
- Rebuilt for Python 3.9

* Fri May 15 2020 Charalampos Stratakis <cstratak@redhat.com> - 0.2.1-1
- Initial package.