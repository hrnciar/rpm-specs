%global pypi_name python-markdown-math
%global srcname markdown-math

Name:           python-%{srcname}
Version:        0.7
Release:        2%{?dist}
Summary:        Math extension for Python-Markdown

License:        BSD
URL:            https://github.com/mitya57/python-markdown-math
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(markdown)

%description
Extension for Python-Markdown: this extension adds math
formulas support to Python-Markdown.

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Extension for Python-Markdown: this extension adds math
formulas support to Python-Markdown.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} test.py


%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/mdx_math.py
%{python3_sitelib}/python_markdown_math-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul  6 2020 José Matos <jamatos@fedoraproject.org> - 0.7-1
- update to 0.7
- remove requires python3dist(setuptools) since it used just during installation

* Sun May 03 2020 José Matos <jamatos@fedoraproject.org> - 0.6-1
- Initial package.
