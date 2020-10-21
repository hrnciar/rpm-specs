# Created by pyp2rpm-3.3.4
%global pypi_name urlbuster

Name:           %{pypi_name}
Version:        0.5.0
Release:        2%{?dist}
Summary:        URL bruteforcer to locate files or directories

License:        MIT
URL:            https://github.com/cytopia/urlbuster
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Powerful web directory fuzzer to locate existing and/or hidden files or
directories.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Powerful web directory fuzzer to locate existing and/or hidden files or
directories.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files
%{_bindir}/%{pypi_name}
%{_datadir}/%{pypi_name}/

%files -n python3-%{pypi_name}
%doc README.md examples/
%license LICENSE.txt
%{_bindir}/urlbuster
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sun Aug 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.0-2
- Add examples (rhbz#1856864)

* Tue Jul 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.0-1
- Initial package for Fedora
