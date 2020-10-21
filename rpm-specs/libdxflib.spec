Name:           libdxflib
Version:        3.17.0
Release:        11%{?dist}
Summary:        A C++ library for reading and writing DXF files

License:        GPLv2+
URL:            http://www.ribbonsoft.com/en/90-dxflib
Source0:        https://qcad.org/archives/dxflib/dxflib-%{version}-src.tar.gz

# https://github.com/qcad/qcad/pull/15
Patch0:         dxflib-Use-std-istream.patch

BuildRequires:  gcc-c++
BuildRequires:  qt4-devel

%description
dxflib is an open source C++ library mainly for parsing DXF files.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
dxflib is an open source C++ library mainly for parsing DXF files.

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -qn dxflib-%{version}-src
# Build as a shared library
sed -i 's/CONFIG += staticlib/CONFIG += shared/' dxflib.pro

%patch0 -p4


%build
# https://github.com/qcad/qcad/pull/16
%{qmake_qt4} \
  VERSION=%{version} \
  CONFIG-=qt

%make_build


%install
install -d -m 0755 %{buildroot}%{_libdir}
cp -pr %{name}.so* %{buildroot}%{_libdir}

install -d -m 0755 %{buildroot}%{_includedir}/dxflib
cp -pr src/*.h %{buildroot}%{_includedir}/dxflib

# Generate pkgconfig file
install -d -m 0755 %{buildroot}%{_libdir}/pkgconfig
cat << 'EOF' > %{buildroot}%{_libdir}/pkgconfig/dxflib.pc
prefix=%{_prefix}
exec_prefix=%{_exec_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: dxflib
Description: A C++ library for reading and writing DXF files
Version: %{version}
Libs: -L${libdir} -ldxflib
Cflags: -I${includedir}/dxflib
EOF


%ldconfig_scriptlets

%files
%license gpl-2.0greater.txt dxflib_commercial_license.txt
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/dxflib.pc


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.17.0-6
- fix scriptlets, better Qt dep, use %%qmake_qt4

* Tue Feb 20 2018 Samuel Rakitničan <samuel.rakitnican@gmail.com>
- Use ldconfig_scriptlets macro

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 02 2017 Samuel Rakitničan <samuel.rakitnican@gmail.com> - 3.17.0-2
- Remove unicode trademark character from description
- Use macro for make
- Pass the option to qmake to disable linking against Qt

* Wed May 31 2017 Samuel Rakitničan <samuel.rakitnican@gmail.com> - 3.17.0-1
- Initial build
