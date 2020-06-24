%bcond_with tests  # disable tests unless upt is available

%global srcname upt-fedora

Name:		python-upt-fedora	
Version:	0.3
Release:	3%{?dist}
Summary:	Fedora backend for upt

License:	BSD
URL:		https://framagit.org/upt/upt-fedora
Source0:	%pypi_source
BuildArch:	noarch

%description
Fedora backend for upt.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:	Fedora backend for upt
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires: python%{python3_pkgversion}-devel
Requires:	python%{python3_pkgversion}-jinja2
Requires:	upt

%description -n python%{python3_pkgversion}-%{srcname}
Fedora backend for upt.

%prep
%setup -q -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m unittest
%endif

%files -n python%{python3_pkgversion}-%{srcname}
%doc README.md CHANGELOG
%license LICENSE
%{python3_sitelib}/upt_fedora-*.egg-info/
%{python3_sitelib}/upt_fedora/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 29 2019 Jeremy Bertozzi <jeremy.bertozzi@gmail.com> - 0.3-1
- Initial package

