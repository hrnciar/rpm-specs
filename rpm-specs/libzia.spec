Name:		libzia
Version:	4.20
Release:	1%{?dist}
Summary:	Platform abstraction layer for the tucnak package
License:	GPLv2
URL:		http://tucnak.nagano.cz/
Source:		http://tucnak.nagano.cz/%{name}-%{version}.tar.gz
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	glib2-devel
BuildRequires:	gtk2-devel
BuildRequires:	SDL-devel
BuildRequires:	libpng-devel
BuildRequires:	libftdi-devel
# This is to fulfill Fedora requirement - it marks the interface with
# version number 0. Upstream uses --release versioning in libtool.
# They do not support linking between different versions of tucnak and
# libzia, i.e. tucnak-4.18 needs to be linked to libzia-4.18.
Patch0:		libzia-4.18-soname-fix.patch

%description
Platform abstraction layer for the tucnak package.

%package devel
Summary:	Development files for libzia
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	SDL-devel
Requires:	gtk2-devel
Requires:	libftdi-devel

%description devel
Development files for libzia

%prep
%setup -q
%patch0 -p1 -b .soname-fix

%build
autoreconf -fi
%configure --disable-static
%make_build

%install
%make_install

# drop .la
rm -f %{buildroot}%{_libdir}/libzia.la

# drop unneeded files
rm -f %{buildroot}%{_datadir}/libzia/doc/*
rm -f %{buildroot}%{_datadir}/libzia/settings
rm -f %{buildroot}%{_prefix}/lib/libzia/*
rmdir %{buildroot}%{_datadir}/libzia/doc/ %{buildroot}%{_datadir}/libzia %{buildroot}%{_prefix}/lib/libzia

%files
%license COPYING
%doc AUTHORS
%{_libdir}/libzia-%{version}.so.0*

%files devel
%{_bindir}/zia-config
%{_includedir}/libzia
%{_libdir}/libzia.so

%changelog
* Wed Feb  5 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.20-1
- New version

* Tue Jan 28 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.19-1
- New version
- Added missing requirements
- Dropped configure-fix, fsf-address-fix patch (both upstreamed)

* Wed Jan  8 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.18-3
- More fixes according to review

* Tue Jan  7 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.18-2
- Fixed according to review

* Fri Jan  3 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.18-1
- Initial version
