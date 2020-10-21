%global srcname spdx-lookup

Name:		python-spdx-lookup	
Version:	0.3.2
Release:	4%{?dist}
Summary:	SPDX license list query tool

License:	BSD
URL:		https://github.com/bbqsrc/spdx-lookup-python
Source0:	%pypi_source
BuildArch:	noarch

%description
A tool to query the SPDX license list.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:	SPDX license list query tool
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:	python%{python3_pkgversion}-devel
Requires:	python%{python3_pkgversion}-spdx

%description -n python%{python3_pkgversion}-%{srcname}
A tool to query the SPDX license list.

%prep
%setup -q -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/spdx_lookup/
%{python3_sitelib}/spdx_lookup-*.egg-info/
%{_bindir}/spdx-lookup

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 29 2019 Jeremy Bertozzi <jeremy.bertozzi@gmail.com> - 0.3.2-1
- Initial package
