Name:           c++-gtk-utils
Version:        2.0.16
Release:        18%{?dist}
Summary:        A library for GTK+ programming with C++

License:        LGPLv2
URL:            http://cxx-gtk-utils.sourceforge.net/
Source0:        http://downloads.sourceforge.net/cxx-gtk-utils/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  glib2-devel

# bz 925145
BuildRequires:  autoconf, libtool

# X11 tests:
BuildRequires:  xorg-x11-server-Xvfb

%description
c++-gtk-utils is a lightweight library containing a number of classes and
functions for programming GTK+ programs using C++ in POSIX (Unix-like)
environments, where the user does not want to use a full-on wrapper such as
gtkmm or wxWidgets, or is concerned about exception safety or thread safety of
the wrapper and their documentation.

%package gtk2
Summary:        A library for GTK+ programming with C++ - GTK2 version
BuildRequires:  gtk2-devel

%description gtk2
c++-gtk-utils is a lightweight library containing a number of classes and
functions for programming GTK+ programs using C++ in POSIX (Unix-like)
environments, where the user does not want to use a full-on wrapper such as
gtkmm or wxWidgets, or is concerned about exception safety or thread safety of
the wrapper and their documentation.

This version is built against GTK2.

%package gtk3
Summary:        A library for GTK+ programming with C++ - GTK3 version
BuildRequires:  gtk3-devel

%description gtk3
c++-gtk-utils is a lightweight library containing a number of classes and
functions for programming GTK+ programs using C++ in POSIX (Unix-like)
environments, where the user does not want to use a full-on wrapper such as
gtkmm or wxWidgets, or is concerned about exception safety or thread safety of
the wrapper and their documentation.

This version is built against GTK3.

%package gtk2-devel
Summary:        Development files for the c++-gtk-utils library - GTK2 version
Requires:       %{name}-gtk2%{?_isa} = %{version}-%{release}

%description gtk2-devel
This package contains libraries and header files needed for development of
applications or toolkits which use c++-gtk-utils.

This version is built against GTK2.

%package gtk3-devel
Summary:        Development files for the c++-gtk-utils library - GTK3 version
Requires:       %{name}-gtk3%{?_isa} = %{version}-%{release}

%description gtk3-devel
This package contains libraries and header files needed for development of
applications or toolkits which use c++-gtk-utils.

This version is built against GTK3.

%package devel-doc
Summary:        Development documentation for the c++-gtk-utils library
BuildArch:      noarch

%description devel-doc
This package contains documentation files for development of applications or
toolkits which use c++-gtk-utils.

%prep
%setup -q -n %{name}-%{version} -c
mv %{name}-{,gtk2-}%{version}
cp -a %{name}-gtk{2,3}-%{version}

%build
pushd %{name}-gtk2-%{version}
# autoreconf to update config.guess and config.sub for aarch64 (bz 925145)
cp configure-gtk2.ac configure.ac
autoreconf --force --install
%configure --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
make %{?_smp_mflags} V=1
popd

pushd %{name}-gtk3-%{version}
# autoreconf to update config.guess and config.sub for aarch64 (bz 925145)
cp configure-gtk3.ac configure.ac
autoreconf --force --install
%configure --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
make %{?_smp_mflags} V=1
popd

%install
pushd %{name}-gtk2-%{version}
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la
popd

pushd %{name}-gtk3-%{version}
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la
popd

%check
# "make test" requires a Unicode LANG.
LANG=C.UTF-8
# make test requires an X session, so use Xvfb to provide one.
# Unconditionally non-fatal because of SELinux bug: https://bugzilla.redhat.com/843603
pushd %{name}-gtk2-%{version}
xvfb-run -a make test ||:
popd
pushd %{name}-gtk3-%{version}
xvfb-run -a make test ||:
popd

%ldconfig_scriptlets gtk2
%ldconfig_scriptlets gtk3


%files gtk2
%{_libdir}/libcxx-gtk-utils-2-2.0.so.0*
%dir %{_defaultdocdir}/%{name}
%dir %{_defaultdocdir}/%{name}/2.0
%{_defaultdocdir}/%{name}/2.0/BUGS
%{_defaultdocdir}/%{name}/2.0/COPYING 
%{_defaultdocdir}/%{name}/2.0/NEWS 
%{_defaultdocdir}/%{name}/2.0/README

%files gtk3
%{_libdir}/libcxx-gtk-utils-3-2.0.so.0*
%dir %{_defaultdocdir}/%{name}
%dir %{_defaultdocdir}/%{name}/2.0
%{_defaultdocdir}/%{name}/2.0/BUGS
%{_defaultdocdir}/%{name}/2.0/COPYING 
%{_defaultdocdir}/%{name}/2.0/NEWS 
%{_defaultdocdir}/%{name}/2.0/README

%files gtk2-devel
%{_libdir}/pkgconfig/%{name}-2-2.0.pc
%{_libdir}/libcxx-gtk-utils-2-2.0.so
%{_includedir}/%{name}-2-2.0

%files gtk3-devel
%{_libdir}/pkgconfig/%{name}-3-2.0.pc
%{_libdir}/libcxx-gtk-utils-3-2.0.so
%{_includedir}/%{name}-3-2.0

%files devel-doc
%dir %{_defaultdocdir}/%{name}
%dir %{_defaultdocdir}/%{name}/2.0
%{_defaultdocdir}/%{name}/2.0/COPYING
%{_defaultdocdir}/%{name}/2.0/PORTING-TO-2.0
%{_defaultdocdir}/%{name}/2.0/html

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0.16-15
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 2.0.16-14
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 2.0.16-7
- Fix FTBFS with current libtool

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 28 2013 Frederik Holden <frederik+fedora@frh.no> - 2.0.16-2
- Temporary fix for bz 925145 (aarch64 support) until new upstream release.
- Changed the build step so it doesn't unnecessarily ./configure twice.

* Wed Mar 13 2013 Frederik Holden <frederik+fedora@frh.no> - 2.0.16-1
- Updated to newest upstream release.

* Thu Feb 28 2013 Frederik Holden <frederik+fedora@frh.no> - 2.0.15-2
- Fixed an error in the package summary.

* Thu Feb 14 2013 Frederik Holden <frederik+fedora@frh.no> - 2.0.15-1
- Updated to newest upstream release.

* Tue Feb 12 2013 Frederik Holden <frederik+fedora@frh.no> - 2.0.14-3
- Built for both GTK2 and GTK3, with separate versions for each one.

* Tue Feb 12 2013 Frederik Holden <frederik+fedora@frh.no> - 2.0.14-2
- Made the build more verbose.

* Fri Feb 08 2013 Frederik Holden <frederik+fedora@frh.no> - 2.0.14-1
- Initial version of the package.
