Name:		libsoundio
Version:	2.0.0
Release:	2%{?dist}
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
mkdir build
cd build
%cmake -DBUILD_STATIC_LIBS=FALSE ../
%make_build
make doc

%install
cd build
%make_install

# install docs
install -m 0644 -pDt %{buildroot}%{_docdir}/%{name}-doc/html html/*

%check
cd build
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
* Tue Jun 23 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.0.0-2
- Minor packaging changes according to the review

* Thu Jun 18 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.0.0-1
- Initial release
