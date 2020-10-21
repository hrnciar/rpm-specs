%global pypi_name vcversioner

Name:           python-%{pypi_name}
Version:        2.16.0.0
Release:        1%{?dist}
Summary:        Use version control tags to discover version numbers

License:        ISC
URL:            https://github.com/habnabit/vcversioner
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
Source1:        COPYING

%description
One can write a setup.py with no version information specified. vcversioner
will find a recent, properly-formatted VCS tag and extract a version from it.
It's much more convenient to be able to use your version control system's
tagging mechanism to derive a version number than to have to duplicate that
information all over the place.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
One can write a setup.py with no version information specified. vcversioner
will find a recent, properly-formatted VCS tag and extract a version from it.
It's much more convenient to be able to use your version control system's
tagging mechanism to derive a version number than to have to duplicate that
information all over the place.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
cp -p %{SOURCE1} .

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license COPYING
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Jul 13 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.16.0.0-1
- Initial package.
- include COPYING