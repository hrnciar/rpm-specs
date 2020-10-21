# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           libsigc++30
Version:        3.0.4
Release:        1%{?dist}
Summary:        Typesafe signal framework for C++

License:        LGPLv2+
URL:            https://github.com/libsigcplusplus/libsigcplusplus
Source0:        https://download.gnome.org/sources/libsigc++/%{release_version}/libsigc++-%{version}.tar.xz

BuildRequires:  docbook-style-xsl
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libxslt
BuildRequires:  m4
BuildRequires:  meson
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl-interpreter

%description
libsigc++ implements a typesafe callback system for standard C++. It
allows you to define signals and to connect those signals to any
callback function, either global or a member function, regardless of
whether it is static or virtual.

libsigc++ is used by gtkmm to wrap the GTK+ signal system. It does not
depend on GTK+ or gtkmm.


%package        devel
Summary:        Development tools for the typesafe signal framework for C++
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains the static libraries and header files
needed for development with %{name}.


%package        doc
Summary:        Documentation for %{name}, includes full API docs
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
This package contains the full API documentation for %{name}.


%prep
%setup -q -n libsigc++-%{version}


%build
%meson -Dbuild-documentation=true
%meson_build


%install
%meson_install


%files
%license COPYING
%doc AUTHORS README.md NEWS
%{_libdir}/libsigc-3.0.so.0*

%files devel
%{_includedir}/*
%{_libdir}/sigc++-3.0/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libsigc-3.0.so

%files doc
%doc %{_datadir}/doc/libsigc++-3.0/
%doc %{_datadir}/devhelp/


%changelog
* Mon Sep 28 2020 Kalev Lember <klember@redhat.com> - 3.0.4-1
- Update to 3.0.4
- Switch to meson build system
- Update upstream URL
- Tighten soname globs

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Mar 27 2020 Kalev Lember <klember@redhat.com> - 3.0.3-1
- Update to 3.0.3

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Kalev Lember <klember@redhat.com> - 3.0.2-1
- Update to 3.0.2

* Thu Sep 05 2019 Kalev Lember <klember@redhat.com> - 3.0.0-1
- Initial Fedora packaging, based on libsigc++20
