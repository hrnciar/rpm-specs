Name:           votca-xtp
Version:        1.6.1
%global         uversion %{version}
%global         sover 6
Release:        1%{?dist}
Summary:        VOTCA excitation and charge properties module
License:        ASL 2.0
URL:            http://www.votca.org
Source0:        https://github.com/votca/xtp/archive/v%{uversion}.tar.gz#/%{name}-%{uversion}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake3
BuildRequires:  eigen3-devel
BuildRequires:  libxc-devel
BuildRequires:  hdf5-devel
BuildRequires:  fftw-devel
BuildRequires:  pkgconfig
BuildRequires:  boost-devel
BuildRequires:  votca-csg-devel = %{version}
BuildRequires:  votca-csg = %{version}

Requires:   %{name}-common = %{version}-%{release}
Requires:   %{name}-libs%{_isa} = %{version}-%{release}

%description
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package intended to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains the excitation and charge properties module of VOTCA
package.

%package libs
Summary:        Libraries for VOTCA excitation and charge properties module

%description libs
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package intended to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains libraries for the excitation and charge properties
module of VOTCA package.

%package devel
Summary:        Development headers and libraries for VOTCA XTP
Requires:       %{name}-libs%{_isa} = %{version}-%{release}
Requires:       votca-csg-devel%{_isa} = %{version}

%description devel
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package intended to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains development headers and libraries for the excitation and
charge properties module.

%package common
Summary:        Architecture independent data files for VOTCA XTP
BuildArch:      noarch

%description common
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package intended to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains architecture independent data files for VOTCA XTP.

%prep
%setup -qn xtp-%{uversion}

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake3} .. -DCMAKE_BUILD_TYPE=Release -DENABLE_TESTING=ON
%make_build

%install
%make_install -C%{_target_platform}

%check
make -C %{_target_platform} test CTEST_OUTPUT_ON_FAILURE=1 %{?testargs}

%ldconfig_scriptlets libs

%files
%doc CHANGELOG.md NOTICE README.md
%{_bindir}/xtp_*

%files common
%license LICENSE.md
%{_datadir}/votca/xtp

%files libs
%license LICENSE.md
%{_libdir}/libvotca_xtp.so.%{sover}

%files devel
%{_includedir}/votca/xtp/
%{_libdir}/libvotca_xtp.so

%changelog
* Sun Jun 21 2020 Christoph Junghans <junghans@votca.org> - 1.6.1-1
- Version bump to v1.6.1

* Sat May 30 2020 Jonathan Wakely <jwakely@redhat.com> - 1.6-2
- Rebuilt for Boost 1.73

* Sat Apr 18 2020 Christoph Junghans <junghans@votca.org> - 1.6-1
- Version bump to v1.6 (bug #1825475)
- Drop 381.patch - merged upstream

* Mon Feb 10 2020 Christoph Junghans <junghans@votca.org> - 1.6~rc2-1
- Version bump to 1.6~rc2
- Drop 345.patch & 347.patch - merged upstream
- Add 381.patch to fix 32-bit build

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-0.3rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Christoph Junghans <junghans@votca.org> - 1.6-0.2rc1
- Added upstream 347.patch to fix 32bit builds
- Added upstream 345.patch to fix failing tests

* Thu Dec 05 2019 Christoph Junghans <junghans@votca.org> - 1.6-0.1rc1
- Version bump to 1.6_rc1 (bug #1779897)

* Fri Nov 22 2019 Christoph Junghans <junghans@votca.org> - 1.5.1-1
- Version bump to 1.5.1 (bug #1774855)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Orion Poplawski <orion@nwra.com> - 1.5-1.2
- Rebuild for hdf5 1.10.5

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Feb 02 2019 Christoph Junghans <junghans@votca.org> - 1.5-1
- Version bump to v1.5 (bug #1667602)
- drop 55.patch, merged upstream
- Fix FTBFS (bug #1606654)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Christoph Junghans <junghans@votca.org> - 1.4.1-1.1
- Rebuilt for Boost 1.66
- Add 55.patch

* Sun Sep 03 2017 Christoph Junghans <junghans@votca.org> - 1.4.1-1
- Update to 1.4.1 (#1487881)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Björn Esser <besser82@fedoraproject.org> - 1.4-2.2
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue Feb 07 2017 Kalev Lember <klember@redhat.com> - 1.4-2
- Rebuilt for Boost 1.63

* Sun Oct 30 2016 Christoph Junghans <junghans@votca.org> - 1.4-1
- Update to 1.4

* Mon Oct 03 2016 Christoph Junghans <junghans@votca.org> - 1.4-0.2rc1
- Changes from review (bug #1380540)

* Wed Sep 28 2016 Christoph Junghans <junghans@votca.org> - 1.4-0.1rc1
- Imported 1.4_rc1
