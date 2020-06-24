%?mingw_package_header

Name:           mingw-SDL2_ttf
Version:        2.0.15
Release:        4%{?dist}

%global  pkg_summary  MinGW Windows port of the TrueType font handling library for SDL2
Summary: %{pkg_summary}

License:        zlib
URL:            https://www.libSDL.org/projects/SDL_ttf/
Source0:        %{URL}release/SDL2_ttf-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-freetype
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-SDL2

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-freetype
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-SDL2


%global  pkg_description  Simple DirectMedia Layer (SDL2) is a cross-platform multimedia library \
designed to provide fast access to the graphics frame buffer and audio device. \
This package contains a library that allows you to use TrueType fonts \
to render text in SDL2 applications.

%description
%{pkg_description}


# Win32
%package -n mingw32-SDL2_ttf
Summary: %{pkg_summary}

%description -n mingw32-SDL2_ttf
%{pkg_description}


# Win64
%package -n mingw64-SDL2_ttf
Summary: %{pkg_summary}

%description -n mingw64-SDL2_ttf
%{pkg_description}


%?mingw_debug_package


%prep
%setup -q -n SDL2_ttf-%{version}


%build
%mingw_configure \
    --disable-static \
    --disable-dependency-tracking \

%mingw_make %{?smp_mflags}


%install
%mingw_make DESTDIR=%{buildroot} install


# Drop all .la files
find %{buildroot} -name "*.la" -delete

# Convert CRLF line endings to LF
sed -i 's/\r$//' README.txt CHANGES.txt COPYING.txt

# Win32
%files -n mingw32-SDL2_ttf
%doc CHANGES.txt README.txt
%license COPYING.txt
%{mingw32_bindir}/SDL2_ttf.dll
%{mingw32_libdir}/libSDL2_ttf.dll.a
%{mingw32_libdir}/pkgconfig/SDL2_ttf.pc
%{mingw32_includedir}/SDL2

# Win64
%files -n mingw64-SDL2_ttf
%doc CHANGES.txt README.txt
%license COPYING.txt
%{mingw64_bindir}/SDL2_ttf.dll
%{mingw64_libdir}/libSDL2_ttf.dll.a
%{mingw64_libdir}/pkgconfig/SDL2_ttf.pc
%{mingw64_includedir}/SDL2


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 07 2019 Artur Iwicki <fedora@svgames.pl> - 2.0.15-2
- Fix wrong License: tag (was "LGPLv2+", should be "zlib")
- Fix COPYING.txt being marked as %%doc instead of %%license
- Fix package description containing a leading newline

* Wed Jul 03 2019 Artur Iwicki <fedora@svgames.pl> - 2.0.15-1
- Initial packaging
