%global version_major 0
%global version_minor 8
%global version_micro 1

Name:           sdbus-cpp
Version:        %{version_major}.%{version_minor}.%{version_micro}
Release:        1%{?dist}
Summary:        High-level C++ D-Bus library

License:        LGPLv2
URL:            https://github.com/Kistler-Group/sdbus-cpp
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  cmake >= 3.12
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libsystemd) >= 236

%description
High-level C++ D-Bus library for Linux designed to provide easy-to-use
yet powerful API in modern C++

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.

%package devel-doc
Summary:        Developer documentation for %{name}
BuildArch:      noarch
BuildRequires:  doxygen

%description devel-doc
Developer documentation for %{name}

%package xml2cpp
Summary:        Stub code generator for sdbus-c++
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  pkgconfig(expat)

%description xml2cpp
The stub code generator for generating the adapter and proxy interfaces
out of the D-Bus IDL XML description.


%prep
%autosetup -n %{name}-%{version}


%build
%cmake . \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_CODE_GEN=ON \
    -DBUILD_DOXYGEN_DOC=ON
%make_build
%make_build doc


%install
%make_install


%files
%license %{_docdir}/sdbus-c++/COPYING
%dir %{_docdir}/sdbus-c++
%doc %{_docdir}/sdbus-c++/AUTHORS
%doc %{_docdir}/sdbus-c++/ChangeLog
%doc %{_docdir}/sdbus-c++/NEWS
%doc %{_docdir}/sdbus-c++/README
%{_libdir}/libsdbus-c++.so.%{version_major}
%{_libdir}/libsdbus-c++.so.%{version}
%dir %{_libdir}/cmake/sdbus-c++
%{_libdir}/cmake/sdbus-c++/*.cmake

%files devel
%{_libdir}/pkgconfig/sdbus-c++.pc
%{_libdir}/libsdbus-c++.so
%{_includedir}/*

%files devel-doc
%dir %{_docdir}/sdbus-c++
%doc %{_docdir}/sdbus-c++/*

%files xml2cpp
%{_bindir}/sdbus-c++-xml2cpp


%changelog
* Fri Feb 7 2020 Marek Blaha <mblaha@redhat.com> - 0.8.1-1
- Update to release 0.8.1

* Fri Jan 24 2020 Marek Blaha <mblaha@redhat.com> - 0.7.8-1
- Initial release 0.7.8
