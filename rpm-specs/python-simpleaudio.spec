%global pypi_name simpleaudio

%global pypi_description The simpleaudio module provides asynchronous, cross-platform, \
dependency-free audio playback capability for Python 3.

Name: python-%{pypi_name}
Summary: Simple, asynchronous audio playback module for Python 3
License: MIT

Version: 1.0.4
Release: 2%{?dist}

URL: https://github.com/hamiltron/py-simple-audio
Source0: %pypi_source

BuildRequires: alsa-lib-devel
BuildRequires: gcc
BuildRequires: python3-devel >= 3.3
BuildRequires: python3-setuptools

%description
%{pypi_description}


%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{pypi_description}


%prep
%autosetup -n %{pypi_name}-%{version}


%build
%py3_build


%install
%py3_install


%files -n python3-%{pypi_name}
%license LICENSE.txt
%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/%{pypi_name}-*.egg-info/


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Artur Iwicki <fedora@svgames.pl> - 1.0.4-1
- Initial packaging
