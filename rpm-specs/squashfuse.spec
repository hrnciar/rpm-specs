Name:     squashfuse
Version:  0.1.102
Release:  5%{?dist}
Summary:  FUSE filesystem to mount squashfs archives

License:  BSD
URL:      https://github.com/vasi/squashfuse
Source0:  https://github.com/vasi/squashfuse/archive/%{version}.tar.gz

BuildRequires: autoconf, automake, fuse-devel, gcc, libattr-devel, libtool, libzstd-devel, lz4-devel, xz-devel, zlib-devel
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
Squashfuse lets you mount SquashFS archives in user-space. It supports almost
all features of the SquashFS format, yet is still fast and memory-efficient.
SquashFS is an efficiently compressed, read-only storage format. Support for it
has been built into the Linux kernel since 2009. It is very common on Live CDs
and embedded Linux distributions.


%package devel
Summary: Development files for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Libraries and header files for developing applications that use %{name}.


%package libs
Summary: Libraries for %{name}

%description libs
Libraries for running %{name} applications.


%prep
%autosetup


%build
./autogen.sh
%configure --disable-static --disable-demo
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -print -delete


%files
%license LICENSE
%{_bindir}/*
%{_mandir}/man1/*

%files devel
%{_includedir}/squashfs_fs.h
%{_includedir}/squashfuse.h
%{_libdir}/pkgconfig/squashfuse.pc
%{_libdir}/*.so

%files libs
%{_libdir}/*.so.*

%ldconfig_scriptlets libs

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.102-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.102-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.102-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.102-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 5 2018 Kyle Fazzari <kyrofa@ubuntu.com> - 0.1.102-1
- Update to 0.1.102, which also introduces -libs and -devel packages

* Mon Sep 25 2017 Kyle Fazzari <kyrofa@ubuntu.com> - 0.1.100-1
- Initial version of the package
