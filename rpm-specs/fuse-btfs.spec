Summary:	FUSE filesystem Bittorrent
Name:		fuse-btfs
Version:	2.22
Release:	2%{?dist}

License:	GPLv3
URL:		https://github.com/johang/btfs
Source0:	https://github.com/johang/btfs/archive/v%{version}/btfs-%{version}.tar.gz

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig(fuse)
BuildRequires:	pkgconfig(libtorrent-rasterbar)
BuildRequires:	pkgconfig(libcurl)

%description
With BTFS, you can mount any .torrent file or magnet link and then use it as
any read-only directory in your file tree. The contents of the files will be
downloaded on-demand as they are read by applications. Tools like ls, cat and
cp works as expected. Applications like vlc and mplayer can also work without
changes.

%prep
%autosetup -n btfs-%{version}

%build
autoreconf -i
%configure
%make_build

%install
%{make_install}

%files
%{_bindir}/*
%{_mandir}/man1/*

%doc README.md
%license LICENSE


%changelog
* Thu Sep 3 2020 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.22-2
- Spec changes based on review

* Sat Aug 15 2020 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.22-1
- Initial version of the package
