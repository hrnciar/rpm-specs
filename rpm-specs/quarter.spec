%global sover 20

Name:           quarter
Version:        1.1.0
Release:        1%{?dist}
Summary:        Lightweight glue library between Coin and Qt

License:        BSD
URL:            https://grey.colorado.edu/quarter/
Source0:        https://github.com/coin3d/%{name}/archive/Quarter-%{version}.tar.gz

Patch0:         quarter-cpack_fix.patch

BuildRequires:  cmake gcc gcc-c++ doxygen
BuildRequires:  mesa-libGL-devel
BuildRequires:  Coin4-devel
BuildRequires:  qt5-qtbase-devel
# Needed for Cmake UI Config
BuildRequires:  qt5-qttools-static
BuildRequires:  libspnav-devel

%description
Quarter is a light-weight glue library that provides seamless integration
between Systems in Motions's Coin high-level 3D visualization library and
Trolltech's Qt 2D user interface library.

Qt and Coin is a perfect match since they are both open source, widely portable
and easy to use. Quarter has evolved from Systems in Motion's own experiences
using Coin and Qt together in our applications.

The functionality in Quarter revolves around QuarterWidget, a subclass of
QGLWidget. This widget provides functionality for rendering of Coin scenegraphs
and translation of QEvents into SoEvents. Using this widget is as easy as using
any other QWidget.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.


%package doc
Summary:        Development documentation for %{name}
Requires:       %{name}-devel = %{version}-%{release}
BuildArch:      noarch

%description doc
%{summary}.


%prep
%autosetup -p1 -n %{name}-Quarter-%{version}


%build
mkdir build-%_target_cpu && cd build-%_target_cpu
%cmake -DQUARTER_BUILD_DOCUMENTATION=ON ../

%make_build


%install
cd build-%_target_cpu
%make_install


%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so.1*
%{_libdir}/*.so.%{sover}
%{_libdir}/qt5/plugins/designer/*

%files devel
%{_includedir}/Quarter/
%{_libdir}/*.so
%{_libdir}/cmake/Quarter-%{version}/
%{_libdir}/pkgconfig/Quarter.pc

%files doc
%{_docdir}/Quarter/


%changelog
* Sun Apr 19 2020 Richard Shaw <hobbes1069@gmail.com> - 1.1.0-1
- Update to 1.1.0.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Richard Shaw <hobbes1069@gmail.com> - 1.0.1-2
- Update per reviewer feedback.

* Tue Dec 17 2019 Richard Shaw <hobbes1069@gmail.com> - 1.0.1-1
- Initial packaging
