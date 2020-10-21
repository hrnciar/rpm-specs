%define __cmake_in_source_build 1
Name:           tflogger
Version:        0.1.1
Release:        12%{?dist}
Summary:        TensorFlow event logger

License:        ASL 2.0
URL:            https://github.com/shogun-toolbox/tflogger
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  catch-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  protobuf-devel

%description
This is a simple library that has been carved out of
TensorFlow's codebase for being able to generate the
required output format for TensorBoard.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} == %{version}-%{release}
Requires:       protobuf-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p 1
sed -i -e "s/Catch2::Catch/Catch2::Catch2/g" test/CMakeLists.txt
sed -i -e "/#include/s|<catch.hpp>|<catch2/catch.hpp>|" test/*.cc


%build
%{__mkdir_p} build-%{_target_platform}
pushd build-%{_target_platform}
%cmake3                     \
  -DBUILD_TESTS=ON          \
  -DLIB_INSTALL_DIR=%{_lib} \
  ..
%make_build
popd


%install
%make_install -C build-%{_target_platform}


%check
pushd build-%{_target_platform}
  %{_bindir}/ctest3 %{?_smp_mflags} -V
popd


%{?ldconfig_scriptlets}


%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}
%{_libdir}/lib%{name}.so


%changelog
* Thu Sep 24 2020 Adrian Reber <adrian@lisas.de> - 0.1.1-12
- Rebuilt for protobuf 3.13

* Tue Sep 22 2020 Jeff Law <law@redhat.com> - 0.1.1-11
- Use cmake_in_source_build to fix FTBFS due to recent cmake macro changes

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 0.1.1-8
- Rebuilt for protobuf 3.12

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Orion Poplawski <orion@nwra.com> - 0.1.1-6
- Rebuild for protobuf 3.11

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.1-3
- Rebuild for protobuf 3.6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 18 2018 Björn Esser <besser82@fedoraproject.org> - 0.1.1-1
- Initial import (rhbz#1579528)

* Thu May 17 2018 Björn Esser <besser82@fedoraproject.org> - 0.1.1-0.1
- Initial rpm release (rhbz#1579528)
