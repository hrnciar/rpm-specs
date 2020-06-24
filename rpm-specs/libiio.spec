Name:          libiio
Version:       0.21
Release:       1%{?dist}
Summary:       Library for Industrial IO
License:       LGPLv2
URL:           https://analogdevicesinc.github.io/libiio/
Source0:       https://github.com/analogdevicesinc/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: bison
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: flex
BuildRequires: gcc
BuildRequires: libserialport-devel
BuildRequires: libaio-devel
BuildRequires: libusbx-devel
BuildRequires: libxml2-devel
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme

%description
Library for interfacing with Linux IIO devices

libiio is used to interface to Linux Industrial Input/Output (IIO) Subsystem.
The Linux IIO subsystem is intended to provide support for devices that in some 
sense are analog to digital or digital to analog converters (ADCs, DACs). This 
includes, but is not limited to ADCs, Accelerometers, Gyros, IMUs, Capacitance 
to Digital Converters (CDCs), Pressure Sensors, Color, Light and Proximity 
Sensors, Temperature Sensors, Magnetometers, DACs, DDS (Direct Digital 
Synthesis), PLLs (Phase Locked Loops), Variable/Programmable Gain Amplifiers 
(VGA, PGA), and RF transceivers.

%package utils
Summary: Utilities for Industrial IO
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
Utilities for accessing IIO using libiio

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%package doc
Summary: Development documentation for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description doc
Documentation for development with %{name}.

%package -n python3-iio
Summary: Python 3 bindings for Industrial IO (libiio)
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n python3-iio
Python 3 bindings for Industrial IO

%prep
%autosetup -p1
sed -i 's/${LIBIIO_VERSION_MAJOR}-doc//' CMakeLists.txt

%build
%cmake -DPYTHON_BINDINGS=on -DWITH_DOC=on .
%make_build

%install
%make_install

#Remove libtool archives.
find %{buildroot} -name '*.la' -delete

%ldconfig_scriptlets

%files
%license COPYING.txt
%{_libdir}/%{name}.so.*
/lib/udev/rules.d/90-libiio.rules

%files utils
%{_bindir}/iio_*
%{_sbindir}/iiod

%files devel
%{_includedir}/iio.h
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}.so

%files doc
%doc %{_docdir}/%{name}

%files -n python3-iio
%{python3_sitelib}/__pycache__/iio*
%{python3_sitelib}/iio*
%{python3_sitelib}/libiio*

%changelog
* Tue Jun 23 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.21-1
- Update to 0.21

* Sat Jun 06 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.20-1
- Update to 0.20

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.19-2
- Rebuilt for Python 3.9

* Sat Feb 15 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.19-1
- Update to 0.19

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.18-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.18-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 12 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.18-1
- Update to 0.18

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 27 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.17-1
- Update to 0.17
- Enable IIOD USB/AIO backend

* Thu Nov 22 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.16-1
- Update to 0.16

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.15-2
- Rebuilt for Python 3.7

* Wed May 23 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.15-1
- Update to 0.15

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.14-1
- Update to 0.14

* Fri Dec 22 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.12-1
- Update to 0.12

* Wed Oct 25 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.11-1
- Update to 0.11

* Wed Aug 16 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.10-1
- Update to 0.10
- Review updates

* Wed Feb 22 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.9-1
- Initial package
