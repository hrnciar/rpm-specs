%global appname wloc

%global appsum Simple Wi-Fi geolocation library and tool
%global appdesc Simple Wi-Fi geolocation library and tool by EasyCoding Team

Name: python-%{appname}
Version: 0.4.0
Release: 3%{?dist}

BuildArch: noarch
Summary: %{appsum}
License: GPLv3+
URL: https://github.com/xvitaly/%{appname}
Source0: %{url}/archive/v%{version}/%{appname}-%{version}.tar.gz

BuildRequires: python3dist(python-networkmanager)
BuildRequires: python3dist(requests)
BuildRequires: python3-devel
BuildRequires: doxygen

%description
%{appdesc}.

%package -n python3-%{appname}
Summary: %{appsum}
Requires: python3dist(python-networkmanager)
%{?python_provide:%python_provide python3-%{appname}}

%description -n python3-%{appname}
%{appdesc}.

%prep
%autosetup -n %{appname}-%{version} -p1
rm -f docs/README.md

%build
doxygen
%py3_build

%install
%py3_install

%files -n python3-%{appname}
%license COPYING
%doc README.md docs/*.md docs/html
%{_bindir}/%{appname}
%{python3_sitelib}/%{appname}
%{python3_sitelib}/%{appname}-*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 24 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.0-1
- Updated to version 0.4.0.
