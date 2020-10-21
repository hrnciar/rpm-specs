Name: liblcf
Summary: Library to handle RPG Maker 2000/2003 game data

# liblcf itself if MIT, but it uses some example code
# from the "inih" library, which is BSD-licensed.
# 
# BSD-licensed:
# - src/ini.cpp (removed before build)
# - src/ini.h   (removed before build)
# - src/inireader.cpp
# - src/inireader.h
License: MIT and BSD

Version: 0.6.2
Release: 3%{?dist}

URL: https://github.com/EasyRPG/liblcf
Source0: %{URL}/archive/%{version}/%{name}-%{version}.tar.gz

Patch0: %{name}--unbundle-inih.patch

BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: make

BuildRequires: expat-devel
BuildRequires: inih-devel
BuildRequires: libicu-devel

%description
%{name} is a library to handle RPG Maker 2000/2003 game data.
It can read and write LCF and XML files.

%{name} is part of the EasyRPG Project.


%package devel
Summary: Development files for %{name}
Requires: %{name}%{?isa} = %{version}-%{release}

%description devel
This package contains files required to develop applications using %{name}.


%package doc
Summary: Documentation for %{name}
BuildArch: noarch

%description doc
This package contains documentation (in HTML format) for %{name}.


%prep
%setup -q
%patch0 -p1


%build
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-DDISABLE_TOOLS=OFF \
	-DDISABLE_UPDATE_MIMEDB=ON \
	./
%cmake_build
%cmake_build --target liblcf_doc


%install
%cmake_install


%check
%cmake_build --target check


%files
%license COPYING
%{_libdir}/%{name}.so.*
%{_datadir}/mime/packages/%{name}*.xml


%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc


%files doc
%license COPYING
%doc doc/*


%changelog
* Sun Aug 02 2020 Artur Iwicki <fedora@svgames.pl> - 0.6.2-3
- Build and install documentation (in -doc subpackage)
- Build and run tests

* Sat Aug 01 2020 Artur Iwicki <fedora@svgames.pl> - 0.6.2-2
- Unbundle the inih library
- Disable the automatic mimedb update during install

* Fri Jul 31 2020 Artur Iwicki <fedora@svgames.pl> - 0.6.2-1
- Initial packaging
