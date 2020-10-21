# Created by pyp2rpm-3.3.4
%global pypi_name rich

Name:           python-%{pypi_name}
Version:        8.0.0
Release:        1%{?dist}
Summary:        Render rich text and beautiful formatting in the terminal

License:        MIT
URL:            https://github.com/willmcgugan/rich
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Rich is a Python library for rich text and beautiful formatting in the terminal.
The Rich API makes it easy to add color and style to terminal output. Rich can
also render pretty tables, progress bars, markdown, syntax highlighted source
code, tracebacks, and more — out of the box.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Rich is a Python library for rich text and beautiful formatting in the terminal.
The Rich API makes it easy to add color and style to terminal output. Rich can
also render pretty tables, progress bars, markdown, syntax highlighted source
code, tracebacks, and more — out of the box.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Sun Oct 18 16:38:50 IST 2020 Parag Nemade <pnemade AT redhat DOT com> - 8.0.0-1
- Update to 8.0.0 version (#1884915)

* Thu Oct  1 08:41:03 IST 2020 Parag Nemade <pnemade AT redhat DOT com> - 7.1.0-1
- Update to 7.1.0 version (#1882733)

* Wed Aug 26 2020 Parag Nemade <pnemade AT redhat DOT com> - 6.0.0-1
- Initial package.
