%global pypi_name sphinxcontrib-log-cabinet
Name:           python-%{pypi_name}
Version:        1.0.1
Release:        5%{?dist}
Summary:        Organize changelog directives in Sphinx docs
License:        BSD
URL:            https://github.com/davidism/sphinxcontrib-log-cabinet
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description %{expand:
Organize changelogs generated by versionadded, versionchanged,
deprecated directives. The log will be sorted by newest to oldest
version. For HTML docs, older versions will be collapsed by default.}

%description %_description


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -n %{pypi_name}-%{version}


%build
%py3_build


%install
%py3_install


%files -n python3-%{pypi_name}
%license LICENSE.rst
%doc README.rst
%doc CHANGES.rst
%{python3_sitelib}/sphinxcontrib
%{python3_sitelib}/sphinxcontrib_log_cabinet-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/sphinxcontrib_log_cabinet-%{version}-py%{python3_version}-nspkg.pth


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-4
- Rebuilt for Python 3.9

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct  5 2019 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.1-1
- New package.
