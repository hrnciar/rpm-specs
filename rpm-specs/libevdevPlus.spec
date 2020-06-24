Name:     libevdevPlus
Version:  0.1.1
Release:  5%{?dist}
Summary:  A C++ wrapper around libevdev
License:  MIT
URL:      https://github.com/YukiWorkshop/libevdevPlus
Source0:  %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:   libevdevPlus-patch0-fix-version

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: make

%description
A c++ wrapper around libevdev (required for ydotool).

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains header files for %{name}.

%prep
%autosetup

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} ..
%make_build

%install
%make_install -C %{_target_platform}
rm -f %{buildroot}%{_libdir}/%{name}.a

%files
%{_libdir}/%{name}.so.0*

%doc README.md

%license LICENSE

%files devel
%{_libdir}/%{name}.so
%{_includedir}/evdevPlus/
%{_libdir}/pkgconfig/*

%changelog
* Sun Mar 29 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.1-5
- fix version in pkgconfig

* Sat Mar 28 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.1-4
- Changes per RHBZ#1808278 and 1808276

* Thu Mar 26 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.1-3
- fix globbing of shared library name
- move pkgconfig files to devel package

* Sun Mar 22 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.1-2
- Changes per RHBZ#1808278

* Sat Feb 29 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.1-1
- Initial version of the package
