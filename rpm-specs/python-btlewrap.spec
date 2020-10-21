%global pypi_name btlewrap

Name:           python-%{pypi_name}
Version:        0.1.0
Release:        1%{?dist}
Summary:        Wrapper around different bluetooth low energy backends

License:        MIT
URL:            https://github.com/ChristianKuehnel/btlewrap
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Bluetooth LowEnergy wrapper for different python backends. This gives you a
nice API so that you can use different Bluetooth implementations on different
platforms.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(bluepy)
BuildRequires:  python3dist(pygatt)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Bluetooth LowEnergy wrapper for different python backends. This gives you a
nice API so that you can use different Bluetooth implementations on different
platforms.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
chmod -x README.rst

%build
%py3_build

%install
%py3_install

%check
%pytest -v test -k "not test_bluepy and not test_pygatt and not test_gatttool"

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%exclude %{python3_sitelib}/test
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Oct 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.0-1
- Update to latest upstream release 0.1.0

* Wed Sep 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.10-1
- Initial package for Fedora