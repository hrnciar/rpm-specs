%{?mingw_package_header}

%global mingw32_py3_incdir %(mingw32-python3 -c 'import distutils.sysconfig; print(distutils.sysconfig.get_python_inc())')
%global mingw64_py3_incdir %(mingw64-python3 -c 'import distutils.sysconfig; print(distutils.sysconfig.get_python_inc())')

%global pkgname pillow

Name:           mingw-python-%{pkgname}
Version:        7.1.2
Release:        2%{?dist}
Summary:        MinGW Windows Python %{pkgname} library

BuildArch:      noarch
# License: see http://www.pythonware.com/products/pil/license.htm
License:        MIT
URL:            http://python-pillow.github.io/
Source0:        https://github.com/python-pillow/Pillow/archive/%{version}/Pillow-%{version}.tar.gz

# MinGW build fixes
Patch0:         pillow_mingw.patch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-setuptools
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw32-freetype
BuildRequires:  mingw32-lcms2
BuildRequires:  mingw32-libimagequant
BuildRequires:  mingw32-libjpeg
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw32-libwebp
BuildRequires:  mingw32-openjpeg2
BuildRequires:  mingw32-tk
BuildRequires:  mingw32-zlib

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-setuptools
BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw64-freetype
BuildRequires:  mingw64-lcms2
BuildRequires:  mingw64-libimagequant
BuildRequires:  mingw64-libjpeg
BuildRequires:  mingw64-libtiff
BuildRequires:  mingw64-libwebp
BuildRequires:  mingw64-openjpeg2
BuildRequires:  mingw64-tk
BuildRequires:  mingw64-zlib


%description
MinGW Windows Python %{pkgname} library.


%package -n mingw32-python3-%{pkgname}
Summary:       MinGW Windows Python2 %{pkgname} library

%description -n mingw32-python3-%{pkgname}
MinGW Windows Python2 %{pkgname} library.


%package -n mingw64-python3-%{pkgname}
Summary:       MinGW Windows Python2 %{pkgname} library

%description -n mingw64-python3-%{pkgname}
MinGW Windows Python2 %{pkgname} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n Pillow-%{version}


%build
PKG_CONFIG=mingw32-pkg-config %{mingw32_python3} setup.py build_ext --disable-platform-guessing
mv build build_mingw32
PKG_CONFIG=mingw64-pkg-config %{mingw64_python3} setup.py build_ext --disable-platform-guessing
mv build build_mingw64


%install
ln -s build_mingw32 build
%{mingw32_python3} setup.py install -O1 --skip-build --root=%{buildroot}
rm build

ln -s build_mingw64 build
%{mingw64_python3} setup.py install -O1 --skip-build  --root=%{buildroot}
rm build

install -d %{buildroot}/%{mingw32_py3_incdir}/Imaging
install -m 644 src/libImaging/*.h %{buildroot}/%{mingw32_py3_incdir}/Imaging

install -d %{buildroot}/%{mingw64_py3_incdir}/Imaging
install -m 644 src/libImaging/*.h %{buildroot}/%{mingw64_py3_incdir}/Imaging

# Remove sample scripts
rm -rf %{buildroot}%{mingw32_bindir}
rm -rf %{buildroot}%{mingw64_bindir}


%files -n mingw32-python3-%{pkgname}
%license docs/COPYING
%{mingw32_python3_sitearch}/*
%{mingw32_py3_incdir}/Imaging/

%files -n mingw64-python3-%{pkgname}
%license docs/COPYING
%{mingw64_python3_sitearch}/*
%{mingw64_py3_incdir}/Imaging/


%changelog
* Sun May 31 2020 Sandro Mani <manisandro@gmail.com> - 7.1.2-2
- Rebuild (python-3.9)

* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 7.1.2-1
- Update to 7.1.2

* Tue Sep 05 2017 Sandro Mani <manisandro@gmail.com> - 4.2.1-1
- Initial package
