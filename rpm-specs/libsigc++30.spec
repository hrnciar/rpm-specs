# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           libsigc++30
Version:        3.0.3
Release:        1%{?dist}
Summary:        Typesafe signal framework for C++

License:        LGPLv2+
URL:            https://libsigcplusplus.github.io/libsigcplusplus/
Source0:        https://download.gnome.org/sources/libsigc++/%{release_version}/libsigc++-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  m4
BuildRequires:  perl-interpreter
BuildRequires:  perl(Getopt::Long)

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
%configure
%make_build


%install
%make_install
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'


%files
%license COPYING
%doc AUTHORS README.md NEWS
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/sigc++-3.0/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%files doc
%doc %{_datadir}/doc/libsigc++-3.0/
%doc %{_datadir}/devhelp/


%changelog
* Fri Mar 27 2020 Kalev Lember <klember@redhat.com> - 3.0.3-1
- Update to 3.0.3

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Kalev Lember <klember@redhat.com> - 3.0.2-1
- Update to 3.0.2

* Thu Sep 05 2019 Kalev Lember <klember@redhat.com> - 3.0.0-1
- Initial Fedora packaging, based on libsigc++20
