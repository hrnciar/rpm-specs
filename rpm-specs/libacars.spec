%global optflags        %{optflags} -flto=auto
%global build_ldflags   %{build_ldflags} -flto

Name:           libacars
Version:        1.3.1
Release:        2%{?dist}
Summary:        A library for decoding various ACARS message payloads
License:        MIT
URL:            https://github.com/szpajder/libacars
Source0:        https://github.com/szpajder/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(zlib)
BuildRequires:  ninja-build

%description
libacars is a library for decoding various ACARS message payloads.

%package devel
Summary:        Development files for libacars
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
libacars is a library for decoding various ACARS message payloads.

This subpackage contains libraries and header files for developing
applications that want to make use of libacars.

%package -n acars-examples
Summary:        Example applications for libacars

%description -n acars-examples
Example applications for for libacars:

 * decode_arinc.c - decodes ARINC-622 messages supplied at the
   command line or from a file.
 * adsc_get_position - illustrates how to extract position-related
   fields from decoded ADS-C message.
 * cpdlc_get_position - illustrates how to extract position-related
   fields from CPDLC position reports.
 * media_advisory - decodes Media Advisory messages (ACARS label SA
   reports)

%prep
%autosetup
mkdir -p %{_target_platform}
sed -i -e "/acars_static/d" src/libacars/CMakeLists.txt

%build
pushd %{_target_platform}
    %cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_AR=/usr/bin/gcc-ar \
    -DCMAKE_RANLIB=/usr/bin/gcc-ranlib \
    -DCMAKE_NM=/usr/bin/gcc-nm \
    -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
    -DCMAKE_SHARED_LINKER_FLAGS="" \
    ..
popd
%ninja_build -C %{_target_platform}

%install
%ninja_install -C %{_target_platform}
rm -rf %{buildroot}/%{_datadir}/doc

%files
%doc CHANGELOG.md README.md
%license LICENSE.md
%{_libdir}/%{name}.so.1

%files devel
%doc doc/API_REFERENCE.md doc/API_REFERENCE.md
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n acars-examples
%{_bindir}/adsc_get_position
%{_bindir}/cpdlc_get_position
%{_bindir}/decode_acars_apps
%{_bindir}/media_advisory

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 24 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 1.3.1-1
- Initial release for Fedora
