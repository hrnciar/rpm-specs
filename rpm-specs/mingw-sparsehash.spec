%{?mingw_package_header}

%global mingw_pkg_name sparsehash

Name:           mingw-%{mingw_pkg_name}
Version:        2.0.3
Release:        2%{?dist}
Summary:        MinGW Extremely memory-efficient C++ hash_map implementation

License:        BSD
URL:            https://github.com/sparsehash/sparsehash
Source0:        %{url}/archive/sparsehash-%{version}.tar.gz
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildArch:      noarch

%description
The Google SparseHash project contains several C++ template hash-map
implementations with different performance characteristics, including
an implementation that optimizes for space and one that optimizes for
speed.

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:        %{summary}

%description -n mingw32-%{mingw_pkg_name}
The Google SparseHash project contains several C++ template hash-map
implementations with different performance characteristics, including
an implementation that optimizes for space and one that optimizes for
speed.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:        %{summary}

%description -n mingw64-%{mingw_pkg_name}
The Google SparseHash project contains several C++ template hash-map
implementations with different performance characteristics, including
an implementation that optimizes for space and one that optimizes for
speed.

%prep
%autosetup -n %{mingw_pkg_name}-%{mingw_pkg_name}-%{version}

%build
%mingw_configure
%mingw_make %{?_smp_mflags}

%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

# Remove unneeded files
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}

%files -n mingw32-%{mingw_pkg_name}
%license COPYING
%doc AUTHORS NEWS README TODO
%{mingw32_includedir}/google/
%{mingw32_includedir}/sparsehash/
%{mingw32_libdir}/pkgconfig/libsparsehash.pc

%files -n mingw64-%{mingw_pkg_name}
%license COPYING
%doc AUTHORS NEWS README TODO
%{mingw64_includedir}/google/
%{mingw64_includedir}/sparsehash/
%{mingw64_libdir}/pkgconfig/libsparsehash.pc

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.0.3-1
- update to 2.0.3

* Sat Aug 25 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.0.2-1
- create from native spec
