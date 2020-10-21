# Created by pyp2rpm-3.3.4
%global pypi_name authheaders

Name:           python-%{pypi_name}
Version:        0.13.0
Release:        1%{?dist}
Summary:        A library wrapping email authentication header verification and generation

# Licensing described in LICENSE file
License:        MIT and zlib and ZPLv2.1
URL:            https://github.com/ValiMail/authentication-headers
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(authres) >= 1.0.1
BuildRequires:  python3dist(dkimpy) >= 0.7.1
BuildRequires:  python3dist(dnspython)
BuildRequires:  python3dist(publicsuffix2)
BuildRequires:  python3dist(setuptools)

%description
%{summary}.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       publicsuffix-list

%description -n python3-%{pypi_name}
%{summary}.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Remove bundled publicsuffix data
rm -f %{pypi_name}/public_suffix_list.txt

%build
%py3_build

%install
%py3_install
# Use public suffix data from installed RPM
ln -sr %{buildroot}%{_datadir}/publicsuffix/public_suffix_list.dat %{buildroot}%{python3_sitelib}/%{pypi_name}/public_suffix_list.txt

%files -n python3-%{pypi_name}
%doc README.md
%license COPYING
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Oct 15 2020 Neal Gompa <ngompa13@gmail.com> - 0.13.0-1
- Initial package.
