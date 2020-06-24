%global pypi_name kerberoast

Name:           %{pypi_name}
Version:        0.1.0
Release:        2%{?dist}
Summary:        Kerberos security toolkit for Python

License:        MIT
URL:            https://github.com/skelsec/kerberoast
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Python-based Kerberos security toolkit.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python-based Kerberos security toolkit.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e '/^#!\//, 1d' kerberoast/kerberoast.py

%build
%py3_build

%install
%py3_install

%files
%{_bindir}/kerberoast

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-2
- Rebuilt for Python 3.9

* Wed Apr 15 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.0-1
- Update to new upstream version 0.1.0

* Thu Mar 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.9-1
- Initial package for Fedora
