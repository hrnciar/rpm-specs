%global gittag rel_2_10_35

Name:           asdcplib
Version:        2.10.35
Release:        1%{?dist}
Summary:        AS-DCP file access libraries
License:        BSD
URL:            http://www.cinecert.com/asdcplib/

Source0:        https://github.com/cinecert/%{name}/archive/%{gittag}/%{name}-%{version}.tar.gz
Source1:        %{name}.pc

ExcludeArch:    %{ix86} %{arm}

BuildRequires:  cmake
BuildRequires:  gcc-c++
# https://fedoraproject.org/wiki/Licensing:FAQ#What.27s_the_deal_with_the_OpenSSL_license.3F
BuildRequires:  openssl-devel
BuildRequires:  xerces-c-devel

%description
Open source implementation of SMPTE and the MXF Interop “Sound & Picture Track
File” format. It was originally developed with support from DCI. Development
is currently supported by CineCert and other d-cinema manufacturers.

It supports reading and writing MXF files containing sound (PCM), picture (JPEG
2000 or MPEG-2) and timed-text (XML) essence. plain text and cipher text are
both supported using OpenSSL for cryptographic support.

%package        tools
Summary:        AS-DCP file access libraries tools

%description    tools
Open source implementation of SMPTE and the MXF Interop “Sound & Picture Track
File” format. It was originally developed with support from DCI. Development
is currently supported by CineCert and other d-cinema manufacturers.

It supports reading and writing MXF files containing sound (PCM), picture (JPEG
2000 or MPEG-2) and timed-text (XML) essence. plain text and cipher text are
both supported using OpenSSL for cryptographic support.

This package contains tools and testing programs for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{gittag}
sed -i -e 's/DESTINATION lib/DESTINATION %{_lib}/g' src/CMakeLists.txt

# rpmlint fixes
find . -name "*.h" -exec chmod 644 {} \;
find . -name "*.cpp" -exec chmod 644 {} \;
chmod 644 README.md

%build
mkdir build
cd build
%cmake \
    -DCMAKE_SKIP_RPATH=True \
    ..
%make_build

%install
cd build
%make_install

install -p -D -m 644 %{SOURCE1} %{buildroot}%{_libdir}/pkgconfig/%{name}.pc
sed -i \
    -e 's|PREFIX|%{_prefix}|g' \
    -e 's|LIBDIR|%{_libdir}|g' \
    -e 's|INCLUDEDIR|%{_includedir}|g' \
    -e 's|VERSION|%{version}|g' \
    %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

find %{buildroot} -name '*.la' -delete
rm -fr  %{buildroot}%{_prefix}/targets

%ldconfig_scriptlets

%files
%license COPYING
%doc README.md
%{_libdir}/libas02.so.2
%{_libdir}/libas02.so.2.*
%{_libdir}/libasdcp.so.2
%{_libdir}/libasdcp.so.2.*
%{_libdir}/libkumu.so.2
%{_libdir}/libkumu.so.2.*

%files devel
%{_includedir}/*
%{_libdir}/libas02.so
%{_libdir}/libasdcp.so
%{_libdir}/libkumu.so
%{_libdir}/pkgconfig/%{name}.pc

%files tools
%{_bindir}/as-02-info
%{_bindir}/as-02-unwrap
%{_bindir}/as-02-wrap
%{_bindir}/asdcp-info
%{_bindir}/asdcp-test
%{_bindir}/asdcp-unwrap
%{_bindir}/asdcp-util
%{_bindir}/asdcp-wrap
%{_bindir}/blackwave
%{_bindir}/j2c-test
%{_bindir}/klvwalk
%{_bindir}/kmfilegen
%{_bindir}/kmrandgen
%{_bindir}/kmuuidgen
%{_bindir}/wavesplit

%changelog
* Thu Mar 26 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.10.35-1
- Update to 2.10.35

* Sat Feb 08 2020 Simone Caronni <negativo17@gmail.com> - 2.10.34-1
- Update to 2.10.34.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Simone Caronni <negativo17@gmail.com> - 2.10.32-4
- Fix dependency issue after renaming asdcplib-libs.

* Sat Jun 08 2019 Simone Caronni <negativo17@gmail.com> - 2.10.32-3
- Review fixes.

* Sat May 25 2019 Simone Caronni <negativo17@gmail.com> - 2.10.32-2
- Fix RPATH on binaries.

* Tue Feb 26 2019 Simone Caronni <negativo17@gmail.com> - 2.10.32-1
- Update to 2.10.32.

* Fri Oct 19 2018 Simone Caronni <negativo17@gmail.com> - 2.10.31-1
- Update to 2.10.31.

* Mon Oct 01 2018 Simone Caronni <negativo17@gmail.com> - 2.9.30-1
- Update to 2.9.30.

* Mon Feb 27 2017 Simone Caronni <negativo17@gmail.com> - 2.7.19-3
- Adjust build requirements.
- Adjust Source URL.

* Wed Dec 21 2016 Simone Caronni <negativo17@gmail.com> - 2.7.19-2
- Add pkg-config file, as required by VLC.

* Wed Dec 21 2016 Simone Caronni <negativo17@gmail.com> - 2.7.19-1
- First build.