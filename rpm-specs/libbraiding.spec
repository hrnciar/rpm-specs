Name:           libbraiding
Version:        1.1
Release:        1%{?dist}
Summary:        Library for computations on braid groups

License:        GPLv2+
URL:            https://github.com/miguelmarco/libbraiding
Source0:        https://github.com/miguelmarco/libbraiding/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  libtool

%description
This library allows various computations on braid groups, such as normal
forms.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p0

# Upstream does not generate the configure script
autoreconf -fi .

%build
%configure --disable-static

# Work around libtool reordering -Wl,--as-needed after all the libraries.
sed -i 's|CC=.g..|& -Wl,--as-needed|' libtool

%make_build

%install
%make_install

# We do not want the libtool files
rm -f %{buildroot}%{_libdir}/*.la

%files
%license LICENSE
%doc README.md
%{_libdir}/%{name}.so.0
%{_libdir}/%{name}.so.0.*

%files devel
%doc CHANGELOG
%{_includedir}/braiding.h
%{_includedir}/cbraid*.h
%{_libdir}/%{name}.so

%changelog
* Sat Sep 12 2020 Jerry James <loganjerry@gmail.com> - 1.1-1
- Version 1.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 24 2018 Jerry James <loganjerry@gmail.com> - 1.0-1
- Initial RPM
