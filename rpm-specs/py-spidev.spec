Name:           py-spidev
Version:        3.4
Release:        5%{?dist}
Summary:        A python library for manipulating SPI via spidev
License:        MIT
URL:            https://github.com/doceme/py-spidev/
Source0:        https://github.com/doceme/py-spidev/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
A python module for interfacing with SPI devices from user 
space via the spidev linux kernel driver.

%package -n python3-spidev
Summary:  A python library for manipulating SPI
%{?python_provide:%python_provide python3-spidev}

%description -n python3-spidev
A python module for interfacing with SPI devices from user 
space via the spidev linux kernel driver.


%prep
%autosetup

%build
%py3_build

%install
%py3_install

%files -n python3-spidev
%license LICENSE
%{python3_sitearch}/spidev*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.4-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 30 2019 Peter Robinson <pbrobinson@fedoraproject.org> 3.4-1
- Initial package
