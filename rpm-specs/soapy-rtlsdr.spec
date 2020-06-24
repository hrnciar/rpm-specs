Name:           soapy-rtlsdr
Version:        0.3.0
Release:        1%{?dist}
Summary:        SoapySDR module for RTL-SDR hardware

License:        MIT
URL:            https://github.com/pothosware/SoapyRTLSDR
Source0:        https://github.com/pothosware/SoapyRTLSDR/archive/%{name}-%{version}.tar.gz

BuildRequires:  cmake gcc-c++ SoapySDR-devel rtl-sdr-devel

%description
SoapyRTLSDR is a plug-in module for SoapySDR adding support for
RTL-SDR hardware.

%prep
%autosetup -n %{name}-%{version}

%build
mkdir build
cd build
%cmake ..
%make_build


%install
cd build
%make_install


%ldconfig_scriptlets
%files
%license LICENSE.txt
%{_libdir}/SoapySDR/modules0.7/librtlsdrSupport.so

%changelog
* Sun Apr 12 2020 Matt Domsch <matt@domsch.com> 0.3.0-1
- Upstream 0.3.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug  7 2018 Matt Domsch <matt@domsch.com> 0.2.5-1
- initial Fedora packaging
