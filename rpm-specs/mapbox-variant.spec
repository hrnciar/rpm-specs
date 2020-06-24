%global debug_package %{nil}

Name:           mapbox-variant
Version:        1.1.6
Release:        3%{?dist}
Summary:        A header-only alternative to boost::variant for C++11 and C++14

License:        Boost and BSD
URL:            https://github.com/mapbox/variant
Source0:        https://github.com/mapbox/variant/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  catch1-devel

%description
Mapbox variant has the same speedy performance of boost::variant but is
faster to compile, results in smaller binaries, and has no dependencies.


%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description    devel
Mapbox variant has the same speedy performance of boost::variant but is
faster to compile, results in smaller binaries, and has no dependencies.


%prep
%autosetup -p 1 -n variant-%{version}
sed -i -e 's/-Werror //' Makefile
sed -i -e 's/-march=native //' Makefile
rm -f test/include/catch.hpp


%build


%install
mkdir -p %{buildroot}%{_includedir}
cp -pr include/mapbox %{buildroot}%{_includedir}


%check
%make_build test CXXFLAGS="-I/usr/include/catch %{optflags}"


%files devel
%doc README.md doc
%license LICENSE LICENSE_1_0.txt
%{_includedir}/mapbox


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 25 2019 Tom Hughes <tom@compton.nu> - 1.1.6-1
- Update to 1.1.6 upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Tom Hughes <tom@compton.nu> - 1.1.5-5
- Build using catch1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May  3 2017 Tom Hughes <tom@compton.nu> - 1.1.5-2
- Turn off -Werror and -march=native

* Sun Apr  9 2017 Tom Hughes <tom@compton.nu> - 1.1.5-1
- Initial build of 1.1.5
