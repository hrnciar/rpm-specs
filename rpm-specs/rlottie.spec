%global commit0 a718c7e2dfd7d292324ca50d596b02b786299252
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20191224

Name: rlottie
Version: 0
Release: 7.%{date}git%{shortcommit0}%{?dist}

# Main source: LGPLv2+
# rapidjson (base) - MIT
# rapidjson (msinttypes) - BSD
# freetype rasterizer - FTL
# vector (vinterpolator) - MPLv1.1
License: LGPLv2+ and MIT and FTL and BSD and MPLv1.1
Summary: Platform independent standalone library that plays Lottie Animation

URL: https://github.com/Samsung/%{name}
Source0: %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: gtest-devel
BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: gcc

%description
rlottie is a platform independent standalone C++ library for rendering
vector based animations and art in realtime.

Lottie loads and renders animations and vectors exported in the bodymovin
JSON format. Bodymovin JSON can be created and exported from After Effects
with bodymovin, Sketch with Lottie Sketch Export, and from Haiku.

For the first time, designers can create and ship beautiful animations
without an engineer painstakingly recreating it by hand. Since the animation
is backed by JSON they are extremely small in size but can be large in
complexity.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n %{name}-%{commit0}
sed -e "s/, 'werror=true'//" -e "s/, 'optimization=s'//" -i meson.build

%build
%meson \
    -Dtest=true \
    -Dthread=true \
    -Dexample=false \
    -Dcache=false \
    -Dlog=false \
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

%changelog
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
