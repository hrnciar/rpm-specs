Name: rlottie
Version: 0.2
Release: 2%{?dist}

# Main source: MIT
# rapidjson (base) - MIT
# rapidjson (msinttypes) - BSD
# freetype rasterizer - FTL
# vector (vinterpolator) - MPLv1.1
License: MIT and FTL and BSD and MPLv1.1
Summary: Platform independent standalone library that plays Lottie Animation

URL: https://github.com/Samsung/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0: %{name}-gcc11.patch

BuildRequires: gtest-devel
BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: cmake
BuildRequires: gcc

%description
rlottie is a platform independent standalone c++ library for rendering
vector based animations and art in realtime.

Lottie loads and renders animations and vectors exported in the bodymovin
JSON format. Bodymovin JSON can be created and exported from After Effects
with bodymovin, Sketch with Lottie Sketch Export, and from Haiku.

For the first time, designers can create and ship beautiful animations
without an engineer painstakingly recreating it by hand. Since the animation
is backed by JSON they are extremely small in size but can be large in
complexity!

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -p1
sed -e "s/, 'optimization=s'//" -i meson.build

%build
%meson \
    -Dwerror=false \
    -Dtest=true \
    -Dthread=true \
    -Dexample=false \
    -Dcache=false \
    -Dlog=false \
    -Dcmake=true \
    -Dmodule=false
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc AUTHORS README.md
%license COPYING licenses/*
%{_libdir}/lib%{name}.so.0*

%files devel
%{_includedir}/%{name}*.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/

%changelog
* Fri Oct 16 2020 Jeff Law <law@redhat.com> - 0.2-2
- Fix missing #include for gcc-11

* Wed Oct 14 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.2-1
- Updated to version 0.2.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-9.20191224gita718c7e
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-8.20191224gita718c7e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 13 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0-7.20191224gita718c7e
- Enabled aarch64 again.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-6.20191224gita718c7e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0-5.20191224gita718c7e
- Updated to latest snapshot.

* Fri Aug 09 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0-4.20190805git33d4fca
- Updated to latest snapshot.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-3.20190707git0a43020
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0-2.20190707git0a43020
- Disabled internal cache (currently broken).

* Mon Jul 08 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.20190707git0a43020
- Initial SPEC release.
