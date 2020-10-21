Name:		libsoundio
Version:	2.0.0
Release:	5%{?dist}
Summary:	C library for cross-platform real-time audio input and output
License:	MIT
URL:		http://libsound.io/
Source0:	http://github.com/andrewrk/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	alsa-lib-devel
BuildRequires:	cmake
BuildRequires:	coreutils
BuildRequires:	doxygen
BuildRequires:	gcc
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	pulseaudio-libs-devel

%description
C library providing cross-platform audio input and output. The API is suitable
for real-time software such as digital audio workstations as well as consumer
software such as music players.

%package devel
Summary:	Development files for libsoundio
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for libsoundio.

%package doc
Summary:	Documentation for libsoundio
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for libsoundio.

%package utils
Summary:	Utilities for libsoundio

%description utils
Utilities files for libsoundio.

%prep
%setup -q

%build
%cmake -DBUILD_STATIC_LIBS=FALSE
%cmake_build
cd %{__cmake_builddir}
make doc

%install
%cmake_install

# install docs
cd %{__cmake_builddir}
install -m 0644 -pDt %{buildroot}%{_docdir}/%{name}-doc/html html/*

%check
cd %{__cmake_builddir}
./unit_tests
./overflow
./underflow

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_libdir}/libsoundio.so.*

%files devel
%{_includedir}/soundio
%{_libdir}/libsoundio.so

%files doc
%doc %{_docdir}/%{name}-doc/html
%doc example

%files utils
%{_bindir}/sio_list_devices
%{_bindir}/sio_microphone
%{_bindir}/sio_record
%{_bindir}/sio_sine

%changelog
* Thu Aug  6 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.0.0-5
- Fixed FTBFS
  Resolves: rhbz#1864049

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.0.0-2
- Minor packaging changes according to the review

* Thu Jun 18 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.0.0-1
- Initial release
