%global catch_version 1.9.6
%global benchmark_version 1.2.0
%global variant_version 1.1.5

%global debug_package %{nil}

Name:           geometry-hpp
Version:        2.0.3
Release:        1%{?dist}
Summary:        Generic C++ interfaces for geometry types, collections, and features

License:        ISC
URL:            https://github.com/mapbox/geometry.hpp
Source0:        https://github.com/mapbox/geometry.hpp/archive/v%{version}/%{name}-%{version}.tar.gz
# Rip out mason stuff - we use our own packages
Patch0:         geometry-hpp-mason.patch

BuildRequires:  cmake gcc-c++
BuildRequires:  catch1-devel >= %{catch_version}
BuildRequires:  google-benchmark-devel >= %{benchmark_version}
BuildRequires:  mapbox-variant-devel >= %{variant_version}
BuildRequires:  mapbox-variant-static >= %{variant_version}

%description
Provides header-only, generic C++ interfaces for geometry
types, geometry collections, and features.

These types are designed to be easy to parse and serialize
to GeoJSON and to be a robust and high performance container
for data processing and conversion.


%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

Requires:       mapbox-variant-devel >= %{variant_version}

%description    devel
Provides header-only, generic C++ interfaces for geometry
types, geometry collections, and features.

These types are designed to be easy to parse and serialize
to GeoJSON and to be a robust and high performance container
for data processing and conversion.


%prep
%autosetup -p 1 -n geometry.hpp-%{version}


%build
%make_build release CXXFLAGS="%{optflags}" WERROR="false"


%install
mkdir -p %{buildroot}%{_includedir}
cp -pr include/mapbox %{buildroot}%{_includedir}


%check
%make_build test


%files devel
%doc README.md
%license LICENSE
%{_includedir}/mapbox


%changelog
* Wed Jul 29 2020 Tom Hughes <tom@compton.nu> - 2.0.3-1
- Update to 2.0.3 upstream release

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Tom Hughes <tom@compton.nu> - 2.0.1-1
- Update to 2.0.1 upstream release

* Tue Jun 30 2020 Tom Hughes <tom@compton.nu> - 1.1.0-1
- Update to 1.1.0 upstream release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Tom Hughes <tom@compton.nu> - 1.0.0-1
- Update to 1.0.0 upstream release

* Sat Jul 21 2018 Tom Hughes <tom@compton.nu> - 0.9.3-1
- Update to 0.9.3 upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul  8 2017 Tom Hughes <tom@compton.nu> - 0.9.2-1
- Update to 0.9.2 upstream release

* Sun Apr  9 2017 Tom Hughes <tom@compton.nu> - 0.9.1-1
- Initial build of 0.9.1
