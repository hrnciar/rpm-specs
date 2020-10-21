Summary:	GLib Ncurses Toolkit
Name:		libgnt
Version:	2.14.0
Release:	3%{?dist}
License:	GPLv2+
URL:		https://keep.imfreedom.org/libgnt/libgnt/
BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:	gobject-introspection
BuildRequires:	gtk-doc
BuildRequires:	glib2-devel
BuildRequires:	libxml2-devel
BuildRequires:	ncurses-devel
BuildRequires:	python3-devel
BuildRequires:	gnupg2
Source0:	https://dl.bintray.com/pidgin/releases/%{name}-%{version}.tar.xz
Source1:	https://dl.bintray.com/pidgin/releases/%{name}-%{version}.tar.xz.asc
# https://issues.imfreedom.org/issue/LIBGNT-10
Source2:	libgnt-maintainers-keyring.asc

%description
GNT is an ncurses toolkit for creating text-mode graphical user interfaces
in a fast and easy way. It is based on GLib and ncurses.

%package devel
Summary:	Developmentfiles for libgnt
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for libgnt.

%package doc
Summary:	Documentation for libgnt

%description doc
Documentation files for libgnt.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%doc README.md
%{_libdir}/libgnt.so.*
%{_libdir}/gnt

%files devel
%{_libdir}/libgnt.so
%{_libdir}/pkgconfig/gnt.pc
%{_includedir}/gnt

%files doc
%{_datadir}/gtk-doc

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.14.0-2
- Fixed according to the review

* Thu Jul 16 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 2.14.0-1
- Initial package
