%global gitcommit_full f5a28c74fba7a99736fe49d3a5243eca29517ae9
%global gitcommit %(c=%{gitcommit_full}; echo ${c:0:7})
%global date 20181010

Name:           libcorrect
Version:        0
Release:        4.%{date}git%{gitcommit}%{?dist}
Summary:        C library for Convolutional codes and Reed-Solomon
License:        BSD
URL:            https://github.com/quiet/libcorrect
Source0:        %{url}/tarball/%{gitcommit_full}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build

%description
libcorrect is a library for Forward Error Correction. By using libcorrect,
extra redundancy can be encoded into a packet of data and then be sent
across a lossy channel. When the packet is received, it can be decoded to
recover the original, pre-encoded data.

%package devel
Summary:        Development files for libcorrect
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
libcorrect is a library for Forward Error Correction. By using libcorrect,
extra redundancy can be encoded into a packet of data and then be sent
across a lossy channel. When the packet is received, it can be decoded to
recover the original, pre-encoded data.

This subpackage contains libraries and header files for developing
applications that want to make use of libcorrect.

%prep
%autosetup -p1 -n quiet-%{name}-%{gitcommit}
echo "set_property(TARGET correct PROPERTY SOVERSION 0.0.0)" >> CMakeLists.txt
sed -e "s|DESTINATION lib|DESTINATION %{_lib}|" \
    -e '/CMAKE_C_FLAGS/d' \
    -e 's|}" HAVE_SSE)|}" HAVE_SSE_dd)|' \
    -e "/(fec_shim_static/d" \
    -e "s| fec_shim_static||" \
    -e "/(correct_static/d" \
    -e "s| correct_static||" -i CMakeLists.txt


%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release
%ninja_build -C %{_target_platform}

%install
%ninja_install -C %{_target_platform}

%files
%license LICENSE
%doc README.md
%{_libdir}/libcorrect.so.0.0.0

%files devel
%{_includedir}/correct*.h
%{_libdir}/libcorrect.so

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.20181010gitf5a28c7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-3.20181010gitf5a28c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-2.20181010gitf5a28c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 24 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 0-1.20181010gitf5a28c7
- Initial release for Fedora
