%global tilp_version 1.18
%global _udevdir %{_prefix}/lib/udev/rules.d

Name:           libticables2
Version:        1.3.5
Release:        9%{?dist}
Summary:        Texas Instruments link cables library

License:        GPLv2+
URL:            https://sourceforge.net/projects/tilp/
Source0:        http://sourceforge.net/projects/tilp/files/tilp2-linux/tilp2-%{tilp_version}/%{name}-%{version}.tar.bz2
# Udev rules taken from Arch AUR package.
Source1:        http://tc01.fedorapeople.org/tilp2/69-libticables.rules

# It seems the ppc64le patch is still needed, whoops.
Patch0:         ppc64le.patch

BuildRequires:  glib2-devel, pkgconfig, libusb1-devel, tfdocgen, gettext
BuildRequires:  autoconf, automake, libtool, gettext-devel

%package devel

Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package doc

Summary:        HTML documentation for %{name}
BuildArch:      noarch

%description
The ticables library is able to handle the different link cables
designed for Texas Instruments's graphing calculators (also called
handhelds) in a fairly transparent fashion. With this library, the
developer does not have to worry about the different link cables'
characteristics as well as the different platforms. The library
provides a complete API which is very easy to use and makes things
easier.

%description devel
Include files and libraries required for developing applications
that make use of libticables.

%description doc
HTML documentation for linking and developing applications
using libticables2.

%prep
%setup -q
sed -i 's/\r$//' docs/html/style.css
%patch0 -p1

# Invoke auto(re)conf.
autoreconf --force --install

%build
%configure --enable-libusb10 --disable-static
make %{?_smp_mflags}

%check
make -C tests check

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/libticables2.la
make -C docs install DESTDIR=%{buildroot}
rm %{buildroot}/%{_pkgdocdir}/COPYING
mkdir -p %{buildroot}%{_udevdir}
cp -a %SOURCE1 %{buildroot}%{_udevdir}/69-libticables.rules
%find_lang %{name}

%files -f %{name}.lang
%{_udevdir}/69-libticables.rules
%{_libdir}/libticables2.so.*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%doc %{_pkgdocdir}/AUTHORS
%doc %{_pkgdocdir}/ChangeLog
%license COPYING

%files doc
%doc %{_pkgdocdir}/html/
%license COPYING

%files devel
%dir %{_includedir}/tilp2
%{_includedir}/tilp2/export1.h
%{_includedir}/tilp2/stdints1.h
%{_includedir}/tilp2/ticables.h
%{_includedir}/tilp2/timeout.h
%{_libdir}/libticables2.so
%{_libdir}/pkgconfig/ticables2.pc

%post
/sbin/udevadm control --reload-rules
%{?ldconfig}

%ldconfig_postun

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 04 2016 Ben Rosser <rosser.bjr@gmail.com> - 1.3.5-1
- Update to latest upstream release.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 30 2015 Rafael dos Santos <rdossant@redhat.com> - 1.3.4-6
- Add PPC64le support

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 1.3.4-4
- Add AArch64 support

* Mon Apr 6 2015 'Ben Rosser' <rosser.bjr@gmail.com> 1.3.4-3
- Added a patch that adds error checking around libusb_init, preventing the tests from crashing under mock.

* Fri Mar 6 2015 'Ben Rosser' <rosser.bjr@gmail.com> 1.3.4-2
- Package now owns its documentation directory.
- Changed macros from define to global.
- The tilp2 include dir is now co-owned between this package and libticonv-devel.
- The doc subpackage now has a license.
- The test suite is now ran in the check section.

* Fri Feb 27 2015 'Ben Rosser' <rosser.bjr@gmail.com> 1.3.4-1
- Release bump from 0 to 1.
- Added HTML documentation subpackage.
- Fixed localization to use gettext and find_lang macro.
- Cleaned up commands for installing udev rule.

* Sat Apr 20 2013 'Ben Rosser' <rosser.bjr@gmail.com> 1.3.4-0
- Updated to latest upstream version of tilp

* Wed Sep 12 2012 'Ben Rosser' <rosser.bjr@gmail.com> 1.3.3-2
- Placed udev rules in correct directory (/lib, not /etc)

* Wed Jul 11 2012 'Ben Rosser' <rosser.bjr@gmail.com> 1.3.3-1
- Added full documentation, built by tfdocgen

* Thu Jul 5 2012 'Ben Rosser' <rosser.bjr@gmail.com> 1.3.3-0
- Updated package to 1.3.3, vastly improved specfile
- Added devel subpackage for all devel files
- Udev rules are now hosted online by me

* Sat Jul 30 2011 'Ben Rosser' <rosser.bjr@gmail.com> 1.3.2-0
- Initial version of the package

