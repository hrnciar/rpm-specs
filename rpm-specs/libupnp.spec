Version: 1.8.4
Summary: Universal Plug and Play (UPnP) SDK
Name: libupnp
Release: 4%{?dist}
License: BSD
URL: https://sourceforge.net/projects/pupnp
Source: https://downloads.sourceforge.net/pupnp/%{name}-%{version}.tar.bz2
Patch0: libupnp-1.8.4-nobump.patch
Patch1: 96.patch

BuildRequires: gcc autoconf automake


%description
The Universal Plug and Play (UPnP) SDK for Linux provides 
support for building UPnP-compliant control points, devices, 
and bridges on Linux.

%package devel
Summary: Include files needed for development with libupnp
Requires: libupnp%{?_isa} = %{version}-%{release}

%description devel
The libupnp-devel package contains the files necessary for development with
the UPnP SDK libraries.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
autoreconf

%build
%configure \
  --enable-static=no \
  --enable-ipv6

# remove rpath from libtool
sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install

%{__rm} %{buildroot}%{_libdir}/{libixml.la,libupnp.la}

%ldconfig_scriptlets

%files
%license COPYING
%doc THANKS
%{_libdir}/libixml.so.10*
%{_libdir}/libupnp.so.10*

%files devel
%{_includedir}/upnp/
%{_libdir}/libixml.so
%{_libdir}/libupnp.so
%{_libdir}/pkgconfig/libupnp.pc

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Nicolas Chauvet <kwizart@gmail.com> - 1.8.4-1
- Update to 1.8.4
- Revert the ABI bump since it's the same as 1.8.3
- Add back patch for largefile support

* Thu Dec 13 2018 Dennis Gilmore <dennis@ausil.us> - 1.8.3-4
- pull in patch from upstream so that samples will build on 32 bit arches with
- largefile support, enables gerbera to run on armv7hl and i686

* Fri Jul 20 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.8.3-3
- Add missng cc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 13 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.8.3-1
- Update to 1.8.3
- Drop libthreadutil

* Fri Apr 13 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.6.25-1
- Update to 1.6.25
- Spec file clean-up
- Avoid rpath

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 07 2017 Michael Cronenworth <mike@cchtml.com> - 1.6.21-1
- libupnp 1.6.21

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul 18 2016 Adam Jackson <ajax@redhat.com> - 1.6.20-1
- libupnp 1.6.20
- Don't write to the filesystem on unhandled POST requests

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 09 2013 Adam Jackson <ajax@redhat.com> 1.6.19-1
- libupnp 1.6.19
- Build with --enable-ipv6 (#917210)

* Sun Oct 27 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.6.18-4
- Adapt to possibly unversioned doc dirs.
- Include LICENSE and THANKS in main package.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jan 29 2013 Adam Jackson <ajax@redhat.com> 1.6.18-1
- libupnp 1.6.18 (#905577)

* Tue Oct 16 2012 Adam Jackson <ajax@redhat.com> 1.6.17-1
- libupnp 1.6.17

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jul 30 2011 Matěj Cepl <mcepl@redhat.com> - 1.6.13-2
- Rebuilt against new libraries.

* Tue May 31 2011 Adam Jackson <ajax@redhat.com> 1.6.13-1
- libupnp 1.6.13

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu May 01 2008 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.6.6-1
- Update to version 1.6.6

* Sun Feb 03 2008 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.6.5-1
- Update to version 1.6.5

* Sun Jan 27 2008 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.6.4-1
- Update to version 1.6.4

* Fri Jan 04 2008 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.6.3-3
- No more building static library

* Sun Dec 30 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.6.3-2
- Spec file cleanup

* Sun Dec 30 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.6.3-1
- Update to version 1.6.3

* Thu Dec 13 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.6.2-1
- Update to version 1.6.2

* Sun Nov 18 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.6.1-1
- Update to version 1.6.1

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.6.0-2
- Rebuild for selinux ppc32 issue.

* Wed Jun 13 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.6.0-1
- Update to version 1.6.0

* Tue May 01 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.4.6-1
- Update to version 1.4.6

* Sat Apr 21 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.4.4-1
- Update to version 1.4.4

* Tue Mar 06 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.4.3-1
- Update to version 1.4.3

* Fri Feb 02 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.4.2-1
- Update to version 1.4.2

* Wed Jul 05 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.4.1-1
- Update to version 1.4.1

* Fri Jun 23 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.4.0-3
- modified patch for x86_64 arch

* Fri Jun 23 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.4.0-2
- Add a patch for x86_64 arch

* Sun Jun 11 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.4.0-1
- Update to 1.4.0

* Sun Mar 05 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.3.1-1
- Update to 1.3.1

* Tue Feb 14 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.2.1a-6
- Rebuild for FC5

* Fri Feb 10 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 1.2.1a-5
- Rebuild for FC5

* Mon Jan  9 2006 Eric Tanguy 1.2.1a-4
- Include libupnp.so symlink in package to take care of non versioning of libupnp.so.1.2.1

* Sun Jan  8 2006 Paul Howarth 1.2.1a-3
- Disable stripping of object code for sane debuginfo generation
- Edit makefiles to hnnor RPM optflags
- Install libraries in %%{_libdir} rather than hardcoded /usr/lib
- Fix libupnp.so symlink
- Own directory %%{_includedir}/upnp
- Fix permissions in -devel package

* Fri Jan 06 2006 Eric Tanguy 1.2.1a-2
- Use 'install -p' to preserve timestamps
- Devel now require full version-release of main package

* Thu Dec 22 2005 Eric Tanguy 1.2.1a-1
- Modify spec file from 
http://rpm.pbone.net/index.php3/stat/4/idpl/2378737/com/libupnp-1.2.1a_DSM320-3.i386.rpm.html
