%global pypi_name ldapdomaindump

Name:           %{pypi_name}
Version:        0.9.3
Release:        2%{?dist}
Summary:        Active Directory information dumper via LDAP

License:        MIT
URL:            https://github.com/dirkjanm/ldapdomaindump/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Active Directory information dumper via LDAP.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Active Directory information dumper via LDAP.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e '/^#!\//, 1d' ldapdomaindump/__main__.py

%build
%py3_build

%install
%py3_install

%files
%doc Readme.md
%license LICENSE
%{_bindir}/ldapdomaindump
%{_bindir}/ldd2bloodhound
%{_bindir}/ldd2pretty

%files -n python3-%{pypi_name}
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Jun 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.3-2
- Remove shebang (rhbz#1840298)

* Tue Jun 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.3-1
- Add license and readme file
- Update to latest upstream release 0.9.3

* Tue May 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.2-1
- Initial package for Fedora

