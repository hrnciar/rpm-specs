%global gitrev 1b6103d

Name:           flexiport
Version:        2.0.0
Release:        18.20120701git1b6103d%{?dist}
Summary:        Flexible communications library

License:        LGPLv3
URL:            https://github.com/gbiggs/flexiport
# wget --content-disposition https://github.com/gbiggs/flexiport/tarball/1b6103da
Source0:        https://github.com/gbiggs/%{name}/tarball/1b6103da/gbiggs-%{name}-%{gitrev}.tar.gz
# Submitted upstream:
# https://github.com/gbiggs/flexiport/issues/2
Patch0:         flexiport-2.0.0-gcc47.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  python-sphinx

%description
Flexiport provides a consistent interface for communicating over a range of
data port types. Currently serial (including serial-over-USB), TCP and UDP
ports are supported. Logging is supported which allows communications sessions
to be played back at a later date without the original hardware present.

%package devel
Summary: Header files and libraries for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries and header files for %{name}

%prep
%setup -q -n gbiggs-%{name}-%{gitrev}
%patch0 -p0
# The "breathe" module is not available, so don't use it
sed -i 's/extensions/#extensions/' doc/conf.py.in
# Fix multilib installation directories
sed -i 's/\"lib\"/\"%{_lib}\"/' CMakeLists.txt

%build
%cmake -DBUILD_EXAMPLES=OFF  .
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}-2/html/{.doctrees,.buildinfo}

%ldconfig_scriptlets

%files
%doc COPYING COPYING.LESSER
%{_libdir}/*.so.*

%files devel
%{_docdir}/%{name}-2
%{_datadir}/%{name}-2
%{_includedir}/%{name}-2
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{name}


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-18.20120701git1b6103d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-17.20120701git1b6103d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-16.20120701git1b6103d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-15.20120701git1b6103d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-14.20120701git1b6103d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-13.20120701git1b6103d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-12.20120701git1b6103d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11.20120701git1b6103d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10.20120701git1b6103d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-9.20120701git1b6103d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0.0-8.20120701git1b6103d
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-7.20120701git1b6103d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-6.20120701git1b6103d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-5.20120701git1b6103d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-4.20120701git1b6103d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-3.20120701git1b6103d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 01 2012 Rich Mattes <richmattes@gmail.com> - 2.0.0-2.20120701git1b6103d
- Added missing BuildRequires 
- Use github's tag download for tarball
- Added explaination for sed calls
- Added gitrev to package version
- Added isa to devel package requirement of base package

* Sat Dec 31 2011 Rich Mattes <richmattes@gmail.com> - 2.0.0-1.20111231git
- Initial build
