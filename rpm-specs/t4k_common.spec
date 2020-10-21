Name: t4k_common
Version: 0.1.1
Release: 26%{?dist}
URL: https://github.com/tux4kids/t4kcommon/
Summary: Library for Tux4Kids applications
License: GPLv3+
Source0: https://github.com/tux4kids/t4kcommon/archive/debian/0.1.1-1.1/t4k_common-0.1.1.tar.gz
Patch0: t4k_common-0.1.1.patch
BuildRequires:  gcc
BuildRequires: SDL-devel SDL_mixer-devel SDL_image-devel
BuildRequires: SDL_Pango-devel SDL_net-devel librsvg2-devel cairo-devel
BuildRequires: libpng-devel libxml2-devel doxygen
Provides: bundled(liblinebreak)

%package devel
Summary: Development files for the Tux4Kids library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description
library of code shared by TuxMath, TuxType, and
possibly other Tux4Kids apps in the future.

%description devel
library of code shared by TuxMath, TuxType, and
possibly other Tux4Kids apps in the future.

These are the development files.

%prep
%setup -q

%patch0 -p1

%build
export CPPFLAGS="$CPPFLAGS -fcommon"
%configure
make %{?_smp_mflags}
doxygen
rm -f doxygen/html/installdox

%install
INSTALL='install -p' make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_includedir}/t4k_scandir.h
chmod 755 $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so

%ldconfig_scriptlets

%files
%license COPYING
%doc README
%{_libdir}/lib%{name}.so.*
%{_datadir}/%{name}/

%files devel
%doc doxygen/html/
%{_libdir}/lib%{name}.so
%{_includedir}/t4k*.h
%{_libdir}/pkgconfig/t4k_common.pc

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.1.1-25
- Fix FTBFS.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.1.1-23
- New upstream location.

* Wed Aug 14 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.1.1-22
- Apply patch from BZ 1665008.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild


* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Jon Ciesla <limburgher@gmail.com> - 0.1.1-7
- Fix libpng15 fix, BZ 825462.

* Mon Jan 23 2012 Jon Ciesla <limburgher@gmail.com> - 0.1.1-6
- libpng15 fix.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.1.1-4
- Rebuild for new libpng

* Thu Nov 10 2011 Jon Ciesla <limb@jcomserv.net> - 0.1.1-3
- Rebuild for libpng 1.5.

* Mon Jul 18 2011 Jon Ciesla <limb@jcomserv.net> - 0.1.1-2
- Swapped doc,defatttr lines for devel.
- Removed installdox script.
- Noted liblinebreak bundling exception.
- Added _isa for -devel main package requires.

* Mon Jul 18 2011 Jon Ciesla <limb@jcomserv.net> - 0.1.1-1
- Updated to newest upstream.
- Dropped .pc from base package.
- Moved doxygen docs to -devel.
- Changed solib permission handling.

* Mon Mar 14 2011 Jon Ciesla <limb@jcomserv.net> - 0.0.3-3
- Fixed multiple review issues from comment #3.

* Wed Feb 23 2011 Jon Ciesla <limb@jcomserv.net> - 0.0.3-2
- Fixed directory ownership and macro per informal review comments.

* Wed Dec 29 2010 Jon Ciesla <limb@jcomserv.net> - 0.0.3-1
- initial rpm
