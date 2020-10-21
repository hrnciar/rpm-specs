Name:           mingw-pkg-config
Version:        0.28
Release:        15%{?dist}
Summary:        A tool for determining compilation options

License:        GPLv2+
URL:            http://pkgconfig.freedesktop.org
Source0:        http://www.freedesktop.org/software/pkgconfig/releases/pkg-config-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95


%description
The pkgconfig tool determines compilation options. For each required
library, it reads the configuration file and outputs the necessary
compiler and linker flags.


# Mingw32
%package -n mingw32-pkg-config
Summary:        A tool for determining compilation options for the win32 target
Requires:       mingw32-filesystem >= 95

%description -n mingw32-pkg-config
The pkgconfig tool determines compilation options. For each required
library, it reads the configuration file and outputs the necessary
compiler and linker flags.

# Mingw64
%package -n mingw64-pkg-config
Summary:        A tool for determining compilation options for the win64 target
Requires:       mingw64-filesystem >= 95

%description -n mingw64-pkg-config
The pkgconfig tool determines compilation options. For each required
library, it reads the configuration file and outputs the necessary
compiler and linker flags.


%prep
%setup -q -n pkg-config-%{version}


%build
%global _configure ../configure

mkdir build_win32
pushd build_win32
    %configure \
        --disable-shared \
        --disable-host-tool \
        --program-prefix=%{mingw32_target}- \
        --with-pc-path=%{mingw32_libdir}/pkgconfig:%{mingw32_datadir}/pkgconfig

    make %{?_smp_mflags}
popd

mkdir build_win64
pushd build_win64
    %configure \
        --disable-shared \
        --disable-host-tool \
        --program-prefix=%{mingw64_target}- \
        --with-pc-path=%{mingw64_libdir}/pkgconfig:%{mingw64_datadir}/pkgconfig

    make %{?_smp_mflags}
popd


%install
make install -C build_win32 DESTDIR=$RPM_BUILD_ROOT
make install -C build_win64 DESTDIR=$RPM_BUILD_ROOT

# These files conflict with ordinary pkg-config.
rm -rf ${RPM_BUILD_ROOT}%{_datadir}/aclocal
rm -rf ${RPM_BUILD_ROOT}%{_datadir}/doc/pkg-config


%files -n mingw32-pkg-config
%doc AUTHORS README NEWS COPYING pkg-config-guide.html
%{_bindir}/%{mingw32_target}-pkg-config
%{_mandir}/man1/%{mingw32_target}-pkg-config.1*

%files -n mingw64-pkg-config
%doc AUTHORS README NEWS COPYING pkg-config-guide.html
%{_bindir}/%{mingw64_target}-pkg-config
%{_mandir}/man1/%{mingw64_target}-pkg-config.1*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Apr 13 2013 Kalev Lember <kalevlember@gmail.com> - 0.28-1
- Update to 0.28

* Sat Apr 13 2013 Kalev Lember <kalevlember@gmail.com> - 0.27.1-1
- Update to 0.27.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Sep 16 2012 Kalev Lember <kalevlember@gmail.com> - 0.27-1
- Update to 0.27
- Drop deps on popt, 0.27 no longer uses it

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 27 2012 Kalev Lember <kalevlember@gmail.com> - 0.26-4
- Use the configure macro

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.26-3
- Added support for win64

* Tue Jan 31 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.26-2
- Dropped the configure argument --with-installed-glib as it's not needed
  anymore as of pkg-config 0.26
- Fixed typo in RPM macros

* Tue Jan 31 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.26-1
- Initial package (based on the OpenSuSE mingw32-cross-pkg-config package)

