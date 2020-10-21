Name: fsverity-utils
Version: 1.1
Release: 3%{?dist}
Summary: fsverity utilities

License: BSD
URL:     https://git.kernel.org/pub/scm/linux/kernel/git/ebiggers/fsverity-utils.git
Source0: https://git.kernel.org/pub/scm/linux/kernel/git/ebiggers/fsverity-utils.git/snapshot/fsverity-utils-1.1.tar.gz

BuildRequires: gcc make
BuildRequires: kernel-headers glibc-headers
BuildRequires: openssl-devel

%description
This is fsverity, a userspace utility for fs-verity.
fs-verity is a Linux kernel feature that does transparent on-demand
integrity/authenticity verification of the contents of read-only files,
using a hidden Merkle tree (hash tree) associated with the file.
The mechanism is similar to dm-verity, but implemented at the file level
rather than at the block device level. The fsverity utility allows you
to set up fs-verity protected files.

%package devel
Summary:          Development package for fsverity-utils
Group:            Development/System
Requires:         %{name} = %{version}-%{release}
%description devel
Development package for fsverity-utils. This package includes the
libfsverity header and library files.

%prep
%autosetup %{name}-%{version}

%build
# Install into /usr/bin
make CFLAGS="%{optflags} -g" %{_smp_mflags} USE_SHARED_LIB=1

%install
%make_install PREFIX=/usr LIBDIR=%{_libdir}  CFLAGS="%{optflags} -g" USE_SHARED_LIB=1

%files
%doc README.md
%license COPYING
%{_bindir}/fsverity
%{_libdir}/*.so.0


%files devel
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 15 2020 Colin Walters <walters@verbum.org> - 1.1-2
- Move .so to -devel, hardcode soname

* Mon Jun 15 2020 Jes Sorensen <Jes.Sorensen@gmail.com> - 1.1-1
- Update to version 1.1, split into fsverity-utils and fsverity-utils-devel

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Colin Walters <walters@verbum.org> - 1.0-1
- Initial version
