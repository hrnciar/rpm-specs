Name:		soapy-uhd
Version:	0.3.6
Release:	1%{?dist}
Summary:	Soapy SDR plugins for UHD supported SDR devices
License:	GPLv3
URL:		https://github.com/pothosware/SoapyUHD
Source:		%{URL}/archive/%{name}-%{version}.tar.gz
BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	uhd-devel
BuildRequires:	SoapySDR-devel
BuildRequires:	boost-devel
# For module directories
Requires:	uhd
Requires:	SoapySDR

%description
Soapy SDR plugins for UHD supported SDR devices.

%prep
%setup -q -n SoapyUHD-%{name}-%{version}

%build
mkdir build
cd build
%cmake ../
%make_build

%install
cd build
%make_install

%files
%license COPYING
%doc README.md Changelog.txt
%{_libdir}/SoapySDR/modules*.*/*.so
%{_libdir}/uhd/modules/*.so

%changelog
* Thu Apr 16 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.3.6-1
- Initial version
