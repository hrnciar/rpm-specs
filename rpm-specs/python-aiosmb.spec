%global pypi_name aiosmb

Name:           python-%{pypi_name}
Version:        0.2.28
Release:        1%{?dist}
Summary:        Asynchronous SMB protocol implementation

License:        MIT
URL:            https://github.com/skelsec/aiosmb
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Fully asynchronous SMB library written in pure Python.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Fully asynchronous SMB library written in pure Python.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
rm -rf external
# Remove shebang
sed -i -e '/^#!\//, 1d' aiosmb/{authentication/spnego/asn1_structs.py,\
authentication/spnego/native.py,authentication/spnego/sspi.py,\
commons/connection/target.py,crypto/pure/RC4/RC4.py}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
# Missing license file: https://github.com/skelsec/aiosmb/pull/4
#%license LICENSE
%{_bindir}/asmbclient
%{_bindir}/asmbshareenum
%{_bindir}/asmbprotocolenum
%{_bindir}/asmbosenum
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Fri Sep 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.28-1
- Update to latest upstream release 0.2.28 (#1882047)

* Thu Sep 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.27-1
- Update to latest upstream release 0.2.27 (#1879298)

* Mon Jul 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.26-1
- Update to latest upstream release 0.2.26

* Mon Jun 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.20-1
- Update to latest upstream release 0.2.20

* Sun Apr 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.2.10-1
- Initial package for Fedora

