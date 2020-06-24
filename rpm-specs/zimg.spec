Name:           zimg
Version:        2.9.3
Release:        2%{?dist}
Summary:        Scaling, color space conversion, and dithering library
License:        WTFPL
URL:            https://github.com/sekrit-twc/zimg

Source0:        %{url}/archive/release-%{version}/%{name}-%{version}.tar.gz

# Included in 2.9.4:
Patch:          https://github.com/sekrit-twc/zimg/commit/9ae36d7d5f7420eaacd9644451933512fa13d716.patch#/zimg-ftbfs.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool

%description
The "z" library implements the commonly required image processing basics of
scaling, color space conversion, and depth conversion. A simple API enables
conversion between any supported formats to operate with minimal knowledge from
the programmer. All library routines were designed from the ground-up with
correctness, flexibility, and thread-safety as first priorities. Allocation,
buffering, and I/O are cleanly separated from processing, allowing the
programmer to adapt "z" to many scenarios.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n zimg-release-%{version}

%build
autoreconf -vif
%configure \
    --disable-static \
    --enable-testapp
%make_build V=1

%install
%make_install
install -m 755 -p -D testapp %{buildroot}%{_bindir}/testapp

find %{buildroot} -name '*.la' -delete

# Pick up docs in the files section
rm -fr %{buildroot}%{_docdir}/%{name}

%ldconfig_scriptlets

%files
%license COPYING
%doc README.md ChangeLog
%{_libdir}/lib%{name}.so.2.0.0
%{_libdir}/lib%{name}.so.2

%files devel
%{_bindir}/testapp
%{_includedir}/*
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Mon Apr 20 2020 Simone Caronni <negativo17@gmail.com> - 2.9.3-2
- Fix FTBFS in Rawhide.

* Wed Mar 04 2020 Simone Caronni <negativo17@gmail.com> - 2.9.3-1
- Update to 2.9.3.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 Leigh Scott <leigh123linux@googlemail.com> - 2.9.2-1
- Update to 2.9.2 release

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 08 2019 Simone Caronni <negativo17@gmail.com> - 2.8-3
- Review fixes.

* Sat May 25 2019 Simone Caronni <negativo17@gmail.com> - 2.8-2
- rpmlint fixes.

* Thu Mar 28 2019 Simone Caronni <negativo17@gmail.com> - 2.8-1
- First build.
