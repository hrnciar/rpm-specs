%global pypi_name badchars
%{?python_disable_dependency_generator}

Name:           %{pypi_name}
Version:        0.4.0
Release:        4%{?dist}
Summary:        HEX bad char generator for different programming languages

License:        MIT
URL:            https://github.com/cytopia/badchars
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
A HEX bad char generator to instruct encoders such as shikata-ga-nai to
transform those to other chars.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A HEX bad char generator to instruct encoders such as shikata-ga-nai to
transform those to other chars.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files
%{_bindir}/%{pypi_name}

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Sep 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.0-4
- Disable dependency generator (rhbz#1871463) 

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.0-2
- Remove requirement (rhbz#1856891)

* Tue Jul 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.0-1
- Initial package for Fedora
