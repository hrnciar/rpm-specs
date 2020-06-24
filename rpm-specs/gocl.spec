%global api_version 0.2

Name:           gocl
Version:        0.2.0
Release:        15%{?dist}
Summary:        GLib/GObject based library for OpenCL

License:        LGPLv3
URL:            https://github.com/elima/gocl/
Source0:        https://github.com/elima/gocl/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         gocl-0.2.0-format-security.patch

BuildRequires:  automake
BuildRequires:  glibc-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  ocl-icd-devel opencl-headers


%description
Gocl is a GLib/GObject based library that aims at simplifying the
use of OpenCL in GNOME software. It is intended to be a lightweight
wrapper that adapts OpenCL programming patterns and boilerplate, and
expose a simpler API that is known and comfortable to GNOME
developers. Examples of such adaptations are the integration with
GLib’s main loop, exposing non-blocking APIs, GError based error
reporting and full gobject-introspection support. It will also be
including convenient API to simplify code for the most common use
patterns.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1


%build
./autogen.sh
%configure --disable-static --enable-introspection=yes --enable-tests=yes --enable-gtk-doc
make %{?_smp_mflags}


%install
%make_install

# NOTE: We intentionally don't ship *.la files
find %{buildroot} -type f -name '*.la' | xargs rm -f -- || :


%ldconfig_scriptlets


%files
%doc COPYING
%{_libdir}/libgocl-%{api_version}.so.*
%{_libdir}/girepository-1.0/


%files devel
%doc examples/Makefile.am examples/*.c examples/*.cl examples/js/*.js
%{_libdir}/libgocl-%{api_version}.so
%{_libdir}/pkgconfig/%{name}-%{api_version}.pc
%{_datadir}/gir-1.0/
%{_datadir}/gtk-doc/
%{_includedir}/gocl-%{api_version}/


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.2.0-4
- Rebuilt for gobject-introspection 1.41.4

* Mon Jun 23 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.2.0-3
- Fix FTBFS with -Werror=format-security (#1037097, #1106699)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 11 2014 Fabian Deutsch <fabiand@fedoraproject.org> - 0.2.0-1
- Update to upstream 0.2.0

* Tue Oct 01 2013 Björn Esser <bjoern.esser@gmail.com> - 0.1.6-2
- rebuilt for ocl-icd-2.0.4-1.git20131001.4ee231e

* Tue Oct 01 2013 Fabian Deutsch <fabiand@fedoraproject.org> - 0.1.6-1
- Update to upstream 0.1.6
- Removed merged build patch

* Wed Sep 11 2013 Fabian Deutsch <fabiand@fedoraproject.org> - 0.1.4-3
- Move all examples to devel package
- Remove trash line from build patch

* Wed Sep 11 2013 Fabian Deutsch <fabiand@fedoraproject.org> - 0.1.4-2
- Own directories
- Package examples
- Use global instead of define

* Sun Aug 18 2013 Fabian Deutsch <fabiand@fedoraproject.org> - 0.1.4-1
- Initial package
