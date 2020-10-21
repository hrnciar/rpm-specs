
%global srcname fastprogress

Name: python-%{srcname}
Version: 1.0.0
Release: 1%{?dist}
Summary: Progress bar for Jupyter Notebook and console 

License: ASL 2.0
URL: https://github.com/fastai/fastprogress
Source0: %{pypi_source}

BuildArch: noarch

%global _description %{expand:
A Python-based, fast and simple progress bar 
for Jupyter Notebook and console.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Sun Oct 18 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 1.0.0-1
- New upstream (1.0.0)
- Add BuildReq python-setuptools

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.2.3-1
- Initial spec file

