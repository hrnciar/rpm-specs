# cpptoml is header only, so there's no debuginfo
%global debug_package %{nil}

Name:           cpptoml
Version:        0.1.1
Release:        2%{?dist}
Summary:        Header-only C++ TOML library 

License:        MIT
URL:            https://github.com/skystrife/cpptoml
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		0001-Modify-build-to-use-GNUInstallDirs.patch

BuildRequires:  cmake >= 3.1.0
BuildRequires:	make
BuildRequires:  gcc-c++

%description
A header-only library for parsing TOML configuration files.

Supports TOML v0.5.0.

This includes support for the new DateTime format, inline tables, multi-line
basic and raw strings, digit separators, hexadecimal integers, octal integers,
binary integers, and float special values.


%package devel
Summary:	Header files for cpptoml


%description devel
Header files to develop applications that use the TOML format.

Supports TOML v0.5.0.

This includes support for the new DateTime format, inline tables, multi-line
basic and raw strings, digit separators, hexadecimal integers, octal integers,
binary integers, and float special values.


%prep
%autosetup -p1


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%cmake .. -DCPPTOML_BUILD_EXAMPLES=OFF
popd


%install
%make_install -C %{_target_platform}


%files devel
%license LICENSE
%doc README.md
%{_includedir}/cpptoml.h
%{_libdir}/cmake/cpptoml/


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Dakota Williams <raineforest@raineforest.me> 0.1.1-1
- Initial packaging 
