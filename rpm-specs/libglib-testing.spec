Name:           libglib-testing
Version:        0.1.0
Release:        2%{?dist}
Summary:        GLib-based test library and harness

License:        LGPLv2+
URL:            https://gitlab.gnome.org/pwithnall/libglib-testing
Source0:        https://gitlab.gnome.org/pwithnall/libglib-testing/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(gio-2.0)

%description
libglib-testing is a test library providing test harnesses and mock classes
which complement the classes provided by GLib. It is intended to be used by
any project which uses GLib and which wants to write internal unit tests.

%package devel
Summary:        Development files for %{name}
License:        LGPLv2+
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the pkg-config file and development headers
for %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%{_libdir}/libglib-testing-0.so.0*

%files devel
%{_datadir}/gtk-doc/
%{_includedir}/glib-testing-0/
%{_libdir}/libglib-testing-0.so
%{_libdir}/pkgconfig/glib-testing-0.pc

%changelog
* Thu Aug 27 2020 Bastien Nocera <bnocera@redhat.com> - 0.1.0-2
+ libglib-testing-0.1.0-2
- Fix review comments

* Thu Jul 23 2020 Bastien Nocera <bnocera@redhat.com> - 0.1.0-1
+ libglib-testing-0.1.0-1
- First package
