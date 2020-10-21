%global pypi_name devtools

Name:           python-%{pypi_name}
Version:        0.6
Release:        1%{?dist}
Summary:        Dev tools for Python

License:        MIT
URL:            https://github.com/samuelcolvin/python-devtools
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
The debug print command Python never had (and other things).

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pygments
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-isort
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest-sugar
BuildRequires:  python3-pytest-toolbox
BuildRequires:  python3-numpy
BuildRequires:  python3-multidict
%{?python_provide:%python_provide python3-%{pypi_name}}
 
%description -n python3-%{pypi_name}
The debug print command Python never had (and other things).

%package -n python-%{pypi_name}-doc
Summary:        %{name} documentation

BuildRequires:  python3-ansi2html
BuildRequires:  python3-pygments
BuildRequires:  mkdocs
BuildRequires:  python3-markdown
#BuildRequires:  mkdocs-exclude=
BuildRequires:  mkdocs-material
#BuildRequires:  python-markdown-include

%description -n python-%{pypi_name}-doc
Documentation for %{name}.

%prep
%autosetup -n python-%{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# mkdocs build

%install
%py3_install

#%check
#PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests \
#  -k "not test_exotic_types and not test_kwargs_multiline and not test_small_call_frame_warning and not test_multiple"

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%files -n python-%{pypi_name}-doc
#%doc site
%license LICENSE

%changelog
* Sat Aug 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.6-1
- Update to latest upstream release 0.6
- Fix FTBFS (rhbz#1842118)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-4
- Rebuilt for Python 3.9

* Fri Mar 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.1-3
- Exclude three failing tests
- Use license from tarball

* Mon Jan 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.1-2
- Fix description
- Add license (rhbz#1787452)

* Thu Jan 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.1-1
- Initial package for Fedora
