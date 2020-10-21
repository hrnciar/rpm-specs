%bcond_without lz4
%bcond_without uuid

Name:           erofs-utils
Version:        1.1
Release:        2%{?dist}

Summary:        Utilities for working with EROFS
License:        GPLv2+
URL:            https://git.kernel.org/pub/scm/linux/kernel/git/xiang/erofs-utils.git

Source0:        %{url}/snapshot/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libtool
%if %{with lz4}
BuildRequires:  lz4-devel
%endif
%if %{with uuid}
BuildRequires:  libuuid-devel
%endif

%description
EROFS stands for Enhanced Read-Only File System.  Different from other
read-only file systems, it is designed for flexibility, scalability, and
simplicity for high performance.

The %{name} package includes mkfs.erofs to create EROFS images.


%prep
%autosetup
autoreconf -fi

%build
%configure \
    %{?with_lz4:--enable-lz4} %{!?with_lz4:--disable-lz4} \
    %{?with_uuid:--with-uuid} %{!?with_uuid:--without-uuid}
%make_build

%install
%make_install


%files
%{_bindir}/mkfs.erofs
%{_mandir}/man1/mkfs.erofs.1*
%doc AUTHORS ChangeLog README
%license COPYING


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 13 2020 David Michael <fedora.dm0@gmail.com> - 1.1-1
- Update to the 1.1 release.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 David Michael <fedora.dm0@gmail.com> - 1.0-1
- Initial package.
