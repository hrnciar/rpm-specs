Name:           soapy-rtlsdr
Version:        0.3.1
Release:        1%{?dist}
Summary:        SoapySDR module for RTL-SDR hardware

License:        MIT
URL:            https://github.com/pothosware/SoapyRTLSDR
Source0:        https://github.com/pothosware/SoapyRTLSDR/archive/soapy-rtl-sdr-%{version}.tar.gz

BuildRequires:  cmake gcc-c++ SoapySDR-devel rtl-sdr-devel

%description
SoapyRTLSDR is a plug-in module for SoapySDR adding support for
RTL-SDR hardware.

%prep
%autosetup -n SoapyRTLSDR-soapy-rtl-sdr-%{version}

%build
%cmake
%cmake_build


%install
%cmake_install


%ldconfig_scriptlets
%files
%license LICENSE.txt
%{_libdir}/SoapySDR/modules0.7/librtlsdrSupport.so

%changelog
* Sun Aug  2 2020 Matt Domsch <matt@domsch.com> 0.3.1-1
- Upstream 0.3.1, changed tagging, tgz name and internal path name
- Fedora 33 cmake updates

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

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
