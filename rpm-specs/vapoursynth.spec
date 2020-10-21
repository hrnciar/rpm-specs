#global _with_tests 1
#global _with_ffmpeg 1
#global _with_ImageMagick 1

Name:       vapoursynth
Version:    48
Release:    10%{?dist}
Summary:    Video processing framework with simplicity in mind
License:    LGPLv2
URL:        http://www.vapoursynth.com

Source0:    https://github.com/%{name}/%{name}/archive/R%{version}/%{name}-R%{version}.tar.gz
Patch0:     %{name}-version-info.patch
Patch1:     https://github.com/vapoursynth/vapoursynth/commit/a53ed4dda74d61d4cb56842dc0c6e6e7c3870e11.patch#/%{name}-python38.patch
Patch2:     %{name}-gcc11.patch

ExclusiveArch:  %{ix86} x86_64

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  nasm
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(tesseract)
BuildRequires:  pkgconfig(zimg)
BuildRequires:  python3
BuildRequires:  python3-Cython
BuildRequires:  python3-setuptools

%{?_with_tests:
BuildRequires:  %{name}-devel
BuildRequires:  python3dist(pytest)
}

%{?_with_ImageMagick:
BuildRequires:  pkgconfig(Magick++) >= 7.0
}

%{?_with_ffmpeg:
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
}

%description
VapourSynth is an application for video manipulation. Or a plugin. Or a library.
It’s hard to tell because it has a core library written in C++ and a Python
module to allow video scripts to be created.


%package        libs
Summary:        VapourSynth's core library with a C++ API
Obsoletes:      lib%{name} < %{version}-%{release}
Provides:       lib%{name} == %{version}-%{release}

%description    libs
VapourSynth's core library with a C++ API.


%package -n     python3-%{name}
Summary:        Python interface for VapourSynth

%description -n python3-%{name}
Python interface for VapourSynth/VSSCript.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.


%package        tools
Summary:        Extra tools for VapourSynth

%description    tools
This package contains the vspipe tool for interfacing with VapourSynth.


%package        plugins
Summary:        VapourSynth plugins
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    plugins
VapourSynth plugins.


%prep
%autosetup -p1 -n %{name}-R%{version}


%build
autoreconf -vif
%configure \
    --disable-static \
    --enable-x86-asm \
    --enable-core \
    --enable-vsscript \
    --enable-vspipe \
    --enable-python-module \
    --enable-eedi3 \
    --%{?_with_ImageMagick:enable}%{!?_with_ImageMagick:disable}-imwri \
    --enable-miscfilters \
    --enable-morpho \
    --enable-ocr \
    --enable-removegrain \
    --%{?_with_ffmpeg:enable}%{!?_with_ffmpeg:disable}-subtext \
    --enable-vinverse \
    --enable-vivtc \

%make_build


%install
%py3_install
%make_install
find %{buildroot} -type f -name "*.la" -delete

# Let RPM pick up docs in the files section
rm -fr %{buildroot}%{_docdir}/%{name}

%ldconfig_scriptlets libs
%ldconfig_scriptlets -n python3-%{name}


%{?_with_tests:
%check
%{python3} -m pytest -v
}


%files libs
%doc ChangeLog
%license COPYING.LGPLv2.1 ofl.txt
%dir %{_libdir}/%{name}
%{_libdir}/lib%{name}.so.*
%{_libdir}/lib%{name}-script.so.*

%files -n python3-%{name}
%{python3_sitearch}/%{name}.so
%{python3_sitearch}/VapourSynth-*.egg-info

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}-script.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}-script.pc

%files tools
%{_bindir}/vspipe

%files plugins
%{_libdir}/%{name}/lib*.so


%changelog
* Sat Oct 17 2020 Jeff Law <law@redhat.com> - 48-10
- Fix missing #include for gcc-11

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 48-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 48-8
- Rebuilt for Python 3.9

* Sat Mar 07 2020 Simone Caronni <negativo17@gmail.com> - 48-7
- Fix broken dependency.

* Sat Feb 29 2020 Simone Caronni <negativo17@gmail.com> - 48-6
- Make it exclusive for i686/x86_64.
- Fix build on RHEL/CentOS 8.

* Tue Feb 25 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 48-5
- Add tests
- Cosmetic spec file improvements

* Thu Feb 20 2020 Simone Caronni <negativo17@gmail.com> - 48-4
- More review fixes.
- Use upstream patch for Python 3.8.

* Fri Feb 07 2020 Simone Caronni <negativo17@gmail.com> - 48-3
- Review fixes.

* Sun Jan 26 2020 Simone Caronni <negativo17@gmail.com> - 48-2
- Move script library into main library package.
- Fix build with Python 3.8.

* Thu Jan 16 2020 Simone Caronni <negativo17@gmail.com> - 48-1
- First build.
