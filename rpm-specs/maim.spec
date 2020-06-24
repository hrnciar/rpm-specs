Name:			maim
Version:		5.5.3
Release:		2%{?dist}
Summary:		Command-line screen capture tool

License:		GPLv3
URL:			https://github.com/naelstrof/maim
Source0:		https://github.com/naelstrof/maim/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	libX11-devel
BuildRequires:	libXrender-devel
BuildRequires:	libXfixes-devel
BuildRequires:	libXrandr-devel
BuildRequires:	libXcomposite-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
BuildRequires:	mesa-libGL-devel
BuildRequires:	glm-devel
BuildRequires:	libslopy-devel

%description
maim (make image) is a screenshot utility that provides options for capturing
predetermined or user selected regions of your desktop.

%prep
%autosetup

%build
%cmake .
%make_build

%install
%make_install

%check
ctest -V %{?_smp_mflags}

%files
%doc README.md
%{_bindir}/maim
%{_mandir}/man1/maim.1.*

%license COPYING license.txt

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 19 2019 Aymen Qader <qader.aymen@gmail.com> 5.5.3-1
- Initial version of the package
