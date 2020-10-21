%global debug_package %{nil}

Name:           robin-map
Version:        0.6.3
Release:        3%{?dist}
Summary:        C++ implementation of a fast hash map and hash set using robin hood hashing

License:        MIT
URL:            https://github.com/Tessil/robin-map
Source0:        https://github.com/Tessil/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  cmake gcc-c++
BuildRequires:  boost-devel

%description
The robin-map library is a C++ implementation of a fast hash map and hash set
using open-addressing and linear robin hood hashing with backward shift
deletion to resolve collisions.

*** This is a header only library. ***
The package you want is %{name}-devel.


%package devel
Summary:        %{summary}

%description devel
The robin-map library is a C++ implementation of a fast hash map and hash set
using open-addressing and linear robin hood hashing with backward shift
deletion to resolve collisions.

Four classes are provided: tsl::robin_map, tsl::robin_set, tsl::robin_pg_map
and tsl::robin_pg_set. The first two are faster and use a power of two growth
policy, the last two use a prime growth policy instead and are able to cope
better with a poor hash function. Use the prime version if there is a chance of
repeating patterns in the lower bits of your hash (e.g. you are storing
pointers with an identity hash function). See GrowthPolicy for details.

A benchmark of tsl::robin_map against other hash maps may be found here. This
page also gives some advices on which hash table structure you should try for
your use case (useful if you are a bit lost with the multiple hash tables
implementations in the tsl namespace).


%prep
%autosetup -p1


%build
%cmake


%install
%cmake_install


%check
pushd tests
%cmake
%cmake_build
%{_vpath_builddir}/tsl_robin_map_tests


%files devel
%license LICENSE
%doc README.md
%{_datadir}/cmake/tsl-%{name}/*.cmake
%{_includedir}/tsl/


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 21 2020 Richard Shaw <hobbes1069@gmail.com> - 0.6.3-1
- Update to 0.6.3.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Richard Shaw <hobbes1069@gmail.com> - 0.6.2-1
- Update to 0.6.2.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Richard Shaw <hobbes1069@gmail.com> - 0.6.1-1
- Update to 0.6.1.

* Tue Feb 12 2019 Richard Shaw <hobbes1069@gmail.com> - 0.6.0-2
- Add patch for GCC 9 warnings.

* Mon Feb 11 2019 Richard Shaw <hobbes1069@gmail.com> - 0.6.0-1
- Update to 0.6.0.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Richard Shaw <hobbes1069@gmail.com> - 0.2.0-1
- Initial packaging.
