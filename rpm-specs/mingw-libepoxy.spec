%{?mingw_package_header}

Name:           mingw-libepoxy
Version:        1.5.4
Release:        2%{?dist}
Summary:        MinGW Windows libepoxy library

License:        MIT
URL:            https://github.com/anholt/libepoxy
Source0:        https://github.com/anholt/libepoxy/releases/download/%{version}/libepoxy-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  python3

%description
Epoxy is a library for handling OpenGL function pointer management.

This package contains the MinGW Windows cross compiled libepoxy library.


%package -n mingw32-libepoxy
Summary:        MinGW Windows libepoxy library

%description -n mingw32-libepoxy
Epoxy is a library for handling OpenGL function pointer management.

This package contains the MinGW Windows cross compiled libepoxy library.


%package -n mingw64-libepoxy
Summary:        MinGW Windows libepoxy library

%description -n mingw64-libepoxy
Epoxy is a library for handling OpenGL function pointer management.

This package contains the MinGW Windows cross compiled libepoxy library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n libepoxy-%{version}


%build
%mingw_meson
%mingw_ninja


%install
%mingw_ninja_install


%files -n mingw32-libepoxy
%license COPYING
%{mingw32_bindir}/libepoxy-0.dll
%{mingw32_libdir}/libepoxy.dll.a
%{mingw32_libdir}/pkgconfig/epoxy.pc
%{mingw32_includedir}/epoxy/

%files -n mingw64-libepoxy
%license COPYING
%{mingw64_bindir}/libepoxy-0.dll
%{mingw64_libdir}/libepoxy.dll.a
%{mingw64_libdir}/pkgconfig/epoxy.pc
%{mingw64_includedir}/epoxy/

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 26 2019 Sandro Mani <manisandro@gmail.com> - 1.5.4-1
- Update to 1.5.4

* Wed Aug 28 2019 Sandro Mani <manisandro@gmail.com> - 1.5.3-1
- Update to 1.5.3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Christophe Fergeau <cfergeau@redhat.com> - 1.5.2-1
- Update to 1.5.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.4.3-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 15 2017 Kalev Lember <klember@redhat.com> - 1.4.3-1
- Update to 1.4.3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Kalev Lember <klember@redhat.com> - 1.4.1-1
- Update to 1.4.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 07 2016 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.3.1-3
- Add BuildRequires: python to fix FTBFS

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 05 2015 Kalev Lember <klember@redhat.com> - 1.3.1-1
- Update to 1.3.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 24 2015 Kalev Lember <kalevlember@gmail.com> - 1.2-2
- Package review fixes (#1205194)
- Don't explicitly BR mingw{32,64}-binutils
- Fix the license tag

* Tue Mar 24 2015 Kalev Lember <kalevlember@gmail.com> - 1.2-1
- Initial Fedora packaging
