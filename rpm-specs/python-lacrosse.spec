%global pypi_name pylacrosse
%global pkg_name lacrosse

Name:           python-%{pkg_name}
Version:        0.4
Release:        2%{?dist}
Summary:        LaCrosse Python sensor library

License:        LGPLv2+
URL:            http://github.com/hthiery/python-lacrosse
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Python libray to work with the Jeelink USB RF adapter.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pyserial)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(nose)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
Python libray to work with the Jeelink USB RF adapter.

%prep
%autosetup -n %{name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pkg_name}
%doc AUTHORS README.rst
%license COPYING
%{_bindir}/pylacrosse
%{python3_sitelib}/%{pypi_name}/
# Unversioned egg-info: https://github.com/hthiery/python-lacrosse/issues/11
%{python3_sitelib}/%{pypi_name}*py%{python3_version}.egg-info/
%exclude %{python3_sitelib}/tests

%changelog
* Sat Oct 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4-2
- Add missing BR (#1879768)

* Thu Sep 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4-1
- Initial package for Fedora