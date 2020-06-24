Name:           wimlib
Version:        1.13.2
Release:        1%{?dist}
Summary:        Open source Windows Imaging (WIM) library

# Library is dual licensed, utilities are GPLv3+, some internal headers are CC0
License:        (GPLv3+ or LGPLv3+) and GPLv3+ and CC0
URL:            https://wimlib.net/
Source0:        %{url}/downloads/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libntfs-3g)
BuildRequires:  pkgconfig(libxml-2.0)

%description
wimlib is a C library for creating, modifying, extracting, and mounting files in
the Windows Imaging Format (WIM files). wimlib and its command-line frontend
'wimlib-imagex' provide a free and cross-platform alternative to Microsoft's
WIMGAPI, ImageX, and DISM.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%package utils
Summary:        Tools for creating, modifying, extracting, and mounting WIM files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description utils
This package provides tools for creating, modifying, extracting, and mounting
files in the Windows Imaging Format (WIM files).


%prep
%autosetup


%build
%configure \
    --disable-silent-rules \
    --disable-static
# Remove Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build


%install
%make_install
find $RPM_BUILD_ROOT -name "*.la" -delete


%files
%doc NEWS README
%license COPYING COPYING.CC0 COPYING.GPLv3 COPYING.LGPLv3
%{_libdir}/*.so.15*


%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc


%files utils
%{_bindir}/*
%{_mandir}/man1/*.1.*


%changelog
* Mon May 25 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.13.2-1
- Update to 1.13.2

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 26 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.13.1-1
- Initial RPM release
